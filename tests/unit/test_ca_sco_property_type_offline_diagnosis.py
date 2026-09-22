from __future__ import annotations

import csv
import importlib.util
import io
import json
import struct
import sys
import zlib
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
LEGACY_EXECUTION_SCHEMA_PATH = (
    ROOT / "schemas/common/property_type_semantic_verification_execution.schema.json"
)
EXECUTION_SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_semantic_verification_execution.v1_1.schema.json"
)
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_property_type_offline_diagnosis_runner",
        RUNNER_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RUNNER = _load_runner()


def _synthetic_fields(property_type: str = "IN03") -> list[str]:
    values = [f"SYNTHETIC_{index}" for index in range(25)]
    values[0] = "SYNTHETIC_ID"
    values[1] = property_type
    return values


def _csv_record(fields: list[str], *, quoting: int = csv.QUOTE_MINIMAL) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\r\n", quoting=quoting)
    writer.writerow(fields)
    return output.getvalue().encode("utf-8")


def _member_prefix_from_raw(member_name: str, raw: bytes) -> bytes:
    compressor = zlib.compressobj(level=6, wbits=-15)
    compressed = compressor.compress(raw) + compressor.flush()
    filename = member_name.encode("utf-8")
    local_header = struct.pack(
        "<4s5H3I2H",
        b"PK\x03\x04",
        20,
        0x0800,
        8,
        0,
        0,
        0,
        0,
        0,
        len(filename),
        0,
    )
    body = local_header + filename + compressed
    assert len(body) <= RUNNER.RANGE_RESPONSE_BYTES
    return body + b"\x00" * (RUNNER.RANGE_RESPONSE_BYTES - len(body))


def _header_record() -> bytes:
    return _csv_record(list(RUNNER.CANONICAL_HEADER))


def test_projector_matches_stdlib_csv_on_privacy_safe_synthetic_matrix() -> None:
    cases: list[tuple[list[str], int]] = []

    base = _synthetic_fields()
    cases.append((base, csv.QUOTE_MINIMAL))

    first_field_commas = _synthetic_fields()
    first_field_commas[0] = "SYNTHETIC,ID,WITH,COMMAS"
    cases.append((first_field_commas, csv.QUOTE_MINIMAL))

    first_field_quotes = _synthetic_fields()
    first_field_quotes[0] = 'SYNTHETIC "ID"'
    cases.append((first_field_quotes, csv.QUOTE_MINIMAL))

    unrelated_embedded_newline = _synthetic_fields()
    unrelated_embedded_newline[7] = "SYNTHETIC LINE 1\nSYNTHETIC LINE 2"
    cases.append((unrelated_embedded_newline, csv.QUOTE_MINIMAL))

    later_commas_and_quotes = _synthetic_fields()
    later_commas_and_quotes[18] = 'SYNTHETIC "STREET", UNIT 2'
    cases.append((later_commas_and_quotes, csv.QUOTE_MINIMAL))

    unrelated_embedded_crlf = _synthetic_fields()
    unrelated_embedded_crlf[24] = "SYNTHETIC A\r\nSYNTHETIC B"
    cases.append((unrelated_embedded_crlf, csv.QUOTE_MINIMAL))

    quote_all = _synthetic_fields("IN01")
    cases.append((quote_all, csv.QUOTE_ALL))

    for fields, quoting in cases:
        record = _csv_record(fields, quoting=quoting)
        stdlib_rows = list(
            csv.reader(
                io.StringIO(record.decode("utf-8"), newline=""),
                strict=True,
            )
        )
        assert len(stdlib_rows) == 1

        projected, column_count = RUNNER._project_property_type(record)
        assert projected == stdlib_rows[0][RUNNER.PROPERTY_TYPE_INDEX]
        assert projected == fields[RUNNER.PROPERTY_TYPE_INDEX]
        assert column_count == len(RUNNER.CANONICAL_HEADER) == 25


def test_shape_rule_is_strict_but_remediation_does_not_relax_it() -> None:
    assert RUNNER.PROPERTY_TYPE_RE.fullmatch("IN03") is not None
    assert RUNNER.PROPERTY_TYPE_RE.fullmatch("AC01") is not None
    assert RUNNER.PROPERTY_TYPE_RE.fullmatch("ZZZZ") is not None

    for synthetic_variant in (" IN03", "IN03 ", "in03", "IN3", "IN003"):
        assert RUNNER.PROPERTY_TYPE_RE.fullmatch(synthetic_variant) is None


def test_remediation_distinguishes_shape_from_utf8_encoding() -> None:
    member = RUNNER.CANONICAL_MEMBERS[0]

    shape_rows = [_csv_record(_synthetic_fields(" IN03"))]
    shape_rows.extend(_csv_record(_synthetic_fields("IN03")) for _ in range(3))
    shape_body = _member_prefix_from_raw(
        member.name,
        _header_record() + b"".join(shape_rows),
    )
    with pytest.raises(RUNNER.RunnerStop) as shape_exc:
        RUNNER._process_member(member, shape_body)
    assert shape_exc.value.reason == "PROPERTY_TYPE_FORMAT_UNEXPECTED"

    invalid_utf8_fields = [b"SYNTHETIC_ID", b"\xff"] + [b"SYNTHETIC"] * 23
    invalid_utf8_row = b",".join(invalid_utf8_fields) + b"\r\n"
    encoding_rows = [invalid_utf8_row]
    encoding_rows.extend(_csv_record(_synthetic_fields("IN03")) for _ in range(3))
    encoding_body = _member_prefix_from_raw(
        member.name,
        _header_record() + b"".join(encoding_rows),
    )
    with pytest.raises(RUNNER.RunnerStop) as encoding_exc:
        RUNNER._process_member(member, encoding_body)
    assert encoding_exc.value.reason == "PROPERTY_TYPE_ENCODING_UNEXPECTED"

    schema = json.loads(EXECUTION_SCHEMA_PATH.read_text(encoding="utf-8"))
    legacy_schema = json.loads(LEGACY_EXECUTION_SCHEMA_PATH.read_text(encoding="utf-8"))
    stop_reasons = schema["properties"]["stop_reason"]["anyOf"][1]["enum"]
    legacy_stop_reasons = legacy_schema["properties"]["stop_reason"]["anyOf"][1]["enum"]

    assert schema["properties"]["schema_version"]["const"] == "1.1.0"
    assert legacy_schema["properties"]["schema_version"]["const"] == "1.0.0"
    assert "PROPERTY_TYPE_ENCODING_UNEXPECTED" in stop_reasons
    assert "PROPERTY_TYPE_FORMAT_UNEXPECTED" in stop_reasons
    assert "PROPERTY_TYPE_ENCODING_UNEXPECTED" not in legacy_stop_reasons
    assert "PROPERTY_TYPE_FORMAT_UNEXPECTED" in legacy_stop_reasons


def test_offline_remediation_keeps_network_workflow_absent() -> None:
    assert not WORKFLOW_PATH.exists()
