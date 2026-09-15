from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/"
    "property_type_code_shape_provenance_offline_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.v1.json"
)
SECOND_EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json"
)
SECOND_APPROVAL_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_second_semantic_execution_approval.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
DIAGNOSIS_TEST_PATH = (
    ROOT / "tests/unit/test_ca_sco_property_type_offline_diagnosis.py"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
SOURCE_ID = "ca.sco.unclaimed_property.bulk"
EXPECTED_REVIEW_BASE = "9d0243987c843172fe46c971ead0bf3947098336"
EXPECTED_CANONICAL_BASE = "e97c1f62959f603bdd3df79538d4b70255594c70"
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_proposal_is_schema_valid_and_offline_only() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_OFFLINE_NOT_EXECUTED"
    scope = proposal["offline_review_scope"]
    state = proposal["implementation_state"]
    assert isinstance(scope, dict)
    assert isinstance(state, dict)
    assert scope["repository_only"] is True
    assert scope["sco_network_access_allowed"] is False
    assert scope["sco_source_body_access_allowed"] is False
    assert scope["authority_document_download_allowed"] is False
    assert scope["new_external_authority_lookup_allowed"] is False
    assert scope["source_value_reconstruction_allowed"] is False
    assert state["network_workflow_present"] is False
    assert state["proposal_performed_sco_request"] is False
    assert state["proposal_performed_source_body_access"] is False
    assert state["proposal_downloaded_authority_document"] is False
    assert state["proposal_executed_provenance_review"] is False


def test_proposal_is_pinned_to_second_execution_closure_and_canonical_runner() -> None:
    proposal = _load(PROPOSAL_PATH)
    review_base = proposal["review_base"]
    canonical = proposal["canonical_runner_base"]
    assert isinstance(review_base, dict)
    assert isinstance(canonical, dict)

    assert review_base["sha"] == EXPECTED_REVIEW_BASE
    assert review_base["second_execution_run"] == "34995672539"
    assert review_base["second_execution_schema_version"] == "1.1.0"
    assert canonical["sha"] == EXPECTED_CANONICAL_BASE
    assert canonical["runner_path"] == (
        "scripts/ca_sco_property_type_semantic_verification.py"
    )


def test_second_run_facts_and_consumed_approvals_are_not_reinterpreted() -> None:
    proposal = _load(PROPOSAL_PATH)
    execution = _load(SECOND_EVIDENCE_PATH)
    approval = _load(SECOND_APPROVAL_PATH)
    historical = proposal["historical_execution_state"]
    consumed = proposal["consumed_authorizations"]
    assert isinstance(historical, dict)
    assert isinstance(consumed, dict)

    assert historical["second_result"] == execution["semantic_result_status"]
    assert historical["second_stop_reason"] == execution["stop_reason"]
    assert historical["second_result"] == "STOPPED_FAIL_CLOSED"
    assert historical["second_stop_reason"] == "PROPERTY_TYPE_FORMAT_UNEXPECTED"
    assert historical["offending_source_value_persisted"] is False
    assert historical["offending_source_bytes_persisted"] is False
    assert historical["semantic_compatibility_resolved"] is False
    assert historical["third_execution_authorized"] is False

    assert consumed["execution_approval_ref"] == approval["execution_approval_ref"]
    assert consumed["privacy_approval_ref"] == approval["privacy_approval_ref"]
    assert consumed["single_use"] is True
    assert consumed["consumed"] is True
    assert consumed["reusable"] is False


def test_regex_is_recorded_but_no_semantic_or_parser_change_is_authorized() -> None:
    proposal = _load(PROPOSAL_PATH)
    forbidden = proposal["forbidden_changes"]
    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert isinstance(forbidden, dict)

    assert EXPECTED_REGEX in runner_text
    for key in (
        "regex_change_authorized",
        "regex_relaxation_authorized",
        "trimming_authorized",
        "uppercasing_authorized",
        "normalization_authorized",
        "parser_change_authorized",
        "logging_expansion_authorized",
        "privacy_expansion_authorized",
        "third_real_execution_authorized",
    ):
        assert forbidden[key] is False


def test_provenance_categories_fail_closed_and_keep_parser_claim_bounded() -> None:
    proposal = _load(PROPOSAL_PATH)
    classification = proposal["provenance_classification"]
    assumptions = proposal["assumptions_under_review"]
    diagnosis_text = DIAGNOSIS_TEST_PATH.read_text(encoding="utf-8")
    assert isinstance(classification, dict)
    assert isinstance(assumptions, list)

    assert classification["unknown_must_fail_closed_to"] == (
        "PROVENANCE_INSUFFICIENT"
    )
    assert (
        classification[
            "external_reference_without_retained_content_counts_as_direct_offline_proof"
        ]
        is False
    )
    statuses = classification["allowed_statuses"]
    assert statuses == [
        "SUPPORTED_BY_REPOSITORY_EVIDENCE",
        "REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED",
        "PROVENANCE_INSUFFICIENT",
    ]
    ids = {item["assumption_id"] for item in assumptions}
    assert ids == {
        "PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1",
        "GENERAL_CODE_SHAPE_AA99",
        "SPECIAL_CODE_ZZZZ",
        "CALIFORNIA_INSURANCE_CODE_SET",
        "CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY",
    }
    assert "test_projector_matches_stdlib_csv_on_privacy_safe_synthetic_matrix" in (
        diagnosis_text
    )


def test_network_workflow_and_downstream_gates_remain_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    safety = proposal["safety_state"]
    policy = _load(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    assert isinstance(safety, dict)

    assert not WORKFLOW_PATH.exists()
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["authorized_processing_purposes"] == []
    assert policy["allowed_fields"] == []
    assert policy["allow_pii"] is False

    source = next(
        item for item in registry["sources"] if item["source_id"] == SOURCE_ID
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False
    assert safety["approved_real_sources"] == 0
    assert safety["semantic_compatibility_resolved"] is False
    assert safety["production_classification_active"] is False
    assert safety["identity_resolution_allowed"] is False
    assert safety["genealogy_allowed"] is False
    assert safety["beneficiary_matching_allowed"] is False
    assert safety["outreach_allowed"] is False
    assert safety["claim_submission_allowed"] is False


def test_schema_blocks_network_reuse_and_contract_change_invention() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()

    network_enabled = copy.deepcopy(proposal)
    network_enabled["offline_review_scope"]["sco_network_access_allowed"] = True
    with pytest.raises(ValidationError):
        validator.validate(network_enabled)

    reused_approval = copy.deepcopy(proposal)
    reused_approval["consumed_authorizations"]["reusable"] = True
    with pytest.raises(ValidationError):
        validator.validate(reused_approval)

    regex_change = copy.deepcopy(proposal)
    regex_change["forbidden_changes"]["regex_change_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(regex_change)
