# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ca-same-bytes-deeper-insurance-discovery-offline`

Latest product-critical lifecycle:

`D010_CONTINUATION_VALIDATED_LIVE -> INSURANCE_NOT_OBSERVED_IN_16_ROWS -> SAME_BYTES_DEEPER_VALIDATOR_IMPLEMENTED_OFFLINE -> FRESH_LIVE_AUTHORIZATION_NEXT`

Classification: `A — Product Critical`.

Offline implementation audit:

`docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE.md`

## Prior Live Evidence

Run:

`35243232091` — attempt `1` — SUCCESS.

Persisted derived evidence:

`sources/evidence/ca_sco_mvp1_property_type_row_defer.module_live_once.v2.json`

Observed:

- HEAD `1`;
- Range GET `4`;
- source body bytes `524288`;
- rows examined `16` (`4/member`);
- `DEFER_UNCLASSIFIABLE`: `16`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- stop reason: none.

D-010 continuation is therefore validated live, but source activation remains held because the tiny deterministic sample did not demonstrate insurance discovery.

The approvals used for that run remain consumed/non-reusable. No retry is authorized.

## Same-Bytes Deeper Validator

New runner:

`scripts/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

Runner blob:

`d7c7321aa01a86af346dfbe8c1d7cde6e91d1755`

Tests:

`tests/unit/test_ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

Test blob:

`2ffd378a4b9a94eef8f68907b0dbd24660fbcb8b`

Implementation CI:

`35244998206` — SUCCESS.

The validator reuses the existing transport/archive/parser/projector and D-010 classifier. The historical live-validated D-010 runner remains unchanged.

## Bounded Discovery Contract

Future live source-response envelope remains unchanged:

- HEAD max: `1`;
- Range GET max: `4`;
- HTTP max total: `5`;
- bytes per Range: `131072`;
- source body bytes total: `524288`;
- additional Range: false;
- full-body fallback: false.

Logical row depth increases only within those same bytes:

- complete data rows max/member: `256`;
- complete data rows max/total: `1024`;
- prior depth: `4/member`, `16 total`;
- maximum logical-depth increase: `64x`.

Existing transient caps remain unchanged:

- uncompressed bytes/member: `262144`;
- uncompressed bytes total: `1048576`;
- logical record bytes: `32768`.

Only complete logical records are classified. An incomplete trailing record inside the fixed prefix is ignored without persistence or inference.

D-010 remains unchanged:

- nonconforming/unknown PROPERTY_TYPE -> `DEFER_UNCLASSIFIABLE`;
- no normalization/regex relaxation/repair;
- exact insurance vocabulary `IN01-IN08`, `IN99`;
- `IN03` remains primary MVP-1 target;
- only aggregate counts, per-member scan metadata and exact recognized authority-backed insurance codes are allowed as discovery evidence;
- no raw row/body, PROPERTY_ID, source PROPERTY_TYPE or owner/holder persistence.

## Offline Acceptance Evidence

Synthetic regression coverage proves:

- insurance can be discovered after the previous four-row boundary;
- `IN03` is detected when present deeper in the same prefix;
- `IN01`/`IN99` are detected without inventing `IN03`;
- row `257` is not observed when the `256/member` cap is reached;
- transport drift remains fail-closed before Range reads;
- source response-byte budget remains exactly unchanged.

No California network request occurred in this work package.

## Product / Source State

- transport/archive baseline: **CONFIRMED LIVE**;
- California authority vocabulary: **RESOLVED**;
- D-010 row-defer semantics: **VALIDATED LIVE**;
- same-byte deeper discovery validator: **OFFLINE READY**;
- California source activation: **HELD / NOT YET APPROVED**;
- approved real sources: `0`;
- production classification: inactive;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_LIVE_VALIDATION_AUTHORIZATION`

Classification: `A — Product Critical`.

A fresh explicit Product Owner authorization must mint exactly:

1. one new single-use bounded execution approval;
2. one new single-use transient-row memory-only privacy approval covering up to `256 rows/member`, `1024 total`, while keeping the existing `524288` source-byte envelope.

After fresh authorization:

`one same-byte deeper live validation -> evidence/source decision -> if insurance observed, bounded CA source activation -> MVP-1 candidate -> economics -> reviewer`

Do not reuse prior approvals, repeat the 16-row sample, widen source-response bytes, or reopen generic transport/PROPERTY_TYPE diagnostics absent new contradictory evidence.
