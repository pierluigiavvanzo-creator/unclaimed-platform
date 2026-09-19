from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_multiline_quoted_record_offline_remediation.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_multiline_quoted_record_offline_remediation.schema.json"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_multiline_remediation_analysis_is_valid_and_offline_only() -> None:
    proposal = _load(PROPOSAL)
    Draft202012Validator(_load(SCHEMA)).validate(proposal)

    assert proposal["status"] == (
        "ANALYZED_OFFLINE_REMEDIATION_FEASIBLE_NOT_IMPLEMENTED"
    )

    scope = proposal["scope"]
    assert scope["repository_only"] is True
    assert scope["synthetic_fixtures_only"] is True
    assert scope["source_network_access_performed"] is False
    assert scope["download_performed"] is False
    assert scope["owner_pii_processed"] is False
    assert scope["fourth_attempt_prepared"] is False
    assert scope["fourth_attempt_authorized"] is False


def test_analysis_preserves_privacy_and_execution_gates() -> None:
    proposal = _load(PROPOSAL)
    design = proposal["remediation_design"]
    gate = proposal["implementation_gate"]

    assert design["implementation_state"] == "NOT_IMPLEMENTED"
    assert design["auxiliary_memory_target"] == (
        "CONSTANT_WITH_RESPECT_TO_LOGICAL_RECORD_LENGTH"
    )
    assert design["owner_field_decoding_allowed"] is False
    assert design["owner_field_buffering_allowed"] is False
    assert design["owner_row_persistence_allowed"] is False
    assert design["owner_field_logging_allowed"] is False
    assert design["row_specific_human_inspection_allowed"] is False

    assert gate["production_parser_change_allowed_by_this_analysis"] is False
    assert gate["execution_runner_change_allowed_by_this_analysis"] is False
    assert gate["new_approval_artifacts_allowed"] is False
    assert gate["real_execution_allowed"] is False
    assert gate["required_next_action"] == (
        "IMPLEMENT_NY_OSC_STREAMING_MULTILINE_QUOTED_RECORD_PARSER_OFFLINE"
    )


def test_analysis_does_not_overclaim_real_file_cause() -> None:
    proposal = _load(PROPOSAL)
    evidence = proposal["evidence"]
    analysis = proposal["root_cause_analysis"]

    assert evidence["exact_real_file_cause_confirmed"] is False
    assert evidence["raw_file_retained"] is False
    assert evidence["offending_record_retained"] is False
    assert analysis["source_corruption_claimed"] is False
    assert analysis["compatible_unconfirmed_hypothesis"] == (
        "QUOTED_FIELD_CONTAINS_EMBEDDED_LINE_BREAK"
    )
