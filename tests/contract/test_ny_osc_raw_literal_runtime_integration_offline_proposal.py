from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

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


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_raw_literal_runtime_integration_proposal_validates() -> None:
    proposal = _load(PROPOSAL)
    Draft202012Validator(_load(SCHEMA)).validate(proposal)

    assert proposal["status"] == "PROPOSED_NOT_IMPLEMENTED"
    assert proposal["baseline"]["checkpoint"] == (
        "fc162aa0d938ec7a5560d115631bcc762694e244"
    )
    assert proposal["baseline"]["parser_mode"] == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert proposal["baseline"]["parser_mode_review_result"] == "PASS"


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


def test_future_candidate_is_synthetic_only_and_not_materialized() -> None:
    proposal = _load(PROPOSAL)
    candidate = proposal["proposed_offline_runtime_candidate"]
    auth = candidate["authorization_contract"]
    result = candidate["result_contract"]
    runtime = candidate["runtime_function"]

    assert candidate["phase"] == "SYNTHETIC_ONLY_RUNTIME_INTEGRATION"
    assert auth["proposed_version"] == "1.2.0"
    assert auth["mode"] == "SYNTHETIC_TEST_ONLY"
    assert auth["real_execution_mode_allowed"] is False
    assert auth["quote_dialect_mode"] == "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"

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

    assert FUTURE_AUTH_V1_2.exists() is False
    assert FUTURE_RESULT_V1_3.exists() is False


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


def test_synthetic_matrix_covers_runtime_and_privacy_boundaries() -> None:
    cases = {
        item["case_id"]: item
        for item in _load(PROPOSAL)["synthetic_acceptance_matrix"]
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
    assert cases["OWNER_VALUES_NEVER_RETURNED"]["expected_no_owner_values_returned"] is True
    assert cases["QUOTE_DIAGNOSTIC_CANNOT_APPEAR"][
        "quote_dialect_diagnostic_required_null"
    ] is True
    assert cases["REAL_MODE_REJECTED_IN_OFFLINE_CANDIDATE"][
        "authorized_real_once_allowed"
    ] is False


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

    assert no_grant["runtime_implementation"] is False
    assert no_grant["real_runtime_activation"] is False
    assert no_grant["sixth_retry"] is False
    assert no_grant["seventh_attempt_preparation"] is False
    assert no_grant["seventh_attempt_execution"] is False


def test_future_real_activation_requires_new_human_gates() -> None:
    prerequisites = set(_load(PROPOSAL)["future_real_activation_prerequisites"])

    assert "SEPARATE_SEVENTH_ATTEMPT_PROPOSAL" in prerequisites
    assert "SEPARATE_FRESH_TRANSIENT_LOCAL_APPROVAL" in prerequisites
    assert "SEPARATE_FRESH_TRANSIENT_PII_APPROVAL" in prerequisites
    assert "SEPARATE_FRESH_LISTING_PREFLIGHT_AUTHORIZATION" in prerequisites
    assert "SEPARATE_EXPLICIT_SEVENTH_EXECUTION_AUTHORIZATION" in prerequisites
