from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json"
)
SCHEMA_PATH = (
    ROOT
    / "schemas/common/"
    "property_type_semantic_verification_execution.v1_1.schema.json"
)
AUTH_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_second_semantic_execution_approval.v1.json"
)
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)
EXECUTION_REF = "APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED"
PRIVACY_REF = "APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_second_execution_evidence_validates_against_v1_1() -> None:
    schema = _load(SCHEMA_PATH)
    evidence = _load(EVIDENCE_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(evidence)

    assert evidence["schema_version"] == "1.1.0"
    assert evidence["execution_approval_ref"] == EXECUTION_REF
    assert evidence["privacy_approval_ref"] == PRIVACY_REF


def test_second_execution_stopped_on_decoded_shape_mismatch() -> None:
    evidence = _load(EVIDENCE_PATH)
    assert evidence["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert evidence["stop_reason"] == "PROPERTY_TYPE_FORMAT_UNEXPECTED"
    assert evidence["stop_reason"] != "PROPERTY_TYPE_ENCODING_UNEXPECTED"

    sample = evidence["sample_summary"]
    assert isinstance(sample, dict)
    assert sample["sample_rows_examined"] == 0
    assert sample["distinct_property_type_codes"] == []
    assert sample["distinct_insurance_codes"] == []
    assert all(value == 0 for value in sample["rows_examined_per_member"].values())


def test_second_execution_exact_budget_and_safety_state() -> None:
    evidence = _load(EVIDENCE_PATH)
    requests = evidence["requests_summary"]
    controls = evidence["controls"]
    safety = evidence["safety_state"]
    assert isinstance(requests, dict)
    assert isinstance(controls, dict)
    assert isinstance(safety, dict)

    assert requests == {
        "head_requests": 1,
        "http_requests_total": 2,
        "range_requests": 1,
        "total_body_bytes_read": 131072,
    }
    assert controls["head_requests_max"] == 1
    assert controls["range_requests_max"] == 4
    assert controls["http_requests_max_total"] == 5
    assert controls["total_source_response_body_bytes_max"] == 524288
    assert controls["additional_range_allowed"] is False
    assert controls["full_body_fallback_allowed"] is False
    assert all(value is False for value in safety.values())


def test_second_execution_transport_metadata_matched_expected_target() -> None:
    evidence = _load(EVIDENCE_PATH)
    target = evidence["target"]
    observed = evidence["transport_verification"]
    assert isinstance(target, dict)
    assert isinstance(observed, dict)

    assert observed["head_performed"] is True
    assert observed["head_status"] == 200
    assert observed["content_length"] == target["expected_content_length"]
    assert observed["content_type"] == target["expected_media_type"]
    assert observed["accept_ranges"] == target["expected_accept_ranges"]
    assert observed["etag"] == target["expected_etag"]


def test_second_execution_used_fresh_single_use_authorization_and_workflow_is_absent() -> None:
    authorization = _load(AUTH_PATH)
    assert authorization["single_use"] is True
    assert authorization["execution_approval_ref"] == EXECUTION_REF
    assert authorization["privacy_approval_ref"] == PRIVACY_REF
    assert not WORKFLOW_PATH.exists()
