"""NY OSC seventh-attempt real-capable transient runtime v1.4.

The module performs no network access and exposes no CLI. It can only build a real
authorization from four separately granted, machine-bound artifacts for attempt 7.
The executor accepts an already-downloaded FINDERS.zip in the dedicated OS temp path,
runs the reviewed RAW-literal schema discovery, and logically deletes the local archive.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal, Self, cast

from pydantic import BaseModel, ConfigDict, Field, model_validator

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NyOwnerNameQuoteDialectDiagnosticResult,
    NyOwnerNameSchemaDiscoveryAuthorization,
    NyOwnerNameSchemaDiscoveryResult,
    NyOwnerNameStructuralDiagnosticResult,
    discover_ny_owner_name_schema,
)
from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution import (
    EXPECTED_LOCAL_NAME,
    _is_authorized_temp_path,
)

EXPECTED_ATTEMPT_NUMBER = 7
EXPECTED_PROPOSAL_REF = (
    "sources/proposals/"
    "ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json"
)
EXPECTED_PROPOSAL_CHECKPOINT: Literal[
    "18c270bd89d7c4e0c37a5bc046a1f09e49dc672e"
] = "18c270bd89d7c4e0c37a5bc046a1f09e49dc672e"
EXPECTED_PROPOSAL_CI_RUN_ID = 35653220457
EXPECTED_PREFLIGHT_FRESHNESS_SECONDS = 900


class NyTransientLocalExecutionAuthorizationV1_3(BaseModel):
    """Attempt-7 real authorization compiled from four separately granted artifacts."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.3.0"] = "1.3.0"
    mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[7] = 7
    seventh_transient_local_approval_ref: str = Field(min_length=1)
    seventh_transient_pii_approval_ref: str = Field(min_length=1)
    seventh_fresh_preflight_receipt_ref: str = Field(min_length=1)
    seventh_execution_authorization_ref: str = Field(min_length=1)
    local_file_approval_granted: Literal[True]
    transient_pii_approval_granted: Literal[True]
    fresh_preflight_exact_match: Literal[True]
    execution_authorization_granted: Literal[True]
    proposal_checkpoint: Literal[
        "18c270bd89d7c4e0c37a5bc046a1f09e49dc672e"
    ] = EXPECTED_PROPOSAL_CHECKPOINT
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    expected_local_filename: Literal["FINDERS.zip"] = EXPECTED_LOCAL_NAME
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


NyTransientLocalExecutionReasonV1_4 = Literal[
    "LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
    "LOCAL_ARCHIVE_READ_EXCEEDS_DOWNLOAD_CAP",
    "ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
    "NOT_A_ZIP_ARCHIVE",
    "ARCHIVE_HAS_NO_FILES",
    "ARCHIVE_MEMBER_COUNT_EXCEEDS_CAP",
    "AMBIGUOUS_TEXT_MEMBER_LAYOUT",
    "UNCOMPRESSED_TEXT_EXCEEDS_CAP",
    "UNEXPECTED_DATA_FIELD_COUNT",
    "PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED",
    "TEXT_MEMBER_EMPTY",
    "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
]

_NY_TRANSIENT_LOCAL_EXECUTION_REASONS_V1_4 = frozenset(
    {
        "LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
        "LOCAL_ARCHIVE_READ_EXCEEDS_DOWNLOAD_CAP",
        "ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
        "NOT_A_ZIP_ARCHIVE",
        "ARCHIVE_HAS_NO_FILES",
        "ARCHIVE_MEMBER_COUNT_EXCEEDS_CAP",
        "AMBIGUOUS_TEXT_MEMBER_LAYOUT",
        "UNCOMPRESSED_TEXT_EXCEEDS_CAP",
        "UNEXPECTED_DATA_FIELD_COUNT",
        "PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED",
        "TEXT_MEMBER_EMPTY",
        "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
    }
)


def _coerce_execution_reason_v1_4(
    reason_code: str,
) -> NyTransientLocalExecutionReasonV1_4:
    if reason_code not in _NY_TRANSIENT_LOCAL_EXECUTION_REASONS_V1_4:
        raise RuntimeError("unsupported NY OSC transient execution v1.4 reason code")
    return cast(NyTransientLocalExecutionReasonV1_4, reason_code)


class NyTransientLocalExecutionResultV1_4(BaseModel):
    """Attempt-7 real execution receipt with non-PII authorization provenance."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.4.0"] = "1.4.0"
    execution_mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[7] = 7
    proposal_checkpoint: Literal[
        "18c270bd89d7c4e0c37a5bc046a1f09e49dc672e"
    ] = EXPECTED_PROPOSAL_CHECKPOINT
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    status: Literal["DISCOVERED", "BLOCKED"]
    reason_code: NyTransientLocalExecutionReasonV1_4
    local_file_deleted: Literal[True]
    logical_deletion_only: Literal[True] = True
    physical_secure_erasure_guaranteed: Literal[False] = False
    archive_byte_count: int = Field(ge=0)
    schema_result: NyOwnerNameSchemaDiscoveryResult | None = None
    schema_discovery_quote_dialect_mode: Literal[
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    ] = "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    structural_diagnostic: NyOwnerNameStructuralDiagnosticResult | None = None
    quote_dialect_diagnostic: None = None
    execution_authorization_ref: str = Field(min_length=1)
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
    def validate_bindings(self) -> Self:
        local_only_reasons = {
            "LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
            "LOCAL_ARCHIVE_READ_EXCEEDS_DOWNLOAD_CAP",
        }
        discovered_reason = "DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED"
        expects_structural = self.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
        has_structural = self.structural_diagnostic is not None

        expected_status = (
            "DISCOVERED" if self.reason_code == discovered_reason else "BLOCKED"
        )
        if self.status != expected_status:
            raise ValueError("execution status does not match v1.4 reason code")

        if expects_structural != has_structural:
            raise ValueError(
                "structural diagnostic must be present only for unexpected field count"
            )
        if self.quote_dialect_diagnostic is not None:
            raise ValueError("RAW-literal v1.4 cannot carry quote dialect diagnostic")

        expected_provenance = {
            "single_use": True,
            "reusable": False,
            "retry_authorized": False,
            "consumed_by_execution": True,
            "status_after_execution": "CONSUMED_SINGLE_USE_NON_REUSABLE",
            "owner_pii_included": False,
        }
        if self.execution_authorization_consumption_provenance != expected_provenance:
            raise ValueError("execution authorization consumption provenance mismatch")

        if self.schema_result is None:
            if self.reason_code not in local_only_reasons:
                raise ValueError(
                    "schema-discovery result is required for discovery-origin reasons"
                )
        else:
            if self.reason_code in local_only_reasons:
                raise ValueError(
                    "local archive cap reasons cannot carry schema-discovery result"
                )
            schema_status = (
                "DISCOVERED"
                if self.schema_result.status == "DISCOVERED"
                else "BLOCKED"
            )
            if self.status != schema_status:
                raise ValueError("execution status must match schema-discovery status")
            if self.reason_code != self.schema_result.reason_code:
                raise ValueError("execution reason must match schema-discovery reason")

        return self


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"unable to read authorization artifact: {path.name}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"authorization artifact must be a JSON object: {path.name}")
    return payload


def _require_string(record: dict[str, Any], key: str, label: str) -> str:
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


def _parse_utc_timestamp(value: object, label: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label} timestamp is missing")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{label} timestamp is invalid") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{label} timestamp must include timezone")
    return parsed.astimezone(UTC)


def build_real_execution_authorization_v1_3(
    local_approval_path: Path,
    transient_pii_approval_path: Path,
    fresh_preflight_receipt_path: Path,
    execution_authorization_path: Path,
    *,
    expected_runner_checkpoint: str,
    now_utc: datetime | None = None,
) -> NyTransientLocalExecutionAuthorizationV1_3:
    """Compile attempt-7 real authorization from four fresh machine-bound artifacts."""

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
    if preflight.get("download_performed") is not False:
        raise ValueError("fresh preflight must not perform download")
    if preflight.get("owner_file_opened") is not False:
        raise ValueError("fresh preflight must not open owner file")
    if preflight.get("owner_pii_processed") is not False:
        raise ValueError("fresh preflight must not process owner PII")
    if preflight.get("contains_owner_pii") is not False:
        raise ValueError("fresh preflight receipt must contain no owner PII")

    performed_at = _parse_utc_timestamp(
        preflight.get("performed_at_utc"),
        "fresh preflight",
    )
    now = (now_utc or datetime.now(UTC)).astimezone(UTC)
    age_seconds = (now - performed_at).total_seconds()
    if age_seconds < 0 or age_seconds > EXPECTED_PREFLIGHT_FRESHNESS_SECONDS:
        raise ValueError("fresh preflight is stale or future-dated")

    local_ref = _require_string(local, "execution_approval_ref", "transient-local approval")
    pii_ref = _require_string(pii, "execution_approval_ref", "transient-PII approval")
    preflight_ref = _require_string(preflight, "receipt_ref", "fresh preflight receipt")
    execution_ref = _require_string(
        execution,
        "execution_approval_ref",
        "execution authorization",
    )
    if len({local_ref, pii_ref, preflight_ref, execution_ref}) != 4:
        raise ValueError("all four seventh binding refs must be distinct")

    if execution.get("fresh_preflight_receipt_ref") != preflight_ref:
        raise ValueError("execution authorization preflight receipt binding mismatch")
    if execution.get("fresh_preflight_status") != "EXACT_MATCH":
        raise ValueError("execution authorization requires exact-match preflight")
    if execution.get("download_authority") != "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP":
        raise ValueError("execution authorization download authority mismatch")
    if execution.get("execution_authority") != "ONE_BOUND_GATE7_EXECUTION":
        raise ValueError("execution authorization Gate 7 authority mismatch")

    local_scope = local.get("scope")
    if not isinstance(local_scope, dict):
        raise ValueError("transient-local scope is missing")
    required_local_scope = {
        "expected_local_filename": "FINDERS.zip",
        "max_download_bytes": 450000000,
        "dedicated_os_temp_directory_required": True,
        "immediate_logical_deletion_required": True,
        "durable_raw_persistence_allowed": False,
        "repository_persistence_allowed": False,
        "cloud_sync_allowed": False,
        "chat_upload_allowed": False,
        "physical_secure_erasure_guaranteed": False,
    }
    if local_scope != required_local_scope:
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
    if bounds != required_bounds:
        raise ValueError("transient-PII execution bounds mismatch")

    processing_scope = pii.get("processing_scope")
    if not isinstance(processing_scope, dict):
        raise ValueError("transient-PII processing scope is missing")
    required_processing_scope = {
        "transient_owner_pii_in_memory_allowed": True,
        "owner_rows_persistence_allowed": False,
        "owner_field_decoding_allowed": False,
        "owner_field_buffering_allowed": False,
        "owner_field_logging_allowed": False,
        "row_specific_human_inspection_allowed": False,
        "derived_non_pii_schema_metadata_persistence_allowed": True,
        "structural_diagnostic_persistence_allowed": True,
        "quote_dialect_diagnostic_persistence_allowed": False,
    }
    if processing_scope != required_processing_scope:
        raise ValueError("transient-PII processing scope mismatch")

    execution_scope = execution.get("authorization_scope")
    required_execution_scope = {
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
    }
    if execution_scope != required_execution_scope:
        raise ValueError("execution authorization scope mismatch")

    return NyTransientLocalExecutionAuthorizationV1_3(
        seventh_transient_local_approval_ref=local_ref,
        seventh_transient_pii_approval_ref=pii_ref,
        seventh_fresh_preflight_receipt_ref=preflight_ref,
        seventh_execution_authorization_ref=execution_ref,
        local_file_approval_granted=True,
        transient_pii_approval_granted=True,
        fresh_preflight_exact_match=True,
        execution_authorization_granted=True,
        runner_checkpoint=expected_runner_checkpoint,
    )


def execute_transient_local_file_discovery_v1_4(
    authorization: NyTransientLocalExecutionAuthorizationV1_3,
    archive_path: Path,
) -> NyTransientLocalExecutionResultV1_4:
    """Run one attempt-7 RAW-literal discovery and delete the local raw file."""

    if archive_path.name.lower() != authorization.expected_local_filename.lower():
        raise ValueError("local archive filename does not match authorized identity")
    if not _is_authorized_temp_path(archive_path):
        raise ValueError("local archive must be inside the dedicated OS-temp directory")
    if not archive_path.is_file():
        raise ValueError("local archive file is missing")

    archive_byte_count = archive_path.stat().st_size

    def result(
        *,
        status: Literal["DISCOVERED", "BLOCKED"],
        reason_code: NyTransientLocalExecutionReasonV1_4,
        observed_archive_byte_count: int,
        schema_result: NyOwnerNameSchemaDiscoveryResult | None,
        structural_diagnostic: NyOwnerNameStructuralDiagnosticResult | None = None,
    ) -> NyTransientLocalExecutionResultV1_4:
        return NyTransientLocalExecutionResultV1_4(
            runner_checkpoint=authorization.runner_checkpoint,
            status=status,
            reason_code=reason_code,
            local_file_deleted=True,
            archive_byte_count=observed_archive_byte_count,
            schema_result=schema_result,
            structural_diagnostic=structural_diagnostic,
            quote_dialect_diagnostic=None,
            execution_authorization_ref=(
                authorization.seventh_execution_authorization_ref
            ),
        )

    try:
        if archive_byte_count > authorization.max_download_bytes:
            return result(
                status="BLOCKED",
                reason_code="LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
                observed_archive_byte_count=archive_byte_count,
                schema_result=None,
            )

        with archive_path.open("rb") as stream:
            archive_bytes = stream.read(authorization.max_download_bytes + 1)

        if len(archive_bytes) > authorization.max_download_bytes:
            return result(
                status="BLOCKED",
                reason_code="LOCAL_ARCHIVE_READ_EXCEEDS_DOWNLOAD_CAP",
                observed_archive_byte_count=len(archive_bytes),
                schema_result=None,
            )

        schema_auth = NyOwnerNameSchemaDiscoveryAuthorization(
            mode="AUTHORIZED_TRANSIENT_MEMORY_ONLY",
            approval_id=authorization.seventh_transient_pii_approval_ref,
            max_download_bytes=authorization.max_download_bytes,
            max_uncompressed_bytes=authorization.max_uncompressed_bytes,
            max_archive_members=authorization.max_archive_members,
            persist_raw_bytes=False,
            persist_owner_rows=False,
            owner_field_logging=False,
            row_specific_human_inspection=False,
        )
        structural_diagnostics: list[NyOwnerNameStructuralDiagnosticResult] = []
        quote_dialect_diagnostics: list[NyOwnerNameQuoteDialectDiagnosticResult] = []

        schema_result = discover_ny_owner_name_schema(
            schema_auth,
            archive_bytes,
            structural_diagnostic_sink=structural_diagnostics.append,
            quote_dialect_mode=authorization.quote_dialect_mode,
            quote_dialect_diagnostic_sink=quote_dialect_diagnostics.append,
        )

        if len(structural_diagnostics) > 1:
            raise RuntimeError("schema discovery emitted multiple structural diagnostics")
        if quote_dialect_diagnostics:
            raise RuntimeError(
                "RAW-literal schema discovery emitted quote dialect diagnostic"
            )

        reason_code = _coerce_execution_reason_v1_4(schema_result.reason_code)
        status: Literal["DISCOVERED", "BLOCKED"] = (
            "DISCOVERED" if schema_result.status == "DISCOVERED" else "BLOCKED"
        )
        return result(
            status=status,
            reason_code=reason_code,
            observed_archive_byte_count=archive_byte_count,
            schema_result=schema_result,
            structural_diagnostic=(
                structural_diagnostics[0] if structural_diagnostics else None
            ),
        )
    finally:
        if archive_path.exists():
            try:
                archive_path.unlink()
            except OSError as exc:
                raise RuntimeError(
                    "transient local raw file deletion failed; stop and secure the device"
                ) from exc
        if archive_path.exists():
            raise RuntimeError(
                "transient local raw file still exists after deletion attempt"
            )
