import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    NyMvp1FollowUpCostMeasurementInput,
    measure_follow_up_cost,
)

_REPO_ROOT = Path(__file__).resolve().parents[2]
_INPUT_SCHEMA = (
    _REPO_ROOT
    / "schemas"
    / "economics"
    / "ny_mvp1_follow_up_cost_measurement_input.schema.json"
)
_RESULT_SCHEMA = (
    _REPO_ROOT
    / "schemas"
    / "economics"
    / "ny_mvp1_follow_up_cost_measurement_result.schema.json"
)


def _validator(path: Path) -> Draft202012Validator:
    return Draft202012Validator(json.loads(path.read_text(encoding="utf-8")))


def _payload(*, with_rate: bool = False) -> dict[str, object]:
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
            "observed_at": "2026-09-18T08:00:00Z",
        },
        "source_data": {
            "amount_cents": 0,
            "currency": "USD",
            "measurement_method": "ZERO_DIRECT_COST_DOCUMENTED",
            "allocation_basis": "ZERO_DIRECT_COST_PER_CANDIDATE",
            "evidence_ref": "synthetic:source-cost",
            "observed_at": "2026-09-18T08:00:00Z",
        },
        "human_review": {
            "duration_seconds": 125,
            "measurement_method": "REVIEWER_TIMER",
            "evidence_ref": "synthetic:review-timer",
            "observed_at": "2026-09-18T08:00:00Z",
        },
        "manual_research": {
            "duration_seconds": 65,
            "measurement_method": "MANUAL_TIMER",
            "evidence_ref": "synthetic:research-timer",
            "observed_at": "2026-09-18T08:00:00Z",
        },
        "human_labor_rate": None,
    }
    if with_rate:
        payload["human_labor_rate"] = {
            "cents_per_hour": 7200,
            "currency": "USD",
            "evidence_ref": "synthetic:labor-rate",
            "observed_at": "2026-09-18T08:00:00Z",
        }
    return payload


def test_input_and_result_validate_against_contracts_without_labor_rate() -> None:
    payload = _payload()
    _validator(_INPUT_SCHEMA).validate(payload)

    model = NyMvp1FollowUpCostMeasurementInput.model_validate(payload)
    result = measure_follow_up_cost(model).model_dump(mode="json")

    _validator(_RESULT_SCHEMA).validate(result)
    assert result["fully_loaded_follow_up_cost_cents"] is None


def test_input_and_result_validate_against_contracts_with_documented_labor_rate() -> None:
    payload = _payload(with_rate=True)
    _validator(_INPUT_SCHEMA).validate(payload)

    model = NyMvp1FollowUpCostMeasurementInput.model_validate(payload)
    result = measure_follow_up_cost(model).model_dump(mode="json")

    _validator(_RESULT_SCHEMA).validate(result)
    assert result["fully_loaded_follow_up_cost_cents"] == 417


def test_contract_rejects_owner_pii_flag() -> None:
    payload = _payload()
    payload["owner_pii_included"] = True

    with pytest.raises(ValidationError):
        _validator(_INPUT_SCHEMA).validate(payload)


def test_contract_rejects_missing_measurement_evidence() -> None:
    payload = _payload()
    automated = dict(payload["automated_processing"])
    automated["evidence_ref"] = ""
    payload["automated_processing"] = automated

    with pytest.raises(ValidationError):
        _validator(_INPUT_SCHEMA).validate(payload)


def test_result_contract_rejects_commercial_recommendation() -> None:
    model = NyMvp1FollowUpCostMeasurementInput.model_validate(_payload())
    result = measure_follow_up_cost(model).model_dump(mode="json")
    result["no_commercial_recommendation"] = False

    with pytest.raises(ValidationError):
        _validator(_RESULT_SCHEMA).validate(result)
