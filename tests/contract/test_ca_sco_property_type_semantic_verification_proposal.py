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
    ROOT / "schemas/common/property_type_semantic_verification_proposal.schema.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_semantic_verification.v1.json"
)
EXAMPLES_PATH = (
    ROOT
    / "schemas/examples/"
    "ca_sco_500_plus_property_type_semantic_verification.examples.json"
)
EVIDENCE_PATH = (
    ROOT / "sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json"
)
FIELD_PRIVACY_PATH = (
    ROOT / "sources/proposals/ca_sco_segment_500_plus.field_privacy_readiness.v1.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
SOURCE_ID = "ca.sco.unclaimed_property.bulk"


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validator() -> Draft202012Validator:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_proposal_is_valid_non_authorizing_and_not_executed() -> None:
    proposal = load_json(PROPOSAL_PATH)
    validator().validate(proposal)

    assert proposal["proposal_status"] == "PROPOSAL_ONLY_NOT_AUTHORIZED"
    assert proposal["source_approved"] is False
    assert proposal["source_enabled"] is False
    assert proposal["real_acquisition_authorized"] is False
    assert proposal["network_execution_authorized"] is False
    assert proposal["row_access_authorized"] is False
    assert proposal["network_request_performed"] is False
    assert proposal["body_access_performed"] is False
    assert proposal["execution_approval_ref"] is None

    implementation = proposal["implementation_state"]
    assert isinstance(implementation, dict)
    assert implementation["execution_runner_present"] is False
    assert implementation["network_workflow_present"] is False
    assert implementation["proposal_execution_performed"] is False
    assert not RUNNER_PATH.exists()
    assert not WORKFLOW_PATH.exists()


def test_valid_and_invalid_examples_behave_as_declared() -> None:
    examples = load_json(EXAMPLES_PATH)
    validator().validate(examples["proposal.valid"])

    with pytest.raises(ValidationError):
        validator().validate(examples["proposal.invalid_authorizes_row_access"])


def test_semantic_question_is_narrow_and_sample_only() -> None:
    proposal = load_json(PROPOSAL_PATH)
    question = proposal["semantic_question"]
    authority = proposal["authority_reference"]
    assert isinstance(question, dict)
    assert isinstance(authority, dict)

    assert question["field"] == "PROPERTY_TYPE"
    assert (
        question["proof_boundary"]
        == "SAMPLE_ONLY_DOES_NOT_PROVE_FULL_DATASET_DOMAIN_OR_GLOBAL_CODE_FREQUENCY"
    )
    assert question["production_classification_activation_allowed"] is False
    assert authority["official_insurance_codes"] == [
        "IN01",
        "IN02",
        "IN03",
        "IN04",
        "IN05",
        "IN06",
        "IN07",
        "IN08",
        "IN99",
    ]


def test_sampling_and_network_budgets_are_exact_and_bounded() -> None:
    proposal = load_json(PROPOSAL_PATH)
    sample = proposal["sample_plan"]
    caps = proposal["transport_caps"]
    evidence = load_json(EVIDENCE_PATH)
    assert isinstance(sample, dict)
    assert isinstance(caps, dict)

    members = sample["canonical_members"]
    assert isinstance(members, list)
    assert len(members) == 4
    assert sample["data_rows_max_per_member"] == 4
    assert sample["data_rows_max_total"] == 16
    assert sample["representativeness_claimed"] is False

    evidence_members = evidence["archive"]["members"]
    assert [
        {"name": member["name"], "local_header_offset": member["local_header_offset"]}
        for member in evidence_members
    ] == members

    assert caps["head_requests_max"] == 1
    assert caps["range_requests_max"] == 4
    assert caps["http_requests_max_total"] == 5
    assert caps["range_response_bytes_max_each"] == 131_072
    assert caps["total_source_response_body_bytes_max"] == 4 * 131_072
    assert caps["uncompressed_transient_bytes_max_each"] == 262_144
    assert caps["uncompressed_transient_bytes_max_total"] == 4 * 262_144
    assert caps["logical_record_bytes_max"] == 32_768
    assert caps["full_body_request_allowed"] is False
    assert caps["additional_range_on_incomplete_sample_allowed"] is False


def test_transport_identity_is_anchored_to_canonical_evidence() -> None:
    proposal = load_json(PROPOSAL_PATH)
    caps = proposal["transport_caps"]
    evidence = load_json(EVIDENCE_PATH)
    target = evidence["target"]
    assert isinstance(caps, dict)
    assert isinstance(target, dict)

    assert caps["endpoint"] == target["endpoint"]
    assert caps["expected_content_length"] == target["expected_content_length"]
    assert caps["expected_etag"] == target["expected_etag"]
    assert caps["expected_media_type"] == target["expected_media_type"]
    assert caps["expected_accept_ranges"] == target["expected_accept_ranges"]
    assert caps["https_required"] is True
    assert caps["allowed_host"] == "claimit.ca.gov"
    assert caps["redirects_allowed"] is False
    assert caps["if_match_required"] is True


def test_persistence_is_property_type_summary_only() -> None:
    proposal = load_json(PROPOSAL_PATH)
    controls = proposal["row_processing_controls"]
    privacy = proposal["privacy_and_persistence"]
    assert isinstance(controls, dict)
    assert isinstance(privacy, dict)

    assert controls["property_type_column_index_zero_based"] == 1
    assert controls["property_id_use_allowed"] is False
    assert controls["nonallowlisted_field_use_allowed"] is False
    assert controls["nonallowlisted_field_persistence_allowed"] is False
    assert controls["full_row_persistence_allowed"] is False

    assert privacy["property_id_persistence_allowed"] is False
    assert privacy["per_row_property_type_persistence_allowed"] is False
    assert privacy["derived_property_type_summary_persistence_allowed"] is True
    assert privacy["transient_buffer_retention_days"] == 0
    assert (
        privacy["transient_buffer_disposal"]
        == "IMMEDIATE_AFTER_PROJECTION_OR_STOP"
    )
    assert privacy["record_values_in_logs_allowed"] is False
    assert privacy["raw_bytes_in_logs_allowed"] is False
    assert privacy["owner_holder_values_in_logs_allowed"] is False


def test_current_field_privacy_boundary_and_source_authority_remain_closed() -> None:
    proposal = load_json(PROPOSAL_PATH)
    field_privacy = load_json(FIELD_PRIVACY_PATH)
    policy = load_json(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))

    required = field_privacy["field_minimization"]["required_fields"]
    assert required == ["PROPERTY_ID", "PROPERTY_TYPE"]
    assert proposal["semantic_question"]["field"] == "PROPERTY_TYPE"

    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    assert policy["authorized_processing_purposes"] == []
    assert policy["allowed_fields"] == []
    assert policy["allow_pii"] is False

    candidate = next(
        source for source in registry["sources"] if source["source_id"] == SOURCE_ID
    )
    assert candidate["enabled"] is False
    assert candidate["approved_for_use"] is False


def test_schema_blocks_execution_and_cap_widening() -> None:
    proposal = load_json(PROPOSAL_PATH)

    authorized = copy.deepcopy(proposal)
    authorized["network_execution_authorized"] = True
    with pytest.raises(ValidationError):
        validator().validate(authorized)

    rows_widened = copy.deepcopy(proposal)
    rows_widened["sample_plan"]["data_rows_max_total"] = 17
    with pytest.raises(ValidationError):
        validator().validate(rows_widened)

    bytes_widened = copy.deepcopy(proposal)
    bytes_widened["transport_caps"]["total_source_response_body_bytes_max"] += 1
    with pytest.raises(ValidationError):
        validator().validate(bytes_widened)

    persistence_widened = copy.deepcopy(proposal)
    persistence = persistence_widened["privacy_and_persistence"]
    persistence["raw_full_row_persistence_allowed"] = True
    with pytest.raises(ValidationError):
        validator().validate(persistence_widened)
