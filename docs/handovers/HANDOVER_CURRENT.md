# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before current implementation candidate: `6105c22a7d31df7afca00282eff7e9798e98b868`
- Current candidate: `m3-ca-sco-property-type-runner-implementation`
- Functional candidate HEAD before audit/docs closure: `d2b8977a0fd34474ecb545c6ecfefc354b551b30`
- Functional candidate CI: `34951460475` — SUCCESS
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
- SCO bounded `PROPERTY_TYPE` runner implementation CANDIDATE + SYNTHETIC/MOCK CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical `$500+` Facts

Source segment endpoint:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Transport identity from prior canonical evidence:
- Content-Length `162,416,884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- `Accept-Ranges: bytes`.

Four canonical DEFLATED, non-encrypted CSV members:
1. `From_500_To_Beyond_1_of_4.csv` — local-header offset `0`
2. `From_500_To_Beyond_2_of_4.csv` — `59,747,797`
3. `From_500_To_Beyond_3_of_4.csv` — `96,862,896`
4. `From_500_To_Beyond_4_of_4.csv` — `134,174,190`

Exact canonical header contains 25 columns. `PROPERTY_TYPE` is zero-based column index `1`.

No real CSV data row has yet been sampled.

## Canonical Semantic Purpose / Question

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

First-purpose field boundary:
- `PROPERTY_ID`
- `PROPERTY_TYPE`

During semantic verification, `PROPERTY_ID` use/persistence is prohibited; only `PROPERTY_TYPE` semantics are tested.

Semantic question:
Are bounded sampled `PROPERTY_TYPE` values NAUPA-style code tokens, and is every observed `IN`-prefixed value one of official SCO insurance codes `IN01-IN08` or `IN99`?

Proof boundary:
`SAMPLE_ONLY_DOES_NOT_PROVE_FULL_DATASET_DOMAIN_OR_GLOBAL_CODE_FREQUENCY`.

Production activation remains false for every outcome.

## Canonical Runner Design

Design:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_runner_design.v1.json`

Design schema:
`schemas/common/property_type_semantic_runner_design.schema.json`

Execution evidence schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

Canonical design functional SHA:
`62e32ebe38e218bbe4312f48ff2fa2eefb010df9`

Canonical runner-design CI:
`34947637509` — SUCCESS.

## Owner Implementation Authorization

Owner instruction:
`approvo implementazione bounded runner PROPERTY_TYPE con soli test synthetic/mock`

Approval reference:
`OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_SYNTHETIC_MOCK_ONLY`

Evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_runner_implementation_approval.v1.json`

Schema:
`schemas/common/property_type_semantic_runner_implementation_authorization.schema.json`

Authorized:
- runner implementation;
- synthetic/mock testing.

Not authorized:
- real network execution;
- network one-shot workflow;
- real row access;
- transient-row privacy exposure;
- source approval;
- registry activation.

## Current Candidate — Runner Implementation

Branch:
`m3-ca-sco-property-type-runner-implementation`

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Functional candidate HEAD before audit/docs closure:
`d2b8977a0fd34474ecb545c6ecfefc354b551b30`

At functional closure vs canonical:
- ahead `3`;
- behind `0`;
- merge-base exactly `6105c22a7d31df7afca00282eff7e9798e98b868`.

Implementation audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_IMPLEMENTATION.md`

Network one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

CURRENT: ABSENT.

## Runner Behavior

The runner core accepts an injected transport so tests can execute with no network. A fixed `HttpTransport` implementation exists for a later separately authorized real-execution gate, but it was not invoked in this task and is not wired into GitHub Actions.

Before transport access, `execute()` requires non-empty execution-approval and privacy-approval references.

Transport behavior:
- HTTPS fixed host/endpoint;
- exact HEAD metadata verification;
- one fixed Range GET per canonical member;
- `If-Match` with canonical ETag;
- no redirect behavior from `http.client`;
- non-206/ignored Range -> STOP before response body read;
- exact Content-Range validation;
- no fallback to full body.

ZIP/CSV behavior:
- exact canonical local member name and DEFLATE/no-encryption expectation;
- bounded incremental decompression;
- exact canonical 25-column header required;
- header + maximum first 4 complete data rows/member;
- byte-level CSV projection captures only `PROPERTY_TYPE` while counting columns;
- no semantic use/persistence of `PROPERTY_ID`;
- malformed/empty `PROPERTY_TYPE` -> STOP;
- unknown `IN`-prefixed code -> STOP.

## Exact Caps

- 4 members;
- 4 data rows/member maximum;
- 16 rows maximum total;
- 1 HEAD maximum;
- 4 Range GET maximum;
- 5 HTTP requests maximum total;
- 131,072 source bytes/Range maximum;
- 524,288 source bytes total maximum;
- 262,144 uncompressed transient bytes/member maximum;
- 1,048,576 uncompressed transient bytes total maximum;
- 32,768 bytes/logical record maximum;
- no extra Range;
- no full-body fallback;
- no automatic cap widening.

## Persistence / Privacy Boundary

Execution evidence may contain only derived values allowed by the canonical execution schema:
- aggregate sample rows examined;
- rows examined/member;
- distinct `PROPERTY_TYPE` codes;
- distinct official insurance codes;
- request/byte counters;
- semantic result status;
- stop reason;
- fixed safety flags and transport metadata.

Never persist/log:
- raw Range body;
- full CSV row;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE` values.

Real CSV parsing may still transiently expose prohibited owner/holder bytes. Therefore actual real execution remains blocked until separate transient-row privacy approval.

## Synthetic / Mock Tests

Tests use only synthetic in-memory DEFLATE member prefixes and mock transport.

Covered:
- official insurance-code success sample;
- no-insurance inconclusive sample;
- unknown insurance prefix code -> fail closed;
- ignored Range/non-206 -> body read count remains zero;
- header mismatch;
- row column-count mismatch;
- missing privacy approval before transport;
- missing execution approval before transport;
- explicit live-network CLI opt-in;
- network workflow absence;
- execution evidence schema validation.

## CI History

Initial implementation commit:
`2679964f8bd99893c2545faa1b153bc73f0adb00`

Run `34950942449`:
- Streamlit SUCCESS;
- quality FAILED at Ruff only because `Mapping` was imported from `typing`.

Lint-fix commit:
`773dc427a8be4d97807c74fdf73c08692a35ac7c`

Run `34951326633`:
- Ruff PASS;
- mypy PASS;
- contract FAILED because an older semantic-proposal test still asserted permanent runner absence.

Historical-contract fix commit:
`d2b8977a0fd34474ecb545c6ecfefc354b551b30`

Run `34951460475`:
- Ruff PASS;
- mypy PASS;
- contract PASS;
- smoke PASS;
- full pytest PASS, including new runner unit tests;
- frontend install/lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS;
- overall SUCCESS for both jobs.

No force-push/history rewrite was used.

## Real Network / Data Access During Implementation

- new SCO requests: `0`;
- new SCO response-body bytes: `0`;
- real CSV rows read: `0`;
- real PII processed: `0`;
- network workflow created: `false`.

## Current Governance State

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

Runner implementation is authorized only in the synthetic/mock candidate scope. Real semantic execution, real row access, transient-row privacy exposure, PII processing, identity resolution, beneficiary matching and outreach remain BLOCKED.

## SINGLE NEXT ACTION

`HUMAN_PROPERTY_TYPE_RUNNER_CANDIDATE_PROMOTION`

If the owner approves, promote:
`m3-ca-sco-property-type-runner-implementation -> m2-state-governance-core`

Promotion must be a non-force fast-forward after ancestry verification and must remain non-executing.

Even after promotion, actual bounded real SCO semantic sampling requires another explicit owner execution approval **and** transient-row privacy approval. No real row may be read before those later gates.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
M3 two-field privacy boundary: CANONICAL + CI VERIFIED
M3 PROPERTY_TYPE semantic proposal: CANONICAL + CI VERIFIED
M3 runner design: CANONICAL + CI VERIFIED
M3 runner implementation: CANDIDATE + SYNTHETIC/MOCK CI VERIFIED
Canonical dev HEAD before candidate: 6105c22a7d31df7afca00282eff7e9798e98b868
Candidate branch: m3-ca-sco-property-type-runner-implementation
Functional candidate SHA: d2b8977a0fd34474ecb545c6ecfefc354b551b30
Functional candidate CI: 34951460475 SUCCESS
Rows cap: 16 total / 4 per member
Range cap: 4
Source-body cap: 524288 bytes
Full-body fallback: false
Runner: PRESENT ON CANDIDATE
Network workflow: ABSENT
New SCO network/body access: 0
Real semantic execution: BLOCKED
Transient-row privacy approval: MISSING
Real row access: BLOCKED
Real PII: BLOCKED
Matching: BLOCKED
Outreach: BLOCKED
SCO policy: PROPOSED
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: HUMAN_PROPERTY_TYPE_RUNNER_CANDIDATE_PROMOTION
CONTEXT HEALTH: coherent; repository is source of truth
```
