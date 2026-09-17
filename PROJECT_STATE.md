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

Latest reviewed action:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Reviewed implementation checkpoint:

- HEAD `16a7e6f82a17a3f27b74195067aa1cff34bcba0e`;
- CI `35218563391` — **SUCCESS**.

Review result:

`FAIL_MINIMAL_REMEDIATION_REQUIRED`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW.md`

## Adopted Transport / Archive-Layout Baseline

The active semantic runner remains correctly pinned to:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- offsets `0`, `59745428`, `96861315`, `134172553`.

The review found no defect in the adopted runtime baseline.

## Proposal Review Finding

Proposal `1.1.0` correctly adopted the current baseline and remained non-authorizing, but it removed reviewed contract fields unrelated to baseline/provenance refresh.

Material omissions include explicit privacy/persistence allowlists and v1.2 outcome fields, plus supporting provenance/acceptance fields. Therefore the proposal cannot yet be used as the frozen boundary for fresh execution authorization.

The historical proposal `1.0.0` remains preserved unchanged as provenance.

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

No fresh execution or transient-row privacy approval exists.

No California SCO request or network workflow was performed by the review.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout baseline adopted: `true`;
- semantic execution proposal rebound to adopted baseline: `true`;
- proposal refresh human review: `FAIL_MINIMAL_REMEDIATION_REQUIRED`;
- fresh execution/privacy authorization: `false`;
- semantic compatibility resolved: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED.

## Next Recommended Action

Execute exclusively:

`REMEDIATE_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_CONTRACT_PRESERVATION`

Classification:

`A — Product Critical`

Repository-only remediation. Restore the reviewed fields omitted from proposal/schema `1.1.0`, preserve the adopted baseline and current runtime exactly, extend contract assertions, and perform no California SCO request, workflow creation, approval grant/reuse or downstream activation.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
