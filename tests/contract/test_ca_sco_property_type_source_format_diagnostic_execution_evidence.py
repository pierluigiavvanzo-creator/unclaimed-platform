from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_source_format_diagnostic.execution.v1.json"
)
EXECUTION_APPROVAL_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_property_type_source_format_diagnostic_execution_approval.v1.json"
)
PRIVACY_APPROVAL_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_property_type_source_format_diagnostic_"
    "full_row_transient_privacy_approval.v1.json"
)
WORKFLOW_PATH = (
    ROOT
    / ".github/workflows/"
    "ca-sco-property-type-source-format-diagnostic-once.yml"
)
PACKAGE_SHA = "cd76250b9527be91e7e7ac4b3aa658c864cf9172"
RUN_ID = "35090057224"
BRANCH = "m3-ca-sco-property-type-source-format-diagnostic-execution-one-shot"
EXPECTED_CLASS = "INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH"
ALLOWED_FIELDS = {
    "diagnostic_result_status",
    "source_format_diagnostic_class",
    "fail_closed_reason_code",
    "source_identity_verified",
    "head_requests",
    "range_requests",
    "http_requests_total",
    "source_response_body_bytes_read",
    "transient_rows_examined",
    "full_row_crosscheck_rows_examined",
    "safety_flags",
}
EXPECTED_SAFETY_FLAGS = {
    "any_row_field_value_persisted": False,
    "full_archive_downloaded": False,
    "full_row_persisted": False,
    "owner_holder_values_persisted": False,
    "parser_exception_text_persisted": False,
    "property_id_persisted": False,
    "property_type_derivative_persisted": False,
    "property_type_persisted": False,
    "raw_body_persisted": False,
    "remediation_performed": False,
    "row_exact_length_persisted": False,
    "row_hash_persisted": False,
    "source_derived_free_text_persisted": False,
}


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_source_format_evidence_is_bounded_and_non_value_bearing() -> None:
    evidence = _load(EVIDENCE_PATH)
    assert set(evidence) == ALLOWED_FIELDS
    assert evidence["diagnostic_result_status"] == "SOURCE_FORMAT_CLASSIFIED"
    assert evidence["source_format_diagnostic_class"] == EXPECTED_CLASS
    assert evidence["fail_closed_reason_code"] is None
    assert evidence["source_identity_verified"] is True
    assert evidence["head_requests"] == 1
    assert evidence["range_requests"] == 1
    assert evidence["http_requests_total"] == 2
    assert evidence["source_response_body_bytes_read"] == 131072
    assert evidence["transient_rows_examined"] == 1
    assert evidence["full_row_crosscheck_rows_examined"] == 1

    safety = evidence["safety_flags"]
    assert isinstance(safety, dict)
    assert safety == EXPECTED_SAFETY_FLAGS


def test_both_source_format_approvals_are_consumed_and_non_reusable() -> None:
    expected = (
        (
            EXECUTION_APPROVAL_PATH,
            "APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED",
        ),
        (
            PRIVACY_APPROVAL_PATH,
            "APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_"
            "FULL_ROW_TRANSIENT_PRIVACY_BOUNDED",
        ),
    )
    for path, approval_ref in expected:
        approval = _load(path)
        assert approval["approval_ref"] == approval_ref
        assert approval["authorization_artifact_package_sha"] == PACKAGE_SHA
        assert approval["single_use"] is True
        assert approval["reusable"] is False
        assert approval["status"] == "CONSUMED"
        assert approval["execution_run_id"] == RUN_ID
        assert approval["execution_branch"] == BRANCH
        assert isinstance(approval["consumed_at_utc"], str)
        assert approval["consumed_at_utc"]


def test_source_format_one_shot_workflow_is_absent_after_execution() -> None:
    assert not WORKFLOW_PATH.exists()


def test_evidence_contains_no_source_value_or_parser_exception_fields() -> None:
    serialized = EVIDENCE_PATH.read_text(encoding="utf-8")
    forbidden_field_names = (
        '"property_type"',
        '"property_type_bytes"',
        '"property_type_hash"',
        '"property_type_exact_length"',
        '"full_row"',
        '"row_hash"',
        '"row_exact_length"',
        '"property_id"',
        '"owner_holder_values"',
        '"parser_exception_text"',
        '"source_derived_free_text"',
    )
    for field_name in forbidden_field_names:
        assert field_name not in serialized
