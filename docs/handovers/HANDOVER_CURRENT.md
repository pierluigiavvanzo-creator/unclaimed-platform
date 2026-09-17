# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ca-same-bytes-deeper-live-validation-once`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Canonical Read Order

Before any new change read, in order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect the task-relevant artifacts named below.

## D-010 Boundary

Policy remains:

`ROW_DEFER_CONTINUE_METADATA_ONLY`

Exact California authority-backed insurance vocabulary:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN08, IN99`

Primary narrow MVP-1 target remains:

`IN03 — Proceeds Due Beneficiaries`

D-010 is unchanged: no trimming, normalization, repair, uppercasing, regex relaxation, semantic inference, per-row/source-value persistence or row-specific human inspection. Nonconforming/unknown values are `DEFER_UNCLASSIFIABLE` and only aggregate completeness evidence persists.

## Same-Bytes Deeper Validator

Runner:

`scripts/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

Pinned blob:

`d7c7321aa01a86af346dfbe8c1d7cde6e91d1755`

Classifier blob:

`05e8637e42070dd6f04218592d20d4a230ab948e`

Policy blob:

`840d09d87187c53d26f4d562527dcb92d810a9f3`

Transport/archive runner blob:

`706183d5425da16b25f8186574cc356135803326`

The runner keeps the source-response envelope fixed at `1 HEAD + 4 Range + 524288 bytes` while allowing up to `256 complete rows/member`, `1024 total` under unchanged transient decompression and logical-record caps.

## Fresh Authorization Lifecycle — Completed

Owner authorization:

`APPROVO FRESH SAME-BYTES DEEPER LIVE VALIDATION + TRANSIENT-ROW PRIVACY — 256/MEMBER, 1024 TOTAL, 524288 SOURCE BYTES MAX`

Authorization base:

- branch: `mvp1-ca-same-bytes-deeper-insurance-discovery-offline`;
- HEAD: `eebb18693c9a75de4d060bdfeb38d98d0975ccfc`;
- CI: `35245311115` — SUCCESS.

Authorization checkpoint:

`888ec27ffc7563698dbf84c3a454a5964a015c90`

Fresh refs:

- execution: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_REAL_SOURCE_VALIDATION_BOUNDED_D4F29A61`;
- privacy: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_TRANSIENT_ROW_PRIVACY_BOUNDED_D4F29A61`.

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Do not retry, rerun or reuse them.

Machine record:

`sources/evidence/ca_sco_mvp1_same_bytes_deeper_insurance_discovery_live_validation_approval.v1.json`

Authorization audit:

`docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_LIVE_VALIDATION_AUTHORIZATION.md`

## One-Shot Live Execution — Completed

Trigger commit:

`85a33d7fdbd1ab1487e8b47c54e83a5f64051ff0`

Workflow run:

`35255228459` — attempt `1` — SUCCESS.

Lifecycle:

1. checkout/setup: PASS;
2. module-mode startup: PASS;
3. exact authorization/blob/bounds preflight: PASS;
4. fresh refs consumed and pushed before source access: PASS;
5. exactly one same-bytes deeper live execution: PASS;
6. privacy/hard-cap evidence validation: PASS;
7. derived evidence persistence/upload: PASS;
8. workflow + trigger cleanup: COMPLETE.

Persisted evidence commit from GitHub Actions:

`df5a28191f9bbb54da51374fb6bab60b9303b650`

Cleanup commits:

- workflow removal: `3c0fc265d7732c9e1d8d20fd021d7712908107f0`;
- trigger removal: `84d32e105d3a044cc31900597ca8f53d4386fbae`.

No live one-shot workflow remains armed.

## Live Evidence

Evidence:

`sources/evidence/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.module_live_once.v1.json`

Evidence review:

`docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_LIVE_EVIDENCE_REVIEW.md`

Observed transport:

- HEAD status: `200`;
- content length: `162560390`;
- content type: `application/zip`;
- accept-ranges: `bytes`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- last-modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

Exact source use:

- HEAD: `1`;
- Range GET: `4`;
- HTTP total: `5`;
- source-response bytes: `524288`;
- no additional Range;
- no full-body fallback.

Logical scan:

- `256` rows in each of the four canonical members;
- `1024` total;
- all member scan statuses: `ROW_CAP_REACHED`.

Classification:

- deferred unclassifiable: `1024`;
- shape-valid non-target: `0`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- distinct recognized insurance codes: `[]`;
- semantic result: `NO_INSURANCE_CODE_OBSERVED_IN_BOUNDED_SAMPLE`;
- stop reason: `null`.

## Privacy State

PASS.

No raw source body/row, `PROPERTY_ID`, per-row/source `PROPERTY_TYPE`, owner/holder value, identity resolution, beneficiary matching, outreach or production classification activation was persisted or performed.

## Product Interpretation

D-010 continuation and the transport/archive path remain technically valid. The live deeper scan increased logical depth `64x` over the earlier 16-row run without increasing source-response bytes.

However, all `1024/1024` examined rows remained unclassifiable under the unchanged authority-backed boundary and no exact insurance code was observed.

Do **not** infer that the entire California source contains no insurance records. The source remains held, not rejected.

For MVP-1 prioritization, the current California SCO `PROPERTY_TYPE` discovery path is now **frozen pending genuinely new evidence or a separately justified authority-backed interpretation path**. Do not repeat or simply widen the same scan.

Current state:

- California source approval: HELD / NOT YET APPROVED;
- CA `PROPERTY_TYPE` discovery path: FROZEN FOR MVP-1 PENDING NEW EVIDENCE;
- approved real sources: `0`;
- production classification: inactive;
- real MVP-1 candidates: `0`.

## Task-Relevant Artifacts for Next Work

Inspect at least:

1. `PRODUCT_STRATEGY_MVP1.md`;
2. `sources/registry.yaml`;
3. `docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_LIVE_EVIDENCE_REVIEW.md`;
4. `sources/evidence/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.module_live_once.v1.json`;
5. `docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE.md`;
6. D-010 in `DECISIONS.md`.

## SINGLE NEXT ACTION

Execute exclusively:

`BENCHMARK_MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_OFFLINE`

Classification: `A — Product Critical`.

Goal:

Benchmark concrete alternative lawful public/authorized source paths and select the shortest credible path to the first approved real source and first insurance candidate.

Compare at minimum:

- authority and provenance quality;
- insurance-specific signal available before identity work;
- machine accessibility and stability;
- privacy/PII burden;
- source/acquisition cost;
- update cadence;
- integration effort and reuse opportunities;
- expected time-to-first-candidate;
- commercial relevance to MVP-1.

This action is research/offline only. It does not authorize a new California request or any other real-source acquisition. Any later live source use requires the applicable fresh authorization gate.

Do not repeat the 16-row or 1024-row California scan and do not reopen generic transport/CSV/PROPERTY_TYPE diagnostics absent genuinely new evidence.
