from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/common/property_type_semantic_verification_execution.schema.json"
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_semantic.execution.v1.json"
)
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_real_bounded_execution_evidence_is_valid_and_fail_closed() -> None:
    schema = _load(SCHEMA_PATH)
    evidence = _load(EVIDENCE_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(evidence)

    assert evidence["execution_approval_ref"] == (
        "OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED"
    )
    assert evidence["privacy_approval_ref"] == (
        "OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED"
    )
    assert evidence["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert evidence["stop_reason"] == "PROPERTY_TYPE_FORMAT_UNEXPECTED"

    requests = evidence["requests_summary"]
    assert isinstance(requests, dict)
    assert requests["head_requests"] == 1
    assert requests["range_requests"] == 1
    assert requests["http_requests_total"] == 2
    assert requests["total_body_bytes_read"] == 131_072

    sample = evidence["sample_summary"]
    assert isinstance(sample, dict)
    assert sample["sample_rows_examined"] == 0
    assert sample["distinct_property_type_codes"] == []
    assert sample["distinct_insurance_codes"] == []
    assert all(value == 0 for value in sample["rows_examined_per_member"].values())

    safety = evidence["safety_state"]
    assert isinstance(safety, dict)
    assert all(value is False for value in safety.values())


def test_one_shot_workflow_is_removed_after_execution() -> None:
    assert not WORKFLOW_PATH.exists()
