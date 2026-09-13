from __future__ import annotations

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/reviewer", tags=["reviewer"])


class MilestoneSummary(BaseModel):
    id: Literal["M0", "M1", "M2", "M3"]
    label: str
    status: Literal[
        "VERIFIED",
        "COMPLETE",
        "READINESS_GATES_VERIFIED",
        "IN_PROGRESS",
        "BLOCKED",
    ]


class SourceRegistrySummary(BaseModel):
    approved_real_sources: int
    real_source_activation: Literal["BLOCKED", "APPROVED"]
    california_sco_candidate: Literal["NOT_APPROVED", "APPROVED"]


class RawArtifactSummary(BaseModel):
    source_id: str
    source_uri: str
    authority: str
    acquisition_method: str
    content_hash: str
    byte_count: int
    content_type: str
    storage_reference: str
    synthetic: Literal[True]
    immutable: Literal[True]


class GovernanceSummary(BaseModel):
    privacy_policy: Literal["PASS_SYNTHETIC_SCOPE"]
    provenance: Literal["PASS"]
    approval: Literal["NOT_REQUIRED_SYNTHETIC"]
    retention: Literal["PASS"]
    data_minimization: Literal["PASS"]
    unnecessary_pii: Literal["ABSENT"]


class AuditSummary(BaseModel):
    model: Literal["M2_AUDIT_HASH_CHAIN"]
    algorithm: Literal["SHA-256"]
    chain_verification: Literal["VERIFIED_BY_TEST_SUITE"]
    append_only: Literal[True]
    durable_persistence: Literal["PENDING"]


BlockedCapability = Literal[
    "REAL_ACQUISITION",
    "BENEFICIARY_MATCHING",
    "OUTREACH",
    "CLAIMANT_VERIFICATION",
    "FEE_AGREEMENT",
    "CLAIM_SUBMISSION",
]


class ReviewerOperationsSummary(BaseModel):
    contract_version: Literal["1.0.0"]
    data_mode: Literal["GOVERNED_SYNTHETIC_PREVIEW"]
    read_only: Literal[True]
    snapshot_date: str
    milestones: tuple[MilestoneSummary, ...]
    source_registry: SourceRegistrySummary
    blocked_capabilities: tuple[BlockedCapability, ...]
    raw_artifact: RawArtifactSummary
    governance: GovernanceSummary
    audit: AuditSummary


def build_operations_summary() -> ReviewerOperationsSummary:
    content_hash = "5027920b97e7e5827cc45e4fe8484108025e31b792f735809cdb878e2f717bd7"
    return ReviewerOperationsSummary(
        contract_version="1.0.0",
        data_mode="GOVERNED_SYNTHETIC_PREVIEW",
        read_only=True,
        snapshot_date="2026-09-13",
        milestones=(
            MilestoneSummary(id="M0", label="Repository & Development Harness", status="VERIFIED"),
            MilestoneSummary(id="M1", label="Machine Contracts", status="VERIFIED"),
            MilestoneSummary(id="M2", label="State & Governance Core", status="VERIFIED"),
            MilestoneSummary(
                id="M3",
                label="California Data Spike Readiness",
                status="READINESS_GATES_VERIFIED",
            ),
        ),
        source_registry=SourceRegistrySummary(
            approved_real_sources=0,
            real_source_activation="BLOCKED",
            california_sco_candidate="NOT_APPROVED",
        ),
        blocked_capabilities=(
            "REAL_ACQUISITION",
            "BENEFICIARY_MATCHING",
            "OUTREACH",
            "CLAIMANT_VERIFICATION",
            "FEE_AGREEMENT",
            "CLAIM_SUBMISSION",
        ),
        raw_artifact=RawArtifactSummary(
            source_id="synthetic-reviewer-fixture",
            source_uri="synthetic://reviewer/m3/raw-artifact",
            authority="SYNTHETIC_TEST_FIXTURE",
            acquisition_method="SYNTHETIC_FIXTURE",
            content_hash=content_hash,
            byte_count=51,
            content_type="text/csv",
            storage_reference=f"raw://synthetic/sha256/{content_hash}",
            synthetic=True,
            immutable=True,
        ),
        governance=GovernanceSummary(
            privacy_policy="PASS_SYNTHETIC_SCOPE",
            provenance="PASS",
            approval="NOT_REQUIRED_SYNTHETIC",
            retention="PASS",
            data_minimization="PASS",
            unnecessary_pii="ABSENT",
        ),
        audit=AuditSummary(
            model="M2_AUDIT_HASH_CHAIN",
            algorithm="SHA-256",
            chain_verification="VERIFIED_BY_TEST_SUITE",
            append_only=True,
            durable_persistence="PENDING",
        ),
    )


@router.get("/operations-summary", response_model=ReviewerOperationsSummary)
def operations_summary() -> ReviewerOperationsSummary:
    """Return the governed synthetic snapshot used by the first reviewer console."""
    return build_operations_summary()
