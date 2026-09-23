from datetime import UTC, datetime, timedelta
from uuid import UUID

from unclaimed_platform.domain.ny_mvp1_follow_up_cost import DocumentedHumanLaborRate
from unclaimed_platform.domain.ny_osc_one_candidate_transient_materialization import (
    LaneChangeEvent,
    SyntheticL1InstrumentationInput,
    SyntheticNyOscCandidateRecord,
    select_and_materialize_synthetic_one_candidate,
)

NOW = datetime(2026, 9, 23, 18, 0, tzinfo=UTC)


def record(*, ordinal=12345, **overrides):
    data = dict(
        source_snapshot_ref="synthetic:snapshot:2026-09-23",
        source_record_ordinal=ordinal,
        property_id="SYNTHETIC-PROP-001",
        property_type_code="IN03",
        property_owner_count=1,
        owner_name="SYNTHETIC OWNER ALPHA",
        holder_name="SYNTHETIC LIFE INSURER",
        holder_report_year="2025",
    )
    data.update(overrides)
    return SyntheticNyOscCandidateRecord(**data)


def instrumentation(*, budget=1000, with_rate=True, lane="F2"):
    rate = None
    if with_rate:
        rate = DocumentedHumanLaborRate(
            cents_per_hour=7200,
            currency="USD",
            evidence_ref="synthetic:labor-rate",
            observed_at=NOW,
        )
    return SyntheticL1InstrumentationInput(
        measurement_id=UUID("11111111-1111-4111-8111-111111111111"),
        initial_lane=lane,
        lane_assignment_evidence_refs=("synthetic:friction-fixture",),
        stage_started_at=NOW,
        stage_completed_at=NOW + timedelta(seconds=190),
        stage_evidence_ref="synthetic:l1-timer",
        approved_incremental_budget_cents=budget,
        budget_evidence_ref="owner-approved:synthetic-l1-budget",
        automated_processing={
            "amount_cents": 37,
            "currency": "USD",
            "measurement_method": "SYSTEM_METERED",
            "allocation_basis": "PER_CANDIDATE_DIRECT",
            "evidence_ref": "synthetic:automation-meter",
            "observed_at": NOW,
        },
        source_data={
            "amount_cents": 0,
            "currency": "USD",
            "measurement_method": "ZERO_DIRECT_COST_DOCUMENTED",
            "allocation_basis": "ZERO_DIRECT_COST_PER_CANDIDATE",
            "evidence_ref": "synthetic:source-cost",
            "observed_at": NOW,
        },
        human_review={
            "duration_seconds": 125,
            "measurement_method": "REVIEWER_TIMER",
            "evidence_ref": "synthetic:review-timer",
            "observed_at": NOW,
        },
        manual_research={
            "duration_seconds": 65,
            "measurement_method": "MANUAL_TIMER",
            "evidence_ref": "synthetic:research-timer",
            "observed_at": NOW,
        },
        human_labor_rate=rate,
    )


def materialize(records=None, **instrumentation_kwargs):
    if records is None:
        records = [record()]
    return select_and_materialize_synthetic_one_candidate(
        records,
        instrumentation(**instrumentation_kwargs),
    )


def test_selects_first_eligible_record_in_physical_source_order_and_stops():
    result = materialize(
        [
            record(ordinal=10, property_type_code="IN01"),
            record(ordinal=20, property_id="FIRST-ELIGIBLE"),
            record(ordinal=30, property_id="SECOND-ELIGIBLE"),
        ]
    )
    assert result.status == "MATERIALIZED"
    assert result.records_evaluated == 2
    assert result.selected_source_record_ordinal == 20
    assert result.persistent_candidate is not None
    assert result.persistent_candidate.source_record_ordinal == 20


def test_happy_path_materializes_non_pii_envelope_and_economic_ledger():
    result = materialize()
    assert result.persistent_candidate is not None
    assert result.economic_case_ledger is not None
    assert result.persistent_candidate.property_type_code == "IN03"
    assert result.persistent_candidate.property_owner_count == 1
    assert result.persistent_candidate.persistent_candidate_contains_owner_pii is False
    assert result.economic_case_ledger.lane.initial_lane == "F2"
    assert result.economic_case_ledger.lane.value_prediction_performed is False
    assert result.economic_case_ledger.current_discovery_stage == "L1"
    pre_value = result.economic_case_ledger.pre_value_discovery_cost
    assert pre_value.state == "VALUE_REQUIRES_UNAUTHORIZED_SCOPE"
    assert pre_value.accumulated_pre_value_cost_cents == 417
    assert result.precontact_value_evidence is not None
    assert result.precontact_value_evidence.recoverable_value_state == (
        "UNKNOWN_PRE_CLAIM_REVIEW"
    )
    assert result.economic_case_ledger.integration_hooks.explicit_case_economics_computed is False


def test_case_id_uses_non_pii_provenance_not_owner_or_property_id():
    first = materialize()
    second = materialize(
        [
            record(
                property_id="DIFFERENT-SYNTHETIC-PROP",
                owner_name="DIFFERENT SYNTHETIC OWNER",
            )
        ]
    )
    assert first.persistent_candidate is not None
    assert second.persistent_candidate is not None
    assert first.persistent_candidate.case_id == second.persistent_candidate.case_id


def test_serialized_result_does_not_return_transient_owner_or_property_id_values():
    owner = "SYNTHETIC OWNER SECRET MARKER"
    prop = "SYNTHETIC-PROPERTY-SECRET-MARKER"
    result = materialize([record(owner_name=owner, property_id=prop)])
    payload = result.model_dump_json()
    assert owner not in payload
    assert prop not in payload
    assert result.safety.transient_values_returned is False
    assert result.safety.owner_pii_persisted is False


def test_no_eligible_candidate_produces_explicit_zero_candidate_stop():
    result = materialize(
        [
            record(ordinal=10, property_type_code="IN01"),
            record(ordinal=20, property_owner_count=2),
            record(ordinal=30, property_id="   "),
        ]
    )
    assert result.status == "STOPPED_NO_ELIGIBLE_CANDIDATE"
    assert result.reason_code == "NO_ELIGIBLE_SINGLE_OWNER_IN03_CANDIDATE_FOUND"
    assert result.records_evaluated == 3
    assert result.persistent_candidate is None
    assert result.economic_case_ledger is None


def test_out_of_order_fixture_fails_closed_instead_of_reordering_or_ranking():
    result = materialize(
        [
            record(ordinal=20, property_type_code="IN01"),
            record(ordinal=10),
        ]
    )
    assert result.status == "STOPPED_NO_ELIGIBLE_CANDIDATE"
    assert result.reason_code == "SOURCE_ORDER_NOT_STRICTLY_INCREASING"
    assert result.persistent_candidate is None


def test_budget_stop_loss_is_evidenced_not_guessed():
    result = materialize(budget=400)
    assert result.economic_case_ledger is not None
    pre_value = result.economic_case_ledger.pre_value_discovery_cost
    assert pre_value.accumulated_pre_value_cost_cents == 417
    assert pre_value.approved_incremental_budget_cents == 400
    assert pre_value.budget_exceeded is True
    assert pre_value.state == "VALUE_STILL_UNKNOWN_STOPPED"
    assert pre_value.stop_reason == "STOP_PRE_VALUE_DISCOVERY_COST_TOO_HIGH"


def test_missing_documented_labor_rate_keeps_pre_value_cost_measuring():
    result = materialize(with_rate=False)
    assert result.economic_case_ledger is not None
    pre_value = result.economic_case_ledger.pre_value_discovery_cost
    assert pre_value.accumulated_pre_value_cost_cents is None
    assert pre_value.direct_machine_and_data_cost_cents == 37
    assert pre_value.total_human_seconds == 190
    assert pre_value.state == "MEASURING"
    assert pre_value.stop_reason == "STOP_FULLY_LOADED_PRE_VALUE_COST_UNAVAILABLE"


def test_safety_boundary_remains_synthetic_only_and_authorizes_nothing():
    result = materialize(lane="F3")
    safety = result.safety
    assert safety.synthetic_only is True
    assert safety.real_source_accessed is False
    assert safety.download_performed is False
    assert safety.real_owner_pii_processed is False
    assert safety.real_candidate_materialized is False
    assert safety.identity_resolution_performed is False
    assert safety.outreach_performed is False
    assert safety.value_research_performed is False
    assert safety.claim_activity_performed is False
    assert result.authorization_granted is False


def test_lane_change_provenance_is_typed_and_not_a_value_prediction():
    lane_change = LaneChangeEvent(
        from_lane="F2",
        to_lane="F3",
        changed_at=NOW + timedelta(seconds=100),
        reason_code="SYNTHETIC_COMPLEX_DOCUMENT_CONDITION_OBSERVED",
        evidence_refs=("synthetic:lane-change-evidence",),
        value_evidence_used=False,
    )
    instrument = instrumentation().model_copy(
        update={"lane_change_events": (lane_change,)}
    )
    result = select_and_materialize_synthetic_one_candidate([record()], instrument)

    assert result.economic_case_ledger is not None
    lane = result.economic_case_ledger.lane
    assert lane.initial_lane == "F2"
    assert lane.current_lane == "F3"
    assert len(lane.lane_change_events) == 1
    assert lane.lane_change_events[0].value_evidence_used is False
    assert lane.value_prediction_performed is False