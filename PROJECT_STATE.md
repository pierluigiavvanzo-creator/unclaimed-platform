# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition contracts/adapters,
immutable raw storage/provenance, privacy/data-minimization gates, SCO source governance, transport
preflight, source-approval readiness, segmented transport evidence and the `$500+` bounded structure
inspection are canonical and CI verified on `m2-state-governance-core`.

Canonical development HEAD before the current candidate:
`74af507796f8bcc4ab45baba6abffe6714f9f6c6`.

Stable `main` remains:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

Streamlit Community Cloud remains the active reviewer target. Repository-side Vercel integration is
decommissioned. Supabase remains untouched.

## Canonical `$500+` Structure Evidence

Target:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Structure-only execution run `34864433849` succeeded using 5 HTTP Range responses and `393,216`
source-body bytes. The full archive was not downloaded. Exactly zero CSV data rows were parsed and no
record values were persisted.

Four non-encrypted DEFLATED CSV members were found. All four produced the same 25-label header
candidate. Exact evidence is canonical at:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

The source-access policy remains `PROPOSED`; registry `enabled` and `approved_for_use` remain false;
approved real sources remain `0`; real PII, identity resolution, matching and outreach remain blocked.

## Current Candidate — Field / Privacy Readiness

Branch:
`m3-ca-sco-field-privacy-readiness`

Functional candidate HEAD before persistent-doc closure:
`8e303caa6fcb10f943382861842297f405786a5b`.

Candidate CI:
`34889037049` — SUCCESS for `quality` and `streamlit-candidate`.

No SCO network request or body access occurred in this task.

New artifacts:

- `schemas/common/source_field_privacy_readiness.schema.json`;
- `schemas/examples/ca_sco_500_plus_field_privacy_readiness.examples.json`;
- `sources/proposals/ca_sco_segment_500_plus.field_privacy_readiness.v1.json`;
- `tests/contract/test_ca_sco_field_privacy_readiness.py`;
- `docs/audits/M3_CA_SCO_FIELD_PRIVACY_READINESS.md`.

The proposal is machine-fixed to `READINESS_PROPOSAL_NOT_AUTHORIZED` and
`BLOCKED_PENDING_POLICY_AND_PII_APPROVAL`.

### Proposed product purpose

`INSURANCE_RELEVANCE_TRIAGE_ONLY`

The only future decision contemplated by this proposal is whether a record appears plausibly
insurance-related and merits later human-gated review. Identity resolution, beneficiary matching,
genealogy, outreach, claim submission, fee agreements and claimant verification are explicitly excluded.

### Proposed minimized field scope

All 25 verified header labels are classified exactly once.

Required / proposed future row allowlist:

- `PROPERTY_ID`
- `PROPERTY_TYPE`
- `HOLDER_NAME`

Optional: none.

Prohibited for this purpose:

- `OWNER_NAME` and all owner address/geography fields;
- all holder street/city/state/ZIP fields.

Unresolved and therefore not allowlisted:

- `CASH_REPORTED`;
- `SHARES_REPORTED`;
- `NAME_OF_SECURITIES_REPORTED`;
- `NO_OF_OWNERS`;
- `CURRENT_CASH_BALANCE`;
- `NUMBER_OF_PENDING_CLAIMS`;
- `NUMBER_OF_PAID_CLAIMS`;
- `CUSIP`.

`HOLDER_NAME` is a field-level potential-PII candidate, but actual PII presence remains
`UNVERIFIED_NO_ROWS_SAMPLED`. PII processing remains unauthorized until separate human/legal review
approves necessity/proportionality.

### Draft retention/privacy controls

Retention candidate:

- status `DRAFT_NOT_APPROVED`;
- projected triage-record maximum `7` days;
- basis `PROJECT_SAFETY_CANDIDATE_NOT_LEGAL_REQUIREMENT`;
- full archive persistence false;
- full-row persistence false;
- approved policy ref null.

The 7-day value is a conservative project safety proposal, not a legal requirement.

Privacy candidate:

- status `DRAFT_NOT_TRUSTED`;
- purpose limited to `INSURANCE_RELEVANCE_TRIAGE_ONLY`;
- candidate fields limited to `PROPERTY_ID`, `PROPERTY_TYPE`, `HOLDER_NAME`;
- encryption at rest, least privilege and access logging required;
- record values in logs, export, identity resolution, matching and outreach prohibited;
- trusted policy ref null.

No trusted project privacy-policy artifact or approved production retention policy currently exists in
the canonical repository; the proposal deliberately does not invent either.

## Verification

Candidate CI `34889037049` passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- reviewer frontend dependency install, lint, typecheck and build;
- Streamlit safety and startup smoke.

Contract tests bind the proposal to the canonical 25-field evidence, enforce the exact 3-field future
scope, verify policy/registry remain fail-closed and reject source authorization, field widening and an
invented trusted privacy-policy reference.

## Remaining Blockers

Before any real row-level acquisition:

- retention policy approval;
- trusted project privacy-policy approval;
- explicit approval of `HOLDER_NAME` PII necessity;
- actual PII presence remains unverified because no row was sampled;
- real-acquisition client review;
- source-approval reference;
- policy transition to `APPROVED` under a separate gate;
- registry activation under a separate gate.

## Next Recommended Action

**Human/legal/privacy/retention review gate** for the current candidate. Review the proposed 3-field
minimization, the `HOLDER_NAME` necessity rationale, and the draft 7-day retention/privacy controls.
Do not authorize row access, PII processing, source approval or registry activation as an implicit part
of candidate promotion.
