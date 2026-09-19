from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NY_DOCUMENTED_FIELDS,
    NyOwnerNameSchemaDiscoveryAuthorization,
    NyOwnerNameStructuralDiagnosticResult,
    discover_ny_owner_name_schema,
)

ROOT = Path(__file__).resolve().parents[2]
AUTH_SCHEMA = ROOT / "schemas/agents/ny_owner_name_schema_discovery_authorization.schema.json"
RESULT_SCHEMA = ROOT / "schemas/agents/ny_owner_name_schema_discovery_result.schema.json"
DIAGNOSTIC_SCHEMA = (
    ROOT / "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _archive() -> bytes:
    row = "|".join(
        [
            "1",
            "IN03",
            "Synthetic description",
            "1",
            "Synthetic Owner",
            "1 Synthetic Street",
            "",
            "",
            "Albany",
            "NY",
            "12207-0000",
            "USA",
            "Synthetic Holder",
            "2026",
        ]
    )
    payload = ("|".join(NY_DOCUMENTED_FIELDS) + "\n" + row + "\n").encode("utf-8")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("owner_names.txt", payload)
    return buffer.getvalue()


def _authorization(archive_bytes: bytes) -> NyOwnerNameSchemaDiscoveryAuthorization:
    return NyOwnerNameSchemaDiscoveryAuthorization(
        mode="SYNTHETIC_TEST",
        approval_id="synthetic-gate2-approval",
        max_download_bytes=len(archive_bytes),
        max_uncompressed_bytes=100_000,
        max_archive_members=1,
        persist_raw_bytes=False,
        persist_owner_rows=False,
        owner_field_logging=False,
        row_specific_human_inspection=False,
    )


def test_authorization_and_result_validate_against_json_schema() -> None:
    archive_bytes = _archive()
    authorization = _authorization(archive_bytes)
    result = discover_ny_owner_name_schema(authorization, archive_bytes)

    Draft202012Validator(_load(AUTH_SCHEMA)).validate(
        authorization.model_dump(mode="json")
    )
    Draft202012Validator(_load(RESULT_SCHEMA)).validate(result.model_dump(mode="json"))


def test_result_schema_rejects_raw_persistence() -> None:
    archive_bytes = _archive()
    result = discover_ny_owner_name_schema(
        _authorization(archive_bytes),
        archive_bytes,
    ).model_dump(mode="json")
    result["raw_file_persisted"] = True

    with pytest.raises(ValidationError):
        Draft202012Validator(_load(RESULT_SCHEMA)).validate(result)


def test_serialized_contract_has_no_raw_bytes_or_owner_value_fields() -> None:
    auth_schema = _load(AUTH_SCHEMA)
    result_schema = _load(RESULT_SCHEMA)

    assert "archive_bytes" not in auth_schema["properties"]
    assert "raw_bytes" not in result_schema["properties"]
    assert "owner_name" not in result_schema["properties"]
    assert "owner_address" not in result_schema["properties"]


def test_structural_diagnostic_contract_is_non_pii_and_strict() -> None:
    diagnostic = NyOwnerNameStructuralDiagnosticResult(
        classification="QUOTE_SUPPRESSED_DELIMITER_OBSERVED",
        structural_field_count=13,
        raw_pipe_count=13,
        structural_pipe_count=12,
        suppressed_pipe_count=1,
        quote_byte_count=2,
        quote_open_event_count=1,
        quote_close_event_count=1,
        doubled_quote_pair_count=0,
        physical_line_breaks_inside_quotes=0,
    )
    schema = _load(DIAGNOSTIC_SCHEMA)
    payload = diagnostic.model_dump(mode="json")
    Draft202012Validator(schema).validate(payload)
    properties = schema["properties"]
    for forbidden in (
        "raw_record", "record_excerpt", "record_offset", "field_lengths",
        "property_id", "owner_name", "owner_address", "holder_name",
    ):
        assert forbidden not in properties
    payload["owner_name"] = "Synthetic Owner"
    with pytest.raises(ValidationError):
        Draft202012Validator(schema).validate(payload)
