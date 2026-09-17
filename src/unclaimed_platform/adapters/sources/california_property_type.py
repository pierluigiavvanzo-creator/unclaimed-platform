from __future__ import annotations

import re
from dataclasses import dataclass
from enum import StrEnum

PROPERTY_TYPE_RE = re.compile(r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$")

CA_INSURANCE_CODES: dict[str, str] = {
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

MVP1_PRIMARY_PROPERTY_TYPE = "IN03"


class PropertyTypeDisposition(StrEnum):
    INSURANCE = "INSURANCE"
    SHAPE_VALID_NON_TARGET = "SHAPE_VALID_NON_TARGET"
    DEFER_UNCLASSIFIABLE = "DEFER_UNCLASSIFIABLE"


@dataclass(frozen=True)
class PropertyTypeClassification:
    disposition: PropertyTypeDisposition
    authority_description: str | None
    mvp1_primary_target: bool
    continue_source: bool
    persist_source_value: bool = False


def classify_property_type(value: str) -> PropertyTypeClassification:
    """Classify CA SCO PROPERTY_TYPE without modifying source semantics.

    A nonconforming value is not normalized, interpreted as non-insurance, or
    persisted. It is deferred as unclassifiable while source processing may
    continue. Exact authority-backed insurance codes are recognized directly.
    Other shape-valid values remain non-target for this insurance vertical
    slice without claiming that shape alone proves semantic validity.
    """
    if PROPERTY_TYPE_RE.fullmatch(value) is None:
        return PropertyTypeClassification(
            disposition=PropertyTypeDisposition.DEFER_UNCLASSIFIABLE,
            authority_description=None,
            mvp1_primary_target=False,
            continue_source=True,
        )

    description = CA_INSURANCE_CODES.get(value)
    if description is not None:
        return PropertyTypeClassification(
            disposition=PropertyTypeDisposition.INSURANCE,
            authority_description=description,
            mvp1_primary_target=value == MVP1_PRIMARY_PROPERTY_TYPE,
            continue_source=True,
        )

    return PropertyTypeClassification(
        disposition=PropertyTypeDisposition.SHAPE_VALID_NON_TARGET,
        authority_description=None,
        mvp1_primary_target=False,
        continue_source=True,
    )
