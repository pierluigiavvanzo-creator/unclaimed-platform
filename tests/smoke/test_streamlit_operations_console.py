import pytest

from unclaimed_platform.api.reviewer import synthetic_operations_snapshot
from unclaimed_platform.ui.streamlit_console import load_safe_snapshot, validate_safe_snapshot


def test_streamlit_snapshot_preserves_m3_safety_boundaries() -> None:
    snapshot = load_safe_snapshot()

    assert snapshot.contract_version == "1.0.0"
    assert snapshot.mode == "SYNTHETIC_READ_ONLY"
    assert snapshot.source_registry.approved_real_sources == 0
    assert snapshot.source_registry.real_acquisition == "BLOCKED"
    assert snapshot.source_registry.beneficiary_matching == "BLOCKED"
    assert snapshot.governance.pii_mode == "NO_REAL_PII"
    assert snapshot.raw_artifact.synthetic is True
    assert snapshot.raw_artifact.immutable is True


def test_streamlit_snapshot_fails_closed_if_real_source_is_approved() -> None:
    snapshot = synthetic_operations_snapshot()
    unsafe_source_registry = snapshot.source_registry.model_copy(
        update={"approved_real_sources": 1}
    )
    unsafe_snapshot = snapshot.model_copy(update={"source_registry": unsafe_source_registry})

    with pytest.raises(RuntimeError, match="approved real sources must remain zero"):
        validate_safe_snapshot(unsafe_snapshot)
