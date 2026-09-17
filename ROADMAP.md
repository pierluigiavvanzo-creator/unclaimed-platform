# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | ADOPTED BASELINE; PROPOSAL REFRESH REVIEW FOUND NARROW CONTRACT-PRESERVATION DEFECT | runtime pins correct; proposal needs minimal restoration of omitted reviewed fields before authorization |
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
- refreshed proposal `1.1.0` binds correctly to the adopted baseline;
- review checkpoint `16a7e6f82a17a3f27b74195067aa1cff34bcba0e`, CI `35218563391` — **SUCCESS**;
- human refresh review result: `FAIL_MINIMAL_REMEDIATION_REQUIRED`;
- all previous execution/privacy approvals remain consumed and non-reusable;
- no fresh execution/privacy approval exists;
- semantic compatibility remains unresolved;
- approved real sources remain `0`.

## Review Defect

The refresh removed previously reviewed fields unrelated to transport baseline binding. The most material omissions are explicit privacy/persistence allowlists and v1.2 outcome-contract null/default constraints.

This is a narrow repository-contract defect. It does not invalidate the runner or adopted baseline and does not justify new transport diagnostics.

## Preserved Runtime Boundary

Unchanged:

- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 fail-closed mapping;
- deterministic four-member prefix sample;
- request/byte caps;
- no widening or automatic retry;
- source policy / registry / production gates.

## Approval State

All prior real-source and structural-revalidation execution/privacy approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Fresh single-use execution and transient-row privacy authorization remain blocked until the proposal contract is minimally repaired and human-reviewed.

## Next Product Work

Execute exclusively:

`REMEDIATE_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_CONTRACT_PRESERVATION`

Classification:

`A — Product Critical`

Restore only the reviewed fields omitted from proposal/schema `1.1.0`, retain the adopted baseline and additive `automatic_retry_allowed = false`, extend the contract test to compare restored design fields with proposal `1.0.0`, and run CI. No California SCO access, approval grant/reuse, workflow creation or downstream activation.

After CI-green remediation, immediately re-review the proposal and then take the shortest safe route to fresh single-use authorization and exactly one bounded real-source semantic execution.
