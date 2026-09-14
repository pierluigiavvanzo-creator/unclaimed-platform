# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical development HEAD before current candidate: `74af507796f8bcc4ab45baba6abffe6714f9f6c6`
- Current candidate: `m3-ca-sco-field-privacy-readiness`
- Functional candidate HEAD before persistent-doc closure: `8e303caa6fcb10f943382861842297f405786a5b`
- Functional candidate CI: `34889037049` — SUCCESS
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` — unchanged
- Never develop directly on `main`.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition/raw persistence/privacy CANONICAL + VERIFIED.
- Streamlit reviewer CANONICAL + CI VERIFIED.
- California SCO source governance CANONICAL + CI VERIFIED.
- SCO transport evidence CANONICAL + CI VERIFIED.
- SCO source-approval readiness CANONICAL + CI VERIFIED.
- SCO data-scope proposal CANONICAL + CI VERIFIED.
- SCO segmented transport evidence CANONICAL + CI VERIFIED.
- SCO `$500+` structure inspection EXECUTED + CANONICAL + CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical `$500+` Structure Evidence

Target:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Owner-authorized structure-only run:
`34864433849` — SUCCESS.

Execution facts:

- 5 HTTP Range requests, all `206`;
- total source-body bytes read `393,216`;
- full archive downloaded `false`;
- CSV data rows parsed `0`;
- record values persisted `false`.

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Four non-encrypted DEFLATED CSV members were found. All four yielded the same high-confidence,
comma-delimited UTF-8 header candidate with 25 labels:

`PROPERTY_ID`, `PROPERTY_TYPE`, `CASH_REPORTED`, `SHARES_REPORTED`,
`NAME_OF_SECURITIES_REPORTED`, `NO_OF_OWNERS`, `OWNER_NAME`, `OWNER_STREET_1`,
`OWNER_STREET_2`, `OWNER_STREET_3`, `OWNER_CITY`, `OWNER_STATE`, `OWNER_ZIP`,
`OWNER_COUNTRY_CODE`, `CURRENT_CASH_BALANCE`, `NUMBER_OF_PENDING_CLAIMS`,
`NUMBER_OF_PAID_CLAIMS`, `HOLDER_NAME`, `HOLDER_STREET_1`, `HOLDER_STREET_2`,
`HOLDER_STREET_3`, `HOLDER_CITY`, `HOLDER_STATE`, `HOLDER_ZIP`, `CUSIP`.

Exactly zero data rows have been sampled, so actual row values, field population rates, actual PII
presence and row-level semantic consistency remain unverified.

## Current Candidate — Field / PII / Retention / Privacy Readiness

Branch:
`m3-ca-sco-field-privacy-readiness`

New artifacts:

- `schemas/common/source_field_privacy_readiness.schema.json`
- `schemas/examples/ca_sco_500_plus_field_privacy_readiness.examples.json`
- `sources/proposals/ca_sco_segment_500_plus.field_privacy_readiness.v1.json`
- `tests/contract/test_ca_sco_field_privacy_readiness.py`
- `docs/audits/M3_CA_SCO_FIELD_PRIVACY_READINESS.md`

No California SCO network request or source-body access occurred in this task.

Machine state:

- package status `READINESS_PROPOSAL_NOT_AUTHORIZED`;
- readiness status `BLOCKED_PENDING_POLICY_AND_PII_APPROVAL`;
- source approved false;
- source enabled false;
- real acquisition authorized false;
- row access authorized false;
- PII processing authorized false.

## Product Purpose

Proposed first row-level purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Permitted future decision only:
classify a record as potentially insurance-related or not, for later human-gated review.

Explicitly excluded:

- identity resolution;
- beneficiary matching;
- genealogical research;
- outreach;
- claim submission;
- fee agreements;
- claimant verification.

## Field Minimization

All 25 verified labels are partitioned exactly once.

Required / proposed future row allowlist:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`
3. `HOLDER_NAME`

Optional fields: none.

Prohibited for this purpose:

- `OWNER_NAME`;
- `OWNER_STREET_1`, `OWNER_STREET_2`, `OWNER_STREET_3`;
- `OWNER_CITY`, `OWNER_STATE`, `OWNER_ZIP`, `OWNER_COUNTRY_CODE`;
- `HOLDER_STREET_1`, `HOLDER_STREET_2`, `HOLDER_STREET_3`;
- `HOLDER_CITY`, `HOLDER_STATE`, `HOLDER_ZIP`.

The holder street-line prohibition is a conservative project-minimization inference; the prior header
heuristic did not list those three street labels among its potential-PII indicators.

Unresolved / not allowlisted:

- `CASH_REPORTED`;
- `SHARES_REPORTED`;
- `NAME_OF_SECURITIES_REPORTED`;
- `NO_OF_OWNERS`;
- `CURRENT_CASH_BALANCE`;
- `NUMBER_OF_PENDING_CLAIMS`;
- `NUMBER_OF_PAID_CLAIMS`;
- `CUSIP`.

These fields may be relevant to later economic/claims/securities purposes, but their necessity is not
established for insurance-relevance triage.

## PII Boundary

Actual PII presence remains:
`UNVERIFIED_NO_ROWS_SAMPLED`.

`HOLDER_NAME` is the only required field currently also identified as a structure-level potential-PII
candidate. The proposal does not authorize processing it. Human/legal review must explicitly approve
necessity/proportionality before any row access.

Owner identity/address and holder address/geography fields are proposed unnecessary for the triage
purpose.

## Retention Candidate

- status `DRAFT_NOT_APPROVED`;
- policy candidate `ca.sco.500_plus.triage.retention`;
- projected triage-record maximum `7` days;
- basis `PROJECT_SAFETY_CANDIDATE_NOT_LEGAL_REQUIREMENT`;
- full archive persistence false;
- full row persistence false;
- delete on stop true;
- approved policy ref null;
- human/legal activation required.

The 7-day period is a project safety proposal, not a statement of California law.

## Privacy Candidate

- status `DRAFT_NOT_TRUSTED`;
- candidate policy `project.privacy.ca_sco_500_plus.triage`;
- purpose limited to `INSURANCE_RELEVANCE_TRIAGE_ONLY`;
- candidate allowed fields exactly `PROPERTY_ID`, `PROPERTY_TYPE`, `HOLDER_NAME`;
- encryption at rest required;
- least privilege required;
- access logging required;
- record values in logs false;
- export false;
- identity resolution false;
- beneficiary matching false;
- outreach false;
- trusted policy ref null;
- human/legal activation required.

No trusted project privacy-policy artifact or approved production retention policy currently exists in
the canonical repository. Do not invent or auto-approve either.

## Functional Candidate Verification

Functional HEAD:
`8e303caa6fcb10f943382861842297f405786a5b`.

CI:
`34889037049` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- frontend install/lint/typecheck/build;
- Streamlit safety/startup smoke.

Tests verify:

- package remains non-authorizing;
- all 25 canonical labels are classified exactly once;
- future scope is exactly 3 fields;
- source policy remains `PROPOSED` and empty-authority/fail-closed;
- registry remains disabled/unapproved;
- PII, retention and privacy candidates remain unapproved/untrusted;
- attempts to authorize acquisition, widen fields or invent a trusted privacy ref are schema-invalid.

## Canonical Authorization State — UNCHANGED

`policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json` remains:

- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `privacy_policy_ref: null`;
- `retention_policy_ref: null`;
- `authorized_processing_purposes: []`;
- `allowed_fields: []`;
- `allow_pii: false`.

`sources/registry.yaml` remains:

- `enabled: false`;
- `approved_for_use: false`.

Approved real sources remain `0`.

## Blocking Items

Before any real acquisition:

1. retention policy approved;
2. trusted project privacy policy approved;
3. `HOLDER_NAME` PII necessity approved;
4. actual PII presence still unverified until a separately authorized minimized row operation;
5. real-acquisition client reviewed;
6. source approval reference assigned;
7. source policy approved under a separate gate;
8. registry enabled under a separate gate.

## SINGLE NEXT ACTION

**Human/legal/privacy/retention review gate** for the current candidate.

Review the 3-field minimization, `HOLDER_NAME` necessity rationale, draft 7-day retention candidate and
privacy controls. Candidate promotion, if later authorized, must still remain non-authorizing and must
not change the canonical policy or registry.

No SCO body/network access is needed for that review.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
Canonical baseline before candidate: 74af507796f8bcc4ab45baba6abffe6714f9f6c6
Current candidate: m3-ca-sco-field-privacy-readiness
Functional candidate: 8e303caa6fcb10f943382861842297f405786a5b
Functional candidate CI: 34889037049 SUCCESS
Purpose: INSURANCE_RELEVANCE_TRIAGE_ONLY
Proposed future row fields: PROPERTY_ID, PROPERTY_TYPE, HOLDER_NAME
Retention candidate: 7 days, DRAFT_NOT_APPROVED, not a legal requirement
Privacy candidate: DRAFT_NOT_TRUSTED
Actual PII presence: UNVERIFIED_NO_ROWS_SAMPLED
Real acquisition: BLOCKED
Real PII: BLOCKED
Identity resolution: BLOCKED
Beneficiary matching: BLOCKED
Outreach: BLOCKED
SCO policy: PROPOSED
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
SCO network/body access in this task: 0
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: human/legal/privacy/retention review gate
CONTEXT HEALTH: coherent; repository is source of truth
```
