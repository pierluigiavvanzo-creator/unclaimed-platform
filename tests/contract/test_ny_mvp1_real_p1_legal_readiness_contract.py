import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_mvp1_real_p1_controller_legal_basis_transparency_readiness.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_mvp1_real_p1_controller_legal_basis_transparency_readiness.schema.json"
)


def _proposal() -> dict[str, object]:
    return json.loads(PROPOSAL.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    return Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_legal_readiness_proposal_validates() -> None:
    _validator().validate(_proposal())


def test_readiness_cannot_claim_execution_is_allowed() -> None:
    payload = copy.deepcopy(_proposal())
    payload["controller_readiness"]["execution_allowed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_readiness_cannot_select_a_final_gdpr_basis_yet() -> None:
    payload = copy.deepcopy(_proposal())
    payload["article_6_basis_assessment"]["final_basis_selected"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_article_14_exception_cannot_be_assumed() -> None:
    payload = copy.deepcopy(_proposal())
    payload["transparency_article_14"]["article_14_5_exception_assumed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_public_source_does_not_create_gdpr_exception() -> None:
    payload = copy.deepcopy(_proposal())
    payload["gdpr_applicability"]["public_source_exception_assumed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_full_file_acquisition_remains_blocked_pending_necessity_review() -> None:
    payload = copy.deepcopy(_proposal())
    payload["full_file_necessity_and_minimisation"]["state"] = "READY"
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_scope_definition_cannot_grant_any_real_p1_gate() -> None:
    payload = copy.deepcopy(_proposal())
    payload["authorization_does_not_grant"]["any_of_seven_p1_gates"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_result_is_fail_closed_until_controller_and_transparency_are_resolved() -> None:
    payload = _proposal()
    assert payload["review_result"] == "CONDITIONAL_FAIL_NOT_READY_FOR_REAL_P1"
    assert payload["controller_readiness"]["controller_identity_state"] == (
        "UNRESOLVED_BLOCKING"
    )
    assert payload["transparency_article_14"]["state"] == (
        "UNRESOLVED_BLOCKING_IF_GDPR_APPLIES"
    )
    assert payload["dpia_readiness"]["project_policy"] == (
        "DPIA_SCREEN_REQUIRED_BEFORE_REAL_P1_IF_GDPR_APPLIES"
    )
