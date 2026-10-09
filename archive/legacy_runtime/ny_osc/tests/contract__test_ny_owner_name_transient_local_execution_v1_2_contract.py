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
RESULT_V1_1 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_1.schema.json"
)
RESULT_V1_2 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_2.schema.json"
)
DISCOVERY = ROOT / "schemas/agents/ny_owner_name_schema_discovery_result.schema.json"
STRUCTURAL = (
    ROOT / "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json"
)
QUOTE = (
    ROOT / "schemas/agents/ny_owner_name_quote_dialect_diagnostic_result.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _registry() -> Registry:
    registry = Registry()
    for path in (DISCOVERY, STRUCTURAL, QUOTE):
        schema = _load(path)
        registry = registry.with_resource(
            str(schema["$id"]),
            Resource.from_contents(schema),
        )
    return registry


def test_v1_1_authorization_requires_line_local_mode() -> None:
    schema = _load(AUTH_V1_1)
    payload = {
        "contract_version": "1.1.0",
        "mode": "SYNTHETIC_TEST",
        "attempt_number": 1,
        "local_file_approval_ref": "local",
        "gate2_approval_ref": "gate2",
        "local_file_approval_granted": True,
        "gate2_approval_granted": True,
        "expected_local_filename": "FINDERS.zip",
        "max_download_bytes": 100,
        "max_uncompressed_bytes": 1000,
        "max_archive_members": 1,
        "delete_local_file_immediately": True,
        "durable_raw_persistence_allowed": False,
        "repository_persistence_allowed": False,
        "cloud_sync_allowed": False,
        "owner_field_logging_allowed": False,
        "row_specific_human_inspection_allowed": False,
        "quote_dialect_mode": "LINE_LOCAL_ARBITRATION",
    }
    Draft202012Validator(schema).validate(payload)

    missing = dict(payload)
    missing.pop("quote_dialect_mode")
    with pytest.raises(ValidationError):
        Draft202012Validator(schema).validate(missing)

    wrong = dict(payload)
    wrong["quote_dialect_mode"] = "MULTILINE_LEGACY"
    with pytest.raises(ValidationError):
        Draft202012Validator(schema).validate(wrong)


def test_v1_2_requires_mutually_exclusive_reason_bound_diagnostics() -> None:
    schema = _load(RESULT_V1_2)
    validator = Draft202012Validator(schema, registry=_registry())

    base = {
        "contract_version": "1.2.0",
        "status": "BLOCKED",
        "reason_code": "QUOTE_DIALECT_AMBIGUOUS",
        "local_file_deleted": True,
        "logical_deletion_only": True,
        "physical_secure_erasure_guaranteed": False,
        "archive_byte_count": 100,
        "schema_discovery_quote_dialect_mode": "LINE_LOCAL_ARBITRATION",
        "structural_diagnostic": None,
        "quote_dialect_diagnostic": {
            "contract_version": "1.0.0",
            "source_id": "ny.osc.unclaimed_funds.owner_name_file",
            "diagnostic_scope": "QUOTE_DIALECT_STRUCTURAL_ONLY",
            "reason_code": "QUOTE_DIALECT_AMBIGUOUS",
            "classification": "RAW_AND_QUOTE_AWARE_FIELD_COUNTS_DIVERGE",
            "expected_field_count": 14,
            "raw_field_count": 15,
            "quote_aware_field_count": 14,
            "raw_pipe_count": 14,
            "quote_aware_structural_pipe_count": 13,
            "suppressed_pipe_count": 1,
            "quote_byte_count": 2,
            "quote_open_event_count": 1,
            "quote_close_event_count": 1,
            "doubled_quote_pair_count": 0,
            "ended_inside_quote": False,
            "no_raw_record_returned": True,
            "no_owner_values_returned": True,
        },
        "schema_result": {
            "contract_version": "1.0.0",
            "status": "BLOCKED",
            "reason_code": "QUOTE_DIALECT_AMBIGUOUS",
            "source_id": "ny.osc.unclaimed_funds.owner_name_file",
            "gate_id": (
                "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_"
                "TRANSIENT_PII_AUTHORIZATION"
            ),
            "approval_id": "synthetic",
            "archive_byte_count": 100,
            "archive_member_count": 1,
            "member_names_persisted": False,
            "selected_text_member_present": True,
            "selected_member_uncompressed_bytes": 1000,
            "observed_delimiter": "|",
            "documented_layout_field_count": 14,
            "observed_data_field_count": None,
            "observed_header_state": "NO_HEADER_OBSERVED",
            "physical_header_names": [],
            "aggregate_complete_record_count": 0,
            "property_type_code_column_index_zero_based": 1,
            "property_type_ascii_record_count": 0,
            "nature_of_property_mapping_state": "NOT_CONFIRMED",
            "encoding_state": "NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY",
            "raw_file_persisted": False,
            "owner_rows_persisted": False,
            "owner_field_logging": False,
            "row_specific_human_inspection": False,
            "no_owner_values_returned": True,
        },
        "no_raw_path_returned": True,
        "no_owner_values_returned": True,
    }
    validator.validate(base)

    missing = dict(base)
    missing["quote_dialect_diagnostic"] = None
    with pytest.raises(ValidationError):
        validator.validate(missing)

    dual = json.loads(json.dumps(base))
    dual["structural_diagnostic"] = {
        "contract_version": "1.0.0",
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "diagnostic_scope": "STRUCTURAL_ONLY",
        "reason_code": "UNEXPECTED_DATA_FIELD_COUNT",
        "classification": "RAW_DELIMITER_COUNT_BELOW_DOCUMENTED",
        "expected_field_count": 14,
        "structural_field_count": 13,
        "raw_pipe_count": 12,
        "structural_pipe_count": 12,
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
    with pytest.raises(ValidationError):
        validator.validate(dual)

    wrong_reason = json.loads(json.dumps(base))
    wrong_reason["schema_result"]["reason_code"] = "UNEXPECTED_DATA_FIELD_COUNT"
    with pytest.raises(ValidationError):
        validator.validate(wrong_reason)


def test_v1_2_discovered_requires_schema_result() -> None:
    schema = _load(RESULT_V1_2)
    validator = Draft202012Validator(schema, registry=_registry())
    payload = {
        "contract_version": "1.2.0",
        "status": "DISCOVERED",
        "reason_code": "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
        "local_file_deleted": True,
        "logical_deletion_only": True,
        "physical_secure_erasure_guaranteed": False,
        "archive_byte_count": 100,
        "schema_result": None,
        "schema_discovery_quote_dialect_mode": "LINE_LOCAL_ARBITRATION",
        "structural_diagnostic": None,
        "quote_dialect_diagnostic": None,
        "no_raw_path_returned": True,
        "no_owner_values_returned": True,
    }
    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_historical_v1_1_and_gate5_are_not_retargeted() -> None:
    result_v1_1 = _load(RESULT_V1_1)
    assert result_v1_1["$id"].endswith(":1.1.0")
    assert "quote_dialect_diagnostic" not in result_v1_1["properties"]

    runner = (ROOT / "scripts/ny_osc_gate5_transient_local.ps1").read_text(
        encoding="utf-8"
    )
    assert "ny_owner_name_transient_local_execution_v1_2" not in runner
    assert "LINE_LOCAL_ARBITRATION" not in runner

def _blocked_schema_result(reason_code: str) -> dict[str, object]:
    return {
        "contract_version": "1.0.0",
        "status": "BLOCKED",
        "reason_code": reason_code,
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "gate_id": (
            "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_"
            "TRANSIENT_PII_AUTHORIZATION"
        ),
        "approval_id": "synthetic",
        "archive_byte_count": 100,
        "archive_member_count": 1,
        "member_names_persisted": False,
        "selected_text_member_present": True,
        "selected_member_uncompressed_bytes": 1000,
        "observed_delimiter": None,
        "documented_layout_field_count": 14,
        "observed_data_field_count": None,
        "observed_header_state": "NOT_EVALUATED",
        "physical_header_names": [],
        "aggregate_complete_record_count": None,
        "property_type_code_column_index_zero_based": 1,
        "property_type_ascii_record_count": None,
        "nature_of_property_mapping_state": "NOT_CONFIRMED",
        "encoding_state": "NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY",
        "raw_file_persisted": False,
        "owner_rows_persisted": False,
        "owner_field_logging": False,
        "row_specific_human_inspection": False,
        "no_owner_values_returned": True,
    }


def test_v1_2_rejects_non_special_blocked_reason_mismatch() -> None:
    schema = _load(RESULT_V1_2)
    validator = Draft202012Validator(schema, registry=_registry())

    payload = {
        "contract_version": "1.2.0",
        "status": "BLOCKED",
        "reason_code": "NOT_A_ZIP_ARCHIVE",
        "local_file_deleted": True,
        "logical_deletion_only": True,
        "physical_secure_erasure_guaranteed": False,
        "archive_byte_count": 100,
        "schema_result": _blocked_schema_result("ARCHIVE_HAS_NO_FILES"),
        "schema_discovery_quote_dialect_mode": "LINE_LOCAL_ARBITRATION",
        "structural_diagnostic": None,
        "quote_dialect_diagnostic": None,
        "no_raw_path_returned": True,
        "no_owner_values_returned": True,
    }

    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_v1_2_rejects_discovered_reason_mismatch() -> None:
    schema = _load(RESULT_V1_2)
    validator = Draft202012Validator(schema, registry=_registry())

    discovered = _blocked_schema_result("TEXT_MEMBER_EMPTY")
    discovered.update(
        {
            "status": "DISCOVERED",
            "reason_code": "TEXT_MEMBER_EMPTY",
            "observed_delimiter": "|",
            "observed_data_field_count": 14,
            "aggregate_complete_record_count": 1,
            "property_type_ascii_record_count": 1,
            "nature_of_property_mapping_state": (
                "DETERMINISTIC_DOCUMENTED_POSITION_REQUIRES_LATER_CODE_VALIDATION"
            ),
        }
    )
    payload = {
        "contract_version": "1.2.0",
        "status": "DISCOVERED",
        "reason_code": "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
        "local_file_deleted": True,
        "logical_deletion_only": True,
        "physical_secure_erasure_guaranteed": False,
        "archive_byte_count": 100,
        "schema_result": discovered,
        "schema_discovery_quote_dialect_mode": "LINE_LOCAL_ARBITRATION",
        "structural_diagnostic": None,
        "quote_dialect_diagnostic": None,
        "no_raw_path_returned": True,
        "no_owner_values_returned": True,
    }

    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_v1_2_local_cap_reason_rejects_schema_result() -> None:
    schema = _load(RESULT_V1_2)
    validator = Draft202012Validator(schema, registry=_registry())

    payload = {
        "contract_version": "1.2.0",
        "status": "BLOCKED",
        "reason_code": "LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
        "local_file_deleted": True,
        "logical_deletion_only": True,
        "physical_secure_erasure_guaranteed": False,
        "archive_byte_count": 101,
        "schema_result": _blocked_schema_result("NOT_A_ZIP_ARCHIVE"),
        "schema_discovery_quote_dialect_mode": "LINE_LOCAL_ARBITRATION",
        "structural_diagnostic": None,
        "quote_dialect_diagnostic": None,
        "no_raw_path_returned": True,
        "no_owner_values_returned": True,
    }

    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_ci_typechecks_line_local_runtime_sources() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "Mypy NY OSC line-local runtime" in workflow
    assert (
        "src/unclaimed_platform/adapters/sources/"
        "ny_owner_name_transient_local_execution.py"
    ) in workflow
    assert (
        "src/unclaimed_platform/adapters/sources/"
        "ny_owner_name_transient_local_execution_v1_2.py"
    ) in workflow

