from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_diagnostic.execution.v1.json"
)
EXECUTION_APPROVAL_PATH = (
    ROOT / "sources/evidence/ca_sco_property_type_diagnostic_execution_approval.v1.json"
)
PRIVACY_APPROVAL_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_property_type_diagnostic_transient_row_privacy_approval.v1.json"
)
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-diagnostic-remediation-once.yml"
)
PACKAGE_SHA = "daeaa7bfb7f7d73a61f011d394cc88393625866c"
ALLOWED_CLASSES = {
    "SURROUNDING_ASCII_WHITESPACE_ONLY",
    "ASCII_CASE_ONLY",
    "SURROUNDING_ASCII_WHITESPACE_AND_CASE",
    "NON_ASCII_OR_CONTROL_CONTENT",
    "ASCII_STRUCTURAL_MISMATCH",
}
ALLOWED_FIELDS = {
    "diagnostic_result_status",
    "diagnostic_class",
    "fail_closed_reason_code",
    "source_identity_verified",
    "head_requests",
    "range_requests",
    "http_requests_total",
    "source_response_body_bytes_read",
    "transient_rows_examined",
    "safety_flags",
}


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_diagnostic_execution_evidence_is_bounded_and_non_value_bearing() -> None:
    evidence = _load(EVIDENCE_PATH)
    assert set(evidence) == ALLOWED_FIELDS
    assert evidence["diagnostic_result_status"] == "DIAGNOSTIC_CLASSIFIED"
    assert evidence["diagnostic_class"] == "ASCII_STRUCTURAL_MISMATCH"
    assert evidence["diagnostic_class"] in ALLOWED_CLASSES
    assert evidence["fail_closed_reason_code"] is None
    assert evidence["source_identity_verified"] is True
    assert evidence["head_requests"] == 1
    assert evidence["range_requests"] == 1
    assert evidence["http_requests_total"] == 2
    assert evidence["source_response_body_bytes_read"] == 131072
    assert evidence["transient_rows_examined"] == 1

    safety = evidence["safety_flags"]
    assert isinstance(safety, dict)
    assert safety == {
        "exact_property_type_persisted": False,
        "full_archive_downloaded": False,
        "full_row_persisted": False,
        "owner_holder_values_persisted": False,
        "property_id_persisted": False,
        "property_type_derivative_persisted": False,
        "raw_body_persisted": False,
        "remediation_performed": False,
    }


def test_both_fresh_approvals_are_consumed_and_non_reusable() -> None:
    expected = (
        (
            EXECUTION_APPROVAL_PATH,
            "APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED",
        ),
        (
            PRIVACY_APPROVAL_PATH,
            "APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED",
        ),
    )
    for path, approval_ref in expected:
        evidence = _load(path)
        assert evidence["approval_ref"] == approval_ref
        assert evidence["authorization_artifact_package_sha"] == PACKAGE_SHA
        assert evidence["single_use"] is True
        assert evidence["reusable"] is False
        assert evidence["status"] == "CONSUMED"
        assert evidence["execution_run_id"] == "35019840276"
        assert evidence["execution_branch"] == (
            "m3-ca-sco-property-type-diagnostic-execution-one-shot"
        )
        assert isinstance(evidence["consumed_at_utc"], str)
        assert evidence["consumed_at_utc"]


def test_one_shot_workflow_is_absent_after_execution() -> None:
    assert not WORKFLOW_PATH.exists()
