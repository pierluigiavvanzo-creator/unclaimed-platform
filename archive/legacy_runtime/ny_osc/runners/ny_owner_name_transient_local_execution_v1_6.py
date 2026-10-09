"""NY OSC attempt-9 bounded runtime v1.6.

Attempt 9 exists only because attempt 8 produced a concrete real-source blocker:
14 pipe bytes / 15 structural fields.  This runtime tests the terminal-empty-field
hypothesis and, only if it is confirmed for every complete record, treats the
source as the documented 14 fields plus a transport-level terminal delimiter.
No owner values are returned or persisted.
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
from unclaimed_platform.adapters.sources.ny_owner_name_trailing_delimiter_diagnostic import (
    NyOwnerNameTrailingDelimiterDiagnosticResult,
    diagnose_ny_owner_name_trailing_delimiter,
)

EXPECTED_ATTEMPT_NUMBER = 9
EXPECTED_PROPOSAL_REF = (
    "sources/proposals/ny_osc_owner_name_file_ninth_bounded_attempt_authorization.v1.json"
)
EXPECTED_PROPOSAL_CHECKPOINT: Literal[
    "9170f27480ccd49eafd040346fa80e0fe9ab078f"
] = "9170f27480ccd49eafd040346fa80e0fe9ab078f"


class NyTransientLocalExecutionAuthorizationV1_5(BaseModel):
    """Attempt-9 real authorization compiled from four machine-bound artifacts."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.5.0"] = "1.5.0"
    mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[9] = 9
    ninth_transient_local_approval_ref: str = Field(min_length=1)
    ninth_transient_pii_approval_ref: str = Field(min_length=1)
    ninth_fresh_preflight_receipt_ref: str = Field(min_length=1)
    ninth_execution_authorization_ref: str = Field(min_length=1)
    authorized_download_started_at_utc: str = Field(min_length=1)
    local_file_approval_granted: Literal[True]
    transient_pii_approval_granted: Literal[True]
    fresh_preflight_exact_match: Literal[True]
    execution_authorization_granted: Literal[True]
    proposal_checkpoint: Literal[
        "9170f27480ccd49eafd040346fa80e0fe9ab078f"
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
    downloads_max: Literal[1] = 1
    retries_max: Literal[0] = 0
    direct_network_client_allowed: Literal[False] = False


class NyTransientLocalExecutionResultV1_6(BaseModel):
    """Persistable attempt-9 result containing only aggregate structural metadata."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.6.0"] = "1.6.0"
    execution_mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[9] = 9
    proposal_checkpoint: Literal[
        "9170f27480ccd49eafd040346fa80e0fe9ab078f"
    ] = EXPECTED_PROPOSAL_CHECKPOINT
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    status: Literal["DISCOVERED", "BLOCKED"]
    reason_code: Literal[
        "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER_CONFIRMED",
        "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED",
        "EXECUTION_ERROR",
    ]
    local_file_deleted: Literal[True]
    logical_deletion_only: Literal[True] = True
    physical_secure_erasure_guaranteed: Literal[False] = False
    archive_byte_count: int = Field(ge=0)
    diagnostic: NyOwnerNameTrailingDelimiterDiagnosticResult | None = None
    normalized_documented_field_count: Literal[14] = 14
    terminal_empty_field_ignored_for_structural_width: bool
    structural_normalization_allowed: bool
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
    no_raw_record_returned: Literal[True] = True
    no_owner_values_returned: Literal[True] = True

    @model_validator(mode="after")
    def validate_result(self) -> Self:
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
        confirmed = (
            self.reason_code
            == "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER_CONFIRMED"
        )
        if (self.status == "DISCOVERED") != confirmed:
            raise ValueError("status/reason mismatch")
        if self.structural_normalization_allowed != confirmed:
            raise ValueError("normalization flag/reason mismatch")
        if self.terminal_empty_field_ignored_for_structural_width != confirmed:
            raise ValueError("terminal-field normalization flag/reason mismatch")
        return self


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"unable to read authorization artifact: {path.name}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"authorization artifact must be an object: {path.name}")
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
    if record.get("runner_checkpoint") != expected_runner_checkpoint:
        raise ValueError(f"{label} runner checkpoint mismatch")
    if record.get("runner_ci_conclusion") != "SUCCESS":
        raise ValueError(f"{label} runner CI is not successful")


def build_real_execution_authorization_v1_5(
    local_approval_path: Path,
    transient_pii_approval_path: Path,
    fresh_preflight_receipt_path: Path,
    execution_authorization_path: Path,
    *,
    expected_runner_checkpoint: str,
    authorized_download_started_at_utc: str,
    now_utc: datetime | None = None,
) -> NyTransientLocalExecutionAuthorizationV1_5:
    """Compile one attempt-9 authorization and validate download-start freshness."""

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

    local_ref = _required_string(local, "execution_approval_ref", "local approval")
    pii_ref = _required_string(pii, "execution_approval_ref", "PII approval")
    preflight_ref = _required_string(preflight, "receipt_ref", "preflight receipt")
    execution_ref = _required_string(
        execution, "execution_approval_ref", "execution authorization"
    )
    if len({local_ref, pii_ref, preflight_ref, execution_ref}) != 4:
        raise ValueError("all four attempt-9 binding refs must be distinct")
    if execution.get("fresh_preflight_receipt_ref") != preflight_ref:
        raise ValueError("execution authorization preflight binding mismatch")
    if execution.get("fresh_preflight_status") != "EXACT_MATCH":
        raise ValueError("execution authorization requires exact-match preflight")
    if execution.get("download_authority") != "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP":
        raise ValueError("execution authorization download authority mismatch")
    if execution.get("execution_authority") != "ONE_BOUND_GATE9_EXECUTION":
        raise ValueError("execution authorization Gate 9 authority mismatch")

    return NyTransientLocalExecutionAuthorizationV1_5(
        ninth_transient_local_approval_ref=local_ref,
        ninth_transient_pii_approval_ref=pii_ref,
        ninth_fresh_preflight_receipt_ref=preflight_ref,
        ninth_execution_authorization_ref=execution_ref,
        authorized_download_started_at_utc=canonical_start,
        local_file_approval_granted=True,
        transient_pii_approval_granted=True,
        fresh_preflight_exact_match=True,
        execution_authorization_granted=True,
        runner_checkpoint=expected_runner_checkpoint,
    )


def execute_transient_local_file_discovery_v1_6(
    authorization: NyTransientLocalExecutionAuthorizationV1_5,
    archive_path: Path,
) -> NyTransientLocalExecutionResultV1_6:
    """Execute the bounded trailing-delimiter diagnostic exactly once."""

    archive_byte_count = archive_path.stat().st_size
    diagnostic: NyOwnerNameTrailingDelimiterDiagnosticResult | None = None
    reason_code: Literal[
        "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER_CONFIRMED",
        "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED",
        "EXECUTION_ERROR",
    ] = "EXECUTION_ERROR"
    status: Literal["DISCOVERED", "BLOCKED"] = "BLOCKED"
    confirmed = False
    try:
        diagnostic = diagnose_ny_owner_name_trailing_delimiter(
            archive_path,
            max_download_bytes=authorization.max_download_bytes,
            max_uncompressed_bytes=authorization.max_uncompressed_bytes,
            max_archive_members=authorization.max_archive_members,
        )
        confirmed = diagnostic.structural_normalization_allowed
        if confirmed:
            status = "DISCOVERED"
            reason_code = (
                "DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER_CONFIRMED"
            )
        else:
            reason_code = "TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED"
    finally:
        archive_path.unlink(missing_ok=True)

    return NyTransientLocalExecutionResultV1_6(
        runner_checkpoint=authorization.runner_checkpoint,
        status=status,
        reason_code=reason_code,
        local_file_deleted=True,
        archive_byte_count=archive_byte_count,
        diagnostic=diagnostic,
        terminal_empty_field_ignored_for_structural_width=confirmed,
        structural_normalization_allowed=confirmed,
        execution_authorization_ref=(
            authorization.ninth_execution_authorization_ref
        ),
        authorized_download_started_at_utc=(
            authorization.authorized_download_started_at_utc
        ),
    )
