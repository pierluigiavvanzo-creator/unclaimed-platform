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

`m3-ca-sco-v1-2-real-source-proposal-adopted-baseline-refresh`

Completed action:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Authoritative adopted-baseline base:

- HEAD `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28`;
- CI `35210199280` — **SUCCESS**.

Refresh audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ADOPTED_BASELINE_REFRESH.md`

Refreshed proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`

The historical v1.0.0 proposal remains preserved unchanged as provenance.

## Adopted Transport / Archive-Layout Baseline

Semantic runner active pins remain:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- offsets `0`, `59745428`, `96861315`, `134172553`.

The refreshed proposal is bound to exactly these values and the contract regression compares them directly with the runner.

## Runtime / D-008 State

Unchanged:

- semantic runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- parser/projector unchanged;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` unchanged;
- trimming/casing/normalization unchanged;
- D-008 `WHOLE_SOURCE_STOP` unchanged;
- sample/request/byte caps unchanged;
- no automatic retry/widening.

## Authorization / Privacy State

All historical and structural-revalidation execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

The refreshed proposal grants no replacement approval.

Fresh single-use execution and transient-row privacy approvals remain required before any future real-source semantic execution.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout baseline adopted: `true`;
- semantic execution proposal rebound to adopted baseline: `true`;
- proposal human review after refresh: `false`;
- fresh execution/privacy authorization: `false`;
- semantic compatibility resolved: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED.

## Next Recommended Action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification:

`A — Product Critical`

This next action is repository-only. Review whether proposal version `1.1.0` faithfully preserves the previously accepted v1.2 execution design while rebinding only transport/archive-layout provenance to the adopted baseline. It must not access California SCO, grant/reuse approvals, create a network workflow, modify runtime/parser/regex/normalization/D-008, or activate source/downstream gates.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
