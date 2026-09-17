# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | COMPLETE FOR CURRENT MVP-1 HYPOTHESIS; CA PROPERTY_TYPE PATH FROZEN | run `35255228459` + derived evidence v1 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — NEW YORK OSC SOURCE CONTRACT / PRIVACY GATE NEXT | first approved real source remains blocker |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## California Outcome

Latest deeper live execution:

`35255228459` — attempt `1` — SUCCESS.

It examined `1024` rows (`256/member`) under the unchanged `524288`-byte source-response envelope. All `1024` were deferred as unclassifiable and no authority-backed insurance code was observed.

California remains held rather than rejected, but repeating/widening the same `PROPERTY_TYPE` discovery pattern is no longer on the MVP-1 critical path without genuinely new evidence.

## Alternative Lawful Source Benchmark

Completed:

`BENCHMARK_MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_OFFLINE`

Audit:

`docs/audits/MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_BENCHMARK.md`

Selected next source candidate:

`New York OSC Owner Name File`

Product reasons:

- official bulk-download request path;
- quarterly refresh;
- owner/name address plus nature-of-property and reporter semantics are officially disclosed;
- official New York insurance table includes `IN03 — Proceeds Due Beneficiaries`;
- OSC explicitly supports an Abandoned Property Location Service Provider workflow;
- lower expected semantic/integration friction than the California feed.

The source is **not approved or acquired yet**. Exact file schema remains unknown and must not be inferred.

Benchmark disposition of alternatives:

- Texas SIFT: DEFER / secondary;
- Pennsylvania aggregate data: DEFER for market sizing only;
- Illinois: REJECT for bulk MVP-1 ingest because no bulk/API is provided;
- Washington: REJECT for commercial list acquisition because the official public-records guidance prohibits releasing lists for commercial purpose.

## MVP-1 Critical Path

Current intended sequence:

`NY source contract + privacy gate (offline)`

`-> fresh human authorization`

`-> request/download official NY Owner Name File`

`-> fail-closed first-file schema discovery`

`-> insurance classification using authority-backed NY semantics`

`-> candidate creation`

`-> provenance/evidence`

`-> economics with source value marked UNKNOWN_FROM_SOURCE where unsupported`

`-> Streamlit reviewer`

`-> human continue/stop decision`

## Next Product Work

Execute exclusively:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

Classification: `A — Product Critical`.

No real New York file request/download or PII processing is part of that action.