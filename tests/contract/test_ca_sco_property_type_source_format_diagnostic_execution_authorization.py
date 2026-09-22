from __future__ import annotations

import copy
import csv
import io
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = (
    ROOT
    / "schemas/common/"
    "property_type_source_format_diagnostic_execution_authorization.schema.json"
)
ARTIFACT_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus."
    "property_type_source_format_diagnostic_execution_authorization.v1.json"
)
PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_source_format_diagnostic.v1.json"
)
POLICY_PATH = (
    ROOT / "policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json"
)
REGISTRY_PATH = ROOT / "sources/registry.yaml"
FUTURE_WORKFLOW_PATH = (
    ROOT
    / ".github/workflows/"
    "ca-sco-property-type-source-format-diagnostic-once.yml"
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
EXPECTED_CLASSES = [
    "FULL_ROW_UTF8_DECODE_FAILED",
    "STDLIB_STRICT_CSV_PARSE_FAILED",
    "STDLIB_COLUMN_SHAPE_NOT_CANONICAL",
    "PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER",
    "INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH",
]
REQUIRED_FAIL_REASONS = {
    "APPROVAL_EVIDENCE_INVALID_OR_INCOMPLETE",
    "SOURCE_IDENTITY_DRIFT",
    "TARGET_ASCII_STRUCTURAL_MISMATCH_NOT_REPRODUCED_WITHIN_BOUND",
    "INDEPENDENT_PARSER_RECORD_COUNT_UNEXPECTED",
    "INDEPENDENT_PARSER_FRAMING_INVARIANT_VIOLATION",
    "FULL_ROW_PRIVACY_BOUNDARY_VIOLATION",
    "PERSISTENCE_BOUNDARY_VIOLATION",
    "NETWORK_BOUNDARY_VIOLATION",
}


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _parse_pinned(text: str) -> list[list[str]]:
    stream = io.StringIO(text, newline="")
    return list(
        csv.reader(
            stream,
            delimiter=",",
            quotechar='"',
            doublequote=True,
            escapechar=None,
            skipinitialspace=False,
            strict=True,
        )
    )


def _synthetic_row(*, embedded_value: str = "SYNTHETIC") -> str:
    values = ["SYNTHETIC_VALUE"] * 25
    values[0] = "SYNTHETIC_ID"
    values[1] = "IN03"
    values[2] = embedded_value
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\r\n")
    writer.writerow(values)
    return output.getvalue()


def test_artifact_validates_and_remains_pending_human_authorization() -> None:
    artifact = _load(ARTIFACT_PATH)
    _validator().validate(artifact)

    assert artifact["status"] == "PENDING_HUMAN_AUTHORIZATION"
    assert artifact["gate"] == (
        "HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW"
    )
    assert artifact["review_base_sha"] == (
        "2975eef60d9ece94a68ef2cd6f2a0707ccfa4083"
    )
    assert artifact["proposal_package_sha"] == (
        "d8dc240bd74e271f88b2ef4583f6b79e533918b2"
    )

    authorization = artifact["authorization_boundary"]
    assert isinstance(authorization, dict)
    assert authorization["artifact_preparation_authorized"] is True
    for key, value in authorization.items():
        if key != "artifact_preparation_authorized":
            assert value is False


def test_fresh_approvals_are_distinct_ungranted_and_evidence_absent() -> None:
    artifact = _load(ARTIFACT_PATH)
    approvals = artifact["required_approvals"]
    assert isinstance(approvals, dict)
    execution = approvals["execution"]
    privacy = approvals["full_row_transient_privacy"]
    assert isinstance(execution, dict)
    assert isinstance(privacy, dict)

    assert execution["approval_ref"] == (
        "APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED"
    )
    assert privacy["approval_ref"] == (
        "APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_"
        "FULL_ROW_TRANSIENT_PRIVACY_BOUNDED"
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
    expected_evidence = (
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
    for path, approval_ref in expected_evidence:
        assert path.exists()
        evidence = _load(path)
        assert evidence["approval_ref"] == approval_ref
        assert evidence["authorization_artifact_package_sha"] == (
            "cd76250b9527be91e7e7ac4b3aa658c864cf9172"
        )
        assert evidence["single_use"] is True
        assert evidence["reusable"] is False
        assert evidence["status"] == "CONSUMED"
    assert not FUTURE_WORKFLOW_PATH.exists()


def test_execution_boundary_exactly_matches_reviewed_proposal_bounds() -> None:
    artifact = _load(ARTIFACT_PATH)
    proposal = _load(PROPOSAL_PATH)
    execution = artifact["execution_boundary"]
    proposed = proposal["future_source_scope_if_later_authorized"]
    assert isinstance(execution, dict)
    assert isinstance(proposed, dict)

    for key, value in execution.items():
        assert proposed[key] == value


def test_mandatory_tightenings_are_machine_locked() -> None:
    artifact = _load(ARTIFACT_PATH)
    parser = artifact["independent_parser_contract"]
    classifier = artifact["classification_contract"]
    tightenings = artifact["mandatory_review_tightenings"]
    assert isinstance(parser, dict)
    assert isinstance(classifier, dict)
    assert isinstance(tightenings, dict)

    assert classifier["first_match_wins"] is True
    assert classifier["classification_precedence"] == EXPECTED_CLASSES
    assert classifier["classification_reordering_allowed"] is False
    assert parser["logical_row_input_source"] == (
        "SAME_IN_MEMORY_LOGICAL_RECORD_BYTES_FROM_FIRST_REPRODUCED_"
        "ASCII_STRUCTURAL_MISMATCH"
    )
    assert parser["source_reread_allowed"] is False
    assert parser["additional_range_for_comparator_allowed"] is False
    assert parser["text_stream_construction"] == (
        "IO_STRINGIO_DECODED_ROW_NEWLINE_EMPTY"
    )
    assert parser["text_stream_newline_argument"] == ""
    assert parser["expected_csv_records_exact"] == 1
    assert parser["zero_or_multiple_records_behavior"] == "STOP_FAIL_CLOSED"
    assert set(tightenings) == {"T-1", "T-2", "T-3", "T-4", "T-5"}


def test_pinned_stdlib_framing_handles_quoted_lf_and_crlf_as_one_record() -> None:
    for embedded in ("LINE1\nLINE2", "LINE1\r\nLINE2"):
        records = _parse_pinned(_synthetic_row(embedded_value=embedded))
        assert len(records) == 1
        assert len(records[0]) == 25
        assert records[0][2] == embedded


def test_two_record_input_is_detected_by_exact_record_count_rule() -> None:
    text = _synthetic_row() + _synthetic_row()
    records = _parse_pinned(text)
    assert len(records) == 2
    assert len(records) != 1
    artifact = _load(ARTIFACT_PATH)
    assert "INDEPENDENT_PARSER_RECORD_COUNT_UNEXPECTED" in (
        artifact["fail_closed_reason_codes"]
    )


def test_fail_closed_and_output_contract_are_non_value_bearing() -> None:
    artifact = _load(ARTIFACT_PATH)
    reasons = artifact["fail_closed_reason_codes"]
    assert isinstance(reasons, list)
    assert REQUIRED_FAIL_REASONS.issubset(set(reasons))
    assert len(reasons) == len(set(reasons))

    output = artifact["output_contract"]
    assert isinstance(output, dict)
    assert output["source_format_diagnostic_class_when_stopped_fail_closed"] is None
    assert output["fail_closed_reason_code_when_classified"] is None
    forbidden_true_keys = (
        "source_derived_free_text_allowed",
        "parser_exception_text_allowed",
        "full_row_allowed",
        "any_row_field_value_allowed",
        "property_type_allowed",
        "property_type_bytes_allowed",
        "property_type_hash_allowed",
        "property_type_exact_length_allowed",
        "property_type_fragments_allowed",
        "property_type_codepoints_allowed",
        "transformed_property_type_allowed",
        "property_id_allowed",
        "owner_holder_values_allowed",
        "row_hash_allowed",
        "row_exact_length_allowed",
        "raw_response_body_allowed",
    )
    for key in forbidden_true_keys:
        assert output[key] is False


def test_privacy_boundary_is_one_row_transient_only_and_not_authorized() -> None:
    artifact = _load(ARTIFACT_PATH)
    privacy = artifact["privacy_boundary"]
    assert isinstance(privacy, dict)
    assert privacy["full_row_transient_exposure_is_privacy_expansion"] is True
    assert privacy["full_row_transient_rows_max"] == 1
    assert privacy["full_row_transient_exposure_authorized_by_artifact_preparation"] is False
    assert privacy["same_logical_row_bytes_only"] is True
    assert privacy["discard_after_classification_or_fail_closed"] is True
    assert privacy["persist_full_row"] is False
    assert privacy["persist_any_row_field_value"] is False
    assert privacy["record_source_values_in_logs"] is False
    assert privacy["persist_parser_exception_text"] is False


def test_policy_registry_and_downstream_gates_remain_closed() -> None:
    artifact = _load(ARTIFACT_PATH)
    safety = artifact["safety_state"]
    assert isinstance(safety, dict)
    assert safety["source_policy_status"] == "PROPOSED"
    assert safety["registry_enabled"] is False
    assert safety["registry_approved_for_use"] is False
    assert safety["approved_real_sources"] == 0
    assert safety["production_classification_active"] is False
    assert safety["downstream_gates_remain_closed"] is True

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


def test_schema_rejects_authorization_widening_and_tightening_removal() -> None:
    artifact = _load(ARTIFACT_PATH)
    validator = _validator()
    invalid_cases: list[dict[str, object]] = []

    execution_authorized = copy.deepcopy(artifact)
    execution_authorized["authorization_boundary"][
        "source_format_diagnostic_execution_authorized"
    ] = True
    invalid_cases.append(execution_authorized)

    approval_granted = copy.deepcopy(artifact)
    approval_granted["required_approvals"]["execution"]["granted"] = True
    invalid_cases.append(approval_granted)

    widened_range = copy.deepcopy(artifact)
    widened_range["execution_boundary"]["range_requests_max"] = 2
    invalid_cases.append(widened_range)

    reread = copy.deepcopy(artifact)
    reread["independent_parser_contract"]["source_reread_allowed"] = True
    invalid_cases.append(reread)

    newline_changed = copy.deepcopy(artifact)
    newline_changed["independent_parser_contract"][
        "text_stream_newline_argument"
    ] = None
    invalid_cases.append(newline_changed)

    record_count_changed = copy.deepcopy(artifact)
    record_count_changed["independent_parser_contract"][
        "expected_csv_records_exact"
    ] = 2
    invalid_cases.append(record_count_changed)

    free_text = copy.deepcopy(artifact)
    free_text["output_contract"]["parser_exception_text_allowed"] = True
    invalid_cases.append(free_text)

    reordered = copy.deepcopy(artifact)
    reordered["classification_contract"]["classification_precedence"] = list(
        reversed(EXPECTED_CLASSES)
    )
    invalid_cases.append(reordered)

    for invalid in invalid_cases:
        with pytest.raises(ValidationError):
            validator.validate(invalid)


def test_next_gate_is_human_review_only() -> None:
    artifact = _load(ARTIFACT_PATH)
    assert artifact["next_gate"] == (
        "HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_"
        "EXECUTION_AUTHORIZATION_REVIEW"
    )
    assert artifact["next_gate_after_both_fresh_approvals"] == (
        "ONE_SHOT_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION"
    )
    assert artifact["next_gate_after_diagnostic_result"] == (
        "HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EVIDENCE_REVIEW"
    )
