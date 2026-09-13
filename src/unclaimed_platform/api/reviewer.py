from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict

router = APIRouter(prefix="/api/reviewer", tags=["reviewer"])


class MilestoneStatus(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    label: str
    status: str


class SourceRegistryStatus(BaseModel):
    model_config = ConfigDict(frozen=True)

    approved_real_sources: int
    real_acquisition: Literal["BLOCKED"]
    beneficiary_matching: Literal["BLOCKED"]


class RawArtifactSummary(BaseModel):
    model_config = ConfigDict(frozen=True)

    artifact_id: str
    sha256: str
    byte_count: int
    content_type: str
    source_id: str
    source_uri: str
    authority: str
    acquisition_method: str
    retrieved_at: str
    provenance_sha256: str
    synthetic: bool
    immutable: bool


class GovernanceStatus(BaseModel):
    model_config = ConfigDict(frozen=True)

    privacy_gate: Literal["PASS_SYNTHETIC_ONLY"]
    source_approval_gate: Literal["BLOCKED_NO_REAL_SOURCE"]
    retention_policy: Literal["REQUIRED"]
    pii_mode: Literal["NO_REAL_PII"]


class AuditStatus(BaseModel):
    model_config = ConfigDict(frozen=True)

    chain: Literal["HEALTHY_SYNTHETIC"]
    algorithm: Literal["SHA-256"]
    durable_backend: Literal["PENDING"]


class PlatformReadiness(BaseModel):
    model_config = ConfigDict(frozen=True)

    vercel: Literal["NOT_CONNECTED"]
    supabase: Literal["NOT_CONNECTED"]


class OperationsSnapshot(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"]
    mode: Literal["SYNTHETIC_READ_ONLY"]
    milestones: list[MilestoneStatus]
    source_registry: SourceRegistryStatus
    raw_artifact: RawArtifactSummary
    governance: GovernanceStatus
    audit: AuditStatus
    platform: PlatformReadiness


def synthetic_operations_snapshot() -> OperationsSnapshot:
    return OperationsSnapshot(
        contract_version="1.0.0",
        mode="SYNTHETIC_READ_ONLY",
        milestones=[
            MilestoneStatus(id="M0", label="Repository & Development Harness", status="VERIFIED"),
            MilestoneStatus(id="M1", label="Machine Contracts", status="VERIFIED"),
            MilestoneStatus(id="M2", label="State & Governance Core", status="VERIFIED"),
            MilestoneStatus(
                id="M3",
                label="California Data Spike Readiness",
                status="GOVERNANCE_READY_REAL_ACQUISITION_BLOCKED",
            ),
        ],
        source_registry=SourceRegistryStatus(
            approved_real_sources=0,
            real_acquisition="BLOCKED",
            beneficiary_matching="BLOCKED",
        ),
        raw_artifact=RawArtifactSummary(
            artifact_id="synthetic:m3-operations-console-demo",
            sha256="d8f9fb455e7c7cc962a71f11201ef8b5d8922262b3010bd7a84afc711c8b279f",
            byte_count=49,
            content_type="text/plain",
            source_id="synthetic-m3-demo",
            source_uri="synthetic://m3/operations-console",
            authority="UNCLAIMED_PLATFORM_TEST_FIXTURE",
            acquisition_method="SYNTHETIC_FIXTURE",
            retrieved_at="2026-09-13T00:00:00Z",
            provenance_sha256="f4e9c9868f9fb7f10d19c00135019afd9262df5ac209e070a13b51b8af5319ee",
            synthetic=True,
            immutable=True,
        ),
        governance=GovernanceStatus(
            privacy_gate="PASS_SYNTHETIC_ONLY",
            source_approval_gate="BLOCKED_NO_REAL_SOURCE",
            retention_policy="REQUIRED",
            pii_mode="NO_REAL_PII",
        ),
        audit=AuditStatus(
            chain="HEALTHY_SYNTHETIC",
            algorithm="SHA-256",
            durable_backend="PENDING",
        ),
        platform=PlatformReadiness(
            vercel="NOT_CONNECTED",
            supabase="NOT_CONNECTED",
        ),
    )


@router.get("/m3/operations", response_model=OperationsSnapshot)
def get_m3_operations() -> OperationsSnapshot:
    """Return the governed, read-only M3 reviewer snapshot."""
    return synthetic_operations_snapshot()
