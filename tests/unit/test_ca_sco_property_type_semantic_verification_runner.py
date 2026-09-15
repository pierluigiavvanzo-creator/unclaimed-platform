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
from typing import Any

import pytest
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
EXECUTION_SCHEMA_PATH = (
    ROOT / "schemas/common/property_type_semantic_verification_execution.schema.json"
)


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_property_type_semantic_verification",
        RUNNER_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RUNNER = _load_runner()


def _execution_validator() -> Draft202012Validator:
    schema = json.loads(EXECUTION_SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _row(property_type: str, *, columns: int = 25) -> list[str]:
    values = ["SYNTHETIC_VALUE"] * columns
    values[0] = "SYNTHETIC_ID"
    if columns > 1:
        values[1] = property_type
    return values


def _member_prefix(
    member_name: str,
    codes: list[str],
    *,
    header: tuple[str, ...] | None = None,
    row_columns: int = 25,
) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\r\n")
    writer.writerow(header or RUNNER.CANONICAL_HEADER)
    for code in codes:
        writer.writerow(_row(code, columns=row_columns))

    raw = output.getvalue().encode("utf-8")
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


class MockRangeHandle:
    def __init__(
        self,
        status: int,
        headers: dict[str, str],
        body: bytes,
    ) -> None:
        self.status = status
        self.headers = headers
        self._body = body
        self.read_calls = 0
        self.closed = False

    def read(self, max_bytes: int) -> bytes:
        self.read_calls += 1
        return self._body[:max_bytes]

    def close(self) -> None:
        self.closed = True


class MockTransport:
    def __init__(
        self,
        *,
        codes_by_member: dict[str, list[str]] | None = None,
        range_status: int = 206,
        head_headers: dict[str, str] | None = None,
        mutate_header: bool = False,
        row_columns: int = 25,
    ) -> None:
        default_codes = ["IN03", "AC01", "ZZZZ", "IN01"]
        self.codes_by_member = codes_by_member or {
            member.name: list(default_codes) for member in RUNNER.CANONICAL_MEMBERS
        }
        self.range_status = range_status
        self.head_headers = head_headers or {
            "content-length": str(RUNNER.EXPECTED_LENGTH),
            "content-type": "application/zip",
            "accept-ranges": "bytes",
            "etag": RUNNER.EXPECTED_ETAG,
            "last-modified": "SYNTHETIC",
        }
        self.mutate_header = mutate_header
        self.row_columns = row_columns
        self.head_calls = 0
        self.range_calls: list[tuple[int, int]] = []
        self.handles: list[MockRangeHandle] = []

    def head(self, timeout_seconds: int) -> Any:
        assert timeout_seconds == RUNNER.DEFAULT_TIMEOUT_SECONDS
        self.head_calls += 1
        return RUNNER.HeadObservation(status=200, headers=self.head_headers)

    def open_range(
        self,
        start: int,
        end: int,
        timeout_seconds: int,
    ) -> MockRangeHandle:
        assert timeout_seconds == RUNNER.DEFAULT_TIMEOUT_SECONDS
        self.range_calls.append((start, end))
        member = next(
            item for item in RUNNER.CANONICAL_MEMBERS if item.local_header_offset == start
        )
        header = tuple(RUNNER.CANONICAL_HEADER)
        if self.mutate_header:
            mutable = list(header)
            mutable[1] = "WRONG_PROPERTY_TYPE"
            header = tuple(mutable)
        body = _member_prefix(
            member.name,
            self.codes_by_member[member.name],
            header=header,
            row_columns=self.row_columns,
        )
        handle = MockRangeHandle(
            self.range_status,
            {
                "content-range": f"bytes {start}-{end}/{RUNNER.EXPECTED_LENGTH}",
                "content-length": str(RUNNER.RANGE_RESPONSE_BYTES),
            },
            body,
        )
        self.handles.append(handle)
        return handle


def _execute(transport: MockTransport) -> dict[str, Any]:
    return RUNNER.execute(
        execution_approval_ref="SYNTHETIC_EXECUTION_APPROVAL",
        privacy_approval_ref="SYNTHETIC_PRIVACY_APPROVAL",
        transport=transport,
    )


def test_synthetic_success_is_bounded_and_schema_valid() -> None:
    transport = MockTransport()
    result = _execute(transport)

    assert result["semantic_result_status"] == "SAMPLE_COMPATIBLE_INSURANCE_CODE_OBSERVED"
    assert result["stop_reason"] is None
    assert result["requests_summary"] == {
        "head_requests": 1,
        "range_requests": 4,
        "http_requests_total": 5,
        "total_body_bytes_read": 524_288,
    }
    assert result["sample_summary"]["sample_rows_examined"] == 16
    assert result["sample_summary"]["distinct_property_type_codes"] == [
        "AC01",
        "IN01",
        "IN03",
        "ZZZZ",
    ]
    assert result["sample_summary"]["distinct_insurance_codes"] == ["IN01", "IN03"]
    assert transport.head_calls == 1
    assert len(transport.range_calls) == 4
    assert all(handle.read_calls == 1 for handle in transport.handles)
    assert all(handle.closed for handle in transport.handles)
    _execution_validator().validate(result)


def test_synthetic_no_insurance_is_inconclusive_not_success() -> None:
    codes = {
        member.name: ["AC01", "MS01", "SC01", "ZZZZ"]
        for member in RUNNER.CANONICAL_MEMBERS
    }
    result = _execute(MockTransport(codes_by_member=codes))

    assert (
        result["semantic_result_status"]
        == "SAMPLE_CODE_SHAPE_COMPATIBLE_NO_INSURANCE_CODE_OBSERVED"
    )
    assert result["stop_reason"] is None
    assert result["sample_summary"]["distinct_insurance_codes"] == []
    _execution_validator().validate(result)


def test_unknown_insurance_code_stops_fail_closed() -> None:
    codes = {
        member.name: ["IN42", "AC01", "SC01", "ZZZZ"]
        for member in RUNNER.CANONICAL_MEMBERS
    }
    result = _execute(MockTransport(codes_by_member=codes))

    assert result["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert result["stop_reason"] == "UNRECOGNIZED_INSURANCE_PREFIX_CODE"
    _execution_validator().validate(result)


def test_ignored_range_stops_without_reading_unexpected_body() -> None:
    transport = MockTransport(range_status=200)
    result = _execute(transport)

    assert result["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert result["stop_reason"] == "RANGE_RESPONSE_NOT_PARTIAL"
    assert len(transport.handles) == 1
    assert transport.handles[0].read_calls == 0
    assert transport.handles[0].closed is True
    assert result["requests_summary"]["total_body_bytes_read"] == 0
    _execution_validator().validate(result)


def test_header_mismatch_stops_before_accepting_data_rows() -> None:
    result = _execute(MockTransport(mutate_header=True))

    assert result["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert result["stop_reason"] == "HEADER_MISMATCH"
    assert result["sample_summary"]["sample_rows_examined"] == 0
    _execution_validator().validate(result)


def test_row_column_count_mismatch_stops() -> None:
    result = _execute(MockTransport(row_columns=24))

    assert result["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert result["stop_reason"] == "ROW_COLUMN_COUNT_MISMATCH"
    _execution_validator().validate(result)


def test_missing_privacy_approval_fails_before_transport() -> None:
    transport = MockTransport()
    with pytest.raises(RUNNER.RunnerAuthorizationError):
        RUNNER.execute(
            execution_approval_ref="SYNTHETIC_EXECUTION_APPROVAL",
            privacy_approval_ref="",
            transport=transport,
        )

    assert transport.head_calls == 0
    assert transport.range_calls == []


def test_missing_execution_approval_fails_before_transport() -> None:
    transport = MockTransport()
    with pytest.raises(RUNNER.RunnerAuthorizationError):
        RUNNER.execute(
            execution_approval_ref="",
            privacy_approval_ref="SYNTHETIC_PRIVACY_APPROVAL",
            transport=transport,
        )

    assert transport.head_calls == 0
    assert transport.range_calls == []


def test_live_cli_is_opt_in_and_workflow_remains_absent() -> None:
    workflow = ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
    assert not workflow.exists()

    with pytest.raises(SystemExit):
        RUNNER._parse_args(
            [
                "--approval-ref",
                "SYNTHETIC_EXECUTION_APPROVAL",
                "--privacy-approval-ref",
                "SYNTHETIC_PRIVACY_APPROVAL",
                "--output",
                "ignored.json",
            ]
        )
