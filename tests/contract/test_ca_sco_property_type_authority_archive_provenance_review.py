from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_authority_archive_provenance_review.schema.json"
)
REVIEW_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_authority_archive_provenance.review.v1.json"
)
ARCHIVE_META_PATH = (
    ROOT / "sources/evidence/ca_sco_property_type_authority_archive.v1.json"
)
ARCHIVE_PATH = (
    ROOT
    / "sources/authority/ca/sco/upd_naupa_ii_codes_dormancy_periods/"
    "7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5.pdf"
)
PRIOR_REVIEW_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
TEMP_REVIEW_WORKFLOW_PATH = (
    ROOT / ".github/workflows/property-type-authority-provenance-review-offline.yml"
)
EXPECTED_ARCHIVE_SHA256 = (
    "7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5"
)
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"
EXPECTED_INSURANCE_CODES = [
    "IN01",
    "IN02",
    "IN03",
    "IN04",
    "IN05",
    "IN06",
    "IN07",
    "IN08",
    "IN99",
]


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _classification_map() -> dict[str, dict[str, object]]:
    review = _load(REVIEW_PATH)
    classifications = review["classifications"]
    assert isinstance(classifications, list)
    return {str(item["assumption_id"]): item for item in classifications}


def test_review_is_schema_valid_and_strictly_offline() -> None:
    review = _load(REVIEW_PATH)
    _validator().validate(review)

    assert review["review_status"] == (
        "COMPLETED_OFFLINE_ARCHIVE_PROVENANCE_REVIEW_FAIL_CLOSED"
    )
    assert review["review_scope"] == {
        "archived_authority_only": True,
        "authority_network_access_performed": False,
        "authority_retrieval_performed": False,
        "sco_dataset_access_performed": False,
        "claimit_access_performed": False,
        "source_row_access_performed": False,
        "source_value_reconstructed_or_inferred": False,
        "runner_modified": False,
        "parser_modified": False,
        "regex_modified": False,
        "normalization_modified": False,
        "third_real_execution_performed": False,
    }


def test_review_is_pinned_to_verified_immutable_archive() -> None:
    review = _load(REVIEW_PATH)
    authority = review["authority_archive"]
    assert isinstance(authority, dict)
    assert authority["sha256"] == EXPECTED_ARCHIVE_SHA256
    assert authority["body_bytes"] == 329585
    assert authority["page_count"] == 4
    assert authority["archival_run_id"] == 35012019831
    assert authority["one_shot_approval_state"] == "CONSUMED_NON_REUSABLE"

    assert ARCHIVE_PATH.exists()
    assert ARCHIVE_PATH.stat().st_size == 329585
    digest = hashlib.sha256(ARCHIVE_PATH.read_bytes()).hexdigest()
    assert digest == EXPECTED_ARCHIVE_SHA256

    archive_meta = _load(ARCHIVE_META_PATH)
    assert archive_meta["sha256"] == EXPECTED_ARCHIVE_SHA256
    assert archive_meta["body_bytes"] == 329585
    assert archive_meta["semantic_extraction_performed"] is False


def test_all_four_pages_were_reviewed_after_archive_verification() -> None:
    method = _load(REVIEW_PATH)["review_method"]
    assert isinstance(method, dict)
    assert method == {
        "archive_sha256_verified": True,
        "archive_size_verified": True,
        "text_extraction_used_as_helper": True,
        "all_pages_rendered": True,
        "all_pages_visually_reviewed": True,
        "pages_reviewed": [1, 2, 3, 4],
        "offline_extractor_run_id": 35013189623,
    }
    assert not TEMP_REVIEW_WORKFLOW_PATH.exists()


def test_general_shape_is_supported_only_with_scope_boundary() -> None:
    item = _classification_map()["GENERAL_CODE_SHAPE_AA99"]
    assert item["status"] == "SUPPORTED_BY_ARCHIVED_AUTHORITY_WITH_SCOPE_BOUNDARY"
    assert item["authority_pages"] == [1, 2, 3]
    assert "arbitrary AA99" in str(item["proof_boundary"])
    assert "ASCII" in str(item["proof_boundary"])

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert EXPECTED_REGEX in runner_text

    decision = _load(REVIEW_PATH)["decision"]
    assert isinstance(decision, dict)
    assert decision["current_shape_regex_contradicted_by_authority"] is False
    assert decision["regex_change_authorized"] is False
    assert decision["regex_relaxation_authorized"] is False
    assert decision["trimming_authorized"] is False
    assert decision["uppercasing_authorized"] is False
    assert decision["normalization_authorized"] is False


def test_zzzz_is_directly_supported_by_archived_authority() -> None:
    item = _classification_map()["SPECIAL_CODE_ZZZZ"]
    assert item["status"] == "SUPPORTED_BY_ARCHIVED_AUTHORITY"
    assert item["authority_pages"] == [3]
    assert "ZZZZ" in str(item["authority_supported_statement"])
    assert "Properties Not Identified Above" in str(
        item["authority_supported_statement"]
    )


def test_insurance_code_set_is_directly_supported_by_archived_authority() -> None:
    item = _classification_map()["CALIFORNIA_INSURANCE_CODE_SET"]
    assert item["status"] == "SUPPORTED_BY_ARCHIVED_AUTHORITY"
    assert item["authority_pages"] == [1]
    supported = str(item["authority_supported_statement"])
    for code in EXPECTED_INSURANCE_CODES:
        assert code in supported

    prior = _load(PRIOR_REVIEW_PATH)
    prior_items = prior["classifications"]
    assert isinstance(prior_items, list)
    prior_insurance = next(
        entry
        for entry in prior_items
        if entry["assumption_id"] == "CALIFORNIA_INSURANCE_CODE_SET"
    )
    assert prior_insurance["status"] == (
        "REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED"
    )


def test_target_provenance_resolves_without_resolving_source_mismatch() -> None:
    review = _load(REVIEW_PATH)
    assert review["summary"] == {
        "supported_by_archived_authority": 2,
        "supported_by_archived_authority_with_scope_boundary": 1,
        "target_provenance_resolved": True,
        "source_semantic_mismatch_resolved": False,
    }

    decision = review["decision"]
    assert isinstance(decision, dict)
    assert decision["result"] == (
        "ARCHIVED_AUTHORITY_RESOLVES_TARGET_PROVENANCE_SOURCE_SEMANTIC_MISMATCH_REMAINS"
    )
    assert decision["authority_provenance_resolved"] is True
    assert decision["semantic_compatibility_resolved"] is False
    assert decision["source_value_classification_authorized"] is False
    assert decision["parser_change_authorized"] is False
    assert decision["third_real_execution_authorized"] is False
    assert decision["additional_authority_retrieval_authorized"] is False
    assert decision["source_approval_authorized"] is False


def test_downstream_safety_gates_remain_closed() -> None:
    review = _load(REVIEW_PATH)
    safety = review["safety_state"]
    assert isinstance(safety, dict)
    assert safety["source_policy_status"] == "PROPOSED"
    assert safety["registry_enabled"] is False
    assert safety["registry_approved_for_use"] is False
    assert safety["production_classification_active"] is False
    assert safety["identity_resolution_allowed"] is False
    assert safety["genealogy_allowed"] is False
    assert safety["beneficiary_matching_allowed"] is False
    assert safety["outreach_allowed"] is False
    assert safety["claim_submission_allowed"] is False
    assert safety["authority_archival_approval_reusable"] is False
    assert safety["prior_execution_privacy_approvals_reusable"] is False

    policy = _load(POLICY_PATH)
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False

    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    source = next(
        entry
        for entry in registry["sources"]
        if entry["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False


def test_next_step_is_a_new_human_decision_not_an_implicit_approval() -> None:
    next_step = _load(REVIEW_PATH)["next_step"]
    assert next_step == {
        "status": "SEPARATE_HUMAN_DECISION_REQUIRED",
        "recommended_action": (
            "DECIDE_WHETHER_TO_PREPARE_BOUNDED_PROPERTY_TYPE_DIAGNOSTIC_"
            "REMEDIATION_EVIDENCE_PROPOSAL"
        ),
        "proposal_preparation_authorized_by_this_review": False,
        "diagnostic_execution_authorized_by_this_review": False,
        "runtime_change_authorized_by_this_review": False,
        "approval_token_defined_by_this_review": False,
    }


def test_schema_rejects_silent_runtime_or_execution_authorization() -> None:
    review = _load(REVIEW_PATH)
    validator = _validator()

    regex_change = copy.deepcopy(review)
    regex_change["decision"]["regex_change_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(regex_change)

    source_classification = copy.deepcopy(review)
    source_classification["decision"]["source_value_classification_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(source_classification)

    third_execution = copy.deepcopy(review)
    third_execution["decision"]["third_real_execution_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(third_execution)

    new_retrieval = copy.deepcopy(review)
    new_retrieval["decision"]["additional_authority_retrieval_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(new_retrieval)
