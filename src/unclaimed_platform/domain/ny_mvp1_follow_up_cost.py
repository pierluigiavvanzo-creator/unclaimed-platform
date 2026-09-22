"""Deterministic NY MVP-1 follow-up cost measurement contracts."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal
from typing import Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator


class MeasuredCostComponent(BaseModel):
    """A documented per-candidate monetary cost component."""

    model_config = ConfigDict(frozen=True)

    amount_cents: int = Field(ge=0)
    currency: Literal["USD"]
    measurement_method: Literal[
        "SYSTEM_METERED",
        "INVOICE_ALLOCATED",
        "RATE_CARD_ALLOCATED",
        "ZERO_DIRECT_COST_DOCUMENTED",
        "OTHER_DOCUMENTED",
    ]
    allocation_basis: Literal[
        "PER_CANDIDATE_DIRECT",
        "BATCH_ALLOCATED_PER_CANDIDATE",
        "ZERO_DIRECT_COST_PER_CANDIDATE",
    ]
    evidence_ref: str = Field(min_length=1)
    observed_at: AwareDatetime

    @model_validator(mode="after")
    def validate_zero_cost_markers(self) -> MeasuredCostComponent:
        zero_method = self.measurement_method == "ZERO_DIRECT_COST_DOCUMENTED"
        zero_basis = self.allocation_basis == "ZERO_DIRECT_COST_PER_CANDIDATE"
        if zero_method != zero_basis:
            raise ValueError("zero direct cost method and allocation basis must agree")
        if zero_method and self.amount_cents != 0:
            raise ValueError("documented zero direct cost must have amount_cents=0")
        return self


class MeasuredDurationComponent(BaseModel):
    """A documented per-candidate human-effort duration."""

    model_config = ConfigDict(frozen=True)

    duration_seconds: int = Field(ge=0)
    measurement_method: Literal[
        "SYSTEM_TIMER",
        "REVIEWER_TIMER",
        "MANUAL_TIMER",
        "OTHER_DOCUMENTED",
    ]
    evidence_ref: str = Field(min_length=1)
    observed_at: AwareDatetime


class DocumentedHumanLaborRate(BaseModel):
    """Optional documented labor rate; never inferred from duration alone."""

    model_config = ConfigDict(frozen=True)

    cents_per_hour: int = Field(ge=0)
    currency: Literal["USD"]
    evidence_ref: str = Field(min_length=1)
    observed_at: AwareDatetime


class NyMvp1FollowUpCostMeasurementInput(BaseModel):
    """Explicit measured inputs; contains no owner PII or assumed defaults."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_TEST", "MEASURED_WORKFLOW"]
    measurement_id: UUID
    candidate_case_id: UUID
    owner_pii_included: Literal[False]
    automated_processing: MeasuredCostComponent
    source_data: MeasuredCostComponent
    human_review: MeasuredDurationComponent
    manual_research: MeasuredDurationComponent
    human_labor_rate: DocumentedHumanLaborRate | None = None


class NyMvp1FollowUpCostMeasurementResult(BaseModel):
    """Aggregated deterministic measurement result without business recommendation."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    measurement_id: UUID
    candidate_case_id: UUID
    currency: Literal["USD"] = "USD"
    automated_processing_cost_cents: int = Field(ge=0)
    source_data_cost_cents: int = Field(ge=0)
    direct_machine_and_data_cost_cents: int = Field(ge=0)
    human_review_seconds: int = Field(ge=0)
    manual_research_seconds: int = Field(ge=0)
    total_human_seconds: int = Field(ge=0)
    human_labor_rate_state: Literal[
        "NOT_PROVIDED",
        "DOCUMENTED",
    ]
    human_labor_rate_cents_per_hour: int | None = Field(default=None, ge=0)
    human_labor_cost_state: Literal[
        "NOT_COMPUTED_NO_RATE",
        "COMPUTED_FROM_DOCUMENTED_RATE",
    ]
    human_labor_cost_cents: int | None = Field(default=None, ge=0)
    fully_loaded_follow_up_cost_state: Literal[
        "NOT_COMPUTABLE_NO_LABOR_RATE",
        "COMPUTED_FROM_MEASURED_COMPONENTS",
    ]
    fully_loaded_follow_up_cost_cents: int | None = Field(default=None, ge=0)
    evidence_refs: tuple[str, ...] = Field(min_length=4)
    owner_pii_included: Literal[False]
    no_commercial_recommendation: Literal[True]

    @model_validator(mode="after")
    def validate_aggregates_and_states(self) -> NyMvp1FollowUpCostMeasurementResult:
        if self.direct_machine_and_data_cost_cents != (
            self.automated_processing_cost_cents + self.source_data_cost_cents
        ):
            raise ValueError("direct machine/data cost does not equal component sum")
        if self.total_human_seconds != self.human_review_seconds + self.manual_research_seconds:
            raise ValueError("total human seconds does not equal component sum")

        if self.human_labor_rate_state == "NOT_PROVIDED":
            if self.human_labor_rate_cents_per_hour is not None:
                raise ValueError("labor rate value present while rate state is NOT_PROVIDED")
            if self.human_labor_cost_state != "NOT_COMPUTED_NO_RATE":
                raise ValueError("labor cost state must fail closed without a rate")
            if self.human_labor_cost_cents is not None:
                raise ValueError("labor cost cannot exist without a documented rate")
            if self.fully_loaded_follow_up_cost_state != "NOT_COMPUTABLE_NO_LABOR_RATE":
                raise ValueError("fully loaded cost must remain unavailable without a labor rate")
            if self.fully_loaded_follow_up_cost_cents is not None:
                raise ValueError("fully loaded cost cannot exist without a labor rate")
        else:
            if self.human_labor_rate_cents_per_hour is None:
                raise ValueError("documented labor rate state requires a rate value")
            if self.human_labor_cost_state != "COMPUTED_FROM_DOCUMENTED_RATE":
                raise ValueError("labor cost state must reflect documented rate")
            if self.human_labor_cost_cents is None:
                raise ValueError("documented labor rate requires computed labor cost")
            if self.fully_loaded_follow_up_cost_state != "COMPUTED_FROM_MEASURED_COMPONENTS":
                raise ValueError("fully loaded state must reflect measured components")
            if self.fully_loaded_follow_up_cost_cents != (
                self.direct_machine_and_data_cost_cents + self.human_labor_cost_cents
            ):
                raise ValueError("fully loaded cost does not equal component sum")
        return self


def _round_cents(value: Decimal) -> int:
    return int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def _human_labor_cost_cents(total_seconds: int, cents_per_hour: int) -> int:
    raw = Decimal(total_seconds) * Decimal(cents_per_hour) / Decimal(3600)
    return _round_cents(raw)


def measure_follow_up_cost(
    inputs: NyMvp1FollowUpCostMeasurementInput,
) -> NyMvp1FollowUpCostMeasurementResult:
    """Aggregate measured per-candidate costs/times and optional documented labor rate."""

    if inputs.automated_processing.currency != inputs.source_data.currency:
        raise ValueError("monetary cost components must use the same currency")
    if inputs.automated_processing.currency != "USD":
        raise ValueError("NY MVP-1 follow-up cost contract currently requires USD")
    if inputs.human_labor_rate is not None and inputs.human_labor_rate.currency != "USD":
        raise ValueError("human labor rate must use USD")

    direct_cost = (
        inputs.automated_processing.amount_cents + inputs.source_data.amount_cents
    )
    total_human_seconds = (
        inputs.human_review.duration_seconds + inputs.manual_research.duration_seconds
    )

    evidence_refs = [
        inputs.automated_processing.evidence_ref,
        inputs.source_data.evidence_ref,
        inputs.human_review.evidence_ref,
        inputs.manual_research.evidence_ref,
    ]

    if inputs.human_labor_rate is None:
        labor_rate_state: Literal["NOT_PROVIDED", "DOCUMENTED"] = "NOT_PROVIDED"
        labor_rate_cents_per_hour = None
        labor_cost_state: Literal[
            "NOT_COMPUTED_NO_RATE", "COMPUTED_FROM_DOCUMENTED_RATE"
        ] = "NOT_COMPUTED_NO_RATE"
        labor_cost_cents = None
        fully_loaded_state: Literal[
            "NOT_COMPUTABLE_NO_LABOR_RATE",
            "COMPUTED_FROM_MEASURED_COMPONENTS",
        ] = "NOT_COMPUTABLE_NO_LABOR_RATE"
        fully_loaded_cost_cents = None
    else:
        labor_rate_state = "DOCUMENTED"
        labor_rate_cents_per_hour = inputs.human_labor_rate.cents_per_hour
        labor_cost_state = "COMPUTED_FROM_DOCUMENTED_RATE"
        labor_cost_cents = _human_labor_cost_cents(
            total_human_seconds,
            inputs.human_labor_rate.cents_per_hour,
        )
        fully_loaded_state = "COMPUTED_FROM_MEASURED_COMPONENTS"
        fully_loaded_cost_cents = direct_cost + labor_cost_cents
        evidence_refs.append(inputs.human_labor_rate.evidence_ref)

    return NyMvp1FollowUpCostMeasurementResult(
        measurement_id=inputs.measurement_id,
        candidate_case_id=inputs.candidate_case_id,
        automated_processing_cost_cents=inputs.automated_processing.amount_cents,
        source_data_cost_cents=inputs.source_data.amount_cents,
        direct_machine_and_data_cost_cents=direct_cost,
        human_review_seconds=inputs.human_review.duration_seconds,
        manual_research_seconds=inputs.manual_research.duration_seconds,
        total_human_seconds=total_human_seconds,
        human_labor_rate_state=labor_rate_state,
        human_labor_rate_cents_per_hour=labor_rate_cents_per_hour,
        human_labor_cost_state=labor_cost_state,
        human_labor_cost_cents=labor_cost_cents,
        fully_loaded_follow_up_cost_state=fully_loaded_state,
        fully_loaded_follow_up_cost_cents=fully_loaded_cost_cents,
        evidence_refs=tuple(dict.fromkeys(evidence_refs)),
        owner_pii_included=False,
        no_commercial_recommendation=True,
    )
