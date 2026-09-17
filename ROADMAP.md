# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | D-010 CONTINUATION VALIDATED; DEEPER LIVE 1024-ROW SCAN COMPLETED; CA PROPERTY_TYPE DISCOVERY PATH HELD FOR MVP-1 | run `35255228459` + derived evidence v1 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — ALTERNATIVE LAWFUL REAL-SOURCE BENCHMARK NEXT | first approved real source remains blocker |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Latest Product-Critical Evidence

Same-bytes deeper live run:

`35255228459` — attempt `1` — SUCCESS.

Observed envelope:

- HEAD `1`;
- Range GET `4`;
- HTTP total `5`;
- source bytes `524288`;
- rows examined `1024` (`256/member`);
- all four members: `ROW_CAP_REACHED`.

Classification:

- deferred unclassifiable rows: `1024`;
- shape-valid non-target: `0`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- recognized authority codes: `[]`;
- stop reason: none.

D-010 continuation remains proven and privacy controls passed. Logical row depth increased `64x` over the prior 16-row scan without increasing source-response bytes.

## California Decision

California source approval remains **HELD / NOT YET APPROVED**. The source is not rejected.

The current California SCO `PROPERTY_TYPE` discovery path is frozen for MVP-1 because another equivalent scan no longer offers a credible improvement in `ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME` after `1024/1024` examined rows remained unclassifiable under the unchanged authority-backed boundary.

Consumed refs from run `35255228459` are non-reusable. The temporary workflow and trigger were removed.

## Source State

- transport/archive baseline: CONFIRMED LIVE;
- California authority semantics: RESOLVED;
- D-010 continuation: VALIDATED LIVE;
- same-byte deeper validation: COMPLETED;
- CA `PROPERTY_TYPE` discovery path: FROZEN FOR MVP-1 PENDING NEW EVIDENCE;
- California source approval: HELD;
- approved real sources: `0`;
- real candidates: `0`.

## Next Product Work

Execute exclusively:

`BENCHMARK_MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_OFFLINE`

Classification: `A — Product Critical`.

Purpose:

Find the shortest lawful path to a first approved real source with deterministic insurance relevance. Compare concrete source candidates on authority/provenance, insurance signal, machine accessibility, privacy burden, source/acquisition cost, update cadence, integration effort and expected time-to-first-candidate.

No new California live access is part of this benchmark. Do not repeat the 16-row or 1024-row scan, widen the same source-response envelope, or reopen generic transport/CSV/PROPERTY_TYPE diagnostics without genuinely new evidence.
