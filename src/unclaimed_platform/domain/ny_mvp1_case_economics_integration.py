"""Fail-closed bridge from measured follow-up cost to explicit case economics."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    NyMvp1FollowUpCostMeasurementResult,
)
from unclaimed_platform.domain.ny_mvp1_value_evidence import (
    NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS,
    NyMvp1ExplicitCaseEconomicsInput,
    NyMvp1ExplicitCaseEconomicsResult,
    compute_explicit_case_economics,
)


class NyMvp1CaseEconomicsIntegrationInput(BaseModel):
    """Evidence-backed value/fee inputs waiting for a fully loaded follow-up cost."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    recoverable_value_cents: int = Field(ge=0)
    agreed_fee_bps: int = Field(ge=0, le=NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS)
    value_evidence_ref: str = Field(min_length=1)
    fee_evidence_ref: str = Field(min_length=1)
    fee_rule_scope_confirmed: Literal[True] = True


class NyMvp1CaseEconomicsIntegrationResult(BaseModel):
    """Integration state with provenance and no automatic commercial decision."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    integration_state: Literal[
        "READY_FOR_EXPLICIT_ECONOMICS",
        "BLOCKED_FOLLOW_UP_COST_UNAVAILABLE",
    ]
    reason_code: Literal[
        "FULLY_LOADED_FOLLOW_UP_COST_AVAILABLE",
        "FULLY_LOADED_FOLLOW_UP_COST_UNAVAILABLE",
    ]
    candidate_case_id: str = Field(min_length=1)
    follow_up_cost_measurement_id: str = Field(min_length=1)
    follow_up_cost_measurement_ref: str = Field(min_length=1)
    follow_up_cost_evidence_refs: tuple[str, ...] = Field(min_length=4)
    recoverable_value_cents: int = Field(ge=0)
    agreed_fee_bps: int = Field(ge=0, le=NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS)
    value_evidence_ref: str = Field(min_length=1)
    fee_evidence_ref: str = Field(min_length=1)
    fee_rule_scope_confirmed: Literal[True]
    measured_follow_up_cost_cents: int | None = Field(default=None, ge=0)
    explicit_economics_input: NyMvp1ExplicitCaseEconomicsInput | None
    explicit_economics_result: NyMvp1ExplicitCaseEconomicsResult | None
    no_commercial_recommendation: Literal[True] = True

    @model_validator(mode="after")
    def validate_fail_closed_states(self) -> NyMvp1CaseEconomicsIntegrationResult:
        ready = self.integration_state == "READY_FOR_EXPLICIT_ECONOMICS"

        if ready:
            if self.reason_code != "FULLY_LOADED_FOLLOW_UP_COST_AVAILABLE":
                raise ValueError("ready integration requires available-cost reason code")
            if self.measured_follow_up_cost_cents is None:
                raise ValueError("ready integration requires measured follow-up cost")
            if self.explicit_economics_input is None:
                raise ValueError("ready integration requires explicit economics input")
            if self.explicit_economics_result is None:
                raise ValueError("ready integration requires explicit economics result")
            if (
                self.explicit_economics_input.measured_follow_up_cost_cents
                != self.measured_follow_up_cost_cents
            ):
                raise ValueError("explicit economics input must use fully loaded follow-up cost")
        else:
            if self.reason_code != "FULLY_LOADED_FOLLOW_UP_COST_UNAVAILABLE":
                raise ValueError("blocked integration requires unavailable-cost reason code")
            if self.measured_follow_up_cost_cents is not None:
                raise ValueError("blocked integration cannot expose a substitute follow-up cost")
            if self.explicit_economics_input is not None:
                raise ValueError("blocked integration cannot create explicit economics input")
            if self.explicit_economics_result is not None:
                raise ValueError("blocked integration cannot compute explicit economics result")

        return self


def integrate_follow_up_cost_with_case_economics(
    economics_input: NyMvp1CaseEconomicsIntegrationInput,
    follow_up_cost: NyMvp1FollowUpCostMeasurementResult,
) -> NyMvp1CaseEconomicsIntegrationResult:
    """Use only a fully loaded measured cost as case-economics follow-up cost."""

    measurement_id = str(follow_up_cost.measurement_id)
    case_id = str(follow_up_cost.candidate_case_id)
    measurement_ref = f"follow-up-cost-measurement:{measurement_id}"

    if (
        follow_up_cost.fully_loaded_follow_up_cost_state
        != "COMPUTED_FROM_MEASURED_COMPONENTS"
        or follow_up_cost.fully_loaded_follow_up_cost_cents is None
    ):
        return NyMvp1CaseEconomicsIntegrationResult(
            integration_state="BLOCKED_FOLLOW_UP_COST_UNAVAILABLE",
            reason_code="FULLY_LOADED_FOLLOW_UP_COST_UNAVAILABLE",
            candidate_case_id=case_id,
            follow_up_cost_measurement_id=measurement_id,
            follow_up_cost_measurement_ref=measurement_ref,
            follow_up_cost_evidence_refs=follow_up_cost.evidence_refs,
            recoverable_value_cents=economics_input.recoverable_value_cents,
            agreed_fee_bps=economics_input.agreed_fee_bps,
            value_evidence_ref=economics_input.value_evidence_ref,
            fee_evidence_ref=economics_input.fee_evidence_ref,
            fee_rule_scope_confirmed=True,
            measured_follow_up_cost_cents=None,
            explicit_economics_input=None,
            explicit_economics_result=None,
        )

    explicit_input = NyMvp1ExplicitCaseEconomicsInput(
        recoverable_value_cents=economics_input.recoverable_value_cents,
        agreed_fee_bps=economics_input.agreed_fee_bps,
        measured_follow_up_cost_cents=follow_up_cost.fully_loaded_follow_up_cost_cents,
        value_evidence_ref=economics_input.value_evidence_ref,
        fee_evidence_ref=economics_input.fee_evidence_ref,
        cost_evidence_ref=measurement_ref,
        fee_rule_scope_confirmed=True,
    )
    explicit_result = compute_explicit_case_economics(explicit_input)

    return NyMvp1CaseEconomicsIntegrationResult(
        integration_state="READY_FOR_EXPLICIT_ECONOMICS",
        reason_code="FULLY_LOADED_FOLLOW_UP_COST_AVAILABLE",
        candidate_case_id=case_id,
        follow_up_cost_measurement_id=measurement_id,
        follow_up_cost_measurement_ref=measurement_ref,
        follow_up_cost_evidence_refs=follow_up_cost.evidence_refs,
        recoverable_value_cents=economics_input.recoverable_value_cents,
        agreed_fee_bps=economics_input.agreed_fee_bps,
        value_evidence_ref=economics_input.value_evidence_ref,
        fee_evidence_ref=economics_input.fee_evidence_ref,
        fee_rule_scope_confirmed=True,
        measured_follow_up_cost_cents=follow_up_cost.fully_loaded_follow_up_cost_cents,
        explicit_economics_input=explicit_input,
        explicit_economics_result=explicit_result,
    )
