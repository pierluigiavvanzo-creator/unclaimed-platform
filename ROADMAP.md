# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | REVIEWED TRANSPORT/ARCHIVE BASELINE ADOPTED; REAL SEMANTIC PROPOSAL REFRESH NEXT | current content length, ETag and canonical offsets adopted in runner; CI green; no source request during adoption |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler required to reach one lawful approved real source. Do not return to transport diagnostics unless new evidence invalidates the adopted baseline.

## Verified M3 State

- D-008 `WHOLE_SOURCE_STOP` remains unchanged;
- semantic runner contract remains `1.2.0`;
- structural revalidation run `35198720002` completed **SUCCESS** on attempt `1`;
- candidate transport/archive-layout evidence was human-reviewed and accepted;
- reviewed baseline is now explicitly adopted in the semantic runner;
- implementation CI `35208763198` is **SUCCESS** on checkpoint `1eb8f79bac3024c7b69785663e3102a0fe83f8fd`;
- no California SCO request occurred during baseline adoption;
- all previous execution/privacy approvals remain consumed and non-reusable;
- semantic compatibility remains unresolved.

## Adopted Baseline

Runtime transport/archive-layout pins:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- canonical offsets `0`, `59745428`, `96861315`, `134172553`.

Contract regression verifies equality between these runtime pins and the persisted human-reviewed structural evidence.

## Preserved Runtime Boundary

Unchanged:

- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 fail-closed mapping;
- sample and request/byte caps;
- source policy / registry / production gates.

## Approval State

All prior real-source and structural-revalidation execution/privacy approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

A future real semantic verification requires fresh single-use execution and transient-row privacy authorization after the execution proposal is rebound to the adopted baseline.

## MVP-1 Commercial Baseline To Establish

Once one lawful approved real source exists, immediately measure where available:

- records examined;
- records surviving insurance classification;
- candidate cases produced;
- candidate-to-review conversion;
- human review time per candidate;
- automated/source cost per candidate;
- supportable recoverable-value/revenue evidence;
- principal failure/drop-off reasons;
- false-positive or unresolved-case signals;
- additional manual research burden.

No commercial threshold is invented in advance.

## Next Product Work

Execute exclusively:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification:

`A — Product Critical`

Reuse the existing v1.2 execution proposal rather than creating a new execution design. Update only its stale canonical offsets/baseline provenance and any strictly dependent contract assertions. Preserve sample plan, privacy controls, D-008, hard caps and no-retry boundary. This refresh is repository-only and must perform no California SCO request or grant fresh approvals.

After the refreshed proposal is validated, take the shortest safe route through human review + fresh authorization to exactly one bounded real-source semantic execution, then evaluate source approval rather than expanding infrastructure.
