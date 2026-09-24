import copy
import json

import pytest
from pydantic import ValidationError

from unclaimed_platform.domain.ny_mvp1_controller_fact_binder import (
    ControllerFactsInput,
    assess_controller_facts,
)

NOT_FORMED = {
    "schema_version": "1.0.0",
    "artifact_id": "ny.mvp1.stage_b.controller_facts_input",
    "formation_state": "NOT_YET_FORMED",
    "operating_model": None,
    "legal_name": None,
    "entity_type": None,
    "formation_jurisdiction": None,
    "principal_business_address": None,
    "privacy_contact": None,
    "relevant_eu_branch_office_employee_agent_or_stable_arrangement": None,
    "eu_person_or_entity_live_owner_pii_access": None,
    "lsp_customer_agreement_signing_entity": None,
    "lsp_fee_receiving_entity": None,
    "us_only_mvp1_market": None,
    "eu_targeting": None,
    "eu_monitoring": None,
}

FORMED_US = {
    "schema_version": "1.0.0",
    "artifact_id": "ny.mvp1.stage_b.controller_facts_input",
    "formation_state": "FORMED",
    "operating_model": "US_CONTROLLER_US_MARKET",
    "legal_name": "Synthetic Stage B Controller LLC",
    "entity_type": "LLC",
    "formation_jurisdiction": "US-SYNTHETIC-JURISDICTION",
    "principal_business_address": "SYNTHETIC_BUSINESS_ADDRESS_FOR_TESTS_ONLY",
    "privacy_contact": None,
    "relevant_eu_branch_office_employee_agent_or_stable_arrangement": False,
    "eu_person_or_entity_live_owner_pii_access": False,
    "lsp_customer_agreement_signing_entity": "Synthetic Stage B Controller LLC",
    "lsp_fee_receiving_entity": "Synthetic Stage B Controller LLC",
    "us_only_mvp1_market": True,
    "eu_targeting": False,
    "eu_monitoring": False,
}


def _facts(payload: dict[str, object]) -> ControllerFactsInput:
    return ControllerFactsInput.model_validate(payload)


def test_not_formed_stays_blocked_and_grants_nothing() -> None:
    result = assess_controller_facts(_facts(NOT_FORMED))
    assert result.status == "BLOCKED_ENTITY_NOT_FORMED"
    assert result.next_action == "HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1"
    assert result.real_p1_execution_allowed is False
    assert result.all_seven_p1_gates_state == "NOT_GRANTED"


def test_clean_formed_us_facts_route_to_professional_review_not_execution() -> None:
    result = assess_controller_facts(_facts(FORMED_US))
    assert result.status == "FACTS_BOUND_US_TRACK_PENDING_PROFESSIONAL_REVIEW"
    assert result.next_action == "HUMAN_VERIFY_US_TAX_NY_NEXUS_AND_LEGAL_READINESS"
    assert result.real_p1_execution_allowed is False
    assert result.authorization_does_not_grant.any_p1_gate is False


def test_output_does_not_persist_legal_name_or_address() -> None:
    result = assess_controller_facts(_facts(FORMED_US)).model_dump(mode="json")
    serialized = json.dumps(result)
    assert "Synthetic Stage B Controller LLC" not in serialized
    assert "SYNTHETIC_BUSINESS_ADDRESS_FOR_TESTS_ONLY" not in serialized
    assert result["sensitive_or_identifying_values_persisted"] is False


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("relevant_eu_branch_office_employee_agent_or_stable_arrangement", True),
        ("eu_person_or_entity_live_owner_pii_access", True),
        ("us_only_mvp1_market", False),
        ("eu_targeting", True),
        ("eu_monitoring", True),
    ],
)
def test_eu_or_non_us_conditions_route_to_human_review(field: str, value: bool) -> None:
    payload = copy.deepcopy(FORMED_US)
    payload[field] = value
    result = assess_controller_facts(_facts(payload))
    assert result.status == "ROUTE_TO_HUMAN_LEGAL_PRIVACY_REVIEW"
    assert result.next_action == (
        "HUMAN_REVIEW_CONTROLLER_TERRITORIAL_SCOPE_AND_LIVE_PII_ACCESS"
    )
    assert result.real_p1_execution_allowed is False


def test_formed_controller_cannot_omit_legal_name() -> None:
    payload = copy.deepcopy(FORMED_US)
    payload["legal_name"] = None
    with pytest.raises(ValidationError):
        ControllerFactsInput.model_validate(payload)
