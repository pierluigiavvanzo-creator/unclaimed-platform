# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | ADOPTED BASELINE + REFRESHED REAL-SEMANTIC PROPOSAL; HUMAN REVIEW NEXT | current content length, ETag and canonical offsets active in runner; proposal v1.1.0 rebound to those pins |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler required to reach one lawful approved real source.

## Verified M3 State

- D-008 `WHOLE_SOURCE_STOP` remains unchanged;
- semantic runner contract remains `1.2.0`;
- reviewed transport/archive-layout baseline is adopted in the runner;
- adopted pins are content length `162560390`, ETag `"222dd79f04c2a0a8fff166b01c8da746"`, offsets `0`, `59745428`, `96861315`, `134172553`;
- historical real-source execution proposal v1.0.0 is preserved as provenance;
- refreshed proposal v1.1.0 is bound to the adopted baseline and current CI-green runner;
- all previous execution/privacy approvals remain consumed and non-reusable;
- no fresh execution/privacy approval currently exists;
- semantic compatibility remains unresolved;
- approved real sources remain `0`.

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

A future real semantic verification still requires fresh single-use execution and transient-row privacy authorization after human review of the refreshed proposal.

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

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification:

`A — Product Critical`

Review proposal version `1.1.0` only. Confirm that it changes the stale baseline/provenance binding while preserving sample plan, D-008, privacy, request/byte caps, no-retry/no-widening and non-authorizing status. Do not access California SCO or activate any downstream gate.

After a PASS, take the shortest safe route through fresh single-use authorization to exactly one bounded real-source semantic execution, then evaluate source approval rather than expanding infrastructure.
