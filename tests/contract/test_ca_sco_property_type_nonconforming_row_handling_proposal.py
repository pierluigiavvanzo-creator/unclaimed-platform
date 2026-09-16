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
    "property_type_nonconforming_row_handling_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_nonconforming_row_handling.v1.json"
)
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_source_format_diagnostic.execution.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"
EXPECTED_OPTIONS = [
    "WHOLE_SOURCE_STOP",
    "ROW_LEVEL_DEFER_OR_QUARANTINE",
    "HUMAN_REVIEW_ROUTE",
]
EXPECTED_STATUSES = [
    "PROPERTY_TYPE_NONCONFORMING_STOPPED",
    "PROPERTY_TYPE_NONCONFORMING_DEFERRED_POLICY_REQUIRED",
    "PROPERTY_TYPE_NONCONFORMING_HUMAN_REVIEW_REQUIRED",
]
EXPECTED_REASONS = [
    "PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE",
    "ROW_CONTINUATION_POLICY_NOT_AUTHORIZED",
    "REAL_ROW_RETENTION_NOT_AUTHORIZED",
    "ROW_SPECIFIC_HUMAN_INSPECTION_NOT_AUTHORIZED",
]


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_proposal_validates_and_selects_no_handling_policy() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    options = proposal["candidate_handling_options"]
    assert isinstance(options, list)
    assert [item["option_id"] for item in options] == EXPECTED_OPTIONS
    assert all(item["fail_closed"] is True for item in options)
    assert all(item["authorized_by_this_proposal"] is False for item in options)

    constraints = proposal["proposal_comparison_constraints"]
    assert isinstance(constraints, dict)
    assert constraints["selected_option"] is None
    assert constraints["selection_authorized_by_this_proposal"] is False
    assert constraints["silent_row_skip_allowed"] is False
    assert constraints["silent_source_continuation_allowed"] is False
    assert constraints["silent_semantic_acceptance_allowed"] is False
    assert constraints["automatic_correction_allowed"] is False
    assert constraints["normalization_allowed"] is False
    assert constraints["regex_relaxation_allowed"] is False


def test_base_is_pinned_to_green_source_format_evidence_review() -> None:
    proposal = _load(PROPOSAL_PATH)
    base = proposal["base_state"]
    assert isinstance(base, dict)
    assert base["branch"] == (
        "m3-ca-sco-property-type-source-format-diagnostic-evidence-review"
    )
    assert base["head_sha"] == "27b1a19874449b0170fc0c47328340122d443529"
    assert base["head_ci_run"] == "35092673600"
    assert base["source_format_execution_run_id"] == "35090057224"
    assert base["source_format_diagnostic_class"] == (
        "INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH"
    )
    assert base["source_format_evidence_review_decision"] == (
        "PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_"
        "NO_RUNTIME_CHANGE_AUTHORIZED"
    )

    evidence = _load(EVIDENCE_PATH)
    assert evidence["diagnostic_result_status"] == "SOURCE_FORMAT_CLASSIFIED"
    assert evidence["source_format_diagnostic_class"] == (
        "INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH"
    )
    assert evidence["source_identity_verified"] is True
    assert evidence["head_requests"] == 1
    assert evidence["range_requests"] == 1
    assert evidence["http_requests_total"] == 2
    assert evidence["source_response_body_bytes_read"] == 131072
    assert evidence["transient_rows_examined"] == 1
    assert evidence["full_row_crosscheck_rows_examined"] == 1


def test_validation_contract_is_unchanged_and_no_normalization_is_allowed() -> None:
    proposal = _load(PROPOSAL_PATH)
    validation = proposal["unchanged_validation_contract"]
    assert isinstance(validation, dict)
    assert validation["property_type_zero_based_index"] == 1
    assert validation["regex"] == EXPECTED_REGEX
    assert validation["trim_before_validation"] is False
    assert validation["ascii_uppercase_before_validation"] is False
    assert validation["unicode_normalization_before_validation"] is False
    assert validation["alternate_token_acceptance"] is False
    assert validation["parser_or_projector_change"] is False

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    expected_line = (
        'PROPERTY_TYPE_RE = re.compile(r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$")'
    )
    assert expected_line in runner_text


def test_non_value_bearing_control_contract_and_privacy_boundary_are_locked() -> None:
    proposal = _load(PROPOSAL_PATH)
    control = proposal["non_value_bearing_control_contract"]
    assert isinstance(control, dict)
    assert control["status_codes"] == EXPECTED_STATUSES
    assert control["reason_codes"] == EXPECTED_REASONS
    for key in (
        "may_persist_exact_property_type",
        "may_persist_property_type_derivative",
        "may_persist_row_or_field_hash",
        "may_persist_exact_row_or_field_length",
        "may_persist_property_id",
        "may_persist_owner_holder_values",
        "may_persist_source_derived_free_text",
        "may_log_real_row_or_field_content",
    ):
        assert control[key] is False

    privacy = proposal["privacy_and_persistence_boundaries"]
    assert isinstance(privacy, dict)
    assert privacy["metadata_only_handling_design_requires_privacy_expansion"] is False
    assert privacy["real_row_or_field_retention_is_privacy_expansion"] is True
    assert privacy["real_row_or_field_retention_authorized_by_this_proposal"] is False
    assert privacy["row_specific_human_inspection_is_privacy_expansion"] is True
    assert privacy["row_specific_human_inspection_authorized_by_this_proposal"] is False
    assert (
        privacy["future_privacy_expansion_requires_separate_reviewed_authorization_path"]
        is True
    )
    assert (
        privacy["future_real_source_execution_requires_separate_reviewed_authorization_path"]
        is True
    )
    assert privacy["approval_tokens_defined_by_this_proposal"] is False


def test_proposal_authorizes_only_offline_preparation() -> None:
    proposal = _load(PROPOSAL_PATH)
    auth = proposal["authorization_boundary"]
    assert isinstance(auth, dict)
    assert auth["proposal_preparation_authorized"] is True
    for key, value in auth.items():
        if key != "proposal_preparation_authorized":
            assert value is False

    implementation = proposal["implementation_state"]
    assert isinstance(implementation, dict)
    assert implementation["proposal_only"] is True
    for key, value in implementation.items():
        if key not in {"proposal_branch", "proposal_only"}:
            assert value is False

    consumed = proposal["consumed_authorizations"]
    assert isinstance(consumed, list)
    assert len(consumed) == 7
    assert all(item["consumed"] is True for item in consumed)
    assert all(item["reusable"] is False for item in consumed)


def test_policy_registry_production_and_downstream_gates_remain_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    safety = proposal["safety_state"]
    assert isinstance(safety, dict)
    assert safety["source_policy_status"] == "PROPOSED"
    assert safety["registry_enabled"] is False
    assert safety["registry_approved_for_use"] is False
    assert safety["approved_real_sources"] == 0
    assert safety["authority_provenance_resolved"] is True
    assert safety["semantic_compatibility_resolved"] is False
    assert safety["production_classification_active"] is False
    assert safety["downstream_gates_remain_closed"] is True

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
    assert proposal["next_gate"] == (
        "HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW"
    )


def test_schema_rejects_policy_selection_privacy_or_runtime_authorization() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()

    invalid_cases: list[dict[str, object]] = []

    selected = copy.deepcopy(proposal)
    selected["proposal_comparison_constraints"]["selected_option"] = "WHOLE_SOURCE_STOP"
    invalid_cases.append(selected)

    continuation = copy.deepcopy(proposal)
    continuation["proposal_comparison_constraints"]["silent_source_continuation_allowed"] = True
    invalid_cases.append(continuation)

    retained = copy.deepcopy(proposal)
    retained["privacy_and_persistence_boundaries"][
        "real_row_or_field_retention_authorized_by_this_proposal"
    ] = True
    invalid_cases.append(retained)

    runtime = copy.deepcopy(proposal)
    runtime["authorization_boundary"]["runtime_handling_change_authorized"] = True
    invalid_cases.append(runtime)

    regex = copy.deepcopy(proposal)
    regex["unchanged_validation_contract"]["regex"] = ".*"
    invalid_cases.append(regex)

    for invalid in invalid_cases:
        with pytest.raises(ValidationError):
            validator.validate(invalid)
