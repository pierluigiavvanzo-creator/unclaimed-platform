from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
TRIGGER_PATH = (
    ROOT / ".github/ca-sco-property-type-semantic-verification-once.trigger.json"
)
AUTH_PATH = (
    ROOT
    / "docs/audits/"
    "M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_"
    "V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION.md"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus."
    "property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json"
)
EXECUTION_REF = (
    "OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_"
    "REAL_SOURCE_EXECUTION_BOUNDED_A2139884"
)
PRIVACY_REF = (
    "OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_"
    "TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884"
)
AUTHORIZED_BASE = "5872db1368a5b9a2cdee79a0c2e54aa0b9b00dfa"
REVIEWED_PROPOSAL_SHA = "a2139884d99bcd0bd1c06ea7374778347bbd64b1"
EXECUTION_BRANCH = (
    "m3-ca-sco-property-type-nonconforming-row-handling-policy-"
    "v1-2-real-source-execution-once"
)


def test_authorized_execution_stage_workflow_is_exactly_bounded() -> None:
    assert WORKFLOW_PATH.exists()
    text = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert EXECUTION_BRANCH in text
    assert f"--approval-ref {EXECUTION_REF}" in text
    assert f"--privacy-approval-ref {PRIVACY_REF}" in text
    assert "property_type_semantic_verification_execution.v1_2.schema.json" in text
    assert "--live-network" in text
    assert "GITHUB_RUN_ATTEMPT" in text
    assert "automatic/manual retry is not authorized" in text
    assert "if: steps.gate.outputs.execute == 'true'" in text
    assert "workflow_dispatch" not in text
    assert "retention-days: 7" in text
    assert "total_body_bytes_read'] <= 524288" in text
    assert "sample_rows_examined'] <= 16" in text
    assert "PROPERTY_TYPE_NONCONFORMING_STOPPED" in text
    assert "PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE" in text


def test_execution_stage_uses_fresh_unconsumed_authorization() -> None:
    auth_text = AUTH_PATH.read_text(encoding="utf-8")
    assert EXECUTION_REF in auth_text
    assert PRIVACY_REF in auth_text
    assert "GRANTED_NOT_CONSUMED" in auth_text
    assert REVIEWED_PROPOSAL_SHA in auth_text
    assert "runtime contract: `1.2.0`" in auth_text
    assert "No automatic retry is authorized" in auth_text

    proposal = json.loads(PROPOSAL_PATH.read_text(encoding="utf-8"))
    assert proposal["proposal_version"] == "1.0.0"
    assert proposal["base_state"]["execution_schema_version"] == "1.2.0"
    assert proposal["transport_caps"]["http_requests_max_total"] == 5
    assert proposal["transport_caps"]["automatic_widening_allowed"] is False
    assert proposal["v1_2_outcome_contract"][
        "source_continuation_after_property_type_format_unexpected"
    ] is False


def test_optional_execution_trigger_is_exact_if_present() -> None:
    if not TRIGGER_PATH.exists():
        return

    marker = json.loads(TRIGGER_PATH.read_text(encoding="utf-8"))
    assert marker == {
        "authorization_checkpoint_sha": AUTHORIZED_BASE,
        "execution_approval_ref": EXECUTION_REF,
        "privacy_approval_ref": PRIVACY_REF,
        "reviewed_proposal_sha": REVIEWED_PROPOSAL_SHA,
        "runtime_contract": "1.2.0",
        "single_use": True,
    }
