from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/"
    "property_type_diagnostic_remediation_evidence_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_diagnostic_remediation_evidence.v1.json"
)
AUTHORITY_REVIEW_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_authority_archive_provenance.review.v1.json"
)
SECOND_EXECUTION_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
FUTURE_DIAGNOSTIC_WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-diagnostic-remediation-once.yml"
)
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"
EXPECTED_CLASSES = [
    "SURROUNDING_ASCII_WHITESPACE_ONLY",
    "ASCII_CASE_ONLY",
    "SURROUNDING_ASCII_WHITESPACE_AND_CASE",
    "NON_ASCII_OR_CONTROL_CONTENT",
    "ASCII_STRUCTURAL_MISMATCH",
]


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_proposal_is_schema_valid_and_not_authorized_for_execution() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    authorization = proposal["authorization_boundary"]
    assert isinstance(authorization, dict)
    assert authorization["proposal_preparation_authorized"] is True
    assert authorization["diagnostic_execution_authorized"] is False
    assert authorization["transient_row_privacy_exposure_authorized"] is False
    assert authorization["network_workflow_authorized"] is False
    assert authorization["runtime_change_authorized"] is False
    assert authorization["remediation_authorized"] is False
    assert authorization["third_semantic_execution_authorized"] is False
    assert authorization["approval_token_defined_by_this_proposal"] is False
    assert authorization["fresh_execution_and_privacy_approvals_required_after_human_review"] is True


def test_base_is_pinned_to_verified_review_and_second_execution() -> None:
    proposal = _load(PROPOSAL_PATH)
    base = proposal["base_state"]
    assert isinstance(base, dict)
    assert base["branch"] == "m3-ca-sco-property-type-authority-archive-provenance-review"
    assert base["head_sha"] == "961d6a908dd9656f5ce19823be074011010833bf"
    assert base["head_ci_run"] == "35014204079"
    assert base["authority_review_package_sha"] == (
        "0b08163c624165fed4394e74265363fab53b2f5a"
    )
    assert base["authority_review_ci"] == "35013841037"
    assert base["second_execution_run_id"] == "34995672539"
    assert base["second_execution_schema_version"] == "1.1.0"
    assert base["second_execution_result"] == "STOPPED_FAIL_CLOSED"
    assert base["second_execution_stop_reason"] == "PROPERTY_TYPE_FORMAT_UNEXPECTED"

    authority_review = _load(AUTHORITY_REVIEW_PATH)
    decision = authority_review["decision"]
    assert isinstance(decision, dict)
    assert decision["result"] == (
        "ARCHIVED_AUTHORITY_RESOLVES_TARGET_PROVENANCE_SOURCE_SEMANTIC_MISMATCH_REMAINS"
    )
    assert decision["current_shape_regex_contradicted_by_authority"] is False
    assert decision["semantic_compatibility_resolved"] is False

    second = _load(SECOND_EXECUTION_PATH)
    assert second["schema_version"] == "1.1.0"
    assert second["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert second["stop_reason"] == "PROPERTY_TYPE_FORMAT_UNEXPECTED"
    requests = second["requests_summary"]
    assert isinstance(requests, dict)
    assert requests == {
        "head_requests": 1,
        "http_requests_total": 2,
        "range_requests": 1,
        "total_body_bytes_read": 131072,
    }


def test_future_diagnostic_scope_is_stricter_and_fail_closed() -> None:
    proposal = _load(PROPOSAL_PATH)
    scope = proposal["future_diagnostic_scope_if_later_authorized"]
    assert isinstance(scope, dict)
    assert scope["source_network_access_authorized_by_this_proposal"] is False
    assert scope["canonical_member"] == "From_500_To_Beyond_1_of_4.csv"
    assert scope["members_max"] == 1
    assert scope["transient_data_rows_max"] == 4
    assert scope["stop_at_first_reproduced_format_mismatch"] is True
    assert scope["head_requests_max"] == 1
    assert scope["range_requests_max"] == 1
    assert scope["http_requests_max_total"] == 2
    assert scope["range_response_bytes_max_each"] == 131072
    assert scope["source_response_body_bytes_max_total"] == 131072
    assert scope["uncompressed_transient_bytes_max_total"] == 262144
    assert scope["logical_record_bytes_max"] == 32768
    assert scope["retries_max"] == 0
    assert scope["redirects_allowed"] is False
    assert scope["additional_range_allowed"] is False
    assert scope["full_body_fallback_allowed"] is False
    assert scope["automatic_widening_allowed"] is False
    assert scope["source_identity_drift_behavior"] == "STOP_FAIL_CLOSED"
    assert scope["mismatch_not_reproduced_within_bound_behavior"] == (
        "STOP_FAIL_CLOSED"
    )
    assert scope["authority_network_access_allowed"] is False
    assert scope["other_source_or_endpoint_access_allowed"] is False


def test_diagnostic_derivation_is_categorical_and_non_value_bearing() -> None:
    proposal = _load(PROPOSAL_PATH)
    boundary = proposal["diagnostic_derivation_boundary_if_later_authorized"]
    assert isinstance(boundary, dict)
    assert boundary["current_regex"] == EXPECTED_REGEX
    assert boundary["unicode_normalization_probe_allowed"] is False
    assert boundary["stdlib_full_row_parser_crosscheck_allowed"] is False
    assert boundary["custom_parser_change_allowed"] is False
    assert boundary["regex_change_allowed"] is False
    assert boundary["regex_relaxation_allowed"] is False
    assert boundary["source_value_acceptance_after_probe_allowed"] is False
    assert boundary["remediation_application_during_diagnostic_allowed"] is False

    for key in (
        "persist_exact_property_type",
        "persist_property_type_bytes",
        "persist_property_type_hash",
        "persist_property_type_exact_length",
        "persist_property_type_fragments",
        "persist_property_type_codepoints",
        "persist_transformed_property_type",
        "persist_full_row",
        "persist_raw_response_body",
        "persist_property_id",
        "persist_owner_holder_values",
        "record_source_values_in_logs",
    ):
        assert boundary[key] is False

    classes = proposal["diagnostic_classes"]
    assert isinstance(classes, list)
    assert [item["class_id"] for item in classes] == EXPECTED_CLASSES
    assert all(item["automatic_remediation"] is False for item in classes)

    output = proposal["diagnostic_output_contract_if_later_authorized"]
    assert isinstance(output, dict)
    assert output["diagnostic_class_values"] == EXPECTED_CLASSES
    assert output["free_text_source_derived_output_allowed"] is False
    assert output["per_row_value_output_allowed"] is False
    assert output["distinct_property_type_code_output_allowed"] is False
    assert output["transformed_value_output_allowed"] is False


def test_no_remediation_is_implicitly_authorized() -> None:
    proposal = _load(PROPOSAL_PATH)
    remediation = proposal["remediation_decision_map"]
    assert isinstance(remediation, list)
    assert [item["diagnostic_class"] for item in remediation] == EXPECTED_CLASSES
    assert all(item["authorized_by_this_proposal"] is False for item in remediation)

    parser = proposal["parser_boundary"]
    assert isinstance(parser, dict)
    assert parser["current_custom_projector_remains_unchanged"] is True
    assert parser["real_row_stdlib_csv_crosscheck_in_scope"] is False
    assert parser["existing_synthetic_stdlib_differential_matrix_remains_relevant"] is True

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert 'PROPERTY_TYPE_RE = re.compile(r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$")' in runner_text
    assert 'raise RunnerStop("PROPERTY_TYPE_ENCODING_UNEXPECTED")' in runner_text
    assert 'raise RunnerStop("PROPERTY_TYPE_FORMAT_UNEXPECTED")' in runner_text
    assert not FUTURE_DIAGNOSTIC_WORKFLOW_PATH.exists()


def test_consumed_approvals_are_explicitly_non_reusable() -> None:
    proposal = _load(PROPOSAL_PATH)
    consumed = proposal["consumed_authorizations"]
    assert isinstance(consumed, list)
    assert {item["approval_ref"] for item in consumed} == {
        "APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED",
        "APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED",
        "APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT",
    }
    assert all(item["consumed"] is True for item in consumed)
    assert all(item["reusable"] is False for item in consumed)


def test_policy_registry_and_downstream_gates_remain_closed() -> None:
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
    assert safety["identity_resolution_allowed"] is False
    assert safety["genealogy_allowed"] is False
    assert safety["beneficiary_matching_allowed"] is False
    assert safety["outreach_allowed"] is False
    assert safety["claim_submission_allowed"] is False

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


def test_next_gate_is_review_only_and_schema_rejects_silent_widening() -> None:
    proposal = _load(PROPOSAL_PATH)
    assert proposal["next_gate"] == (
        "HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW"
    )
    validator = _validator()

    execution = copy.deepcopy(proposal)
    execution["authorization_boundary"]["diagnostic_execution_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(execution)

    privacy = copy.deepcopy(proposal)
    privacy["authorization_boundary"]["transient_row_privacy_exposure_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(privacy)

    widened = copy.deepcopy(proposal)
    widened["future_diagnostic_scope_if_later_authorized"]["range_requests_max"] = 2
    with pytest.raises(ValidationError):
        validator.validate(widened)

    value_persistence = copy.deepcopy(proposal)
    value_persistence["diagnostic_derivation_boundary_if_later_authorized"] [
        "persist_property_type_hash"
    ] = True
    with pytest.raises(ValidationError):
        validator.validate(value_persistence)

    approval_reuse = copy.deepcopy(proposal)
    approval_reuse["consumed_authorizations"][0]["reusable"] = True
    with pytest.raises(ValidationError):
        validator.validate(approval_reuse)

    remediation = copy.deepcopy(proposal)
    remediation["remediation_decision_map"][0]["authorized_by_this_proposal"] = True
    with pytest.raises(ValidationError):
        validator.validate(remediation)
