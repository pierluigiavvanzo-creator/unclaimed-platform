from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_second_semantic_execution_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_second_semantic_execution.v1.json"
)
HISTORICAL_APPROVAL_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic_execution_approval.v1.json"
)
HISTORICAL_EXECUTION_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic.execution.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
EXECUTION_V1_1_SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_semantic_verification_execution.v1_1.schema.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
SOURCE_ID = "ca.sco.unclaimed_property.bulk"
EXPECTED_CANONICAL_BASE = "e97c1f62959f603bdd3df79538d4b70255594c70"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_property_type_semantic_verification_second_proposal",
        RUNNER_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_second_execution_proposal_is_valid_and_non_authorizing() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    fresh = proposal["fresh_authorization_requirements"]
    implementation = proposal["implementation_state"]
    assert isinstance(fresh, dict)
    assert isinstance(implementation, dict)
    assert fresh["execution_approval_status"] == "REQUIRED_NOT_GRANTED"
    assert fresh["execution_approval_ref"] is None
    assert fresh["transient_row_privacy_approval_status"] == "REQUIRED_NOT_GRANTED"
    assert fresh["transient_row_privacy_approval_ref"] is None
    assert fresh["network_workflow_creation_authorized"] is False
    assert fresh["real_execution_authorized"] is False
    assert implementation["network_workflow_present"] is False
    assert implementation["network_request_performed_during_proposal"] is False
    assert implementation["source_body_access_performed_during_proposal"] is False
    assert implementation["proposal_execution_performed"] is False


def test_historical_approvals_are_explicitly_consumed_and_not_reused() -> None:
    proposal = _load(PROPOSAL_PATH)
    historical = proposal["historical_attempt"]
    old_approval = _load(HISTORICAL_APPROVAL_PATH)
    old_execution = _load(HISTORICAL_EXECUTION_PATH)
    assert isinstance(historical, dict)

    assert historical["workflow_run"] == "34965097988"
    assert historical["schema_version"] == "1.0.0"
    assert (
        historical["result"]
        == old_execution["semantic_result_status"]
        == "STOPPED_FAIL_CLOSED"
    )
    assert (
        historical["stop_reason"]
        == old_execution["stop_reason"]
        == "PROPERTY_TYPE_FORMAT_UNEXPECTED"
    )
    assert historical["root_cause"] == "UNRESOLVED"
    assert historical["execution_approval_ref"] == old_approval["execution_approval_ref"]
    assert historical["privacy_approval_ref"] == old_approval["privacy_approval_ref"]
    assert historical["execution_approval_consumed"] is True
    assert historical["privacy_approval_consumed"] is True
    assert historical["approvals_reusable"] is False
    assert historical["offending_source_value_or_bytes_persisted"] is False


def test_proposal_is_pinned_to_historical_v1_1_contract_and_unchanged_caps() -> None:
    proposal = _load(PROPOSAL_PATH)
    runner = _load_runner()
    base = proposal["canonical_base"]
    caps = proposal["transport_caps"]
    controls = proposal["row_processing_controls"]
    historical_schema = _load(EXECUTION_V1_1_SCHEMA_PATH)
    assert isinstance(base, dict)
    assert isinstance(caps, dict)
    assert isinstance(controls, dict)

    assert base["branch"] == "m2-state-governance-core"
    assert base["sha"] == EXPECTED_CANONICAL_BASE
    assert base["future_execution_schema_version"] == "1.1.0"
    assert historical_schema["properties"]["schema_version"] == {"const": "1.1.0"}
    assert caps["head_requests_max"] == runner.MAX_HEAD_REQUESTS == 1
    assert caps["range_requests_max"] == runner.MAX_RANGE_REQUESTS == 4
    assert caps["http_requests_max_total"] == runner.MAX_HTTP_REQUESTS == 5
    assert (
        caps["range_response_bytes_max_each"]
        == runner.RANGE_RESPONSE_BYTES
        == 131_072
    )
    assert (
        caps["source_response_body_bytes_max_total"]
        == runner.MAX_TOTAL_RESPONSE_BYTES
        == 524_288
    )
    assert (
        caps["uncompressed_transient_bytes_max_each"]
        == runner.MAX_UNCOMPRESSED_BYTES_PER_MEMBER
        == 262_144
    )
    assert (
        caps["uncompressed_transient_bytes_max_total"]
        == runner.MAX_UNCOMPRESSED_BYTES_TOTAL
        == 1_048_576
    )
    assert (
        caps["logical_record_bytes_max"]
        == runner.MAX_LOGICAL_RECORD_BYTES
        == 32_768
    )
    assert caps["additional_range_allowed"] is False
    assert caps["full_body_fallback_allowed"] is False
    assert caps["automatic_widening_allowed"] is False
    expected_pattern = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"
    assert controls["property_type_code_shape_regex"] == expected_pattern
    assert runner.PROPERTY_TYPE_RE.pattern == expected_pattern


def test_v1_1_contract_contains_distinct_encoding_and_format_reasons() -> None:
    proposal = _load(PROPOSAL_PATH)
    execution_schema = _load(EXECUTION_V1_1_SCHEMA_PATH)
    reasons = proposal["stop_conditions"]
    diagnostic = proposal["v1_1_diagnostic_outcomes"]
    assert isinstance(reasons, list)
    assert isinstance(diagnostic, dict)

    assert "PROPERTY_TYPE_ENCODING_UNEXPECTED" in reasons
    assert "PROPERTY_TYPE_FORMAT_UNEXPECTED" in reasons
    assert (
        diagnostic["invalid_utf8_property_type_stop_reason"]
        == "PROPERTY_TYPE_ENCODING_UNEXPECTED"
    )
    assert (
        diagnostic["decoded_shape_mismatch_stop_reason"]
        == "PROPERTY_TYPE_FORMAT_UNEXPECTED"
    )
    assert diagnostic["historical_v1_stop_reinterpreted"] is False
    serialized = json.dumps(execution_schema, sort_keys=True)
    assert "PROPERTY_TYPE_ENCODING_UNEXPECTED" in serialized
    assert "PROPERTY_TYPE_FORMAT_UNEXPECTED" in serialized


def test_privacy_boundary_and_downstream_governance_remain_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    privacy = proposal["privacy_controls"]
    safety = proposal["safety_state"]
    policy = _load(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    assert isinstance(privacy, dict)
    assert isinstance(safety, dict)

    assert privacy["memory_only"] is True
    assert privacy["transient_buffer_retention_days"] == 0
    assert privacy["immediate_disposal"] is True
    for key in (
        "raw_body_persistence",
        "full_row_persistence",
        "property_id_persistence",
        "owner_holder_persistence",
        "per_row_property_type_persistence",
        "offending_bytes_persistence",
        "offending_value_hash_persistence",
        "offending_value_length_persistence",
        "record_values_in_logs",
    ):
        assert privacy[key] is False

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["authorized_processing_purposes"] == []
    assert policy["allowed_fields"] == []
    assert policy["allow_pii"] is False
    source = next(
        item for item in registry["sources"] if item["source_id"] == SOURCE_ID
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False
    assert all(value is False for value in safety.values())


def test_schema_blocks_approval_invention_cap_widening_and_privacy_widening() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()

    invented_approval = copy.deepcopy(proposal)
    invented_approval["fresh_authorization_requirements"][
        "real_execution_authorized"
    ] = True
    with pytest.raises(ValidationError):
        validator.validate(invented_approval)

    cap_widened = copy.deepcopy(proposal)
    cap_widened["transport_caps"]["http_requests_max_total"] = 6
    with pytest.raises(ValidationError):
        validator.validate(cap_widened)

    privacy_widened = copy.deepcopy(proposal)
    privacy_widened["privacy_controls"]["per_row_property_type_persistence"] = True
    with pytest.raises(ValidationError):
        validator.validate(privacy_widened)
