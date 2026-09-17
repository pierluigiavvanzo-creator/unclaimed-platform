# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ca-property-type-authority-row-defer`

Latest completed product action:

`IMPLEMENT_CA_SCO_AUTHORITY_BACKED_PROPERTY_TYPE_ROW_DEFER_FOR_MVP1`

Classification: `A — Product Critical`.

Audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_AUTHORITY_BACKED_MVP1_REMEDIATION.md`

## Evidence Review Result

The last authorized real-source execution confirmed the adopted transport/archive baseline and reached the canonical `PROPERTY_TYPE` field, where the old D-008 policy stopped on `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Earlier diagnostic evidence already proves that the examined row is valid strict UTF-8 / strict CSV with 25 columns and that stdlib column index `1` agrees with the custom projector. Transport and parser disagreement are therefore not active blockers.

## Authority-Backed Semantics

California SCO authority provenance is resolved.

Exact insurance codes:

- `IN01` — Individual Policy Benefits or Claim Payments;
- `IN02` — Group Policy Benefits or Claim Payments;
- `IN03` — Proceeds Due Beneficiaries;
- `IN04` — Proceeds from Matured Policies, Endowments, or Annuities;
- `IN05` — Premium Refunds;
- `IN06` — Unidentified Remittances;
- `IN07` — Other Amounts Due Under Policy Terms;
- `IN08` — Agent Credit Balances;
- `IN99` — Aggregate Insurance Property.

The authority does not justify normalizing or reconstructing a malformed value.

## D-010 Product Policy

D-010 supersedes D-008 only for the California SCO MVP-1 classification continuation path.

Nonconforming `PROPERTY_TYPE` behavior:

`DEFER_UNCLASSIFIABLE -> aggregate count -> continue later rows`

The row is not normalized, repaired, persisted, treated as non-insurance, silently omitted or routed to row-specific inspection.

Unknown `INxx` values outside the exact authority vocabulary are also deferred.

Transport/header/CSV-column/hard-cap failures remain whole-source fail-closed.

## MVP-1 Target

Primary high-precision target:

`IN03 — Proceeds Due Beneficiaries`

All nine exact California insurance codes remain insurance-valid. `IN03` is only the first commercial slice; this does not downgrade the other insurance codes.

## Implementation State

Implemented offline:

- `policies/states/CA/ca_sco_property_type_classification.v1.json`;
- `src/unclaimed_platform/adapters/sources/california_property_type.py`;
- `scripts/ca_sco_mvp1_property_type_validation.py`;
- unit and contract tests for authority vocabulary, unknown-`INxx` defer, row-defer continuation and fail-closed transport behavior.

Historical runner `scripts/ca_sco_property_type_semantic_verification.py` remains unchanged as evidence/provenance.

No California source request was performed by this remediation.

## Product / Commercial State

- transport/archive baseline: **CONFIRMED LIVE**;
- authority vocabulary: **RESOLVED**;
- D-008 whole-source product blocker: **SUPERSEDED BY D-010 FOR MVP-1 PATH**;
- row-defer classifier: **IMPLEMENTED OFFLINE**;
- bounded live row-defer validation: **NOT YET AUTHORIZED**;
- approved real sources: `0`;
- real MVP-1 candidate cases: `0`.

All previous execution/privacy approvals remain `CONSUMED_SINGLE_USE_NON_REUSABLE`.

## SINGLE NEXT ACTION

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION`

Grant exactly one fresh bounded execution approval and one fresh transient-row memory-only privacy approval for `scripts/ca_sco_mvp1_property_type_validation.py`.

After explicit authorization:

`one bounded live validation -> source decision -> if PASS, activate bounded CA insurance path -> candidate/economics/reviewer`

Do not reopen transport or generic PROPERTY_TYPE diagnostics absent new contradictory evidence.
