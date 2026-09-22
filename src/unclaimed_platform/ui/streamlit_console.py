"""Safe read model adapters for the Streamlit reviewer surfaces."""

from unclaimed_platform.api.reviewer import (
    Mvp1IntegratedEconomicsReviewerSnapshot,
    OperationsSnapshot,
    synthetic_mvp1_integrated_economics_snapshot,
    synthetic_operations_snapshot,
)
from unclaimed_platform.domain.mvp1_vertical_slice import (
    Mvp1SyntheticCaseReview,
    synthetic_ny_mvp1_case_review,
)
from unclaimed_platform.domain.ny_mvp1_value_evidence import (
    NyMvp1PrecontactEconomicsEvidence,
    ny_mvp1_precontact_economics_evidence,
)


def validate_safe_snapshot(snapshot: OperationsSnapshot) -> OperationsSnapshot:
    """Fail closed if the reviewer snapshot violates M3 safety invariants."""
    violations: list[str] = []

    if snapshot.contract_version != "2.0.0":
        violations.append("unexpected contract version")
    if snapshot.mode != "SYNTHETIC_READ_ONLY":
        violations.append("reviewer mode is not synthetic read-only")
    if snapshot.source_registry.approved_real_sources != 0:
        violations.append("approved real sources must remain zero")
    if snapshot.source_registry.real_acquisition != "BLOCKED":
        violations.append("real acquisition must remain blocked")
    if snapshot.source_registry.beneficiary_matching != "BLOCKED":
        violations.append("beneficiary matching must remain blocked")
    if snapshot.governance.pii_mode != "NO_REAL_PII":
        violations.append("real PII must remain disabled")
    if not snapshot.raw_artifact.synthetic:
        violations.append("raw artifact must remain synthetic")
    if not snapshot.raw_artifact.immutable:
        violations.append("raw artifact must remain immutable")

    if violations:
        raise RuntimeError("Unsafe reviewer snapshot: " + "; ".join(violations))

    return snapshot


def load_safe_snapshot() -> OperationsSnapshot:
    """Load the current governed synthetic snapshot and validate it before display."""
    return validate_safe_snapshot(synthetic_operations_snapshot())


def validate_safe_mvp1_case(case: Mvp1SyntheticCaseReview) -> Mvp1SyntheticCaseReview:
    """Fail closed if the synthetic MVP-1 case crosses any real-data boundary."""
    violations: list[str] = []

    if case.contract_version != "1.0.0":
        violations.append("unexpected MVP-1 contract version")
    if case.mode != "SYNTHETIC_READ_ONLY":
        violations.append("MVP-1 case mode is not synthetic read-only")
    if case.source_state != "REGISTERED_CANDIDATE_UNAPPROVED_NOT_ACQUIRED":
        violations.append("New York source must remain unapproved and unacquired")
    if case.classification.authority_code != "IN03" or not case.classification.primary_target:
        violations.append("synthetic MVP-1 reviewer case must remain exact IN03 primary target")
    if case.candidate.status != "CREATED":
        violations.append("synthetic MVP-1 candidate must be created")
    if case.economics.recoverable_value_state != "UNKNOWN_FROM_SOURCE":
        violations.append("recoverable value must remain unknown from source")
    if case.economics.invented_amounts:
        violations.append("invented monetary amounts are forbidden")
    if case.economics.commercial_threshold_applied:
        violations.append("commercial threshold must not be invented or applied")
    if case.provenance.real_source_accessed:
        violations.append("real source access is forbidden in synthetic vertical slice")

    safety = case.safety
    if safety.owner_file_downloaded:
        violations.append("owner file download is forbidden in synthetic vertical slice")
    if safety.real_owner_pii_processed:
        violations.append("real owner PII is forbidden in synthetic vertical slice")
    if safety.identity_resolution_performed:
        violations.append("identity resolution is forbidden in synthetic vertical slice")
    if safety.beneficiary_matching_performed:
        violations.append("beneficiary matching is forbidden in synthetic vertical slice")
    if safety.outreach_performed:
        violations.append("outreach is forbidden in synthetic vertical slice")
    if safety.representation_performed:
        violations.append("representation is forbidden in synthetic vertical slice")
    if safety.claim_activity_performed:
        violations.append("claim activity is forbidden in synthetic vertical slice")

    if violations:
        raise RuntimeError("Unsafe MVP-1 synthetic case: " + "; ".join(violations))

    return case


def load_safe_mvp1_case() -> Mvp1SyntheticCaseReview:
    """Load and validate the deterministic synthetic MVP-1 case-review slice."""
    return validate_safe_mvp1_case(synthetic_ny_mvp1_case_review())


def validate_safe_mvp1_economics(
    evidence: NyMvp1PrecontactEconomicsEvidence,
) -> NyMvp1PrecontactEconomicsEvidence:
    """Fail closed if pre-contact economics starts implying unsupported value or fees."""
    violations: list[str] = []

    if evidence.contract_version != "1.0.0":
        violations.append("unexpected NY economics contract version")
    if evidence.mode != "OFFLINE_PRECONTACT_EVIDENCE":
        violations.append("NY economics mode is not offline pre-contact evidence")
    if evidence.exact_recoverable_value_cents is not None:
        violations.append("exact recoverable value must remain unavailable pre-contact")
    if evidence.owner_file_discloses_amount:
        violations.append("Owner Name File must not be represented as disclosing amount")
    if evidence.statutory_fee_cap_bps != 1500:
        violations.append("unexpected statutory fee cap")
    if evidence.actual_fee_bps is not None:
        violations.append("actual fee rate must remain unsupported pre-contact")
    if evidence.expected_follow_up_cost_cents is not None:
        violations.append("follow-up cost must remain unmeasured until evidence exists")
    if evidence.commercial_actionability != "NOT_COMPUTABLE_PRE_CONTACT":
        violations.append("commercial actionability must remain not computable pre-contact")
    if not evidence.fee_applicability_requires_legal_review:
        violations.append("fee-rule applicability must remain subject to legal review")

    if violations:
        raise RuntimeError("Unsafe NY MVP-1 economics evidence: " + "; ".join(violations))

    return evidence


def load_safe_mvp1_economics() -> NyMvp1PrecontactEconomicsEvidence:
    """Load and validate the current fail-closed pre-contact economics evidence."""
    return validate_safe_mvp1_economics(ny_mvp1_precontact_economics_evidence())


def validate_safe_mvp1_integrated_economics(
    snapshot: Mvp1IntegratedEconomicsReviewerSnapshot,
) -> Mvp1IntegratedEconomicsReviewerSnapshot:
    """Fail closed if integrated economics reviewer states blur synthetic safety boundaries."""
    violations: list[str] = []

    if snapshot.contract_version != "1.0.0":
        violations.append("unexpected integrated economics contract version")
    if snapshot.mode != "SYNTHETIC_READ_ONLY":
        violations.append("integrated economics reviewer must remain synthetic read-only")

    safety = snapshot.safety
    if safety.real_source_accessed:
        violations.append("real source access is forbidden")
    if safety.owner_file_downloaded:
        violations.append("Owner Name File download is forbidden")
    if safety.real_owner_pii_processed:
        violations.append("real owner PII is forbidden")
    if safety.automatic_commercial_recommendation:
        violations.append("automatic commercial recommendation is forbidden")

    ready = snapshot.ready
    if ready.scenario != "READY_WITH_DOCUMENTED_LABOR_RATE":
        violations.append("ready scenario marker is invalid")
    if ready.follow_up_cost.fully_loaded_follow_up_cost_state != (
        "COMPUTED_FROM_MEASURED_COMPONENTS"
    ):
        violations.append("ready scenario requires computed fully loaded cost")
    if ready.integration.integration_state != "READY_FOR_EXPLICIT_ECONOMICS":
        violations.append("ready scenario must reach explicit economics")
    if ready.integration.measured_follow_up_cost_cents is None:
        violations.append("ready scenario requires measured fully loaded cost")
    if ready.integration.explicit_economics_result is None:
        violations.append("ready scenario requires explicit economics result")
    if not ready.integration.no_commercial_recommendation:
        violations.append("ready scenario cannot add automatic commercial recommendation")

    blocked = snapshot.blocked
    if blocked.scenario != "BLOCKED_WITHOUT_DOCUMENTED_LABOR_RATE":
        violations.append("blocked scenario marker is invalid")
    if blocked.follow_up_cost.fully_loaded_follow_up_cost_state != (
        "NOT_COMPUTABLE_NO_LABOR_RATE"
    ):
        violations.append("blocked scenario must preserve missing labor-rate state")
    if blocked.integration.integration_state != "BLOCKED_FOLLOW_UP_COST_UNAVAILABLE":
        violations.append("blocked scenario must remain fail closed")
    if blocked.integration.measured_follow_up_cost_cents is not None:
        violations.append("blocked scenario cannot expose substitute follow-up cost")
    if blocked.integration.explicit_economics_result is not None:
        violations.append("blocked scenario cannot compute explicit economics")
    if not blocked.integration.no_commercial_recommendation:
        violations.append("blocked scenario cannot add automatic commercial recommendation")

    if violations:
        raise RuntimeError(
            "Unsafe NY MVP-1 integrated economics reviewer: " + "; ".join(violations)
        )

    return snapshot


def load_safe_mvp1_integrated_economics(
) -> Mvp1IntegratedEconomicsReviewerSnapshot:
    """Load deterministic synthetic integrated economics and validate before display."""
    return validate_safe_mvp1_integrated_economics(
        synthetic_mvp1_integrated_economics_snapshot()
    )
