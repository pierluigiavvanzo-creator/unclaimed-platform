from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/source_approval_package.schema.json"
EXAMPLES_PATH = ROOT / "schemas/examples/ca_sco_source_approval_package.examples.json"
PACKAGE_PATH = (
    ROOT
    / "sources/proposals/ca_sco_unclaimed_property_bulk.source_approval_package.v1.json"
)
POLICY_PATH = (
    ROOT
    / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
TRANSPORT_EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    / "ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json"
)
SOURCE_ID = "ca.sco.unclaimed_property.bulk"


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_package_is_schema_valid_and_non_authorizing() -> None:
    package = load_json(PACKAGE_PATH)
    validator().validate(package)

    assert package["package_status"] == "READINESS_PROPOSAL_NOT_AUTHORIZED"
    assert package["source_approved"] is False
    assert package["source_enabled"] is False
    assert package["real_acquisition_authorized"] is False
    assert package["network_request_performed"] is False
    assert package["body_access_performed"] is False


def test_schema_rejects_source_approval_claim() -> None:
    examples = load_json(EXAMPLES_PATH)
    validator().validate(examples["package.valid"])

    with pytest.raises(ValidationError):
        validator().validate(examples["package.invalid_authorizes_source"])


def test_schema_rejects_unverified_record_level_field() -> None:
    examples = load_json(EXAMPLES_PATH)
    mutated = deepcopy(examples["package.valid"])
    processing = mutated["proposed_processing"]
    assert isinstance(processing, dict)
    field_scope = processing["field_scope"]
    assert isinstance(field_scope, dict)
    field_scope["proposed_allowed_fields"] = ["synthetic_unverified_field"]

    with pytest.raises(ValidationError):
        validator().validate(mutated)


def test_transport_proposal_is_derived_from_canonical_observation() -> None:
    package = load_json(PACKAGE_PATH)
    evidence = load_json(TRANSPORT_EVIDENCE_PATH)

    proposed = package["proposed_transport"]
    assert isinstance(proposed, dict)

    endpoint_discovery = evidence["endpoint_discovery"]
    transport = evidence["transport"]
    controls = evidence["controls"]
    assert isinstance(endpoint_discovery, dict)
    assert isinstance(transport, dict)
    assert isinstance(controls, dict)

    assert package["source_id"] == evidence["source_id"] == SOURCE_ID
    assert proposed["observed_endpoint"] == endpoint_discovery["extracted_endpoint"]
    assert proposed["allowed_download_hosts"] == controls["allowlisted_hosts"]
    assert proposed["timeout_seconds"] == controls["timeout_seconds"]
    assert proposed["max_bytes"] == transport["content_length"]
    assert proposed["expected_media_types"] == [transport["content_type"]]
    assert transport["response_body_bytes_read"] == 0


def test_existing_policy_and_registry_remain_fail_closed() -> None:
    package = load_json(PACKAGE_PATH)
    policy = load_json(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))

    candidate = next(
        source for source in registry["sources"] if source["source_id"] == SOURCE_ID
    )

    assert package["source_id"] == policy["source_id"] == candidate["source_id"]
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["authorized_processing_purposes"] == []
    assert policy["authorized_data_categories"] == []
    assert policy["allowed_fields"] == []
    assert policy["allow_pii"] is False
    assert policy["approval_ref"] is None

    policy_transport = policy["transport"]
    assert policy_transport["allowed_download_hosts"] == []
    assert policy_transport["redirect_policy"] == "BLOCK_UNTIL_APPROVED"
    assert policy_transport["timeout_seconds"] is None
    assert policy_transport["max_bytes"] is None
    assert policy_transport["expected_media_types"] == []

    assert candidate["enabled"] is False
    assert candidate["approved_for_use"] is False


def test_data_scope_privacy_and_retention_blockers_are_explicit() -> None:
    package = load_json(PACKAGE_PATH)

    processing = package["proposed_processing"]
    privacy = package["proposed_privacy_retention"]
    requirements = package["approval_requirements"]
    decision = package["readiness_decision"]

    assert isinstance(processing, dict)
    assert isinstance(privacy, dict)
    assert isinstance(requirements, dict)
    assert isinstance(decision, dict)

    field_scope = processing["field_scope"]
    pii = processing["pii_necessity"]
    assert isinstance(field_scope, dict)
    assert isinstance(pii, dict)

    assert field_scope["mode"] == "BLOCK_UNTIL_ROW_SCHEMA_VERIFIED"
    assert field_scope["proposed_allowed_fields"] == []
    assert pii["status"] == "UNDETERMINED_BLOCKING"
    assert pii["allow_pii"] is False
    assert privacy["retention_policy_ref"] is None
    assert privacy["retention_duration_days"] is None
    assert privacy["trusted_project_privacy_policy_ref"] is None
    assert privacy["record_level_processing_allowed"] is False
    assert privacy["matching_allowed"] is False
    assert privacy["outreach_allowed"] is False

    required = set(requirements["required_before_approval"])
    assert {
        "ROW_LAYOUT_VERIFIED",
        "FIELD_WHITELIST_SELECTED",
        "PII_NECESSITY_DETERMINED",
        "RETENTION_POLICY_SELECTED",
        "TRUSTED_PROJECT_PRIVACY_POLICY_SELECTED",
        "REAL_ACQUISITION_CLIENT_REVIEWED",
        "APPROVAL_REFERENCE_ASSIGNED",
    } == required

    assert decision["status"] == "BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION"
    assert decision["next_gate"] == "HUMAN_SOURCE_APPROVAL_REVIEW"


def test_package_cannot_be_mutated_into_approval_under_v1_contract() -> None:
    package = load_json(PACKAGE_PATH)
    mutated = deepcopy(package)
    mutated["real_acquisition_authorized"] = True

    with pytest.raises(ValidationError):
        validator().validate(mutated)
