# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | COMPLETE FOR CURRENT MVP-1 HYPOTHESIS; CA PROPERTY_TYPE PATH FROZEN | run `35255228459` + derived evidence v1 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — NY OSC REQUEST-LINK HUMAN GATE NEXT | NY source contract/privacy gate CI `35258458704` SUCCESS |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## California Outcome

Latest deeper live execution:

`35255228459` — attempt `1` — SUCCESS.

It examined `1024` rows (`256/member`) under the unchanged `524288`-byte source-response envelope. All `1024` were deferred as unclassifiable and no authority-backed insurance code was observed.

California remains held rather than rejected. Repeating/widening the same `PROPERTY_TYPE` discovery pattern is not on the MVP-1 critical path without genuinely new evidence.

## Alternative Source Decision

Benchmark completed:

`docs/audits/MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_BENCHMARK.md`

Selected:

`New York OSC Owner Name File`

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

## New York Source Contract / Privacy Gate

Completed offline:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

Audit:

`docs/audits/MVP1_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_PRIVACY_GATE_OFFLINE.md`

CI:

`35258458704` — SUCCESS.

Implemented without requesting/downloading the real file:

- NY candidate registered disabled and unapproved;
- A01 v1.1 CA+NY request/result contracts added alongside unchanged historical v1.0;
- only authority-disclosed semantic fields modeled;
- physical file schema explicitly left unknown;
- New York authority-index insurance vocabulary recorded, with `IN03` primary;
- amount represented as `UNKNOWN_FROM_SOURCE`;
- first real schema discovery constrained to memory-only processing;
- raw file/owner-row persistence and owner-field logging forbidden for first discovery;
- fail-closed adapter blocks acquisition and parser activation;
- request-link authorization separated from later first-download/transient-PII authorization;
- no default download byte cap invented.

## MVP-1 Critical Path

Current sequence:

`NY source contract/privacy gate — DONE`

`-> HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

`-> one official request submission / receive access instructions`

`-> determine actual observable download constraints`

`-> HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

`-> exactly one bounded first-file memory-only schema discovery`

`-> source/schema decision`

`-> insurance classification using observed mapping + NY authority semantics`

`-> candidate creation`

`-> provenance/evidence`

`-> economics (source amount remains UNKNOWN_FROM_SOURCE unless later evidence supports value)`

`-> Streamlit reviewer`

`-> human continue/stop decision`

## Next Product Work

Execute exclusively:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Classification: `A — Product Critical`.

This gate covers only one OSC request submission to obtain access instructions. It does not authorize Owner Name File download or real owner PII processing.