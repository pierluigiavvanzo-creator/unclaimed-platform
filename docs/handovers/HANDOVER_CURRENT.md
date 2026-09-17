# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ca-same-bytes-deeper-insurance-discovery-offline`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## D-010 Product Boundary

Accepted California MVP-1 policy:

`ROW_DEFER_CONTINUE_METADATA_ONLY`

Exact authority-backed insurance vocabulary:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN08, IN99`

Primary narrow MVP-1 target:

`IN03 — Proceeds Due Beneficiaries`

Nonconforming/unknown values remain unresolved and are represented only by aggregate defer evidence. They are not normalized, repaired, persisted, inferred or treated as non-insurance. Later rows may continue.

Transport/header/CSV-column/hard-cap failures remain fail-closed.

## Prior Live Result

One-shot D-010 module-mode run:

`35243232091` — attempt `1` — SUCCESS.

Persisted evidence:

`sources/evidence/ca_sco_mvp1_property_type_row_defer.module_live_once.v2.json`

Observed:

- HEAD: `1`;
- Range GET: `4`;
- HTTP total: `5`;
- source response-body bytes: `524288`;
- rows examined: `16` (`4/member`);
- deferred unclassifiable rows: `16`;
- shape-valid non-target: `0`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- distinct recognized insurance codes: `[]`;
- stop reason: none.

D-010 continuation is validated live. Insurance discovery was not observed in this tiny deterministic prefix sample, so California source activation remains HELD / NOT YET APPROVED. The source is not rejected.

The execution/privacy refs used for that run are consumed and non-reusable. Do not rerun them.

## Completed Offline Action

Executed:

`IMPLEMENT_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE`

Classification: `A — Product Critical`.

Implementation audit:

`docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE.md`

New runner:

`scripts/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

Blob:

`d7c7321aa01a86af346dfbe8c1d7cde6e91d1755`

Tests:

`tests/unit/test_ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

Blob:

`2ffd378a4b9a94eef8f68907b0dbd24660fbcb8b`

Implementation checkpoint before canonical state updates:

`e99aabf96954ae03eec7589079944b417145e969`

Implementation CI:

`35244998206` — SUCCESS.

No California source request occurred during this offline work.

## Same-Bytes Deeper Discovery Contract

The validator reuses the existing transport/archive parser, logical-record framing, strict CSV projection and D-010 classifier. The historical/live-validated D-010 runner was not modified.

Future live source-response envelope remains unchanged:

- HEAD max: `1`;
- Range GET max: `4`;
- HTTP total max: `5`;
- Range response bytes: `131072` each;
- source response-body bytes max total: `524288`;
- additional Range: false;
- full-body fallback: false.

Deeper logical scan caps:

- complete data rows max/member: `256`;
- complete data rows max/total: `1024`;
- previous depth: `4/member`, `16 total`;
- max logical-depth increase: `64x`.

Existing transient decompression caps are unchanged:

- uncompressed bytes max/member: `262144`;
- uncompressed bytes max/total: `1048576`;
- logical record bytes max: `32768`.

Only complete logical records are classified. A partial trailing record at the end of the fixed Range prefix is ignored without persistence or inference.

Allowed output/evidence remains limited to:

- aggregate row/classification counts;
- per-member rows examined;
- per-member scan status (`ROW_CAP_REACHED` or `PREFIX_EXHAUSTED_BEFORE_ROW_CAP`);
- exact recognized authority-backed insurance codes.

No raw source body/row, PROPERTY_ID, source PROPERTY_TYPE value/derivative, owner/holder value or PII is an allowed persistence output.

## Offline Test Evidence

Synthetic tests prove:

1. `IN03` after the previous four-row boundary is discovered;
2. exact `IN01`/`IN99` are recognized without inventing `IN03`;
3. the `256/member` hard cap prevents observation of row `257`;
4. the synthetic transport remains exactly `1 HEAD + 4 Range + 524288 source bytes`;
5. transport metadata drift remains fail-closed before Range reads;
6. module-mode CLI startup works offline;
7. full repository CI is green.

Reuse decision: `REUSE / WRAP` existing deterministic repository components; no new external dependency is warranted.

## Source / Product State

- adopted transport/archive baseline: CONFIRMED LIVE;
- California authority semantics: RESOLVED;
- D-010 row-defer continuation: VALIDATED LIVE;
- same-byte deeper insurance discovery validator: OFFLINE READY;
- current fresh execution/privacy refs: none;
- California source approval: HELD / NOT YET APPROVED;
- production classification: inactive;
- approved real sources: `0`;
- real MVP-1 candidates: `0`.

## Canonical Read Order Before Any New Change

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE.md`;
2. `scripts/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`;
3. `tests/unit/test_ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`;
4. `docs/audits/M3_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_LIVE_EVIDENCE_REVIEW.md`;
5. `sources/evidence/ca_sco_mvp1_property_type_row_defer.module_live_once.v2.json`;
6. D-010 in `DECISIONS.md`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_LIVE_VALIDATION_AUTHORIZATION`

Classification: `A — Product Critical`.

A new explicit Product Owner authorization is required before any source access. It may mint exactly:

1. one fresh single-use bounded execution approval;
2. one fresh single-use transient-row memory-only privacy approval covering at most `256 complete rows/member`, `1024 total`, under the unchanged source-response byte envelope.

The later one-shot live workflow must:

- pin the deeper runner blob and unchanged D-010 classifier/policy/transport baseline;
- invoke module mode;
- reject `run_attempt != 1`;
- consume fresh refs before source access;
- preserve `1 HEAD + 4 Range + 524288 source bytes` maximum;
- preserve uncompressed/logical-record caps;
- persist only aggregate counts/per-member scan metadata/exact recognized authority codes;
- remove workflow/trigger immediately after execution;
- never retry or reuse consumed refs.

After fresh authorization:

`one same-byte deeper live validation -> evidence/source decision -> if insurance observed, bounded CA source activation -> MVP-1 candidate -> economics -> reviewer`

Do not repeat the 16-row sample, widen source-response bytes, or reopen generic transport/CSV/PROPERTY_TYPE diagnostics absent new contradictory evidence.
