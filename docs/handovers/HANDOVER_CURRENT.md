# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Promoted runner-design functional SHA: `62e32ebe38e218bbe4312f48ff2fa2eefb010df9`
- Canonical post-promotion CI: `34947637509` — SUCCESS
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` — unchanged
- Never develop directly on `main`.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition/raw persistence/privacy CANONICAL + VERIFIED.
- Streamlit reviewer CANONICAL + CI VERIFIED.
- SCO source governance CANONICAL + CI VERIFIED.
- SCO transport/source-approval/data-scope readiness CANONICAL + CI VERIFIED.
- SCO segmented transport evidence CANONICAL + CI VERIFIED.
- SCO `$500+` bounded structure inspection EXECUTED + CANONICAL + CI VERIFIED.
- SCO two-field field/privacy boundary CANONICAL + CI VERIFIED.
- SCO `PROPERTY_TYPE` semantic-verification proposal CANONICAL + CI VERIFIED.
- SCO bounded `PROPERTY_TYPE` runner design CANONICAL + CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical `$500+` Evidence

Evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`

Verified:
- four non-encrypted DEFLATED CSV members;
- identical canonical 25-label header;
- prior structure-only execution read `393,216` source bytes;
- data rows parsed `0`.

No real CSV data row has yet been sampled.

## Canonical Semantic Proposal

Proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`

Question:
Are bounded sampled `PROPERTY_TYPE` values NAUPA-style code tokens, and is every observed `IN`-prefixed value one of official SCO insurance codes `IN01-IN08` or `IN99`?

Proof boundary:
`SAMPLE_ONLY_DOES_NOT_PROVE_FULL_DATASET_DOMAIN_OR_GLOBAL_CODE_FREQUENCY`.

Production activation remains false for every outcome.

## Canonical Runner Design

Design:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_runner_design.v1.json`

Schema:
`schemas/common/property_type_semantic_runner_design.schema.json`

Execution evidence schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

Synthetic examples:
`schemas/examples/ca_sco_500_plus_property_type_semantic_verification_execution.examples.json`

Test:
`tests/contract/test_ca_sco_property_type_semantic_runner_design.py`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_DESIGN_REVIEW.md`

Status:
`DESIGN_REVIEW_ONLY_NOT_IMPLEMENTATION_AUTHORIZED`.

Promoted functional SHA:
`62e32ebe38e218bbe4312f48ff2fa2eefb010df9`.

Canonical post-promotion CI:
`34947637509` — SUCCESS for `quality` and `streamlit-candidate`.

## Future Runner Boundary

Planned path:
`scripts/ca_sco_property_type_semantic_verification.py`

CURRENT: ABSENT.

Planned one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

CURRENT: ABSENT.

The runner must require separate non-empty execution and transient-row privacy approval references before any future real network activity.

Endpoint remains fixed:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Transport identity:
- Content-Length `162,416,884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- `Accept-Ranges: bytes`;
- HTTPS only;
- redirects denied;
- `If-Match` required;
- timeout 10 seconds.

## Exact Caps

- 4 members;
- first 4 complete data rows/member;
- 16 rows maximum total;
- 1 HEAD maximum;
- 4 Range GET maximum;
- 5 HTTP requests maximum total;
- 131,072 source bytes/Range maximum;
- 524,288 source bytes total maximum;
- 262,144 uncompressed transient bytes/member maximum;
- 1,048,576 uncompressed transient bytes total maximum;
- 32,768 bytes/logical CSV record maximum;
- no extra Range if sample incomplete;
- no full-body fallback;
- no automatic cap widening.

If Range is ignored/non-206:
STOP before reading unexpected body.

## Header / Row Rules

Exact canonical header has 25 columns.

`PROPERTY_TYPE` zero-based index:
`1`.

Code shape:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Official insurance values:
`IN01`, `IN02`, `IN03`, `IN04`, `IN05`, `IN06`, `IN07`, `IN08`, `IN99`.

Unknown `IN`-prefixed code:
STOP fail closed.

`PROPERTY_ID` use:
false during semantic verification.

Nonallowlisted field use:
false.

## Privacy / Persistence

CSV row parsing may transiently expose prohibited owner/holder columns. This remains separately gated.

Before any future real execution:
- transient-row privacy approval is mandatory;
- buffers in memory only;
- retention `0 days`;
- immediate disposal after projection or STOP.

Never persist/log:
- raw Range body;
- full row;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE`.

Future derived evidence may persist only:
- sample rows examined;
- rows examined/member;
- distinct `PROPERTY_TYPE` codes;
- distinct official insurance codes;
- transport/request byte counters;
- semantic result status;
- stop reason.

## Promotion Evidence

Before promotion:
- canonical `c1b7482cd2e0155c0763b80846a2ec1361173b8e`;
- candidate `62e32ebe38e218bbe4312f48ff2fa2eefb010df9`;
- ahead `2`;
- behind `0`;
- merge-base exactly `c1b7482cd2e0155c0763b80846a2ec1361173b8e`.

Owner explicitly approved:
`m3-ca-sco-property-type-runner-design -> m2-state-governance-core`.

Promotion was a non-force fast-forward to:
`62e32ebe38e218bbe4312f48ff2fa2eefb010df9`.

Canonical post-promotion CI:
`34947637509` — SUCCESS.

No source approval, registry activation, row-level acquisition, PII processing, identity resolution, matching or outreach was authorized by this promotion.

## Canonical Authorization State — UNCHANGED

SCO source policy remains:
- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `authorized_processing_purposes: []`;
- `allowed_fields: []`;
- `allow_pii: false`.

Registry remains:
- `enabled: false`;
- `approved_for_use: false`.

Approved real sources: `0`.

Runner implementation, semantic execution, real row access, PII processing, identity resolution, beneficiary matching and outreach remain BLOCKED.

## SINGLE NEXT ACTION

`HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL`

This gate may authorize implementation of the bounded runner on a new candidate and synthetic/mock testing only.

It must NOT authorize:
- a network one-shot workflow;
- a real SCO request;
- reading a real CSV row;
- transient PII exposure.

Actual one-shot semantic execution remains a later separate human gate plus transient-row privacy approval.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
M3 two-field privacy boundary: CANONICAL + CI VERIFIED
M3 PROPERTY_TYPE semantic proposal: CANONICAL + CI VERIFIED
M3 runner design: CANONICAL + CI VERIFIED
Runner-design functional SHA: 62e32ebe38e218bbe4312f48ff2fa2eefb010df9
Canonical promotion CI: 34947637509 SUCCESS
Rows cap: 16 total / 4 per member
Range cap: 4
Source-body cap: 524288 bytes
Full-body fallback: false
Runner: ABSENT
Network workflow: ABSENT
New SCO network/body access: 0
Implementation approval: MISSING
Semantic execution: BLOCKED
Transient-row privacy approval: MISSING
Real row access: BLOCKED
Real PII: BLOCKED
Matching: BLOCKED
Outreach: BLOCKED
SCO policy: PROPOSED
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL
CONTEXT HEALTH: coherent; repository is source of truth
```
