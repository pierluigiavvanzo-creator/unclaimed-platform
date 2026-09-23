import copy
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from uuid import UUID

import pytest
from jsonschema import Draft202012Validator, ValidationError

from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    DocumentedHumanLaborRate,
)
from unclaimed_platform.domain.ny_osc_one_candidate_transient_materialization import (
    SyntheticL1InstrumentationInput,
    SyntheticNyOscCandidateRecord,
    select_and_materialize_synthetic_one_candidate,
)

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_synthetic_one_candidate_transient_materialization.schema.json"
)
NOW = datetime(2026, 9, 23, 18, 0, tzinfo=UTC)


def _result_dict() -> dict[str, object]:
    record = SyntheticNyOscCandidateRecord(
        source_snapshot_ref="synthetic:snapshot",
        source_record_ordinal=42,
        property_id="SYNTHETIC-PROP",
        property_type_code="IN03",
        property_owner_count=1,
        owner_name="SYNTHETIC OWNER",
        holder_name="SYNTHETIC HOLDER",
        holder_report_year="2025",
    )
    instrument = SyntheticL1InstrumentationInput(
        measurement_id=UUID("11111111-1111-4111-8111-111111111111"),
        initial_lane="F1",
        lane_assignment_evidence_refs=("synthetic:lane",),
        stage_started_at=NOW,
        stage_completed_at=NOW + timedelta(seconds=60),
        stage_evidence_ref="synthetic:l1",
        approved_incremental_budget_cents=1000,
        budget_evidence_ref="synthetic:budget",
        automated_processing={
            "amount_cents": 10,
            "currency": "USD",
            "measurement_method": "SYSTEM_METERED",
            "allocation_basis": "PER_CANDIDATE_DIRECT",
            "evidence_ref": "synthetic:auto",
            "observed_at": NOW,
        },
        source_data={
            "amount_cents": 0,
            "currency": "USD",
            "measurement_method": "ZERO_DIRECT_COST_DOCUMENTED",
            "allocation_basis": "ZERO_DIRECT_COST_PER_CANDIDATE",
            "evidence_ref": "synthetic:data",
            "observed_at": NOW,
        },
        human_review={
            "duration_seconds": 30,
            "measurement_method": "REVIEWER_TIMER",
            "evidence_ref": "synthetic:review",
            "observed_at": NOW,
        },
        manual_research={
            "duration_seconds": 30,
            "measurement_method": "MANUAL_TIMER",
            "evidence_ref": "synthetic:research",
            "observed_at": NOW,
        },
        human_labor_rate=DocumentedHumanLaborRate(
            cents_per_hour=6000,
            currency="USD",
            evidence_ref="synthetic:rate",
            observed_at=NOW,
        ),
    )
    result = select_and_materialize_synthetic_one_candidate([record], instrument)
    return result.model_dump(mode="json")


def _validator() -> Draft202012Validator:
    return Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_runtime_output_validates_against_versioned_schema() -> None:
    _validator().validate(_result_dict())


def test_schema_rejects_owner_pii_flag_expansion() -> None:
    payload = copy.deepcopy(_result_dict())
    payload["economic_case_ledger"]["owner_pii_included"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_schema_rejects_authorization_expansion() -> None:
    payload = copy.deepcopy(_result_dict())
    payload["authorization_granted"] = True
    with pytest.raises(ValidationError):
        _validator().validate(payload)