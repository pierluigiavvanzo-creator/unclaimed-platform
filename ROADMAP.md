# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | $500+ STRUCTURE INSPECTION EXECUTED + CI VERIFIED — SOURCE APPROVAL BLOCKED | One-shot `34864433849` SUCCESS; evidence closure `54f2e90b...`; CI `34886584110` PASS; policy `PROPOSED`; registry disabled/unapproved |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + REPOSITORY-SIDE VERCEL INTEGRATION DECOMMISSIONED | Reviewer contract v2.0.0; Streamlit active; no Vercel runtime integration in repository |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source registered as disabled and not approved.
- Source-governance, approval-readiness, transport-preflight, source-approval-package and data-scope
  inspection contracts versioned and CI verified.
- Owner-authorized metadata-only transport preflights executed without reading dataset bodies.
- Four official SCO value-segment ZIPs observed and recorded.
- `$500 and up` selected as the initial pilot segment based on observed size and product prioritization.
- Owner-authorized `$500+` bounded structure inspection executed successfully.
- Exact structure evidence persisted and contract-tested.
- One-shot network workflow removed immediately after evidence capture.
- No CSV data row, record value, beneficiary matching or outreach has occurred.

## $500+ pilot transport evidence

Observed target:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Verified transport metadata:

- content length: `162,416,884` bytes;
- content type: `application/zip`;
- `Accept-Ranges: bytes`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:34 GMT`.

The `$500+` object is about 5.1% of the observed 3.2 GB `All properties` object. The full archive is not
required for the pilot structure phase.

## Completed bounded structure execution

Branch:
`m3-ca-sco-500-plus-range-inspection`

Execution workflow commit:
`40c5ff8c78cdf03f60dcce73ad1c12c5f4466994`

One-shot workflow run:
`34864433849` — SUCCESS.

Machine result:
`SUCCEEDED_STRUCTURE_ONLY`.

Execution facts:

- 5 HTTP Range GET responses, all `206`;
- one 131,072-byte archive-tail request;
- four 65,536-byte member-prefix requests;
- total source-body bytes read: `393,216`;
- full archive downloaded: `false`;
- CSV data rows parsed: `0`;
- record values persisted: `false`;
- stop reason: `null`.

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Evidence audit:
`docs/audits/M3_CA_SCO_500_PLUS_DATA_SCOPE_EXECUTION.md`.

Evidence closure commit:
`54f2e90b43cf98afb0c607f02c65fa510f71df2d`.

Evidence closure CI:
`34886584110` — PASS for `quality` and `streamlit-candidate`.

## Verified archive/header structure

The ZIP contains exactly four non-encrypted, DEFLATED CSV members:

1. `From_500_To_Beyond_1_of_4.csv`
2. `From_500_To_Beyond_2_of_4.csv`
3. `From_500_To_Beyond_3_of_4.csv`
4. `From_500_To_Beyond_4_of_4.csv`

All four files yielded the same high-confidence comma-delimited UTF-8 header candidate with 25 fields:

`PROPERTY_ID`, `PROPERTY_TYPE`, `CASH_REPORTED`, `SHARES_REPORTED`,
`NAME_OF_SECURITIES_REPORTED`, `NO_OF_OWNERS`, `OWNER_NAME`, `OWNER_STREET_1`,
`OWNER_STREET_2`, `OWNER_STREET_3`, `OWNER_CITY`, `OWNER_STATE`, `OWNER_ZIP`,
`OWNER_COUNTRY_CODE`, `CURRENT_CASH_BALANCE`, `NUMBER_OF_PENDING_CLAIMS`,
`NUMBER_OF_PAID_CLAIMS`, `HOLDER_NAME`, `HOLDER_STREET_1`, `HOLDER_STREET_2`,
`HOLDER_STREET_3`, `HOLDER_CITY`, `HOLDER_STATE`, `HOLDER_ZIP`, `CUSIP`.

This is **header/structure verification only**. No data row was sampled, so row-value consistency,
field population rates and actual PII values remain unknown.

## Current safety state

- source-access policy: `PROPOSED`;
- real acquisition authorized: `false`;
- registry `enabled`: `false`;
- registry `approved_for_use`: `false`;
- approved real sources: `0`;
- full ZIP acquisition: BLOCKED;
- CSV data-row access: BLOCKED;
- record-value processing: BLOCKED;
- real PII processing: BLOCKED;
- identity resolution: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED.

The header heuristic identifies owner/holder/name/address-related labels as possible PII indicators,
but this is not a legal necessity determination and grants no processing authority.

## Verification chain

- non-authorizing data-scope proposal promoted to canonical: `f6bfa0dd...`;
- segmented HEAD preflight: `34862117709` SUCCESS;
- segmented evidence CI: `34862892612` SUCCESS;
- `$500+` contract CI: `34863903807` SUCCESS;
- bounded inspector CI: `34864249090` SUCCESS;
- real structure-only one-shot: `34864433849` SUCCESS;
- evidence closure: `54f2e90b43cf98afb0c607f02c65fa510f71df2d`;
- evidence closure CI: `34886584110` SUCCESS;
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- frontend lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

## Next gate — candidate promotion

The next action is a human promotion decision for:

`m3-ca-sco-500-plus-range-inspection` → `m2-state-governance-core`.

Promotion records verified structure evidence. It does **not** authorize:

- source status `APPROVED`;
- registry activation;
- full ZIP or CSV acquisition;
- data-row or record-value access;
- real PII processing;
- identity resolution;
- beneficiary matching;
- outreach or claims activity.

## Next product work after promotion

Create an isolated, non-authorizing **field-minimization + PII-necessity + retention/privacy readiness
proposal** using only the verified 25 field labels.

That proposal should:

1. define the exact product purpose for the `$500+` pilot;
2. classify each of the 25 labels as required, optional, prohibited, or unresolved for that purpose;
3. minimize owner/holder/address fields before any row access;
4. document PII necessity/proportionality blockers without inventing legal authority;
5. select or propose a production retention policy and duration under human/legal review;
6. select a trusted project privacy-policy reference;
7. define the smallest row-level acquisition contract compatible with the approved field whitelist;
8. remain non-authorizing until an explicit later source-approval gate.

No additional California SCO network/body access is required for this proposal task.

## Still required before source approval or real acquisition

1. `$500+` structure inspection — DONE + VERIFIED;
2. promotion of the verified candidate if owner approves;
3. minimized field whitelist;
4. PII necessity/proportionality determination;
5. production retention policy;
6. trusted privacy policy;
7. real-acquisition client review against finalized controls;
8. explicit source-approval reference;
9. separate policy `APPROVED` + registry activation gate;
10. separate real row-level acquisition authorization;
11. A02 normalization against approved fields only;
12. later identity/matching/outreach gates as independently authorized.

## Out of scope until later gates

- reading real data rows merely to refine the current header evidence;
- source approval before privacy/retention/field minimization is resolved;
- full California acquisition;
- autonomous identity resolution or beneficiary matching;
- autonomous outreach;
- claimant verification, fee agreements or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
