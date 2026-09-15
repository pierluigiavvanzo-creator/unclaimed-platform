# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Promoted runner-implementation functional SHA: `3f612837e4dbb86839942555c34b9384ff4e99a1`
- Canonical post-promotion CI: `34961511401` — SUCCESS
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
- SCO bounded `PROPERTY_TYPE` runner implementation CANONICAL + SYNTHETIC/MOCK CI VERIFIED.
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

Semantic proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`

Question:
Are bounded sampled `PROPERTY_TYPE` values NAUPA-style code tokens, and is every observed `IN`-prefixed value one of official SCO insurance codes `IN01-IN08` or `IN99`?

Proof boundary:
`SAMPLE_ONLY_DOES_NOT_PROVE_FULL_DATASET_DOMAIN_OR_GLOBAL_CODE_FREQUENCY`.

Production activation remains false for every outcome.

## Canonical Runner Implementation

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Promoted functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`.

Implementation authorization evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_runner_implementation_approval.v1.json`

Implementation audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_IMPLEMENTATION.md`

Execution evidence schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

Network one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

CURRENT: ABSENT.

The runner core accepts injected transport and has been exercised only with synthetic in-memory ZIP/DEFLATE fixtures and mock transport. A fixed `HttpTransport` exists for a later separately authorized real execution gate but has not been invoked for SCO during implementation or promotion.

Before transport access, runtime requires non-empty execution and privacy approval references.

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
- no extra Range;
- no full-body fallback;
- no automatic cap widening.

If Range is ignored/non-206: STOP before reading the unexpected body.

## Header / Row Rules

Exact canonical header has 25 columns.

`PROPERTY_TYPE` zero-based index: `1`.

Code shape:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Official insurance values:
`IN01`, `IN02`, `IN03`, `IN04`, `IN05`, `IN06`, `IN07`, `IN08`, `IN99`.

Unknown `IN`-prefixed code: STOP fail closed.

`PROPERTY_ID` use during semantic verification: false.

Nonallowlisted field semantic use: false.

## Privacy / Persistence

Real CSV parsing may transiently expose prohibited owner/holder bytes. This remains separately gated.

Before any future real execution:
- explicit semantic execution approval is mandatory;
- transient-row privacy approval is mandatory;
- buffers remain in memory only;
- retention is `0 days`;
- disposal is immediate after projection or STOP.

Never persist/log:
- raw Range body;
- full row;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE`.

Derived evidence may contain only:
- sample rows examined;
- rows examined/member;
- distinct `PROPERTY_TYPE` codes;
- distinct official insurance codes;
- transport/request byte counters;
- semantic result status;
- stop reason;
- fixed safety flags and transport metadata allowed by schema.

## Promotion Evidence

Before promotion:
- canonical `6105c22a7d31df7afca00282eff7e9798e98b868`;
- candidate `3f612837e4dbb86839942555c34b9384ff4e99a1`;
- ahead `4`;
- behind `0`;
- merge-base exactly `6105c22a7d31df7afca00282eff7e9798e98b868`.

Owner explicitly approved:
`m3-ca-sco-property-type-runner-implementation -> m2-state-governance-core`.

Promotion used `force:false` and fast-forwarded canonical to:
`3f612837e4dbb86839942555c34b9384ff4e99a1`.

Canonical post-promotion CI:
`34961511401` — SUCCESS for `quality` and `streamlit-candidate`.

CI history retained:
- `34950942449` — quality failed at Ruff import rule only;
- `34951326633` — contract failed because historical proposal test still asserted permanent runner absence;
- `34951460475` — functional implementation SUCCESS;
- `34951888095` — candidate docs closure SUCCESS;
- `34961511401` — canonical post-promotion SUCCESS.

No force-push/history rewrite was used.

## Real Network / Data Access During Implementation + Promotion

- new SCO requests: `0`;
- new SCO response-body bytes: `0`;
- real CSV rows read: `0`;
- real PII processed: `0`;
- network workflow created: `false`.

## Canonical Authorization State

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

Runner implementation is canonical, but this does NOT authorize real execution. Real semantic execution, real row access, transient-row privacy exposure, PII processing, identity resolution, beneficiary matching and outreach remain BLOCKED.

## SINGLE NEXT ACTION

`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`

This gate must decide whether to authorize a bounded real semantic run. Any authorization must still include a separate explicit transient-row privacy approval before the runner can read any real CSV row.

Until then, do NOT:
- create/enable the one-shot network workflow;
- make a real SCO request;
- read a real CSV row;
- approve the source or registry;
- process identity, matching or outreach.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
M3 two-field privacy boundary: CANONICAL + CI VERIFIED
M3 PROPERTY_TYPE semantic proposal: CANONICAL + CI VERIFIED
M3 runner design: CANONICAL + CI VERIFIED
M3 runner implementation: CANONICAL + SYNTHETIC/MOCK CI VERIFIED
Promoted functional SHA: 3f612837e4dbb86839942555c34b9384ff4e99a1
Canonical promotion CI: 34961511401 SUCCESS
Rows cap: 16 total / 4 per member
Range cap: 4
Source-body cap: 524288 bytes
Full-body fallback: false
Runner: PRESENT CANONICAL
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
NEXT: HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW
CONTEXT HEALTH: coherent; repository is source of truth
```
