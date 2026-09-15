from __future__ import annotations

import copy
import json
import re
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/"
    "property_type_diagnostic_execution_authorization.schema.json"
)
ARTIFACT_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_diagnostic_execution_authorization.v1.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_diagnostic_remediation_evidence.v1.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
FUTURE_WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-diagnostic-remediation-once.yml"
)
EXECUTION_APPROVAL_PATH = (
    ROOT / "sources/evidence/ca_sco_property_type_diagnostic_execution_approval.v1.json"
)
PRIVACY_APPROVAL_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_property_type_diagnostic_transient_row_privacy_approval.v1.json"
)
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"
EXPECTED_CLASSES = [
    "SURROUNDING_ASCII_WHITESPACE_ONLY",
    "ASCII_CASE_ONLY",
    "SURROUNDING_ASCII_WHITESPACE_AND_CASE",
    "NON_ASCII_OR_CONTROL_CONTENT",
    "ASCII_STRUCTURAL_MISMATCH",
]
EXPECTED_FAIL_REASONS = [
    "APPROVAL_EVIDENCE_INVALID_OR_INCOMPLETE",
    "SOURCE_IDENTITY_DRIFT",
    "HEAD_REQUEST_FAILED",
    "HEAD_RESPONSE_UNEXPECTED",
    "RANGE_REQUEST_FAILED",
    "RANGE_RESPONSE_UNEXPECTED",
    "SOURCE_RESPONSE_BYTE_BUDGET_EXCEEDED",
    "UNCOMPRESSED_TRANSIENT_BYTE_BUDGET_EXCEEDED",
    "LOGICAL_RECORD_BYTE_BUDGET_EXCEEDED",
    "CANONICAL_MEMBER_UNEXPECTED",
    "CSV_PROJECTION_FAILED",
    "PROPERTY_TYPE_ENCODING_UNEXPECTED",
    "PROPERTY_TYPE_EMPTY_UNEXPECTED",
    "FORMAT_MISMATCH_NOT_REPRODUCED_WITHIN_BOUND",
    "CLASSIFIER_INVARIANT_VIOLATION",
    "PERSISTENCE_BOUNDARY_VIOLATION",
    "NETWORK_BOUNDARY_VIOLATION",
]
EXPECTED_CONTROLS = [*(f"U+{value:04X}" for value in range(0x20)), "U+007F"]


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _ascii_upper(value: str) -> str:
    chars: list[str] = []
    for char in value:
        code = ord(char)
        if 0x61 <= code <= 0x7A:
            chars.append(chr(code - 0x20))
        else:
            chars.append(char)
    return "".join(chars)


def _classify(value: str) -> str:
    pattern = re.compile(EXPECTED_REGEX)
    assert value
    assert pattern.fullmatch(value) is None

    stripped = value.strip(" \t")
    if stripped != value and pattern.fullmatch(stripped):
        return "SURROUNDING_ASCII_WHITESPACE_ONLY"

    upper = _ascii_upper(value)
    if upper != value and pattern.fullmatch(upper):
        return "ASCII_CASE_ONLY"

    combined = _ascii_upper(stripped)
    if combined != value and pattern.fullmatch(combined):
        return "SURROUNDING_ASCII_WHITESPACE_AND_CASE"

    if any(ord(char) > 0x7F or ord(char) < 0x20 or ord(char) == 0x7F for char in value):
        return "NON_ASCII_OR_CONTROL_CONTENT"

    return "ASCII_STRUCTURAL_MISMATCH"


def test_artifact_validates_and_remains_not_authorized() -> None:
    artifact = _load(ARTIFACT_PATH)
    _validator().validate(artifact)

    assert artifact["status"] == "PENDING_HUMAN_AUTHORIZATION"
    assert artifact["gate"] == "HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW"
    assert artifact["review_base_sha"] == "06896084475f0f899fc3e002344e22fc49ffa54d"
    assert artifact["proposal_package_sha"] == "020044d3013449fabe566c5164b8f99f9d8cc9ab"

    authorization = artifact["authorization_boundary"]
    assert isinstance(authorization, dict)
    assert authorization["artifact_preparation_authorized"] is True
    assert authorization["diagnostic_execution_authorized"] is False
    assert authorization["transient_row_privacy_exposure_authorized"] is False
    assert authorization["network_workflow_creation_authorized"] is False
    assert authorization["network_execution_authorized"] is False
    assert authorization["runtime_change_authorized"] is False
    assert authorization["remediation_authorized"] is False
    assert authorization["third_real_execution_authorized"] is False


def test_fresh_approvals_are_distinct_single_use_non_reusable_and_not_granted() -> None:
    artifact = _load(ARTIFACT_PATH)
    approvals = artifact["required_approvals"]
    assert isinstance(approvals, dict)
    execution = approvals["execution"]
    privacy = approvals["transient_row_privacy"]
    assert isinstance(execution, dict)
    assert isinstance(privacy, dict)

    assert execution["approval_ref"] == "APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED"
    assert privacy["approval_ref"] == (
        "APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED"
    )
    assert execution["approval_ref"] != privacy["approval_ref"]
    for approval in (execution, privacy):
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["approval_must_pin_artifact_sha"] is True
        assert approval["granted"] is False
    assert approvals["both_required_before_network"] is True

    consumed = set(artifact["consumed_prior_approvals"])
    assert execution["approval_ref"] not in consumed
    assert privacy["approval_ref"] not in consumed
    assert not EXECUTION_APPROVAL_PATH.exists()
    assert not PRIVACY_APPROVAL_PATH.exists()
    assert not FUTURE_WORKFLOW_PATH.exists()


def test_execution_boundary_does_not_widen_reviewed_proposal() -> None:
    artifact = _load(ARTIFACT_PATH)
    proposal = _load(PROPOSAL_PATH)
    execution = artifact["execution_boundary"]
    proposed = proposal["future_diagnostic_scope_if_later_authorized"]
    assert isinstance(execution, dict)
    assert isinstance(proposed, dict)

    for key in (
        "exact_endpoint",
        "expected_content_length",
        "expected_etag",
        "expected_media_type",
        "expected_accept_ranges",
        "canonical_member",
        "canonical_member_local_header_offset",
        "members_max",
        "transient_data_rows_max",
        "stop_at_first_reproduced_format_mismatch",
        "head_requests_max",
        "range_requests_max",
        "http_requests_max_total",
        "range_response_bytes_max_each",
        "source_response_body_bytes_max_total",
        "uncompressed_transient_bytes_max_total",
        "logical_record_bytes_max",
        "retries_max",
        "redirects_allowed",
        "additional_range_allowed",
        "full_body_fallback_allowed",
        "automatic_widening_allowed",
        "authority_network_access_allowed",
        "other_source_or_endpoint_access_allowed",
        "source_identity_drift_behavior",
        "mismatch_not_reproduced_within_bound_behavior",
    ):
        assert execution[key] == proposed[key]


def test_classifier_contract_is_fully_deterministic() -> None:
    artifact = _load(ARTIFACT_PATH)
    classifier = artifact["classifier_contract"]
    assert isinstance(classifier, dict)
    assert classifier["current_regex"] == EXPECTED_REGEX
    assert classifier["classification_precedence"] == EXPECTED_CLASSES
    assert classifier["surrounding_ascii_whitespace_codepoints"] == ["U+0020", "U+0009"]
    assert classifier["non_ascii_definition"] == "ANY_CODEPOINT_GREATER_THAN_U+007F"
    assert classifier["disallowed_ascii_control_codepoints"] == EXPECTED_CONTROLS

    mapping = classifier["ascii_uppercase_mapping"]
    assert isinstance(mapping, dict)
    assert mapping == {
        "input_range": "U+0061-U+007A",
        "output_range": "U+0041-U+005A",
        "offset": -32,
        "all_other_codepoints_unchanged": True,
        "locale_sensitive_behavior_allowed": False,
        "unicode_normalization_allowed": False,
    }
    assert classifier["runtime_transform_acceptance_allowed"] is False
    assert classifier["remediation_during_diagnostic_allowed"] is False


def test_synthetic_classifier_vectors_cover_classes_and_precedence() -> None:
    artifact = _load(ARTIFACT_PATH)
    vectors = artifact["synthetic_classifier_vectors"]
    assert isinstance(vectors, list)
    observed_classes: set[str] = set()
    for vector in vectors:
        assert isinstance(vector, dict)
        expected = vector["expected_class"]
        assert isinstance(expected, str)
        assert _classify(vector["input"]) == expected
        observed_classes.add(expected)

    assert observed_classes == set(EXPECTED_CLASSES)
    assert _classify("\tIN01\t") == "SURROUNDING_ASCII_WHITESPACE_ONLY"
    assert _classify("\tin01\t") == "SURROUNDING_ASCII_WHITESPACE_AND_CASE"
    assert _classify("IN\t01") == "NON_ASCII_OR_CONTROL_CONTENT"
    assert _ascii_upper("éa-z") == "éA-Z"


def test_fail_closed_output_is_enumerated_and_non_value_bearing() -> None:
    artifact = _load(ARTIFACT_PATH)
    assert artifact["fail_closed_reason_codes"] == EXPECTED_FAIL_REASONS

    output = artifact["output_contract"]
    assert isinstance(output, dict)
    assert output["diagnostic_class_when_stopped_fail_closed"] is None
    assert output["fail_closed_reason_code_when_classified"] is None
    assert output["fail_closed_reason_code_when_stopped_fail_closed"] == (
        "REQUIRED_ONE_OF_FAIL_CLOSED_REASON_CODES"
    )
    for key in (
        "source_derived_free_text_allowed",
        "exact_property_type_allowed",
        "property_type_bytes_allowed",
        "property_type_hash_allowed",
        "property_type_exact_length_allowed",
        "property_type_fragments_allowed",
        "property_type_codepoints_allowed",
        "transformed_property_type_allowed",
        "full_row_allowed",
        "raw_response_body_allowed",
        "property_id_allowed",
        "owner_holder_values_allowed",
        "distinct_property_type_codes_allowed",
    ):
        assert output[key] is False


def test_policy_registry_and_downstream_gates_remain_closed() -> None:
    artifact = _load(ARTIFACT_PATH)
    safety = artifact["safety_state"]
    assert isinstance(safety, dict)
    assert safety == {
        "source_policy_status": "PROPOSED",
        "registry_enabled": False,
        "registry_approved_for_use": False,
        "approved_real_sources": 0,
        "semantic_compatibility_resolved": False,
        "production_classification_active": False,
        "downstream_gates_remain_closed": True,
    }

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


def test_schema_rejects_self_authorization_scope_widening_and_privacy_expansion() -> None:
    artifact = _load(ARTIFACT_PATH)
    validator = _validator()

    cases: list[dict[str, object]] = []

    execution_authorized = copy.deepcopy(artifact)
    execution_authorized["authorization_boundary"]["diagnostic_execution_authorized"] = True
    cases.append(execution_authorized)

    approval_granted = copy.deepcopy(artifact)
    approval_granted["required_approvals"]["execution"]["granted"] = True
    cases.append(approval_granted)

    widened_range = copy.deepcopy(artifact)
    widened_range["execution_boundary"]["range_requests_max"] = 2
    cases.append(widened_range)

    retries = copy.deepcopy(artifact)
    retries["execution_boundary"]["retries_max"] = 1
    cases.append(retries)

    redirects = copy.deepcopy(artifact)
    redirects["execution_boundary"]["redirects_allowed"] = True
    cases.append(redirects)

    value_persistence = copy.deepcopy(artifact)
    value_persistence["output_contract"]["property_type_hash_allowed"] = True
    cases.append(value_persistence)

    runtime_remediation = copy.deepcopy(artifact)
    runtime_remediation["classifier_contract"]["runtime_transform_acceptance_allowed"] = True
    cases.append(runtime_remediation)

    for invalid in cases:
        with pytest.raises(ValidationError):
            validator.validate(invalid)


def test_next_gate_is_human_review_only() -> None:
    artifact = _load(ARTIFACT_PATH)
    assert artifact["next_gate"] == (
        "HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW"
    )
    assert artifact["next_gate_after_both_fresh_approvals"] == (
        "ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION"
    )
    assert artifact["next_gate_after_diagnostic_result"] == (
        "HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW"
    )
