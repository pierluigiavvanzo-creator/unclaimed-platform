# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Status

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy gates, SCO source governance, transport evidence, source-approval readiness, data-scope proposals, segmented transport evidence, the `$500+` bounded structure inspection, and the revised two-field field/privacy readiness boundary are now canonical on `m2-state-governance-core`.

Canonical promoted baseline:
`9c2f5b6c82ed787bf0820bdd850e475775fc097c`.

Canonical post-promotion CI:
`34940817455` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

Streamlit remains the active reviewer target. Repository-side Vercel integration remains decommissioned. Supabase remains untouched.

## Canonical `$500+` Structure Evidence

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Verified facts from the prior owner-authorized structure-only run:
- four non-encrypted DEFLATED CSV members;
- identical 25-label header candidate across all four members;
- 5 HTTP `206` Range responses;
- total source-body bytes read `393,216`;
- full archive downloaded `false`;
- CSV data rows parsed `0`;
- record values persisted `false`.

No real data row has yet been sampled.

## Canonical Product Purpose / Field Boundary

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Canonical proposed persisted/allowed row scope:
1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

`HOLDER_NAME` is prohibited for the first triage purpose.

Reason: official California SCO/NAUPA documentation defines insurance property codes `IN01-IN08` and `IN99`, so holder identity is not justified merely to determine insurance relevance. The actual bulk CSV `PROPERTY_TYPE` row-value semantics remain unverified because zero data rows have been sampled.

Official code reference:
`https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`.

## Critical Privacy / Transport Boundary

The source members are CSV files and no server-side column projection capability has been established. A future real-row read may therefore transiently expose bytes from prohibited owner/holder columns before local projection discards them.

Canonical controls require:
- no raw ZIP persistence;
- no full-row persistence;
- no use or persistence of nonallowlisted values;
- real row access remains `false`;
- separate transient-row privacy approval before any row access.

Persisted-field minimization does not itself eliminate transient source-row processing.

## PII / Retention State

The two proposed persisted fields were not identified by the prior header heuristic as potential PII labels. This does not establish that real row processing is PII-free because prohibited identity/address columns are present in the same CSV rows.

Retention state:
- transient source-row buffer retention: `0 days`;
- transient buffer disposal: immediate after projection or stop;
- projected two-field triage-record retention duration: unresolved;
- approved retention policy ref: null.

The earlier seven-day candidate was removed because no production/legal evidence justified that duration.

Privacy candidate remains `DRAFT_NOT_TRUSTED`; trusted privacy-policy ref remains null.

## Authorization State

Unchanged and fail-closed:
- source policy `PROPOSED`;
- real acquisition authorized `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- real row access BLOCKED;
- real PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

Promotion of the two-field boundary did not authorize source access, PII, semantic verification, matching, or outreach.

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
`34940817455` — SUCCESS.

## Remaining Blocking Items

Before any real row access/acquisition:
- production retention policy approved;
- trusted project privacy policy approved;
- transient full-row privacy review completed;
- bounded `PROPERTY_TYPE` semantic-verification plan approved;
- real-acquisition client reviewed;
- source approval reference assigned;
- source policy separately approved;
- registry separately enabled.

## Next Recommended Action

Create an isolated, non-authorizing **`PROPERTY_TYPE` semantic-verification proposal** with explicit row, request, byte, persistence, logging and stop caps. The next task is design/contract/test only: do not read a real row and do not execute network access without a separate explicit owner gate.
