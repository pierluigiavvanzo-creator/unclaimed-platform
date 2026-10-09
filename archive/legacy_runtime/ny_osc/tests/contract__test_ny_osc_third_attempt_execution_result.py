from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_third_attempt_execution_result.v1.json"
)
EXECUTION_SCHEMA = ROOT / "schemas/agents/ny_transient_local_execution_result.schema.json"
DISCOVERY_SCHEMA = ROOT / "schemas/agents/ny_owner_name_schema_discovery_result.schema.json"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_third_attempt_result_is_non_pii_fail_closed_evidence() -> None:
    result = _load(RESULT)
    execution_schema = _load(EXECUTION_SCHEMA)
    discovery_schema = _load(DISCOVERY_SCHEMA)
    registry = Registry().with_resource(
        str(discovery_schema["$id"]),
        Resource.from_contents(discovery_schema),
    )

    Draft202012Validator(execution_schema, registry=registry).validate(result)

    assert result["status"] == "BLOCKED"
    assert result["reason_code"] == "MALFORMED_QUOTED_RECORD"
    assert result["archive_byte_count"] == 409_477_526
    assert result["local_file_deleted"] is True
    assert result["logical_deletion_only"] is True
    assert result["physical_secure_erasure_guaranteed"] is False
    assert result["no_raw_path_returned"] is True
    assert result["no_owner_values_returned"] is True

    schema_result = result["schema_result"]
    assert schema_result["aggregate_complete_record_count"] == 165_438
    assert schema_result["property_type_ascii_record_count"] == 165_438
    assert schema_result["observed_delimiter"] == "|"
    assert schema_result["observed_header_state"] == "NO_HEADER_OBSERVED"
    assert schema_result["raw_file_persisted"] is False
    assert schema_result["owner_rows_persisted"] is False
    assert schema_result["owner_field_logging"] is False
