from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType

import pytest
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL_PATH = ROOT / "sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json"
HISTORICAL_PROPOSAL_PATH = ROOT / "sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json"
SCHEMA_PATH = ROOT / "schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.v1_1.schema.json"
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
WORKFLOW_PATH = ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location("ca_sco_semantic_runner_refresh_contract", RUNNER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RUNNER = _load_runner()


def test_refreshed_proposal_validates_and_remains_non_authorizing() -> None:
    proposal = _load(PROPOSAL_PATH)
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(proposal)

    assert proposal["proposal_version"] == "1.1.0"
    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    fresh = proposal["fresh_authorization_requirements"]
    assert isinstance(fresh, dict)
    assert fresh["execution_approval_status"] == "REQUIRED_NOT_GRANTED"
    assert fresh["execution_approval_ref"] is None
    assert fresh["transient_row_privacy_approval_status"] == "REQUIRED_NOT_GRANTED"
    assert fresh["transient_row_privacy_approval_ref"] is None
    assert fresh["network_workflow_creation_authorized"] is False
    assert fresh["real_execution_authorized"] is False
    assert not WORKFLOW_PATH.exists()


def test_refreshed_proposal_is_bound_to_adopted_runner_baseline() -> None:
    proposal = _load(PROPOSAL_PATH)
    baseline = proposal["adopted_transport_baseline"]
    sample = proposal["sample_plan"]
    base = proposal["base_state"]
    assert isinstance(baseline, dict)
    assert isinstance(sample, dict)
    assert isinstance(base, dict)

    assert base["head_sha"] == "6188806e58ac87ccde7b8d6d20dcb2bbbec67c28"
    assert base["head_ci_run"] == "35210199280"
    assert base["baseline_adopted"] is True
    assert baseline["expected_length"] == RUNNER.EXPECTED_LENGTH == 162_560_390
    assert baseline["expected_etag"] == RUNNER.EXPECTED_ETAG == '"222dd79f04c2a0a8fff166b01c8da746"'

    expected_members = [
        {"name": member.name, "local_header_offset": member.local_header_offset}
        for member in RUNNER.CANONICAL_MEMBERS
    ]
    assert baseline["canonical_members"] == expected_members
    assert sample["canonical_members"] == expected_members
    assert [item["local_header_offset"] for item in expected_members] == [
        0,
        59_745_428,
        96_861_315,
        134_172_553,
    ]


def test_refresh_preserves_historical_proposal_as_provenance() -> None:
    refreshed = _load(PROPOSAL_PATH)
    historical = _load(HISTORICAL_PROPOSAL_PATH)
    assert refreshed["supersedes_proposal_version"] == historical["proposal_version"] == "1.0.0"
    historical_offsets = [
        item["local_header_offset"] for item in historical["sample_plan"]["canonical_members"]
    ]
    assert historical_offsets == [0, 59_747_797, 96_862_896, 134_174_190]
    assert historical_offsets != [
        item["local_header_offset"] for item in refreshed["sample_plan"]["canonical_members"]
    ]


def test_design_caps_d008_privacy_and_parser_boundary_are_unchanged() -> None:
    proposal = _load(PROPOSAL_PATH)
    sample = proposal["sample_plan"]
    caps = proposal["transport_caps"]
    controls = proposal["row_processing_controls"]
    outcome = proposal["v1_2_outcome_contract"]
    privacy = proposal["privacy_controls"]
    assert isinstance(sample, dict)
    assert isinstance(caps, dict)
    assert isinstance(controls, dict)
    assert isinstance(outcome, dict)
    assert isinstance(privacy, dict)

    assert sample["data_rows_max_per_member"] == RUNNER.MAX_ROWS_PER_MEMBER == 4
    assert sample["data_rows_max_total"] == RUNNER.MAX_ROWS_TOTAL == 16
    assert caps["head_requests_max"] == RUNNER.MAX_HEAD_REQUESTS == 1
    assert caps["range_requests_max"] == RUNNER.MAX_RANGE_REQUESTS == 4
    assert caps["http_requests_max_total"] == RUNNER.MAX_HTTP_REQUESTS == 5
    assert caps["range_response_bytes_max_each"] == RUNNER.RANGE_RESPONSE_BYTES
    assert caps["source_response_body_bytes_max_total"] == RUNNER.MAX_TOTAL_RESPONSE_BYTES
    assert caps["automatic_widening_allowed"] is False
    assert caps["automatic_retry_allowed"] is False
    assert controls["property_type_code_shape_regex"] == RUNNER.PROPERTY_TYPE_RE.pattern
    assert controls["trimming_allowed"] is False
    assert controls["uppercasing_allowed"] is False
    assert controls["normalization_allowed"] is False
    assert controls["parser_change_allowed"] is False
    assert controls["projector_change_allowed"] is False
    assert outcome["property_type_format_unexpected_control_status_code"] == RUNNER.PROPERTY_TYPE_NONCONFORMING_STATUS
    assert outcome["property_type_format_unexpected_control_reason_code"] == RUNNER.PROPERTY_TYPE_NONCONFORMING_REASON
    assert outcome["source_continuation_after_property_type_format_unexpected"] is False
    assert privacy["memory_only"] is True
    assert privacy["per_row_property_type_persistence"] is False
    assert privacy["row_specific_human_inspection"] is False


def test_schema_rejects_baseline_or_authorization_widening() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = Draft202012Validator(_load(SCHEMA_PATH))

    wrong_offset = copy.deepcopy(proposal)
    wrong_offset["sample_plan"]["canonical_members"][1]["local_header_offset"] = 59_747_797

    execution = copy.deepcopy(proposal)
    execution["fresh_authorization_requirements"]["real_execution_authorized"] = True

    retry = copy.deepcopy(proposal)
    retry["transport_caps"]["automatic_retry_allowed"] = True

    normalization = copy.deepcopy(proposal)
    normalization["row_processing_controls"]["normalization_allowed"] = True

    for invalid in (wrong_offset, execution, retry, normalization):
        with pytest.raises(ValidationError):
            validator.validate(invalid)
