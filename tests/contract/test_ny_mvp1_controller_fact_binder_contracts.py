import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
INPUT_SCHEMA = ROOT / "schemas/common/ny_mvp1_stage_b_controller_facts_input.schema.json"
OUTPUT_SCHEMA = (
    ROOT / "schemas/common/ny_mvp1_stage_b_controller_fact_binding_assessment.schema.json"
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


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_controller_fact_schemas_are_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(_load(INPUT_SCHEMA))
    Draft202012Validator.check_schema(_load(OUTPUT_SCHEMA))


def test_synthetic_inputs_validate() -> None:
    validator = Draft202012Validator(_load(INPUT_SCHEMA))
    validator.validate(NOT_FORMED)
    validator.validate(FORMED_US)


def test_not_formed_input_cannot_invent_legal_name() -> None:
    payload = copy.deepcopy(NOT_FORMED)
    payload["legal_name"] = "Invented LLC"
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(INPUT_SCHEMA)).validate(payload)


def test_formed_input_requires_material_controller_facts() -> None:
    payload = copy.deepcopy(FORMED_US)
    payload["principal_business_address"] = None
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(INPUT_SCHEMA)).validate(payload)
