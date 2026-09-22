from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/source_approval_readiness.schema.json"
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/ca_sco_unclaimed_property_bulk.approval_readiness.v1.json"
)
EXAMPLES_PATH = ROOT / "schemas/examples/ca_sco_approval_readiness.examples.json"
REGISTRY_PATH = ROOT / "sources/registry.yaml"
POLICY_PATH = (
    ROOT
    / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
SOURCE_ID = "ca.sco.unclaimed_property.bulk"


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_readiness_evidence_is_valid_and_non_authorizing() -> None:
    evidence = load_json(EVIDENCE_PATH)
    validator().validate(evidence)

    assert evidence["review_status"] == "EVIDENCE_ONLY_NOT_APPROVED"
    assert evidence["acquisition_performed"] is False
    assert evidence["source_approved"] is False
    assert evidence["source_enabled"] is False
    assert evidence["advertised_format"] == "CSV"
    assert evidence["advertised_update_cadence"] == "EVERY_THURSDAY"
    assert evidence["advertised_download_hosts"] == ["claimit.ca.gov"]


def test_schema_rejects_evidence_that_claims_acquisition_or_approval() -> None:
    examples = load_json(EXAMPLES_PATH)
    validator().validate(examples["readiness.valid"])

    with pytest.raises(ValidationError):
        validator().validate(examples["readiness.invalid_claims_acquisition"])

    with pytest.raises(ValidationError):
        validator().validate(examples["readiness.invalid_claims_approval"])


def test_readiness_matches_registry_and_proposed_policy() -> None:
    evidence = load_json(EVIDENCE_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    policy = load_json(POLICY_PATH)

    candidate = next(
        source for source in registry["sources"] if source["source_id"] == SOURCE_ID
    )

    assert evidence["source_id"] == candidate["source_id"] == policy["source_id"]
    assert evidence["official_source_page"] == candidate["base_uri"]
    assert evidence["official_source_page"] == policy["official_source_page"]

    assert candidate["enabled"] is False
    assert candidate["approved_for_use"] is False
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["beneficiary_matching_authorized"] is False
    assert policy["outreach_authorized"] is False
    assert policy["allow_pii"] is False


def test_readiness_preserves_unresolved_fail_closed_controls() -> None:
    evidence = load_json(EVIDENCE_PATH)
    unresolved = set(evidence["unresolved_controls"])

    assert {
        "EXACT_DOWNLOAD_URLS",
        "REDIRECT_CHAIN",
        "ACTUAL_MEDIA_TYPE",
        "CURRENT_FILE_SIZE",
        "MAX_BYTES",
        "TIMEOUT_SECONDS",
        "ROW_LAYOUT",
        "PROCESSING_PURPOSE",
        "DATA_CATEGORIES",
        "ALLOWED_FIELDS",
        "PII_NECESSITY",
        "RETENTION_POLICY",
        "TRUSTED_PROJECT_PRIVACY_POLICY",
        "APPROVAL_REFERENCE",
    }.issubset(unresolved)

    transport = evidence["transport_verification"]
    data_scope = evidence["data_scope_verification"]

    assert isinstance(transport, dict)
    assert isinstance(data_scope, dict)
    assert not any(bool(value) for value in transport.values())
    assert not any(bool(value) for value in data_scope.values())
