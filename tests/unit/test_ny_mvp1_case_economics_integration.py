from datetime import UTC, datetime
from uuid import UUID

import pytest
from pydantic import ValidationError

from unclaimed_platform.domain.ny_mvp1_case_economics_integration import (
    NyMvp1CaseEconomicsIntegrationInput,
    NyMvp1CaseEconomicsIntegrationResult,
    integrate_follow_up_cost_with_case_economics,
)
from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    DocumentedHumanLaborRate,
    NyMvp1FollowUpCostMeasurementInput,
    measure_follow_up_cost,
)

_MEASUREMENT_ID = UUID("11111111-1111-4111-8111-111111111111")
_CASE_ID = UUID("22222222-2222-4222-8222-222222222222")
_OBSERVED_AT = datetime(2026, 9, 18, 10, 0, tzinfo=UTC)


def _economics_input() -> NyMvp1CaseEconomicsIntegrationInput:
    return NyMvp1CaseEconomicsIntegrationInput(
        recoverable_value_cents=1_000_000,
        agreed_fee_bps=1200,
        value_evidence_ref="synthetic:value-evidence",
        fee_evidence_ref="synthetic:fee-evidence",
        fee_rule_scope_confirmed=True,
    )


def _follow_up_cost(*, with_labor_rate: bool):
    rate = None
    if with_labor_rate:
        rate = DocumentedHumanLaborRate(
            cents_per_hour=7200,
            currency="USD",
            evidence_ref="synthetic:labor-rate",
            observed_at=_OBSERVED_AT,
        )

    measured = NyMvp1FollowUpCostMeasurementInput(
        mode="SYNTHETIC_TEST",
        measurement_id=_MEASUREMENT_ID,
        candidate_case_id=_CASE_ID,
        owner_pii_included=False,
        automated_processing={
            "amount_cents": 37,
            "currency": "USD",
            "measurement_method": "SYSTEM_METERED",
            "allocation_basis": "PER_CANDIDATE_DIRECT",
            "evidence_ref": "synthetic:automation-meter",
            "observed_at": _OBSERVED_AT,
        },
        source_data={
            "amount_cents": 0,
            "currency": "USD",
            "measurement_method": "ZERO_DIRECT_COST_DOCUMENTED",
            "allocation_basis": "ZERO_DIRECT_COST_PER_CANDIDATE",
            "evidence_ref": "synthetic:source-cost",
            "observed_at": _OBSERVED_AT,
        },
        human_review={
            "duration_seconds": 125,
            "measurement_method": "REVIEWER_TIMER",
            "evidence_ref": "synthetic:review-timer",
            "observed_at": _OBSERVED_AT,
        },
        manual_research={
            "duration_seconds": 65,
            "measurement_method": "MANUAL_TIMER",
            "evidence_ref": "synthetic:research-timer",
            "observed_at": _OBSERVED_AT,
        },
        human_labor_rate=rate,
    )
    return measure_follow_up_cost(measured)


def test_missing_labor_rate_blocks_economics_and_does_not_substitute_direct_cost() -> None:
    follow_up = _follow_up_cost(with_labor_rate=False)

    result = integrate_follow_up_cost_with_case_economics(
        _economics_input(),
        follow_up,
    )

    assert follow_up.direct_machine_and_data_cost_cents == 37
    assert result.integration_state == "BLOCKED_FOLLOW_UP_COST_UNAVAILABLE"
    assert result.measured_follow_up_cost_cents is None
    assert result.explicit_economics_input is None
    assert result.explicit_economics_result is None
    assert result.follow_up_cost_evidence_refs == follow_up.evidence_refs
    assert result.no_commercial_recommendation is True


def test_fully_loaded_cost_populates_existing_explicit_economics_contract() -> None:
    follow_up = _follow_up_cost(with_labor_rate=True)

    result = integrate_follow_up_cost_with_case_economics(
        _economics_input(),
        follow_up,
    )

    assert follow_up.fully_loaded_follow_up_cost_cents == 417
    assert result.integration_state == "READY_FOR_EXPLICIT_ECONOMICS"
    assert result.measured_follow_up_cost_cents == 417
    assert result.explicit_economics_input is not None
    assert result.explicit_economics_result is not None
    assert result.explicit_economics_input.measured_follow_up_cost_cents == 417
    assert result.explicit_economics_result.measured_follow_up_cost_cents == 417
    assert result.explicit_economics_result.gross_fee_cents == 120_000
    assert result.explicit_economics_result.contribution_before_overhead_cents == 119_583
    assert result.follow_up_cost_evidence_refs == follow_up.evidence_refs
    assert result.explicit_economics_input.cost_evidence_ref == (
        "follow-up-cost-measurement:11111111-1111-4111-8111-111111111111"
    )


def test_fee_above_cap_is_rejected_before_integration() -> None:
    with pytest.raises(ValidationError):
        NyMvp1CaseEconomicsIntegrationInput(
            recoverable_value_cents=1_000_000,
            agreed_fee_bps=1501,
            value_evidence_ref="value",
            fee_evidence_ref="fee",
            fee_rule_scope_confirmed=True,
        )


def test_blocked_result_rejects_direct_cost_as_fake_fully_loaded_cost() -> None:
    follow_up = _follow_up_cost(with_labor_rate=False)
    result = integrate_follow_up_cost_with_case_economics(
        _economics_input(),
        follow_up,
    ).model_dump()

    result["measured_follow_up_cost_cents"] = follow_up.direct_machine_and_data_cost_cents

    with pytest.raises(ValidationError, match="blocked integration cannot expose"):
        NyMvp1CaseEconomicsIntegrationResult.model_validate(result)
