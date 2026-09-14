# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | FIELD/PRIVACY READINESS CANDIDATE + CI VERIFIED — SOURCE APPROVAL BLOCKED | Candidate `8e303caa...`; CI `34889037049` SUCCESS; policy `PROPOSED`; registry disabled/unapproved |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + VERCEL REPOSITORY INTEGRATION DECOMMISSIONED | Reviewer contract v2.0.0; Streamlit active |

## Completed M3 Readiness Work

- California source/legal inventory completed.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO source registered disabled and not approved.
- Source governance, approval-readiness, transport-preflight, source-approval-package and data-scope contracts versioned and CI verified.
- Four official SCO value-segment ZIPs observed via metadata-only preflight.
- `$500 and up` selected as initial high-value pilot target.
- Bounded Range inspector implemented and contract-tested.
- Owner-authorized `$500+` structure-only inspection executed using `393,216` bytes and zero data rows.
- Exact 4-member / 25-header structure evidence persisted and promoted to canonical.
- One-shot network workflow removed after evidence capture.
- Field-minimization / PII / retention-privacy readiness proposal now implemented on an isolated candidate with no new SCO access.

## Current Candidate

Branch:
`m3-ca-sco-field-privacy-readiness`

Functional candidate HEAD:
`8e303caa6fcb10f943382861842297f405786a5b`

CI:
`34889037049` — SUCCESS.

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Proposed future row allowlist:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`
3. `HOLDER_NAME`

All owner identity/address fields and holder address/geography fields are prohibited for this purpose.
Eight amount/claims/securities fields remain unresolved and therefore outside the allowlist.

Actual PII presence is still `UNVERIFIED_NO_ROWS_SAMPLED`. `HOLDER_NAME` is a potential-PII field whose
necessity remains subject to human/legal approval. Real PII processing remains blocked.

## Draft Retention / Privacy Controls

Retention candidate:

- `DRAFT_NOT_APPROVED`;
- 7-day projected triage-record maximum;
- explicitly `PROJECT_SAFETY_CANDIDATE_NOT_LEGAL_REQUIREMENT`;
- no full ZIP persistence;
- no full-row persistence;
- approved ref null.

Privacy candidate:

- `DRAFT_NOT_TRUSTED`;
- only purpose `INSURANCE_RELEVANCE_TRIAGE_ONLY`;
- only candidate fields `PROPERTY_ID`, `PROPERTY_TYPE`, `HOLDER_NAME`;
- encryption at rest, least privilege and access logging required;
- no record values in logs, export, identity resolution, matching or outreach;
- trusted ref null.

No approved production retention policy or trusted project privacy-policy artifact exists yet; the
candidate does not invent either.

## Current Safety State

- source policy `PROPOSED`;
- `real_acquisition_authorized: false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- row access BLOCKED;
- record-value processing BLOCKED;
- real PII BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Verification Chain

- canonical `$500+` structure promotion closure: `74af507796f8bcc4ab45baba6abffe6714f9f6c6`;
- field/privacy candidate functional HEAD: `8e303caa6fcb10f943382861842297f405786a5b`;
- candidate CI `34889037049` SUCCESS;
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- frontend lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

## Next Gate

**Human/legal/privacy/retention review** of the candidate proposal.

Review must explicitly address:

1. whether `INSURANCE_RELEVANCE_TRIAGE_ONLY` is the correct first row-level purpose;
2. whether the 3-field scope is sufficiently minimized;
3. whether `HOLDER_NAME` is necessary/proportionate for that purpose;
4. whether the proposed 7-day project safety retention window should be accepted, shortened, changed or rejected;
5. what canonical privacy policy should become trusted configuration;
6. what canonical retention policy should be approved.

This review is not, by itself, source approval or PII authorization.

## Still Required Before Real Acquisition

1. field/privacy readiness candidate review and optional promotion;
2. approved retention policy;
3. trusted project privacy policy;
4. explicit `HOLDER_NAME` necessity/proportionality decision;
5. real-acquisition client review against final controls;
6. explicit source-approval reference;
7. separate source-policy `APPROVED` transition;
8. separate registry activation;
9. separately authorized minimized row-level acquisition;
10. A02 normalization on approved fields only;
11. later identity/matching/outreach gates independently authorized.

## Out of Scope Until Later Gates

- reading real rows to refine this proposal;
- full California archive acquisition;
- processing owner identity/address data for triage;
- autonomous identity resolution, beneficiary matching or outreach;
- claimant verification, fee agreements or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
