"""Single-use transient-local-file bridge for the NY OSC Gate 2 workflow.

The real OSC browser flow writes a ZIP to local storage. This module narrows that
retention expansion to an OS-temp directory, immediately reads the bounded archive
into memory, delegates to the already-verified schema-discovery harness, and then
logically deletes the local raw file in a finally block.

Physical secure erasure is not claimed.
"""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

from unclaimed_platform.adapters.sources.ny_owner_name_schema_discovery import (
    NyOwnerNameSchemaDiscoveryAuthorization,
    NyOwnerNameSchemaDiscoveryResult,
    NyOwnerNameStructuralDiagnosticResult,
    discover_ny_owner_name_schema,
)

LOCAL_APPROVAL_GATE = (
    "HUMAN_NY_OSC_FIRST_DOWNLOAD_TRANSIENT_LOCAL_FILE_RETENTION_AUTHORIZATION"
)
GATE2_ID = "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION"
EXPECTED_LOCAL_NAME = "FINDERS.zip"
TEMP_DIR_PREFIX = "unclaimed-ny-osc-gate2-"


class NyTransientLocalExecutionAuthorization(BaseModel):
    """Execution envelope that requires both local-retention and Gate 2 approvals."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_TEST", "AUTHORIZED_REAL_ONCE"]
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


class NyTransientLocalExecutionResult(BaseModel):
    """Historical v1.0.0 non-PII receipt retained for persisted execution evidence."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    status: Literal["DISCOVERED", "BLOCKED"]
    reason_code: str = Field(min_length=3)
    local_file_deleted: Literal[True]
    logical_deletion_only: Literal[True] = True
    physical_secure_erasure_guaranteed: Literal[False] = False
    archive_byte_count: int = Field(ge=0)
    schema_result: NyOwnerNameSchemaDiscoveryResult | None = None
    no_raw_path_returned: Literal[True] = True
    no_owner_values_returned: Literal[True] = True


class NyTransientLocalExecutionResultV1_1(BaseModel):
    """Current non-PII execution receipt with structural diagnostic telemetry."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.1.0"] = "1.1.0"
    status: Literal["DISCOVERED", "BLOCKED"]
    reason_code: str = Field(min_length=3)
    local_file_deleted: Literal[True]
    logical_deletion_only: Literal[True] = True
    physical_secure_erasure_guaranteed: Literal[False] = False
    archive_byte_count: int = Field(ge=0)
    schema_result: NyOwnerNameSchemaDiscoveryResult | None = None
    structural_diagnostic: NyOwnerNameStructuralDiagnosticResult | None = None
    no_raw_path_returned: Literal[True] = True
    no_owner_values_returned: Literal[True] = True

    @model_validator(mode="after")
    def validate_structural_diagnostic_binding(self) -> Self:
        expects_diagnostic = self.reason_code == "UNEXPECTED_DATA_FIELD_COUNT"
        has_diagnostic = self.structural_diagnostic is not None
        if expects_diagnostic != has_diagnostic:
            raise ValueError(
                "structural diagnostic must be present only for unexpected field count"
            )
        if expects_diagnostic and self.status != "BLOCKED":
            raise ValueError("unexpected field count must remain fail-closed")
        if self.structural_diagnostic is not None:
            if (
                self.schema_result is None
                or self.schema_result.reason_code != "UNEXPECTED_DATA_FIELD_COUNT"
            ):
                raise ValueError(
                    "structural diagnostic requires matching schema-discovery result"
                )
        return self


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("approval artifact must be a JSON object")
    return payload


def build_real_execution_authorization(
    local_approval_path: Path,
    gate2_approval_path: Path,
    *,
    expected_attempt_number: int | None = None,
) -> NyTransientLocalExecutionAuthorization:
    """Build the runtime envelope only when both single-use approvals are granted."""

    local = _load_json(local_approval_path)
    gate2 = _load_json(gate2_approval_path)

    if local.get("authorization_gate") != LOCAL_APPROVAL_GATE:
        raise ValueError("transient-local-file approval gate mismatch")
    if local.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("transient-local-file approval is not available")
    if local.get("single_use") is not True or local.get("reusable") is not False:
        raise ValueError("transient-local-file approval reuse policy mismatch")

    if gate2.get("authorization_gate") != GATE2_ID:
        raise ValueError("Gate 2 approval gate mismatch")
    if gate2.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("Gate 2 approval is not available")
    if gate2.get("single_use") is not True or gate2.get("reusable") is not False:
        raise ValueError("Gate 2 approval reuse policy mismatch")

    local_attempt = local.get("attempt_number")
    gate2_attempt = gate2.get("attempt_number")
    if not isinstance(local_attempt, int) or not isinstance(gate2_attempt, int):
        raise ValueError("approval attempt number is missing")
    if local_attempt != gate2_attempt:
        raise ValueError("approval attempt numbers do not match")
    if (
        expected_attempt_number is not None
        and gate2_attempt != expected_attempt_number
    ):
        raise ValueError("approval attempt number does not match the requested attempt")
    if local.get("retry_authorized") is not False:
        raise ValueError("transient-local-file retry policy mismatch")
    if gate2.get("retry_authorized") is not False:
        raise ValueError("Gate 2 retry policy mismatch")

    local_ref = local.get("execution_approval_ref")
    gate2_ref = gate2.get("execution_approval_ref")
    if not isinstance(local_ref, str) or not local_ref:
        raise ValueError("transient-local-file execution approval ref is missing")
    if not isinstance(gate2_ref, str) or not gate2_ref:
        raise ValueError("Gate 2 execution approval ref is missing")
    if local_ref == gate2_ref:
        raise ValueError("local and Gate 2 approvals must have distinct refs")

    bounds = gate2.get("execution_bounds")
    if not isinstance(bounds, dict):
        raise ValueError("Gate 2 execution bounds are missing")
    if bounds.get("downloads_max") != 1 or bounds.get("retries_max") != 0:
        raise ValueError("Gate 2 single-download zero-retry bounds mismatch")

    local_scope = local.get("scope")
    if not isinstance(local_scope, dict):
        raise ValueError("transient-local-file scope is missing")
    if local_scope.get("max_download_bytes") != bounds.get("max_download_bytes"):
        raise ValueError("approval download byte caps do not match")

    return NyTransientLocalExecutionAuthorization(
        mode="AUTHORIZED_REAL_ONCE",
        attempt_number=gate2_attempt,
        local_file_approval_ref=local_ref,
        gate2_approval_ref=gate2_ref,
        local_file_approval_granted=True,
        gate2_approval_granted=True,
        max_download_bytes=int(bounds["max_download_bytes"]),
        max_uncompressed_bytes=int(bounds["max_uncompressed_bytes"]),
        max_archive_members=int(bounds["max_archive_members"]),
    )


def _is_authorized_temp_path(path: Path) -> bool:
    resolved = path.resolve()
    temp_root = Path(tempfile.gettempdir()).resolve()

    if not resolved.is_relative_to(temp_root):
        return False
    return any(part.startswith(TEMP_DIR_PREFIX) for part in resolved.parts)


def execute_transient_local_file_discovery(
    authorization: NyTransientLocalExecutionAuthorization,
    archive_path: Path,
) -> NyTransientLocalExecutionResultV1_1:
    """Process one already-downloaded temp ZIP and delete it immediately afterward."""

    if archive_path.name.lower() != authorization.expected_local_filename.lower():
        raise ValueError("local archive filename does not match authorized identity")
    if not _is_authorized_temp_path(archive_path):
        raise ValueError("local archive must be inside the dedicated OS-temp directory")
    if not archive_path.is_file():
        raise ValueError("local archive file is missing")

    archive_byte_count = archive_path.stat().st_size

    try:
        if archive_byte_count > authorization.max_download_bytes:
            return NyTransientLocalExecutionResultV1_1(
                status="BLOCKED",
                reason_code="LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
                local_file_deleted=True,
                archive_byte_count=archive_byte_count,
                schema_result=None,
            )

        with archive_path.open("rb") as stream:
            archive_bytes = stream.read(authorization.max_download_bytes + 1)

        if len(archive_bytes) > authorization.max_download_bytes:
            return NyTransientLocalExecutionResultV1_1(
                status="BLOCKED",
                reason_code="LOCAL_ARCHIVE_READ_EXCEEDS_DOWNLOAD_CAP",
                local_file_deleted=True,
                archive_byte_count=len(archive_bytes),
                schema_result=None,
            )

        schema_auth = NyOwnerNameSchemaDiscoveryAuthorization(
            mode=(
                "SYNTHETIC_TEST"
                if authorization.mode == "SYNTHETIC_TEST"
                else "AUTHORIZED_TRANSIENT_MEMORY_ONLY"
            ),
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
        schema_result = discover_ny_owner_name_schema(
            schema_auth,
            archive_bytes,
            structural_diagnostic_sink=structural_diagnostics.append,
        )
        if len(structural_diagnostics) > 1:
            raise RuntimeError("schema discovery emitted multiple structural diagnostics")
        structural_diagnostic = (
            structural_diagnostics[0] if structural_diagnostics else None
        )
        status: Literal["DISCOVERED", "BLOCKED"] = (
            "DISCOVERED" if schema_result.status == "DISCOVERED" else "BLOCKED"
        )
        return NyTransientLocalExecutionResultV1_1(
            status=status,
            reason_code=schema_result.reason_code,
            local_file_deleted=True,
            archive_byte_count=archive_byte_count,
            schema_result=schema_result,
            structural_diagnostic=structural_diagnostic,
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


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the bounded NY OSC transient-local-file schema discovery."
    )
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--local-approval", type=Path, required=True)
    parser.add_argument("--gate2-approval", type=Path, required=True)
    parser.add_argument("--expected-attempt-number", type=int)
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    authorization = build_real_execution_authorization(
        args.local_approval,
        args.gate2_approval,
        expected_attempt_number=args.expected_attempt_number,
    )
    result = execute_transient_local_file_discovery(authorization, args.archive)
    print(result.model_dump_json())
    return 0 if result.status == "DISCOVERED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
