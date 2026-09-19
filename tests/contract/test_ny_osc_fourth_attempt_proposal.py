from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_owner_name_file_fourth_bounded_attempt_authorization.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_fourth_attempt_authorization_proposal.schema.json"
)
THIRD_LOCAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_third_attempt_transient_local_approval.v1.json"
)
THIRD_PII = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_third_attempt_transient_pii_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_fourth_attempt_proposal_is_valid_offline_and_not_authorized() -> None:
    proposal = _load(PROPOSAL)
    Draft202012Validator(_load(SCHEMA)).validate(proposal)

    assert proposal["status"] == "PROPOSED_NOT_AUTHORIZED"

    scope = proposal["request_scope"]
    assert scope["repository_only"] is True
    assert scope["source_network_access_performed"] is False
    assert scope["remote_preflight_performed"] is False
    assert scope["download_performed"] is False
    assert scope["owner_file_opened"] is False
    assert scope["owner_pii_processed"] is False


def test_fourth_attempt_proposal_preserves_bounds_and_zero_retry() -> None:
    proposal = _load(PROPOSAL)
    bounds = proposal["proposed_execution_bounds"]

    assert bounds["attempt_number"] == 4
    assert bounds["downloads_max"] == 1
    assert bounds["retries_max"] == 0
    assert bounds["max_download_bytes"] == 450_000_000
    assert bounds["max_uncompressed_bytes"] == 2_000_000_000
    assert bounds["max_archive_members"] == 1
    assert bounds["text_members_required_exactly"] == 1
    assert bounds["expected_documented_field_count"] == 14
    assert bounds["parser_chunk_bytes"] == 65_536
    assert bounds["automatic_widening_allowed"] is False
    assert bounds["automatic_retry_allowed"] is False


def test_fourth_attempt_requires_two_new_ungranted_approvals() -> None:
    proposal = _load(PROPOSAL)
    approvals = proposal["required_human_authorizations"]

    assert len(approvals) == 2
    assert approvals[0]["approval_phrase"] == (
        "APPROVO NY OSC FOURTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert approvals[1]["approval_phrase"] == (
        "APPROVO NY OSC OWNER NAME FILE FOURTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
    )
    for approval in approvals:
        assert approval["status"] == "NOT_GRANTED"
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False


def test_consumed_third_approvals_cannot_be_reused() -> None:
    for approval_path in (THIRD_LOCAL, THIRD_PII):
        approval = _load(approval_path)
        assert approval["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False

    gate = _load(PROPOSAL)["implementation_gate"]
    assert gate["third_attempt_runner_reuse_allowed"] is False
    assert gate["third_attempt_approval_reuse_allowed"] is False
    assert gate["source_access_allowed"] is False
    assert gate["execution_status"] == "BLOCKED_PROPOSAL_ONLY"
