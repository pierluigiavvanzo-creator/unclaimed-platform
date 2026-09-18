"""Streamlit entrypoint for the governed M3 Operations Console."""

from __future__ import annotations

import sys
from html import escape
from pathlib import Path

import streamlit as st

_REPO_ROOT = Path(__file__).resolve().parents[2]
_SRC_DIR = _REPO_ROOT / "src"
_SRC_PATH = str(_SRC_DIR)
if _SRC_PATH not in sys.path:
    sys.path.insert(0, _SRC_PATH)

from unclaimed_platform.ui.streamlit_console import (  # noqa: E402
    load_safe_mvp1_case,
    load_safe_snapshot,
)


def _display(value: str) -> str:
    return escape(value.replace("_", " "))


def _pill(value: str) -> str:
    normalized = value.replace("_", " ")
    warn = "BLOCKED" in value or value in {"PENDING", "NOT_CONNECTED"}
    tone = "warn" if warn else "ok"
    return f'<span class="uip-pill uip-pill-{tone}">{escape(normalized)}</span>'


def _row(label: str, value: str, *, mono: bool = False) -> str:
    value_class = "uip-row-value uip-mono" if mono else "uip-row-value"
    return (
        '<div class="uip-row">'
        f'<span class="uip-row-label">{escape(label)}</span>'
        f'<span class="{value_class}">{escape(value)}</span>'
        "</div>"
    )


st.set_page_config(page_title="M3 Operations Console", layout="wide")

try:
    snapshot = load_safe_snapshot()
    mvp1_case = load_safe_mvp1_case()
except RuntimeError as exc:
    st.error("Safety boundary violation. Reviewer console stopped.")
    st.code(str(exc))
    st.stop()

_theme_css = (Path(__file__).with_name("theme.css")).read_text(encoding="utf-8")
st.html(f"<style>{_theme_css}</style>")

milestones_html = "".join(
    (
        '<article class="uip-card">'
        '<div class="uip-card-top">'
        f"<span>{escape(milestone.id)}</span>"
        f"{_pill(milestone.status)}"
        "</div>"
        f"<h2>{escape(milestone.label)}</h2>"
        "</article>"
    )
    for milestone in snapshot.milestones
)

governance_rows = "".join(
    [
        _row("Privacy gate", snapshot.governance.privacy_gate.replace("_", " ")),
        _row("Source approval", snapshot.governance.source_approval_gate.replace("_", " ")),
        _row("Retention", snapshot.governance.retention_policy),
        _row("PII mode", snapshot.governance.pii_mode.replace("_", " ")),
    ]
)

artifact_rows = "".join(
    [
        _row("SHA-256", snapshot.raw_artifact.sha256, mono=True),
        _row("Provenance SHA-256", snapshot.raw_artifact.provenance_sha256, mono=True),
        _row("Bytes", str(snapshot.raw_artifact.byte_count)),
        _row("Source", snapshot.raw_artifact.source_uri, mono=True),
    ]
)

audit_rows = "".join(
    [
        _row("Audit chain", snapshot.audit.chain.replace("_", " ")),
        _row("Algorithm", snapshot.audit.algorithm),
        _row("Durable audit backend", snapshot.audit.durable_backend),
        _row("Deployment target", "STREAMLIT COMMUNITY CLOUD"),
        _row("Supabase", snapshot.platform.supabase.replace("_", " ")),
    ]
)

mvp1_case_rows = "".join(
    [
        _row("Property type", mvp1_case.classification.authority_code or "NONE", mono=True),
        _row("Classification", mvp1_case.classification.status.replace("_", " ")),
        _row("Case ID", mvp1_case.candidate.case_id or "NOT CREATED", mono=True),
        _row("Source record", mvp1_case.candidate.source_record_ref, mono=True),
        _row("Input boundary", mvp1_case.provenance.input_boundary.replace("_", " ")),
    ]
)

mvp1_economics_rows = "".join(
    [
        _row("Recoverable value", mvp1_case.economics.recoverable_value_state.replace("_", " ")),
        _row("Fee basis", mvp1_case.economics.fee_basis_state.replace("_", " ")),
        _row(
            "Economic actionability",
            mvp1_case.economics.economic_actionability.replace("_", " "),
        ),
        _row(
            "Reviewer decision",
            mvp1_case.reviewer_decision_required.replace("_", " "),
        ),
    ]
)

page_html = f"""
<div class="uip-shell">
  <header class="uip-hero">
    <div>
      <p class="uip-eyebrow">UNCLAIMED INSURANCE PLATFORM</p>
      <h1 class="uip-title">M3 Operations Console</h1>
      <p class="uip-lede">A read-only view of provenance, governance and deployment readiness.</p>
    </div>
    <div class="uip-mode-card">
      <span>Data mode</span>
      <strong>{_display(snapshot.mode)}</strong>
      <small>Source: authoritative typed Python read model</small>
    </div>
  </header>

  <section class="uip-alert">
    <strong>Safety boundary active.</strong>
    <span>No real acquisition, no beneficiary matching, no real PII.</span>
  </section>

  <section class="uip-grid uip-milestones">
    {milestones_html}
  </section>

  <section class="uip-grid uip-two-col">
    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">MVP-1 SYNTHETIC CASE</p>
      <h2>NY IN03 vertical slice</h2>
      <div class="uip-list">{mvp1_case_rows}</div>
    </article>

    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">CASE ECONOMICS</p>
      <h2>Value evidence is the next commercial blocker</h2>
      <div class="uip-list">{mvp1_economics_rows}</div>
    </article>
  </section>

  <section class="uip-grid uip-two-col">
    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">SOURCE REGISTRY</p>
      <div class="uip-metric">{snapshot.source_registry.approved_real_sources}</div>
      <p>Approved real sources</p>
      <div class="uip-list">
        <div class="uip-row">
          <span class="uip-row-label">Real acquisition</span>
          <span class="uip-row-value">{_pill(snapshot.source_registry.real_acquisition)}</span>
        </div>
        <div class="uip-row">
          <span class="uip-row-label">Beneficiary matching</span>
          <span class="uip-row-value">{_pill(snapshot.source_registry.beneficiary_matching)}</span>
        </div>
      </div>
    </article>

    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">GOVERNANCE</p>
      <div class="uip-list">{governance_rows}</div>
    </article>
  </section>

  <section class="uip-grid uip-two-col">
    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">SYNTHETIC RAW ARTIFACT</p>
      <h2>{escape(snapshot.raw_artifact.artifact_id)}</h2>
      <div class="uip-list">{artifact_rows}</div>
    </article>

    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">AUDIT &amp; PLATFORM</p>
      <div class="uip-list">{audit_rows}</div>
    </article>
  </section>

  <footer class="uip-footer">
    Contract v{escape(snapshot.contract_version)} · Synthetic reviewer surface ·
    deterministic governance remains authoritative
  </footer>
</div>
"""

st.html(page_html)
