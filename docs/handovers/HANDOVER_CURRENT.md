# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-v1-2-real-source-proposal-adopted-baseline-refresh`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California is only a critical-path enabler for the first lawful approved real source. Avoid additional diagnostics/governance that do not shorten that path.

## Latest Completed Action

Completed:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification:

`A — Product Critical`

Base adopted-baseline checkpoint:

- branch `m3-ca-sco-transport-archive-layout-baseline-adoption`;
- HEAD `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28`;
- CI `35210199280` — **SUCCESS**.

Functional refresh checkpoint:

- HEAD `c4dfc596b18fccd3348a388c1d08647d5cd00a45`;
- CI `35217101641` — **SUCCESS**.

Refresh audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ADOPTED_BASELINE_REFRESH.md`

## Refreshed Proposal State

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Proposal version:

`1.1.0`

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

Prepared on:

`2026-09-17`

The proposal now binds to the adopted-baseline checkpoint and records baseline-adoption/evidence-review provenance.

Canonical member offsets now match both the active semantic runner and reviewed structural evidence:

- `From_500_To_Beyond_1_of_4.csv` -> `0`;
- `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
- `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
- `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

Contract regression also verifies:

- runner `EXPECTED_LENGTH = 162560390` equals reviewed structural evidence;
- runner `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"` equals reviewed structural evidence;
- stale historical offsets are rejected by schema validation.

## Runtime Behavior Preserved

Semantic runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Runtime contract:

`1.2.0`

Unchanged by this proposal refresh:

- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP` semantics;
- deterministic four-member prefix sample;
- max 4 data rows/member;
- max 16 data rows total;
- max 1 HEAD request;
- max 4 Range requests;
- max 5 HTTP requests total;
- max 131072 response bytes/range;
- max 524288 source response-body bytes total;
- max 262144 transient uncompressed bytes/member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes/logical record;
- no additional range;
- no full-body fallback;
- no automatic widening;
- later one-shot path remains no automatic retry;
- source policy/registry/production/downstream gates remain closed.

## Network / Approval State

This proposal refresh was repository-only and performed no California SCO request.

All historical semantic and structural execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

The proposal's current fresh-authorization state is:

- execution approval status: `REQUIRED_NOT_GRANTED`;
- execution approval ref: `null`;
- transient-row privacy approval status: `REQUIRED_NOT_GRANTED`;
- transient-row privacy approval ref: `null`;
- network workflow creation authorized: `false`;
- real execution authorized: `false`.

No fresh approval currently exists.

## Source / Product State

- transport/archive-layout baseline adopted: `true`;
- refreshed real-source semantic proposal CI-green: `true`;
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

Then for the next review inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ADOPTED_BASELINE_REFRESH.md`;
2. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`;
3. `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`;
4. `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py`;
5. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION.md`;
6. `sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`;
7. `scripts/ca_sco_property_type_semantic_verification.py`;
8. historical proposal/review/authorization records as provenance only, never as reusable approvals.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

Classification:

`A — Product Critical`

This next action is repository-only.

It must review proposal version `1.1.0` and verify:

- proposal validates against its versioned schema;
- base provenance is pinned to adopted-baseline HEAD `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28` and CI `35210199280`;
- refreshed canonical offsets match active runner and reviewed structural evidence;
- current runner length/ETag remain the reviewed adopted values;
- deterministic sample, request/byte caps, privacy controls and D-008 mapping are unchanged;
- proposal remains non-authorizing;
- all prior approvals remain consumed and non-reusable;
- source policy/registry/production/downstream gates remain closed.

It must not:

- perform any California SCO request;
- create/trigger a network workflow;
- grant execution/privacy approvals;
- reuse consumed approvals;
- modify runtime/parser/projector/regex/trimming/casing/normalization;
- change D-008 semantics;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, beneficiary matching, outreach or claim submission.

If and only if the review accepts proposal version `1.1.0`, the next step should be the minimum fresh single-use authorization gate for exactly one bounded real-source semantic execution. Do not reopen transport diagnostics without new contradictory evidence.
