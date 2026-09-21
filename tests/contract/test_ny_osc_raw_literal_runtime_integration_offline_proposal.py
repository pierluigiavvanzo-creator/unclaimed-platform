from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_raw_literal_runtime_integration_offline_proposal.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_raw_literal_runtime_integration_offline_proposal.schema.json"
)
AUTH_V1_1 = (
    ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_1.schema.json"
)
RESULT_V1_2 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_2.schema.json"
)
FUTURE_AUTH_V1_2 = (
    ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_2.schema.json"
)
FUTURE_RESULT_V1_3 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_3.schema.json"
)
GATE6 = ROOT / "scripts/ny_osc_gate6_transient_local.ps1"

EXPECTED_FUTURE_PREREQUISITES = [
    "HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_REVIEW_PREREQUISITE_REMEDIATION_OFFLINE_PASS",
    "IMPLEMENT_AND_REVIEW_SYNTHETIC_RAW_LITERAL_RUNTIME_INTEGRATION",
    "SEPARATE_SEVENTH_ATTEMPT_PROPOSAL",
    "SEPARATE_FRESH_TRANSIENT_LOCAL_APPROVAL",
    "SEPARATE_FRESH_TRANSIENT_PII_APPROVAL",
    "SEPARATE_FRESH_LISTING_PREFLIGHT_AUTHORIZATION",
    "SEPARATE_EXPLICIT_SEVENTH_EXECUTION_AUTHORIZATION",
]


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator() -> Draft202012Validator:
    return Draft202012Validator(_load(SCHEMA))


def test_remediated_runtime_integration_proposal_validates() -> None:
    proposal = _load(PROPOSAL)
    _validator().validate(proposal)

    assert proposal["schema_version"] == "1.1.1"
    assert proposal["artifact_version"] == "1.1.1"
    assert proposal["status"] == "REMEDIATED_PROPOSED_NOT_IMPLEMENTED"
    assert proposal["baseline"]["checkpoint"] == (
        "fc162aa0d938ec7a5560d115631bcc762694e244"
    )
    assert proposal["baseline"]["parser_mode"] == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert proposal["baseline"]["parser_mode_review_result"] == "PASS"


def test_review_remediation_uses_existing_synthetic_wire_value() -> None:
    proposal = _load(PROPOSAL)
    remediation = proposal["review_remediation"]
    auth = proposal["proposed_offline_runtime_candidate"]["authorization_contract"]

    assert remediation["reviewed_result"] == "CHANGES_REQUIRED_BEFORE_IMPLEMENTATION"
    assert "AUTHORIZATION_MODE_WIRE_VALUE_AMBIGUOUS" in remediation["findings"]

    assert auth["mode"] == "SYNTHETIC_TEST"
    assert auth["allowed_mode_values"] == ["SYNTHETIC_TEST"]
    assert auth["forbidden_mode_values"] == ["AUTHORIZED_REAL_ONCE"]
    assert auth["real_execution_mode_allowed"] is False
    assert auth["synthetic_only_semantics"] == (
        "ENFORCED_BY_SCHEMA_ENUM_NOT_BY_NEW_WIRE_VALUE"
    )
    assert auth["quote_dialect_mode"] == "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"


def test_review_prerequisite_remediation_replaces_impossible_gate() -> None:
    proposal = _load(PROPOSAL)
    remediation = proposal["review_prerequisite_remediation"]
    prerequisites = proposal["future_real_activation_prerequisites"]

    old_gate = (
        "HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_OFFLINE_PROPOSAL_PASS"
    )
    new_gate = (
        "HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_"
        "REVIEW_PREREQUISITE_REMEDIATION_OFFLINE_PASS"
    )

    assert remediation["reviewed_result"] == "CHANGES_REQUIRED_BEFORE_IMPLEMENTATION"
    assert remediation["previous_impossible_prerequisite"] == old_gate
    assert remediation["replacement_prerequisite"] == new_gate
    assert old_gate not in prerequisites
    assert prerequisites[0] == new_gate
    assert proposal["next_action"] == (
        "HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_"
        "REVIEW_PREREQUISITE_REMEDIATION_OFFLINE"
    )


def test_historical_runtime_contracts_remain_line_local() -> None:
    proposal = _load(PROPOSAL)
    protected = proposal["protected_historical_runtime"]

    auth = _load(AUTH_V1_1)
    result = _load(RESULT_V1_2)
    gate6 = GATE6.read_text(encoding="utf-8")

    assert auth["properties"]["quote_dialect_mode"]["const"] == (
        "LINE_LOCAL_ARBITRATION"
    )
    assert result["properties"]["schema_discovery_quote_dialect_mode"]["const"] == (
        "LINE_LOCAL_ARBITRATION"
    )
    assert "required_quote_dialect_mode" in gate6
    assert "LINE_LOCAL_ARBITRATION" in gate6
    assert "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY" not in gate6

    assert protected["must_remain_behaviorally_unchanged"] is True
    assert protected["sixth_approvals_state"] == (
        "CONSUMED_SINGLE_USE_NON_REUSABLE"
    )
    assert protected["sixth_retry_authorized"] is False


def test_reviewed_proposal_preserves_synthetic_only_design_after_materialization() -> None:
    proposal = _load(PROPOSAL)
    candidate = proposal["proposed_offline_runtime_candidate"]
    auth = candidate["authorization_contract"]
    result = candidate["result_contract"]
    runtime = candidate["runtime_function"]

    assert candidate["phase"] == "SYNTHETIC_ONLY_RUNTIME_INTEGRATION"
    assert auth["proposed_version"] == "1.2.0"
    assert auth["mode"] == "SYNTHETIC_TEST"
    assert auth["real_execution_mode_allowed"] is False

    assert result["proposed_version"] == "1.3.0"
    assert result["schema_discovery_quote_dialect_mode"] == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert result["quote_dialect_diagnostic_field_policy"] == (
        "REQUIRED_NULL_FOR_ENVELOPE_COMPATIBILITY"
    )
    assert result["quote_dialect_diagnostic_contract_used"] is False

    assert runtime["proposed_name"] == (
        "execute_transient_local_file_discovery_v1_3"
    )
    assert runtime["real_authorization_builder_included"] is False
    assert runtime["cli_entrypoint_change_allowed"] is False
    assert runtime["runner_wiring_allowed"] is False

    assert proposal["implementation_boundaries"]["runtime_schema_files_created"] is False
    assert proposal["implementation_boundaries"]["runtime_code_modified"] is False


def test_raw_literal_reason_contract_removes_quote_specific_failures() -> None:
    reasons = _load(PROPOSAL)["proposed_reason_contract"]
    allowed = set(reasons["allowed_reason_codes"])
    forbidden = set(reasons["forbidden_unreachable_reason_codes"])

    assert "QUOTE_DIALECT_AMBIGUOUS" not in allowed
    assert "MALFORMED_QUOTED_RECORD" not in allowed
    assert forbidden == {
        "QUOTE_DIALECT_AMBIGUOUS",
        "MALFORMED_QUOTED_RECORD",
    }
    assert "UNEXPECTED_DATA_FIELD_COUNT" in allowed
    assert "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED" in allowed
    assert reasons["unexpected_field_count_requires_structural_diagnostic"] is True
    assert reasons["quote_dialect_diagnostic_always_null"] is True
    assert reasons["unknown_reason_codes_fail_closed"] is True


def test_synthetic_matrix_is_exact_and_covers_runtime_privacy_boundaries() -> None:
    proposal = _load(PROPOSAL)
    cases = {
        item["case_id"]: item
        for item in proposal["synthetic_acceptance_matrix"]
    }

    assert set(cases) == {
        "RAW_LITERAL_SIXTH_SHAPE_DISCOVERS",
        "RAW_15_QUOTED_PIPE_BLOCKS",
        "RAW_13_BLOCKS",
        "LOCAL_ARCHIVE_CAP_BLOCKS_BEFORE_SCHEMA",
        "TEMP_FILE_ALWAYS_LOGICALLY_DELETED",
        "OWNER_VALUES_NEVER_RETURNED",
        "QUOTE_DIAGNOSTIC_CANNOT_APPEAR",
        "REAL_MODE_REJECTED_IN_OFFLINE_CANDIDATE",
    }
    assert cases["RAW_LITERAL_SIXTH_SHAPE_DISCOVERS"]["expected_status"] == (
        "DISCOVERED"
    )
    assert cases["RAW_15_QUOTED_PIPE_BLOCKS"]["expected_reason"] == (
        "UNEXPECTED_DATA_FIELD_COUNT"
    )
    assert cases["RAW_13_BLOCKS"]["expected_reason"] == (
        "UNEXPECTED_DATA_FIELD_COUNT"
    )
    assert cases["LOCAL_ARCHIVE_CAP_BLOCKS_BEFORE_SCHEMA"][
        "schema_result_required"
    ] is False
    assert cases["TEMP_FILE_ALWAYS_LOGICALLY_DELETED"][
        "expected_local_file_deleted"
    ] is True
    assert cases["OWNER_VALUES_NEVER_RETURNED"][
        "expected_no_owner_values_returned"
    ] is True
    assert cases["QUOTE_DIAGNOSTIC_CANNOT_APPEAR"][
        "quote_dialect_diagnostic_required_null"
    ] is True
    assert cases["REAL_MODE_REJECTED_IN_OFFLINE_CANDIDATE"][
        "authorized_real_once_allowed"
    ] is False


def test_schema_rejects_synthetic_matrix_drift() -> None:
    payload = copy.deepcopy(_load(PROPOSAL))
    payload["synthetic_acceptance_matrix"][0]["unexpected_new_field"] = True

    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_schema_rejects_implementation_boundary_drift() -> None:
    payload = copy.deepcopy(_load(PROPOSAL))
    payload["implementation_boundaries"]["unexpected_new_flag"] = False

    with pytest.raises(ValidationError):
        _validator().validate(payload)


def test_future_real_activation_prerequisites_are_exact() -> None:
    proposal = _load(PROPOSAL)
    assert proposal["future_real_activation_prerequisites"] == (
        EXPECTED_FUTURE_PREREQUISITES
    )

    drifted = copy.deepcopy(proposal)
    drifted["future_real_activation_prerequisites"][0] = "SILENTLY_CHANGED_GATE"

    with pytest.raises(ValidationError):
        _validator().validate(drifted)


def test_proposal_does_not_authorize_runtime_or_seventh_attempt() -> None:
    proposal = _load(PROPOSAL)
    boundary = proposal["implementation_boundaries"]
    no_grant = proposal["authorization_does_not_grant"]

    assert boundary["proposal_only"] is True
    assert boundary["runtime_code_modified"] is False
    assert boundary["runtime_schema_files_created"] is False
    assert boundary["gate6_runner_modified"] is False
    assert boundary["current_v1_1_authorization_modified"] is False
    assert boundary["current_v1_2_result_modified"] is False
    assert boundary["current_v1_2_runtime_modified"] is False
    assert boundary["real_authorization_builder_created"] is False
    assert boundary["seventh_attempt_proposal_created"] is False
    assert boundary["approval_artifacts_created"] is False
    assert boundary["source_network_access"] is False
    assert boundary["download"] is False
    assert boundary["owner_pii_processing"] is False

    assert boundary["proposal_schema_additional_properties_closed"] is True
    assert boundary["synthetic_matrix_schema_closed"] is True
    assert boundary["future_prerequisites_schema_exact"] is True

    assert no_grant["runtime_implementation"] is False
    assert no_grant["real_runtime_activation"] is False
    assert no_grant["sixth_retry"] is False
    assert no_grant["seventh_attempt_preparation"] is False
    assert no_grant["seventh_attempt_execution"] is False
