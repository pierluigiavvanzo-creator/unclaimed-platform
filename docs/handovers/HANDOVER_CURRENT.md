# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical development HEAD before current candidate: `74af507796f8bcc4ab45baba6abffe6714f9f6c6`
- Current candidate: `m3-ca-sco-field-privacy-readiness`
- Functional candidate HEAD: `648b81b973a4b169c14bcdfd76ac4fa71e76f2e9`
- Functional candidate CI: `34939909880` — SUCCESS
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

No data row has yet been sampled.

## Current Candidate — Revised Field / Privacy Readiness

Package remains:
`READINESS_PROPOSAL_NOT_AUTHORIZED`.

Product purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Current proposed persisted/allowed scope:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

Optional fields: none.

`HOLDER_NAME` was removed from the first-purpose allowlist and is now prohibited for this purpose.

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

Therefore holder identity is not justified merely to determine insurance relevance. However, the actual bulk CSV `PROPERTY_TYPE` row values remain unverified because no data row was sampled. Do not assume production compatibility with these codes until a separately authorized bounded semantic check confirms it.

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

All 25 verified labels remain partitioned exactly once by contract test.

## Critical Transport / Privacy Boundary

The verified source members are CSV. No server-side column projection capability has been established.

Therefore reading a real row may transiently expose bytes from prohibited owner/holder columns before a local parser discards them. Persisted-field minimization alone does not eliminate transient source-row processing.

Machine-enforced candidate controls:
- server-side column projection status `NOT_ESTABLISHED`;
- transient nonallowlisted bytes may be observed: true;
- use of nonallowlisted values: false;
- persistence of nonallowlisted values: false;
- full-row persistence: false;
- row access authorized: false;
- separate transient-row privacy approval required before any real row access.

## PII Boundary

Actual PII presence remains:
`UNVERIFIED_NO_ROWS_SAMPLED`.

No proposed persisted field is currently in the prior header-heuristic potential-PII list. This does not make real row access PII-free because the same CSV rows contain prohibited identity/address columns.

Real PII processing remains unauthorized.

## Privacy / Legal Review References

- CCPA statute: `https://cppa.ca.gov/regulations/pdf/20260101_ccpa_statute.pdf`
- CPPA data-broker guidance: `https://cppa.ca.gov/data_brokers/`

The CCPA statute excludes information lawfully made available from government records from its definition of personal information. That fact does not by itself decide project applicability, data-broker status, other laws, downstream enrichment or permissible commercial use. The package records `HUMAN_COUNSEL_REQUIRED`; no LLM legal approval is claimed.

## Retention Candidate

The earlier seven-day candidate was removed because it lacked a demonstrated production/legal basis.

Current candidate:
- raw archive persistence false;
- full-row persistence false;
- transient source-row buffer retention `0 days`;
- transient buffer disposal immediate after projection or stop;
- projected two-field triage record retention: unresolved;
- approved retention policy ref: null.

No production duration is invented.

## Privacy Candidate

Status:
`DRAFT_NOT_TRUSTED`.

Candidate allowed fields:
- `PROPERTY_ID`
- `PROPERTY_TYPE`.

Encryption at rest, least privilege and access logging are required. Record values in logs, export, identity resolution, beneficiary matching and outreach remain prohibited. Trusted policy ref remains null.

## Future Semantic Verification

A future non-executable stage is defined for `PROPERTY_TYPE` only:

Goal:
`VERIFY_BULK_PROPERTY_TYPE_VALUES_COMPATIBLE_WITH_OFFICIAL_SCO_NAUPA_CODE_SEMANTICS`.

Current state:
- row limit: null / not yet selected;
- row access false;
- network execution false;
- source-body access false.

Do not invent a row limit or execute this stage without a separate proposal and owner gate.

## Candidate Verification

Functional candidate HEAD:
`648b81b973a4b169c14bcdfd76ac4fa71e76f2e9`.

CI:
`34939909880` — SUCCESS.

Passed:
- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- frontend install/lint/typecheck/build;
- Streamlit safety/startup smoke.

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

Identity resolution, beneficiary matching and outreach remain BLOCKED.

## Blocking Items

Before any real row access/acquisition:

1. retention policy approved;
2. trusted project privacy policy approved;
3. transient full-row privacy review completed;
4. bounded `PROPERTY_TYPE` semantic-verification plan approved;
5. real-acquisition client reviewed;
6. source approval reference assigned;
7. source policy approved under separate gate;
8. registry enabled under separate gate.

## SINGLE NEXT ACTION

**Human review of the revised two-field minimization and transient CSV privacy boundary.**

If the owner accepts the candidate, the next repository action is promotion:

`m3-ca-sco-field-privacy-readiness -> m2-state-governance-core`

Promotion must remain non-authorizing. It must not update the SCO policy to `APPROVED`, enable the registry, read a real row, authorize PII, or execute semantic verification.

After promotion and canonical CI, the next separate task is to design a bounded `PROPERTY_TYPE` semantic-verification proposal with explicit row/request/byte caps and its own human gate.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
Canonical baseline before candidate: 74af507796f8bcc4ab45baba6abffe6714f9f6c6
Current candidate: m3-ca-sco-field-privacy-readiness
Functional candidate: 648b81b973a4b169c14bcdfd76ac4fa71e76f2e9
Functional candidate CI: 34939909880 SUCCESS
Purpose: INSURANCE_RELEVANCE_TRIAGE_ONLY
Proposed persisted fields: PROPERTY_ID, PROPERTY_TYPE
HOLDER_NAME: PROHIBITED FOR FIRST TRIAGE
Transient CSV prohibited-field exposure: POSSIBLE / SEPARATELY GATED
Projected retention duration: UNRESOLVED
Transient row buffer retention: 0 DAYS / IMMEDIATE DISPOSAL
Privacy candidate: DRAFT_NOT_TRUSTED
Real acquisition: BLOCKED
Real row access: BLOCKED
Real PII: BLOCKED
Identity resolution: BLOCKED
Beneficiary matching: BLOCKED
Outreach: BLOCKED
SCO policy: PROPOSED
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
New SCO network/body access in this candidate: 0
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: human review, then candidate promotion if accepted
CONTEXT HEALTH: coherent; repository is source of truth
```
