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
    "property_type_authority_provenance_acquisition_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_authority_provenance_acquisition.v1.json"
)
REVIEW_EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json"
)
SEMANTIC_PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_semantic_verification.v1.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
SOURCE_ID = "ca.sco.unclaimed_property.bulk"
EXPECTED_BASE = "dba496d254e94a68f7f74e0b53090cfef972a969"
EXPECTED_REVIEW_SHA = "b274e9db0a28dae1c9f6a1a25c657978dd27d7b4"
EXPECTED_AUTHORITY_URL = (
    "https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf"
)
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_proposal_is_schema_valid_and_not_authorized() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    network = proposal["network_boundary"]
    state = proposal["implementation_state"]
    assert isinstance(network, dict)
    assert isinstance(state, dict)
    assert network["authority_network_access_authorized_by_this_proposal"] is False
    assert state["authority_request_performed"] is False
    assert state["authority_document_downloaded"] is False
    assert state["authority_archive_created"] is False
    assert state["network_workflow_created"] is False
    assert state["semantic_execution_performed"] is False


def test_base_is_pinned_to_verified_offline_review() -> None:
    proposal = _load(PROPOSAL_PATH)
    base = proposal["base_state"]
    assert isinstance(base, dict)
    assert base["head_sha"] == EXPECTED_BASE
    assert base["offline_review_result_sha"] == EXPECTED_REVIEW_SHA
    assert base["offline_review_ci"] == "35003900554"
    assert base["offline_review_decision"] == (
        "NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE"
    )


def test_exactly_one_preexisting_authority_target_is_used() -> None:
    proposal = _load(PROPOSAL_PATH)
    semantic = _load(SEMANTIC_PROPOSAL_PATH)
    targets = proposal["authority_targets"]
    assert isinstance(targets, list)
    assert len(targets) == 1
    target = targets[0]
    assert target["canonical_url"] == EXPECTED_AUTHORITY_URL
    assert (
        semantic["authority_reference"]["sco_naupa_codes_ref"]
        == EXPECTED_AUTHORITY_URL
    )
    assert target["host"] == "www.sco.ca.gov"
    assert target["retrieval_method"] == "GET"
    assert target["document_scope"] == "SINGLE_PDF_ONLY"
    assert target["page_scope"] == "ALL_PAGES_OF_SINGLE_PDF"


def test_network_boundary_is_single_get_fail_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    network = proposal["network_boundary"]
    assert isinstance(network, dict)
    assert network["allowed_hosts_if_later_approved"] == ["www.sco.ca.gov"]
    assert network["allowed_methods_if_later_approved"] == ["GET"]
    assert network["exact_url_only"] is True
    assert network["redirects_allowed"] is False
    assert network["query_parameters_allowed"] is False
    assert network["authentication_allowed"] is False
    assert network["cookies_required_or_allowed"] is False
    assert network["requests_max_total"] == 1
    assert network["retries_max"] == 0
    assert network["response_body_bytes_max"] == 16777216
    assert network["claimit_ca_gov_access_allowed"] is False
    assert network["source_data_access_allowed"] is False


def test_unresolved_claims_match_verified_review() -> None:
    proposal = _load(PROPOSAL_PATH)
    review = _load(REVIEW_EVIDENCE_PATH)
    expected = {
        item["assumption_id"]: item["status"]
        for item in review["classifications"]
        if item["assumption_id"]
        in {
            "GENERAL_CODE_SHAPE_AA99",
            "SPECIAL_CODE_ZZZZ",
            "CALIFORNIA_INSURANCE_CODE_SET",
        }
    }
    actual = {
        item["assumption_id"]: item["current_status"]
        for item in proposal["unresolved_provenance_claims"]
    }
    assert actual == expected


def test_archival_contract_requires_immutable_sha256_and_post_review() -> None:
    proposal = _load(PROPOSAL_PATH)
    archive = proposal["archival_contract"]
    semantic = proposal["semantic_boundary"]
    assert isinstance(archive, dict)
    assert isinstance(semantic, dict)
    assert archive[
        "raw_authority_document_persistence_required_if_later_approved"
    ] is True
    assert archive["raw_document_immutable"] is True
    assert archive["hash_algorithm"] == "SHA-256"
    assert "{sha256}.pdf" in archive["archive_path_template"]
    assert archive["pdf_magic_required"] is True
    assert archive["semantic_extraction_during_retrieval_allowed"] is False
    assert archive["runtime_contract_change_during_retrieval_allowed"] is False
    assert archive["post_archive_review_required_before_semantic_use"] is True
    assert semantic["authority_archive_itself_proves_claims"] is False
    assert semantic["claims_require_post_archive_human_review"] is True


def test_consumed_approvals_and_runtime_semantics_remain_untouched() -> None:
    proposal = _load(PROPOSAL_PATH)
    consumed = proposal["consumed_authorizations"]
    forbidden = proposal["forbidden_actions"]
    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert isinstance(consumed, dict)
    assert isinstance(forbidden, dict)

    assert consumed["consumed"] is True
    assert consumed["reusable"] is False
    assert consumed["used_by_authority_acquisition"] is False
    assert EXPECTED_REGEX in runner_text
    for key in (
        "authority_retrieval_before_human_review",
        "additional_authority_discovery",
        "sco_dataset_access",
        "third_semantic_execution",
        "source_value_reconstruction",
        "runner_change",
        "parser_change",
        "regex_change",
        "regex_relaxation",
        "trimming",
        "uppercasing",
        "normalization",
        "logging_expansion",
        "privacy_expansion",
        "source_approval",
        "registry_activation",
        "production_classification_activation",
    ):
        assert forbidden[key] is True


def test_downstream_gates_remain_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    safety = proposal["safety_state"]
    policy = _load(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    assert isinstance(safety, dict)

    assert not WORKFLOW_PATH.exists()
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
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


def test_schema_blocks_silent_authorization_or_scope_widening() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()

    enabled = copy.deepcopy(proposal)
    enabled["network_boundary"][
        "authority_network_access_authorized_by_this_proposal"
    ] = True
    with pytest.raises(ValidationError):
        validator.validate(enabled)

    widened = copy.deepcopy(proposal)
    widened["network_boundary"]["requests_max_total"] = 2
    with pytest.raises(ValidationError):
        validator.validate(widened)

    redirect = copy.deepcopy(proposal)
    redirect["network_boundary"]["redirects_allowed"] = True
    with pytest.raises(ValidationError):
        validator.validate(redirect)

    reuse = copy.deepcopy(proposal)
    reuse["consumed_authorizations"]["reusable"] = True
    with pytest.raises(ValidationError):
        validator.validate(reuse)
