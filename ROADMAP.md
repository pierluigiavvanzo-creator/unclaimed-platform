# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | REAL-SEMANTIC PROPOSAL REFRESHED + CI GREEN; HUMAN REVIEW NEXT | proposal v1.1.0 rebound to adopted baseline, offsets match runner/evidence, no source request |
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
- reviewed transport/archive-layout baseline is adopted in the semantic runner;
- current runtime pins remain content length `162560390`, ETag `"222dd79f04c2a0a8fff166b01c8da746"`, offsets `0`, `59745428`, `96861315`, `134172553`;
- real-source execution proposal is refreshed to version `1.1.0` and bound to the adopted baseline;
- refresh checkpoint `c4dfc596b18fccd3348a388c1d08647d5cd00a45` passed CI `35217101641` — **SUCCESS**;
- proposal/runner/evidence offset equality is regression-tested;
- no California SCO request occurred during proposal refresh;
- all previous execution/privacy approvals remain consumed and non-reusable;
- fresh execution/privacy approvals are not granted;
- semantic compatibility remains unresolved.

## Preserved Runtime / Privacy Boundary

Unchanged:

- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 fail-closed mapping;
- four-member deterministic prefix sample;
- max 4 data rows/member and 16 total;
- max 1 HEAD, 4 Range, 5 HTTP requests;
- byte/decompression/logical-record caps;
- no additional range;
- no full-body fallback;
- no automatic widening;
- no automatic retry in the later one-shot execution path;
- memory-only transient row handling under fresh privacy approval;
- source policy / registry / production gates remain closed.

## Approval State

All prior real-source and structural-revalidation execution/privacy approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Proposal version `1.1.0` requires a later fresh single-use execution approval and fresh transient-row privacy approval. The proposal itself grants neither.

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

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

Classification:

`A — Product Critical`

Review only refreshed proposal version `1.1.0` and verify that it is correctly pinned to the adopted baseline while preserving the existing sample, D-008, privacy, cap and no-retry/no-widening boundaries. The review is repository-only and must not access California SCO, grant approvals, create a network workflow or activate any source/downstream gate.

If the review accepts the proposal, take the shortest safe route through one fresh authorization gate and exactly one bounded real-source semantic execution, then evaluate source approval rather than expanding infrastructure.
