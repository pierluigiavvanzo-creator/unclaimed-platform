import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_mvp1_real_p1_targetability_execution_scope.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_mvp1_real_p1_targetability_execution_scope.schema.json"
)


def _proposal() -> dict[str, object]:
    return json.loads(PROPOSAL.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    return Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_real_p1_scope_proposal_validates_against_versioned_schema() -> None:
    _validator().validate(_proposal())


def test_scope_cannot_authorize_real_execution() -> None:
    payload = copy.deepcopy(_proposal())
    payload["authorization_does_not_grant"]["real_candidate_materialization"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_l1_cannot_add_external_cash_spend() -> None:
    payload = copy.deepcopy(_proposal())
    payload["l1_selected_candidate_materialization"][
        "max_new_external_cash_spend_cents"
    ] = 1
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_l2a_cannot_enable_paid_data_broker() -> None:
    payload = copy.deepcopy(_proposal())
    payload["l2a_minimal_targetability_discovery"]["paid_data_broker_allowed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_l2a_cannot_enable_outreach() -> None:
    payload = copy.deepcopy(_proposal())
    payload["l2a_minimal_targetability_discovery"]["outreach_allowed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_l0_cannot_use_owner_pii_for_ranking() -> None:
    payload = copy.deepcopy(_proposal())
    payload["l0_selection_pass"]["owner_pii_ranking_allowed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_same_download_extension_requires_all_gates_before_download() -> None:
    payload = _proposal()
    assert payload["co_execution_rule"]["mid_session_wait_for_new_authorization_allowed"] is False
    assert payload["co_execution_rule"]["automatic_scope_widening_allowed"] is False
    assert payload["co_execution_rule"]["automatic_retry_allowed"] is False


def test_scope_keeps_targetability_budget_bounded_and_not_a_profit_threshold() -> None:
    payload = _proposal()
    l2a = payload["l2a_minimal_targetability_discovery"]
    assert l2a["proposed_incremental_external_cash_budget_cents"] == 0
    assert l2a["proposed_manual_research_cap_seconds"] == 900
    assert l2a["manual_research_cap_interpretation"] == (
        "PRODUCT_OWNER_EXPERIMENT_CAP_NOT_EVIDENCE_BACKED_PROFITABILITY_THRESHOLD"
    )
