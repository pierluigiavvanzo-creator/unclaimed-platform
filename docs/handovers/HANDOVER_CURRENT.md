# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-v1-2-real-source-proposal-adopted-baseline-refresh`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California is only a critical-path enabler for the first lawful approved real source.

## Latest Completed Action

Completed:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification:

`A — Product Critical`

Authoritative base:

- branch `m3-ca-sco-transport-archive-layout-baseline-adoption`;
- HEAD `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28`;
- CI `35210199280` — **SUCCESS**.

Refresh audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ADOPTED_BASELINE_REFRESH.md`

## Proposal Artifacts

Historical proposal preserved unchanged as provenance:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Refreshed proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`

Refreshed schema:

`schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.v1_1.schema.json`

Refresh contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal_v1_1.py`

The refresh is non-authorizing and repository-only.

## Adopted Runtime Baseline

Semantic runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Runtime contract:

`1.2.0`

Active pins:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- `From_500_To_Beyond_1_of_4.csv` -> `0`;
- `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
- `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
- `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

Proposal v1.1.0 is bound to these exact values and its contract test compares them directly with the active runner.

## Preserved Execution Design

The refresh reuses the existing v1.2 design. Unchanged:

- four canonical members;
- deterministic first-complete-row prefix sampling;
- max 4 data rows/member and 16 total;
- max 1 HEAD, 4 Range, 5 HTTP requests;
- existing range/body/transient/logical-record byte caps;
- no additional range;
- no full-body fallback;
- no automatic widening;
- no automatic retry;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- trimming/casing/normalization rules;
- D-008 `WHOLE_SOURCE_STOP` fail-closed control disposition;
- transient-row memory-only privacy boundary;
- no row/value persistence or row-specific human inspection.

## Network / Approval State

This proposal refresh performs no California SCO request and creates no network workflow.

All prior execution/privacy approvals, including structural-revalidation approvals, remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No fresh real-source execution or transient-row privacy approval exists yet.

## Source / Product State

- transport/archive-layout baseline adopted: `true`;
- real-source proposal rebound to adopted baseline: `true`;
- refreshed proposal human-reviewed: `false`;
- approved real sources: `0`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- semantic compatibility: unresolved;
- production classification: inactive;
- real MVP-1 candidate cases: `0`;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Canonical Read Order Before Any New Change

Read in exact order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ADOPTED_BASELINE_REFRESH.md`;
2. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`;
3. `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.v1_1.schema.json`;
4. `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal_v1_1.py`;
5. historical proposal v1.0.0 for provenance comparison;
6. `scripts/ca_sco_property_type_semantic_verification.py`;
7. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION.md`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification:

`A — Product Critical`

The review is repository-only.

It must determine whether proposal `1.1.0` faithfully preserves the already accepted v1.2 execution design while changing only the stale transport/archive-layout provenance/binding required by the adopted runtime baseline.

It must verify at least:

- proposal/schema contract validity;
- exact equality of length, ETag and canonical offsets with the active runner;
- historical proposal remains preserved as provenance;
- sample plan and request/byte caps are not widened;
- no automatic retry/widening is introduced;
- regex/parser/projector/normalization boundaries are unchanged;
- D-008 fail-closed behavior is unchanged;
- privacy scope is unchanged;
- proposal remains non-authorizing;
- all consumed approvals remain non-reusable;
- source policy, registry, production classification and downstream gates remain closed.

It must not:

- perform a California SCO request;
- create/trigger a network workflow;
- grant or reuse execution/privacy approvals;
- modify runtime/parser/projector/regex/normalization;
- change D-008;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, beneficiary matching, outreach or claim submission.

A PASS should move directly to the minimum fresh single-use authorization gate for exactly one bounded real-source semantic execution. Do not reopen transport diagnostics without new contradictory evidence.
