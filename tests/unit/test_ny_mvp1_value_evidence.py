import pytest
from pydantic import ValidationError

from unclaimed_platform.domain.ny_mvp1_value_evidence import (
    NyMvp1ExplicitCaseEconomicsInput,
    compute_explicit_case_economics,
    ny_mvp1_precontact_economics_evidence,
)


def test_precontact_economics_fails_closed_without_exact_value() -> None:
    evidence = ny_mvp1_precontact_economics_evidence()

    assert evidence.recoverable_value_state == "UNKNOWN_PRE_CLAIM_REVIEW"
    assert evidence.exact_recoverable_value_cents is None
    assert evidence.owner_file_discloses_amount is False
    assert evidence.actual_fee_bps is None
    assert evidence.expected_follow_up_cost_cents is None
    assert evidence.commercial_actionability == "NOT_COMPUTABLE_PRE_CONTACT"
    assert evidence.statutory_fee_cap_bps == 1500
    assert evidence.fee_applicability_requires_legal_review is True


def test_explicit_economics_computes_from_evidence_backed_integer_inputs() -> None:
    inputs = NyMvp1ExplicitCaseEconomicsInput(
        recoverable_value_cents=1_000_000,
        agreed_fee_bps=1500,
        measured_follow_up_cost_cents=50_000,
        value_evidence_ref="official-value-evidence",
        fee_evidence_ref="valid-fee-rate-evidence",
        cost_evidence_ref="measured-cost-evidence",
        fee_rule_scope_confirmed=True,
    )

    result = compute_explicit_case_economics(inputs)

    assert result.gross_fee_cents == 150_000
    assert result.contribution_before_overhead_cents == 100_000
    assert result.fee_cap_compliant is True
    assert result.no_commercial_recommendation is True


def test_explicit_economics_allows_non_positive_contribution_without_recommendation() -> None:
    inputs = NyMvp1ExplicitCaseEconomicsInput(
        recoverable_value_cents=10_000,
        agreed_fee_bps=1000,
        measured_follow_up_cost_cents=2_000,
        value_evidence_ref="official-value-evidence",
        fee_evidence_ref="valid-fee-rate-evidence",
        cost_evidence_ref="measured-cost-evidence",
        fee_rule_scope_confirmed=True,
    )

    result = compute_explicit_case_economics(inputs)

    assert result.gross_fee_cents == 1_000
    assert result.contribution_before_overhead_cents == -1_000
    assert result.no_commercial_recommendation is True


def test_fee_above_statutory_cap_is_rejected() -> None:
    with pytest.raises(ValidationError):
        NyMvp1ExplicitCaseEconomicsInput(
            recoverable_value_cents=100_000,
            agreed_fee_bps=1501,
            measured_follow_up_cost_cents=0,
            value_evidence_ref="value",
            fee_evidence_ref="fee",
            cost_evidence_ref="cost",
            fee_rule_scope_confirmed=True,
        )


def test_unconfirmed_fee_rule_scope_is_rejected() -> None:
    with pytest.raises(ValidationError):
        NyMvp1ExplicitCaseEconomicsInput(
            recoverable_value_cents=100_000,
            agreed_fee_bps=1000,
            measured_follow_up_cost_cents=0,
            value_evidence_ref="value",
            fee_evidence_ref="fee",
            cost_evidence_ref="cost",
            fee_rule_scope_confirmed=False,
        )
