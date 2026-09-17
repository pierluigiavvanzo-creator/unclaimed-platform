from __future__ import annotations

import json
from pathlib import Path

from unclaimed_platform.adapters.sources.california_property_type import (
    CA_INSURANCE_CODES,
    MVP1_PRIMARY_PROPERTY_TYPE,
    PROPERTY_TYPE_RE,
)

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "policies/states/CA/ca_sco_property_type_classification.v1.json"


def test_policy_matches_authority_backed_runtime_classifier() -> None:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))

    assert policy["schema_version"] == "1.0.0"
    assert policy["source_id"] == "ca.sco.unclaimed_property.bulk"
    assert policy["canonical_shape_regex"] == PROPERTY_TYPE_RE.pattern
    assert policy["insurance_codes"] == CA_INSURANCE_CODES
    assert policy["mvp1_target"]["primary_code"] == MVP1_PRIMARY_PROPERTY_TYPE == "IN03"
    assert policy["insurance_codes"]["IN03"] == "Proceeds Due Beneficiaries"


def test_nonconforming_policy_is_metadata_only_defer_and_continue() -> None:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    handling = policy["nonconforming_row_policy"]

    assert handling["policy_id"] == "ROW_DEFER_CONTINUE_METADATA_ONLY"
    assert handling["semantic_acceptance"] is False
    assert handling["normalization_allowed"] is False
    assert handling["regex_relaxation_allowed"] is False
    assert handling["row_content_persistence_allowed"] is False
    assert handling["property_type_value_persistence_allowed"] is False
    assert handling["row_specific_human_inspection_allowed"] is False
    assert handling["persisted_metadata"] == ["nonconforming_rows_deferred_count"]
    assert handling["continue_after_nonconforming_row"] is True
    assert handling["silent_row_omission_allowed"] is False
    assert handling["deferred_row_is_treated_as_non_insurance"] is False
    assert handling["deferred_row_is_treated_as_unknown_unclassifiable"] is True
