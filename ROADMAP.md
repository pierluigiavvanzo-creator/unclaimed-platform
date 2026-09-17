# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | ADOPTED BASELINE; PROPOSAL CONTRACT REMEDIATED; HUMAN RE-REVIEW NEXT | omitted reviewed fields restored; CI green; runtime baseline unchanged |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler required to reach one lawful approved real source. Do not reopen transport diagnostics without new contradictory evidence.

## Verified M3 State

- D-008 `WHOLE_SOURCE_STOP` remains unchanged;
- semantic runner contract remains `1.2.0`;
- adopted transport/archive-layout baseline remains active and valid;
- active pins remain length `162560390`, ETag `"222dd79f04c2a0a8fff166b01c8da746"`, offsets `0`, `59745428`, `96861315`, `134172553`;
- historical proposal `1.0.0` remains preserved as provenance;
- proposal `1.1.0` remains bound to the adopted baseline;
- previous refresh review result was `FAIL_MINIMAL_REMEDIATION_REQUIRED`;
- contract-preservation remediation checkpoint `509567fb250386e266faf96e3d9acef04631f724`, CI `35220182596` — **SUCCESS**;
- all reviewed fields identified by that FAIL are restored in proposal/schema/test;
- all previous execution/privacy approvals remain consumed and non-reusable;
- no fresh execution/privacy approval exists;
- semantic compatibility remains unresolved;
- approved real sources remain `0`.

## Restored Contract Boundary

The remediation restores exactly the historical reviewed fields required by the prior review, including:

- approval provenance references;
- execution-question text and sample-bias note;
- official insurance-code vocabulary;
- v1.2 outcome null/default constraints;
- privacy/persistence allowlists and derived-summary boundary;
- top-level acceptance criteria.

The contract test now compares these restored fields with proposal `1.0.0` and rejects removal of the privacy allowlist or acceptance contract.

## Preserved Runtime Boundary

Unchanged:

- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 fail-closed mapping;
- deterministic four-member prefix sample;
- request/byte caps;
- no widening;
- `automatic_retry_allowed = false`;
- source policy / registry / production gates.

## Approval State

All prior real-source and structural-revalidation execution/privacy approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Fresh single-use execution and transient-row privacy authorization remain blocked until the remediated proposal passes human re-review.

## Next Product Work

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification:

`A — Product Critical`

Re-review only the remediation delta and confirm that all previously omitted reviewed fields are restored while baseline, runtime, D-008, privacy scope, no-retry/no-widening and non-authorizing state remain unchanged.

After a PASS, move directly to fresh single-use execution + transient-row privacy authorization and exactly one bounded real-source semantic execution, rather than expanding infrastructure.
