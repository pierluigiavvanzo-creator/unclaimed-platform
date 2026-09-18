"""Streamlit entrypoint for the governed MVP-1 reviewer deployment candidate."""

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
    load_safe_mvp1_economics,
    load_safe_mvp1_integrated_economics,
    load_safe_snapshot,
)


def _display(value: str) -> str:
    return escape(value.replace("_", " "))


def _usd_cents(value: int | None) -> str:
    if value is None:
        return "UNAVAILABLE"
    return f"$ {value / 100:,.2f}"


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


st.set_page_config(page_title="MVP-1 Reviewer Console", layout="wide")

try:
    snapshot = load_safe_snapshot()
    mvp1_case = load_safe_mvp1_case()
    mvp1_economics = load_safe_mvp1_economics()
    mvp1_integrated = load_safe_mvp1_integrated_economics()
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
        _row(
            "Recoverable value",
            mvp1_economics.recoverable_value_state.replace("_", " "),
        ),
        _row("Owner file amount", "NOT DISCLOSED"),
        _row(
            "Statutory fee cap",
            f"{mvp1_economics.statutory_fee_cap_bps / 100:.0f}% MAXIMUM — APL 1416 SCOPE",
        ),
        _row("Actual fee rate", "NOT ESTABLISHED"),
        _row("Follow-up cost", mvp1_economics.cost_measurement_state.replace("_", " ")),
        _row(
            "Economic actionability",
            mvp1_economics.commercial_actionability.replace("_", " "),
        ),
        _row(
            "Reviewer decision",
            mvp1_economics.reviewer_decision_required.replace("_", " "),
        ),
    ]
)


ready_result = mvp1_integrated.ready.integration.explicit_economics_result
ready_rows = "".join(
    [
        _row(
            "Integration state",
            mvp1_integrated.ready.integration.integration_state.replace("_", " "),
        ),
        _row(
            "Fully loaded follow-up cost — synthetic",
            _usd_cents(mvp1_integrated.ready.integration.measured_follow_up_cost_cents),
        ),
        _row(
            "Gross fee — synthetic",
            _usd_cents(None if ready_result is None else ready_result.gross_fee_cents),
        ),
        _row(
            "Contribution before overhead — synthetic",
            _usd_cents(
                None
                if ready_result is None
                else ready_result.contribution_before_overhead_cents
            ),
        ),
        _row(
            "Cost evidence refs",
            str(len(mvp1_integrated.ready.integration.follow_up_cost_evidence_refs)),
        ),
        _row("Automatic recommendation", "NONE — HUMAN DECISION REQUIRED"),
    ]
)

blocked_rows = "".join(
    [
        _row(
            "Integration state",
            mvp1_integrated.blocked.integration.integration_state.replace("_", " "),
        ),
        _row(
            "Human labor rate",
            mvp1_integrated.blocked.follow_up_cost.human_labor_rate_state.replace("_", " "),
        ),
        _row(
            "Direct machine/data cost — synthetic",
            _usd_cents(
                mvp1_integrated.blocked.follow_up_cost.direct_machine_and_data_cost_cents
            )
            + " — NOT FULLY LOADED",
        ),
        _row("Fully loaded follow-up cost", "UNAVAILABLE"),
        _row("Explicit economics result", "NOT COMPUTED — FAIL CLOSED"),
        _row(
            "Cost evidence refs",
            str(len(mvp1_integrated.blocked.integration.follow_up_cost_evidence_refs)),
        ),
        _row("Automatic recommendation", "NONE — HUMAN DECISION REQUIRED"),
    ]
)

page_html = f"""
<div class="uip-shell">
  <header class="uip-hero">
    <div>
      <p class="uip-eyebrow">UNCLAIMED INSURANCE PLATFORM</p>
      <h1 class="uip-title">MVP-1 Reviewer Console</h1>
      <p class="uip-lede">Synthetic/test-only review of NY IN03 candidate economics, provenance and governance.</p>
    </div>
    <div class="uip-mode-card">
      <span>Data mode</span>
      <strong>{_display(snapshot.mode)}</strong>
      <small>Source: authoritative typed Python read model</small>
    </div>
  </header>

  <section class="uip-alert">
    <strong>Synthetic/test-only deployment candidate.</strong>
    <span>No real acquisition, no Owner Name File download, no beneficiary matching, no real PII.</span>
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
      <p class="uip-eyebrow">NY PRE-CONTACT ECONOMICS</p>
      <h2>Fail-closed value, fee and cost evidence</h2>
      <div class="uip-list">{mvp1_economics_rows}</div>
    </article>
  </section>


  <section class="uip-grid uip-two-col">
    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">MVP-1 INTEGRATED ECONOMICS — SYNTHETIC TEST</p>
      <h2>Ready: documented fully loaded cost</h2>
      <div class="uip-list">{ready_rows}</div>
    </article>

    <article class="uip-card uip-feature-card">
      <p class="uip-eyebrow">MVP-1 INTEGRATED ECONOMICS — SYNTHETIC TEST / FAIL CLOSED</p>
      <h2>Blocked: labor rate/cost incomplete</h2>
      <div class="uip-list">{blocked_rows}</div>
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
    Contract v{escape(snapshot.contract_version)} · MVP-1 synthetic/test-only deployment candidate ·
    deterministic governance remains authoritative
  </footer>
</div>
"""

st.html(page_html)
