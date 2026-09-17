# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California remains active only as the minimum critical-path enabler required to reach one lawful approved real source.

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Working Checkpoint

Current branch:

`m3-ca-sco-property-type-v1-2-real-source-proposal-adopted-baseline-refresh`

Completed action:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Functional refresh checkpoint:

`c4dfc596b18fccd3348a388c1d08647d5cd00a45`

Refresh CI:

`35217101641` — **SUCCESS**

Refresh audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ADOPTED_BASELINE_REFRESH.md`

## Refreshed Real-Source Execution Proposal

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Current proposal version:

`1.1.0`

Status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

The proposal is now pinned to the CI-green adopted transport/archive-layout baseline checkpoint and uses canonical offsets:

- `0`;
- `59745428`;
- `96861315`;
- `134172553`.

Contract regression verifies these offsets against both the active runner and the persisted reviewed structural evidence. Runner content length and ETag remain the adopted reviewed values.

## Runtime / D-008 State

Unchanged by the proposal refresh:

- semantic runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- parser/projector unchanged;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` unchanged;
- trimming/casing/normalization unchanged;
- D-008 `WHOLE_SOURCE_STOP` unchanged;
- deterministic sample limits and request/byte caps unchanged.

## Authorization / Privacy State

All prior execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

This includes historical semantic execution/privacy approvals and structural-revalidation execution/privacy approvals.

Fresh real-source execution approval: `NOT_GRANTED`.

Fresh transient-row privacy approval: `NOT_GRANTED`.

Network workflow creation authorized: `false`.

Real-source execution authorized: `false`.

The proposal refresh performed no California SCO request and granted no replacement approval.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout baseline adopted: `true`;
- refreshed semantic execution proposal CI-green: `true`;
- proposal human-reviewed after refresh: `false`;
- semantic compatibility resolved: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

The stale-proposal blocker is closed. The shortest safe path is now human review of proposal version `1.1.0`, followed only if accepted by a fresh single-use authorization gate and exactly one bounded real-source semantic execution.

## Next Recommended Action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

Classification:

`A — Product Critical`

The review is repository-only. Review proposal version `1.1.0`, its adopted-baseline provenance, unchanged caps/privacy/D-008 boundary and non-authorizing status. Do not perform California SCO access, grant approvals, create a network workflow, modify runtime/parser/projector/regex/normalization, activate source policy/registry/production classification, or open downstream identity/genealogy/matching/outreach/claim gates.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
