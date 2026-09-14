from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/source_field_privacy_readiness.schema.json"
PROPOSAL_PATH = (
    ROOT / "sources/proposals/ca_sco_segment_500_plus.field_privacy_readiness.v1.json"
)
EXAMPLES_PATH = (
    ROOT / "schemas/examples/ca_sco_500_plus_field_privacy_readiness.examples.json"
)
EVIDENCE_PATH = (
    ROOT / "sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
SOURCE_ID = "ca.sco.unclaimed_property.bulk"


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_readiness_proposal_is_valid_and_non_authorizing() -> None:
    proposal = load_json(PROPOSAL_PATH)
    validator().validate(proposal)

    assert proposal["package_status"] == "READINESS_PROPOSAL_NOT_AUTHORIZED"
    assert proposal["source_approved"] is False
    assert proposal["source_enabled"] is False
    assert proposal["real_acquisition_authorized"] is False
    assert proposal["network_request_performed"] is False
    assert proposal["body_access_performed"] is False

    future = proposal["future_row_contract"]
    assert isinstance(future, dict)
    assert future["status"] == "DRAFT_NOT_EXECUTABLE"
    assert future["row_access_authorized"] is False
    assert future["pii_processing_authorized"] is False


def test_valid_and_invalid_examples_behave_as_declared() -> None:
    examples = load_json(EXAMPLES_PATH)
    validator().validate(examples["proposal.valid"])

    with pytest.raises(ValidationError):
        validator().validate(examples["proposal.invalid_authorizes_source"])


def test_all_25_verified_fields_are_partitioned_exactly_once() -> None:
    proposal = load_json(PROPOSAL_PATH)
    evidence = load_json(EVIDENCE_PATH)

    header_candidates = evidence["csv_header_candidates"]
    assert isinstance(header_candidates, list)
    assert len(header_candidates) == 4
    first = header_candidates[0]
    assert isinstance(first, dict)
    verified = first["labels"]
    assert isinstance(verified, list)
    assert all(
        isinstance(candidate, dict) and candidate["labels"] == verified
        for candidate in header_candidates
    )

    field_scope = proposal["field_minimization"]
    assert isinstance(field_scope, dict)
    assert field_scope["verified_fields"] == verified
    assert field_scope["verified_field_count"] == 25

    groups = [
        field_scope["required_fields"],
        field_scope["optional_fields"],
        field_scope["prohibited_fields"],
        field_scope["unresolved_fields"],
    ]
    flattened = [field for group in groups for field in group]
    assert len(flattened) == 25
    assert len(set(flattened)) == 25
    assert set(flattened) == set(verified)


def test_minimized_triage_scope_contains_only_three_fields() -> None:
    proposal = load_json(PROPOSAL_PATH)
    field_scope = proposal["field_minimization"]
    assert isinstance(field_scope, dict)

    expected = ["PROPERTY_ID", "PROPERTY_TYPE", "HOLDER_NAME"]
    assert field_scope["required_fields"] == expected
    assert field_scope["future_row_allowed_fields"] == expected
    assert field_scope["optional_fields"] == []

    prohibited = set(field_scope["prohibited_fields"])
    assert {
        "OWNER_NAME",
        "OWNER_STREET_1",
        "OWNER_STREET_2",
        "OWNER_STREET_3",
        "OWNER_CITY",
        "OWNER_STATE",
        "OWNER_ZIP",
        "OWNER_COUNTRY_CODE",
        "HOLDER_STREET_1",
        "HOLDER_STREET_2",
        "HOLDER_STREET_3",
        "HOLDER_CITY",
        "HOLDER_STATE",
        "HOLDER_ZIP",
    }.issubset(prohibited)


def test_pii_retention_and_privacy_candidates_remain_unapproved() -> None:
    proposal = load_json(PROPOSAL_PATH)

    pii = proposal["pii_necessity"]
    assert isinstance(pii, dict)
    assert pii["actual_pii_presence_status"] == "UNVERIFIED_NO_ROWS_SAMPLED"
    assert pii["pii_processing_authorized"] is False
    assert pii["required_field_with_potential_pii"] == ["HOLDER_NAME"]

    retention = proposal["retention_candidate"]
    assert isinstance(retention, dict)
    assert retention["candidate_status"] == "DRAFT_NOT_APPROVED"
    assert retention["projected_triage_record_retention_days"] == 7
    assert retention["duration_basis"] == "PROJECT_SAFETY_CANDIDATE_NOT_LEGAL_REQUIREMENT"
    assert retention["approved_policy_ref"] is None

    privacy = proposal["privacy_policy_candidate"]
    assert isinstance(privacy, dict)
    assert privacy["candidate_status"] == "DRAFT_NOT_TRUSTED"
    assert privacy["trusted_policy_ref"] is None
    assert privacy["record_values_in_logs_allowed"] is False
    assert privacy["identity_resolution_allowed"] is False
    assert privacy["beneficiary_matching_allowed"] is False
    assert privacy["outreach_allowed"] is False


def test_source_policy_and_registry_are_unchanged_and_fail_closed() -> None:
    policy = load_json(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["privacy_policy_ref"] is None
    assert policy["retention_policy_ref"] is None
    assert policy["authorized_processing_purposes"] == []
    assert policy["allowed_fields"] == []
    assert policy["allow_pii"] is False

    candidate = next(
        source for source in registry["sources"] if source["source_id"] == SOURCE_ID
    )
    assert candidate["enabled"] is False
    assert candidate["approved_for_use"] is False


def test_schema_blocks_authorization_and_field_scope_widening() -> None:
    proposal = load_json(PROPOSAL_PATH)

    approved = copy.deepcopy(proposal)
    approved["real_acquisition_authorized"] = True
    with pytest.raises(ValidationError):
        validator().validate(approved)

    widened = copy.deepcopy(proposal)
    widened["future_row_contract"]["requested_fields"].append("OWNER_NAME")
    with pytest.raises(ValidationError):
        validator().validate(widened)

    trusted = copy.deepcopy(proposal)
    trusted["privacy_policy_candidate"]["trusted_policy_ref"] = "invented-policy"
    with pytest.raises(ValidationError):
        validator().validate(trusted)
