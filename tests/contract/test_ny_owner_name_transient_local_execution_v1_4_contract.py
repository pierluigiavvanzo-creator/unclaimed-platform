from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]

AUTH_V1_3 = (
    ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_3.schema.json"
)
RESULT_V1_4 = (
    ROOT / "schemas/agents/ny_transient_local_execution_result_v1_4.schema.json"
)
DISCOVERY = ROOT / "schemas/agents/ny_owner_name_schema_discovery_result.schema.json"
STRUCTURAL = (
    ROOT / "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json"
)
LOCAL_APPROVAL = (
    ROOT / "schemas/common/ny_osc_seventh_attempt_transient_local_approval.schema.json"
)
PII_APPROVAL = (
    ROOT / "schemas/common/ny_osc_seventh_attempt_transient_pii_approval.schema.json"
)
PREFLIGHT = (
    ROOT / "schemas/common/ny_osc_seventh_fresh_listing_preflight_receipt.schema.json"
)
EXECUTION_AUTH = (
    ROOT / "schemas/common/ny_osc_seventh_execution_authorization.schema.json"
)

PROPOSAL_REF = (
    "sources/proposals/"
    "ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json"
)
PROPOSAL_CHECKPOINT = "18c270bd89d7c4e0c37a5bc046a1f09e49dc672e"
PROPOSAL_CI = 35653220457
RUNNER = "b" * 40


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _registry() -> Registry:
    registry = Registry()
    for path in (DISCOVERY, STRUCTURAL):
        schema = _load(path)
        registry = registry.with_resource(
            str(schema["$id"]),
            Resource.from_contents(schema),
        )
    return registry


def _common() -> dict[str, object]:
    return {
        "attempt_number": 7,
        "proposal_ref": PROPOSAL_REF,
        "proposal_checkpoint": PROPOSAL_CHECKPOINT,
        "proposal_ci_run_id": PROPOSAL_CI,
        "runner_checkpoint": RUNNER,
        "runner_ci_run_id": 800001,
        "runner_ci_conclusion": "SUCCESS",
    }


def _local_granted() -> dict[str, object]:
    return {
        **_common(),
        "schema_version": "1.0.0",
        "authorization_gate": (
            "HUMAN_NY_OSC_SEVENTH_TRANSIENT_LOCAL_FILE_RETENTION_AUTHORIZATION"
        ),
        "required_owner_authorization": (
            "APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
        ),
        "owner_authorization": (
            "APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
        ),
        "granted_on": "2026-09-21",
        "execution_approval_ref": "local-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "scope": {
            "expected_local_filename": "FINDERS.zip",
            "max_download_bytes": 450000000,
            "dedicated_os_temp_directory_required": True,
            "immediate_logical_deletion_required": True,
            "durable_raw_persistence_allowed": False,
            "repository_persistence_allowed": False,
            "cloud_sync_allowed": False,
            "chat_upload_allowed": False,
            "physical_secure_erasure_guaranteed": False,
        },
        "authorization_does_not_grant": {
            "source_network_access": False,
            "remote_preflight": False,
            "download": False,
            "owner_pii_processing": False,
            "source_activation": False,
            "production_classification_activation": False,
            "identity_resolution": False,
            "beneficiary_matching": False,
            "outreach": False,
            "fee_agreement": False,
            "representation": False,
            "claim_activity": False,
        },
    }


def _pii_granted() -> dict[str, object]:
    return {
        **_common(),
        "schema_version": "1.0.0",
        "authorization_gate": "HUMAN_NY_OSC_SEVENTH_TRANSIENT_PII_AUTHORIZATION",
        "required_owner_authorization": (
            "APPROVO NY OSC OWNER NAME FILE SEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
        ),
        "owner_authorization": (
            "APPROVO NY OSC OWNER NAME FILE SEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
        ),
        "granted_on": "2026-09-21",
        "execution_approval_ref": "pii-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "source_identity": {
            "source_id": "ny.osc.unclaimed_funds.owner_name_file",
            "expected_remote_name": "FINDERS.zip",
            "historical_size_display_for_preflight_only": "390.51 MB",
            "historical_last_modified_display_for_preflight_only": (
                "9/16/2026, 1:33:31 PM"
            ),
            "fresh_preflight_required": True,
        },
        "execution_bounds": {
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
        },
        "processing_scope": {
            "transient_owner_pii_in_memory_allowed": True,
            "owner_rows_persistence_allowed": False,
            "owner_field_decoding_allowed": False,
            "owner_field_buffering_allowed": False,
            "owner_field_logging_allowed": False,
            "row_specific_human_inspection_allowed": False,
            "derived_non_pii_schema_metadata_persistence_allowed": True,
            "structural_diagnostic_persistence_allowed": True,
            "quote_dialect_diagnostic_persistence_allowed": False,
        },
        "authorization_does_not_grant": {
            "source_network_access": False,
            "remote_preflight": False,
            "download": False,
            "source_activation": False,
            "production_classification_activation": False,
            "identity_resolution": False,
            "beneficiary_matching": False,
            "outreach": False,
            "fee_agreement": False,
            "representation": False,
            "claim_activity": False,
        },
    }


def _preflight_exact() -> dict[str, object]:
    listing = {
        "remote_name": "FINDERS.zip",
        "size_display": "390.51 MB",
        "last_modified_display": "9/16/2026, 1:33:31 PM",
    }
    return {
        **_common(),
        "schema_version": "1.0.0",
        "artifact_id": "ny.osc.owner_name_file.seventh_fresh_listing_preflight_receipt",
        "receipt_ref": "preflight-ref",
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "status": "EXACT_MATCH",
        "remote_preflight_performed": True,
        "preflight_authorization_ref": "preflight-auth-ref",
        "performed_at_utc": "2026-09-21T20:00:00Z",
        "freshness_window_seconds": 900,
        "expected_listing": listing,
        "observed_listing": listing,
        "download_performed": False,
        "owner_file_opened": False,
        "owner_pii_processed": False,
        "contains_owner_pii": False,
    }


def _execution_granted() -> dict[str, object]:
    return {
        **_common(),
        "schema_version": "1.0.0",
        "authorization_gate": "HUMAN_NY_OSC_SEVENTH_EXECUTION_AUTHORIZATION",
        "required_owner_authorization": "AUTHORIZE_NY_OSC_SEVENTH_BOUNDED_EXECUTION_ONCE",
        "owner_authorization": "AUTHORIZE_NY_OSC_SEVENTH_BOUNDED_EXECUTION_ONCE",
        "granted_on": "2026-09-21",
        "execution_approval_ref": "execution-ref",
        "status": "GRANTED_NOT_CONSUMED",
        "single_use": True,
        "reusable": False,
        "retry_authorized": False,
        "fresh_preflight_receipt_ref": "preflight-ref",
        "fresh_preflight_status": "EXACT_MATCH",
        "download_authority": "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP",
        "execution_authority": "ONE_BOUND_GATE7_EXECUTION",
        "authorization_scope": {
            "manual_download_allowed": True,
            "direct_network_client_allowed": False,
            "downloads_max": 1,
            "gate7_executions_max": 1,
            "retries_max": 0,
            "source_activation": False,
            "production_classification_activation": False,
            "identity_resolution": False,
            "beneficiary_matching": False,
            "outreach": False,
            "fee_agreement": False,
            "representation": False,
            "claim_activity": False,
        },
    }


def _runtime_auth_payload() -> dict[str, object]:
    return {
        "contract_version": "1.3.0",
        "mode": "AUTHORIZED_REAL_ONCE",
        "attempt_number": 7,
        "seventh_transient_local_approval_ref": "local-ref",
        "seventh_transient_pii_approval_ref": "pii-ref",
        "seventh_fresh_preflight_receipt_ref": "preflight-ref",
        "seventh_execution_authorization_ref": "execution-ref",
        "local_file_approval_granted": True,
        "transient_pii_approval_granted": True,
        "fresh_preflight_exact_match": True,
        "execution_authorization_granted": True,
        "proposal_checkpoint": PROPOSAL_CHECKPOINT,
        "runner_checkpoint": RUNNER,
        "expected_local_filename": "FINDERS.zip",
        "max_download_bytes": 450000000,
        "max_uncompressed_bytes": 2000000000,
        "max_archive_members": 1,
        "delete_local_file_immediately": True,
        "durable_raw_persistence_allowed": False,
        "repository_persistence_allowed": False,
        "cloud_sync_allowed": False,
        "owner_field_logging_allowed": False,
        "row_specific_human_inspection_allowed": False,
        "quote_dialect_mode": "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
        "download_mode": "MANUAL_TO_DEDICATED_OS_TEMP",
        "downloads_max": 1,
        "retries_max": 0,
        "direct_network_client_allowed": False,
    }


def _schema_result() -> dict[str, object]:
    return {
        "contract_version": "1.0.0",
        "status": "DISCOVERED",
        "reason_code": "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
        "source_id": "ny.osc.unclaimed_funds.owner_name_file",
        "gate_id": (
            "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_"
            "TRANSIENT_PII_AUTHORIZATION"
        ),
        "approval_id": "pii-ref",
        "archive_byte_count": 100,
        "archive_member_count": 1,
        "member_names_persisted": False,
        "selected_text_member_present": True,
        "selected_member_uncompressed_bytes": 1000,
        "observed_delimiter": "|",
        "documented_layout_field_count": 14,
        "observed_data_field_count": 14,
        "observed_header_state": "NO_HEADER_OBSERVED",
        "physical_header_names": [],
        "aggregate_complete_record_count": 1,
        "property_type_code_column_index_zero_based": 1,
        "property_type_ascii_record_count": 1,
        "nature_of_property_mapping_state": (
            "DETERMINISTIC_DOCUMENTED_POSITION_REQUIRES_LATER_CODE_VALIDATION"
        ),
        "encoding_state": "NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY",
        "raw_file_persisted": False,
        "owner_rows_persisted": False,
        "owner_field_logging": False,
        "row_specific_human_inspection": False,
        "no_owner_values_returned": True,
    }


def _result_payload() -> dict[str, object]:
    return {
        "contract_version": "1.4.0",
        "execution_mode": "AUTHORIZED_REAL_ONCE",
        "attempt_number": 7,
        "proposal_checkpoint": PROPOSAL_CHECKPOINT,
        "runner_checkpoint": RUNNER,
        "status": "DISCOVERED",
        "reason_code": "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
        "local_file_deleted": True,
        "logical_deletion_only": True,
        "physical_secure_erasure_guaranteed": False,
        "archive_byte_count": 100,
        "schema_result": _schema_result(),
        "schema_discovery_quote_dialect_mode": "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
        "structural_diagnostic": None,
        "quote_dialect_diagnostic": None,
        "execution_authorization_ref": "execution-ref",
        "execution_authorization_consumption_provenance": {
            "single_use": True,
            "reusable": False,
            "retry_authorized": False,
            "consumed_by_execution": True,
            "status_after_execution": "CONSUMED_SINGLE_USE_NON_REUSABLE",
            "owner_pii_included": False,
        },
        "no_raw_path_returned": True,
        "no_owner_values_returned": True,
    }


def test_seventh_approval_contracts_accept_only_bound_single_use_grants() -> None:
    Draft202012Validator(_load(LOCAL_APPROVAL)).validate(_local_granted())
    Draft202012Validator(_load(PII_APPROVAL)).validate(_pii_granted())
    Draft202012Validator(_load(PREFLIGHT)).validate(_preflight_exact())
    Draft202012Validator(_load(EXECUTION_AUTH)).validate(_execution_granted())

    local = _local_granted()
    local["retry_authorized"] = True
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(LOCAL_APPROVAL)).validate(local)

    execution = _execution_granted()
    execution["download_authority"] = "UNBOUNDED_DOWNLOAD"
    with pytest.raises(ValidationError):
        Draft202012Validator(_load(EXECUTION_AUTH)).validate(execution)


def test_real_authorization_v1_3_is_attempt7_real_only() -> None:
    schema = _load(AUTH_V1_3)
    validator = Draft202012Validator(schema)
    payload = _runtime_auth_payload()
    validator.validate(payload)

    synthetic = dict(payload)
    synthetic["mode"] = "SYNTHETIC_TEST"
    with pytest.raises(ValidationError):
        validator.validate(synthetic)

    retry = dict(payload)
    retry["retries_max"] = 1
    with pytest.raises(ValidationError):
        validator.validate(retry)


def test_result_v1_4_requires_execution_authorization_consumption_provenance() -> None:
    schema = _load(RESULT_V1_4)
    validator = Draft202012Validator(schema, registry=_registry())
    payload = _result_payload()
    validator.validate(payload)

    missing = dict(payload)
    missing.pop("execution_authorization_ref")
    with pytest.raises(ValidationError):
        validator.validate(missing)

    bad_provenance = json.loads(json.dumps(payload))
    bad_provenance["execution_authorization_consumption_provenance"][
        "owner_pii_included"
    ] = True
    with pytest.raises(ValidationError):
        validator.validate(bad_provenance)


def test_result_v1_4_rejects_quote_specific_reason_surface() -> None:
    schema = _load(RESULT_V1_4)
    validator = Draft202012Validator(schema, registry=_registry())
    payload = _result_payload()
    payload["status"] = "BLOCKED"
    payload["reason_code"] = "QUOTE_DIALECT_AMBIGUOUS"

    with pytest.raises(ValidationError):
        validator.validate(payload)


def test_seventh_contracts_do_not_change_historical_synthetic_contracts() -> None:
    auth_v1_2 = _load(
        ROOT / "schemas/agents/ny_transient_local_execution_authorization_v1_2.schema.json"
    )
    result_v1_3 = _load(
        ROOT / "schemas/agents/ny_transient_local_execution_result_v1_3.schema.json"
    )

    assert auth_v1_2["properties"]["mode"]["const"] == "SYNTHETIC_TEST"
    assert auth_v1_2["properties"]["quote_dialect_mode"]["const"] == (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    assert result_v1_3["properties"]["contract_version"]["const"] == "1.3.0"
    assert "execution_authorization_ref" not in result_v1_3["properties"]
