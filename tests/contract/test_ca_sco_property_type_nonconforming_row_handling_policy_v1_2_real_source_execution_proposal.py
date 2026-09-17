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
    / "schemas/common/"
    "property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus."
    "property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json"
)
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
V1_2_SCHEMA_PATH = (
    ROOT / "schemas/common/property_type_semantic_verification_execution.v1_2.schema.json"
)
POLICY_PATH = ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
REGISTRY_PATH = ROOT / "sources/registry.yaml"
WORKFLOW_PATH = ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
EXPECTED_REGEX = r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_property_type_semantic_verification_v1_2_real_source_proposal",
        RUNNER_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RUNNER = _load_runner()


def test_proposal_validates_and_is_non_authorizing() -> None:
    proposal = _load(PROPOSAL_PATH)
    _validator().validate(proposal)

    assert proposal["proposal_version"] == "1.1.0"
    assert proposal["prepared_on"] == "2026-09-17"
    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    fresh = proposal["fresh_authorization_requirements"]
    preparation = proposal["preparation_state"]
    assert isinstance(fresh, dict)
    assert isinstance(preparation, dict)
    assert fresh["execution_approval_status"] == "REQUIRED_NOT_GRANTED"
    assert fresh["execution_approval_ref"] is None
    assert fresh["transient_row_privacy_approval_status"] == "REQUIRED_NOT_GRANTED"
    assert fresh["transient_row_privacy_approval_ref"] is None
    assert fresh["network_workflow_creation_authorized"] is False
    assert fresh["real_execution_authorized"] is False
    assert fresh["single_use_approval_required"] is True
    assert all(value is False for value in preparation.values())
    assert not WORKFLOW_PATH.exists()


def test_base_is_pinned_to_ci_green_adopted_baseline_checkpoint() -> None:
    proposal = _load(PROPOSAL_PATH)
    base = proposal["base_state"]
    assert isinstance(base, dict)

    assert base["branch"] == "m3-ca-sco-transport-archive-layout-baseline-adoption"
    assert base["head_sha"] == "6188806e58ac87ccde7b8d6d20dcb2bbbec67c28"
    assert base["head_ci_run"] == "35210199280"
    assert base["implementation_review_result"] == (
        "PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED"
    )
    assert base["baseline_adoption_action"] == (
        "IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION"
    )
    assert base["baseline_adoption_audit"] == (
        "docs/audits/"
        "M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION.md"
    )
    assert base["baseline_evidence_review_result"] == (
        "PASS_CANDIDATE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_EVIDENCE_"
        "ACCEPTED_FOR_SEPARATE_ADOPTION_IMPLEMENTATION"
    )
    assert base["baseline_evidence_path"] == (
        "sources/evidence/"
        "ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json"
    )
    assert base["decision_record"] == "D-008"
    assert base["accepted_design_policy"] == "WHOLE_SOURCE_STOP"
    assert base["accepted_implementation_strategy"] == (
        "ADDITIVE_VERSIONED_CONTROL_DISPOSITION"
    )
    assert base["execution_schema_version"] == "1.2.0"

    execution_schema = _load(V1_2_SCHEMA_PATH)
    assert execution_schema["$id"] == (
        "urn:unclaimed-platform:schema:"
        "property-type-semantic-verification-execution:1.2.0"
    )
    assert RUNNER.PROPERTY_TYPE_RE.pattern == EXPECTED_REGEX


def test_proposal_offsets_match_adopted_runner_and_reviewed_evidence() -> None:
    proposal = _load(PROPOSAL_PATH)
    evidence = _load(EVIDENCE_PATH)
    sample = proposal["sample_plan"]
    assert isinstance(sample, dict)

    proposed_offsets = {
        item["name"]: item["local_header_offset"]
        for item in sample["canonical_members"]
    }
    runner_offsets = {
        member.name: member.local_header_offset for member in RUNNER.CANONICAL_MEMBERS
    }
    evidence_offsets = evidence["CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS"]

    assert proposed_offsets == runner_offsets == evidence_offsets
    assert RUNNER.EXPECTED_LENGTH == evidence["OBSERVED_CONTENT_LENGTH"] == 162560390
    assert RUNNER.EXPECTED_ETAG == evidence["OBSERVED_ETAG"] == (
        '"222dd79f04c2a0a8fff166b01c8da746"'
    )


def test_all_prior_approvals_are_consumed_and_fresh_refs_are_required() -> None:
    proposal = _load(PROPOSAL_PATH)
    historical = proposal["historical_authorization_state"]
    fresh = proposal["fresh_authorization_requirements"]
    assert isinstance(historical, dict)
    assert isinstance(fresh, dict)

    assert historical["all_prior_execution_approvals_consumed"] is True
    assert historical["all_prior_privacy_approvals_consumed"] is True
    assert historical["approvals_reusable"] is False
    assert len(historical["consumed_approval_refs"]) == 8
    assert (
        "OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884"
        in historical["consumed_approval_refs"]
    )
    assert (
        "OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB"
        in historical["consumed_approval_refs"]
    )
    assert fresh["execution_approval_ref"] is None
    assert fresh["transient_row_privacy_approval_ref"] is None


def test_sample_transport_and_validation_caps_match_current_runner() -> None:
    proposal = _load(PROPOSAL_PATH)
    sample = proposal["sample_plan"]
    caps = proposal["transport_caps"]
    controls = proposal["row_processing_controls"]
    assert isinstance(sample, dict)
    assert isinstance(caps, dict)
    assert isinstance(controls, dict)

    assert sample["canonical_member_count"] == len(RUNNER.CANONICAL_MEMBERS) == 4
    assert sample["data_rows_max_per_member"] == RUNNER.MAX_ROWS_PER_MEMBER == 4
    assert sample["data_rows_max_total"] == RUNNER.MAX_ROWS_TOTAL == 16
    assert caps["head_requests_max"] == RUNNER.MAX_HEAD_REQUESTS == 1
    assert caps["range_requests_max"] == RUNNER.MAX_RANGE_REQUESTS == 4
    assert caps["http_requests_max_total"] == RUNNER.MAX_HTTP_REQUESTS == 5
    assert caps["range_response_bytes_max_each"] == RUNNER.RANGE_RESPONSE_BYTES
    assert caps["source_response_body_bytes_max_total"] == RUNNER.MAX_TOTAL_RESPONSE_BYTES
    assert (
        caps["uncompressed_transient_bytes_max_each"]
        == RUNNER.MAX_UNCOMPRESSED_BYTES_PER_MEMBER
    )
    assert (
        caps["uncompressed_transient_bytes_max_total"]
        == RUNNER.MAX_UNCOMPRESSED_BYTES_TOTAL
    )
    assert caps["logical_record_bytes_max"] == RUNNER.MAX_LOGICAL_RECORD_BYTES
    assert caps["additional_range_allowed"] is False
    assert caps["full_body_fallback_allowed"] is False
    assert caps["automatic_widening_allowed"] is False
    assert controls["property_type_code_shape_regex"] == EXPECTED_REGEX
    assert controls["trimming_allowed"] is False
    assert controls["uppercasing_allowed"] is False
    assert controls["normalization_allowed"] is False
    assert controls["regex_relaxation_allowed"] is False
    assert controls["parser_change_allowed"] is False
    assert controls["projector_change_allowed"] is False


def test_v1_2_outcome_contract_preserves_d008_and_does_not_precommit_result() -> None:
    proposal = _load(PROPOSAL_PATH)
    outcome = proposal["v1_2_outcome_contract"]
    question = proposal["execution_question"]
    assert isinstance(outcome, dict)
    assert isinstance(question, dict)

    assert outcome["execution_schema_version"] == "1.2.0"
    assert outcome["property_type_format_unexpected_legacy_status"] == "STOPPED_FAIL_CLOSED"
    assert (
        outcome["property_type_format_unexpected_legacy_stop_reason"]
        == "PROPERTY_TYPE_FORMAT_UNEXPECTED"
    )
    assert (
        outcome["property_type_format_unexpected_control_status_code"]
        == "PROPERTY_TYPE_NONCONFORMING_STOPPED"
    )
    assert (
        outcome["property_type_format_unexpected_control_reason_code"]
        == "PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE"
    )
    assert outcome["unrelated_stop_control_disposition"] is None
    assert outcome["non_stopped_control_disposition"] is None
    assert outcome["source_continuation_after_property_type_format_unexpected"] is False
    assert outcome["later_members_requested_after_trigger"] is False
    assert outcome["silent_row_skip_allowed"] is False
    assert outcome["specific_real_source_outcome_required_for_proposal_acceptance"] is False
    assert question["hidden_source_value_inference_allowed"] is False
    assert question["specific_real_source_outcome_precommitted"] is False


def test_privacy_policy_registry_and_downstream_gates_remain_closed() -> None:
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
        "real_row_quarantine_persistence",
        "row_specific_human_inspection",
        "privacy_expansion_required",
        "control_disposition_source_value_bearing_fields_allowed",
    ):
        assert privacy[key] is False
    assert privacy["control_disposition_allowed_persisted_fields"] == [
        "status_code",
        "reason_code",
    ]

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    source = next(
        item
        for item in registry["sources"]
        if item["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False
    assert safety["approved_real_sources"] == 0
    for key, value in safety.items():
        if key not in {"source_policy_status", "approved_real_sources"}:
            assert value is False


def test_schema_rejects_authorization_widening_privacy_widening_or_result_precommit() -> None:
    proposal = _load(PROPOSAL_PATH)
    validator = _validator()
    invalid_cases: list[dict[str, object]] = []

    execution = copy.deepcopy(proposal)
    execution["fresh_authorization_requirements"]["real_execution_authorized"] = True
    invalid_cases.append(execution)

    invented_ref = copy.deepcopy(proposal)
    invented_ref["fresh_authorization_requirements"]["execution_approval_ref"] = (
        "INVENTED_APPROVAL"
    )
    invalid_cases.append(invented_ref)

    cap = copy.deepcopy(proposal)
    cap["transport_caps"]["http_requests_max_total"] = 6
    invalid_cases.append(cap)

    regex = copy.deepcopy(proposal)
    regex["row_processing_controls"]["property_type_code_shape_regex"] = ".*"
    invalid_cases.append(regex)

    continuation = copy.deepcopy(proposal)
    continuation["v1_2_outcome_contract"][
        "source_continuation_after_property_type_format_unexpected"
    ] = True
    invalid_cases.append(continuation)

    privacy = copy.deepcopy(proposal)
    privacy["privacy_controls"]["per_row_property_type_persistence"] = True
    invalid_cases.append(privacy)

    result = copy.deepcopy(proposal)
    result["execution_question"]["specific_real_source_outcome_precommitted"] = True
    invalid_cases.append(result)

    stale_offset = copy.deepcopy(proposal)
    stale_offset["sample_plan"]["canonical_members"][1]["local_header_offset"] = 59747797
    invalid_cases.append(stale_offset)

    for invalid in invalid_cases:
        with pytest.raises(ValidationError):
            validator.validate(invalid)
