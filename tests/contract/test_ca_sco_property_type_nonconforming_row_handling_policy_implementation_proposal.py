from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/"
    "property_type_nonconforming_row_handling_policy_implementation_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus."
    "property_type_nonconforming_row_handling_policy_implementation.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
V1_1_SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_semantic_verification_execution.v1_1.schema.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_implementation_proposal_validates_and_remains_unauthorized() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    boundary = proposal["implementation_authorization_boundary"]
    assert isinstance(boundary, dict)
    assert boundary["proposal_preparation_authorized"] is True
    for key, value in boundary.items():
        if key != "proposal_preparation_authorized":
            assert value is False


def test_base_is_pinned_to_d008_review_and_design() -> None:
    proposal = _load(PROPOSAL_PATH)
    base = proposal["base_state"]
    design = proposal["accepted_design_contract"]
    assert isinstance(base, dict)
    assert isinstance(design, dict)

    assert base["head_sha"] == "63a6b09cf129202021c80a1c04a479ca2186fe4b"
    assert base["head_ci_run"] == "35096424256"
    assert base["decision_record"] == "D-008"
    assert base["accepted_design_policy"] == "WHOLE_SOURCE_STOP"
    assert design["control_status_code"] == "PROPERTY_TYPE_NONCONFORMING_STOPPED"
    assert design["control_reason_code"] == "PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE"
    assert design["source_continuation_after_trigger"] is False
    assert design["real_row_or_field_retention"] is False


def test_minimal_delta_is_additive_versioned_and_backward_compatible() -> None:
    proposal = _load(PROPOSAL_PATH)
    plan = proposal["minimal_implementation_plan"]
    assert isinstance(plan, dict)
    assert plan["strategy"] == "ADDITIVE_VERSIONED_CONTROL_DISPOSITION"
    assert plan["planned_runtime_files_modified"] == [
        "scripts/ca_sco_property_type_semantic_verification.py"
    ]
    assert plan["planned_new_contract_files"] == [
        "schemas/common/property_type_semantic_verification_execution.v1_2.schema.json"
    ]
    assert plan["planned_existing_contract_files_modified"] == []
    assert plan["historical_v1_1_schema_remains_immutable"] is True
    assert plan["future_execution_schema_version"] == "1.2.0"

    delta = plan["runner_delta"]
    legacy = plan["legacy_compatibility"]
    shape = plan["future_control_disposition_shape"]
    assert isinstance(delta, dict)
    assert isinstance(legacy, dict)
    assert isinstance(shape, dict)

    assert delta["map_only_property_type_format_unexpected"] is True
    assert delta["property_type_projection_change"] is False
    assert delta["property_type_regex_change"] is False
    assert delta["normalization_change"] is False
    assert delta["source_continuation_change"] is False
    assert legacy["semantic_result_status_preserved"] is True
    assert legacy["stop_reason_preserved"] is True
    assert legacy["no_existing_field_removed_or_reinterpreted"] is True
    assert shape["allowed_persisted_fields"] == ["status_code", "reason_code"]
    assert shape["source_value_bearing_fields_allowed"] is False


def test_current_runner_and_v1_1_contract_are_still_unmodified() -> None:
    proposal = _load(PROPOSAL_PATH)
    preparation = proposal["preparation_state"]
    assert isinstance(preparation, dict)
    assert all(value is False for value in preparation.values())

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert '"schema_version": "1.1.0"' in runner_text
    assert (
        'PROPERTY_TYPE_RE = re.compile(r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$")'
        in runner_text
    )
    assert 'raise RunnerStop("PROPERTY_TYPE_FORMAT_UNEXPECTED")' in runner_text
    assert 'result["semantic_result_status"] = "STOPPED_FAIL_CLOSED"' in runner_text
    assert 'result["stop_reason"] = exc.reason' in runner_text
    assert "control_disposition" not in runner_text

    v1_1 = _load(V1_1_SCHEMA_PATH)
    assert v1_1["$id"] == (
        "urn:unclaimed-platform:schema:property-type-semantic-verification-execution:1.1.0"
    )
    properties = v1_1["properties"]
    assert isinstance(properties, dict)
    assert properties["schema_version"] == {"const": "1.1.0"}
    assert "control_disposition" not in properties


def test_continuation_privacy_validation_and_governance_remain_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    validation = proposal["validation_boundary"]
    continuation = proposal["continuation_boundary"]
    privacy = proposal["privacy_and_persistence_boundary"]
    assert isinstance(validation, dict)
    assert isinstance(continuation, dict)
    assert isinstance(privacy, dict)

    assert validation["regex"] == EXPECTED_REGEX
    assert validation["trim_before_validation"] is False
    assert validation["ascii_uppercase_before_validation"] is False
    assert validation["unicode_normalization_before_validation"] is False
    assert validation["alternate_token_acceptance"] is False
    assert validation["parser_or_projector_change"] is False
    assert continuation["continue_after_nonconforming_row"] is False
    assert continuation["later_rows_processed_after_trigger"] is False
    assert continuation["silent_row_skip_allowed"] is False
    assert continuation["silent_source_continuation_allowed"] is False
    assert privacy["may_persist_control_status_code"] is True
    assert privacy["may_persist_control_reason_code"] is True
    for key, value in privacy.items():
        if key not in {"may_persist_control_status_code", "may_persist_control_reason_code"}:
            assert value is False

    policy = _load(POLICY_PATH)
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False

    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    source = next(
        item
        for item in registry["sources"]
        if item["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False


def test_regression_and_rollback_plan_require_no_real_source_or_migration() -> None:
    proposal = _load(PROPOSAL_PATH)
    coverage = proposal["planned_regression_coverage"]
    rollback = proposal["rollback_plan"]
    reuse = proposal["reuse_and_scope"]
    assert isinstance(coverage, dict)
    assert isinstance(rollback, dict)
    assert isinstance(reuse, dict)

    assert coverage["synthetic_only"] is True
    assert len(coverage["tests"]) == 8
    assert coverage["real_source_test_required_for_implementation_acceptance"] is False
    assert coverage["real_source_execution_remains_separate_gate"] is True
    assert rollback["database_migration_required"] is False
    assert rollback["source_state_migration_required"] is False
    assert rollback["historical_evidence_migration_required"] is False
    assert rollback["rollback_restores_runner_output_schema_version"] == "1.1.0"
    assert reuse["new_external_dependency_required"] is False
    assert reuse["new_parser_required"] is False
    assert reuse["new_persistence_layer_required"] is False
    assert reuse["new_network_workflow_required"] is False


def test_schema_rejects_runtime_widening_or_existing_contract_mutation() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()
    invalid_cases: list[dict[str, object]] = []

    runtime = copy.deepcopy(proposal)
    runtime["implementation_authorization_boundary"]["runtime_code_change_authorized"] = True
    invalid_cases.append(runtime)

    continuation = copy.deepcopy(proposal)
    continuation["continuation_boundary"]["continue_after_nonconforming_row"] = True
    invalid_cases.append(continuation)

    privacy = copy.deepcopy(proposal)
    privacy["privacy_and_persistence_boundary"]["may_persist_exact_property_type"] = True
    invalid_cases.append(privacy)

    regex = copy.deepcopy(proposal)
    regex["validation_boundary"]["regex"] = ".*"
    invalid_cases.append(regex)

    mutation = copy.deepcopy(proposal)
    mutation["minimal_implementation_plan"]["planned_existing_contract_files_modified"] = [
        "schemas/common/property_type_semantic_verification_execution.v1_1.schema.json"
    ]
    invalid_cases.append(mutation)

    for invalid in invalid_cases:
        with pytest.raises(ValidationError):
            validator.validate(invalid)
