"""NY OSC attempt-10 bounded product-slice runtime v1.7."""

from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

from unclaimed_platform.adapters.sources.ny_owner_name_attempt8_freshness import (
    EXPECTED_PREFLIGHT_FRESHNESS_SECONDS,
    validate_authorized_download_started_at,
)
from unclaimed_platform.adapters.sources.ny_owner_name_product_slice_v1 import (
    NyOwnerNameProductSliceResultV1,
    run_ny_owner_name_product_slice,
)

EXPECTED_ATTEMPT_NUMBER = 10
EXPECTED_PROPOSAL_REF = (
    "sources/proposals/ny_osc_owner_name_file_tenth_product_slice_authorization.v1.json"
)
EXPECTED_PROPOSAL_CHECKPOINT: Literal[
    "dea34cbc503dd5f6bf62ec6c31483056c4b34966"
] = "dea34cbc503dd5f6bf62ec6c31483056c4b34966"


class NyTransientLocalExecutionAuthorizationV1_6(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.6.0"] = "1.6.0"
    mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[10] = 10
    tenth_transient_local_approval_ref: str = Field(min_length=1)
    tenth_transient_pii_approval_ref: str = Field(min_length=1)
    tenth_fresh_preflight_receipt_ref: str = Field(min_length=1)
    tenth_execution_authorization_ref: str = Field(min_length=1)
    authorized_download_started_at_utc: str = Field(min_length=1)
    proposal_checkpoint: Literal[
        "dea34cbc503dd5f6bf62ec6c31483056c4b34966"
    ] = EXPECTED_PROPOSAL_CHECKPOINT
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    expected_local_filename: Literal["FINDERS.zip"] = "FINDERS.zip"
    max_download_bytes: Literal[450000000] = 450000000
    max_uncompressed_bytes: Literal[2000000000] = 2000000000
    max_archive_members: Literal[1] = 1
    delete_local_file_immediately: Literal[True] = True
    downloads_max: Literal[1] = 1
    retries_max: Literal[0] = 0
    direct_network_client_allowed: Literal[False] = False


class NyTransientLocalExecutionResultV1_7(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.7.0"] = "1.7.0"
    execution_mode: Literal["AUTHORIZED_REAL_ONCE"] = "AUTHORIZED_REAL_ONCE"
    attempt_number: Literal[10] = 10
    proposal_checkpoint: Literal[
        "dea34cbc503dd5f6bf62ec6c31483056c4b34966"
    ] = EXPECTED_PROPOSAL_CHECKPOINT
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    status: Literal["COMPLETED", "BLOCKED"]
    reason_code: Literal["PRODUCT_SLICE_COMPLETED", "EXECUTION_ERROR"]
    local_file_deleted: Literal[True]
    logical_deletion_only: Literal[True] = True
    physical_secure_erasure_guaranteed: Literal[False] = False
    archive_byte_count: int = Field(ge=0)
    product_slice: NyOwnerNameProductSliceResultV1 | None = None
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
    def validate_state(self) -> Self:
        if self.status == "COMPLETED":
            if (
                self.reason_code != "PRODUCT_SLICE_COMPLETED"
                or self.product_slice is None
            ):
                raise ValueError("completed result requires product slice")
        elif self.product_slice is not None:
            raise ValueError("blocked result cannot expose product slice")
        return self


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"unable to read authorization artifact: {path.name}"
        ) from exc
    if not isinstance(value, dict):
        raise ValueError("authorization artifact must be a JSON object")
    return value


def _string(record: dict[str, Any], key: str, label: str) -> str:
    value = record.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label} {key} is missing")
    return value


def _binding(record: dict[str, Any], label: str, runner: str) -> None:
    if record.get("attempt_number") != EXPECTED_ATTEMPT_NUMBER:
        raise ValueError(f"{label} attempt mismatch")
    if record.get("proposal_ref") != EXPECTED_PROPOSAL_REF:
        raise ValueError(f"{label} proposal ref mismatch")
    if record.get("proposal_checkpoint") != EXPECTED_PROPOSAL_CHECKPOINT:
        raise ValueError(f"{label} proposal checkpoint mismatch")
    if record.get("runner_checkpoint") != runner:
        raise ValueError(f"{label} runner checkpoint mismatch")
    if record.get("runner_ci_conclusion") != "SUCCESS":
        raise ValueError(f"{label} runner CI is not successful")


def build_real_execution_authorization_v1_6(
    local_path: Path,
    pii_path: Path,
    preflight_path: Path,
    execution_path: Path,
    *,
    expected_runner_checkpoint: str,
    authorized_download_started_at_utc: str,
    now_utc: datetime | None = None,
) -> NyTransientLocalExecutionAuthorizationV1_6:
    if len(expected_runner_checkpoint) != 40:
        raise ValueError("runner checkpoint must be a Git SHA")
    local = _load(local_path)
    pii = _load(pii_path)
    preflight = _load(preflight_path)
    execution = _load(execution_path)
    for record, label in (
        (local, "local approval"),
        (pii, "PII approval"),
        (preflight, "preflight"),
        (execution, "execution authorization"),
    ):
        _binding(record, label, expected_runner_checkpoint)
    if local.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("local approval is not granted/not-consumed")
    if pii.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("PII approval is not granted/not-consumed")
    if execution.get("status") != "GRANTED_NOT_CONSUMED":
        raise ValueError("execution authorization is not granted/not-consumed")
    if (
        preflight.get("status") != "EXACT_MATCH"
        or preflight.get("remote_preflight_performed") is not True
    ):
        raise ValueError("preflight is not an exact match")
    privacy_keys = (
        "download_performed",
        "owner_file_opened",
        "owner_pii_processed",
        "contains_owner_pii",
    )
    for key in privacy_keys:
        if preflight.get(key) is not False:
            raise ValueError("preflight privacy boundary mismatch")
    if (
        preflight.get("freshness_window_seconds")
        != EXPECTED_PREFLIGHT_FRESHNESS_SECONDS
    ):
        raise ValueError("preflight freshness policy mismatch")
    started = validate_authorized_download_started_at(
        preflight_performed_at_utc=_string(
            preflight,
            "performed_at_utc",
            "preflight",
        ),
        authorized_download_started_at_utc=authorized_download_started_at_utc,
        freshness_window_seconds=EXPECTED_PREFLIGHT_FRESHNESS_SECONDS,
        observed_now_utc=(now_utc or datetime.now(UTC)),
    )
    preflight_ref = _string(preflight, "receipt_ref", "preflight")
    if execution.get("fresh_preflight_receipt_ref") != preflight_ref:
        raise ValueError("execution/preflight binding mismatch")
    expected_download_authority = "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP"
    if execution.get("download_authority") != expected_download_authority:
        raise ValueError("download authority mismatch")
    if execution.get("execution_authority") != "ONE_BOUND_GATE10_EXECUTION":
        raise ValueError("Gate 10 execution authority mismatch")
    return NyTransientLocalExecutionAuthorizationV1_6(
        tenth_transient_local_approval_ref=_string(
            local,
            "execution_approval_ref",
            "local approval",
        ),
        tenth_transient_pii_approval_ref=_string(
            pii,
            "execution_approval_ref",
            "PII approval",
        ),
        tenth_fresh_preflight_receipt_ref=preflight_ref,
        tenth_execution_authorization_ref=_string(
            execution,
            "execution_approval_ref",
            "execution authorization",
        ),
        authorized_download_started_at_utc=(
            started.isoformat().replace("+00:00", "Z")
        ),
        runner_checkpoint=expected_runner_checkpoint,
    )


def execute_transient_local_product_slice_v1_7(
    authorization: NyTransientLocalExecutionAuthorizationV1_6,
    archive_path: Path,
) -> NyTransientLocalExecutionResultV1_7:
    archive_size = archive_path.stat().st_size
    try:
        product_slice = run_ny_owner_name_product_slice(
            archive_path,
            max_download_bytes=authorization.max_download_bytes,
            max_uncompressed_bytes=authorization.max_uncompressed_bytes,
            max_archive_members=authorization.max_archive_members,
        )
        return NyTransientLocalExecutionResultV1_7(
            status="COMPLETED",
            reason_code="PRODUCT_SLICE_COMPLETED",
            local_file_deleted=True,
            archive_byte_count=archive_size,
            product_slice=product_slice,
            execution_authorization_ref=(
                authorization.tenth_execution_authorization_ref
            ),
            authorized_download_started_at_utc=(
                authorization.authorized_download_started_at_utc
            ),
            runner_checkpoint=authorization.runner_checkpoint,
        )
    except Exception:
        return NyTransientLocalExecutionResultV1_7(
            status="BLOCKED",
            reason_code="EXECUTION_ERROR",
            local_file_deleted=True,
            archive_byte_count=archive_size,
            product_slice=None,
            execution_authorization_ref=(
                authorization.tenth_execution_authorization_ref
            ),
            authorized_download_started_at_utc=(
                authorization.authorized_download_started_at_utc
            ),
            runner_checkpoint=authorization.runner_checkpoint,
        )
    finally:
        try:
            archive_path.unlink(missing_ok=True)
            parent = archive_path.parent
            if parent.name.startswith("unclaimed-ny-osc-gate2-tenth-"):
                shutil.rmtree(parent, ignore_errors=True)
        except OSError:
            pass
