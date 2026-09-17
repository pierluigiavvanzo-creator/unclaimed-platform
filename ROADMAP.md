# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | ADOPTED BASELINE; REMEDIATED PROPOSAL REVIEW PASS; FRESH AUTHORIZATION NEXT | proposal accepted as bounded execution boundary; no source access yet |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler required to reach one lawful approved real source. Do not reopen transport diagnostics or add governance/infrastructure work without new evidence that it blocks an A-risk or MVP-1 exit criterion.

## Verified M3 State

- D-008 `WHOLE_SOURCE_STOP` unchanged;
- semantic runner contract `1.2.0` unchanged;
- adopted transport/archive-layout baseline active and valid;
- active pins: length `162560390`, ETag `"222dd79f04c2a0a8fff166b01c8da746"`, offsets `0`, `59745428`, `96861315`, `134172553`;
- historical proposal `1.0.0` preserved as provenance;
- proposal `1.1.0` bound to the adopted baseline;
- prior review defect remediated;
- remediated proposal re-review result: `PASS_REMEDIATED_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_FOR_FRESH_SINGLE_USE_AUTHORIZATION`;
- review checkpoint `ed6a22a3ed5c727b3b4dd7f14416bb06acab2903`, CI `35220411955` — **SUCCESS**;
- all prior execution/privacy approvals consumed and non-reusable;
- no fresh execution/privacy approval yet;
- semantic compatibility unresolved;
- approved real sources `0`.

## Preserved Boundary

Unchanged:

- deterministic four-member prefix sample;
- request/byte caps;
- no widening or automatic retry;
- regex/parser/projector/normalization;
- D-008 fail-closed mapping;
- privacy/persistence allowlists;
- source policy / registry / production gates.

## Next Product Work

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

Classification:

`A — Product Critical`

This is a material human authorization gate. Granting it should create fresh single-use execution and transient-row privacy approval references for exactly one bounded semantic verification, without performing the source request in the authorization action itself.

After explicit authorization, move directly to:

`one bounded real-source semantic execution -> evidence review -> source decision -> if approved, MVP-1 vertical slice`

Avoid further diagnostics or infrastructure expansion unless contradictory evidence makes them necessary.
