# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical promoted HEAD: `9c2f5b6c82ed787bf0820bdd850e475775fc097c`
- Canonical post-promotion CI: `34940817455` — SUCCESS
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` — unchanged
- Never develop directly on `main`.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition/raw persistence/privacy CANONICAL + VERIFIED.
- Streamlit reviewer CANONICAL + CI VERIFIED.
- SCO source governance CANONICAL + CI VERIFIED.
- SCO transport/source-approval/data-scope readiness CANONICAL + CI VERIFIED.
- SCO segmented transport evidence CANONICAL + CI VERIFIED.
- SCO `$500+` bounded structure inspection EXECUTED + CANONICAL + CI VERIFIED.
- SCO revised two-field field/privacy readiness CANONICAL + CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical `$500+` Structure Evidence

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Prior owner-authorized structure-only run:
`34864433849` — SUCCESS.

Observed:
- four non-encrypted DEFLATED CSV members;
- identical 25-label header candidate;
- 5 HTTP `206` Range responses;
- total source-body bytes `393,216`;
- full archive downloaded false;
- CSV data rows parsed `0`;
- record values persisted false.

No real data row has yet been sampled.

## Canonical Product Purpose / Field Boundary

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Canonical proposed persisted/allowed scope:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

Optional fields: none.

`HOLDER_NAME` is prohibited for this first purpose.

## Why HOLDER_NAME Was Removed

Official California SCO/NAUPA documentation defines insurance property codes:

- `IN01` Individual Policy Benefits or Claim Payments
- `IN02` Group Policy Benefits or Claim Payments
- `IN03` Proceeds Due Beneficiaries
- `IN04` Proceeds from Matured Policies, Endowments or Annuities
- `IN05` Premium Refunds
- `IN06` Unidentified Remittances
- `IN07` Other Amounts Due Under Policy Terms
- `IN08` Agent Credit Balances
- `IN99` Aggregate Insurance Property

Authority reference:
`https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`.

Holder identity is therefore not justified merely to determine insurance relevance. However, the actual bulk CSV `PROPERTY_TYPE` row values remain unverified because no data row has been sampled. Do not assume production compatibility with these codes until a separately authorized bounded semantic check confirms it.

## Field Partition

Required:
- `PROPERTY_ID`
- `PROPERTY_TYPE`

Prohibited:
- `OWNER_NAME`;
- all owner street/geography fields;
- `HOLDER_NAME`;
- all holder street/geography fields.

Unresolved/not allowlisted:
- `CASH_REPORTED`;
- `SHARES_REPORTED`;
- `NAME_OF_SECURITIES_REPORTED`;
- `NO_OF_OWNERS`;
- `CURRENT_CASH_BALANCE`;
- `NUMBER_OF_PENDING_CLAIMS`;
- `NUMBER_OF_PAID_CLAIMS`;
- `CUSIP`.

All 25 verified labels are partitioned exactly once by contract test.

## Critical Transport / Privacy Boundary

The verified source members are CSV. No server-side column projection capability has been established.

Reading a future real row may therefore transiently expose bytes from prohibited owner/holder columns before local projection discards them. Persisted-field minimization alone does not eliminate transient source-row processing.

Canonical controls:
- server-side column projection status `NOT_ESTABLISHED`;
- transient nonallowlisted bytes may be observed: true;
- use of nonallowlisted values: false;
- persistence of nonallowlisted values: false;
- raw ZIP persistence: false;
- full-row persistence: false;
- row access authorized: false;
- separate transient-row privacy approval required before any real row access.

## PII / Retention Boundary

Actual PII presence remains:
`UNVERIFIED_NO_ROWS_SAMPLED`.

No proposed persisted field is currently in the prior header-heuristic potential-PII list. This does not make real row access PII-free because the same CSV rows contain prohibited identity/address columns.

Retention:
- transient source-row buffer retention `0 days`;
- transient buffer disposal immediate after projection or stop;
- projected two-field triage record retention unresolved;
- approved retention policy ref null.

The earlier seven-day candidate was removed because it lacked a demonstrated production/legal basis.

Privacy candidate remains `DRAFT_NOT_TRUSTED`; trusted privacy-policy ref remains null.

## Promotion Evidence

Before promotion:
- canonical `74af507796f8bcc4ab45baba6abffe6714f9f6c6`;
- candidate `9c2f5b6c82ed787bf0820bdd850e475775fc097c`;
- ahead `16`;
- behind `0`;
- merge-base exactly `74af507796f8bcc4ab45baba6abffe6714f9f6c6`.

Owner explicitly approved the two-field boundary and promotion:
`m3-ca-sco-field-privacy-readiness -> m2-state-governance-core`.

Promotion was a non-force fast-forward to:
`9c2f5b6c82ed787bf0820bdd850e475775fc097c`.

Canonical post-promotion CI:
`34940817455` — SUCCESS for both `quality` and `streamlit-candidate`.

Verified in canonical CI:
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- frontend dependency install/lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

No source approval, registry activation, row-level acquisition, PII processing, identity resolution, matching or outreach was authorized by promotion.

## Canonical Authorization State — UNCHANGED

SCO source policy remains:
- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `privacy_policy_ref: null`;
- `retention_policy_ref: null`;
- `authorized_processing_purposes: []`;
- `allowed_fields: []`;
- `allow_pii: false`.

Registry remains:
- `enabled: false`;
- `approved_for_use: false`.

Approved real sources: `0`.

Real row access, real PII processing, identity resolution, beneficiary matching and outreach remain BLOCKED.

## Remaining Blocking Items

Before any real row access/acquisition:

1. production retention policy approved;
2. trusted project privacy policy approved;
3. transient full-row privacy review completed;
4. bounded `PROPERTY_TYPE` semantic-verification plan approved;
5. real-acquisition client reviewed;
6. source approval reference assigned;
7. source policy approved under separate gate;
8. registry enabled under separate gate.

## SINGLE NEXT ACTION

Create an isolated, non-authorizing **`PROPERTY_TYPE` semantic-verification proposal**.

Requirements:
1. no real row access while preparing the proposal;
2. no new SCO network/body access while preparing the proposal;
3. define the exact semantic compatibility question;
4. define explicit row, request and byte caps before any future execution;
5. define transient-buffer handling and immediate disposal;
6. prohibit raw ZIP/full-row persistence;
7. prohibit use/persistence of nonallowlisted values;
8. define deterministic stop conditions for malformed/unexpected rows, transport drift, privacy ambiguity or cap exhaustion;
9. remain non-executable and non-authorizing until a separate owner gate.

After proposal CI, stop at a separate human execution gate before reading any data row.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
M3 SCO two-field field/privacy boundary: CANONICAL + CI VERIFIED
Canonical promoted SHA: 9c2f5b6c82ed787bf0820bdd850e475775fc097c
Canonical promotion CI: 34940817455 SUCCESS
Purpose: INSURANCE_RELEVANCE_TRIAGE_ONLY
Proposed persisted fields: PROPERTY_ID, PROPERTY_TYPE
HOLDER_NAME: PROHIBITED FOR FIRST TRIAGE
Transient CSV prohibited-field exposure: POSSIBLE / SEPARATELY GATED
Projected retention duration: UNRESOLVED
Transient row buffer retention: 0 DAYS / IMMEDIATE DISPOSAL
Real acquisition: BLOCKED
Real row access: BLOCKED
Real PII: BLOCKED
Identity resolution: BLOCKED
Beneficiary matching: BLOCKED
Outreach: BLOCKED
SCO policy: PROPOSED
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
New SCO network/body access during promotion: 0
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: design-only PROPERTY_TYPE semantic-verification proposal
CONTEXT HEALTH: coherent; repository is source of truth
```
