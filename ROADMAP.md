# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `$500+` STRUCTURE INSPECTION CANONICAL + CI VERIFIED — SOURCE APPROVAL BLOCKED | Canonical `89a5e626...`; post-promotion CI `34887416658` SUCCESS; policy `PROPOSED`; registry disabled/unapproved |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + REPOSITORY-SIDE VERCEL INTEGRATION DECOMMISSIONED | Reviewer contract v2.0.0; Streamlit active; no Vercel runtime integration in repository |

## Completed M3 readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO source registered as disabled and not approved.
- Source-governance, approval-readiness, transport-preflight, source-approval-package and data-scope contracts versioned and CI verified.
- Four official SCO value-segment ZIPs observed via metadata-only preflight.
- `$500 and up` selected as the initial high-value pilot target.
- Bounded Range inspector implemented and contract-tested.
- Owner-authorized structure-only `$500+` inspection executed successfully.
- Exact structure evidence persisted and contract-tested.
- Temporary one-shot network workflow removed immediately after evidence capture.
- Candidate promoted by non-force fast-forward to canonical `m2-state-governance-core`.
- Canonical post-promotion CI is green.

## Canonical `$500+` Evidence

Target:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Observed:
- `162,416,884` bytes;
- `application/zip`;
- `Accept-Ranges: bytes`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`.

Execution:
- one-shot run `34864433849` SUCCESS;
- machine result `SUCCEEDED_STRUCTURE_ONLY`;
- 5 HTTP `206` Range responses;
- `393,216` total response-body bytes;
- full archive downloaded `false`;
- CSV data rows parsed `0`;
- record values persisted `false`.

Evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`

Four CSV members were found, all non-encrypted and DEFLATED. All four expose the same 25-label header candidate. This verifies structure only, not row values or field necessity.

## Verification Chain

- data-scope proposal canonical baseline `f6bfa0dd...`;
- segmented HEAD preflight `34862117709` SUCCESS;
- segmented evidence CI `34862892612` SUCCESS;
- `$500+` contract CI `34863903807` SUCCESS;
- bounded inspector CI `34864249090` SUCCESS;
- structure-only one-shot `34864433849` SUCCESS;
- evidence closure `54f2e90b43cf98afb0c607f02c65fa510f71df2d`;
- evidence closure CI `34886584110` SUCCESS;
- promotion target `89a5e626c2aa6bf98147522b83973ba62b6d0ccc`;
- canonical post-promotion CI `34887416658` SUCCESS.

## Current Safety State

- source-access policy `PROPOSED`;
- real acquisition authorized `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- CSV data-row access BLOCKED;
- record-value processing BLOCKED;
- real PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Next Product Work

Create an isolated, non-authorizing **field-minimization + PII-necessity + retention/privacy readiness proposal** using only the verified 25 header labels.

The proposal must:
1. define the exact product purpose for the `$500+` pilot;
2. classify each label as required, optional, prohibited or unresolved;
3. minimize owner/holder/address fields before any row access;
4. document PII necessity/proportionality blockers without inventing legal authority;
5. select or propose production retention controls under human/legal review;
6. select a trusted project privacy-policy reference;
7. define the smallest future row-level acquisition contract compatible with the approved whitelist;
8. remain non-authorizing until an explicit later source-approval gate.

No additional SCO network/body access is required for this next task.

## Still Required Before Source Approval / Real Acquisition

1. `$500+` structure inspection — DONE + CANONICAL;
2. minimized field whitelist;
3. PII necessity/proportionality determination;
4. production retention policy;
5. trusted privacy policy;
6. real-acquisition client review against finalized controls;
7. explicit source-approval reference;
8. separate policy `APPROVED` + registry activation gate;
9. separate real row-level acquisition authorization;
10. A02 normalization against approved fields only;
11. later identity/matching/outreach gates as independently authorized.

## Out of Scope Until Later Gates

- reading real data rows merely to refine the header evidence;
- source approval before privacy/retention/field minimization is resolved;
- full California acquisition;
- autonomous identity resolution or beneficiary matching;
- autonomous outreach;
- claimant verification, fee agreements or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
