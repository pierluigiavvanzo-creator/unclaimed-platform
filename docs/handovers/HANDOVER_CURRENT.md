# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before current candidate: `c1b7482cd2e0155c0763b80846a2ec1361173b8e`
- Current candidate: `m3-ca-sco-property-type-runner-design`
- Functional candidate HEAD: `b0824d7cbbe693b1d75f3564abac458bcbc5d5e0`
- Functional candidate CI: `34946533156` — SUCCESS
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
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical `$500+` Evidence

Evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`

Verified:
- four non-encrypted DEFLATED CSV members;
- identical canonical 25-label header;
- local-header offsets:
  1. `From_500_To_Beyond_1_of_4.csv` — `0`
  2. `From_500_To_Beyond_2_of_4.csv` — `59,747,797`
  3. `From_500_To_Beyond_3_of_4.csv` — `96,862,896`
  4. `From_500_To_Beyond_4_of_4.csv` — `134,174,190`
- prior structure-only execution read `393,216` source bytes;
- full archive false;
- data rows parsed `0`.

No real CSV data row has yet been sampled.

## Canonical Semantic Proposal

Proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`

Question:
Are bounded sampled `PROPERTY_TYPE` values NAUPA-style code tokens, and is every observed `IN`-prefixed
value one of official SCO insurance codes `IN01-IN08` or `IN99`?

Proof boundary:
`SAMPLE_ONLY_DOES_NOT_PROVE_FULL_DATASET_DOMAIN_OR_GLOBAL_CODE_FREQUENCY`.

Production activation remains false for every outcome.

## Current Candidate — Runner Design

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

## Reuse-First Decision

Use:
- existing `scripts/ca_sco_500_plus_data_scope_inspection.py` Range/transport/ZIP primitives;
- Python standard library `http.client`, `ssl`, `struct`, `zlib`, `csv`, `re`, `json`, `pathlib`.

Do not add `remotezip`:
- it is a mature MIT Python option and Python 3.11 compatible;
- the repository already has a verified smaller implementation;
- this project requires exact hard request/byte budgets and explicit no-fallback behavior.

Do not use `Papyrine/RemoteZip`:
- C#/.NET;
- documented full-buffer fallback when Range is ignored is incompatible with fail-closed behavior.

No new dependency was added.

## Future Runner Boundary

Planned path:
`scripts/ca_sco_property_type_semantic_verification.py`

CURRENT: ABSENT.

Planned one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

CURRENT: ABSENT.

The runner must require separate non-empty execution and transient-row privacy approval references before
network activity.

Endpoint is fixed:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Transport identity remains:
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

`PROPERTY_TYPE`:
zero-based index `1`.

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

Before real execution:
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

## Candidate Verification

Functional HEAD:
`b0824d7cbbe693b1d75f3564abac458bcbc5d5e0`

CI:
`34946533156` — SUCCESS.

Passed:
- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- frontend install/lint/typecheck/build;
- Streamlit safety/startup smoke.

Diff:
- ahead `1`;
- behind `0`;
- merge-base canonical `c1b7482cd2e0155c0763b80846a2ec1361173b8e`;
- six added design-only files.

No SCO network/body access occurred.

## Authorization State

- source policy: `PROPOSED`;
- registry: disabled + not approved;
- approved real sources: `0`;
- runner implementation: NOT AUTHORIZED;
- semantic execution: BLOCKED;
- transient-row privacy approval: ABSENT;
- real row access: BLOCKED;
- real PII: BLOCKED;
- matching: BLOCKED;
- outreach: BLOCKED.

## SINGLE NEXT ACTION

`HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL`

This gate may authorize implementation of the bounded runner on a new candidate and synthetic/mock
testing only.

It must NOT authorize:
- a network one-shot workflow;
- a real SCO request;
- reading a real CSV row;
- transient PII exposure.

Actual one-shot semantic execution remains a later separate human gate plus transient-row privacy
approval.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
M3 two-field privacy boundary: CANONICAL + CI VERIFIED
M3 PROPERTY_TYPE semantic proposal: CANONICAL + CI VERIFIED
M3 runner design: CANDIDATE + CI VERIFIED
Canonical base: c1b7482cd2e0155c0763b80846a2ec1361173b8e
Candidate: m3-ca-sco-property-type-runner-design
Candidate SHA: b0824d7cbbe693b1d75f3564abac458bcbc5d5e0
Candidate CI: 34946533156 SUCCESS
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
