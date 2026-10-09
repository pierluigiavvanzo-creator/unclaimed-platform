from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_owner_name_file_sixth_bounded_attempt_authorization.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_sixth_attempt_authorization_proposal.schema.json"
)
FIFTH_LOCAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_transient_local_approval.v1.json"
)
FIFTH_PII = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_transient_pii_approval.v1.json"
)
FIFTH_RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_execution_result.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_sixth_attempt_proposal_is_valid_offline_and_not_authorized() -> None:
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


def test_sixth_attempt_binds_line_local_runtime_v1_2() -> None:
    proposal = _load(PROPOSAL)
    bounds = proposal["proposed_execution_bounds"]
    runtime = proposal["verified_runtime_capability"]

    assert bounds["attempt_number"] == 6
    assert bounds["downloads_max"] == 1
    assert bounds["retries_max"] == 0
    assert bounds["max_download_bytes"] == 450_000_000
    assert bounds["max_uncompressed_bytes"] == 2_000_000_000
    assert bounds["max_archive_members"] == 1
    assert bounds["expected_documented_field_count"] == 14
    assert bounds["parser_chunk_bytes"] == 65_536
    assert (
        bounds["required_transient_execution_authorization_contract_version"]
        == "1.1.0"
    )
    assert bounds["required_execution_result_contract_version"] == "1.2.0"
    assert bounds["required_quote_dialect_mode"] == "LINE_LOCAL_ARBITRATION"
    assert bounds["required_structural_diagnostic_contract_version"] == "1.0.0"
    assert (
        bounds["required_quote_dialect_diagnostic_contract_version"]
        == "1.0.0"
    )
    assert runtime["implementation_merge_checkpoint"] == (
        "184ffb411837101f78f8041392deabcb35a87695"
    )
    assert runtime["pull_request_number"] == 21
    assert runtime["pr_ci_run_id"] == 35525533661
    assert runtime["post_merge_ci_run_id"] == 35525620771


def test_sixth_attempt_requires_two_new_ungranted_approvals() -> None:
    approvals = _load(PROPOSAL)["required_human_authorizations"]
    assert [approval["status"] for approval in approvals] == [
        "NOT_GRANTED",
        "NOT_GRANTED",
    ]
    assert approvals[0]["approval_phrase"] == (
        "APPROVO NY OSC SIXTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert approvals[1]["approval_phrase"] == (
        "APPROVO NY OSC OWNER NAME FILE SIXTH BOUNDED "
        "TRANSIENT PII ATTEMPT ONCE"
    )
    assert all(approval["single_use"] is True for approval in approvals)
    assert all(approval["reusable"] is False for approval in approvals)
    assert all(approval["retry_authorized"] is False for approval in approvals)


def test_fifth_attempt_is_consumed_and_never_reused() -> None:
    result = _load(FIFTH_RESULT)
    assert result["status"] == "BLOCKED"
    assert result["reason_code"] == "UNEXPECTED_DATA_FIELD_COUNT"

    for approval_path in (FIFTH_LOCAL, FIFTH_PII):
        approval = _load(approval_path)
        assert approval["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False

    gate = _load(PROPOSAL)["implementation_gate"]
    assert gate["fifth_attempt_runner_reuse_allowed"] is False
    assert gate["fifth_attempt_approval_reuse_allowed"] is False
    assert gate["shared_line_local_schema_discovery_reuse_allowed"] is True
    assert gate["shared_transient_execution_bridge_v1_2_reuse_allowed"] is True
    assert gate["source_access_allowed"] is False


def test_sixth_attempt_fresh_preflight_is_separate_and_not_performed() -> None:
    preflight = _load(PROPOSAL)["fresh_preflight"]
    assert preflight["required_immediately_before_execution"] is True
    assert preflight["performed_for_this_proposal"] is False
    assert preflight["remote_access_authorized_by_this_proposal"] is False
    assert preflight["required_result"] == "EXACT_MATCH_OR_STOP"
