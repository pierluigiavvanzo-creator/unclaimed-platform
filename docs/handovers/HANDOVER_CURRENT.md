# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ca-property-type-row-defer-live-validation-module-once`

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

Nonconforming or unknown insurance-like values are deferred without normalization, repair, semantic inference, row/value persistence or row-specific inspection. Only aggregate deferred-row evidence persists. Later rows may continue.

Transport/header/CSV-column/hard-cap failures remain whole-source fail-closed.

## Fresh Reauthorization Completed

Owner authorization:

`APPROVO FRESH D010 MODULE-MODE LIVE VALIDATION + TRANSIENT-ROW PRIVACY`

Fresh single-use refs:

- execution: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_REAL_SOURCE_VALIDATION_BOUNDED_C6D79506`;
- privacy: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_TRANSIENT_ROW_PRIVACY_BOUNDED_C6D79506`.

Authorization base:

- prior branch: `mvp1-ca-property-type-row-defer-live-validation-once`;
- base HEAD: `3d697efc4612fac070014d81767985ad8300af3f`;
- base CI: `35238612548` — SUCCESS;
- authorization checkpoint on current branch: `de1ca653824cd86af588ab2eff450c40e9ff85c4`;
- authorization-checkpoint CI: `35242982608` — SUCCESS.

Pinned runtime:

- D-010 runner blob: `8e952a80105d56a8e84e6fb9feb5524dd01625d0`;
- classifier blob: `05e8637e42070dd6f04218592d20d4a230ab948e`;
- policy blob: `840d09d87187c53d26f4d562527dcb92d810a9f3`;
- legacy transport/archive runner blob: `706183d5425da16b25f8186574cc356135803326`.

Machine approval record:

`sources/evidence/ca_sco_mvp1_property_type_row_defer_live_validation_approval.v2.json`

Reauthorization audit:

`docs/audits/M3_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_REAUTHORIZATION.md`

Both fresh refs are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Do not reuse or rerun them.

## One-Shot Module-Mode Live Execution

Trigger commit:

`d8008ea67516145532a5c8a47e70c13cb179c5e8`

Workflow run:

`35243232091` — attempt `1` — SUCCESS.

Lifecycle:

1. checkout/setup: PASS;
2. module-mode `--help` startup preflight: PASS;
3. exact authorization/blob/cap preflight: PASS;
4. fresh approval consumption before source access: PASS;
5. exactly one bounded live D-010 execution using `python -m scripts.ca_sco_mvp1_property_type_validation`: PASS;
6. privacy-safe evidence validation: PASS;
7. derived evidence persistence: PASS;
8. artifact upload: PASS;
9. one-shot workflow + trigger cleanup: COMPLETE.

Approval consumption/evidence were pushed by `github-actions[bot]` during the run. Persisted evidence commit:

`b8bbc6e5f4c9bea04a844e4bd1babc4a04e23a0d`

Cleanup commit:

`a1643cf7e97918725a752c7fc256224380f445d4`

## Live Evidence

Persisted derived evidence:

`sources/evidence/ca_sco_mvp1_property_type_row_defer.module_live_once.v2.json`

Evidence review:

`docs/audits/M3_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_LIVE_EVIDENCE_REVIEW.md`

Transport baseline matched:

- HEAD status: `200`;
- content length: `162560390`;
- content type: `application/zip`;
- accept-ranges: `bytes`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- last-modified observed: `Wed, 16 Sep 2026 16:43:22 GMT`.

Exact bounded source use:

- HEAD: `1`;
- Range GET: `4`;
- HTTP total: `5`;
- source response-body bytes: `524288`;
- rows examined: `16` (`4/member`).

Classification result:

- deferred unclassifiable rows: `16`;
- shape-valid non-target rows: `0`;
- recognized insurance rows: `0`;
- `IN03` rows: `0`;
- distinct recognized insurance codes: `[]`;
- semantic status: `NO_INSURANCE_CODE_OBSERVED_IN_BOUNDED_SAMPLE`;
- stop reason: `null`.

## Evidence Interpretation

D-010 live continuation is validated: all 16 authorized rows were processed and nonconforming `PROPERTY_TYPE` values no longer force a whole-source stop.

Insurance discovery was **not observed** in this tiny deterministic prefix sample.

Therefore:

- California source activation is **HELD / NOT YET APPROVED**;
- the source is **not rejected**;
- approved real sources remain `0`;
- production classification remains inactive;
- real MVP-1 candidates remain `0`.

Do not infer that the source contains no insurance records. The sample is deterministic, tiny and not statistically representative.

## Privacy State

PASS.

All `safety_state` flags in the persisted evidence are false. No raw body/full row, `PROPERTY_ID`, per-row or malformed `PROPERTY_TYPE`, owner/holder data, identity resolution, beneficiary matching, outreach or claim action was persisted or performed.

## Product-Critical Hypothesis Now

The only useful next hypothesis is:

> Authority-backed insurance codes may occur later than the first four rows of each canonical member, while the same four already-bounded `131072`-byte compressed prefixes may contain enough data to inspect more logical rows without increasing source requests or source-response bytes.

This is a new bounded product-validation hypothesis, not a reopening of generic transport/CSV/PROPERTY_TYPE diagnostics.

## Canonical Read Order Before Any New Change

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_LIVE_EVIDENCE_REVIEW.md`;
2. `sources/evidence/ca_sco_mvp1_property_type_row_defer.module_live_once.v2.json`;
3. `sources/evidence/ca_sco_mvp1_property_type_row_defer_live_validation_approval.v2.json`;
4. `scripts/ca_sco_mvp1_property_type_validation.py`;
5. `scripts/ca_sco_property_type_semantic_verification.py`;
6. `tests/unit/test_ca_sco_mvp1_property_type_validation.py`;
7. D-010 in `DECISIONS.md`.

## SINGLE NEXT ACTION

Execute exclusively:

`IMPLEMENT_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE`

Classification: `A — Product Critical`.

This action is offline only and requires no California source request or fresh privacy approval.

Goal:

Create and test a deeper bounded logical-row scan using the same future network envelope:

- endpoint unchanged;
- `1` HEAD max;
- `4` Range GET max;
- `131072` bytes per Range;
- `524288` source response-body bytes total;
- no additional Range or full-body fallback;
- D-010 metadata-only defer;
- no normalization/regex relaxation;
- no row/source-value/PII persistence;
- explicit bounded transient-row count and uncompressed-byte caps.

After that offline validator is green, the next material human gate is a fresh single-use execution + transient-row privacy authorization for one deeper live validation.

Do not repeat the same 16-row execution and do not reopen generic transport/CSV diagnostics absent new contradictory evidence.
