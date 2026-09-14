"""Safe read model adapter for the Streamlit M3 Operations Console."""

from unclaimed_platform.api.reviewer import OperationsSnapshot, synthetic_operations_snapshot


def validate_safe_snapshot(snapshot: OperationsSnapshot) -> OperationsSnapshot:
    """Fail closed if the reviewer snapshot violates M3 safety invariants."""
    violations: list[str] = []

    if snapshot.contract_version != "1.0.0":
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
