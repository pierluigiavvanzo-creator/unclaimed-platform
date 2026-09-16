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
    / "schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json"
)
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
REGISTRY_PATH = ROOT / "sources/registry.yaml"
POLICY_PATH = (
    ROOT
    / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)

EXPECTED_MEMBERS = [
    "From_500_To_Beyond_1_of_4.csv",
    "From_500_To_Beyond_2_of_4.csv",
    "From_500_To_Beyond_3_of_4.csv",
    "From_500_To_Beyond_4_of_4.csv",
]
EXPECTED_HISTORICAL_OFFSETS = [0, 59_747_797, 96_862_896, 134_174_190]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_refresh_proposal_is_valid_non_executing_and_pinned_to_reviewed_evidence() -> None:
    proposal = load_json(PROPOSAL_PATH)
    evidence = load_json(EVIDENCE_PATH)
    validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    assert proposal["base_state"] == {
        "branch": "m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-evidence-review",
        "head_sha": "9dbdc3c6f1ef05c577c26c9e3524ba74fdbfda56",
        "head_ci_run": "35125609902",
        "evidence_review_result": "PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED",
        "runtime_contract_version": "1.2.0",
    }
    assert proposal["evidence_basis"]["execution_result"] == {
        "semantic_result_status": evidence["semantic_result_status"],
        "stop_reason": evidence["stop_reason"],
        "control_disposition": evidence["control_disposition"],
    }
    assert proposal["authorization_state"]["network_execution_authorized"] is False
    assert proposal["authorization_state"]["network_request_performed"] is False
    assert proposal["authorization_state"]["workflow_creation_authorized"] is False


def test_observed_drift_is_evidence_only_and_candidate_baseline_remains_unresolved() -> None:
    proposal = load_json(PROPOSAL_PATH)
    baseline = proposal["baseline_state"]
    observed = baseline["observed_drift_evidence"]
    candidate = baseline["candidate_replacement_baseline"]

    assert observed["content_length"] == 162_560_390
    assert observed["etag"] == '"222dd79f04c2a0a8fff166b01c8da746"'
    assert observed["adopted_as_baseline"] is False

    assert candidate["content_length"] is None
    assert candidate["etag"] is None
    assert [entry["name"] for entry in candidate["canonical_member_offsets"]] == EXPECTED_MEMBERS
    assert all(
        entry["local_header_offset"] is None
        for entry in candidate["canonical_member_offsets"]
    )


def test_historical_offsets_are_preserved_only_as_stale_evidence() -> None:
    proposal = load_json(PROPOSAL_PATH)
    members = proposal["baseline_state"]["historical_pinned_members"]

    assert [entry["name"] for entry in members] == EXPECTED_MEMBERS
    assert [entry["local_header_offset"] for entry in members] == EXPECTED_HISTORICAL_OFFSETS
    assert all(
        entry["status"] == "STALE_FOR_FUTURE_EXECUTION_PLANNING_NOT_PROVEN_INVALID"
        for entry in members
    )


def test_strategy_rejects_shortcuts_and_proposes_only_bounded_structural_metadata() -> None:
    proposal = load_json(PROPOSAL_PATH)
    assessment = {
        item["strategy_id"]: item["disposition"]
        for item in proposal["strategy_assessment"]
    }

    assert assessment == {
        "HEAD_ONLY_TRANSPORT_REFRESH": "REJECTED_INSUFFICIENT_ARCHIVE_LAYOUT_PROOF",
        "ARITHMETIC_MEMBER_OFFSET_REBASE": "REJECTED_UNSUPPORTED_INFERENCE",
        "FULL_ARCHIVE_DOWNLOAD_AND_INSPECTION": "REJECTED_SCOPE_TOO_BROAD",
        "BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION": "PROPOSED_FOR_HUMAN_REVIEW",
    }

    design = proposal["proposed_revalidation_design"]
    archive = design["archive_layout_phase"]
    assert design["selected_strategy"] == "BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION"
    assert archive["method"] == "TAIL_EOCD_THEN_BOUNDED_CENTRAL_DIRECTORY_METADATA"
    assert archive["range_requests_max"] == 4
    assert archive["range_response_bytes_max_each"] == 131_072
    assert archive["total_source_response_body_bytes_max"] == 524_288
    assert archive["if_match_required"] is True
    assert archive["central_directory_metadata_only"] is True
    assert archive["decompression_allowed"] is False
    assert archive["csv_parsing_allowed"] is False
    assert archive["row_or_field_inspection_allowed"] is False
    assert archive["full_archive_download_allowed"] is False
    assert archive["automatic_widening_allowed"] is False
    assert archive["arithmetic_offset_rebase_allowed"] is False
    assert archive["canonical_members"] == EXPECTED_MEMBERS


def test_fail_closed_and_adoption_controls_require_review_before_runner_mutation() -> None:
    proposal = load_json(PROPOSAL_PATH)
    design = proposal["proposed_revalidation_design"]
    failure = design["failure_policy"]
    adoption = design["adoption_policy"]
    mutations = proposal["mutation_controls"]

    assert set(failure.values()) <= {"STOP_FAIL_CLOSED", False}
    assert failure["automatic_retry_allowed"] is False
    assert adoption["candidate_baseline_auto_adopted"] is False
    assert adoption["human_evidence_review_required"] is True
    assert adoption["runner_constant_update_allowed_in_revalidation"] is False
    assert adoption["separate_implementation_gate_required"] is True
    assert all(value is False for value in mutations.values())


def test_future_structural_read_requires_fresh_execution_and_privacy_approvals() -> None:
    proposal = load_json(PROPOSAL_PATH)
    auth = proposal["authorization_state"]
    privacy = proposal["privacy_controls"]

    assert auth["fresh_execution_approval_required"] is True
    assert auth["fresh_execution_approval_ref"] is None
    assert auth["fresh_structural_byte_privacy_approval_required"] is True
    assert auth["fresh_structural_byte_privacy_approval_ref"] is None
    assert auth["consumed_approvals_reusable"] is False

    assert privacy["structural_bytes_memory_only"] is True
    assert privacy["retention_days"] == 0
    assert privacy["raw_range_bytes_persisted"] is False
    assert privacy["compressed_payload_parsed_or_decompressed"] is False
    assert privacy["csv_rows_parsed"] is False
    assert privacy["protected_fields_observed"] is False
    assert privacy["noncanonical_member_names_persisted"] is False


def test_schema_rejects_network_authorization_rebaseline_and_scope_widening() -> None:
    valid = load_json(PROPOSAL_PATH)
    validator().validate(valid)

    authorized = copy.deepcopy(valid)
    authorized["authorization_state"]["network_execution_authorized"] = True
    with pytest.raises(ValidationError):
        validator().validate(authorized)

    adopted = copy.deepcopy(valid)
    adopted["baseline_state"]["candidate_replacement_baseline"]["content_length"] = 162_560_390
    with pytest.raises(ValidationError):
        validator().validate(adopted)

    rebased = copy.deepcopy(valid)
    rebased["proposed_revalidation_design"]["archive_layout_phase"]["arithmetic_offset_rebase_allowed"] = True
    with pytest.raises(ValidationError):
        validator().validate(rebased)

    decompression = copy.deepcopy(valid)
    decompression["proposed_revalidation_design"]["archive_layout_phase"]["decompression_allowed"] = True
    with pytest.raises(ValidationError):
        validator().validate(decompression)

    mutation = copy.deepcopy(valid)
    mutation["mutation_controls"]["expected_etag_updated"] = True
    with pytest.raises(ValidationError):
        validator().validate(mutation)


def test_runner_constants_and_source_governance_remain_unchanged() -> None:
    runner = RUNNER_PATH.read_text(encoding="utf-8")
    proposal = load_json(PROPOSAL_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    policy = load_json(POLICY_PATH)

    assert "EXPECTED_LENGTH = 162_416_884" in runner
    assert "EXPECTED_ETAG = '\"b25b315b6cd8007624387c3a00d4b1fe\"'" in runner
    for name, offset in zip(EXPECTED_MEMBERS, EXPECTED_HISTORICAL_OFFSETS, strict=True):
        formatted = f"{offset:,}".replace(",", "_")
        assert name in runner
        assert formatted in runner or str(offset) in runner

    source = next(
        entry
        for entry in registry["sources"]
        if entry["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["beneficiary_matching_authorized"] is False
    assert policy["outreach_authorized"] is False
    assert proposal["safety_state"]["approved_real_sources"] == 0
    assert proposal["safety_state"]["semantic_compatibility_resolved"] is False


def test_next_gate_is_human_proposal_review_only() -> None:
    proposal = load_json(PROPOSAL_PATH)
    assert proposal["next_gate"] == (
        "HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW"
    )
