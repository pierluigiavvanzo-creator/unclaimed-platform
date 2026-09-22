from __future__ import annotations

from unclaimed_platform.adapters.sources.california_property_type import (
    CA_INSURANCE_CODES,
    MVP1_PRIMARY_PROPERTY_TYPE,
    PropertyTypeDisposition,
    classify_property_type,
)


def test_exact_california_insurance_codes_are_authority_backed() -> None:
    assert CA_INSURANCE_CODES == {
        "IN01": "Individual Policy Benefits or Claim Payments",
        "IN02": "Group Policy Benefits or Claim Payments",
        "IN03": "Proceeds Due Beneficiaries",
        "IN04": "Proceeds from Matured Policies, Endowments, or Annuities",
        "IN05": "Premium Refunds",
        "IN06": "Unidentified Remittances",
        "IN07": "Other Amounts Due Under Policy Terms",
        "IN08": "Agent Credit Balances",
        "IN99": "Aggregate Insurance Property",
    }


def test_in03_is_the_narrow_mvp1_primary_target() -> None:
    result = classify_property_type("IN03")
    assert MVP1_PRIMARY_PROPERTY_TYPE == "IN03"
    assert result.disposition is PropertyTypeDisposition.INSURANCE
    assert result.authority_description == "Proceeds Due Beneficiaries"
    assert result.mvp1_primary_target is True
    assert result.continue_source is True
    assert result.persist_source_value is False


def test_other_authority_backed_insurance_codes_are_insurance_not_primary_target() -> None:
    for code in CA_INSURANCE_CODES.keys() - {"IN03"}:
        result = classify_property_type(code)
        assert result.disposition is PropertyTypeDisposition.INSURANCE
        assert result.authority_description == CA_INSURANCE_CODES[code]
        assert result.mvp1_primary_target is False
        assert result.continue_source is True
        assert result.persist_source_value is False


def test_shape_valid_non_target_does_not_claim_semantic_validity() -> None:
    result = classify_property_type("AC01")
    assert result.disposition is PropertyTypeDisposition.SHAPE_VALID_NON_TARGET
    assert result.authority_description is None
    assert result.mvp1_primary_target is False
    assert result.continue_source is True
    assert result.persist_source_value is False


def test_nonconforming_value_is_deferred_without_normalization_or_noninsurance_inference() -> None:
    for value in ("", "IN3", "in03", " IN03", "IN03 ", "????", "ABCDE"):
        result = classify_property_type(value)
        assert result.disposition is PropertyTypeDisposition.DEFER_UNCLASSIFIABLE
        assert result.authority_description is None
        assert result.mvp1_primary_target is False
        assert result.continue_source is True
        assert result.persist_source_value is False


def test_unknown_shape_valid_insurance_prefix_is_deferred_not_misclassified() -> None:
    result = classify_property_type("IN10")
    assert result.disposition is PropertyTypeDisposition.DEFER_UNCLASSIFIABLE
    assert result.authority_description is None
    assert result.mvp1_primary_target is False
    assert result.continue_source is True
    assert result.persist_source_value is False
