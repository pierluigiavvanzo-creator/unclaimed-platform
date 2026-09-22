from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/source_access_governance.schema.json"
POLICY_PATH = ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
EXAMPLES_PATH = ROOT / "schemas/examples/ca_sco_source_governance.examples.json"
REGISTRY_PATH = ROOT / "sources/registry.yaml"
REGISTRY_SCHEMA_PATH = ROOT / "schemas/common/source_registry.schema.json"
SOURCE_ID = "ca.sco.unclaimed_property.bulk"


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def governance_validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_proposed_policy_is_schema_valid_and_non_authorizing() -> None:
    policy = load_json(POLICY_PATH)
    governance_validator().validate(policy)

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["beneficiary_matching_authorized"] is False
    assert policy["outreach_authorized"] is False
    assert policy["allow_pii"] is False

    transport = policy["transport"]
    assert isinstance(transport, dict)
    assert transport["allowed_download_hosts"] == []
    assert transport["redirect_policy"] == "BLOCK_UNTIL_APPROVED"
    assert transport["timeout_seconds"] is None
    assert transport["max_bytes"] is None
    assert transport["expected_media_types"] == []


def test_proposed_policy_cannot_authorize_real_acquisition() -> None:
    examples = load_json(EXAMPLES_PATH)
    governance_validator().validate(examples["proposal.valid"])

    with pytest.raises(ValidationError):
        governance_validator().validate(examples["proposal.invalid_authorizes_real"])


def test_registry_contains_candidate_but_zero_approved_real_sources() -> None:
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    registry_schema = load_json(REGISTRY_SCHEMA_PATH)
    Draft202012Validator.check_schema(registry_schema)
    Draft202012Validator(registry_schema).validate(registry)

    sources = registry["sources"]
    candidate = next(source for source in sources if source["source_id"] == SOURCE_ID)

    assert candidate["enabled"] is False
    assert candidate["approved_for_use"] is False
    assert candidate["provenance_required"] is True
    assert sum(bool(source["approved_for_use"]) for source in sources) == 0


def test_policy_and_registry_identify_same_official_source() -> None:
    policy = load_json(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    candidate = next(source for source in registry["sources"] if source["source_id"] == SOURCE_ID)

    assert policy["source_id"] == candidate["source_id"]
    assert policy["official_source_page"] == candidate["base_uri"]
    assert str(policy["official_source_page"]).startswith("https://")
