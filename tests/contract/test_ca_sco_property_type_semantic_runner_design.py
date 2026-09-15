from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[2]
DESIGN_SCHEMA_PATH = (
    ROOT / "schemas/common/property_type_semantic_runner_design.schema.json"
)
DESIGN_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_semantic_runner_design.v1.json"
)
EXECUTION_SCHEMA_PATH = (
    ROOT / "schemas/common/property_type_semantic_verification_execution.schema.json"
)
EXECUTION_EXAMPLES_PATH = (
    ROOT
    / "schemas/examples/"
    "ca_sco_500_plus_property_type_semantic_verification_execution.examples.json"
)
SEMANTIC_PROPOSAL_PATH = (
    ROOT
    / "sources/proposals/"
    "ca_sco_segment_500_plus.property_type_semantic_verification.v1.json"
)
STRUCTURE_EVIDENCE_PATH = (
    ROOT / "sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json"
)
RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"
WORKFLOW_PATH = (
    ROOT / ".github/workflows/ca-sco-property-type-semantic-verification-once.yml"
)

CANONICAL_MEMBERS = [
    "From_500_To_Beyond_1_of_4.csv",
    "From_500_To_Beyond_2_of_4.csv",
    "From_500_To_Beyond_3_of_4.csv",
    "From_500_To_Beyond_4_of_4.csv",
]


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def validator(path: Path) -> Draft202012Validator:
    schema = load_json(path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def test_runner_design_is_valid_and_still_non_implementing() -> None:
    design = load_json(DESIGN_PATH)
    validator(DESIGN_SCHEMA_PATH).validate(design)

    assert design["status"] == "DESIGN_REVIEW_ONLY_NOT_IMPLEMENTATION_AUTHORIZED"
    boundary = design["implementation_boundary"]
    assert isinstance(boundary, dict)
    assert boundary["runner_present"] is False
    assert boundary["network_workflow_present"] is False
    assert boundary["implementation_authorized"] is False
    assert boundary["execution_authorized"] is False
    assert boundary["real_row_access_authorized"] is False
    assert boundary["transient_row_privacy_approved"] is False
    assert not RUNNER_PATH.exists()
    assert not WORKFLOW_PATH.exists()
    assert design["next_gate"] == "HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL"


def test_design_reuses_exact_canonical_caps_and_identity() -> None:
    design = load_json(DESIGN_PATH)
    semantic = load_json(SEMANTIC_PROPOSAL_PATH)
    evidence = load_json(STRUCTURE_EVIDENCE_PATH)

    caps = design["sampling_caps"]
    proposal_caps = semantic["transport_caps"]
    proposal_sample = semantic["sample_plan"]
    assert isinstance(caps, dict)
    assert isinstance(proposal_caps, dict)
    assert isinstance(proposal_sample, dict)

    assert caps["members"] == proposal_sample["canonical_member_count"] == 4
    assert (
        caps["rows_max_per_member"]
        == proposal_sample["data_rows_max_per_member"]
        == 4
    )
    assert caps["rows_max_total"] == proposal_sample["data_rows_max_total"] == 16
    assert caps["head_requests_max"] == proposal_caps["head_requests_max"] == 1
    assert caps["range_requests_max"] == proposal_caps["range_requests_max"] == 4
    assert (
        caps["http_requests_max_total"]
        == proposal_caps["http_requests_max_total"]
        == 5
    )
    assert (
        caps["range_response_bytes_max_each"]
        == proposal_caps["range_response_bytes_max_each"]
        == 131_072
    )
    assert (
        caps["source_response_body_bytes_max_total"]
        == proposal_caps["total_source_response_body_bytes_max"]
        == 524_288
    )
    assert (
        caps["uncompressed_transient_bytes_max_each"]
        == proposal_caps["uncompressed_transient_bytes_max_each"]
        == 262_144
    )
    assert (
        caps["uncompressed_transient_bytes_max_total"]
        == proposal_caps["uncompressed_transient_bytes_max_total"]
        == 1_048_576
    )
    assert caps["logical_record_bytes_max"] == proposal_caps["logical_record_bytes_max"]
    assert caps["additional_range_allowed"] is False
    assert caps["full_body_fallback_allowed"] is False

    assert design["runner_inputs"]["endpoint_fixed"] == evidence["target"]["endpoint"]


def test_design_locks_exact_canonical_header() -> None:
    design = load_json(DESIGN_PATH)
    evidence = load_json(STRUCTURE_EVIDENCE_PATH)

    expected = evidence["csv_header_candidates"][0]["labels"]
    assert design["canonical_header"] == expected
    assert len(expected) == 25
    assert design["projection_controls"]["property_type_column_index_zero_based"] == 1
    assert design["projection_controls"]["property_id_access_allowed"] is False


def test_execution_examples_validate_without_row_values() -> None:
    examples = load_json(EXECUTION_EXAMPLES_PATH)
    validate = validator(EXECUTION_SCHEMA_PATH)

    validate.validate(examples["execution.synthetic_success"])
    validate.validate(examples["execution.synthetic_inconclusive"])
    validate.validate(examples["execution.synthetic_privacy_stop"])

    encoded = json.dumps(examples, sort_keys=True)
    assert "OWNER_NAME" not in encoded
    assert "HOLDER_NAME" not in encoded
    assert "PROPERTY_ID_VALUE" not in encoded


def test_execution_schema_rejects_budget_widening_and_raw_fields() -> None:
    examples = load_json(EXECUTION_EXAMPLES_PATH)
    validate = validator(EXECUTION_SCHEMA_PATH)

    over_budget = copy.deepcopy(examples["execution.synthetic_success"])
    over_budget["requests_summary"]["total_body_bytes_read"] = 524_289
    with pytest.raises(ValidationError):
        validate.validate(over_budget)

    extra_range = copy.deepcopy(examples["execution.synthetic_success"])
    extra_range["requests_summary"]["range_requests"] = 5
    with pytest.raises(ValidationError):
        validate.validate(extra_range)

    raw_row = copy.deepcopy(examples["execution.synthetic_success"])
    raw_row["sample_summary"]["raw_rows"] = [["secret"]]
    with pytest.raises(ValidationError):
        validate.validate(raw_row)

    property_id = copy.deepcopy(examples["execution.synthetic_success"])
    property_id["sample_summary"]["property_ids"] = ["123"]
    with pytest.raises(ValidationError):
        validate.validate(property_id)


def test_success_and_inconclusive_semantics_are_fail_closed() -> None:
    examples = load_json(EXECUTION_EXAMPLES_PATH)
    validate = validator(EXECUTION_SCHEMA_PATH)

    no_insurance = copy.deepcopy(examples["execution.synthetic_success"])
    no_insurance["sample_summary"]["distinct_insurance_codes"] = []
    with pytest.raises(ValidationError):
        validate.validate(no_insurance)

    missing_member = copy.deepcopy(examples["execution.synthetic_success"])
    rows = missing_member["sample_summary"]["rows_examined_per_member"]
    rows[CANONICAL_MEMBERS[-1]] = 0
    with pytest.raises(ValidationError):
        validate.validate(missing_member)

    inconclusive_with_insurance = copy.deepcopy(
        examples["execution.synthetic_inconclusive"]
    )
    inconclusive_with_insurance["sample_summary"]["distinct_insurance_codes"] = ["IN03"]
    with pytest.raises(ValidationError):
        validate.validate(inconclusive_with_insurance)


def test_range_ignore_and_cap_widening_are_stop_only() -> None:
    design = load_json(DESIGN_PATH)
    failure = design["failure_controls"]
    assert isinstance(failure, dict)

    assert failure["server_ignores_range"] == "STOP_WITHOUT_READING_BODY"
    assert failure["sample_requires_extra_range"] == "STOP_NO_CAP_WIDENING"
    assert failure["data_row_required_beyond_cap"] == "STOP_NO_CAP_WIDENING"
