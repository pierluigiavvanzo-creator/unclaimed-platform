from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/source_transport_preflight_proposal.schema.json"
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/ca_sco_unclaimed_property_bulk.transport_preflight.v1.json"
)
EXAMPLES_PATH = ROOT / "schemas/examples/ca_sco_transport_preflight_proposal.examples.json"
READINESS_PATH = (
    ROOT
    / "sources/evidence/ca_sco_unclaimed_property_bulk.approval_readiness.v1.json"
)
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


def test_transport_preflight_proposal_is_valid_and_non_executing() -> None:
    proposal = load_json(PROPOSAL_PATH)
    validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    assert proposal["network_execution_authorized"] is False
    assert proposal["network_request_performed"] is False
    assert proposal["acquisition_performed"] is False
    assert proposal["source_approved"] is False
    assert proposal["source_enabled"] is False


def test_schema_rejects_execution_acquisition_and_body_access() -> None:
    examples = load_json(EXAMPLES_PATH)
    valid = examples["proposal.valid"]
    validator().validate(valid)

    with pytest.raises(ValidationError):
        validator().validate(examples["proposal.invalid_authorizes_network"])

    request_claim = dict(valid)
    request_claim["network_request_performed"] = True
    with pytest.raises(ValidationError):
        validator().validate(request_claim)

    acquisition_claim = dict(valid)
    acquisition_claim["acquisition_performed"] = True
    with pytest.raises(ValidationError):
        validator().validate(acquisition_claim)

    body_access = dict(valid)
    body_access["execution_constraints"] = dict(valid["execution_constraints"])
    body_access["execution_constraints"]["response_body_bytes_allowed"] = 1
    with pytest.raises(ValidationError):
        validator().validate(body_access)


def test_proposal_matches_readiness_registry_and_policy() -> None:
    proposal = load_json(PROPOSAL_PATH)
    readiness = load_json(READINESS_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    policy = load_json(POLICY_PATH)

    candidate = next(
        source for source in registry["sources"] if source["source_id"] == SOURCE_ID
    )

    assert proposal["source_id"] == readiness["source_id"]
    assert proposal["source_id"] == candidate["source_id"] == policy["source_id"]
    assert proposal["official_source_page"] == readiness["official_source_page"]
    assert proposal["official_source_page"] == candidate["base_uri"]
    assert proposal["official_source_page"] == policy["official_source_page"]
    assert proposal["advertised_download_hosts"] == readiness["advertised_download_hosts"]

    assert candidate["enabled"] is False
    assert candidate["approved_for_use"] is False
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["beneficiary_matching_authorized"] is False
    assert policy["outreach_authorized"] is False
    assert policy["allow_pii"] is False


def test_proposal_requires_metadata_only_observations_and_provenance() -> None:
    proposal = load_json(PROPOSAL_PATH)
    observations = set(proposal["proposed_observations"])
    provenance = set(proposal["required_provenance_fields"])

    assert {
        "EXACT_ENDPOINT_IDENTITY",
        "REDIRECT_CHAIN",
        "HTTP_STATUS",
        "FINAL_HOST",
        "RESPONSE_HEADERS",
        "CONTENT_TYPE",
        "CONTENT_LENGTH",
        "TLS_SCHEME",
        "OBSERVED_AT",
    }.issubset(observations)

    assert {
        "SOURCE_ID",
        "OBSERVED_AT",
        "REQUESTED_ENDPOINT",
        "FINAL_ENDPOINT",
        "REDIRECT_HOPS",
        "HTTP_STATUS",
        "RESPONSE_HEADERS",
        "EXECUTION_APPROVAL_REF",
    }.issubset(provenance)


def test_execution_controls_remain_unresolved_and_fail_closed() -> None:
    proposal = load_json(PROPOSAL_PATH)
    constraints = proposal["execution_constraints"]
    unresolved = set(proposal["unresolved_execution_controls"])

    assert isinstance(constraints, dict)
    assert constraints["execution_approval_ref"] is None
    assert constraints["request_method"] is None
    assert constraints["timeout_seconds"] is None
    assert constraints["max_redirects"] is None
    assert constraints["allowlisted_hosts"] == []
    assert constraints["response_body_bytes_allowed"] == 0
    assert constraints["persist_response_body"] is False
    assert constraints["parse_response_body"] is False
    assert constraints["persist_dataset_artifact"] is False
    assert constraints["pii_processing_allowed"] is False
    assert constraints["beneficiary_matching_allowed"] is False
    assert constraints["outreach_allowed"] is False

    assert {
        "EXACT_ENDPOINT",
        "REQUEST_METHOD",
        "TIMEOUT_SECONDS",
        "MAX_REDIRECTS",
        "ALLOWLISTED_HOSTS",
        "EXECUTION_APPROVAL_REF",
        "OBSERVED_CONTENT_TYPE",
        "OBSERVED_CONTENT_LENGTH",
    }.issubset(unresolved)
