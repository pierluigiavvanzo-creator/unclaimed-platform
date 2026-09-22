from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_owner_name_file_fifth_bounded_attempt_authorization.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_fifth_attempt_authorization_proposal.schema.json"
)
FOURTH_LOCAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fourth_attempt_transient_local_approval.v1.json"
)
FOURTH_PII = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fourth_attempt_transient_pii_approval.v1.json"
)
FOURTH_RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fourth_attempt_execution_result.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_fifth_attempt_proposal_is_valid_offline_and_not_authorized() -> None:
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


def test_fifth_attempt_preserves_bounds_and_requires_diagnostic_bridge() -> None:
    proposal = _load(PROPOSAL)
    bounds = proposal["proposed_execution_bounds"]
    diagnostic = proposal["diagnostic_objective"]

    assert bounds["attempt_number"] == 5
    assert bounds["downloads_max"] == 1
    assert bounds["retries_max"] == 0
    assert bounds["max_download_bytes"] == 450_000_000
    assert bounds["max_uncompressed_bytes"] == 2_000_000_000
    assert bounds["max_archive_members"] == 1
    assert bounds["expected_documented_field_count"] == 14
    assert bounds["parser_chunk_bytes"] == 65_536
    assert bounds["required_execution_result_contract_version"] == "1.1.0"
    assert bounds["required_structural_diagnostic_contract_version"] == "1.0.0"
    assert diagnostic["structural_diagnostic_required_when_triggered"] is True
    assert diagnostic["automatic_row_repair_allowed"] is False
    assert diagnostic["automatic_row_skip_allowed"] is False
    assert diagnostic["automatic_parser_widening_allowed"] is False
    assert diagnostic["automatic_source_acceptance_allowed"] is False
    assert diagnostic["automatic_retry_allowed"] is False


def test_fifth_attempt_requires_two_new_ungranted_approvals() -> None:
    approvals = _load(PROPOSAL)["required_human_authorizations"]

    assert [approval["status"] for approval in approvals] == [
        "NOT_GRANTED",
        "NOT_GRANTED",
    ]
    assert approvals[0]["approval_phrase"] == (
        "APPROVO NY OSC FIFTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert approvals[1]["approval_phrase"] == (
        "APPROVO NY OSC OWNER NAME FILE FIFTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
    )
    assert all(approval["single_use"] is True for approval in approvals)
    assert all(approval["reusable"] is False for approval in approvals)
    assert all(approval["retry_authorized"] is False for approval in approvals)


def test_fourth_attempt_is_consumed_and_not_reused() -> None:
    result = _load(FOURTH_RESULT)
    assert result["status"] == "BLOCKED"
    assert result["reason_code"] == "UNEXPECTED_DATA_FIELD_COUNT"
    assert result["schema_result"]["observed_data_field_count"] == 13
    assert result["schema_result"]["aggregate_complete_record_count"] == 213_454

    for approval_path in (FOURTH_LOCAL, FOURTH_PII):
        approval = _load(approval_path)
        assert approval["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False

    gate = _load(PROPOSAL)["implementation_gate"]
    assert gate["fourth_attempt_runner_reuse_allowed"] is False
    assert gate["fourth_attempt_approval_reuse_allowed"] is False
    assert gate["shared_schema_discovery_parser_reuse_allowed"] is True
    assert gate["shared_transient_execution_bridge_v1_1_reuse_allowed"] is True
    assert gate["source_access_allowed"] is False
    assert gate["execution_status"] == "BLOCKED_PROPOSAL_ONLY"
