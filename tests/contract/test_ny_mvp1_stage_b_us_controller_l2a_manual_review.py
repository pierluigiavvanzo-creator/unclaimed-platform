import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
CONTROLLER = ROOT / "sources/proposals/ny_mvp1_stage_b_us_controller_fact_binding.v1.json"
CONTROLLER_SCHEMA = ROOT / "schemas/common/ny_mvp1_stage_b_us_controller_fact_binding.schema.json"
PROVIDER = ROOT / "sources/proposals/ny_mvp1_stage_b_l2a_manual_provider_review.v1.json"
PROVIDER_SCHEMA = ROOT / "schemas/common/ny_mvp1_stage_b_l2a_manual_provider_review.schema.json"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator(path: Path) -> Draft202012Validator:
    return Draft202012Validator(_load(path))


def test_controller_fact_binding_template_validates_and_stays_unbound() -> None:
    payload = _load(CONTROLLER)
    _validator(CONTROLLER_SCHEMA).validate(payload)
    assert payload["execution_allowed"] is False
    assert payload["human_input_required"] is True
    assert payload["controller_facts"]["legal_name"] is None


def test_controller_template_cannot_invent_entity() -> None:
    payload = copy.deepcopy(_load(CONTROLLER))
    payload["controller_facts"]["legal_name"] = "Invented US LLC"
    with pytest.raises(ValidationError):
        _validator(CONTROLLER_SCHEMA).validate(payload)


def test_manual_provider_review_validates() -> None:
    payload = _load(PROVIDER)
    _validator(PROVIDER_SCHEMA).validate(payload)
    assert payload["provider_candidate"]["provider_id"] == "google-search-manual-us-v1"
    assert payload["provider_candidate"]["external_cash_budget_cents"] == 0
    assert payload["provider_candidate"]["max_search_queries"] == 3


def test_manual_provider_cannot_enable_api_or_automation() -> None:
    payload = copy.deepcopy(_load(PROVIDER))
    payload["provider_candidate"]["api_allowed"] = True
    with pytest.raises(ValidationError):
        _validator(PROVIDER_SCHEMA).validate(payload)

    payload = copy.deepcopy(_load(PROVIDER))
    payload["provider_candidate"]["automation_allowed"] = True
    with pytest.raises(ValidationError):
        _validator(PROVIDER_SCHEMA).validate(payload)


def test_ai_summary_is_not_targetability_evidence() -> None:
    payload = copy.deepcopy(_load(PROVIDER))
    payload["evidence_rules"]["google_ai_overview_or_ai_mode_allowed_as_evidence"] = True
    with pytest.raises(ValidationError):
        _validator(PROVIDER_SCHEMA).validate(payload)


def test_manual_provider_cannot_authorize_real_query() -> None:
    payload = copy.deepcopy(_load(PROVIDER))
    payload["authorization_does_not_grant"]["external_pii_query"] = True
    with pytest.raises(ValidationError):
        _validator(PROVIDER_SCHEMA).validate(payload)


def test_provider_binding_template_matches_existing_zero_spend_contract() -> None:
    payload = _load(PROVIDER)
    binding = payload["provider_binding_template"]
    assert binding == {
        "provider_id": "google-search-manual-us-v1",
        "provider_terms_review_ref": (
            "docs/audits/NY_MVP1_STAGE_B_US_CONTROLLER_L2A_MANUAL_PROVIDER_REVIEW.md"
        ),
        "approved_external_cash_budget_cents": 0,
        "approved_manual_research_cap_seconds": 900,
        "paid_api_allowed": False,
        "paid_data_broker_allowed": False,
        "consumer_report_fcra_product_allowed": False,
    }


def test_websurrogate_is_explicitly_excluded_for_stage_b() -> None:
    payload = _load(PROVIDER)
    exclusions = payload["explicit_source_exclusions"]
    websurrogate = next(
        item for item in exclusions if item.get("source") == "WebSurrogate"
    )
    assert websurrogate["status"].startswith("REJECTED_FOR_STAGE_B")
