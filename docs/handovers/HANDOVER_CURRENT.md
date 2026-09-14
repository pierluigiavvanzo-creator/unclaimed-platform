# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical development HEAD before current candidate:
  `f6bfa0dd4cc0bba0ad48d2bacc6ef5bb7bbbb311`
- Current candidate branch:
  `m3-ca-sco-500-plus-range-inspection`
- Candidate evidence-closure commit:
  `54f2e90b43cf98afb0c607f02c65fa510f71df2d`
- Stable `main` HEAD:
  `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Never develop directly on `main`; promote verified checkpoints only after the applicable owner gate.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Streamlit M3 reviewer CANONICAL + CI VERIFIED.
- California SCO source governance CANONICAL + CI VERIFIED.
- California SCO approval-readiness evidence CANONICAL + CI VERIFIED.
- California SCO transport-preflight evidence CANONICAL + CI VERIFIED.
- California SCO source-approval readiness package CANONICAL + CI VERIFIED.
- California SCO data-scope inspection proposal CANONICAL + CI VERIFIED.
- `$500+` segmented transport evidence CANDIDATE + CI VERIFIED.
- `$500+` bounded structure inspection EXECUTED + EVIDENCE PERSISTED + CI VERIFIED.
- Repository-side Vercel runtime/deployment integration DECOMMISSIONED + CI VERIFIED.
- SCO registry remains `enabled: false` and `approved_for_use: false`.
- SCO source-access policy remains `PROPOSED` and non-authorizing.
- Approved real source count remains `0`.
- Real row-level acquisition remains BLOCKED.
- Beneficiary matching remains BLOCKED.
- Real PII processing remains BLOCKED.
- Supabase untouched.
- `main` unchanged.

## Product strategy — segmented California pilot

The SCO official download page exposes value-segment ZIPs. Metadata-only preflight observed:

- `$0–9.99`: `1,321,027,390` bytes;
- `$10–99.99`: `1,261,492,445` bytes;
- `$100–499.99`: `459,105,796` bytes;
- `$500 and up`: `162,416,884` bytes.

The observed full `All properties` object is `3,203,972,130` bytes.

The `$500+` object was selected as the initial pilot target because it is the smallest observed
segment and aligns with a high-value-first product strategy. This is a product inference, not a claim
that every `$500+` record is commercially viable or insurance-related.

## $500+ transport target

Canonical candidate transport evidence for the selected segment:

- endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- host: `claimit.ca.gov`;
- content type: `application/zip`;
- content length: `162,416,884` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:34 GMT`.

## Owner-authorized bounded structure execution

One-shot workflow commit:
`40c5ff8c78cdf03f60dcce73ad1c12c5f4466994`

Workflow run:
`34864433849` — SUCCESS.

Execution approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T17:21+02:00_BOUNDED_DATA_SCOPE_INSPECTION`

Machine result:
`SUCCEEDED_STRUCTURE_ONLY`

Stop reason:
`null`

Execution budget actually consumed:

- range requests: `5`;
- one archive-tail response: `131,072` bytes;
- four CSV member-prefix responses: `65,536` bytes each;
- total response-body bytes read: `393,216` bytes;
- configured absolute execution cap: `14,811,136` bytes;
- full archive downloaded: `false`.

All five Range responses were HTTP `206`. The server honored Range. No byte-budget widening occurred.

## Verified archive structure

The bounded parser found exactly four members, all non-encrypted and DEFLATED:

1. `From_500_To_Beyond_1_of_4.csv`
2. `From_500_To_Beyond_2_of_4.csv`
3. `From_500_To_Beyond_3_of_4.csv`
4. `From_500_To_Beyond_4_of_4.csv`

ZIP64 was not required. No unsafe-path or unsupported-compression stop condition fired.

## Verified header structure

Each of the four CSV members produced the same high-confidence comma-delimited UTF-8 header
candidate with 25 labels:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`
3. `CASH_REPORTED`
4. `SHARES_REPORTED`
5. `NAME_OF_SECURITIES_REPORTED`
6. `NO_OF_OWNERS`
7. `OWNER_NAME`
8. `OWNER_STREET_1`
9. `OWNER_STREET_2`
10. `OWNER_STREET_3`
11. `OWNER_CITY`
12. `OWNER_STATE`
13. `OWNER_ZIP`
14. `OWNER_COUNTRY_CODE`
15. `CURRENT_CASH_BALANCE`
16. `NUMBER_OF_PENDING_CLAIMS`
17. `NUMBER_OF_PAID_CLAIMS`
18. `HOLDER_NAME`
19. `HOLDER_STREET_1`
20. `HOLDER_STREET_2`
21. `HOLDER_STREET_3`
22. `HOLDER_CITY`
23. `HOLDER_STATE`
24. `HOLDER_ZIP`
25. `CUSIP`

Header confidence recorded by the execution artifact:
`HIGH_DETERMINISTIC_LABEL_HEURISTIC`.

This establishes **archive/member/header structure only**. It does not establish actual row values,
field population rates, semantic consistency of every data row, or the legal necessity of any field.
Exactly zero CSV data rows were parsed.

## Potential PII indicators

The structure-only heuristic marked the following header labels as potential PII indicators:

- `NAME_OF_SECURITIES_REPORTED`
- `NO_OF_OWNERS`
- `OWNER_NAME`
- `OWNER_STREET_1`
- `OWNER_STREET_2`
- `OWNER_STREET_3`
- `OWNER_CITY`
- `OWNER_STATE`
- `OWNER_ZIP`
- `OWNER_COUNTRY_CODE`
- `HOLDER_NAME`
- `HOLDER_CITY`
- `HOLDER_STATE`
- `HOLDER_ZIP`

This is not a legal determination and does not prove a field is populated. It creates a blocker to be
resolved by field minimization and PII necessity/proportionality review before any row-level use.

## Exact persisted evidence

Evidence file:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`

Execution schema:
`schemas/common/source_data_scope_inspection_execution.schema.json`

Evidence audit:
`docs/audits/M3_CA_SCO_500_PLUS_DATA_SCOPE_EXECUTION.md`

Evidence closure commit:
`54f2e90b43cf98afb0c607f02c65fa510f71df2d`

Evidence closure CI:
`34886584110` — SUCCESS.

The one-shot artifact was captured from GitHub Actions, not reconstructed from chat logs.
Artifact ID:
`10356079506`

Artifact ZIP digest:
`sha256:606923fdcf0b3090b63203c321c3d899633d940c5d4ad1d3fd265b0acb8b94d6`

Exact evidence JSON SHA-256 before repository persistence:
`d4faa41885901551da378318a368d0f92f8b55de745710dcf5faf5edc53bf947`

## One-shot cleanup

The network-capable workflow:
`.github/workflows/ca-sco-500-plus-data-scope-once.yml`

was removed in the same evidence-closure commit. Contract tests assert that the workflow is absent.
No reusable network workflow remains for this execution.

## Verified safety state

The exact execution evidence records:

- full archive downloaded: `false`;
- raw body persisted: `false`;
- temporary source files created: `false`;
- CSV data rows parsed: `0`;
- record values persisted: `false`;
- real PII processing authorized: `false`;
- identity resolution performed: `false`;
- beneficiary matching performed: `false`;
- outreach performed: `false`;
- source approved: `false`;
- source enabled: `false`.

Canonical authorization state remains unchanged:

`policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json`

- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `approval_ref: null`;
- `allow_pii: false`;
- beneficiary matching unauthorized;
- outreach unauthorized.

`sources/registry.yaml`

- `enabled: false`;
- `approved_for_use: false`.

## CI / verification chain

- data-scope proposal canonical baseline: `f6bfa0dd4cc0bba0ad48d2bacc6ef5bb7bbbb311`;
- segmented HEAD preflight workflow: `34862117709` SUCCESS;
- segmented evidence CI after formatting fix: `34862892612` SUCCESS;
- `$500+` contract CI: `34863903807` SUCCESS;
- bounded inspector implementation CI: `34864249090` SUCCESS;
- owner-authorized structure-only execution: `34864433849` SUCCESS;
- evidence closure commit: `54f2e90b43cf98afb0c607f02c65fa510f71df2d`;
- evidence closure CI: `34886584110` SUCCESS;
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- frontend lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

## What is resolved

Resolved:

- actual `$500+` ZIP member count and names;
- archive compression/encryption properties for those four members;
- consistent 25-field CSV header candidate across all four members;
- structure-level potential PII indicators;
- viability of using Range requests for structure inspection without downloading the complete ZIP.

## What remains unresolved / blocked

- actual data-row contents and consistency;
- whether any potential-PII field is populated for a specific record;
- field-by-field necessity and proportionality for the intended product purpose;
- minimized production whitelist;
- production retention duration/policy;
- trusted project privacy-policy reference;
- reviewed real-acquisition client under final field/privacy controls;
- explicit source-approval reference;
- policy `APPROVED` transition;
- registry activation;
- real row-level acquisition;
- A02 real normalization;
- identity resolution, beneficiary matching and outreach.

No additional source-body access is required to address the next readiness step.

## SINGLE NEXT ACTION

**HUMAN PROMOTION GATE ONLY:** decide whether to promote verified candidate branch
`m3-ca-sco-500-plus-range-inspection` into canonical `m2-state-governance-core`.

Before promotion:

1. compare candidate vs canonical;
2. require clean ancestry and no behind commits;
3. verify the temporary one-shot workflow is absent;
4. require evidence-closure CI `34886584110` to remain SUCCESS.

If the owner explicitly approves promotion:

1. fast-forward canonical without force;
2. verify canonical CI on the promoted SHA;
3. update persistent docs with promotion evidence if needed;
4. stop before any additional source-body action.

Promotion does **not** authorize source approval, registry activation, row-level data access, real PII,
identity resolution, matching or outreach.

After promotion, the next product task is an isolated, non-authorizing **field-minimization +
PII-necessity + retention/privacy readiness proposal** based only on the verified 25 labels. That task
requires no SCO network or body access.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
M3 SCO data-scope proposal: CANONICAL + CI VERIFIED
M3 SCO segmented transport evidence: CANDIDATE + CI VERIFIED
M3 SCO $500+ structure inspection: EXECUTED + EVIDENCE PERSISTED + CI VERIFIED
Candidate branch: m3-ca-sco-500-plus-range-inspection
Candidate evidence SHA: 54f2e90b43cf98afb0c607f02c65fa510f71df2d
One-shot run: 34864433849 SUCCESS
Evidence closure CI: 34886584110 SUCCESS
Range requests: 5 x HTTP 206
Source body bytes read: 393216
Archive members: 4 CSV
Verified header candidate: 25 labels, identical across all 4 CSVs
CSV data rows parsed: 0
Record values persisted: false
SCO policy: PROPOSED + NON-AUTHORIZING
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
Real PII: BLOCKED
Identity resolution: BLOCKED
Beneficiary matching: BLOCKED
Outreach: BLOCKED
Vercel repository integration: DECOMMISSIONED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: owner promotion decision for current verified candidate
AFTER PROMOTION: offline field-minimization + PII/retention/privacy readiness proposal
CONTEXT HEALTH: coherent; repository is source of truth
```
