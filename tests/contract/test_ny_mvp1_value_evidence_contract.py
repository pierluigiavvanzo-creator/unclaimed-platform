import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

from unclaimed_platform.domain.ny_mvp1_value_evidence import (
    NyMvp1ExplicitCaseEconomicsInput,
    compute_explicit_case_economics,
    ny_mvp1_precontact_economics_evidence,
)

_REPO_ROOT = Path(__file__).resolve().parents[2]
_PRECONTACT_SCHEMA = (
    _REPO_ROOT / "schemas" / "economics" / "ny_mvp1_precontact_evidence.schema.json"
)
_INPUT_SCHEMA = (
    _REPO_ROOT
    / "schemas"
    / "economics"
    / "ny_mvp1_explicit_case_economics_input.schema.json"
)
_RESULT_SCHEMA = (
    _REPO_ROOT
    / "schemas"
    / "economics"
    / "ny_mvp1_explicit_case_economics_result.schema.json"
)


def _validator(path: Path) -> Draft202012Validator:
    return Draft202012Validator(json.loads(path.read_text(encoding="utf-8")))


def _valid_input() -> NyMvp1ExplicitCaseEconomicsInput:
    return NyMvp1ExplicitCaseEconomicsInput(
        recoverable_value_cents=500_000,
        agreed_fee_bps=1200,
        measured_follow_up_cost_cents=20_000,
        value_evidence_ref="official-value-evidence",
        fee_evidence_ref="valid-fee-rate-evidence",
        cost_evidence_ref="measured-cost-evidence",
        fee_rule_scope_confirmed=True,
    )


def test_precontact_evidence_validates_against_schema() -> None:
    payload = ny_mvp1_precontact_economics_evidence().model_dump(mode="json")

    _validator(_PRECONTACT_SCHEMA).validate(payload)


def test_explicit_input_and_result_validate_against_schemas() -> None:
    inputs = _valid_input()
    result = compute_explicit_case_economics(inputs)

    _validator(_INPUT_SCHEMA).validate(inputs.model_dump(mode="json"))
    _validator(_RESULT_SCHEMA).validate(result.model_dump(mode="json"))


def test_precontact_contract_rejects_invented_exact_value() -> None:
    payload = ny_mvp1_precontact_economics_evidence().model_dump(mode="json")
    payload["exact_recoverable_value_cents"] = 100_000

    with pytest.raises(ValidationError):
        _validator(_PRECONTACT_SCHEMA).validate(payload)


def test_input_contract_rejects_fee_above_cap() -> None:
    payload = _valid_input().model_dump(mode="json")
    payload["agreed_fee_bps"] = 1501

    with pytest.raises(ValidationError):
        _validator(_INPUT_SCHEMA).validate(payload)


def test_result_contract_rejects_commercial_recommendation_flag() -> None:
    result = compute_explicit_case_economics(_valid_input()).model_dump(mode="json")
    result["no_commercial_recommendation"] = False

    with pytest.raises(ValidationError):
        _validator(_RESULT_SCHEMA).validate(result)
