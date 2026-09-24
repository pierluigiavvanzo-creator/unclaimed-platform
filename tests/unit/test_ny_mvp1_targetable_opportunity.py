from unclaimed_platform.domain.ny_mvp1_targetable_opportunity import (
    SyntheticTargetabilityEvidence,
    SyntheticTargetingCandidate,
    classify_targetability,
    evaluate_synthetic_targetable_opportunity,
    select_persistence_first_candidate,
)


def candidate(*, ordinal: int, year: int, **overrides):
    data = dict(
        source_record_ordinal=ordinal,
        property_type_code="IN03",
        property_owner_count=1,
        property_id_present=True,
        holder_report_year=year,
    )
    data.update(overrides)
    return SyntheticTargetingCandidate(**data)


def evidence(**overrides):
    data = dict(
        service_need_state="MATERIAL_EVIDENCE",
        resolvability_state="EASY",
        evidence_refs=("synthetic:targetability",),
        targetability_decision_cost_state="MEASURED",
        targetability_decision_cost_cents=125,
    )
    data.update(overrides)
    return SyntheticTargetabilityEvidence(**data)


def test_persistence_first_selects_oldest_report_year_not_first_source_record():
    result = select_persistence_first_candidate(
        [
            candidate(ordinal=10, year=2025),
            candidate(ordinal=20, year=2012),
            candidate(ordinal=30, year=2020),
        ]
    )
    assert result.status == "SELECTED"
    assert result.selected_source_record_ordinal == 20
    assert result.selected_holder_report_year == 2012
    assert result.owner_pii_used_for_ranking is False
    assert result.value_prediction_performed is False


def test_persistence_tie_breaks_by_source_order():
    result = select_persistence_first_candidate(
        [
            candidate(ordinal=30, year=2010),
            candidate(ordinal=20, year=2010),
        ]
    )
    assert result.selected_source_record_ordinal == 20


def test_ineligible_records_are_excluded_without_value_inference():
    result = select_persistence_first_candidate(
        [
            candidate(ordinal=10, year=2010, property_type_code="IN01"),
            candidate(ordinal=20, year=2011, property_owner_count=2),
            candidate(ordinal=30, year=2012, property_id_present=False),
        ]
    )
    assert result.status == "STOPPED_NO_ELIGIBLE_CANDIDATE"
    assert result.eligible_records_count == 0


def test_t0_self_service_likely_is_not_a_value_label():
    result = classify_targetability(
        evidence(service_need_state="LOW_EVIDENCE", resolvability_state="EASY")
    )
    assert result.targetability_class == "T0_SELF_SERVICE_LIKELY"
    assert result.value_prediction_performed is False
    assert result.monetary_value_used_for_targeting is False
    assert result.targetability_score is None


def test_t1_unresolved_locatable_requires_material_need_and_easy_resolution():
    result = classify_targetability(evidence())
    assert result.targetability_class == "T1_UNRESOLVED_BUT_LOCATABLE"
    assert result.recommended_next_scope == "SEPARATE_L3_OUTREACH_REVIEW"
    assert result.awareness_state == "UNKNOWN_UNTIL_OUTREACH"


def test_t2_estate_path_requires_evidence_and_bounded_representative_path():
    result = classify_targetability(
        evidence(
            resolvability_state="BOUNDED",
            estate_path_state="EVIDENCE_PRESENT",
            representative_path_state="BOUNDED_DISCOVERABLE",
        )
    )
    assert result.targetability_class == "T2_ESTATE_OR_REPRESENTATIVE_PATH"


def test_t3_hard_but_bounded_is_not_high_value():
    result = classify_targetability(
        evidence(resolvability_state="BOUNDED")
    )
    assert result.targetability_class == "T3_HARD_BUT_BOUNDED"
    assert result.value_prediction_performed is False


def test_unbounded_resolution_stops():
    result = classify_targetability(
        evidence(resolvability_state="UNBOUNDED")
    )
    assert result.targetability_class == "T4_UNBOUNDED_OR_UNRESOLVED_STOP"
    assert result.recommended_next_scope == "STOP"


def test_insufficient_evidence_does_not_fabricate_t_class():
    result = classify_targetability(
        evidence(
            service_need_state="UNKNOWN",
            resolvability_state="UNKNOWN",
            targetability_decision_cost_state="NOT_MEASURED",
            targetability_decision_cost_cents=None,
        )
    )
    assert result.state == "UNRESOLVED_REQUIRES_L2"
    assert result.targetability_class is None
    assert result.recommended_next_scope == "L2_MINIMAL_TARGETABILITY_DISCOVERY"


def test_friction_lane_is_explicitly_not_used_as_targeting():
    result = classify_targetability(evidence(friction_lane="F3"))
    assert result.friction_lane == "F3"
    assert result.friction_lane_used_as_targeting is False


def test_end_to_end_safety_authorizes_nothing_real():
    result = evaluate_synthetic_targetable_opportunity(
        [candidate(ordinal=1, year=2015)],
        evidence(),
    )
    assert result.safety.synthetic_only is True
    assert result.safety.real_source_accessed is False
    assert result.safety.real_owner_pii_processed is False
    assert result.safety.identity_resolution_performed is False
    assert result.safety.outreach_performed is False
    assert result.safety.value_research_performed is False
    assert result.authorization_granted is False
    assert result.economics_policy.l1_max_new_external_cash_spend_cents == 0
    assert result.economics_policy.l2_incremental_budget_state == (
        "UNSET_REQUIRES_PRODUCT_OWNER"
    )
