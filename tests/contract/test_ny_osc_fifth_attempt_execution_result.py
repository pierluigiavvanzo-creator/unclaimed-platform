from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_execution_result.v1.json"
)
EXECUTION_SCHEMA = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_1.schema.json"
)
DISCOVERY_SCHEMA = (
    ROOT / "schemas/agents/ny_owner_name_schema_discovery_result.schema.json"
)
DIAGNOSTIC_SCHEMA = (
    ROOT / "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_fifth_attempt_result_is_non_pii_fail_closed_evidence() -> None:
    result = _load(RESULT)
    execution_schema = _load(EXECUTION_SCHEMA)
    discovery_schema = _load(DISCOVERY_SCHEMA)
    diagnostic_schema = _load(DIAGNOSTIC_SCHEMA)

    registry = (
        Registry()
        .with_resource(
            str(discovery_schema["$id"]),
            Resource.from_contents(discovery_schema),
        )
        .with_resource(
            str(diagnostic_schema["$id"]),
            Resource.from_contents(diagnostic_schema),
        )
    )

    Draft202012Validator(execution_schema, registry=registry).validate(result)

    assert result["contract_version"] == "1.1.0"
    assert result["status"] == "BLOCKED"
    assert result["reason_code"] == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result["archive_byte_count"] == 409_477_526
    assert result["local_file_deleted"] is True
    assert result["logical_deletion_only"] is True
    assert result["physical_secure_erasure_guaranteed"] is False
    assert result["no_raw_path_returned"] is True
    assert result["no_owner_values_returned"] is True

    schema_result = result["schema_result"]
    assert schema_result["observed_data_field_count"] == 13
    assert schema_result["aggregate_complete_record_count"] == 213_454
    assert schema_result["property_type_ascii_record_count"] == 213_454
    assert schema_result["observed_delimiter"] == "|"
    assert schema_result["observed_header_state"] == "NO_HEADER_OBSERVED"
    assert schema_result["raw_file_persisted"] is False
    assert schema_result["owner_rows_persisted"] is False
    assert schema_result["owner_field_logging"] is False
    assert schema_result["row_specific_human_inspection"] is False
    assert schema_result["no_owner_values_returned"] is True

    diagnostic = result["structural_diagnostic"]
    assert diagnostic["classification"] == "QUOTED_DELIMITER_INTERACTION_AMBIGUOUS"
    assert diagnostic["expected_field_count"] == 14
    assert diagnostic["structural_field_count"] == 13
    assert diagnostic["raw_pipe_count"] == 228_072
    assert diagnostic["structural_pipe_count"] == 12
    assert diagnostic["suppressed_pipe_count"] == 228_060
    assert diagnostic["quote_byte_count"] == 3
    assert diagnostic["quote_open_event_count"] == 1
    assert diagnostic["quote_close_event_count"] == 1
    assert diagnostic["doubled_quote_pair_count"] == 0
    assert diagnostic["physical_line_breaks_inside_quotes"] == 17_543
    assert diagnostic["ended_inside_quote"] is False
    assert diagnostic["no_raw_record_returned"] is True
    assert diagnostic["no_owner_values_returned"] is True
