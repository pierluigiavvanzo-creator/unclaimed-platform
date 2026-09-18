import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from unclaimed_platform.api.reviewer import (
    synthetic_mvp1_integrated_economics_snapshot,
)

_REPO_ROOT = Path(__file__).resolve().parents[2]
_SCHEMA_DIR = _REPO_ROOT / "schemas"
_REVIEWER_SCHEMA = (
    _SCHEMA_DIR / "ui" / "ny_mvp1_integrated_economics_reviewer.schema.json"
)
_FOLLOW_UP_SCHEMA = (
    _SCHEMA_DIR
    / "economics"
    / "ny_mvp1_follow_up_cost_measurement_result.schema.json"
)
_INTEGRATION_SCHEMA = (
    _SCHEMA_DIR
    / "economics"
    / "ny_mvp1_case_economics_integration_result.schema.json"
)
_EXPLICIT_INPUT_SCHEMA = (
    _SCHEMA_DIR / "economics" / "ny_mvp1_explicit_case_economics_input.schema.json"
)
_EXPLICIT_RESULT_SCHEMA = (
    _SCHEMA_DIR / "economics" / "ny_mvp1_explicit_case_economics_result.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_integrated_economics_reviewer_snapshot_validates_against_schema() -> None:
    resources = [
        _load(_FOLLOW_UP_SCHEMA),
        _load(_INTEGRATION_SCHEMA),
        _load(_EXPLICIT_INPUT_SCHEMA),
        _load(_EXPLICIT_RESULT_SCHEMA),
    ]
    registry = Registry().with_resources(
        [(resource["$id"], Resource.from_contents(resource)) for resource in resources]
    )
    validator = Draft202012Validator(_load(_REVIEWER_SCHEMA), registry=registry)

    payload = synthetic_mvp1_integrated_economics_snapshot().model_dump(mode="json")

    validator.validate(payload)
