import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

from unclaimed_platform.domain.ny_mvp1_targetable_opportunity import (
    SyntheticTargetabilityEvidence,
    SyntheticTargetingCandidate,
    evaluate_synthetic_targetable_opportunity,
)

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/common/ny_mvp1_targetable_opportunity_filter.schema.json"


def _result() -> dict[str, object]:
    record = SyntheticTargetingCandidate(
        source_record_ordinal=42,
        property_type_code="IN03",
        property_owner_count=1,
        property_id_present=True,
        holder_report_year=2015,
    )
    evidence = SyntheticTargetabilityEvidence(
        service_need_state="MATERIAL_EVIDENCE",
        resolvability_state="EASY",
        evidence_refs=("synthetic:targetability",),
        targetability_decision_cost_state="MEASURED",
        targetability_decision_cost_cents=100,
    )
    return evaluate_synthetic_targetable_opportunity(
        [record], evidence
    ).model_dump(mode="json")


def _validator() -> Draft202012Validator:
    return Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_runtime_output_validates_against_versioned_schema() -> None:
    _validator().validate(_result())


def test_schema_rejects_targetability_score() -> None:
    payload = copy.deepcopy(_result())
    payload["targetability"]["targetability_score"] = 85
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_schema_rejects_value_prediction() -> None:
    payload = copy.deepcopy(_result())
    payload["targetability"]["value_prediction_performed"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_schema_rejects_real_authorization() -> None:
    payload = copy.deepcopy(_result())
    payload["authorization_granted"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)
