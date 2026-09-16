from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json"
)
SCHEMA_PATH = (
    ROOT / "schemas/common/property_type_semantic_verification_execution.v1_2.schema.json"
)
AUDIT_PATH = (
    ROOT
    / "docs/audits/"
    "M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_"
    "V1_2_REAL_SOURCE_EXECUTION.md"
)
POLICY_PATH = ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
REGISTRY_PATH = ROOT / "sources/registry.yaml"
WORKFLOW_PATH = ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
TRIGGER_PATH = ROOT / ".github/ca-sco-property-type-semantic-verification-once.trigger.json"
EXECUTION_REF = (
    "OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_"
    "REAL_SOURCE_EXECUTION_BOUNDED_A2139884"
)
PRIVACY_REF = (
    "OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_"
    "TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_v1_2_real_source_evidence_validates_and_is_fail_closed_transport_drift() -> None:
    evidence = _load(EVIDENCE_PATH)
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(evidence)

    assert evidence["schema_version"] == "1.2.0"
    assert evidence["execution_approval_ref"] == EXECUTION_REF
    assert evidence["privacy_approval_ref"] == PRIVACY_REF
    assert evidence["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert evidence["stop_reason"] == "TRANSPORT_METADATA_DRIFT"
    assert evidence["control_disposition"] is None


def test_v1_2_real_source_execution_stopped_before_body_or_row_access() -> None:
    evidence = _load(EVIDENCE_PATH)
    requests = evidence["requests_summary"]
    sample = evidence["sample_summary"]
    transport = evidence["transport_verification"]
    target = evidence["target"]
    assert isinstance(requests, dict)
    assert isinstance(sample, dict)
    assert isinstance(transport, dict)
    assert isinstance(target, dict)

    assert requests == {
        "head_requests": 1,
        "http_requests_total": 1,
        "range_requests": 0,
        "total_body_bytes_read": 0,
    }
    assert sample["sample_rows_examined"] == 0
    assert all(value == 0 for value in sample["rows_examined_per_member"].values())
    assert sample["distinct_property_type_codes"] == []
    assert sample["distinct_insurance_codes"] == []

    assert target["expected_content_length"] == 162416884
    assert target["expected_etag"] == '"b25b315b6cd8007624387c3a00d4b1fe"'
    assert transport["head_performed"] is True
    assert transport["head_status"] == 200
    assert transport["content_length"] == 162560390
    assert transport["etag"] == '"222dd79f04c2a0a8fff166b01c8da746"'
    assert transport["content_type"] == "application/zip"
    assert transport["accept_ranges"] == "bytes"


def test_v1_2_real_source_execution_preserved_privacy_and_downstream_closure() -> None:
    evidence = _load(EVIDENCE_PATH)
    safety = evidence["safety_state"]
    assert isinstance(safety, dict)
    assert all(value is False for value in safety.values())

    policy = _load(POLICY_PATH)
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    assert policy["status"] == "PROPOSED"
    assert policy["real_acquisition_authorized"] is False
    source = next(
        item
        for item in registry["sources"]
        if item["source_id"] == "ca.sco.unclaimed_property.bulk"
    )
    assert source["enabled"] is False
    assert source["approved_for_use"] is False


def test_v1_2_fresh_approvals_are_consumed_and_one_shot_workflow_is_removed() -> None:
    audit = AUDIT_PATH.read_text(encoding="utf-8")
    assert EXECUTION_REF in audit
    assert PRIVACY_REF in audit
    assert "CONSUMED_SINGLE_USE_NON_REUSABLE" in audit
    assert "35123686954" in audit
    assert "TRANSPORT_METADATA_DRIFT" in audit
    assert not WORKFLOW_PATH.exists()
    assert not TRIGGER_PATH.exists()
