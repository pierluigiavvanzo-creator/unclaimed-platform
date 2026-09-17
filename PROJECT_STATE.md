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

`m3-ca-sco-v1-2-proposal-contract-preservation-remediation`

Completed action:

`REMEDIATE_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_CONTRACT_PRESERVATION`

Implementation checkpoint before state closure:

- HEAD `509567fb250386e266faf96e3d9acef04631f724`;
- CI `35220182596` — **SUCCESS**.

Remediation audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_CONTRACT_PRESERVATION_REMEDIATION.md`

## Adopted Transport / Archive-Layout Baseline

The active semantic runner remains correctly pinned to:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- offsets `0`, `59745428`, `96861315`, `134172553`.

The remediation does not modify this adopted baseline.

## Proposal Contract State

Proposal `1.1.0` retains the adopted baseline/provenance binding and now restores all reviewed historical design fields omitted by the first refresh.

Restored contract areas include:

- consumed historical approval references;
- execution question text;
- deterministic sample-bias note;
- official insurance codes;
- v1.2 null/default outcome constraints;
- privacy/persistence allowlists;
- derived-summary persistence boundary;
- top-level acceptance criteria.

The v1.1 schema requires those values, and the contract test compares the restored design fields against historical proposal `1.0.0` where appropriate.

The historical proposal remains preserved unchanged as provenance.

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
- `automatic_retry_allowed = false` retained.

## Authorization / Privacy State

All historical and structural-revalidation execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No fresh execution or transient-row privacy approval exists.

No California SCO request or network workflow was performed by the remediation.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout baseline adopted: `true`;
- semantic execution proposal rebound to adopted baseline: `true`;
- proposal contract-preservation remediation: `CI_GREEN_PENDING_HUMAN_RE_REVIEW`;
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

Perform only the minimum re-review of the remediated proposal/schema/test. Confirm that the fields identified by the previous FAIL are restored exactly, while adopted baseline, runtime, D-008, privacy scope and non-authorizing state remain unchanged. Do not access California SCO, create a network workflow, grant/reuse approvals or activate downstream gates.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
