# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ca-property-type-authority-row-defer`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Latest Product-Critical Result

The prior one-shot v1.2 live execution confirmed the adopted CA SCO transport/archive baseline but stopped on a canonical field-level `PROPERTY_TYPE_FORMAT_UNEXPECTED` under D-008.

Earlier source-format diagnostics already proved this was not parser/projector disagreement: strict UTF-8 and strict stdlib CSV parsing succeeded, a canonical 25-column row was produced, and stdlib field index `1` agreed with the custom projector.

The Product Owner then directed:

`risolvere Property_Type usando semantica/documentazione ufficiale california e procedere verso MVP-1`

## California Authority Result

California SCO authority now provides the product boundary:

- `IN01` — Individual Policy Benefits or Claim Payments;
- `IN02` — Group Policy Benefits or Claim Payments;
- `IN03` — Proceeds Due Beneficiaries;
- `IN04` — Proceeds from Matured Policies, Endowments, or Annuities;
- `IN05` — Premium Refunds;
- `IN06` — Unidentified Remittances;
- `IN07` — Other Amounts Due Under Policy Terms;
- `IN08` — Agent Credit Balances;
- `IN99` — Aggregate Insurance Property.

Authority archive:

`sources/authority/ca/sco/upd_naupa_ii_codes_dormancy_periods/7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5.pdf`

Authority review:

`sources/evidence/ca_sco_segment_500_plus.property_type_authority_archive_provenance.review.v1.json`

The authority does not justify normalizing, trimming, uppercasing, repairing or reconstructing a malformed source value.

## D-010 — MVP-1 Row Defer

Accepted decision:

`ROW_DEFER_CONTINUE_METADATA_ONLY`

D-010 supersedes D-008 whole-source continuation behavior only for the California SCO MVP-1 classification path.

A nonconforming or unknown `INxx` value is:

- `DEFER_UNCLASSIFIABLE`;
- not normalized;
- not classified as non-insurance;
- not persisted;
- represented only by aggregate `nonconforming_rows_deferred_count`;
- allowed to defer while later rows continue.

Transport/header/CSV-column/hard-cap failures remain whole-source fail-closed.

## MVP-1 Commercial Target

Primary narrow target:

`IN03 — Proceeds Due Beneficiaries`

This is the first high-precision commercial slice. All nine exact authority-backed `INxx` codes remain valid insurance codes.

## Implementation

Added on branch:

- `policies/states/CA/ca_sco_property_type_classification.v1.json`;
- `src/unclaimed_platform/adapters/sources/california_property_type.py`;
- `scripts/ca_sco_mvp1_property_type_validation.py`;
- `tests/unit/test_california_property_type.py`;
- `tests/unit/test_ca_sco_mvp1_property_type_validation.py`;
- `tests/contract/test_ca_sco_property_type_classification_policy.py`;
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_AUTHORITY_BACKED_MVP1_REMEDIATION.md`.

The historical v1.2 semantic runner is unchanged.

Synthetic tests prove that a malformed first row can be deferred while a later `IN03` is observed, unknown `INxx` is deferred, and transport drift still stops fail-closed.

## Network / Privacy State

This remediation performed no new California SCO source request.

All previous execution/privacy refs remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No current fresh validation approval exists.

## Product State

- live transport baseline: CONFIRMED;
- authority semantics: RESOLVED;
- exact insurance vocabulary: RESOLVED;
- D-010 row-defer implementation: OFFLINE READY;
- D-010 live validation: NOT YET AUTHORIZED;
- approved real sources: `0`;
- candidate cases: `0`.

## Canonical Read Order

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_AUTHORITY_BACKED_MVP1_REMEDIATION.md`;
2. `policies/states/CA/ca_sco_property_type_classification.v1.json`;
3. `src/unclaimed_platform/adapters/sources/california_property_type.py`;
4. `scripts/ca_sco_mvp1_property_type_validation.py`;
5. the latest consumed v1.2 execution audit/evidence;
6. D-010 in `DECISIONS.md`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION`

Classification: `A — Product Critical`.

It may mint exactly:

1. one fresh single-use bounded execution approval for `scripts/ca_sco_mvp1_property_type_validation.py`;
2. one fresh single-use transient-row memory-only privacy approval.

It must preserve:

- adopted transport baseline and current request/byte caps;
- no retry / no widening;
- exact authority insurance vocabulary;
- no normalization or regex relaxation;
- metadata-only deferred-row aggregate count;
- no malformed source value or row/PII persistence.

After explicit authorization, proceed directly:

`one bounded live D-010 validation -> source decision -> if PASS, bounded California insurance activation -> MVP-1 candidate -> economics -> reviewer`

Do not reopen transport or generic PROPERTY_TYPE diagnostics absent new contradictory evidence.
