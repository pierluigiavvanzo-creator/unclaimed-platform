import pytest

from unclaimed_platform.domain.mvp1_vertical_slice import (
    CandidateCaseSummary,
    SyntheticPostSchemaRecord,
    assess_candidate_economics,
    build_mvp1_candidate,
    classify_ny_semantic_record,
    synthetic_ny_mvp1_case_review,
)


def _record(code: str) -> SyntheticPostSchemaRecord:
    return SyntheticPostSchemaRecord(
        synthetic_record_ref=f"synthetic-{code}",
        synthetic_owner_ref="synthetic-owner",
        nature_of_property=code,
        reported_by="SYNTHETIC_REPORTER",
        reported_when="SYNTHETIC_PERIOD",
    )


def test_exact_in03_is_primary_mvp1_insurance() -> None:
    result = classify_ny_semantic_record(_record("IN03"))

    assert result.status == "MVP1_PRIMARY_INSURANCE"
    assert result.authority_code == "IN03"
    assert result.authority_description == "Proceeds Due Beneficiaries"
    assert result.primary_target is True


def test_other_exact_insurance_code_does_not_create_primary_candidate() -> None:
    record = _record("IN01")
    classification = classify_ny_semantic_record(record)
    candidate = build_mvp1_candidate(record, classification)

    assert classification.status == "INSURANCE_OTHER"
    assert classification.primary_target is False
    assert candidate.status == "NOT_CREATED"
    assert candidate.case_id is None


def test_unknown_code_is_not_promoted_to_insurance() -> None:
    record = _record("IN99")
    classification = classify_ny_semantic_record(record)
    candidate = build_mvp1_candidate(record, classification)

    assert classification.status == "NO_AUTHORITY_BACKED_INSURANCE_MATCH"
    assert classification.authority_code is None
    assert candidate.status == "NOT_CREATED"


def test_synthetic_case_is_deterministic_and_keeps_economics_unknown() -> None:
    first = synthetic_ny_mvp1_case_review()
    second = synthetic_ny_mvp1_case_review()

    assert first.candidate.case_id == second.candidate.case_id
    assert first.candidate.status == "CREATED"
    assert first.economics.recoverable_value_state == "UNKNOWN_FROM_SOURCE"
    assert first.economics.fee_basis_state == "NOT_COMPUTABLE_FROM_SOURCE"
    assert first.economics.invented_amounts is False
    assert first.economics.commercial_threshold_applied is False
    assert first.provenance.real_source_accessed is False
    assert first.safety.real_owner_pii_processed is False


def test_economics_rejects_non_created_candidate() -> None:
    candidate = CandidateCaseSummary(
        status="NOT_CREATED",
        case_id=None,
        lifecycle_state="NOT_CREATED",
        source_record_ref="synthetic-non-candidate",
        owner_reference="synthetic-owner",
        reason_code="MVP1_PRIMARY_TARGET_REQUIRED",
    )

    with pytest.raises(ValueError, match="created MVP-1 candidate"):
        assess_candidate_economics(candidate)
