import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

from unclaimed_platform.domain.ny_mvp1_case_economics_integration import (
    NyMvp1CaseEconomicsIntegrationInput,
    integrate_follow_up_cost_with_case_economics,
)
from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    NyMvp1FollowUpCostMeasurementInput,
    measure_follow_up_cost,
)

_REPO_ROOT = Path(__file__).resolve().parents[2]
_ECONOMICS_DIR = _REPO_ROOT / "schemas" / "economics"
_INPUT_SCHEMA = _ECONOMICS_DIR / "ny_mvp1_case_economics_integration_input.schema.json"
_RESULT_SCHEMA = _ECONOMICS_DIR / "ny_mvp1_case_economics_integration_result.schema.json"
_EXPLICIT_INPUT_SCHEMA = _ECONOMICS_DIR / "ny_mvp1_explicit_case_economics_input.schema.json"
_EXPLICIT_RESULT_SCHEMA = _ECONOMICS_DIR / "ny_mvp1_explicit_case_economics_result.schema.json"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _result_validator() -> Draft202012Validator:
    explicit_input = _load(_EXPLICIT_INPUT_SCHEMA)
    explicit_result = _load(_EXPLICIT_RESULT_SCHEMA)
    registry = Registry().with_resources(
        [
            (explicit_input["$id"], Resource.from_contents(explicit_input)),
            (explicit_result["$id"], Resource.from_contents(explicit_result)),
        ]
    )
    return Draft202012Validator(_load(_RESULT_SCHEMA), registry=registry)


def _economics_input() -> NyMvp1CaseEconomicsIntegrationInput:
    return NyMvp1CaseEconomicsIntegrationInput(
        recoverable_value_cents=1_000_000,
        agreed_fee_bps=1200,
        value_evidence_ref="synthetic:value-evidence",
        fee_evidence_ref="synthetic:fee-evidence",
        fee_rule_scope_confirmed=True,
    )


def _follow_up_payload(*, with_rate: bool) -> dict[str, object]:
    payload: dict[str, object] = {
        "contract_version": "1.0.0",
        "mode": "SYNTHETIC_TEST",
        "measurement_id": "11111111-1111-4111-8111-111111111111",
        "candidate_case_id": "22222222-2222-4222-8222-222222222222",
        "owner_pii_included": False,
        "automated_processing": {
            "amount_cents": 37,
            "currency": "USD",
            "measurement_method": "SYSTEM_METERED",
            "allocation_basis": "PER_CANDIDATE_DIRECT",
            "evidence_ref": "synthetic:automation-meter",
            "observed_at": "2026-09-18T10:00:00Z",
        },
        "source_data": {
            "amount_cents": 0,
            "currency": "USD",
            "measurement_method": "ZERO_DIRECT_COST_DOCUMENTED",
            "allocation_basis": "ZERO_DIRECT_COST_PER_CANDIDATE",
            "evidence_ref": "synthetic:source-cost",
            "observed_at": "2026-09-18T10:00:00Z",
        },
        "human_review": {
            "duration_seconds": 125,
            "measurement_method": "REVIEWER_TIMER",
            "evidence_ref": "synthetic:review-timer",
            "observed_at": "2026-09-18T10:00:00Z",
        },
        "manual_research": {
            "duration_seconds": 65,
            "measurement_method": "MANUAL_TIMER",
            "evidence_ref": "synthetic:research-timer",
            "observed_at": "2026-09-18T10:00:00Z",
        },
        "human_labor_rate": None,
    }
    if with_rate:
        payload["human_labor_rate"] = {
            "cents_per_hour": 7200,
            "currency": "USD",
            "evidence_ref": "synthetic:labor-rate",
            "observed_at": "2026-09-18T10:00:00Z",
        }
    return payload


def test_integration_input_validates_against_schema() -> None:
    payload = _economics_input().model_dump(mode="json")

    Draft202012Validator(_load(_INPUT_SCHEMA)).validate(payload)


@pytest.mark.parametrize("with_rate", [False, True])
def test_integration_result_validates_against_schema(with_rate: bool) -> None:
    follow_up_input = NyMvp1FollowUpCostMeasurementInput.model_validate(
        _follow_up_payload(with_rate=with_rate)
    )
    follow_up_result = measure_follow_up_cost(follow_up_input)
    result = integrate_follow_up_cost_with_case_economics(
        _economics_input(),
        follow_up_result,
    )

    _result_validator().validate(result.model_dump(mode="json"))


def test_blocked_contract_rejects_substituted_direct_machine_data_cost() -> None:
    follow_up_input = NyMvp1FollowUpCostMeasurementInput.model_validate(
        _follow_up_payload(with_rate=False)
    )
    follow_up_result = measure_follow_up_cost(follow_up_input)
    result = integrate_follow_up_cost_with_case_economics(
        _economics_input(),
        follow_up_result,
    ).model_dump(mode="json")
    result["measured_follow_up_cost_cents"] = (
        follow_up_result.direct_machine_and_data_cost_cents
    )

    with pytest.raises(ValidationError):
        _result_validator().validate(result)


def test_ready_contract_preserves_all_cost_evidence_refs() -> None:
    follow_up_input = NyMvp1FollowUpCostMeasurementInput.model_validate(
        _follow_up_payload(with_rate=True)
    )
    follow_up_result = measure_follow_up_cost(follow_up_input)
    result = integrate_follow_up_cost_with_case_economics(
        _economics_input(),
        follow_up_result,
    )

    assert result.follow_up_cost_evidence_refs == follow_up_result.evidence_refs
    assert len(result.follow_up_cost_evidence_refs) == 5
