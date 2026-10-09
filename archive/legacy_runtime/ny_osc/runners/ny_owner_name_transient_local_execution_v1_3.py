"""Synthetic-only NY OSC RAW-literal transient execution runtime v1.3.

This module deliberately exposes no CLI and no real-authorization builder. It accepts
only the versioned synthetic authorization v1.2, runs the reviewed
DOCUMENTED_WIDTH_RAW_LITERAL_POLICY schema-discovery mode against an already-created
synthetic local archive, and logically deletes that file in a finally block.

Physical secure erasure is not claimed.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal, Self, cast

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


class NyTransientLocalExecutionAuthorizationV1_2(BaseModel):
    """Synthetic-only authorization for the reviewed RAW-literal parser mode."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.2.0"] = "1.2.0"
    mode: Literal["SYNTHETIC_TEST"] = "SYNTHETIC_TEST"
    attempt_number: int = Field(default=1, ge=1)
    local_file_approval_ref: str = Field(min_length=1)
    gate2_approval_ref: str = Field(min_length=1)
    local_file_approval_granted: Literal[True]
    gate2_approval_granted: Literal[True]
    expected_local_filename: Literal["FINDERS.zip"] = EXPECTED_LOCAL_NAME
    max_download_bytes: int = Field(gt=0)
    max_uncompressed_bytes: int = Field(gt=0)
    max_archive_members: int = Field(gt=0)
    delete_local_file_immediately: Literal[True] = True
    durable_raw_persistence_allowed: Literal[False] = False
    repository_persistence_allowed: Literal[False] = False
    cloud_sync_allowed: Literal[False] = False
    owner_field_logging_allowed: Literal[False] = False
    row_specific_human_inspection_allowed: Literal[False] = False
    quote_dialect_mode: Literal["DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"] = (
        "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"
    )


NyTransientLocalExecutionReasonV1_3 = Literal[
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

_NY_TRANSIENT_LOCAL_EXECUTION_REASONS_V1_3 = frozenset(
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


def _coerce_execution_reason_v1_3(
    reason_code: str,
) -> NyTransientLocalExecutionReasonV1_3:
    if reason_code not in _NY_TRANSIENT_LOCAL_EXECUTION_REASONS_V1_3:
        raise RuntimeError("unsupported NY OSC transient execution v1.3 reason code")
    return cast(NyTransientLocalExecutionReasonV1_3, reason_code)


class NyTransientLocalExecutionResultV1_3(BaseModel):
    """Synthetic RAW-literal receipt with fail-closed reason/diagnostic bindings."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.3.0"] = "1.3.0"
    status: Literal["DISCOVERED", "BLOCKED"]
    reason_code: NyTransientLocalExecutionReasonV1_3
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
            raise ValueError("execution status does not match v1.3 reason code")

        if expects_structural != has_structural:
            raise ValueError(
                "structural diagnostic must be present only for unexpected field count"
            )
        if self.quote_dialect_diagnostic is not None:
            raise ValueError("RAW-literal v1.3 cannot carry quote dialect diagnostic")

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


def execute_transient_local_file_discovery_v1_3(
    authorization: NyTransientLocalExecutionAuthorizationV1_2,
    archive_path: Path,
) -> NyTransientLocalExecutionResultV1_3:
    """Run synthetic-only RAW-literal discovery and delete the local file afterward."""

    if archive_path.name.lower() != authorization.expected_local_filename.lower():
        raise ValueError("local archive filename does not match authorized identity")
    if not _is_authorized_temp_path(archive_path):
        raise ValueError("local archive must be inside the dedicated OS-temp directory")
    if not archive_path.is_file():
        raise ValueError("local archive file is missing")

    archive_byte_count = archive_path.stat().st_size

    try:
        if archive_byte_count > authorization.max_download_bytes:
            return NyTransientLocalExecutionResultV1_3(
                status="BLOCKED",
                reason_code="LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
                local_file_deleted=True,
                archive_byte_count=archive_byte_count,
                schema_result=None,
            )

        with archive_path.open("rb") as stream:
            archive_bytes = stream.read(authorization.max_download_bytes + 1)

        if len(archive_bytes) > authorization.max_download_bytes:
            return NyTransientLocalExecutionResultV1_3(
                status="BLOCKED",
                reason_code="LOCAL_ARCHIVE_READ_EXCEEDS_DOWNLOAD_CAP",
                local_file_deleted=True,
                archive_byte_count=len(archive_bytes),
                schema_result=None,
            )

        schema_auth = NyOwnerNameSchemaDiscoveryAuthorization(
            mode="SYNTHETIC_TEST",
            approval_id=authorization.gate2_approval_ref,
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

        reason_code = _coerce_execution_reason_v1_3(schema_result.reason_code)
        status: Literal["DISCOVERED", "BLOCKED"] = (
            "DISCOVERED" if schema_result.status == "DISCOVERED" else "BLOCKED"
        )
        return NyTransientLocalExecutionResultV1_3(
            status=status,
            reason_code=reason_code,
            local_file_deleted=True,
            archive_byte_count=archive_byte_count,
            schema_result=schema_result,
            structural_diagnostic=(
                structural_diagnostics[0] if structural_diagnostics else None
            ),
            quote_dialect_diagnostic=None,
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
