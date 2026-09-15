from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_semantic_runner_implementation_authorization.schema.json"
)
AUTH_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_runner_implementation_approval.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_implementation_authorization_is_mock_only_and_valid() -> None:
    schema = _load(SCHEMA_PATH)
    authorization = _load(AUTH_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    ).validate(authorization)

    scope = authorization["authorized_scope"]
    assert isinstance(scope, dict)
    assert scope["runner_implementation"] is True
    assert scope["synthetic_mock_testing"] is True
    assert scope["real_network_execution"] is False
    assert scope["network_workflow"] is False
    assert scope["real_row_access"] is False
    assert scope["transient_row_privacy"] is False
    assert scope["source_approval"] is False
    assert scope["registry_activation"] is False


def test_runner_exists_but_network_workflow_remains_absent() -> None:
    assert RUNNER_PATH.exists()
    assert not WORKFLOW_PATH.exists()


def test_source_policy_and_registry_remain_fail_closed() -> None:
    policy = _load(POLICY_PATH)
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["authorized_processing_purposes"] == []
    assert policy["allowed_fields"] == []
    assert policy["allow_pii"] is False

    assert "enabled: false" in registry_text
    assert "approved_for_use: false" in registry_text
