from datetime import UTC, datetime
from typing import Literal
from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict

from unclaimed_platform.domain.mvp1_vertical_slice import (
    Mvp1SyntheticCaseReview,
    synthetic_ny_mvp1_case_review,
)
from unclaimed_platform.domain.ny_mvp1_case_economics_integration import (
    NyMvp1CaseEconomicsIntegrationInput,
    NyMvp1CaseEconomicsIntegrationResult,
    integrate_follow_up_cost_with_case_economics,
)
from unclaimed_platform.domain.ny_mvp1_follow_up_cost import (
    DocumentedHumanLaborRate,
    MeasuredCostComponent,
    MeasuredDurationComponent,
    NyMvp1FollowUpCostMeasurementInput,
    NyMvp1FollowUpCostMeasurementResult,
    measure_follow_up_cost,
)
from unclaimed_platform.domain.ny_mvp1_value_evidence import (
    NyMvp1PrecontactEconomicsEvidence,
    ny_mvp1_precontact_economics_evidence,
)

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

    supabase: Literal["NOT_CONNECTED"]


class OperationsSnapshot(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["2.0.0"]
    mode: Literal["SYNTHETIC_READ_ONLY"]
    milestones: list[MilestoneStatus]
    source_registry: SourceRegistryStatus
    raw_artifact: RawArtifactSummary
    governance: GovernanceStatus
    audit: AuditStatus
    platform: PlatformReadiness



class Mvp1IntegratedEconomicsSafety(BaseModel):
    model_config = ConfigDict(frozen=True)

    real_source_accessed: Literal[False]
    owner_file_downloaded: Literal[False]
    real_owner_pii_processed: Literal[False]
    automatic_commercial_recommendation: Literal[False]


class Mvp1IntegratedEconomicsScenario(BaseModel):
    model_config = ConfigDict(frozen=True)

    scenario: Literal[
        "READY_WITH_DOCUMENTED_LABOR_RATE",
        "BLOCKED_WITHOUT_DOCUMENTED_LABOR_RATE",
    ]
    follow_up_cost: NyMvp1FollowUpCostMeasurementResult
    integration: NyMvp1CaseEconomicsIntegrationResult


class Mvp1IntegratedEconomicsReviewerSnapshot(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"]
    mode: Literal["SYNTHETIC_READ_ONLY"]
    ready: Mvp1IntegratedEconomicsScenario
    blocked: Mvp1IntegratedEconomicsScenario
    safety: Mvp1IntegratedEconomicsSafety


def _synthetic_follow_up_cost(
    *,
    with_labor_rate: bool,
    measurement_id: UUID,
) -> NyMvp1FollowUpCostMeasurementResult:
    observed_at = datetime(2026, 9, 18, 10, 0, tzinfo=UTC)
    scenario_key = "ready" if with_labor_rate else "blocked"

    labor_rate = None
    if with_labor_rate:
        labor_rate = DocumentedHumanLaborRate(
            cents_per_hour=7200,
            currency="USD",
            evidence_ref="synthetic:reviewer:ready:labor-rate",
            observed_at=observed_at,
        )

    measured = NyMvp1FollowUpCostMeasurementInput(
        mode="SYNTHETIC_TEST",
        measurement_id=measurement_id,
        candidate_case_id=UUID("22222222-2222-4222-8222-222222222222"),
        owner_pii_included=False,
        automated_processing=MeasuredCostComponent(
            amount_cents=37,
            currency="USD",
            measurement_method="SYSTEM_METERED",
            allocation_basis="PER_CANDIDATE_DIRECT",
            evidence_ref=f"synthetic:reviewer:{scenario_key}:automation-meter",
            observed_at=observed_at,
        ),
        source_data=MeasuredCostComponent(
            amount_cents=0,
            currency="USD",
            measurement_method="ZERO_DIRECT_COST_DOCUMENTED",
            allocation_basis="ZERO_DIRECT_COST_PER_CANDIDATE",
            evidence_ref=f"synthetic:reviewer:{scenario_key}:source-cost",
            observed_at=observed_at,
        ),
        human_review=MeasuredDurationComponent(
            duration_seconds=125,
            measurement_method="REVIEWER_TIMER",
            evidence_ref=f"synthetic:reviewer:{scenario_key}:review-timer",
            observed_at=observed_at,
        ),
        manual_research=MeasuredDurationComponent(
            duration_seconds=65,
            measurement_method="MANUAL_TIMER",
            evidence_ref=f"synthetic:reviewer:{scenario_key}:research-timer",
            observed_at=observed_at,
        ),
        human_labor_rate=labor_rate,
    )
    return measure_follow_up_cost(measured)


def synthetic_mvp1_integrated_economics_snapshot(
) -> Mvp1IntegratedEconomicsReviewerSnapshot:
    """Return deterministic ready/blocked synthetic economics reviewer scenarios."""

    economics_input = NyMvp1CaseEconomicsIntegrationInput(
        recoverable_value_cents=1_000_000,
        agreed_fee_bps=1200,
        value_evidence_ref="synthetic:reviewer:value-evidence",
        fee_evidence_ref="synthetic:reviewer:fee-evidence",
        fee_rule_scope_confirmed=True,
    )
    ready_cost = _synthetic_follow_up_cost(
        with_labor_rate=True,
        measurement_id=UUID("33333333-3333-4333-8333-333333333333"),
    )
    blocked_cost = _synthetic_follow_up_cost(
        with_labor_rate=False,
        measurement_id=UUID("44444444-4444-4444-8444-444444444444"),
    )

    return Mvp1IntegratedEconomicsReviewerSnapshot(
        contract_version="1.0.0",
        mode="SYNTHETIC_READ_ONLY",
        ready=Mvp1IntegratedEconomicsScenario(
            scenario="READY_WITH_DOCUMENTED_LABOR_RATE",
            follow_up_cost=ready_cost,
            integration=integrate_follow_up_cost_with_case_economics(
                economics_input,
                ready_cost,
            ),
        ),
        blocked=Mvp1IntegratedEconomicsScenario(
            scenario="BLOCKED_WITHOUT_DOCUMENTED_LABOR_RATE",
            follow_up_cost=blocked_cost,
            integration=integrate_follow_up_cost_with_case_economics(
                economics_input,
                blocked_cost,
            ),
        ),
        safety=Mvp1IntegratedEconomicsSafety(
            real_source_accessed=False,
            owner_file_downloaded=False,
            real_owner_pii_processed=False,
            automatic_commercial_recommendation=False,
        ),
    )

def synthetic_operations_snapshot() -> OperationsSnapshot:
    return OperationsSnapshot(
        contract_version="2.0.0",
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
            supabase="NOT_CONNECTED",
        ),
    )


@router.get("/m3/operations", response_model=OperationsSnapshot)
def get_m3_operations() -> OperationsSnapshot:
    """Return the governed, read-only M3 reviewer snapshot."""
    return synthetic_operations_snapshot()


@router.get("/mvp1/synthetic-case", response_model=Mvp1SyntheticCaseReview)
def get_mvp1_synthetic_case() -> Mvp1SyntheticCaseReview:
    """Return the governed synthetic MVP-1 case-review vertical slice."""
    return synthetic_ny_mvp1_case_review()


@router.get(
    "/mvp1/economics/precontact",
    response_model=NyMvp1PrecontactEconomicsEvidence,
)
def get_mvp1_precontact_economics() -> NyMvp1PrecontactEconomicsEvidence:
    """Return the fail-closed NY MVP-1 pre-contact economics evidence state."""
    return ny_mvp1_precontact_economics_evidence()


@router.get(
    "/mvp1/economics/integrated",
    response_model=Mvp1IntegratedEconomicsReviewerSnapshot,
)
def get_mvp1_integrated_economics() -> Mvp1IntegratedEconomicsReviewerSnapshot:
    """Return ready and blocked synthetic integrated-economics reviewer states."""
    return synthetic_mvp1_integrated_economics_snapshot()
