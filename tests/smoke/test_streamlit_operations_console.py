from pathlib import Path

import pytest

from unclaimed_platform.api.reviewer import synthetic_operations_snapshot
from unclaimed_platform.ui.streamlit_console import load_safe_snapshot, validate_safe_snapshot

_REPO_ROOT = Path(__file__).resolve().parents[2]


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


def test_streamlit_console_reuses_vercel_visual_language() -> None:
    app_path = _REPO_ROOT / "apps" / "reviewer-streamlit" / "streamlit_app.py"
    theme_path = _REPO_ROOT / "apps" / "reviewer-streamlit" / "theme.css"

    app_source = app_path.read_text(encoding="utf-8")
    theme = theme_path.read_text(encoding="utf-8")

    assert "theme.css" in app_source
    assert "authoritative typed Python read model" in app_source
    assert "st.metric" not in app_source
    assert "st.info" not in app_source
    assert "st.html(page_html)" in app_source
    assert "st.markdown(page_html" not in app_source
    assert "#071018" in theme
    assert "#123148" in theme
    assert "#7ed7c4" in theme
    assert "#f3c67d" in theme
    assert ".uip-mode-card" in theme
    assert ".uip-pill-warn" in theme
