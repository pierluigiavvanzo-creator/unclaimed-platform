from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = (
    ROOT
    / "sources/proposals"
    / "ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json"
)
SCHEMA = (
    ROOT
    / "schemas/common"
    / "ny_osc_seventh_attempt_authorization_proposal.schema.json"
)
SIXTH_RESULT = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_execution_result.v1.json"
)
SIXTH_LOCAL_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_local_approval.v1.json"
)
SIXTH_PII_APPROVAL = (
    ROOT
    / "sources/evidence"
    / "ny_osc_owner_name_file_sixth_attempt_transient_pii_approval.v1.json"
)
SYNTH_AUTH_V1_2 = (
    ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_2.schema.json"
)
SYNTH_RESULT_V1_3 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_3.schema.json"
)
SYNTH_RUNTIME_V1_3 = (
    ROOT
    / "src/unclaimed_platform/adapters/sources"
    / "ny_owner_name_transient_local_execution_v1_3.py"
)
GATE6 = ROOT / "scripts/ny_osc_gate6_transient_local.ps1"

FUTURE_REAL_AUTH_V1_3 = (
    ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_3.schema.json"
)
FUTURE_REAL_RESULT_V1_4 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_4.schema.json"
)
FUTURE_REAL_RUNTIME_V1_4 = (
    ROOT
    / "src/unclaimed_platform/adapters/sources"
    / "ny_owner_name_transient_local_execution_v1_4.py"
)
FUTURE_GATE7 = ROOT / "scripts/ny_osc_gate7_transient_local.ps1"

FUTURE_SEVENTH_APPROVAL_SCHEMAS = (
    ROOT / "schemas/common/ny_osc_seventh_attempt_transient_local_approval.schema.json",
    ROOT / "schemas/common/ny_osc_seventh_attempt_transient_pii_approval.schema.json",
    ROOT / "schemas/common/ny_osc_seventh_fresh_listing_preflight_receipt.schema.json",
    ROOT / "schemas/common/ny_osc_seventh_execution_authorization.schema.json",
)


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_seventh_attempt_proposal_validates_and_is_not_authorized() -> None:
    proposal = _load(PROPOSAL)
    Draft202012Validator(_load(SCHEMA)).validate(proposal)

    assert proposal["schema_version"] == "1.1.0"
    assert proposal["artifact_version"] == "1.1.0"
    assert proposal["status"] == "REMEDIATED_PROPOSED_NOT_AUTHORIZED"
    assert proposal["request_scope"] == {
        "repository_only": True,
        "source_network_access_performed": False,
        "remote_preflight_performed": False,
        "download_performed": False,
        "owner_file_opened": False,
        "owner_pii_processed": False,
        "approval_artifacts_created": False,
        "gate7_runner_created": False,
        "real_runtime_created": False,
    }
    assert proposal["next_action"] == (
        "HUMAN_REVIEW_NY_OSC_SEVENTH_ATTEMPT_EXECUTION_AUTH_BINDING_"
        "REMEDIATION_OFFLINE"
    )


def test_seventh_proposal_is_bound_to_reviewed_synthetic_runtime() -> None:
    proposal = _load(PROPOSAL)
    baseline = proposal["canonical_baseline"]
    capability = proposal["verified_synthetic_capability"]

    assert baseline["checkpoint"] == "c03f2af4a0fc97232ac5be0abcfe3dd6ae47340a"
    assert baseline["ci_run_id"] == 35642325234
    assert baseline["ci_conclusion"] == "SUCCESS"
    assert baseline["synthetic_runtime_human_review_result"] == "PASS"

    assert capability["authorization_contract_version"] == "1.2.0"
    assert capability["authorization_mode"] == "SYNTHETIC_TEST"
    assert capability["real_mode_allowed"] is False
    assert capability["result_contract_version"] == "1.3.0"
    assert capability["quote_dialect_mode"] == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert capability["real_authorization_builder_present"] is False
    assert capability["cli_present"] is False
    assert capability["gate7_runner_present"] is False


def test_sixth_evidence_and_consumed_approvals_remain_historical() -> None:
    proposal = _load(PROPOSAL)
    sixth = _load(SIXTH_RESULT)
    local = _load(SIXTH_LOCAL_APPROVAL)
    pii = _load(SIXTH_PII_APPROVAL)

    assert sixth["status"] == "BLOCKED"
    assert sixth["reason_code"] == "QUOTE_DIALECT_AMBIGUOUS"
    assert sixth["schema_discovery_quote_dialect_mode"] == "LINE_LOCAL_ARBITRATION"

    assert local["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
    assert pii["status"] == "CONSUMED_SINGLE_USE_NON_REUSABLE"
    assert local["reusable"] is False
    assert pii["reusable"] is False
    assert local["retry_authorized"] is False
    assert pii["retry_authorized"] is False

    implementation = proposal["implementation_gate"]
    assert implementation["sixth_attempt_runner_reuse_allowed"] is False
    assert implementation["sixth_attempt_approval_reuse_allowed"] is False


def test_current_synthetic_runtime_cannot_be_silently_retargeted() -> None:
    proposal = _load(PROPOSAL)
    synth_auth = _load(SYNTH_AUTH_V1_2)
    synth_result = _load(SYNTH_RESULT_V1_3)
    synth_source = SYNTH_RUNTIME_V1_3.read_text(encoding="utf-8")

    assert synth_auth["properties"]["mode"]["const"] == "SYNTHETIC_TEST"
    assert synth_auth["properties"]["quote_dialect_mode"]["const"] == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert synth_result["properties"]["schema_discovery_quote_dialect_mode"]["const"] == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert "AUTHORIZED_REAL_ONCE" not in synth_source
    assert "def main(" not in synth_source
    assert "build_real_execution_authorization" not in synth_source

    implementation = proposal["implementation_gate"]
    assert implementation["synthetic_v1_2_authorization_retarget_allowed"] is False
    assert implementation["synthetic_v1_3_result_retarget_allowed"] is False
    assert implementation["synthetic_v1_3_runtime_retarget_allowed"] is False


def test_reviewed_proposal_preserves_version_additive_real_package_design() -> None:
    proposal = _load(PROPOSAL)
    package = proposal["proposed_real_runtime_package"]

    assert package["status"] == "REQUIRED_BEFORE_ANY_SEVENTH_APPROVAL_OR_PREFLIGHT"
    assert package["version_additive"] is True
    assert package["historical_synthetic_contracts_must_remain_unchanged"] is True

    assert package["authorization_contract"]["proposed_version"] == "1.3.0"
    assert package["authorization_contract"]["mode"] == "AUTHORIZED_REAL_ONCE"
    assert package["authorization_contract"]["attempt_number"] == 7
    assert package["authorization_contract"]["synthetic_mode_allowed"] is False

    assert package["result_contract"]["proposed_version"] == "1.4.0"
    assert package["result_contract"]["execution_mode"] == "AUTHORIZED_REAL_ONCE"
    assert package["result_contract"]["attempt_number"] == 7
    assert package["runtime"]["proposed_function"] == (
        "execute_transient_local_file_discovery_v1_4"
    )
    assert package["runtime"]["current_v1_3_runtime_retarget_allowed"] is False

    implementation = proposal["implementation_gate"]
    assert implementation["seventh_attempt_real_runtime_status"] == "NOT_CREATED"
    assert implementation["seventh_attempt_runner_status"] == "NOT_CREATED"
    assert implementation["seventh_attempt_approval_contract_status"] == "NOT_CREATED"
    assert implementation["seventh_attempt_approval_artifacts_status"] == "NOT_CREATED"
    assert implementation["final_execution_authorization_contract_status"] == "NOT_CREATED"
    assert implementation["final_execution_authorization_artifact_status"] == "NOT_CREATED"


def test_seventh_execution_bounds_preserve_caps_and_raw_literal_policy() -> None:
    proposal = _load(PROPOSAL)
    bounds = proposal["proposed_execution_bounds"]

    assert bounds == {
        "attempt_number": 7,
        "downloads_max": 1,
        "retries_max": 0,
        "max_download_bytes": 450000000,
        "max_uncompressed_bytes": 2000000000,
        "max_archive_members": 1,
        "text_members_required_exactly": 1,
        "expected_delimiter": "|",
        "expected_documented_field_count": 14,
        "parser_chunk_bytes": 65536,
        "required_transient_execution_authorization_contract_version": "1.3.0",
        "required_execution_result_contract_version": "1.4.0",
        "required_quote_dialect_mode": "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
        "required_structural_diagnostic_contract_version": "1.0.0",
        "quote_dialect_diagnostic_required_null": True,
        "automatic_widening_allowed": False,
        "automatic_retry_allowed": False,
    }


def test_seventh_preflight_is_separate_fresh_and_not_authorized() -> None:
    proposal = _load(PROPOSAL)
    preflight = proposal["fresh_preflight"]

    assert preflight["required_immediately_before_execution"] is True
    assert preflight["performed_for_this_proposal"] is False
    assert preflight["remote_access_authorized_by_this_proposal"] is False
    assert preflight["freshness_window_seconds"] == 900
    assert preflight["required_result"] == "EXACT_MATCH_OR_STOP"
    assert preflight["drift_behavior"] == "STOP_BEFORE_DOWNLOAD_AND_REFRESH_PROPOSAL"
    assert preflight["separate_preflight_authorization_required"] is True


def test_future_human_gates_are_separate_and_ungranted() -> None:
    gates = _load(PROPOSAL)["future_human_gates"]

    assert [item["sequence"] for item in gates] == [1, 2, 3, 4, 5, 6]
    assert gates[0]["gate"] == (
        "HUMAN_REVIEW_NY_OSC_SEVENTH_ATTEMPT_EXECUTION_AUTH_BINDING_"
        "REMEDIATION_OFFLINE"
    )
    assert gates[0]["status"] == "PENDING"
    assert gates[1]["status"] == "NOT_STARTED"

    assert gates[2]["approval_phrase"] == (
        "APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
    )
    assert gates[3]["approval_phrase"] == (
        "APPROVO NY OSC OWNER NAME FILE SEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
    )
    assert gates[4]["approval_phrase"] == (
        "AUTHORIZE_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT"
    )
    assert gates[5]["approval_phrase"] == (
        "AUTHORIZE_NY_OSC_SEVENTH_BOUNDED_EXECUTION_ONCE"
    )

    for item in gates[2:]:
        assert item["status"] == "NOT_GRANTED"


def test_gate6_remains_historical_line_local() -> None:
    gate6 = GATE6.read_text(encoding="utf-8")

    assert 'required_quote_dialect_mode -ne "LINE_LOCAL_ARBITRATION"' in gate6
    assert "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY" not in gate6
    assert "seventh" not in gate6.lower()


def test_proposal_does_not_grant_source_or_execution_authority() -> None:
    no_grant = _load(PROPOSAL)["authorization_does_not_grant"]

    assert all(value is False for value in no_grant.values())



def test_final_execution_authorization_is_machine_bound_and_explicit() -> None:
    proposal = _load(PROPOSAL)
    package = proposal["proposed_real_runtime_package"]
    auth = package["authorization_contract"]
    result = package["result_contract"]
    runtime = package["runtime"]
    gate7 = package["gate7_runner"]

    expected_refs = [
        "seventh_transient_local_approval_ref",
        "seventh_transient_pii_approval_ref",
        "seventh_fresh_preflight_receipt_ref",
        "seventh_execution_authorization_ref",
    ]
    assert auth["required_binding_refs"] == expected_refs
    assert auth["all_bindings_same_attempt_required"] is True
    assert auth["all_bindings_same_proposal_checkpoint_required"] is True
    assert auth["all_bindings_same_runner_checkpoint_required"] is True
    assert auth["all_approvals_granted_not_consumed_at_start_required"] is True
    assert auth["fresh_preflight_status_required"] == "EXACT_MATCH"
    assert auth["fresh_preflight_max_age_seconds"] == 900

    assert runtime["real_authorization_builder_required_inputs"] == expected_refs

    assert gate7["must_verify_explicit_execution_authorization"] is True
    assert gate7["must_verify_explicit_execution_authorization_before_temp_creation"] is True
    assert gate7["must_verify_explicit_execution_authorization_before_download"] is True
    assert gate7["must_verify_all_bound_refs_attempt_7"] is True
    assert gate7["must_verify_all_bound_refs_same_proposal_checkpoint"] is True
    assert gate7["must_verify_all_bound_refs_same_runner_checkpoint"] is True
    assert gate7["download_mode"] == "MANUAL_TO_DEDICATED_OS_TEMP"
    assert gate7["download_authority_source"] == "SEVENTH_EXECUTION_AUTHORIZATION"
    assert gate7["downloads_max"] == 1
    assert gate7["retries_max"] == 0

    assert result["execution_authorization_ref_required"] is True
    assert result["execution_authorization_consumption_provenance_required"] is True
    assert result["execution_authorization_provenance_owner_pii_allowed"] is False


def test_final_execution_gate_grants_one_manual_download_and_one_bound_execution() -> None:
    proposal = _load(PROPOSAL)
    gates = proposal["future_human_gates"]
    local = gates[2]
    pii = gates[3]
    preflight = gates[4]
    execution = gates[5]

    assert local["grants"] == "TRANSIENT_LOCAL_RETENTION_SCOPE_ONLY_NO_DOWNLOAD"
    assert pii["grants"] == "TRANSIENT_PII_PROCESSING_SCOPE_ONLY_NO_DOWNLOAD"
    assert preflight["grants"] == "PREFLIGHT_ONLY_NO_DOWNLOAD_NO_OWNER_FILE_OPEN"

    assert execution["gate"] == "HUMAN_NY_OSC_SEVENTH_EXECUTION_AUTHORIZATION"
    assert execution["status"] == "NOT_GRANTED"
    assert execution["single_use"] is True
    assert execution["reusable"] is False
    assert execution["retry_authorized"] is False
    assert execution["requires_exact_match_fresh_preflight"] is True
    assert execution["download_authority"] == (
        "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP"
    )
    assert execution["execution_authority"] == "ONE_BOUND_GATE7_EXECUTION"
    assert execution["grants"] == (
        "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP_PLUS_ONE_BOUND_"
        "GATE7_EXECUTION_AFTER_EXACT_MATCH_FRESH_PREFLIGHT"
    )


def test_review_remediation_records_original_review_failure_without_granting_authority() -> None:
    proposal = _load(PROPOSAL)
    remediation = proposal["review_remediation"]

    assert remediation["reviewed_gate"] == (
        "HUMAN_REVIEW_NY_OSC_SEVENTH_ATTEMPT_OFFLINE_PROPOSAL"
    )
    assert remediation["reviewed_result"] == "CHANGES_REQUIRED_BEFORE_IMPLEMENTATION"
    assert remediation["findings"] == [
        "FINAL_EXECUTION_AUTHORIZATION_NOT_MACHINE_BOUND_TO_FUTURE_"
        "AUTHORIZATION_AND_GATE7",
        "DOWNLOAD_AUTHORITY_SEMANTICS_AMBIGUOUS",
    ]
    assert proposal["authorization_does_not_grant"]["download"] is False
    assert proposal["authorization_does_not_grant"]["seventh_attempt_execution"] is False
