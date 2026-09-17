# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California remains active only as the minimum critical-path enabler required to reach one lawful approved real source. Repository-only ceremony or diagnostics that do not shorten that path are deprioritized.

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Working Checkpoint

Current branch:

`m3-ca-sco-v1-2-proposal-contract-preservation-remediation`

Latest completed action:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Review checkpoint before state closure:

- HEAD `ed6a22a3ed5c727b3b4dd7f14416bb06acab2903`;
- CI `35220411955` — **SUCCESS**.

Review result:

`PASS_REMEDIATED_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_FOR_FRESH_SINGLE_USE_AUTHORIZATION`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REMEDIATION_RE_REVIEW.md`

## Adopted Transport / Archive-Layout Baseline

The active semantic runner remains correctly pinned to:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- offsets `0`, `59745428`, `96861315`, `134172553`.

No transport diagnostic is reopened.

## Proposal Contract State

Proposal `1.1.0` is accepted as the frozen proposal boundary for a separate fresh authorization gate.

The previously omitted reviewed fields are restored exactly from historical proposal `1.0.0`, including approval provenance, execution question, sample-bias note, official insurance codes, v1.2 null/default outcome constraints, privacy/persistence allowlists, derived-summary boundary and top-level acceptance criteria.

The v1.1 schema and contract tests enforce these values. Historical proposal `1.0.0` remains preserved unchanged as provenance.

## Runtime / D-008 State

Unchanged:

- semantic runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- parser/projector unchanged;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` unchanged;
- trimming/casing/normalization unchanged;
- D-008 `WHOLE_SOURCE_STOP` unchanged;
- deterministic sample/request/byte caps unchanged;
- no automatic widening;
- `automatic_retry_allowed = false`.

## Authorization / Privacy State

All historical and structural-revalidation execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Fresh single-use real-source execution approval: **NOT GRANTED**.

Fresh transient-row privacy approval: **NOT GRANTED**.

No California SCO request or network workflow was performed by the review.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout baseline adopted: `true`;
- semantic execution proposal accepted for fresh authorization: `true`;
- fresh execution/privacy authorization: `false`;
- semantic compatibility resolved: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`;
- commercial baseline from real cases: not established;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED.

## Next Recommended Action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

Classification:

`A — Product Critical`

This is the next material human gate. It may grant fresh single-use execution and transient-row privacy approvals for exactly one bounded real-source semantic execution, but must not itself access California SCO or create/trigger the execution workflow.

After explicit authorization, proceed directly to exactly one bounded real-source semantic execution, evidence review and source decision. Do not add diagnostics or infrastructure unless new contradictory evidence creates a genuine A-risk blocker.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
