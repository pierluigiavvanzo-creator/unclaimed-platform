from __future__ import annotations

import json
import math
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_documented_width_quote_arbitration_offline_proposal.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_documented_width_quote_arbitration_offline_proposal.schema.json"
)
FIFTH_RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_execution_result.v1.json"
)
SIXTH_RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_execution_result.v1.json"
)
SIXTH_LOCAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_local_approval.v1.json"
)
SIXTH_PII = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_pii_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _wilson_lower_95(successes: int, total: int) -> float:
    proportion = successes / total
    z = 1.96
    denominator = 1 + (z * z / total)
    centre = (proportion + z * z / (2 * total)) / denominator
    half_width = (
        z
        * math.sqrt(
            proportion * (1 - proportion) / total
            + z * z / (4 * total * total)
        )
        / denominator
    )
    return centre - half_width


def test_remediated_proposal_validates_and_remains_offline_only() -> None:
    proposal = _load(PROPOSAL)
    Draft202012Validator(_load(SCHEMA)).validate(proposal)

    assert proposal["artifact_version"] == "1.1.0"
    assert proposal["status"] == "REMEDIATED_PROPOSED_NOT_IMPLEMENTED"
    scope = proposal["request_scope"]
    assert scope["repository_only"] is True
    assert scope["source_network_access_performed"] is False
    assert scope["download_performed"] is False
    assert scope["parser_modified"] is False
    assert scope["runtime_activated"] is False
    assert scope["seventh_attempt_prepared"] is False


def test_proposal_binds_fifth_and_sixth_structural_evidence() -> None:
    proposal = _load(PROPOSAL)
    evidence = proposal["evidence_basis"]
    fifth = _load(FIFTH_RESULT)
    sixth = _load(SIXTH_RESULT)

    fifth_diagnostic = fifth["structural_diagnostic"]
    assert fifth_diagnostic["physical_line_breaks_inside_quotes"] == 17_543
    assert fifth_diagnostic["raw_pipe_count"] == 228_072
    assert evidence["fifth_verified_identity"] == (
        "(17543 + 1) * 13 = 228072"
    )

    sixth_diagnostic = sixth["quote_dialect_diagnostic"]
    assert sixth["reason_code"] == "QUOTE_DIALECT_AMBIGUOUS"
    assert sixth_diagnostic["raw_field_count"] == 14
    assert sixth_diagnostic["quote_aware_field_count"] == 6
    assert sixth_diagnostic["raw_pipe_count"] == 13
    assert sixth_diagnostic["suppressed_pipe_count"] == 8
    assert sixth_diagnostic["ended_inside_quote"] is True


def test_review_remediation_separates_structure_from_source_truth() -> None:
    proposal = _load(PROPOSAL)
    remediation = proposal["review_remediation"]
    algorithm = proposal["proposed_algorithm"]

    assert remediation["reviewed_result"] == (
        "CHANGES_REQUIRED_BEFORE_IMPLEMENTATION"
    )
    assert remediation["source_authoritative_quote_semantics_still_unknown"] is True
    assert remediation["candidate_quote_interpretation_label"] == (
        "CANDIDATE_SAME_LINE_QUOTE_INTERPRETATION_NOT_OSC_SOURCE_TRUTH"
    )
    assert algorithm["quote_aware_interpretation"] == (
        "CANDIDATE_SAME_LINE_QUOTE_INTERPRETATION_NOT_OSC_SOURCE_TRUTH"
    )
    assert algorithm["source_wide_quote_dialect_inference_allowed"] is False


def test_statistical_policy_records_insufficient_discriminating_sample_and_raw_fallback() -> None:
    policy = _load(PROPOSAL)["statistical_resolution_policy"]
    evidence = policy["current_retained_evidence"]
    resolution = policy["current_resolution"]

    assert policy["policy_source"] == "PRODUCT_OWNER"
    assert policy["policy_is_source_authority"] is False
    assert policy["decision_threshold"] == pytest.approx(0.66)

    assert evidence["discriminating_record_count"] == 1
    assert evidence["raw_supported_record_count"] == 1
    assert evidence["candidate_quote_aware_supported_record_count"] == 0
    assert evidence["raw_point_estimate"] == pytest.approx(1.0)

    expected_lower = _wilson_lower_95(1, 1)
    assert evidence["raw_wilson_95_lower_bound"] == pytest.approx(
        expected_lower,
        abs=1e-10,
    )
    assert expected_lower < policy["decision_threshold"]
    assert evidence["decision_threshold_met_robustly"] is False
    assert evidence["statistical_probability_claim_about_osc_dialect_allowed"] is False

    assert resolution["threshold_met_robustly"] is False
    assert resolution["fallback_applied"] is True
    assert resolution["selected_candidate_interpretation"] == (
        "RAW_PIPE_WITH_DOUBLE_QUOTE_LITERAL"
    )
    assert resolution["source_truth_claimed"] is False


def test_decision_matrix_classifies_first_then_applies_current_owner_policy() -> None:
    proposal = _load(PROPOSAL)
    algorithm = proposal["proposed_algorithm"]
    matrix = {item["case_id"]: item for item in algorithm["decision_matrix"]}

    assert algorithm["mode_name"] == "DOCUMENTED_WIDTH_ARBITRATION"
    assert algorithm["physical_record_boundary"] == "LF_OR_CRLF_HARD_BOUNDARY"
    assert algorithm["quote_state_may_cross_physical_record_boundary"] is False

    assert matrix["STRUCTURE_EQUIVALENT"] == {
        "case_id": "STRUCTURE_EQUIVALENT",
        "condition": "RAW_14_AND_CANDIDATE_QUOTE_AWARE_14",
        "structural_classification": "EQUIVALENT_DOCUMENTED_WIDTH",
        "policy_resolution": "ACCEPT_EQUIVALENT_STRUCTURE",
    }
    assert matrix["RAW_WIDTH_ONLY"]["structural_classification"] == (
        "RAW_WIDTH_ONLY_DIALECT_UNRESOLVED"
    )
    assert matrix["RAW_WIDTH_ONLY"]["policy_resolution"] == (
        "ACCEPT_RAW_UNDER_CURRENT_OWNER_FALLBACK"
    )
    assert matrix["QUOTE_WIDTH_ONLY"]["structural_classification"] == (
        "QUOTE_WIDTH_ONLY_DIALECT_UNRESOLVED"
    )
    assert matrix["QUOTE_WIDTH_ONLY"]["policy_resolution"] == (
        "BLOCK_UNDER_CURRENT_RAW_OWNER_FALLBACK"
    )
    assert matrix["NO_DOCUMENTED_WIDTH"]["policy_resolution"] == (
        "BLOCK_FAIL_CLOSED"
    )


def test_synthetic_matrix_reflects_remediated_current_policy() -> None:
    cases = {
        item["case_id"]: item
        for item in _load(PROPOSAL)["synthetic_acceptance_matrix"]
    }

    sixth_shape = cases["SIXTH_SHAPE_OPEN_QUOTE_RAW_14"]
    assert sixth_shape["structural_classification"] == (
        "RAW_WIDTH_ONLY_DIALECT_UNRESOLVED"
    )
    assert sixth_shape["current_policy_outcome"] == (
        "ACCEPT_RAW_UNDER_CURRENT_OWNER_FALLBACK"
    )

    quoted_pipe = cases["SAME_LINE_QUOTED_PIPE"]
    assert quoted_pipe["structural_classification"] == (
        "QUOTE_WIDTH_ONLY_DIALECT_UNRESOLVED"
    )
    assert quoted_pipe["current_policy_outcome"] == (
        "BLOCK_UNDER_CURRENT_RAW_OWNER_FALLBACK"
    )

    open_quote = cases["QUOTE_AWARE_14_BUT_OPEN_AT_EOL"]
    assert open_quote["current_policy_outcome"] == "BLOCK_FAIL_CLOSED"


def test_sixth_approvals_remain_consumed_and_future_scan_is_not_authorized() -> None:
    for path in (SIXTH_LOCAL, SIXTH_PII):
        approval = _load(path)
        assert approval["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False

    proposal = _load(PROPOSAL)
    boundary = proposal["implementation_boundary"]
    observability = proposal["proposed_non_pii_observability"]
    no_grant = proposal["authorization_does_not_grant"]

    assert boundary["implementation_status"] == "NOT_IMPLEMENTED"
    assert boundary["statistical_policy_implementation_authorized"] is False
    assert boundary["full_file_structural_scan_authorized"] is False
    assert boundary["runner_change_authorized"] is False
    assert boundary["seventh_attempt_proposal_authorized"] is False
    assert boundary["source_access_allowed"] is False

    assert observability["future_full_file_structural_scan_proposed_not_authorized"] is True
    assert observability["future_scan_execution_authorized"] is False

    assert no_grant["parser_implementation"] is False
    assert no_grant["runtime_activation"] is False
    assert no_grant["statistical_scan_execution"] is False
    assert no_grant["seventh_attempt_preparation"] is False
    assert no_grant["seventh_attempt_execution"] is False
