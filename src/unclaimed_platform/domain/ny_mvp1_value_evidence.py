"""Deterministic New York MVP-1 economics evidence and explicit-input arithmetic."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS = 1500


class NyMvp1PrecontactEconomicsEvidence(BaseModel):
    """Fail-closed economics state before claim review / ownership verification."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["OFFLINE_PRECONTACT_EVIDENCE"] = "OFFLINE_PRECONTACT_EVIDENCE"
    jurisdiction: Literal["NY"] = "NY"
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = (
        "ny.osc.unclaimed_funds.owner_name_file"
    )
    recoverable_value_state: Literal["UNKNOWN_PRE_CLAIM_REVIEW"] = (
        "UNKNOWN_PRE_CLAIM_REVIEW"
    )
    exact_recoverable_value_cents: None = None
    owner_file_discloses_amount: Literal[False] = False
    claim_review_required_for_exact_amount: Literal[True] = True
    fee_rule_scope: Literal["ABP_1416_LOCATION_SERVICES_SUBJECT_TO_EXCEPTIONS"] = (
        "ABP_1416_LOCATION_SERVICES_SUBJECT_TO_EXCEPTIONS"
    )
    statutory_fee_cap_bps: Literal[1500] = NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS
    actual_fee_bps: None = None
    fee_applicability_requires_legal_review: Literal[True] = True
    expected_follow_up_cost_cents: None = None
    cost_measurement_state: Literal["NOT_MEASURED"] = "NOT_MEASURED"
    commercial_actionability: Literal["NOT_COMPUTABLE_PRE_CONTACT"] = (
        "NOT_COMPUTABLE_PRE_CONTACT"
    )
    reason_codes: tuple[
        Literal["RECOVERABLE_VALUE_UNDISCLOSED_PRE_CLAIM_REVIEW"],
        Literal["ACTUAL_FEE_RATE_UNSUPPORTED"],
        Literal["FOLLOW_UP_COST_NOT_MEASURED"],
    ] = (
        "RECOVERABLE_VALUE_UNDISCLOSED_PRE_CLAIM_REVIEW",
        "ACTUAL_FEE_RATE_UNSUPPORTED",
        "FOLLOW_UP_COST_NOT_MEASURED",
    )
    reviewer_decision_required: Literal["CONTINUE_VALUE_RESEARCH_OR_STOP"] = (
        "CONTINUE_VALUE_RESEARCH_OR_STOP"
    )


class NyMvp1ExplicitCaseEconomicsInput(BaseModel):
    """Explicit evidence-backed monetary inputs for deterministic arithmetic."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    recoverable_value_cents: int = Field(ge=0)
    agreed_fee_bps: int = Field(ge=0, le=NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS)
    measured_follow_up_cost_cents: int = Field(ge=0)
    value_evidence_ref: str = Field(min_length=1)
    fee_evidence_ref: str = Field(min_length=1)
    cost_evidence_ref: str = Field(min_length=1)
    fee_rule_scope_confirmed: Literal[True] = True


class NyMvp1ExplicitCaseEconomicsResult(BaseModel):
    """Arithmetic result only; it deliberately contains no commercial recommendation."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    recoverable_value_cents: int = Field(ge=0)
    agreed_fee_bps: int = Field(ge=0, le=NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS)
    statutory_fee_cap_bps: Literal[1500] = NY_LOCATION_SERVICE_PROVIDER_FEE_CAP_BPS
    gross_fee_cents: int = Field(ge=0)
    measured_follow_up_cost_cents: int = Field(ge=0)
    contribution_before_overhead_cents: int
    fee_cap_compliant: Literal[True] = True
    legal_scope_assumption: Literal["ABP_1416_LOCATION_SERVICE"] = (
        "ABP_1416_LOCATION_SERVICE"
    )
    no_commercial_recommendation: Literal[True] = True
    value_evidence_ref: str = Field(min_length=1)
    fee_evidence_ref: str = Field(min_length=1)
    cost_evidence_ref: str = Field(min_length=1)


def ny_mvp1_precontact_economics_evidence() -> NyMvp1PrecontactEconomicsEvidence:
    """Return the current evidence-backed pre-contact economics state."""

    return NyMvp1PrecontactEconomicsEvidence()


def _fee_cents(recoverable_value_cents: int, agreed_fee_bps: int) -> int:
    raw_fee = (
        Decimal(recoverable_value_cents)
        * Decimal(agreed_fee_bps)
        / Decimal(10_000)
    )
    return int(raw_fee.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def compute_explicit_case_economics(
    inputs: NyMvp1ExplicitCaseEconomicsInput,
) -> NyMvp1ExplicitCaseEconomicsResult:
    """Compute deterministic case arithmetic from explicit evidence-backed inputs."""

    gross_fee_cents = _fee_cents(inputs.recoverable_value_cents, inputs.agreed_fee_bps)
    contribution_before_overhead_cents = (
        gross_fee_cents - inputs.measured_follow_up_cost_cents
    )

    return NyMvp1ExplicitCaseEconomicsResult(
        recoverable_value_cents=inputs.recoverable_value_cents,
        agreed_fee_bps=inputs.agreed_fee_bps,
        gross_fee_cents=gross_fee_cents,
        measured_follow_up_cost_cents=inputs.measured_follow_up_cost_cents,
        contribution_before_overhead_cents=contribution_before_overhead_cents,
        value_evidence_ref=inputs.value_evidence_ref,
        fee_evidence_ref=inputs.fee_evidence_ref,
        cost_evidence_ref=inputs.cost_evidence_ref,
    )
