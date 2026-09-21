from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
AUTH_V1_1 = (
    ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_1.schema.json"
)
AUTH_V1_2 = (
    ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_2.schema.json"
)
RESULT_V1_2 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_2.schema.json"
)
RESULT_V1_3 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_3.schema.json"
)
DISCOVERY = ROOT / "schemas/agents/ny_owner_name_schema_discovery_result.schema.json"
STRUCTURAL = (
    ROOT / "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json"
)
GATE6 = ROOT / "scripts/ny_osc_gate6_transient_local.ps1"
RUNTIME_V1_3 = (
    ROOT
    / "src/unclaimed_platform/adapters/sources"
    / "ny_owner_name_transient_local_execution_v1_3.py"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _registry() -> Registry:
    registry = Registry()
    for path in (DISCOVERY, STRUCTURAL):
        schema = _load(path)
        registry = registry.with_resource(
            str(schema["$id"]),
            Resource.from_contents(schema),
        )
    return registry


def _auth_payload() -> dict[str, object]:
    return {
        "contract_version": "1.2.0",
        "mode": "SYNTHETIC_TEST",
        "attempt_number": 1,
        "local_file_approval_ref": "synthetic-local",
        "gate2_approval_ref": "synthetic-gate2",
        "local_file_approval_granted": True,
        "gate2_approval_granted": True,
        "expected_local_filename": "FINDERS.zip",
        "max_download_bytes": 100_000,
        "max_uncompressed_bytes": 100_000,
        "max_archive_members": 1,
        "delete_local_file_immediately": True,
        "durable_raw_persistence_allowed": False,
        "repository_persistence_allowed": False,
        "cloud_sync_allowed": False,
        "owner_field_logging_allowed": False,
        "row_specific_human_inspection_allowed": False,
        "quote_dialect_mode": "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
    }


def _schema_result(
    *,
    status: str,
    reason_code: str,
    observed_data_field_count: int | None,
) -> dict[str, object]:
    return {
        "contract_version": "1.0.0",
        "status": status,
        "reason_code": reason_code,
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "gate_id": (
            "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_"
            "TRANSIENT_PII_AUTHORIZATION"
        ),
        "approval_id": "synthetic-gate2",
        "archive_byte_count": 100,
        "archive_member_count": 1,
        "member_names_persisted": False,
        "selected_text_member_present": True,
        "selected_member_uncompressed_bytes": 1000,
        "observed_delimiter": "|",
        "documented_layout_field_count": 14,
        "observed_data_field_count": observed_data_field_count,
        "observed_header_state": "NO_HEADER_OBSERVED",
        "physical_header_names": [],
        "aggregate_complete_record_count": 1,
        "property_type_code_column_index_zero_based": 1,
        "property_type_ascii_record_count": 1,
        "nature_of_property_mapping_state": (
            "DETERMINISTIC_DOCUMENTED_POSITION_REQUIRES_LATER_CODE_VALIDATION"
        ),
        "encoding_state": "NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY",
        "raw_file_persisted": False,
        "owner_rows_persisted": False,
        "owner_field_logging": False,
        "row_specific_human_inspection": False,
        "no_owner_values_returned": True,
    }


def _structural(field_count: int) -> dict[str, object]:
    raw_pipes = field_count - 1
    return {
        "contract_version": "1.0.0",
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "diagnostic_scope": "STRUCTURAL_ONLY",
        "reason_code": "UNEXPECTED_DATA_FIELD_COUNT",
        "classification": (
            "RAW_DELIMITER_COUNT_BELOW_DOCUMENTED"
            if field_count < 14
            else "STRUCTURAL_MISMATCH_UNCLASSIFIED"
        ),
        "expected_field_count": 14,
        "structural_field_count": field_count,
        "raw_pipe_count": raw_pipes,
        "structural_pipe_count": raw_pipes,
        "suppressed_pipe_count": 0,
        "quote_byte_count": 0,
        "quote_open_event_count": 0,
        "quote_close_event_count": 0,
        "doubled_quote_pair_count": 0,
        "physical_line_breaks_inside_quotes": 0,
        "ended_inside_quote": False,
        "no_raw_record_returned": True,
        "no_owner_values_returned": True,
    }


def _result_payload(
    *,
    status: str,
    reason_code: str,
    schema_result: dict[str, object] | None,
    structural_diagnostic: dict[str, object] | None = None,
) -> dict[str, object]:
    return {
        "contract_version": "1.3.0",
        "status": status,
        "reason_code": reason_code,
        "local_file_deleted": True,
        "logical_deletion_only": True,
        "physical_secure_erasure_guaranteed": False,
        "archive_byte_count": 100,
        "schema_result": schema_result,
        "schema_discovery_quote_dialect_mode": (
            "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
        ),
        "structural_diagnostic": structural_diagnostic,
        "quote_dialect_diagnostic": None,
        "no_raw_path_returned": True,
        "no_owner_values_returned": True,
    }


def test_v1_2_authorization_is_synthetic_raw_literal_only() -> None:
    schema = _load(AUTH_V1_2)
    validator = Draft202012Validator(schema)
    payload = _auth_payload()
    validator.validate(payload)

    real = dict(payload)
    real["mode"] = "AUTHORIZED_REAL_ONCE"
    with pytest.raises(ValidationError):
        validator.validate(real)

    line_local = dict(payload)
    line_local["quote_dialect_mode"] = "LINE_LOCAL_ARBITRATION"
    with pytest.raises(ValidationError):
        validator.validate(line_local)


def test_v1_3_discovered_contract_accepts_only_raw_literal_provenance() -> None:
    schema = _load(RESULT_V1_3)
    validator = Draft202012Validator(schema, registry=_registry())
    payload = _result_payload(
        status="DISCOVERED",
        reason_code="DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
        schema_result=_schema_result(
            status="DISCOVERED",
            reason_code="DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
            observed_data_field_count=14,
        ),
    )
    validator.validate(payload)

    wrong_mode = json.loads(json.dumps(payload))
    wrong_mode["schema_discovery_quote_dialect_mode"] = "LINE_LOCAL_ARBITRATION"
    with pytest.raises(ValidationError):
        validator.validate(wrong_mode)


def test_v1_3_unexpected_width_requires_structural_diagnostic() -> None:
    schema = _load(RESULT_V1_3)
    validator = Draft202012Validator(schema, registry=_registry())
    payload = _result_payload(
        status="BLOCKED",
        reason_code="UNEXPECTED_DATA_FIELD_COUNT",
        schema_result=_schema_result(
            status="BLOCKED",
            reason_code="UNEXPECTED_DATA_FIELD_COUNT",
            observed_data_field_count=15,
        ),
        structural_diagnostic=_structural(15),
    )
    validator.validate(payload)

    missing = json.loads(json.dumps(payload))
    missing["structural_diagnostic"] = None
    with pytest.raises(ValidationError):
        validator.validate(missing)


def test_v1_3_quote_specific_reasons_and_diagnostics_are_rejected() -> None:
    schema = _load(RESULT_V1_3)
    validator = Draft202012Validator(schema, registry=_registry())

    quote_reason = _result_payload(
        status="BLOCKED",
        reason_code="QUOTE_DIALECT_AMBIGUOUS",
        schema_result=_schema_result(
            status="BLOCKED",
            reason_code="QUOTE_DIALECT_AMBIGUOUS",
            observed_data_field_count=None,
        ),
    )
    with pytest.raises(ValidationError):
        validator.validate(quote_reason)

    malformed_reason = _result_payload(
        status="BLOCKED",
        reason_code="MALFORMED_QUOTED_RECORD",
        schema_result=_schema_result(
            status="BLOCKED",
            reason_code="MALFORMED_QUOTED_RECORD",
            observed_data_field_count=None,
        ),
    )
    with pytest.raises(ValidationError):
        validator.validate(malformed_reason)

    valid = _result_payload(
        status="DISCOVERED",
        reason_code="DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
        schema_result=_schema_result(
            status="DISCOVERED",
            reason_code="DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
            observed_data_field_count=14,
        ),
    )
    valid["quote_dialect_diagnostic"] = {"unexpected": True}
    with pytest.raises(ValidationError):
        validator.validate(valid)


def test_v1_3_local_cap_reason_requires_null_schema_result() -> None:
    schema = _load(RESULT_V1_3)
    validator = Draft202012Validator(schema, registry=_registry())
    payload = _result_payload(
        status="BLOCKED",
        reason_code="LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
        schema_result=None,
    )
    validator.validate(payload)

    wrong = json.loads(json.dumps(payload))
    wrong["schema_result"] = _schema_result(
        status="BLOCKED",
        reason_code="NOT_A_ZIP_ARCHIVE",
        observed_data_field_count=None,
    )
    with pytest.raises(ValidationError):
        validator.validate(wrong)


def test_historical_v1_1_v1_2_and_gate6_are_not_retargeted() -> None:
    auth_v1_1 = _load(AUTH_V1_1)
    result_v1_2 = _load(RESULT_V1_2)
    gate6 = GATE6.read_text(encoding="utf-8")

    assert auth_v1_1["properties"]["quote_dialect_mode"]["const"] == (
        "LINE_LOCAL_ARBITRATION"
    )
    assert "AUTHORIZED_REAL_ONCE" in auth_v1_1["properties"]["mode"]["enum"]
    assert result_v1_2["properties"]["schema_discovery_quote_dialect_mode"]["const"] == (
        "LINE_LOCAL_ARBITRATION"
    )
    assert "QUOTE_DIALECT_AMBIGUOUS" in result_v1_2["properties"]["reason_code"]["enum"]
    assert "required_quote_dialect_mode" in gate6
    assert "LINE_LOCAL_ARBITRATION" in gate6
    assert "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY" not in gate6


def test_v1_3_runtime_has_no_cli_or_real_builder() -> None:
    source = RUNTIME_V1_3.read_text(encoding="utf-8")

    assert "argparse" not in source
    assert "def main(" not in source
    assert "build_real_execution_authorization" not in source
    assert "AUTHORIZED_REAL_ONCE" not in source
