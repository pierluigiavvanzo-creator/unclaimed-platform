"""Streamlit entrypoint for the governed M3 Operations Console."""

import sys
from pathlib import Path

import streamlit as st

_REPO_ROOT = Path(__file__).resolve().parents[2]
_SRC_DIR = _REPO_ROOT / "src"
_SRC_PATH = str(_SRC_DIR)
if _SRC_PATH not in sys.path:
    sys.path.insert(0, _SRC_PATH)

from unclaimed_platform.ui.streamlit_console import load_safe_snapshot  # noqa: E402

st.set_page_config(page_title="M3 Operations Console", layout="wide")

try:
    snapshot = load_safe_snapshot()
except RuntimeError as exc:
    st.error("Safety boundary violation. Reviewer console stopped.")
    st.code(str(exc))
    st.stop()

st.caption("UNCLAIMED INSURANCE PLATFORM")
st.title("M3 Operations Console")
st.write("Read-only view of provenance, governance and deployment readiness.")
st.info("Safety boundary active: no real acquisition, no beneficiary matching, no real PII.")

left, right = st.columns([2, 1])
with left:
    st.subheader("Milestones")
    milestone_columns = st.columns(len(snapshot.milestones))
    for column, milestone in zip(milestone_columns, snapshot.milestones, strict=True):
        with column:
            st.metric(milestone.id, milestone.status.replace("_", " "))
            st.caption(milestone.label)
with right:
    st.subheader("Data mode")
    st.success(snapshot.mode.replace("_", " "))
    st.caption("Source: authoritative typed Python read model")

source_col, governance_col = st.columns(2)
with source_col:
    st.subheader("Source registry")
    st.metric("Approved real sources", snapshot.source_registry.approved_real_sources)
    st.write(f"Real acquisition: **{snapshot.source_registry.real_acquisition}**")
    st.write(f"Beneficiary matching: **{snapshot.source_registry.beneficiary_matching}**")

with governance_col:
    st.subheader("Governance")
    st.write(f"Privacy gate: **{snapshot.governance.privacy_gate.replace('_', ' ')}**")
    st.write(f"Source approval: **{snapshot.governance.source_approval_gate.replace('_', ' ')}**")
    st.write(f"Retention: **{snapshot.governance.retention_policy}**")
    st.write(f"PII mode: **{snapshot.governance.pii_mode.replace('_', ' ')}**")

artifact_col, audit_col = st.columns(2)
with artifact_col:
    st.subheader("Synthetic raw artifact")
    st.code(snapshot.raw_artifact.artifact_id)
    st.write(f"SHA-256: `{snapshot.raw_artifact.sha256}`")
    st.write(f"Provenance SHA-256: `{snapshot.raw_artifact.provenance_sha256}`")
    st.write(f"Bytes: **{snapshot.raw_artifact.byte_count}**")
    st.write(f"Source: `{snapshot.raw_artifact.source_uri}`")

with audit_col:
    st.subheader("Audit & platform")
    st.write(f"Audit chain: **{snapshot.audit.chain.replace('_', ' ')}**")
    st.write(f"Algorithm: **{snapshot.audit.algorithm}**")
    st.write(f"Durable audit backend: **{snapshot.audit.durable_backend}**")
    st.write("Deployment target: **STREAMLIT COMMUNITY CLOUD CANDIDATE**")
    st.write(f"Supabase: **{snapshot.platform.supabase.replace('_', ' ')}**")

st.divider()
st.caption(
    f"Contract v{snapshot.contract_version} · Synthetic reviewer surface · "
    "deterministic governance remains authoritative"
)
