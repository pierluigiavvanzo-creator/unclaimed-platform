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
    "property_type_source_format_diagnostic_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_source_format_diagnostic.v1.json"
)
EXECUTION_EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_diagnostic.execution.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
FUTURE_WORKFLOW_PATH = (
    ROOT
    / ".github/workflows/"
    "ca-sco-property-type-source-format-diagnostic-once.yml"
)
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"
EXPECTED_CLASSES = [
    "FULL_ROW_UTF8_DECODE_FAILED",
    "STDLIB_STRICT_CSV_PARSE_FAILED",
    "STDLIB_COLUMN_SHAPE_NOT_CANONICAL",
    "PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER",
    "INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH",
]


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_proposal_validates_and_authorizes_nothing_beyond_preparation() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    auth = proposal["authorization_boundary"]
    assert isinstance(auth, dict)
    assert auth["proposal_preparation_authorized"] is True
    for key in (
        "source_format_diagnostic_execution_authorized",
        "full_row_transient_privacy_exposure_authorized",
        "network_workflow_authorized",
        "network_execution_authorized",
        "runtime_change_authorized",
        "parser_change_authorized",
        "regex_change_authorized",
        "remediation_authorized",
        "additional_authority_retrieval_authorized",
        "approval_token_defined_by_this_proposal",
    ):
        assert auth[key] is False


def test_base_is_pinned_to_reviewed_ascii_structural_mismatch() -> None:
    proposal = _load(PROPOSAL_PATH)
    base = proposal["base_state"]
    assert isinstance(base, dict)
    assert base["branch"] == "m3-ca-sco-property-type-diagnostic-evidence-review"
    assert base["head_sha"] == "9195d27e17b89703f7179a9db2ba5dccad43a75e"
    assert base["head_ci_run"] == "35058889923"
    assert base["diagnostic_execution_run_id"] == "35019840276"
    assert base["diagnostic_result_status"] == "DIAGNOSTIC_CLASSIFIED"
    assert base["diagnostic_class"] == "ASCII_STRUCTURAL_MISMATCH"
    assert base["diagnostic_evidence_review_decision"] == (
        "PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED"
    )

    evidence = _load(EXECUTION_EVIDENCE_PATH)
    assert evidence["diagnostic_result_status"] == "DIAGNOSTIC_CLASSIFIED"
    assert evidence["diagnostic_class"] == "ASCII_STRUCTURAL_MISMATCH"
    assert evidence["source_identity_verified"] is True
    assert evidence["head_requests"] == 1
    assert evidence["range_requests"] == 1
    assert evidence["http_requests_total"] == 2
    assert evidence["source_response_body_bytes_read"] == 131072
    assert evidence["transient_rows_examined"] == 1


def test_future_source_scope_does_not_widen_network_row_or_byte_budget() -> None:
    proposal = _load(PROPOSAL_PATH)
    scope = proposal["future_source_scope_if_later_authorized"]
    assert isinstance(scope, dict)
    assert scope["source_network_access_authorized_by_this_proposal"] is False
    assert scope["members_max"] == 1
    assert scope["transient_data_rows_max"] == 4
    assert scope["full_row_crosscheck_rows_max"] == 1
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
    assert scope["authority_network_access_allowed"] is False
    assert scope["other_source_or_endpoint_access_allowed"] is False


def test_independent_parser_and_privacy_boundaries_are_explicit() -> None:
    proposal = _load(PROPOSAL_PATH)
    parser = proposal["independent_parser_contract_if_later_authorized"]
    assert isinstance(parser, dict)
    assert parser["implementation"] == "PYTHON_STDLIB_CSV_READER"
    assert parser["strict"] is True
    assert parser["delimiter"] == ","
    assert parser["quotechar"] == '"'
    assert parser["doublequote"] is True
    assert parser["escapechar"] is None
    assert parser["skipinitialspace"] is False
    assert parser["row_text_decode"] == "UTF_8_STRICT"
    assert parser["canonical_column_count"] == 25
    assert parser["property_type_zero_based_index"] == 1
    assert parser["current_custom_projector_remains_unchanged"] is True
    assert parser["current_regex_remains_unchanged"] == EXPECTED_REGEX
    assert parser["unicode_normalization_allowed"] is False
    assert parser["runtime_remediation_allowed"] is False

    privacy = proposal["future_privacy_boundary_if_later_authorized"]
    assert isinstance(privacy, dict)
    assert privacy["full_row_transient_exposure_is_privacy_expansion"] is True
    assert privacy["full_row_transient_exposure_authorized_by_this_proposal"] is False
    assert privacy["full_row_transient_rows_max"] == 1
    assert privacy["fresh_execution_approval_required_before_network"] is True
    assert privacy["fresh_full_row_privacy_approval_required_before_network"] is True
    assert privacy["approval_tokens_defined_by_this_proposal"] is False
    for key in (
        "persist_full_row",
        "persist_any_row_field_value",
        "persist_property_type",
        "persist_property_type_bytes",
        "persist_property_type_hash",
        "persist_property_type_exact_length",
        "persist_property_type_fragments",
        "persist_property_type_codepoints",
        "persist_transformed_property_type",
        "persist_property_id",
        "persist_owner_holder_values",
        "persist_row_hash",
        "persist_row_exact_length",
        "record_source_values_in_logs",
        "source_derived_free_text_allowed",
    ):
        assert privacy[key] is False


def test_classes_are_categorical_and_do_not_auto_remediate() -> None:
    proposal = _load(PROPOSAL_PATH)
    classes = proposal["diagnostic_classes_if_later_authorized"]
    assert isinstance(classes, list)
    assert [item["class_id"] for item in classes] == EXPECTED_CLASSES
    assert all(item["automatic_remediation"] is False for item in classes)

    output = proposal["diagnostic_output_contract_if_later_authorized"]
    assert isinstance(output, dict)
    assert output["source_format_diagnostic_class_values"] == EXPECTED_CLASSES
    assert output["exact_or_derived_source_values_allowed"] is False
    assert output["source_derived_free_text_allowed"] is False
    assert output["parser_exception_text_allowed"] is False
    assert output["row_or_field_hashes_allowed"] is False

    decisions = proposal["decision_map"]
    assert isinstance(decisions, list)
    assert [item["diagnostic_class"] for item in decisions] == EXPECTED_CLASSES
    assert all(item["authorized_by_this_proposal"] is False for item in decisions)


def test_prior_approvals_remain_consumed_and_no_workflow_or_runtime_change_exists() -> None:
    proposal = _load(PROPOSAL_PATH)
    consumed = proposal["consumed_authorizations"]
    assert isinstance(consumed, list)
    assert len(consumed) == 5
    assert all(item["consumed"] is True for item in consumed)
    assert all(item["reusable"] is False for item in consumed)

    implementation = proposal["implementation_state"]
    assert isinstance(implementation, dict)
    for key in (
        "source_request_performed",
        "authority_request_performed",
        "full_row_source_access_performed",
        "diagnostic_execution_performed",
        "network_workflow_created",
        "runner_modified",
        "parser_modified",
        "regex_modified",
        "normalization_modified",
        "logging_modified",
        "persistence_modified",
    ):
        assert implementation[key] is False

    runner_text = RUNNER_PATH.read_text(encoding="utf-8")
    assert 'PROPERTY_TYPE_RE = re.compile(r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$")' in runner_text
    assert not FUTURE_WORKFLOW_PATH.exists()


def test_policy_registry_downstream_and_human_gate_remain_closed() -> None:
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
        "HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW"
    )


def test_schema_rejects_execution_privacy_widening_or_remediation() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()

    cases: list[dict[str, object]] = []
    execution = copy.deepcopy(proposal)
    execution["authorization_boundary"]["source_format_diagnostic_execution_authorized"] = True
    cases.append(execution)

    privacy = copy.deepcopy(proposal)
    privacy["authorization_boundary"]["full_row_transient_privacy_exposure_authorized"] = True
    cases.append(privacy)

    widened = copy.deepcopy(proposal)
    widened["future_source_scope_if_later_authorized"]["range_requests_max"] = 2
    cases.append(widened)

    persisted = copy.deepcopy(proposal)
    persisted["future_privacy_boundary_if_later_authorized"]["persist_full_row"] = True
    cases.append(persisted)

    remediated = copy.deepcopy(proposal)
    remediated["decision_map"][0]["authorized_by_this_proposal"] = True
    cases.append(remediated)

    for invalid in cases:
        with pytest.raises(ValidationError):
            validator.validate(invalid)
