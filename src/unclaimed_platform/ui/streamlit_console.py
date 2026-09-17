"""Safe read model adapters for the Streamlit reviewer surfaces."""

from unclaimed_platform.api.reviewer import OperationsSnapshot, synthetic_operations_snapshot
from unclaimed_platform.domain.mvp1_vertical_slice import (
    Mvp1SyntheticCaseReview,
    synthetic_ny_mvp1_case_review,
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
