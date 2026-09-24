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


def test_bifurcated_legal_readiness_proposal_validates() -> None:
    _validator().validate(_proposal())


def test_us_controller_track_is_only_a_pending_fact_hypothesis() -> None:
    payload = _proposal()
    track = payload["territorial_scope_tracks"]["us_controller_us_market"]
    assert track["state"] == "PREFERRED_MVP_HYPOTHESIS_PENDING_FACTS"
    assert track["gdpr_controller_scope_assessment"] == (
        "LIKELY_OUTSIDE_GDPR_CONTROLLER_SCOPE_IF_ALL_CONDITIONS_TRUE_NOT_A_LEGAL_DETERMINATION"
    )
    assert track["execution_allowed"] is False


def test_eu_controller_track_retains_gdpr_blockers() -> None:
    payload = _proposal()
    track = payload["territorial_scope_tracks"]["eu_controller_or_eu_establishment"]
    assert track["gdpr_article_3_1_expected_to_apply_if_trigger_true"] is True
    assert track["article_6_basis_required"] is True
    assert track["article_14_path_required"] is True
    assert track["execution_allowed"] is False


def test_eu_processor_does_not_automatically_expand_us_controller_scope() -> None:
    payload = _proposal()
    track = payload["territorial_scope_tracks"]["us_controller_with_eu_processor_only"]
    assert track["controller_gdpr_scope_not_automatically_triggered_by_eu_processor"] is True
    assert track["eu_processor_may_have_own_gdpr_processor_obligations"] is True


def test_us_track_cannot_be_marked_execution_ready() -> None:
    payload = copy.deepcopy(_proposal())
    payload["territorial_scope_tracks"]["us_controller_us_market"]["execution_allowed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_controller_identity_cannot_be_invented_by_this_review() -> None:
    payload = copy.deepcopy(_proposal())
    payload["controller_readiness"]["controller_legal_name"] = "Invented LLC"
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_live_pii_access_from_eu_is_not_enabled_by_default() -> None:
    payload = copy.deepcopy(_proposal())
    payload["preferred_mvp_privacy_architecture"]["eu_developer_access_to_live_owner_pii"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_gdpr_article_14_exception_is_not_assumed_if_gdpr_track_applies() -> None:
    payload = copy.deepcopy(_proposal())
    payload["gdpr_track_requirements_if_triggered"]["article_14_5_exception_assumed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_scope_definition_cannot_grant_real_p1() -> None:
    payload = copy.deepcopy(_proposal())
    payload["authorization_does_not_grant"]["any_of_seven_p1_gates"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_review_requires_operating_model_and_entity_facts() -> None:
    payload = _proposal()
    assert payload["review_result"] == (
        "BIFURCATED_READY_FOR_CONTROLLER_OPERATING_MODEL_FACTS_NOT_READY_FOR_REAL_P1"
    )
    assert payload["next_action_if_approved"] == (
        "HUMAN_SELECT_P1_CONTROLLER_OPERATING_MODEL_AND_SUPPLY_ENTITY_FACTS"
    )
    assert len(payload["controller_fact_requirements"]) >= 10
