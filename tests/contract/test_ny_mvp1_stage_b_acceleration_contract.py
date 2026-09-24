import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = ROOT / "sources/proposals/ny_mvp1_stage_b_pilot_p1_acceleration.v1.json"
SCHEMA = ROOT / "schemas/common/ny_mvp1_stage_b_pilot_p1_acceleration.schema.json"


def _proposal() -> dict[str, object]:
    return json.loads(PROPOSAL.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    return Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_stage_b_acceleration_proposal_validates() -> None:
    _validator().validate(_proposal())


def test_stage_b_is_one_real_p1_targetability_experiment() -> None:
    payload = _proposal()
    assert payload["stage_b_definition"] == "PILOT_P1_ONE_REAL_TARGETABILITY_EXPERIMENT"
    assert payload["no_scale_before_review"] is True


def test_l1_minimization_retains_file_pii_gate() -> None:
    payload = _proposal()
    lane = payload["lanes"]["l1_privacy_minimization"]
    assert lane["status"] == "IMPLEMENTED_OFFLINE_PENDING_REVIEW"
    assert lane["l1_pii_file_gate_retained"] is True
    assert lane["l2a_direct_pii_materialization_requires_preapproval"] is True


def test_stage_b_does_not_require_outreach_or_claim() -> None:
    payload = _proposal()
    assert "OUTREACH" in payload["stage_b_exit_does_not_require"]
    assert "CLAIM_SUBMISSION" in payload["stage_b_exit_does_not_require"]
    assert payload["lanes"]["l2a_targetability"]["outreach_allowed"] is False
    assert payload["lanes"]["l2a_targetability"]["value_research_allowed"] is False


def test_stage_b_keeps_external_spend_at_zero() -> None:
    payload = _proposal()
    lane = payload["lanes"]["l2a_targetability"]
    assert lane["external_paid_spend_cents"] == 0
    assert lane["paid_api_allowed"] is False
    assert lane["paid_data_broker_allowed"] is False


def test_stage_b_cannot_authorize_real_execution() -> None:
    payload = copy.deepcopy(_proposal())
    payload["authorization_does_not_grant"]["any_p1_gate"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_stage_b_cannot_skip_controller_entity_facts() -> None:
    payload = copy.deepcopy(_proposal())
    payload["lanes"]["controller_track"]["execution_allowed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_stage_b_fast_track_requires_only_three_human_input_groups() -> None:
    payload = _proposal()
    assert payload["remaining_human_inputs_minimum"] == [
        "CONTROLLER_OPERATING_MODEL_AND_ENTITY_FACTS",
        "EXACT_L2A_PROVIDER_OR_MANUAL_RESEARCH_SOURCE_SET",
        "FRESH_SINGLE_USE_EXECUTION_APPROVALS",
    ]
