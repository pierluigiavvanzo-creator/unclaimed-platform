"""Synthetic MVP-1 vertical slice for New York pre-real-source product validation."""

from __future__ import annotations

from typing import Literal
from uuid import NAMESPACE_URL, uuid5

from pydantic import BaseModel, ConfigDict

NY_OSC_SOURCE_ID = "ny.osc.unclaimed_funds.owner_name_file"
NY_MVP1_PRIMARY_CODE = "IN03"
NY_INSURANCE_CODES: dict[str, str] = {
    "IN01": "Individual Policy Benefits or Claim Payments",
    "IN02": "Group Policy Benefits or Claim Payments",
    "IN03": "Proceeds Due Beneficiaries",
    "IN04": "Proceeds from Matured Policies, Endowments or Annuities",
    "IN05": "Premium Refunds",
    "IN06": "Unidentified Remittances",
    "IN07": "Other Amounts Due Under Policy Terms",
    "IN12": "Retained Asset, Benefit Access or Similar Distribution Accounts",
    "IN77": "Limiting Age (superannuated) contracts",
}


class SyntheticPostSchemaRecord(BaseModel):
    """Synthetic semantic record positioned after a hypothetical schema-mapping boundary."""

    model_config = ConfigDict(frozen=True)

    data_mode: Literal["SYNTHETIC_POST_SCHEMA_MAPPING"] = "SYNTHETIC_POST_SCHEMA_MAPPING"
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OSC_SOURCE_ID
    jurisdiction: Literal["NY"] = "NY"
    synthetic_record_ref: str
    synthetic_owner_ref: str
    nature_of_property: str
    reported_by: str
    reported_when: str
    recoverable_value_state: Literal["UNKNOWN_FROM_SOURCE"] = "UNKNOWN_FROM_SOURCE"


class InsuranceClassification(BaseModel):
    model_config = ConfigDict(frozen=True)

    status: Literal[
        "MVP1_PRIMARY_INSURANCE",
        "INSURANCE_OTHER",
        "NO_AUTHORITY_BACKED_INSURANCE_MATCH",
    ]
    authority_code: str | None
    authority_description: str | None
    primary_target: bool
    reason_code: str


class CandidateCaseSummary(BaseModel):
    model_config = ConfigDict(frozen=True)

    status: Literal["CREATED", "NOT_CREATED"]
    case_id: str | None
    lifecycle_state: Literal["SYNTHETIC_REVIEW_READY", "NOT_CREATED"]
    source_record_ref: str
    owner_reference: str
    reason_code: str
    identity_resolution_performed: Literal[False] = False
    beneficiary_matching_performed: Literal[False] = False


class EconomicAssessment(BaseModel):
    model_config = ConfigDict(frozen=True)

    recoverable_value_state: Literal["UNKNOWN_FROM_SOURCE"] = "UNKNOWN_FROM_SOURCE"
    source_amount_available: Literal[False] = False
    fee_basis_state: Literal["NOT_COMPUTABLE_FROM_SOURCE"] = "NOT_COMPUTABLE_FROM_SOURCE"
    economic_actionability: Literal["VALUE_EVIDENCE_REQUIRED"] = "VALUE_EVIDENCE_REQUIRED"
    commercial_threshold_applied: Literal[False] = False
    invented_amounts: Literal[False] = False
    required_next_evidence: list[str]


class ProvenanceSummary(BaseModel):
    model_config = ConfigDict(frozen=True)

    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OSC_SOURCE_ID
    authority: Literal[
        "New York State Office of the State Comptroller, Office of Unclaimed Funds"
    ] = "New York State Office of the State Comptroller, Office of Unclaimed Funds"
    source_contract_ref: Literal[
        "policies/states/NY/ny_osc_owner_name_file.v1.json"
    ] = "policies/states/NY/ny_osc_owner_name_file.v1.json"
    input_boundary: Literal["SYNTHETIC_POST_SCHEMA_MAPPING"] = (
        "SYNTHETIC_POST_SCHEMA_MAPPING"
    )
    synthetic_fixture: Literal[True] = True
    real_source_accessed: Literal[False] = False


class SafetySummary(BaseModel):
    model_config = ConfigDict(frozen=True)

    owner_file_downloaded: Literal[False] = False
    real_owner_pii_processed: Literal[False] = False
    identity_resolution_performed: Literal[False] = False
    beneficiary_matching_performed: Literal[False] = False
    outreach_performed: Literal[False] = False
    representation_performed: Literal[False] = False
    claim_activity_performed: Literal[False] = False


class Mvp1SyntheticCaseReview(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_READ_ONLY"] = "SYNTHETIC_READ_ONLY"
    source_state: Literal["REGISTERED_CANDIDATE_UNAPPROVED_NOT_ACQUIRED"] = (
        "REGISTERED_CANDIDATE_UNAPPROVED_NOT_ACQUIRED"
    )
    classification: InsuranceClassification
    candidate: CandidateCaseSummary
    economics: EconomicAssessment
    provenance: ProvenanceSummary
    safety: SafetySummary
    reviewer_decision_required: Literal["CONTINUE_VALUE_RESEARCH_OR_STOP"] = (
        "CONTINUE_VALUE_RESEARCH_OR_STOP"
    )


def classify_ny_semantic_record(record: SyntheticPostSchemaRecord) -> InsuranceClassification:
    """Classify exact authority-backed insurance codes without normalization or inference."""
    description = NY_INSURANCE_CODES.get(record.nature_of_property)
    if description is None:
        return InsuranceClassification(
            status="NO_AUTHORITY_BACKED_INSURANCE_MATCH",
            authority_code=None,
            authority_description=None,
            primary_target=False,
            reason_code="EXACT_CODE_NOT_IN_NY_INSURANCE_VOCABULARY",
        )

    if record.nature_of_property == NY_MVP1_PRIMARY_CODE:
        return InsuranceClassification(
            status="MVP1_PRIMARY_INSURANCE",
            authority_code=record.nature_of_property,
            authority_description=description,
            primary_target=True,
            reason_code="EXACT_AUTHORITY_BACKED_IN03_MATCH",
        )

    return InsuranceClassification(
        status="INSURANCE_OTHER",
        authority_code=record.nature_of_property,
        authority_description=description,
        primary_target=False,
        reason_code="EXACT_AUTHORITY_BACKED_INSURANCE_NON_PRIMARY",
    )


def build_mvp1_candidate(
    record: SyntheticPostSchemaRecord,
    classification: InsuranceClassification,
) -> CandidateCaseSummary:
    """Create a deterministic synthetic case only for the narrow IN03 MVP-1 target."""
    if not classification.primary_target:
        return CandidateCaseSummary(
            status="NOT_CREATED",
            case_id=None,
            lifecycle_state="NOT_CREATED",
            source_record_ref=record.synthetic_record_ref,
            owner_reference=record.synthetic_owner_ref,
            reason_code="MVP1_PRIMARY_TARGET_REQUIRED",
        )

    case_id = str(
        uuid5(
            NAMESPACE_URL,
            f"{record.source_id}:{record.synthetic_record_ref}:mvp1-synthetic-case",
        )
    )
    return CandidateCaseSummary(
        status="CREATED",
        case_id=case_id,
        lifecycle_state="SYNTHETIC_REVIEW_READY",
        source_record_ref=record.synthetic_record_ref,
        owner_reference=record.synthetic_owner_ref,
        reason_code="PRIMARY_IN03_MATCH",
    )


def assess_candidate_economics(candidate: CandidateCaseSummary) -> EconomicAssessment:
    """Expose the current economic blocker without inventing a value or fee basis."""
    if candidate.status != "CREATED":
        raise ValueError("economic assessment requires a created MVP-1 candidate")

    return EconomicAssessment(
        required_next_evidence=[
            "recoverable_value_evidence",
            "expected_follow_up_cost",
            "lawful_fee_basis",
        ]
    )


def synthetic_ny_mvp1_case_review() -> Mvp1SyntheticCaseReview:
    """Return one deterministic synthetic case traversing classification to reviewer."""
    record = SyntheticPostSchemaRecord(
        synthetic_record_ref="synthetic-ny-in03-001",
        synthetic_owner_ref="synthetic-owner-001",
        nature_of_property="IN03",
        reported_by="SYNTHETIC_LIFE_INSURER",
        reported_when="SYNTHETIC_QUARTER",
    )
    classification = classify_ny_semantic_record(record)
    candidate = build_mvp1_candidate(record, classification)
    economics = assess_candidate_economics(candidate)

    return Mvp1SyntheticCaseReview(
        classification=classification,
        candidate=candidate,
        economics=economics,
        provenance=ProvenanceSummary(),
        safety=SafetySummary(),
    )
