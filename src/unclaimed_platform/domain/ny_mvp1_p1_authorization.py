"""Fresh single-use authorization binding for NY MVP-1 real P1.

This module performs no network I/O and does not open the owner file. It only
validates pre-created local authorization artifacts and a fresh preflight receipt.
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

SCOPE_REF = "sources/proposals/ny_mvp1_real_p1_targetability_execution_scope.v1.json"
SCOPE_BLOB_SHA = "52e23fefee358ea51d6d7e6aa3085b7491807a9c"

GateId = Literal[
    "HUMAN_NY_MVP1_P1_TRANSIENT_LOCAL_FILE_APPROVAL",
    "HUMAN_NY_MVP1_P1_L1_TRANSIENT_PII_APPROVAL",
    "HUMAN_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_AUTHORIZATION",
    "HUMAN_NY_MVP1_P1_L1_EXECUTION_AUTHORIZATION",
    "HUMAN_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_APPROVAL",
    "HUMAN_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_APPROVAL",
    "HUMAN_NY_MVP1_P1_L2A_EXECUTION_AUTHORIZATION",
]

GATE_PHRASES: dict[str, str] = {
    "HUMAN_NY_MVP1_P1_TRANSIENT_LOCAL_FILE_APPROVAL":
        "APPROVE_NY_MVP1_P1_TRANSIENT_LOCAL_FILE_ONCE",
    "HUMAN_NY_MVP1_P1_L1_TRANSIENT_PII_APPROVAL":
        "APPROVE_NY_MVP1_P1_L1_TRANSIENT_PII_ONCE",
    "HUMAN_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_AUTHORIZATION":
        "AUTHORIZE_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_ONCE",
    "HUMAN_NY_MVP1_P1_L1_EXECUTION_AUTHORIZATION":
        "AUTHORIZE_NY_MVP1_P1_L1_EXECUTION_ONCE",
    "HUMAN_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_APPROVAL":
        "APPROVE_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_ONCE",
    "HUMAN_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_APPROVAL":
        "APPROVE_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_ONCE",
    "HUMAN_NY_MVP1_P1_L2A_EXECUTION_AUTHORIZATION":
        "AUTHORIZE_NY_MVP1_P1_L2A_EXECUTION_ONCE",
}


class ProviderBinding(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    provider_id: str = Field(min_length=1)
    provider_terms_review_ref: str = Field(min_length=1)
    approved_external_cash_budget_cents: Literal[0] = 0
    approved_manual_research_cap_seconds: Literal[900] = 900
    paid_api_allowed: Literal[False] = False
    paid_data_broker_allowed: Literal[False] = False
    consumer_report_fcra_product_allowed: Literal[False] = False


class SingleUseGateArtifact(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["1.0.0"] = "1.0.0"
    artifact_id: Literal["ny.mvp1.p1.single_use_gate"] = "ny.mvp1.p1.single_use_gate"
    gate_id: GateId
    required_owner_phrase: str = Field(min_length=1)
    owner_authorization: str | None
    granted_on: str | None
    execution_approval_ref: str | None
    status: Literal[
        "NOT_GRANTED",
        "GRANTED_NOT_CONSUMED",
        "CONSUMED_SINGLE_USE_NON_REUSABLE",
    ]
    single_use: Literal[True] = True
    reusable: Literal[False] = False
    retry_authorized: Literal[False] = False
    scope_ref: Literal[
        "sources/proposals/ny_mvp1_real_p1_targetability_execution_scope.v1.json"
    ] = SCOPE_REF
    scope_blob_sha: Literal[
        "52e23fefee358ea51d6d7e6aa3085b7491807a9c"
    ] = SCOPE_BLOB_SHA
    runner_checkpoint: str | None = Field(default=None, pattern=r"^[0-9a-f]{40}$")
    runner_ci_run_id: int | None = Field(default=None, ge=1)
    runner_ci_conclusion: str | None = None
    provider_binding: ProviderBinding | None = None
    consumed_on: str | None = None
    execution_result_ref: str | None = None

    @model_validator(mode="after")
    def validate_gate(self) -> Self:
        expected_phrase = GATE_PHRASES[self.gate_id]
        if self.required_owner_phrase != expected_phrase:
            raise ValueError("required owner phrase does not match gate")
        is_provider_gate = (
            self.gate_id == "HUMAN_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_APPROVAL"
        )
        if not is_provider_gate and self.provider_binding is not None:
            raise ValueError("provider binding is allowed only on provider/budget gate")
        if self.status == "NOT_GRANTED":
            if any(
                value is not None
                for value in (
                    self.owner_authorization,
                    self.granted_on,
                    self.execution_approval_ref,
                    self.runner_checkpoint,
                    self.runner_ci_run_id,
                    self.runner_ci_conclusion,
                    self.consumed_on,
                    self.execution_result_ref,
                )
            ):
                raise ValueError("not-granted gate cannot contain execution approval state")
            if self.provider_binding is not None:
                raise ValueError("not-granted provider gate cannot bind a provider")
        elif self.status == "GRANTED_NOT_CONSUMED":
            if self.owner_authorization != expected_phrase:
                raise ValueError("owner authorization phrase mismatch")
            if not self.granted_on or not self.execution_approval_ref:
                raise ValueError("granted gate requires date and approval ref")
            if not self.runner_checkpoint or not self.runner_ci_run_id:
                raise ValueError("granted gate requires runner binding")
            if self.runner_ci_conclusion != "SUCCESS":
                raise ValueError("granted gate requires successful runner CI")
            if self.consumed_on is not None or self.execution_result_ref is not None:
                raise ValueError("unconsumed gate cannot contain consumption state")
            if is_provider_gate and self.provider_binding is None:
                raise ValueError("provider/budget gate requires approved provider binding")
        else:
            if self.owner_authorization != expected_phrase:
                raise ValueError("consumed gate owner authorization mismatch")
            if not self.consumed_on or not self.execution_result_ref:
                raise ValueError("consumed gate requires consumption provenance")
        return self


class FreshPreflightReceipt(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["1.0.0"] = "1.0.0"
    artifact_id: Literal["ny.mvp1.p1.fresh_listing_preflight_receipt"] = (
        "ny.mvp1.p1.fresh_listing_preflight_receipt"
    )
    receipt_ref: str = Field(min_length=1)
    status: Literal["EXACT_MATCH"] = "EXACT_MATCH"
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = (
        "ny.osc.unclaimed_funds.owner_name_file"
    )
    performed_at_utc: str = Field(min_length=1)
    freshness_window_seconds: Literal[900] = 900
    remote_name: Literal["FINDERS.zip", "FINDERS.ZIP", "NYSFINDERS.ZIP"]
    remote_size_display: str = Field(min_length=1)
    remote_last_modified_display: str = Field(min_length=1)
    remote_preflight_performed: Literal[True] = True
    download_performed: Literal[False] = False
    owner_file_opened: Literal[False] = False
    owner_pii_processed: Literal[False] = False
    contains_owner_pii: Literal[False] = False
    source_snapshot_ref: str = Field(min_length=1)
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    preflight_authorization_ref: str = Field(min_length=1)


class P1ExecutionAuthorization(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    execution_mode: Literal["AUTHORIZED_REAL_LOCAL_FILE_ONCE"] = (
        "AUTHORIZED_REAL_LOCAL_FILE_ONCE"
    )
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = (
        "ny.osc.unclaimed_funds.owner_name_file"
    )
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    source_snapshot_ref: str = Field(min_length=1)
    fresh_preflight_receipt_ref: str = Field(min_length=1)
    authorized_download_started_at_utc: str = Field(min_length=1)
    local_file_approval_ref: str = Field(min_length=1)
    l1_pii_approval_ref: str = Field(min_length=1)
    preflight_authorization_ref: str = Field(min_length=1)
    l1_execution_authorization_ref: str = Field(min_length=1)
    l2a_enabled: bool = False
    l2a_pii_approval_ref: str | None = None
    l2a_provider_budget_approval_ref: str | None = None
    l2a_execution_authorization_ref: str | None = None
    provider_binding: ProviderBinding | None = None
    max_download_bytes: Literal[450000000] = 450000000
    max_uncompressed_bytes: Literal[2000000000] = 2000000000
    max_archive_members: Literal[1] = 1
    downloads_max: Literal[1] = 1
    executions_max: Literal[1] = 1
    retries_max: Literal[0] = 0
    direct_network_client_allowed: Literal[False] = False
    delete_local_file_immediately: Literal[True] = True

    @model_validator(mode="after")
    def validate_l2a_shape(self) -> Self:
        optional = (
            self.l2a_pii_approval_ref,
            self.l2a_provider_budget_approval_ref,
            self.l2a_execution_authorization_ref,
            self.provider_binding,
        )
        if self.l2a_enabled and any(value is None for value in optional):
            raise ValueError("L2-A enabled requires all L2-A authorization bindings")
        if not self.l2a_enabled and any(value is not None for value in optional):
            raise ValueError("L2-A disabled cannot contain L2-A bindings")
        return self


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"unable to read authorization artifact: {path.name}") from exc
    if not isinstance(value, dict):
        raise ValueError("authorization artifact must be a JSON object")
    return value


def _load_gate(path: Path) -> SingleUseGateArtifact:
    return SingleUseGateArtifact.model_validate(_load_json(path))


def _require_gate(
    gate: SingleUseGateArtifact,
    expected_gate_id: GateId,
    runner_checkpoint: str,
) -> None:
    if gate.gate_id != expected_gate_id:
        raise ValueError("gate id mismatch")
    if gate.status != "GRANTED_NOT_CONSUMED":
        raise ValueError(f"{expected_gate_id} is not granted/not-consumed")
    if gate.runner_checkpoint != runner_checkpoint:
        raise ValueError("gate runner checkpoint mismatch")
    if gate.runner_ci_conclusion != "SUCCESS":
        raise ValueError("gate runner CI is not successful")


def build_p1_execution_authorization(
    *,
    local_file_gate_path: Path,
    l1_pii_gate_path: Path,
    preflight_gate_path: Path,
    l1_execution_gate_path: Path,
    preflight_receipt_path: Path,
    expected_runner_checkpoint: str,
    authorized_download_started_at_utc: str,
    l2a_pii_gate_path: Path | None = None,
    l2a_provider_budget_gate_path: Path | None = None,
    l2a_execution_gate_path: Path | None = None,
    now_utc: datetime | None = None,
) -> P1ExecutionAuthorization:
    """Bind fresh gates and receipt into one single-use local execution authority."""

    if len(expected_runner_checkpoint) != 40:
        raise ValueError("runner checkpoint must be a Git SHA")

    local_gate = _load_gate(local_file_gate_path)
    l1_pii_gate = _load_gate(l1_pii_gate_path)
    preflight_gate = _load_gate(preflight_gate_path)
    l1_exec_gate = _load_gate(l1_execution_gate_path)

    _require_gate(
        local_gate,
        "HUMAN_NY_MVP1_P1_TRANSIENT_LOCAL_FILE_APPROVAL",
        expected_runner_checkpoint,
    )
    _require_gate(
        l1_pii_gate,
        "HUMAN_NY_MVP1_P1_L1_TRANSIENT_PII_APPROVAL",
        expected_runner_checkpoint,
    )
    _require_gate(
        preflight_gate,
        "HUMAN_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_AUTHORIZATION",
        expected_runner_checkpoint,
    )
    _require_gate(
        l1_exec_gate,
        "HUMAN_NY_MVP1_P1_L1_EXECUTION_AUTHORIZATION",
        expected_runner_checkpoint,
    )

    receipt = FreshPreflightReceipt.model_validate(_load_json(preflight_receipt_path))
    if receipt.runner_checkpoint != expected_runner_checkpoint:
        raise ValueError("preflight receipt runner checkpoint mismatch")
    if receipt.preflight_authorization_ref != preflight_gate.execution_approval_ref:
        raise ValueError("preflight receipt is not bound to approved preflight gate")
    if receipt.freshness_window_seconds != EXPECTED_PREFLIGHT_FRESHNESS_SECONDS:
        raise ValueError("preflight freshness policy mismatch")

    started = validate_authorized_download_started_at(
        preflight_performed_at_utc=receipt.performed_at_utc,
        authorized_download_started_at_utc=authorized_download_started_at_utc,
        freshness_window_seconds=receipt.freshness_window_seconds,
        observed_now_utc=(now_utc or datetime.now(UTC)),
    )

    l2_paths = (
        l2a_pii_gate_path,
        l2a_provider_budget_gate_path,
        l2a_execution_gate_path,
    )
    l2a_enabled = any(path is not None for path in l2_paths)
    if l2a_enabled and any(path is None for path in l2_paths):
        raise ValueError("L2-A requires all three fresh gate artifacts")

    l2a_pii_ref: str | None = None
    l2a_provider_ref: str | None = None
    l2a_exec_ref: str | None = None
    provider_binding: ProviderBinding | None = None
    if l2a_enabled:
        assert l2a_pii_gate_path is not None
        assert l2a_provider_budget_gate_path is not None
        assert l2a_execution_gate_path is not None
        l2_pii = _load_gate(l2a_pii_gate_path)
        l2_provider = _load_gate(l2a_provider_budget_gate_path)
        l2_exec = _load_gate(l2a_execution_gate_path)
        _require_gate(
            l2_pii,
            "HUMAN_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_APPROVAL",
            expected_runner_checkpoint,
        )
        _require_gate(
            l2_provider,
            "HUMAN_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_APPROVAL",
            expected_runner_checkpoint,
        )
        _require_gate(
            l2_exec,
            "HUMAN_NY_MVP1_P1_L2A_EXECUTION_AUTHORIZATION",
            expected_runner_checkpoint,
        )
        if l2_provider.provider_binding is None:
            raise ValueError("L2-A provider/budget gate lacks provider binding")
        l2a_pii_ref = l2_pii.execution_approval_ref
        l2a_provider_ref = l2_provider.execution_approval_ref
        l2a_exec_ref = l2_exec.execution_approval_ref
        provider_binding = l2_provider.provider_binding

    refs = (
        local_gate.execution_approval_ref,
        l1_pii_gate.execution_approval_ref,
        preflight_gate.execution_approval_ref,
        l1_exec_gate.execution_approval_ref,
    )
    if any(ref is None for ref in refs):
        raise ValueError("L1 authorization reference missing")

    return P1ExecutionAuthorization(
        runner_checkpoint=expected_runner_checkpoint,
        source_snapshot_ref=receipt.source_snapshot_ref,
        fresh_preflight_receipt_ref=receipt.receipt_ref,
        authorized_download_started_at_utc=started.isoformat().replace("+00:00", "Z"),
        local_file_approval_ref=refs[0],
        l1_pii_approval_ref=refs[1],
        preflight_authorization_ref=refs[2],
        l1_execution_authorization_ref=refs[3],
        l2a_enabled=l2a_enabled,
        l2a_pii_approval_ref=l2a_pii_ref,
        l2a_provider_budget_approval_ref=l2a_provider_ref,
        l2a_execution_authorization_ref=l2a_exec_ref,
        provider_binding=provider_binding,
    )
