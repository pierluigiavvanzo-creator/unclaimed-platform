# M3 California SCO — Authority-Backed PROPERTY_TYPE MVP-1 Remediation

Date: 2026-09-17

Status: **IMPLEMENTED OFFLINE — D-010 ACCEPTED — ROW-DEFER VALIDATOR READY — REAL-SOURCE VALIDATION NOT YET AUTHORIZED**

## Classification

`A — Product Critical`

## Product objective

Remove the semantic `PROPERTY_TYPE` blocker without inventing source semantics, then move directly toward:

`approved real source -> insurance classification -> candidate -> economics -> reviewer`

## Evidence review conclusion

The latest adopted-baseline one-shot execution confirmed the live transport/archive baseline and reached:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- D-008 control status `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- D-008 reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

Earlier source-format evidence already established for the examined row that strict UTF-8 decoding and strict stdlib CSV parsing succeed, the canonical 25-column record is produced, and stdlib index `1` agrees with the custom projector. The unresolved condition is therefore a canonical-field semantic/structural nonconformance, not a transport or parser disagreement.

## California authority basis

The immutable archived California SCO authority:

`sources/authority/ca/sco/upd_naupa_ii_codes_dormancy_periods/7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5.pdf`

and current California SCO reporting material establish the exact California insurance property vocabulary:

- `IN01` — Individual Policy Benefits or Claim Payments;
- `IN02` — Group Policy Benefits or Claim Payments;
- `IN03` — Proceeds Due Beneficiaries;
- `IN04` — Proceeds from Matured Policies, Endowments, or Annuities;
- `IN05` — Premium Refunds;
- `IN06` — Unidentified Remittances;
- `IN07` — Other Amounts Due Under Policy Terms;
- `IN08` — Agent Credit Balances;
- `IN99` — Aggregate Insurance Property.

The authority does **not** justify trimming, case conversion, normalization, regex relaxation or semantic reconstruction of the nonconforming value.

## Decision

`D-010 — Authority-backed row defer for California SCO MVP-1 PROPERTY_TYPE classification`

For the California SCO MVP-1 product path, a nonconforming `PROPERTY_TYPE` is now:

- `DEFER_UNCLASSIFIABLE`;
- not normalized or repaired;
- not inferred to be non-insurance;
- not persisted;
- represented only by aggregate `nonconforming_rows_deferred_count` completeness evidence;
- allowed to coexist with continuation to later rows.

Unknown shape-valid `INxx` values not present in the exact authority vocabulary are also deferred rather than treated as non-insurance.

Transport, malformed CSV/header/column shape and hard-cap failures remain fail-closed source stops.

## MVP-1 target

`IN03` is the first narrow product target because the California authority description is exactly `Proceeds Due Beneficiaries`.

This is a high-precision product targeting rule, not a modification of California semantics. The other eight authority-backed insurance codes remain classified as insurance and may support later product expansion.

## Implementation

Added:

- `policies/states/CA/ca_sco_property_type_classification.v1.json`;
- `src/unclaimed_platform/adapters/sources/california_property_type.py`;
- `scripts/ca_sco_mvp1_property_type_validation.py`;
- `tests/unit/test_california_property_type.py`;
- `tests/unit/test_ca_sco_mvp1_property_type_validation.py`;
- `tests/contract/test_ca_sco_property_type_classification_policy.py`.

The historical v1.2 semantic diagnostic runner remains unchanged and preserved as evidence.

## Synthetic proof

The new validator proves offline that:

1. a nonconforming first sampled row is deferred rather than terminating the source;
2. a later exact `IN03` row is still detected;
3. exact authority-backed insurance codes are classified as insurance;
4. unknown `INxx` values are deferred;
5. shape-valid non-`IN` values remain non-target without claiming semantic authority;
6. transport metadata drift remains fail-closed;
7. no real source value is persisted by the classifier.

## Privacy / completeness boundary

No privacy expansion is introduced by the offline implementation.

The new persisted completeness metadata is aggregate only:

`nonconforming_rows_deferred_count`

No exact malformed `PROPERTY_TYPE`, derivative, row content, `PROPERTY_ID`, owner/holder data, hash, exact length or source-derived free text is permitted by D-010.

## Network / authorization state

This remediation performs no California SCO request.

All previous real-source execution/privacy approvals remain consumed and non-reusable.

A fresh single-use execution approval and fresh transient-row memory-only privacy approval are required before validating D-010 against the live source.

## Commercial effect

This removes the design-level whole-source-stop blocker. If one bounded live validation confirms that nonconforming rows can be deferred while exact California insurance codes are observed, the next product decision should be source activation for the bounded insurance path and immediate transition to MVP-1 candidate generation rather than further PROPERTY_TYPE diagnostics.

## Next single action

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION`

After explicit fresh single-use execution + transient-row privacy authorization, execute exactly one bounded validation using `scripts/ca_sco_mvp1_property_type_validation.py`, preserve only the aggregate/authority-code evidence described above, and proceed directly to source decision.
