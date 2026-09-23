"""NY OSC eighth-attempt transient runtime v1.5.

No network access is performed here.  Attempt 8 preserves the reviewed v1.4
RAW-literal executor and changes only the authorization/freshness handoff: the
fresh-preflight deadline is bound to a runner-confirmed download-start marker,
not to the later post-download processing time.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

from unclaimed_platform.adapters.sources.ny_owner_name_attempt8_freshness import (
    EXPECTED_PREFLIGHT_FRESHNESS_SECONDS,
    validate_authorized_download_started_at,
)
from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NyOwnerNameSchemaDiscoveryResult,
    NyOwnerNameStructuralDiagnosticResult,
)
from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_4 import (
    NyTransientLocalExecutionAuthorizationV1_3,
    NyTransientLocalExecutionReasonV1_4,
    execute_transient_local_file_discovery_v1_4,
)

EXPECTED_ATTEMPT_NUMBER = 8
EXPECTED_PROPOSAL_REF = (
    "sources/proposals/"
    "ny_osc_owner_name_file_eighth_bounded_attempt_authorization.v1.json"
)
EXPECTED_PROPOSAL_CHECKPOINT: Literal[
    "0364207e12e70afe4ccaf80e981791871325110a"
] = "0364207e12e70afe4ccaf80e981791871325110a"
EXPECTED_PROPOSAL_CI_RUN_ID = 35749555291


class NyTransientLocalExecutionAuthorizationV1_4(BaseModel):
    """Attempt-8 real authorization compiled from four machine-bound artifacts."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.4.0"] = "1.4.0"
    mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[8] = 8
    eighth_transient_local_approval_ref: str = Field(min_length=1)
    eighth_transient_pii_approval_ref: str = Field(min_length=1)
    eighth_fresh_preflight_receipt_ref: str = Field(min_length=1)
    eighth_execution_authorization_ref: str = Field(min_length=1)
    authorized_download_started_at_utc: str = Field(min_length=1)
    local_file_approval_granted: Literal[True]
    transient_pii_approval_granted: Literal[True]
    fresh_preflight_exact_match: Literal[True]
    execution_authorization_granted: Literal[True]
    proposal_checkpoint: Literal[
        "0364207e12e70afe4ccaf80e981791871325110a"
    ] = EXPECTED_PROPOSAL_CHECKPOINT
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    expected_local_filename: Literal["FINDERS.zip"] = "FINDERS.zip"
    max_download_bytes: Literal[450000000] = 450000000
    max_uncompressed_bytes: Literal[2000000000] = 2000000000
    max_archive_members: Literal[1] = 1
    delete_local_file_immediately: Literal[True] = True
    durable_raw_persistence_allowed: Literal[False] = False
    repository_persistence_allowed: Literal[False] = False
    cloud_sync_allowed: Literal[False] = False
    owner_field_logging_allowed: Literal[False] = False
    row_specific_human_inspection_allowed: Literal[False] = False
    quote_dialect_mode: Literal["DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"] = (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )
    download_mode: Literal["MANUAL_TO_DEDICATED_OS_TEMP"] = (
        "MANUAL_TO_DEDICATED_OS_TEMP"
    )
    downloads_max: Literal[1] = 1
    retries_max: Literal[0] = 0
    direct_network_client_allowed: Literal[False] = False


class NyTransientLocalExecutionResultV1_5(BaseModel):
    """Attempt-8 result carrying only non-PII execution provenance."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.5.0"] = "1.5.0"
    execution_mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[8] = 8
    proposal_checkpoint: Literal[
        "0364207e12e70afe4ccaf80e981791871325110a"
    ] = EXPECTED_PROPOSAL_CHECKPOINT
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    status: Literal["DISCOVERED", "BLOCKED"]
    reason_code: NyTransientLocalExecutionReasonV1_4
    local_file_deleted: Literal[True]
    logical_deletion_only: Literal[True] = True
    physical_secure_erasure_guaranteed: Literal[False] = False
    archive_byte_count: int = Field(ge=0)
    schema_result: NyOwnerNameSchemaDiscoveryResult | None = None
    structural_diagnostic: NyOwnerNameStructuralDiagnosticResult | None = None
    quote_dialect_diagnostic: None = None
    execution_authorization_ref: str = Field(min_length=1)
    authorized_download_started_at_utc: str = Field(min_length=1)
    freshness_bound_to_download_start: Literal[True] = True
    execution_authorization_consumption_provenance: dict[str, object] = Field(
        default_factory=lambda: {
            "single_use": True,
            "reusable": False,
            "retry_authorized": False,
            "consumed_by_execution": True,
            "status_after_execution": "CONSUMED_SINGLE_USE_NON_REUSABLE",
            "owner_pii_included": False,
        }
    )
    no_raw_path_returned: Literal[True] = True
    no_owner_values_returned: Literal[True] = True

    @model_validator(mode="after")
    def validate_provenance(self) -> Self:
        expected = {
            "single_use": True,
            "reusable": False,
            "retry_authorized": False,
            "consumed_by_execution": True,
            "status_after_execution": "CONSUMED_SINGLE_USE_NON_REUSABLE",
            "owner_pii_included": False,
        }
        if self.execution_authorization_consumption_provenance != expected:
            raise ValueError("execution authorization consumption provenance mismatch")
        expected_status = (
            "DISCOVERED"
            if self.reason_code == "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
            else "BLOCKED"
        )
        if self.status != expected_status:
            raise ValueError("execution status does not match reason code")
        return self


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"unable to read authorization artifact: {path.name}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"authorization artifact must be a JSON object: {path.name}")
    return payload


def _required_string(record: dict[str, Any], key: str, label: str) -> str:
    value = record.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label} {key} is missing")
    return value


def _assert_common_binding(
    record: dict[str, Any],
    *,
    label: str,
    expected_runner_checkpoint: str,
) -> None:
    if record.get("attempt_number") != EXPECTED_ATTEMPT_NUMBER:
        raise ValueError(f"{label} attempt number mismatch")
    if record.get("proposal_ref") != EXPECTED_PROPOSAL_REF:
        raise ValueError(f"{label} proposal ref mismatch")
    if record.get("proposal_checkpoint") != EXPECTED_PROPOSAL_CHECKPOINT:
        raise ValueError(f"{label} proposal checkpoint mismatch")
    if record.get("proposal_ci_run_id") != EXPECTED_PROPOSAL_CI_RUN_ID:
        raise ValueError(f"{label} proposal CI mismatch")
    if record.get("runner_checkpoint") != expected_runner_checkpoint:
        raise ValueError(f"{label} runner checkpoint mismatch")
    if record.get("runner_ci_conclusion") != "SUCCESS":
        raise ValueError(f"{label} runner CI is not successful")


def build_real_execution_authorization_v1_4(
    local_approval_path: Path,
    transient_pii_approval_path: Path,
    fresh_preflight_receipt_path: Path,
    execution_authorization_path: Path,
    *,
    expected_runner_checkpoint: str,
    authorized_download_started_at_utc: str,
    now_utc: datetime | None = None,
) -> NyTransientLocalExecutionAuthorizationV1_4:
    """Compile attempt-8 authorization using download-start freshness semantics."""

    if len(expected_runner_checkpoint) != 40 or any(
        char not in "0123456789abcdef" for char in expected_runner_checkpoint
    ):
        raise ValueError("expected runner checkpoint must be a lowercase 40-char Git SHA")

    local = _load_json(local_approval_path)
    pii = _load_json(transient_pii_approval_path)
    preflight = _load_json(fresh_preflight_receipt_path)
    execution = _load_json(execution_authorization_path)

    for record, label in (
        (local, "transient-local approval"),
        (pii, "transient-PII approval"),
        (preflight, "fresh preflight receipt"),
        (execution, "execution authorization"),
    ):
        _assert_common_binding(
            record,
            label=label,
            expected_runner_checkpoint=expected_runner_checkpoint,
        )

    if local.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("transient-local approval is not granted/not-consumed")
    if pii.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("transient-PII approval is not granted/not-consumed")
    if execution.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("execution authorization is not granted/not-consumed")
    if preflight.get("status") != "EXACT_MATCH":
        raise ValueError("fresh preflight is not an exact match")
    if preflight.get("remote_preflight_performed") is not True:
        raise ValueError("fresh preflight was not performed")
    if preflight.get("freshness_window_seconds") != EXPECTED_PREFLIGHT_FRESHNESS_SECONDS:
        raise ValueError("fresh preflight freshness policy mismatch")
    for key in (
        "download_performed",
        "owner_file_opened",
        "owner_pii_processed",
        "contains_owner_pii",
    ):
        if preflight.get(key) is not False:
            raise ValueError("fresh preflight privacy boundary mismatch")

    validated_start = validate_authorized_download_started_at(
        preflight_performed_at_utc=_required_string(
            preflight, "performed_at_utc", "fresh preflight"
        ),
        authorized_download_started_at_utc=authorized_download_started_at_utc,
        freshness_window_seconds=EXPECTED_PREFLIGHT_FRESHNESS_SECONDS,
        observed_now_utc=(now_utc or datetime.now(UTC)),
    )
    canonical_start = validated_start.isoformat().replace("+00:00", "Z")

    local_ref = _required_string(local, "execution_approval_ref", "transient-local approval")
    pii_ref = _required_string(pii, "execution_approval_ref", "transient-PII approval")
    preflight_ref = _required_string(preflight, "receipt_ref", "fresh preflight receipt")
    execution_ref = _required_string(
        execution, "execution_approval_ref", "execution authorization"
    )
    if len({local_ref, pii_ref, preflight_ref, execution_ref}) != 4:
        raise ValueError("all four eighth-attempt binding refs must be distinct")

    if execution.get("fresh_preflight_receipt_ref") != preflight_ref:
        raise ValueError("execution authorization preflight receipt binding mismatch")
    if execution.get("fresh_preflight_status") != "EXACT_MATCH":
        raise ValueError("execution authorization requires exact-match preflight")
    if execution.get("download_authority") != "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP":
        raise ValueError("execution authorization download authority mismatch")
    if execution.get("execution_authority") != "ONE_BOUND_GATE8_EXECUTION":
        raise ValueError("execution authorization Gate 8 authority mismatch")

    local_scope = local.get("scope")
    if not isinstance(local_scope, dict):
        raise ValueError("transient-local scope is missing")
    required_local = {
        "expected_local_filename": "FINDERS.zip",
        "max_download_bytes": 450000000,
        "dedicated_os_temp_directory_required": True,
        "immediate_logical_deletion_required": True,
        "durable_raw_persistence_allowed": False,
        "repository_persistence_allowed": False,
        "cloud_sync_allowed": False,
        "chat_upload_allowed": False,
    }
    for key, expected in required_local.items():
        if local_scope.get(key) != expected:
            raise ValueError("transient-local scope mismatch")

    bounds = pii.get("execution_bounds")
    if not isinstance(bounds, dict):
        raise ValueError("transient-PII execution bounds are missing")
    required_bounds = {
        "downloads_max": 1,
        "retries_max": 0,
        "max_download_bytes": 450000000,
        "max_uncompressed_bytes": 2000000000,
        "max_archive_members": 1,
        "required_transient_execution_authorization_contract_version": "1.4.0",
        "required_execution_result_contract_version": "1.5.0",
        "required_quote_dialect_mode": "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY",
        "automatic_retry_allowed": False,
    }
    for key, expected in required_bounds.items():
        if bounds.get(key) != expected:
            raise ValueError("transient-PII execution bounds mismatch")

    processing = pii.get("processing_scope")
    if not isinstance(processing, dict):
        raise ValueError("transient-PII processing scope is missing")
    forbidden_true = (
        "owner_rows_persistence_allowed",
        "owner_field_decoding_allowed",
        "owner_field_buffering_allowed",
        "owner_field_logging_allowed",
        "row_specific_human_inspection_allowed",
    )
    if processing.get("transient_owner_pii_in_memory_allowed") is not True:
        raise ValueError("transient-PII processing scope mismatch")
    if any(processing.get(key) is not False for key in forbidden_true):
        raise ValueError("transient-PII processing scope mismatch")

    scope = execution.get("authorization_scope")
    if not isinstance(scope, dict):
        raise ValueError("execution authorization scope is missing")
    required_execution_scope = {
        "manual_download_allowed": True,
        "direct_network_client_allowed": False,
        "downloads_max": 1,
        "gate8_executions_max": 1,
        "retries_max": 0,
        "source_activation": False,
        "production_classification_activation": False,
        "identity_resolution": False,
        "beneficiary_matching": False,
        "outreach": False,
        "fee_agreement": False,
        "representation": False,
        "claim_activity": False,
    }
    for key, expected in required_execution_scope.items():
        if scope.get(key) != expected:
            raise ValueError("execution authorization scope mismatch")

    return NyTransientLocalExecutionAuthorizationV1_4(
        eighth_transient_local_approval_ref=local_ref,
        eighth_transient_pii_approval_ref=pii_ref,
        eighth_fresh_preflight_receipt_ref=preflight_ref,
        eighth_execution_authorization_ref=execution_ref,
        authorized_download_started_at_utc=canonical_start,
        local_file_approval_granted=True,
        transient_pii_approval_granted=True,
        fresh_preflight_exact_match=True,
        execution_authorization_granted=True,
        runner_checkpoint=expected_runner_checkpoint,
    )


def execute_transient_local_file_discovery_v1_5(
    authorization: NyTransientLocalExecutionAuthorizationV1_4,
    archive_path: Path,
) -> NyTransientLocalExecutionResultV1_5:
    """Run one attempt-8 discovery using the reviewed v1.4 data-path executor."""

    compatibility_authorization = NyTransientLocalExecutionAuthorizationV1_3(
        seventh_transient_local_approval_ref=(
            authorization.eighth_transient_local_approval_ref
        ),
        seventh_transient_pii_approval_ref=(
            authorization.eighth_transient_pii_approval_ref
        ),
        seventh_fresh_preflight_receipt_ref=(
            authorization.eighth_fresh_preflight_receipt_ref
        ),
        seventh_execution_authorization_ref=(
            authorization.eighth_execution_authorization_ref
        ),
        local_file_approval_granted=True,
        transient_pii_approval_granted=True,
        fresh_preflight_exact_match=True,
        execution_authorization_granted=True,
        runner_checkpoint=authorization.runner_checkpoint,
    )

    prior = execute_transient_local_file_discovery_v1_4(
        compatibility_authorization,
        archive_path,
    )

    return NyTransientLocalExecutionResultV1_5(
        runner_checkpoint=authorization.runner_checkpoint,
        status=prior.status,
        reason_code=prior.reason_code,
        local_file_deleted=prior.local_file_deleted,
        archive_byte_count=prior.archive_byte_count,
        schema_result=prior.schema_result,
        structural_diagnostic=prior.structural_diagnostic,
        quote_dialect_diagnostic=None,
        execution_authorization_ref=(
            authorization.eighth_execution_authorization_ref
        ),
        authorized_download_started_at_utc=(
            authorization.authorized_download_started_at_utc
        ),
    )
