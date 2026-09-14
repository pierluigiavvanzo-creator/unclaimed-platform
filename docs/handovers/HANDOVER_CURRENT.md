# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical promoted baseline: `89a5e626c2aa6bf98147522b83973ba62b6d0ccc`
- Canonical post-promotion CI: `34887416658` — SUCCESS
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` — unchanged
- Do not develop directly on `main`.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition/raw persistence/privacy CANONICAL + VERIFIED.
- Streamlit reviewer CANONICAL + CI VERIFIED.
- California SCO source governance CANONICAL + CI VERIFIED.
- SCO transport-preflight evidence CANONICAL + CI VERIFIED.
- SCO source-approval readiness package CANONICAL + CI VERIFIED.
- SCO data-scope inspection proposal CANONICAL + CI VERIFIED.
- SCO segmented transport evidence CANONICAL + CI VERIFIED.
- SCO `$500+` bounded structure inspection EXECUTED + EVIDENCE PERSISTED + CANONICAL + CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Product strategy — segmented California pilot

Metadata-only preflight observed official SCO value segments:
- `$0–9.99`: `1,321,027,390` bytes;
- `$10–99.99`: `1,261,492,445` bytes;
- `$100–499.99`: `459,105,796` bytes;
- `$500 and up`: `162,416,884` bytes;
- full `All properties`: `3,203,972,130` bytes.

The `$500+` segment is the initial pilot target because it is the smallest observed segment and fits the high-value-first product strategy. This is product prioritization, not proof that each record is commercially viable or insurance-related.

## Canonical `$500+` transport target

- endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- host: `claimit.ca.gov`;
- content type: `application/zip`;
- content length: `162,416,884` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:34 GMT`.

## Owner-authorized structure inspection

One-shot workflow commit:
`40c5ff8c78cdf03f60dcce73ad1c12c5f4466994`

Workflow run:
`34864433849` — SUCCESS

Approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T17:21+02:00_BOUNDED_DATA_SCOPE_INSPECTION`

Machine result:
`SUCCEEDED_STRUCTURE_ONLY`

Observed execution:
- 5 Range requests, all HTTP `206`;
- one archive-tail response of `131,072` bytes;
- four member-prefix responses of `65,536` bytes each;
- total source response-body bytes `393,216`;
- full archive downloaded `false`;
- CSV data rows parsed `0`;
- record values persisted `false`;
- stop reason `null`.

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`

Audit:
`docs/audits/M3_CA_SCO_500_PLUS_DATA_SCOPE_EXECUTION.md`

Evidence closure commit:
`54f2e90b43cf98afb0c607f02c65fa510f71df2d`

Evidence closure CI:
`34886584110` — SUCCESS

The network-capable one-shot workflow was removed immediately after evidence capture and its absence is contract-tested.

## Verified archive/header structure

Exactly four non-encrypted DEFLATED CSV members were found:
1. `From_500_To_Beyond_1_of_4.csv`
2. `From_500_To_Beyond_2_of_4.csv`
3. `From_500_To_Beyond_3_of_4.csv`
4. `From_500_To_Beyond_4_of_4.csv`

All four yielded the same high-confidence comma-delimited UTF-8 header candidate with 25 labels:
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

Header confidence:
`HIGH_DETERMINISTIC_LABEL_HEURISTIC`

This is structure verification only. No data row was sampled, so row values, population rates, actual PII values and field necessity remain unknown.

## Potential PII indicators

Structure-level heuristic flagged:
`NAME_OF_SECURITIES_REPORTED`, `NO_OF_OWNERS`, `OWNER_NAME`, `OWNER_STREET_1`, `OWNER_STREET_2`, `OWNER_STREET_3`, `OWNER_CITY`, `OWNER_STATE`, `OWNER_ZIP`, `OWNER_COUNTRY_CODE`, `HOLDER_NAME`, `HOLDER_CITY`, `HOLDER_STATE`, `HOLDER_ZIP`.

This is not a legal determination and grants no processing authority.

## Canonical authorization state

Unchanged:
- policy `policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json` remains `PROPOSED`;
- `real_acquisition_authorized: false`;
- `approval_ref: null`;
- `allow_pii: false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Promotion evidence

Before promotion:
- canonical `f6bfa0dd4cc0bba0ad48d2bacc6ef5bb7bbbb311`;
- candidate `89a5e626c2aa6bf98147522b83973ba62b6d0ccc`;
- ahead `8`;
- behind `0`;
- merge-base exactly `f6bfa0dd4cc0bba0ad48d2bacc6ef5bb7bbbb311`.

Owner explicitly authorized:
`m3-ca-sco-500-plus-range-inspection -> m2-state-governance-core`

Promotion was a non-force fast-forward to:
`89a5e626c2aa6bf98147522b83973ba62b6d0ccc`.

Canonical post-promotion CI:
`34887416658` — SUCCESS for both `quality` and `streamlit-candidate`.

Verified in canonical CI:
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- frontend dependency install/lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

No source approval, registry activation, row-level acquisition, PII processing, identity resolution, matching or outreach was authorized by promotion.

## What remains unresolved / blocked

- field-by-field necessity/proportionality for the intended product purpose;
- minimized production field whitelist;
- production retention duration/policy;
- trusted project privacy-policy reference;
- reviewed real-acquisition client under final field/privacy controls;
- explicit source-approval reference;
- policy `APPROVED` transition;
- registry activation;
- real row-level acquisition;
- A02 real normalization;
- identity resolution, beneficiary matching and outreach.

No additional source-body access is required for the next step.

## SINGLE NEXT ACTION

Create an isolated, non-authorizing **field-minimization + PII-necessity + retention/privacy readiness proposal** based only on the verified 25 labels.

Requirements:
1. no SCO network/body access;
2. define exact product purpose for the `$500+` pilot;
3. classify all 25 labels as required, optional, prohibited or unresolved;
4. minimize owner/holder/address fields before any row access;
5. document PII necessity/proportionality blockers without inventing legal authority;
6. select/propose retention controls under human/legal review;
7. select a trusted privacy-policy reference;
8. define the smallest future row-level acquisition contract compatible with the whitelist;
9. remain non-authorizing and stop at a later explicit source-approval gate.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
M3 SCO data-scope proposal: CANONICAL + CI VERIFIED
M3 SCO segmented transport evidence: CANONICAL + CI VERIFIED
M3 SCO $500+ structure inspection: CANONICAL + CI VERIFIED
Canonical promoted SHA: 89a5e626c2aa6bf98147522b83973ba62b6d0ccc
Canonical promotion CI: 34887416658 SUCCESS
One-shot execution: 34864433849 SUCCESS
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
NEXT: offline field-minimization + PII/retention/privacy readiness proposal
CONTEXT HEALTH: coherent; repository is source of truth
```
