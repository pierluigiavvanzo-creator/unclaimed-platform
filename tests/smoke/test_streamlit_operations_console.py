from pathlib import Path

import pytest

from unclaimed_platform.api.reviewer import synthetic_operations_snapshot
from unclaimed_platform.ui.streamlit_console import (
    load_safe_mvp1_case,
    load_safe_mvp1_economics,
    load_safe_snapshot,
    validate_safe_mvp1_case,
    validate_safe_mvp1_economics,
    validate_safe_snapshot,
)

_REPO_ROOT = Path(__file__).resolve().parents[2]


def test_streamlit_snapshot_preserves_m3_safety_boundaries() -> None:
    snapshot = load_safe_snapshot()

    assert snapshot.contract_version == "2.0.0"
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


def test_streamlit_mvp1_case_preserves_synthetic_safety_boundaries() -> None:
    case = load_safe_mvp1_case()

    assert case.mode == "SYNTHETIC_READ_ONLY"
    assert case.classification.authority_code == "IN03"
    assert case.classification.primary_target is True
    assert case.candidate.status == "CREATED"
    assert case.economics.recoverable_value_state == "UNKNOWN_FROM_SOURCE"
    assert case.economics.invented_amounts is False
    assert case.provenance.real_source_accessed is False
    assert case.safety.owner_file_downloaded is False
    assert case.safety.real_owner_pii_processed is False


def test_streamlit_mvp1_case_fails_closed_on_real_source_access() -> None:
    case = load_safe_mvp1_case()
    unsafe_provenance = case.provenance.model_copy(update={"real_source_accessed": True})
    unsafe_case = case.model_copy(update={"provenance": unsafe_provenance})

    with pytest.raises(RuntimeError, match="real source access is forbidden"):
        validate_safe_mvp1_case(unsafe_case)




def test_streamlit_mvp1_economics_preserves_precontact_fail_closed_state() -> None:
    evidence = load_safe_mvp1_economics()

    assert evidence.mode == "OFFLINE_PRECONTACT_EVIDENCE"
    assert evidence.exact_recoverable_value_cents is None
    assert evidence.owner_file_discloses_amount is False
    assert evidence.statutory_fee_cap_bps == 1500
    assert evidence.actual_fee_bps is None
    assert evidence.expected_follow_up_cost_cents is None
    assert evidence.commercial_actionability == "NOT_COMPUTABLE_PRE_CONTACT"


def test_streamlit_mvp1_economics_fails_closed_on_invented_value() -> None:
    evidence = load_safe_mvp1_economics()
    unsafe = evidence.model_copy(update={"exact_recoverable_value_cents": 100_000})

    with pytest.raises(RuntimeError, match="exact recoverable value"):
        validate_safe_mvp1_economics(unsafe)

def test_streamlit_console_preserves_verified_visual_language() -> None:
    app_path = _REPO_ROOT / "apps" / "reviewer-streamlit" / "streamlit_app.py"
    theme_path = _REPO_ROOT / "apps" / "reviewer-streamlit" / "theme.css"

    app_source = app_path.read_text(encoding="utf-8")
    theme = theme_path.read_text(encoding="utf-8")

    assert "theme.css" in app_source
    assert "authoritative typed Python read model" in app_source
    assert "MVP-1 SYNTHETIC CASE" in app_source
    assert "NY PRE-CONTACT ECONOMICS" in app_source
    assert "Statutory fee cap" in app_source
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
    assert "white-space: nowrap" in theme
    assert 'data-testid="stToolbar"' in theme
    assert 'data-testid="stStatusWidget"' in theme
    assert 'data-testid="stAppDeployButton"' in theme
