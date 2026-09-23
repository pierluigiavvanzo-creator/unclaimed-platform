"""Synthetic-only NY OSC one-candidate materialization and economic instrumentation."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal
from uuid import NAMESPACE_URL, UUID, uuid5

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator

from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    DocumentedHumanLaborRate,
    MeasuredCostComponent,
    MeasuredDurationComponent,
    NyMvp1FollowUpCostMeasurementInput,
    NyMvp1FollowUpCostMeasurementResult,
    measure_follow_up_cost,
)
from unclaimed_platform.domain.ny_mvp1_value_evidence import (
    NyMvp1PrecontactEconomicsEvidence,
    ny_mvp1_precontact_economics_evidence,
)

NY_OSC_SOURCE_ID = "ny.osc.unclaimed_funds.owner_name_file"
NY_OSC_ONE_CANDIDATE_SELECTION_RULE_VERSION = "1.0.0"
DOCUMENTED_SHAPE = "EXACTLY_13_PIPES_DOCUMENTED_14_FIELDS"

FrictionLane = Literal["F0", "F1", "F2", "F3"]
EconomicDiscoveryStage = Literal["L0", "L1", "L2", "L3", "L4", "L5"]
PreValueDiscoveryCostState = Literal[
    "NOT_STARTED",
    "MEASURING",
    "VALUE_KNOWN",
    "VALUE_STILL_UNKNOWN_STOPPED",
    "VALUE_REQUIRES_UNAUTHORIZED_SCOPE",
]


class SyntheticNyOscCandidateRecord(BaseModel):
    """Synthetic substitute for the approved transient six-field candidate scope."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    data_mode: Literal["SYNTHETIC_TEST_ONLY"] = "SYNTHETIC_TEST_ONLY"
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OSC_SOURCE_ID
    source_snapshot_ref: str = Field(min_length=1)
    source_record_ordinal: int = Field(ge=1)
    structural_shape: str = DOCUMENTED_SHAPE
    property_id: str = Field(min_length=1)
    property_type_code: str = Field(min_length=1)
    property_owner_count: int = Field(ge=0)
    owner_name: str = Field(min_length=1)
    holder_name: str = Field(min_length=1)
    holder_report_year: str = Field(min_length=1)


class LaneChangeEvent(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    from_lane: FrictionLane
    to_lane: FrictionLane
    changed_at: AwareDatetime
    reason_code: str = Field(min_length=1)
    evidence_refs: tuple[str, ...] = Field(min_length=1)
    value_evidence_used: Literal[False] = False


class SyntheticL1InstrumentationInput(BaseModel):
    """Explicit synthetic evidence used to validate future L1 economic instrumentation."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    measurement_id: UUID
    initial_lane: FrictionLane
    lane_assignment_evidence_refs: tuple[str, ...] = Field(min_length=1)
    lane_change_events: tuple[LaneChangeEvent, ...] = ()
    stage_started_at: AwareDatetime
    stage_completed_at: AwareDatetime
    stage_evidence_ref: str = Field(min_length=1)
    approved_incremental_budget_cents: int = Field(ge=0)
    budget_evidence_ref: str = Field(min_length=1)
    automated_processing: MeasuredCostComponent
    source_data: MeasuredCostComponent
    human_review: MeasuredDurationComponent
    manual_research: MeasuredDurationComponent
    human_labor_rate: DocumentedHumanLaborRate | None = None
    next_information_objective: Literal[
        "CONFIRM_MINIMUM_CASE_STRUCTURE_ONLY"
    ] = "CONFIRM_MINIMUM_CASE_STRUCTURE_ONLY"
    expected_decision_unlocked: Literal[
        "REQUEST_MINIMUM_L2_SCOPE_OR_STOP"
    ] = "REQUEST_MINIMUM_L2_SCOPE_OR_STOP"
    fail_closed_stop_condition: Literal[
        "STOP_IF_INELIGIBLE_SCOPE_INSUFFICIENT_OR_BUDGET_EXCEEDED"
    ] = "STOP_IF_INELIGIBLE_SCOPE_INSUFFICIENT_OR_BUDGET_EXCEEDED"

    @model_validator(mode="after")
    def validate_stage_window(self) -> SyntheticL1InstrumentationInput:
        if self.stage_completed_at < self.stage_started_at:
            raise ValueError("stage_completed_at cannot precede stage_started_at")
        return self


class FrictionLaneAssignment(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    initial_lane: FrictionLane
    current_lane: FrictionLane
    assignment_basis: Literal[
        "EXPLICIT_SYNTHETIC_FRICTION_FIXTURE_NOT_VALUE_PREDICTION"
    ] = "EXPLICIT_SYNTHETIC_FRICTION_FIXTURE_NOT_VALUE_PREDICTION"
    evidence_refs: tuple[str, ...] = Field(min_length=1)
    lane_change_events: tuple[LaneChangeEvent, ...] = ()
    value_prediction_performed: Literal[False] = False

    @model_validator(mode="after")
    def validate_lane_history(self) -> FrictionLaneAssignment:
        expected_from = self.initial_lane
        for event in self.lane_change_events:
            if event.from_lane != expected_from:
                raise ValueError("lane change history is not contiguous")
            if event.to_lane == event.from_lane:
                raise ValueError("lane change event must change the lane")
            expected_from = event.to_lane
        if self.current_lane != expected_from:
            raise ValueError("current lane must equal the final lane history state")
        return self


class EconomicStageEvent(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    stage: EconomicDiscoveryStage
    event: Literal["ENTERED", "COMPLETED"]
    occurred_at: AwareDatetime
    evidence_ref: str = Field(min_length=1)


class PersistentCandidateEnvelope(BaseModel):
    """Durable candidate envelope that excludes Owner Name and Property ID."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    case_id: UUID
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OSC_SOURCE_ID
    source_snapshot_ref: str = Field(min_length=1)
    source_record_ordinal: int = Field(ge=1)
    selection_rule_version: Literal["1.0.0"] = NY_OSC_ONE_CANDIDATE_SELECTION_RULE_VERSION
    property_type_code: Literal["IN03"] = "IN03"
    property_owner_count: Literal[1] = 1
    reported_by: str = Field(min_length=1)
    reported_when: str = Field(min_length=1)
    candidate_state: Literal["SYNTHETIC_TRANSIENT_MATERIALIZED"] = (
        "SYNTHETIC_TRANSIENT_MATERIALIZED"
    )
    value_evidence_state: Literal["UNKNOWN_PRE_CLAIM_REVIEW"] = (
        "UNKNOWN_PRE_CLAIM_REVIEW"
    )
    persistent_candidate_contains_owner_pii: Literal[False] = False
    owner_name_persisted: Literal[False] = False
    property_id_persisted: Literal[False] = False
    raw_row_persisted: Literal[False] = False
    address_fields_persisted: Literal[False] = False


class PreValueDiscoveryCostSummary(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    state: PreValueDiscoveryCostState
    currency: Literal["USD"] = "USD"
    accumulated_pre_value_cost_cents: int | None = Field(default=None, ge=0)
    direct_machine_and_data_cost_cents: int = Field(ge=0)
    human_labor_cost_cents: int | None = Field(default=None, ge=0)
    total_human_seconds: int = Field(ge=0)
    elapsed_seconds: int = Field(ge=0)
    evidence_refs: tuple[str, ...] = Field(min_length=4)
    value_known_at_stage: None = None
    stop_reason: Literal[
        "STOP_FULLY_LOADED_PRE_VALUE_COST_UNAVAILABLE",
        "STOP_PRE_VALUE_DISCOVERY_COST_TOO_HIGH",
        "STOP_REQUIRES_SEPARATELY_AUTHORIZED_L2_SCOPE",
    ]
    privacy_legal_scope_required: Literal[
        "L2_MINIMAL_IDENTITY_CONTACTABILITY_DISCOVERY"
    ] = "L2_MINIMAL_IDENTITY_CONTACTABILITY_DISCOVERY"
    approved_incremental_budget_cents: int = Field(ge=0)
    budget_evidence_ref: str = Field(min_length=1)
    budget_exceeded: bool | None


class EconomicIntegrationHooks(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    value_evidence_component: Literal[
        "unclaimed_platform.domain.ny_mvp1_value_evidence.ny_mvp1_precontact_economics_evidence"
    ] = "unclaimed_platform.domain.ny_mvp1_value_evidence.ny_mvp1_precontact_economics_evidence"
    follow_up_cost_component: Literal[
        "unclaimed_platform.domain.ny_mvp1_follow_up_cost.measure_follow_up_cost"
    ] = "unclaimed_platform.domain.ny_mvp1_follow_up_cost.measure_follow_up_cost"
    case_economics_component: Literal[
        "unclaimed_platform.domain.ny_mvp1_case_economics_integration."
        "integrate_follow_up_cost_with_case_economics"
    ] = (
        "unclaimed_platform.domain.ny_mvp1_case_economics_integration."
        "integrate_follow_up_cost_with_case_economics"
    )
    case_economics_integration_state: Literal[
        "BLOCKED_VALUE_AND_FEE_EVIDENCE_REQUIRED"
    ] = "BLOCKED_VALUE_AND_FEE_EVIDENCE_REQUIRED"
    explicit_case_economics_computed: Literal[False] = False


class EconomicCaseLedger(BaseModel):
    """Non-PII economics evidence record for the synthetic one-case experiment."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_TEST_ONLY"] = "SYNTHETIC_TEST_ONLY"
    case_id: UUID
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OSC_SOURCE_ID
    source_snapshot_ref: str = Field(min_length=1)
    selection_rule_version: Literal["1.0.0"] = NY_OSC_ONE_CANDIDATE_SELECTION_RULE_VERSION
    source_record_ordinal: int = Field(ge=1)
    lane: FrictionLaneAssignment
    stage_events: tuple[EconomicStageEvent, ...] = Field(min_length=2)
    current_discovery_stage: Literal["L1"] = "L1"
    pre_value_discovery_cost: PreValueDiscoveryCostSummary
    value_evidence_state: Literal["UNKNOWN_PRE_CLAIM_REVIEW"] = (
        "UNKNOWN_PRE_CLAIM_REVIEW"
    )
    value_evidence_ref: Literal[
        "component:ny_mvp1_precontact_economics_evidence"
    ] = "component:ny_mvp1_precontact_economics_evidence"
    candidate_selected: Literal[True] = True
    identity_work_started: Literal[False] = False
    contactability_established: Literal[False] = False
    contact_attempts_count: Literal[0] = 0
    agreement_offered: Literal[False] = False
    agreement_signed: Literal[False] = False
    claim_recovery_started: Literal[False] = False
    recovery_success: Literal[False] = False
    fee_billed_cents: None = None
    fee_collected_cents: None = None
    integration_hooks: EconomicIntegrationHooks
    owner_pii_included: Literal[False] = False
    no_lane_value_prediction: Literal[True] = True
    no_commercial_recommendation: Literal[True] = True


class SyntheticMaterializationSafety(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    synthetic_only: Literal[True] = True
    real_source_accessed: Literal[False] = False
    remote_preflight_performed: Literal[False] = False
    download_performed: Literal[False] = False
    real_owner_pii_processed: Literal[False] = False
    real_candidate_materialized: Literal[False] = False
    identity_resolution_performed: Literal[False] = False
    beneficiary_matching_performed: Literal[False] = False
    address_enrichment_performed: Literal[False] = False
    outreach_performed: Literal[False] = False
    value_research_performed: Literal[False] = False
    fee_agreement_performed: Literal[False] = False
    representation_performed: Literal[False] = False
    claim_activity_performed: Literal[False] = False
    transient_values_returned: Literal[False] = False
    owner_pii_persisted: Literal[False] = False
    transient_fields_disposed: tuple[str, ...] = (
        "Property ID",
        "Property Type Code",
        "Property Owner Count",
        "Owner Name",
        "Holder Name",
        "Holder Report Year",
    )


class SyntheticOneCandidateMaterializationResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_ONLY"] = "SYNTHETIC_ONLY"
    status: Literal["MATERIALIZED", "STOPPED_NO_ELIGIBLE_CANDIDATE"]
    reason_code: Literal[
        "SYNTHETIC_ONE_CANDIDATE_MATERIALIZED",
        "NO_ELIGIBLE_SINGLE_OWNER_IN03_CANDIDATE_FOUND",
        "SOURCE_ORDER_NOT_STRICTLY_INCREASING",
    ]
    records_evaluated: int = Field(ge=0)
    selected_source_record_ordinal: int | None = Field(default=None, ge=1)
    persistent_candidate: PersistentCandidateEnvelope | None
    economic_case_ledger: EconomicCaseLedger | None
    precontact_value_evidence: NyMvp1PrecontactEconomicsEvidence | None
    follow_up_cost: NyMvp1FollowUpCostMeasurementResult | None
    safety: SyntheticMaterializationSafety
    review_state: Literal[
        "READY_FOR_SYNTHETIC_REVIEW",
        "STOPPED_BEFORE_MATERIALIZATION",
    ]
    authorization_granted: Literal[False] = False

    @model_validator(mode="after")
    def validate_status_shape(self) -> SyntheticOneCandidateMaterializationResult:
        if self.status == "MATERIALIZED":
            if self.selected_source_record_ordinal is None:
                raise ValueError("materialized result requires selected ordinal")
            if self.persistent_candidate is None or self.economic_case_ledger is None:
                raise ValueError(
                    "materialized result requires candidate envelope and economic ledger"
                )
            if self.precontact_value_evidence is None or self.follow_up_cost is None:
                raise ValueError(
                    "materialized result requires reused economics evidence and cost result"
                )
            if self.review_state != "READY_FOR_SYNTHETIC_REVIEW":
                raise ValueError("materialized result must be ready for synthetic review")
        else:
            if self.selected_source_record_ordinal is not None:
                raise ValueError("stopped result cannot expose selected ordinal")
            if any(
                item is not None
                for item in (
                    self.persistent_candidate,
                    self.economic_case_ledger,
                    self.precontact_value_evidence,
                    self.follow_up_cost,
                )
            ):
                raise ValueError("stopped result cannot materialize candidate/economics artifacts")
            if self.review_state != "STOPPED_BEFORE_MATERIALIZATION":
                raise ValueError("stopped result must stop before materialization")
        return self


def _is_eligible(record: SyntheticNyOscCandidateRecord) -> bool:
    return (
        record.structural_shape == DOCUMENTED_SHAPE
        and record.property_type_code == "IN03"
        and record.property_owner_count == 1
        and bool(record.property_id.strip())
    )


def _deterministic_case_id(record: SyntheticNyOscCandidateRecord) -> UUID:
    identity = "|".join(
        (
            record.source_id,
            record.source_snapshot_ref,
            str(record.source_record_ordinal),
            "IN03",
            NY_OSC_ONE_CANDIDATE_SELECTION_RULE_VERSION,
        )
    )
    return uuid5(NAMESPACE_URL, identity)


def _stopped(
    reason_code: Literal[
        "NO_ELIGIBLE_SINGLE_OWNER_IN03_CANDIDATE_FOUND",
        "SOURCE_ORDER_NOT_STRICTLY_INCREASING",
    ],
    records_evaluated: int,
) -> SyntheticOneCandidateMaterializationResult:
    return SyntheticOneCandidateMaterializationResult(
        status="STOPPED_NO_ELIGIBLE_CANDIDATE",
        reason_code=reason_code,
        records_evaluated=records_evaluated,
        selected_source_record_ordinal=None,
        persistent_candidate=None,
        economic_case_ledger=None,
        precontact_value_evidence=None,
        follow_up_cost=None,
        safety=SyntheticMaterializationSafety(),
        review_state="STOPPED_BEFORE_MATERIALIZATION",
    )


def select_and_materialize_synthetic_one_candidate(
    records: Sequence[SyntheticNyOscCandidateRecord],
    instrumentation: SyntheticL1InstrumentationInput,
) -> SyntheticOneCandidateMaterializationResult:
    """Select first eligible source-order fixture and emit only non-PII durable artifacts."""

    prior_ordinal = 0
    selected: SyntheticNyOscCandidateRecord | None = None
    records_evaluated = 0
    for candidate in records:
        records_evaluated += 1
        if candidate.source_record_ordinal <= prior_ordinal:
            return _stopped("SOURCE_ORDER_NOT_STRICTLY_INCREASING", records_evaluated)
        prior_ordinal = candidate.source_record_ordinal
        if _is_eligible(candidate):
            selected = candidate
            break

    if selected is None:
        return _stopped(
            "NO_ELIGIBLE_SINGLE_OWNER_IN03_CANDIDATE_FOUND",
            records_evaluated,
        )

    case_id = _deterministic_case_id(selected)
    envelope = PersistentCandidateEnvelope(
        case_id=case_id,
        source_snapshot_ref=selected.source_snapshot_ref,
        source_record_ordinal=selected.source_record_ordinal,
        reported_by=selected.holder_name,
        reported_when=selected.holder_report_year,
    )

    follow_up_input = NyMvp1FollowUpCostMeasurementInput(
        mode="SYNTHETIC_TEST",
        measurement_id=instrumentation.measurement_id,
        candidate_case_id=case_id,
        owner_pii_included=False,
        automated_processing=instrumentation.automated_processing,
        source_data=instrumentation.source_data,
        human_review=instrumentation.human_review,
        manual_research=instrumentation.manual_research,
        human_labor_rate=instrumentation.human_labor_rate,
    )
    follow_up = measure_follow_up_cost(follow_up_input)
    value_evidence = ny_mvp1_precontact_economics_evidence()

    elapsed_seconds = int(
        (instrumentation.stage_completed_at - instrumentation.stage_started_at).total_seconds()
    )
    fully_loaded = follow_up.fully_loaded_follow_up_cost_cents
    if fully_loaded is None:
        pre_value_state: PreValueDiscoveryCostState = "MEASURING"
        stop_reason = "STOP_FULLY_LOADED_PRE_VALUE_COST_UNAVAILABLE"
        budget_exceeded = None
    elif fully_loaded > instrumentation.approved_incremental_budget_cents:
        pre_value_state = "VALUE_STILL_UNKNOWN_STOPPED"
        stop_reason = "STOP_PRE_VALUE_DISCOVERY_COST_TOO_HIGH"
        budget_exceeded = True
    else:
        pre_value_state = "VALUE_REQUIRES_UNAUTHORIZED_SCOPE"
        stop_reason = "STOP_REQUIRES_SEPARATELY_AUTHORIZED_L2_SCOPE"
        budget_exceeded = False

    pre_value = PreValueDiscoveryCostSummary(
        state=pre_value_state,
        accumulated_pre_value_cost_cents=fully_loaded,
        direct_machine_and_data_cost_cents=follow_up.direct_machine_and_data_cost_cents,
        human_labor_cost_cents=follow_up.human_labor_cost_cents,
        total_human_seconds=follow_up.total_human_seconds,
        elapsed_seconds=elapsed_seconds,
        evidence_refs=follow_up.evidence_refs,
        stop_reason=stop_reason,
        approved_incremental_budget_cents=instrumentation.approved_incremental_budget_cents,
        budget_evidence_ref=instrumentation.budget_evidence_ref,
        budget_exceeded=budget_exceeded,
    )

    current_lane = (
        instrumentation.lane_change_events[-1].to_lane
        if instrumentation.lane_change_events
        else instrumentation.initial_lane
    )

    ledger = EconomicCaseLedger(
        case_id=case_id,
        source_snapshot_ref=selected.source_snapshot_ref,
        source_record_ordinal=selected.source_record_ordinal,
        lane=FrictionLaneAssignment(
            initial_lane=instrumentation.initial_lane,
            current_lane=current_lane,
            evidence_refs=instrumentation.lane_assignment_evidence_refs,
            lane_change_events=instrumentation.lane_change_events,
        ),
        stage_events=(
            EconomicStageEvent(
                stage="L0",
                event="COMPLETED",
                occurred_at=instrumentation.stage_started_at,
                evidence_ref="selection-rule:ny-osc-one-candidate-v1",
            ),
            EconomicStageEvent(
                stage="L1",
                event="COMPLETED",
                occurred_at=instrumentation.stage_completed_at,
                evidence_ref=instrumentation.stage_evidence_ref,
            ),
        ),
        pre_value_discovery_cost=pre_value,
        integration_hooks=EconomicIntegrationHooks(),
    )

    return SyntheticOneCandidateMaterializationResult(
        status="MATERIALIZED",
        reason_code="SYNTHETIC_ONE_CANDIDATE_MATERIALIZED",
        records_evaluated=records_evaluated,
        selected_source_record_ordinal=selected.source_record_ordinal,
        persistent_candidate=envelope,
        economic_case_ledger=ledger,
        precontact_value_evidence=value_evidence,
        follow_up_cost=follow_up,
        safety=SyntheticMaterializationSafety(),
        review_state="READY_FOR_SYNTHETIC_REVIEW",
    )