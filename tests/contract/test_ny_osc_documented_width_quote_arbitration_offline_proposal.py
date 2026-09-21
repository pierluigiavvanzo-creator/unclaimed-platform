from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_documented_width_quote_arbitration_offline_proposal.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_documented_width_quote_arbitration_offline_proposal.schema.json"
)
FIFTH_RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_fifth_attempt_execution_result.v1.json"
)
SIXTH_RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_execution_result.v1.json"
)
SIXTH_LOCAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_local_approval.v1.json"
)
SIXTH_PII = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_pii_approval.v1.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_documented_width_proposal_validates_and_is_offline_only() -> None:
    proposal = _load(PROPOSAL)
    Draft202012Validator(_load(SCHEMA)).validate(proposal)

    assert proposal["status"] == "PROPOSED_NOT_IMPLEMENTED"
    scope = proposal["request_scope"]
    assert scope["repository_only"] is True
    assert scope["source_network_access_performed"] is False
    assert scope["download_performed"] is False
    assert scope["parser_modified"] is False
    assert scope["runtime_activated"] is False
    assert scope["seventh_attempt_prepared"] is False


def test_proposal_binds_fifth_and_sixth_structural_evidence() -> None:
    proposal = _load(PROPOSAL)
    evidence = proposal["evidence_basis"]
    fifth = _load(FIFTH_RESULT)
    sixth = _load(SIXTH_RESULT)

    fifth_diagnostic = fifth["structural_diagnostic"]
    assert fifth_diagnostic["physical_line_breaks_inside_quotes"] == 17_543
    assert fifth_diagnostic["raw_pipe_count"] == 228_072
    assert evidence["fifth_verified_identity"] == (
        "(17543 + 1) * 13 = 228072"
    )

    sixth_diagnostic = sixth["quote_dialect_diagnostic"]
    assert sixth["reason_code"] == "QUOTE_DIALECT_AMBIGUOUS"
    assert sixth_diagnostic["raw_field_count"] == 14
    assert sixth_diagnostic["quote_aware_field_count"] == 6
    assert sixth_diagnostic["raw_pipe_count"] == 13
    assert sixth_diagnostic["suppressed_pipe_count"] == 8
    assert sixth_diagnostic["ended_inside_quote"] is True


def test_decision_matrix_requires_unique_documented_width_or_blocks() -> None:
    proposal = _load(PROPOSAL)
    algorithm = proposal["proposed_algorithm"]
    matrix = {
        item["case_id"]: item
        for item in algorithm["decision_matrix"]
    }

    assert algorithm["mode_name"] == "DOCUMENTED_WIDTH_ARBITRATION"
    assert algorithm["physical_record_boundary"] == "LF_OR_CRLF_HARD_BOUNDARY"
    assert algorithm["quote_state_may_cross_physical_record_boundary"] is False

    assert matrix["STRUCTURE_EQUIVALENT"]["outcome"] == (
        "ACCEPT_EQUIVALENT_STRUCTURE"
    )
    assert matrix["RAW_UNIQUE_DOCUMENTED_WIDTH"]["outcome"] == (
        "ACCEPT_RAW_UNIQUE_DOCUMENTED_WIDTH"
    )
    assert matrix["QUOTE_AWARE_UNIQUE_DOCUMENTED_WIDTH"]["outcome"] == (
        "ACCEPT_QUOTE_AWARE_UNIQUE_DOCUMENTED_WIDTH"
    )
    assert matrix["NO_UNIQUE_DOCUMENTED_WIDTH"]["outcome"] == (
        "BLOCK_NO_UNIQUE_DOCUMENTED_WIDTH"
    )


def test_synthetic_matrix_covers_sixth_shape_and_quoted_pipe() -> None:
    cases = {
        item["case_id"]: item
        for item in _load(PROPOSAL)["synthetic_acceptance_matrix"]
    }

    sixth_shape = cases["SIXTH_SHAPE_OPEN_QUOTE_RAW_14"]
    assert sixth_shape["raw_field_count"] == 14
    assert sixth_shape["quote_aware_field_count"] == 6
    assert sixth_shape["ended_inside_quote"] is True
    assert sixth_shape["expected_outcome"] == (
        "ACCEPT_RAW_UNIQUE_DOCUMENTED_WIDTH"
    )

    quoted_pipe = cases["SAME_LINE_QUOTED_PIPE"]
    assert quoted_pipe["raw_field_count"] == 15
    assert quoted_pipe["quote_aware_field_count"] == 14
    assert quoted_pipe["ended_inside_quote"] is False
    assert quoted_pipe["expected_outcome"] == (
        "ACCEPT_QUOTE_AWARE_UNIQUE_DOCUMENTED_WIDTH"
    )

    open_quote = cases["QUOTE_AWARE_14_BUT_OPEN_AT_EOL"]
    assert open_quote["expected_outcome"] == (
        "BLOCK_NO_UNIQUE_DOCUMENTED_WIDTH"
    )


def test_sixth_approvals_remain_consumed_and_no_seventh_is_authorized() -> None:
    for path in (SIXTH_LOCAL, SIXTH_PII):
        approval = _load(path)
        assert approval["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
        assert approval["reusable"] is False
        assert approval["retry_authorized"] is False

    proposal = _load(PROPOSAL)
    boundary = proposal["implementation_boundary"]
    no_grant = proposal["authorization_does_not_grant"]

    assert boundary["implementation_status"] == "NOT_IMPLEMENTED"
    assert boundary["runner_change_authorized"] is False
    assert boundary["seventh_attempt_proposal_authorized"] is False
    assert boundary["source_access_allowed"] is False
    assert no_grant["parser_implementation"] is False
    assert no_grant["runtime_activation"] is False
    assert no_grant["seventh_attempt_preparation"] is False
    assert no_grant["seventh_attempt_execution"] is False
