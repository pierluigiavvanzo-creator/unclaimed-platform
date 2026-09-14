from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/source_data_scope_inspection_proposal.schema.json"
EXAMPLES_PATH = ROOT / "schemas/examples/ca_sco_data_scope_inspection_proposal.examples.json"
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/ca_sco_unclaimed_property_bulk.data_scope_inspection.v1.json"
)
TRANSPORT_EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json"
)
SOURCE_APPROVAL_PACKAGE_PATH = (
    ROOT
    / "sources/proposals/ca_sco_unclaimed_property_bulk.source_approval_package.v1.json"
)
POLICY_PATH = (
    ROOT
    / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
SOURCE_ID = "ca.sco.unclaimed_property.bulk"


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def proposal_validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_real_proposal_and_valid_example_match_contract() -> None:
    validator = proposal_validator()
    proposal = load_json(PROPOSAL_PATH)
    examples = load_json(EXAMPLES_PATH)

    validator.validate(proposal)
    validator.validate(examples["proposal.valid"])


def test_contract_rejects_execution_authorization_and_data_rows() -> None:
    validator = proposal_validator()
    examples = load_json(EXAMPLES_PATH)
    valid = copy.deepcopy(examples["proposal.valid"])

    with pytest.raises(ValidationError):
        validator.validate(examples["proposal.invalid_authorizes_execution"])

    with pytest.raises(ValidationError):
        validator.validate(examples["proposal.invalid_allows_data_rows"])

    valid["network_execution_authorized"] = True
    with pytest.raises(ValidationError):
        validator.validate(valid)

    valid = copy.deepcopy(examples["proposal.valid"])
    valid["inspection_scope"]["csv_data_rows_allowed"] = 1
    with pytest.raises(ValidationError):
        validator.validate(valid)


def test_proposal_is_machine_enforced_non_authorizing() -> None:
    proposal = load_json(PROPOSAL_PATH)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    assert proposal["source_approved"] is False
    assert proposal["source_enabled"] is False
    assert proposal["real_acquisition_authorized"] is False
    assert proposal["network_execution_authorized"] is False
    assert proposal["network_request_performed"] is False
    assert proposal["body_access_performed"] is False
    assert proposal["body_bytes_read"] == 0

    gate = proposal["execution_gate"]
    assert gate["execution_approval_required"] is True
    assert gate["execution_approval_ref"] is None
    assert gate["execution_authorized"] is False
    assert gate["authorized_scope"] is None
    assert proposal["next_gate"] == "HUMAN_DATA_SCOPE_INSPECTION_EXECUTION"


def test_transport_controls_reuse_canonical_observation() -> None:
    proposal = load_json(PROPOSAL_PATH)
    evidence = load_json(TRANSPORT_EVIDENCE_PATH)

    transport = proposal["transport_controls"]
    observed = evidence["transport"]
    evidence_controls = evidence["controls"]

    assert transport["endpoint"] == observed["final_endpoint"]
    assert transport["allowed_host"] == observed["final_host"]
    assert transport["expected_media_type"] == observed["content_type"]
    assert transport["expected_content_length"] == observed["content_length"]
    assert transport["timeout_seconds"] == evidence_controls["timeout_seconds"]
    assert transport["accept_ranges_required"] == observed["response_headers"]["accept-ranges"]
    assert transport["request_mode"] == "HTTP_RANGE_GET_ONLY"
    assert transport["full_body_request_allowed"] is False


def test_range_budget_is_exact_and_bounded() -> None:
    proposal = load_json(PROPOSAL_PATH)
    budget = proposal["range_budget"]
    transport = proposal["transport_controls"]

    calculated_body_cap = (
        budget["archive_tail_suffix_bytes"]
        + budget["central_directory_max_bytes"]
        + (
            budget["max_csv_candidate_members"]
            * budget["member_probe_max_response_bytes_each"]
        )
    )
    calculated_request_cap = 2 + budget["max_csv_candidate_members"]

    assert calculated_body_cap == budget["max_total_response_body_bytes"]
    assert calculated_request_cap == budget["max_range_requests"]
    assert budget["max_total_response_body_bytes"] < transport["expected_content_length"]
    assert budget["budget_basis"] == "PROJECT_SAFETY_CAPS_NOT_SOURCE_FACTS"


def test_header_only_scope_never_allows_record_values() -> None:
    proposal = load_json(PROPOSAL_PATH)
    scope = proposal["inspection_scope"]
    csv_plan = proposal["csv_header_plan"]
    outputs = proposal["proposed_outputs"]

    assert scope["purpose_id"] == "SOURCE_STRUCTURE_VERIFICATION_ONLY"
    assert scope["csv_data_rows_allowed"] == 0
    assert scope["record_values_allowed"] is False
    assert scope["pii_indicator_basis"] == "HEADER_LABELS_ONLY"
    assert csv_plan["max_logical_records_per_member"] == 1
    assert csv_plan["max_data_rows_parsed"] == 0
    assert csv_plan["raw_member_bytes_persisted"] is False
    assert csv_plan["raw_header_bytes_persisted"] is False
    assert outputs["record_values"] == "PROHIBITED"
    assert outputs["raw_body_bytes"] == "NOT_PERSISTED"


def test_privacy_and_downstream_prohibitions_are_fail_closed() -> None:
    proposal = load_json(PROPOSAL_PATH)
    scope = proposal["inspection_scope"]
    privacy = proposal["privacy_controls"]

    assert privacy["quarantine_required"] is True
    assert privacy["in_memory_body_processing_only"] is True
    assert privacy["temporary_files_allowed"] is False
    assert privacy["least_privilege_required"] is True
    assert privacy["access_logging_required"] is True
    assert privacy["body_bytes_in_logs_allowed"] is False
    assert privacy["record_values_in_logs_allowed"] is False
    assert privacy["export_allowed"] is False
    assert privacy["matching_allowed"] is False
    assert privacy["outreach_allowed"] is False
    assert scope["identity_resolution_allowed"] is False
    assert scope["beneficiary_matching_allowed"] is False
    assert scope["outreach_allowed"] is False
    assert scope["downstream_record_use_allowed"] is False


def test_proposal_respects_existing_approval_package_blockers() -> None:
    proposal = load_json(PROPOSAL_PATH)
    package = load_json(SOURCE_APPROVAL_PACKAGE_PATH)

    processing = package["proposed_processing"]
    assert proposal["inspection_scope"]["purpose_id"] == processing["purpose_id"]
    assert processing["field_scope"]["proposed_allowed_fields"] == []
    assert processing["pii_necessity"]["status"] == "UNDETERMINED_BLOCKING"
    assert processing["pii_necessity"]["allow_pii"] is False
    assert package["readiness_decision"]["status"] == (
        "BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION"
    )


def test_policy_and_registry_remain_disabled_and_unapproved() -> None:
    policy = load_json(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    candidate = next(
        source for source in registry["sources"] if source["source_id"] == SOURCE_ID
    )

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["allow_pii"] is False
    assert candidate["enabled"] is False
    assert candidate["approved_for_use"] is False
    assert sum(bool(source["approved_for_use"]) for source in registry["sources"]) == 0


def test_proposal_task_contains_no_execution_script_or_one_shot_workflow() -> None:
    assert not (ROOT / "scripts/ca_sco_data_scope_inspection.py").exists()
    assert not (
        ROOT / ".github/workflows/ca-sco-data-scope-inspection-once.yml"
    ).exists()
