# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, California SCO source
governance, transport-preflight evidence, source-approval readiness, and the non-authorizing data-scope
inspection proposal are canonical and CI verified on `m2-state-governance-core`.

Canonical development branch before the current candidate:
`m2-state-governance-core` @ `f6bfa0dd4cc0bba0ad48d2bacc6ef5bb7bbbb311`.

Current isolated candidate branch:
`m3-ca-sco-500-plus-range-inspection`.

The candidate has now completed an owner-authorized, structure-only inspection of the official
California SCO `$500 and up` ZIP. The inspection used HTTP Range GET only, read 393,216 source-body
bytes in total, parsed zero CSV data rows, persisted no raw body bytes, and did not perform identity
resolution, beneficiary matching, outreach, or source approval.

Evidence closure commit:
`54f2e90b43cf98afb0c607f02c65fa510f71df2d`.

Evidence closure CI:
`34886584110` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

Streamlit Community Cloud remains the active reviewer deployment target. Repository-side Vercel
integration remains decommissioned. Supabase remains untouched.

## California SCO Segmented Strategy

Metadata-only preflight established four official value-segment ZIPs. The `$500 and up` object was
selected as the pilot target because it is the smallest observed segment and is aligned with an
initial high-value pilot strategy. This is a product prioritization decision, not a claim that every
record is commercially viable or insurance-related.

Observed `$500+` transport evidence:

- endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- HTTP status: `200`;
- content type: `application/zip`;
- content length: `162,416,884` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:34 GMT`.

The full `All properties` archive remains reference-only for the pilot and was not downloaded.

## Executed $500+ Structure Inspection

Owner-authorized one-shot execution:

- execution workflow commit: `40c5ff8c78cdf03f60dcce73ad1c12c5f4466994`;
- workflow run: `34864433849` — SUCCESS;
- approval ref:
  `OWNER_CHAT_APPROVAL_2026-09-14T17:21+02:00_BOUNDED_DATA_SCOPE_INSPECTION`;
- result: `SUCCEEDED_STRUCTURE_ONLY`;
- stop reason: `null`;
- range requests: `5`, all HTTP `206`;
- total response-body bytes read: `393,216`;
- full archive downloaded: `false`;
- CSV data rows parsed: `0`;
- record values persisted: `false`.

Exact evidence is persisted at:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Audit:
`docs/audits/M3_CA_SCO_500_PLUS_DATA_SCOPE_EXECUTION.md`.

The temporary network workflow was removed immediately after evidence capture and its absence is
contract-tested.

## Verified Archive Structure

The `$500+` ZIP contains four non-encrypted, DEFLATED CSV members:

1. `From_500_To_Beyond_1_of_4.csv`
2. `From_500_To_Beyond_2_of_4.csv`
3. `From_500_To_Beyond_3_of_4.csv`
4. `From_500_To_Beyond_4_of_4.csv`

ZIP64 was not required. No unsafe-path, encryption, unsupported-compression, range-behavior, or budget
stop condition fired.

## Verified Header Candidate Structure

All four CSV members produced the same high-confidence, comma-delimited UTF-8 header candidate with
25 labels:

- `PROPERTY_ID`
- `PROPERTY_TYPE`
- `CASH_REPORTED`
- `SHARES_REPORTED`
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
- `CURRENT_CASH_BALANCE`
- `NUMBER_OF_PENDING_CLAIMS`
- `NUMBER_OF_PAID_CLAIMS`
- `HOLDER_NAME`
- `HOLDER_STREET_1`
- `HOLDER_STREET_2`
- `HOLDER_STREET_3`
- `HOLDER_CITY`
- `HOLDER_STATE`
- `HOLDER_ZIP`
- `CUSIP`

This verifies archive/header structure only. No data row was sampled, so actual record values,
population rates, row-level consistency, and semantic/legal necessity of individual fields remain
unverified.

## Privacy / PII Interpretation

The deterministic header heuristic marked owner/holder/name/address-related labels as potential PII
indicators. This is a structure-level classification hint only. It is not a legal determination and
does not authorize processing of any record value.

Current authorization state remains:

- source-access policy: `PROPOSED`;
- real acquisition authorized: `false`;
- source registry `enabled`: `false`;
- source registry `approved_for_use`: `false`;
- approved real sources: `0`;
- real PII processing authorized: `false`;
- identity resolution: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED.

## Verification Evidence

- data-scope proposal canonical baseline: `f6bfa0dd4cc0bba0ad48d2bacc6ef5bb7bbbb311`;
- segmented metadata preflight run: `34862117709` — SUCCESS;
- segmented evidence CI after formatting fix: `34862892612` — SUCCESS;
- `$500+` contract CI: `34863903807` — SUCCESS;
- bounded range-inspector implementation CI: `34864249090` — SUCCESS;
- one-shot structure execution run: `34864433849` — SUCCESS;
- evidence closure commit: `54f2e90b43cf98afb0c607f02c65fa510f71df2d`;
- evidence closure CI: `34886584110` — SUCCESS;
- Ruff, mypy, contract tests, smoke tests, full pytest: PASS;
- legacy frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

## Resolved Readiness Gap

Resolved by this execution:

- actual `$500+` archive member count and member names;
- compression/encryption structure;
- consistent 25-column header candidate across all four CSV files;
- structure-level potential PII indicators;
- proof that structure inspection can be completed using ~384 KiB rather than downloading the full
  162 MB segment or 3.2 GB complete archive.

## Remaining Readiness Gaps

Still required before source approval or row-level acquisition:

- minimized field whitelist selected from the verified 25 labels;
- explicit purpose/necessity assessment for potential PII fields;
- production retention duration/policy;
- trusted project privacy policy;
- reviewed real-acquisition client against the final field/privacy/transport controls;
- explicit human source-approval reference;
- policy transition to `APPROVED` under a separate gate;
- registry activation under a separate gate;
- separately authorized real row-level acquisition;
- durable production audit persistence and physical retention enforcement;
- first PostgreSQL/Alembic application migration for production data.

No additional source-body access is needed to prepare the next readiness proposal.

## Next Recommended Action

**Human promotion gate only:** decide whether to promote verified candidate branch
`m3-ca-sco-500-plus-range-inspection` into canonical `m2-state-governance-core`.

Promotion records the verified structure evidence and does not authorize source approval, registry
activation, record-value access, real PII processing, identity resolution, beneficiary matching or
outreach.

After promotion, create an isolated, non-authorizing **field-minimization + PII-necessity +
retention/privacy readiness proposal** based only on the verified 25-label structure. That next task
requires no California SCO body/network access.
