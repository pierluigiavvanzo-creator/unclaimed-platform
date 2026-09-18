from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (\n    ROOT\n    / "sources/proposals"\n    / "ny_osc_owner_name_file_third_bounded_attempt_authorization.v1.json"\n)
SCHEMA = (\n    ROOT\n    / "schemas/common"\n    / "ny_osc_third_attempt_authorization_proposal.schema.json"\n)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_third_attempt_proposal_is_offline_and_not_authorized() -> None:
    proposal = _load(PROPOSAL)
    Draft202012Validator(_load(SCHEMA)).validate(proposal)

    assert proposal["status"] == "PROPOSED_NOT_AUTHORIZED"
    assert proposal["request_scope"] == {
        "repository_only": True,
        "source_network_access_performed": False,
        "download_performed": False,
        "owner_file_opened": False,
        "owner_pii_processed": False,
    }
    assert proposal["fresh_preflight"]["performed_for_this_proposal"] is False
    assert proposal["implementation_gate"]["execution_status"] == (
        "BLOCKED_PENDING_SEPARATE_HUMAN_AUTHORIZATION"
    )
    assert all(
        approval["status"] == "NOT_GRANTED"
        for approval in proposal["required_human_authorizations"]
    )


def test_third_attempt_does_not_reuse_consumed_approvals_or_widen_bounds() -> None:
    proposal = _load(PROPOSAL)
    previous = proposal["preceding_attempt"]
    bounds = proposal["proposed_execution_bounds"]
    gate = proposal["implementation_gate"]

    assert previous["transient_local_approval_consumed"] is True
    assert previous["transient_pii_approval_consumed"] is True
    assert previous["approvals_reusable"] is False
    assert previous["retry_authorized"] is False
    assert gate["second_attempt_runner_reuse_allowed"] is False
    assert gate["second_attempt_approval_reuse_allowed"] is False
    assert bounds["attempt_number"] == 3
    assert bounds["downloads_max"] == 1
    assert bounds["retries_max"] == 0
    assert bounds["max_download_bytes"] == 450_000_000
    assert bounds["max_uncompressed_bytes"] == 2_000_000_000
    assert bounds["automatic_widening_allowed"] is False
    assert bounds["automatic_retry_allowed"] is False
