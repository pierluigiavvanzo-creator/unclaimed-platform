# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition contracts/adapters, immutable raw-storage/provenance, privacy/data-minimization gates, source governance, transport-preflight evidence, source-approval readiness, data-scope proposal, segmented transport evidence and the `$500+` bounded structure inspection are now canonical on `m2-state-governance-core`.

Canonical promoted baseline:
`89a5e626c2aa6bf98147522b83973ba62b6d0ccc`.

Canonical post-promotion CI:
`34887416658` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

Streamlit Community Cloud remains the active reviewer target. Repository-side Vercel integration remains decommissioned. Supabase remains untouched.

## California SCO `$500+` Pilot Evidence

Official target:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Observed transport metadata:
- content type `application/zip`;
- content length `162,416,884` bytes;
- `Accept-Ranges: bytes`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- Last-Modified `Wed, 09 Sep 2026 16:32:34 GMT`.

Owner-authorized bounded structure inspection:
- workflow commit `40c5ff8c78cdf03f60dcce73ad1c12c5f4466994`;
- run `34864433849` — SUCCESS;
- result `SUCCEEDED_STRUCTURE_ONLY`;
- 5 HTTP Range responses, all `206`;
- total source-body bytes read `393,216`;
- full archive downloaded `false`;
- CSV data rows parsed `0`;
- record values persisted `false`.

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Evidence audit:
`docs/audits/M3_CA_SCO_500_PLUS_DATA_SCOPE_EXECUTION.md`.

Evidence closure commit:
`54f2e90b43cf98afb0c607f02c65fa510f71df2d`.

Evidence closure CI:
`34886584110` — SUCCESS.

The temporary network-capable one-shot workflow was removed immediately after capture and its absence is contract-tested.

## Verified Structure

The `$500+` ZIP contains four non-encrypted DEFLATED CSV members:
1. `From_500_To_Beyond_1_of_4.csv`
2. `From_500_To_Beyond_2_of_4.csv`
3. `From_500_To_Beyond_3_of_4.csv`
4. `From_500_To_Beyond_4_of_4.csv`

All four produced the same high-confidence comma-delimited UTF-8 header candidate with 25 labels:
`PROPERTY_ID`, `PROPERTY_TYPE`, `CASH_REPORTED`, `SHARES_REPORTED`, `NAME_OF_SECURITIES_REPORTED`, `NO_OF_OWNERS`, `OWNER_NAME`, `OWNER_STREET_1`, `OWNER_STREET_2`, `OWNER_STREET_3`, `OWNER_CITY`, `OWNER_STATE`, `OWNER_ZIP`, `OWNER_COUNTRY_CODE`, `CURRENT_CASH_BALANCE`, `NUMBER_OF_PENDING_CLAIMS`, `NUMBER_OF_PAID_CLAIMS`, `HOLDER_NAME`, `HOLDER_STREET_1`, `HOLDER_STREET_2`, `HOLDER_STREET_3`, `HOLDER_CITY`, `HOLDER_STATE`, `HOLDER_ZIP`, `CUSIP`.

This is archive/header verification only. No data row was sampled; actual record values, field population rates, row-level consistency and legal necessity remain unresolved.

## Authorization State

Unchanged and fail-closed:
- source-access policy `PROPOSED`;
- real acquisition authorized `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- real PII processing `BLOCKED`;
- identity resolution `BLOCKED`;
- beneficiary matching `BLOCKED`;
- outreach `BLOCKED`.

Potential PII indicators inferred from header labels are structure-level hints only; they do not authorize row-value processing.

## Verification Chain

- data-scope proposal canonical baseline `f6bfa0dd4cc0bba0ad48d2bacc6ef5bb7bbbb311`;
- segmented HEAD preflight `34862117709` SUCCESS;
- segmented evidence CI `34862892612` SUCCESS;
- `$500+` contract CI `34863903807` SUCCESS;
- bounded inspector CI `34864249090` SUCCESS;
- structure-only one-shot `34864433849` SUCCESS;
- evidence closure `54f2e90b43cf98afb0c607f02c65fa510f71df2d`;
- evidence closure CI `34886584110` SUCCESS;
- promoted canonical baseline `89a5e626c2aa6bf98147522b83973ba62b6d0ccc`;
- canonical post-promotion CI `34887416658` SUCCESS.

## Remaining Readiness Gaps

Before source approval or any real row-level acquisition:
- minimized field whitelist from the verified 25 labels;
- explicit purpose/necessity assessment for potential PII fields;
- production retention duration/policy;
- trusted project privacy policy;
- real-acquisition client review against final field/privacy/transport controls;
- explicit human source-approval reference;
- separate policy `APPROVED` + registry activation gate;
- separately authorized real row-level acquisition;
- durable production audit persistence and physical retention enforcement;
- first PostgreSQL/Alembic application migration for production data.

## Next Recommended Action

Create an isolated, non-authorizing **field-minimization + PII-necessity + retention/privacy readiness proposal** using only the verified 25 field labels. No additional California SCO network/body access is required for that task.
