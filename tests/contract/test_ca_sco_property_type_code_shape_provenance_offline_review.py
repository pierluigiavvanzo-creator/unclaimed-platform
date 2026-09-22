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
    "property_type_code_shape_provenance_offline_review.schema.json"
)
REVIEW_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json"
)
DATA_SCOPE_PATH = (
    ROOT / "sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json"
)
SEMANTIC_PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_semantic_verification.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
DIAGNOSIS_TEST_PATH = ROOT / "tests/unit/test_ca_sco_property_type_offline_diagnosis.py"
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"


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


def test_review_is_schema_valid_and_repository_only() -> None:
    review = _load(REVIEW_PATH)
    _validator().validate(review)

    assert review["review_status"] == "COMPLETED_OFFLINE_FAIL_CLOSED"
    scope = review["review_scope"]
    assert isinstance(scope, dict)
    assert scope == {
        "repository_only": True,
        "sco_network_access_performed": False,
        "sco_source_body_access_performed": False,
        "external_authority_lookup_performed": False,
        "authority_document_downloaded": False,
        "source_value_reconstructed_or_inferred": False,
        "runner_modified": False,
        "parser_modified": False,
        "regex_modified": False,
    }


def test_property_type_second_field_is_supported_by_retained_headers() -> None:
    review = _classification_map()
    item = review["PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1"]
    assert item["status"] == "SUPPORTED_BY_REPOSITORY_EVIDENCE"

    data_scope = _load(DATA_SCOPE_PATH)
    headers = data_scope["csv_header_candidates"]
    assert isinstance(headers, list)
    assert len(headers) == 4
    for header in headers:
        labels = header["labels"]
        assert header["column_count"] == 25
        assert labels[1] == "PROPERTY_TYPE"

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert "PROPERTY_TYPE_INDEX = 1" in runner_text


def test_general_shape_and_zzzz_fail_closed_on_provenance() -> None:
    review = _classification_map()
    assert review["GENERAL_CODE_SHAPE_AA99"]["status"] == "PROVENANCE_INSUFFICIENT"
    assert review["SPECIAL_CODE_ZZZZ"]["status"] == "PROVENANCE_INSUFFICIENT"

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert EXPECTED_REGEX in runner_text

    decision = _load(REVIEW_PATH)["decision"]
    assert isinstance(decision, dict)
    assert decision["regex_change_authorized"] is False
    assert decision["regex_relaxation_authorized"] is False
    assert decision["trimming_authorized"] is False
    assert decision["uppercasing_authorized"] is False
    assert decision["normalization_authorized"] is False


def test_insurance_code_set_remains_external_reference_not_archived() -> None:
    review = _classification_map()
    item = review["CALIFORNIA_INSURANCE_CODE_SET"]
    assert item["status"] == (
        "REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED"
    )

    semantic = _load(SEMANTIC_PROPOSAL_PATH)
    authority = semantic["authority_reference"]
    assert isinstance(authority, dict)
    assert authority["sco_naupa_codes_ref"].startswith("https://")
    assert authority["official_insurance_codes"] == [
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

    evidence_inputs = _load(REVIEW_PATH)["evidence_inputs"]
    assert isinstance(evidence_inputs, list)
    assert all(not str(ref).lower().endswith(".pdf") for ref in evidence_inputs)


def test_projector_support_is_bounded_to_committed_synthetic_matrix() -> None:
    review = _classification_map()
    item = review["CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY"]
    assert item["status"] == "SUPPORTED_BY_REPOSITORY_EVIDENCE"
    assert "must not be generalized" in str(item["proof_boundary"])

    diagnosis_test = DIAGNOSIS_TEST_PATH.read_text(encoding="utf-8")
    assert "test_projector_matches_stdlib_csv_on_privacy_safe_synthetic_matrix" in (
        diagnosis_test
    )
    for marker in (
        "first_field_commas",
        "first_field_quotes",
        "unrelated_embedded_newline",
        "later_commas_and_quotes",
        "unrelated_embedded_crlf",
        "quote_all",
    ):
        assert marker in diagnosis_test


def test_aggregate_decision_and_downstream_gates_remain_closed() -> None:
    review = _load(REVIEW_PATH)
    assert review["summary"] == {
        "supported_by_repository_evidence": 2,
        "repository_assertion_with_external_reference_not_archived": 1,
        "provenance_insufficient": 2,
    }

    decision = review["decision"]
    assert isinstance(decision, dict)
    assert decision["result"] == (
        "NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE"
    )
    assert decision["parser_change_authorized"] is False
    assert decision["third_real_execution_authorized"] is False
    assert decision["authority_network_access_authorized"] is False

    safety = review["safety_state"]
    assert isinstance(safety, dict)
    assert safety["semantic_compatibility_resolved"] is False
    assert safety["production_classification_active"] is False
    assert safety["identity_resolution_allowed"] is False
    assert safety["genealogy_allowed"] is False
    assert safety["beneficiary_matching_allowed"] is False
    assert safety["outreach_allowed"] is False
    assert safety["claim_submission_allowed"] is False
    assert safety["consumed_execution_privacy_approvals_reusable"] is False

    assert not WORKFLOW_PATH.exists()
    policy = _load(POLICY_PATH)
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False

    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    source = next(
        item
        for item in registry["sources"]
        if item["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False


def test_schema_rejects_network_or_semantic_authorization_invention() -> None:
    review = _load(REVIEW_PATH)
    validator = _validator()

    network = copy.deepcopy(review)
    network["review_scope"]["external_authority_lookup_performed"] = True
    with pytest.raises(ValidationError):
        validator.validate(network)

    regex_change = copy.deepcopy(review)
    regex_change["decision"]["regex_change_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(regex_change)

    third_execution = copy.deepcopy(review)
    third_execution["decision"]["third_real_execution_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(third_execution)
