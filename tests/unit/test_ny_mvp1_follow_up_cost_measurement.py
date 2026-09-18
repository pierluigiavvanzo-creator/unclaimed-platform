from datetime import UTC, datetime
from uuid import UUID

import pytest
from pydantic import ValidationError

from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    DocumentedHumanLaborRate,
    MeasuredCostComponent,
    NyMvp1FollowUpCostMeasurementInput,
    NyMvp1FollowUpCostMeasurementResult,
    measure_follow_up_cost,
)

_MEASUREMENT_ID = UUID("11111111-1111-4111-8111-111111111111")
_CASE_ID = UUID("22222222-2222-4222-8222-222222222222")
_OBSERVED_AT = datetime(2026, 9, 18, 8, 0, tzinfo=UTC)


def _input(
    *,
    labor_rate: DocumentedHumanLaborRate | None = None,
) -> NyMvp1FollowUpCostMeasurementInput:
    return NyMvp1FollowUpCostMeasurementInput(
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
        human_labor_rate=labor_rate,
    )


def test_measured_components_stay_separate_without_labor_rate() -> None:
    result = measure_follow_up_cost(_input())

    assert result.automated_processing_cost_cents == 37
    assert result.source_data_cost_cents == 0
    assert result.direct_machine_and_data_cost_cents == 37
    assert result.human_review_seconds == 125
    assert result.manual_research_seconds == 65
    assert result.total_human_seconds == 190
    assert result.human_labor_rate_state == "NOT_PROVIDED"
    assert result.human_labor_cost_cents is None
    assert result.fully_loaded_follow_up_cost_state == "NOT_COMPUTABLE_NO_LABOR_RATE"
    assert result.fully_loaded_follow_up_cost_cents is None
    assert result.no_commercial_recommendation is True


def test_documented_labor_rate_enables_fully_loaded_cost() -> None:
    rate = DocumentedHumanLaborRate(
        cents_per_hour=7200,
        currency="USD",
        evidence_ref="synthetic:labor-rate",
        observed_at=_OBSERVED_AT,
    )

    result = measure_follow_up_cost(_input(labor_rate=rate))

    assert result.human_labor_rate_state == "DOCUMENTED"
    assert result.human_labor_rate_cents_per_hour == 7200
    assert result.human_labor_cost_cents == 380
    assert result.fully_loaded_follow_up_cost_cents == 417
    assert result.evidence_refs[-1] == "synthetic:labor-rate"


def test_negative_measurement_is_rejected() -> None:
    with pytest.raises(ValidationError):
        MeasuredCostComponent(
            amount_cents=-1,
            currency="USD",
            measurement_method="SYSTEM_METERED",
            allocation_basis="PER_CANDIDATE_DIRECT",
            evidence_ref="synthetic:bad",
            observed_at=_OBSERVED_AT,
        )


def test_zero_direct_cost_marker_requires_zero_amount_and_matching_basis() -> None:
    with pytest.raises(ValidationError, match="documented zero direct cost"):
        MeasuredCostComponent(
            amount_cents=1,
            currency="USD",
            measurement_method="ZERO_DIRECT_COST_DOCUMENTED",
            allocation_basis="ZERO_DIRECT_COST_PER_CANDIDATE",
            evidence_ref="synthetic:bad-zero",
            observed_at=_OBSERVED_AT,
        )

    with pytest.raises(ValidationError, match="must agree"):
        MeasuredCostComponent(
            amount_cents=0,
            currency="USD",
            measurement_method="ZERO_DIRECT_COST_DOCUMENTED",
            allocation_basis="PER_CANDIDATE_DIRECT",
            evidence_ref="synthetic:bad-basis",
            observed_at=_OBSERVED_AT,
        )


def test_owner_pii_flag_cannot_be_enabled() -> None:
    payload = _input().model_dump()
    payload["owner_pii_included"] = True

    with pytest.raises(ValidationError):
        NyMvp1FollowUpCostMeasurementInput.model_validate(payload)


def test_result_rejects_inconsistent_aggregate() -> None:
    result = measure_follow_up_cost(_input()).model_dump()
    result["direct_machine_and_data_cost_cents"] = 999

    with pytest.raises(ValidationError, match="component sum"):
        NyMvp1FollowUpCostMeasurementResult.model_validate(result)


def test_synthetic_fixture_values_are_not_defaulted() -> None:
    schema = NyMvp1FollowUpCostMeasurementInput.model_json_schema()

    assert "default" not in schema["$defs"]["MeasuredCostComponent"]["properties"]["amount_cents"]
    assert "default" not in schema["$defs"]["MeasuredDurationComponent"]["properties"]["duration_seconds"]
