from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_second_attempt_execution_result.v1.json"
)
EXECUTION_SCHEMA = ROOT / "schemas/agents/ny_transient_local_execution_result.schema.json"
DISCOVERY_SCHEMA = ROOT / "schemas/agents/ny_owner_name_schema_discovery_result.schema.json"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_second_attempt_result_is_non_pii_blocked_evidence() -> None:
    result = _load(RESULT)
    execution_schema = _load(EXECUTION_SCHEMA)
    discovery_schema = _load(DISCOVERY_SCHEMA)
    registry = Registry().with_resource(
        str(discovery_schema["$id"]),
        Resource.from_contents(discovery_schema),
    )

    Draft202012Validator(execution_schema, registry=registry).validate(result)
    assert result["status"] == "BLOCKED"
    assert result["reason_code"] == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result["local_file_deleted"] is True
    assert result["no_owner_values_returned"] is True
