"""Synthetic-only MVP-1 targetable-opportunity selection and classification."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

DOCUMENTED_SHAPE = "EXACTLY_13_PIPES_DOCUMENTED_14_FIELDS"
SELECTION_RULE_VERSION = "2.0.0"
SELECTION_BASIS = "PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER"

FrictionLane = Literal["F0", "F1", "F2", "F3"]
ServiceNeedState = Literal["UNKNOWN", "LOW_EVIDENCE", "MATERIAL_EVIDENCE"]
ResolvabilityState = Literal["UNKNOWN", "EASY", "BOUNDED", "UNBOUNDED"]
EstatePathState = Literal["NOT_EVALUATED", "NO_EVIDENCE", "EVIDENCE_PRESENT"]
RepresentativePathState = Literal[
    "NOT_EVALUATED",
    "IDENTIFIED",
    "BOUNDED_DISCOVERABLE",
    "NOT_BOUNDED",
]
TargetabilityClass = Literal[
    "T0_SELF_SERVICE_LIKELY",
    "T1_UNRESOLVED_BUT_LOCATABLE",
    "T2_ESTATE_OR_REPRESENTATIVE_PATH",
    "T3_HARD_BUT_BOUNDED",
    "T4_UNBOUNDED_OR_UNRESOLVED_STOP",
]


class SyntheticTargetingCandidate(BaseModel):
    """Non-owner metadata used to validate future persistence-first selection."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    data_mode: Literal["SYNTHETIC_TEST_ONLY"] = "SYNTHETIC_TEST_ONLY"
    source_record_ordinal: int = Field(ge=1)
    structural_shape: str = DOCUMENTED_SHAPE
    property_type_code: str = Field(min_length=1)
    property_owner_count: int = Field(ge=0)
    property_id_present: bool
    holder_report_year: int = Field(ge=1)


class PersistenceSelectionResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    status: Literal["SELECTED", "STOPPED_NO_ELIGIBLE_CANDIDATE"]
    reason_code: Literal[
        "PERSISTENCE_FIRST_CANDIDATE_SELECTED",
        "NO_ELIGIBLE_SINGLE_OWNER_IN03_WITH_REPORT_YEAR",
    ]
    selection_rule_version: Literal["2.0.0"] = SELECTION_RULE_VERSION
    selection_basis: Literal[
        "PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER"
    ] = SELECTION_BASIS
    records_evaluated: int = Field(ge=0)
    eligible_records_count: int = Field(ge=0)
    selected_source_record_ordinal: int | None = Field(default=None, ge=1)
    selected_holder_report_year: int | None = Field(default=None, ge=1)
    persistence_interpretation: Literal[
        "REPORT_YEAR_IS_PERSISTENCE_SIGNAL_ONLY_NOT_AWARENESS_VALUE_DEATH_OR_CONTACTABILITY"
    ] = "REPORT_YEAR_IS_PERSISTENCE_SIGNAL_ONLY_NOT_AWARENESS_VALUE_DEATH_OR_CONTACTABILITY"
    owner_pii_used_for_ranking: Literal[False] = False
    value_prediction_performed: Literal[False] = False
    authorization_granted: Literal[False] = False

    @model_validator(mode="after")
    def validate_selection_shape(self) -> PersistenceSelectionResult:
        if self.status == "SELECTED":
            if self.selected_source_record_ordinal is None:
                raise ValueError("selected result requires source ordinal")
            if self.selected_holder_report_year is None:
                raise ValueError("selected result requires Holder Report Year")
            if self.eligible_records_count < 1:
                raise ValueError("selected result requires at least one eligible record")
        else:
            if self.selected_source_record_ordinal is not None:
                raise ValueError("stopped result cannot contain selected ordinal")
            if self.selected_holder_report_year is not None:
                raise ValueError("stopped result cannot contain selected report year")
        return self


class SyntheticTargetabilityEvidence(BaseModel):
    """Synthetic evidence fixture for the future L2 targetability decision."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    service_need_state: ServiceNeedState
    resolvability_state: ResolvabilityState
    estate_path_state: EstatePathState = "NOT_EVALUATED"
    representative_path_state: RepresentativePathState = "NOT_EVALUATED"
    friction_lane: FrictionLane | None = None
    evidence_refs: tuple[str, ...] = Field(min_length=1)
    targetability_decision_cost_state: Literal[
        "NOT_MEASURED", "MEASURING", "MEASURED"
    ] = "NOT_MEASURED"
    targetability_decision_cost_cents: int | None = Field(default=None, ge=0)
    awareness_state: Literal["UNKNOWN_UNTIL_OUTREACH"] = "UNKNOWN_UNTIL_OUTREACH"
    owner_pii_included: Literal[False] = False
    value_evidence_used: Literal[False] = False

    @model_validator(mode="after")
    def validate_cost_state(self) -> SyntheticTargetabilityEvidence:
        if self.targetability_decision_cost_state == "MEASURED":
            if self.targetability_decision_cost_cents is None:
                raise ValueError("MEASURED targetability cost requires cents")
        elif self.targetability_decision_cost_cents is not None:
            raise ValueError("cost cents require MEASURED state")
        return self


class TargetabilityDecision(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    state: Literal["CLASSIFIED", "UNRESOLVED_REQUIRES_L2"]
    targetability_class: TargetabilityClass | None
    service_need_state: ServiceNeedState
    resolvability_state: ResolvabilityState
    estate_path_state: EstatePathState
    representative_path_state: RepresentativePathState
    awareness_state: Literal["UNKNOWN_UNTIL_OUTREACH"] = "UNKNOWN_UNTIL_OUTREACH"
    friction_lane: FrictionLane | None = None
    friction_lane_used_as_targeting: Literal[False] = False
    targetability_score: None = None
    value_prediction_performed: Literal[False] = False
    monetary_value_used_for_targeting: Literal[False] = False
    evidence_refs: tuple[str, ...] = Field(min_length=1)
    targetability_decision_cost_state: Literal[
        "NOT_MEASURED", "MEASURING", "MEASURED"
    ]
    targetability_decision_cost_cents: int | None = Field(default=None, ge=0)
    recommended_next_scope: Literal[
        "STOP_OR_LOW_TOUCH_REVIEW",
        "SEPARATE_L3_OUTREACH_REVIEW",
        "STOP",
        "L2_MINIMAL_TARGETABILITY_DISCOVERY",
    ]
    no_commercial_decision: Literal[True] = True


class TargetabilityEconomicPolicy(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    primary_p1_metric: Literal["TARGETABILITY_DECISION_COST"] = (
        "TARGETABILITY_DECISION_COST"
    )
    pre_value_discovery_cost_retained: Literal[True] = True
    l1_max_new_external_cash_spend_cents: Literal[0] = 0
    l1_paid_api_calls_allowed: Literal[False] = False
    l1_paid_data_purchases_allowed: Literal[False] = False
    l2_incremental_budget_state: Literal["UNSET_REQUIRES_PRODUCT_OWNER"] = (
        "UNSET_REQUIRES_PRODUCT_OWNER"
    )


class SyntheticTargetableOpportunitySafety(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    synthetic_only: Literal[True] = True
    real_source_accessed: Literal[False] = False
    real_owner_pii_processed: Literal[False] = False
    real_candidate_materialized: Literal[False] = False
    identity_resolution_performed: Literal[False] = False
    address_enrichment_performed: Literal[False] = False
    third_party_api_used: Literal[False] = False
    outreach_performed: Literal[False] = False
    value_research_performed: Literal[False] = False
    claim_activity_performed: Literal[False] = False


class SyntheticTargetableOpportunityResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_ONLY"] = "SYNTHETIC_ONLY"
    selection: PersistenceSelectionResult
    targetability: TargetabilityDecision | None
    economics_policy: TargetabilityEconomicPolicy = TargetabilityEconomicPolicy()
    safety: SyntheticTargetableOpportunitySafety = SyntheticTargetableOpportunitySafety()
    authorization_granted: Literal[False] = False


def _eligible(candidate: SyntheticTargetingCandidate) -> bool:
    return (
        candidate.structural_shape == DOCUMENTED_SHAPE
        and candidate.property_type_code == "IN03"
        and candidate.property_owner_count == 1
        and candidate.property_id_present
        and candidate.holder_report_year > 0
    )


def select_persistence_first_candidate(
    records: Sequence[SyntheticTargetingCandidate],
) -> PersistenceSelectionResult:
    """Choose oldest reported eligible IN03; source ordinal is the deterministic tie-break."""

    eligible = [record for record in records if _eligible(record)]
    if not eligible:
        return PersistenceSelectionResult(
            status="STOPPED_NO_ELIGIBLE_CANDIDATE",
            reason_code="NO_ELIGIBLE_SINGLE_OWNER_IN03_WITH_REPORT_YEAR",
            records_evaluated=len(records),
            eligible_records_count=0,
        )

    selected = min(
        eligible,
        key=lambda record: (record.holder_report_year, record.source_record_ordinal),
    )
    return PersistenceSelectionResult(
        status="SELECTED",
        reason_code="PERSISTENCE_FIRST_CANDIDATE_SELECTED",
        records_evaluated=len(records),
        eligible_records_count=len(eligible),
        selected_source_record_ordinal=selected.source_record_ordinal,
        selected_holder_report_year=selected.holder_report_year,
    )


def classify_targetability(
    evidence: SyntheticTargetabilityEvidence,
) -> TargetabilityDecision:
    """Classify service need x resolvability without value prediction or scoring."""

    klass: TargetabilityClass | None = None
    state: Literal["CLASSIFIED", "UNRESOLVED_REQUIRES_L2"]
    next_scope: Literal[
        "STOP_OR_LOW_TOUCH_REVIEW",
        "SEPARATE_L3_OUTREACH_REVIEW",
        "STOP",
        "L2_MINIMAL_TARGETABILITY_DISCOVERY",
    ]

    if evidence.resolvability_state == "UNBOUNDED":
        klass = "T4_UNBOUNDED_OR_UNRESOLVED_STOP"
        state = "CLASSIFIED"
        next_scope = "STOP"
    elif (
        evidence.estate_path_state == "EVIDENCE_PRESENT"
        and evidence.representative_path_state
        in {"IDENTIFIED", "BOUNDED_DISCOVERABLE"}
    ):
        klass = "T2_ESTATE_OR_REPRESENTATIVE_PATH"
        state = "CLASSIFIED"
        next_scope = "SEPARATE_L3_OUTREACH_REVIEW"
    elif (
        evidence.estate_path_state == "EVIDENCE_PRESENT"
        and evidence.representative_path_state == "NOT_BOUNDED"
    ):
        klass = "T4_UNBOUNDED_OR_UNRESOLVED_STOP"
        state = "CLASSIFIED"
        next_scope = "STOP"
    elif (
        evidence.service_need_state == "LOW_EVIDENCE"
        and evidence.resolvability_state == "EASY"
    ):
        klass = "T0_SELF_SERVICE_LIKELY"
        state = "CLASSIFIED"
        next_scope = "STOP_OR_LOW_TOUCH_REVIEW"
    elif (
        evidence.service_need_state == "MATERIAL_EVIDENCE"
        and evidence.resolvability_state == "EASY"
    ):
        klass = "T1_UNRESOLVED_BUT_LOCATABLE"
        state = "CLASSIFIED"
        next_scope = "SEPARATE_L3_OUTREACH_REVIEW"
    elif (
        evidence.service_need_state == "MATERIAL_EVIDENCE"
        and evidence.resolvability_state == "BOUNDED"
    ):
        klass = "T3_HARD_BUT_BOUNDED"
        state = "CLASSIFIED"
        next_scope = "SEPARATE_L3_OUTREACH_REVIEW"
    else:
        state = "UNRESOLVED_REQUIRES_L2"
        next_scope = "L2_MINIMAL_TARGETABILITY_DISCOVERY"

    return TargetabilityDecision(
        state=state,
        targetability_class=klass,
        service_need_state=evidence.service_need_state,
        resolvability_state=evidence.resolvability_state,
        estate_path_state=evidence.estate_path_state,
        representative_path_state=evidence.representative_path_state,
        friction_lane=evidence.friction_lane,
        evidence_refs=evidence.evidence_refs,
        targetability_decision_cost_state=evidence.targetability_decision_cost_state,
        targetability_decision_cost_cents=evidence.targetability_decision_cost_cents,
        recommended_next_scope=next_scope,
    )


def evaluate_synthetic_targetable_opportunity(
    records: Sequence[SyntheticTargetingCandidate],
    evidence: SyntheticTargetabilityEvidence | None = None,
) -> SyntheticTargetableOpportunityResult:
    """Synthetic end-to-end contract: persistence selection then optional targetability evidence."""

    selection = select_persistence_first_candidate(records)
    if selection.status != "SELECTED":
        return SyntheticTargetableOpportunityResult(
            selection=selection,
            targetability=None,
        )

    decision = classify_targetability(evidence) if evidence is not None else None
    return SyntheticTargetableOpportunityResult(
        selection=selection,
        targetability=decision,
    )
