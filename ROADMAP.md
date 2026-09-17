# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | COMPLETE FOR CURRENT MVP-1 HYPOTHESIS; CA PROPERTY_TYPE PATH FROZEN | run `35255228459` + derived evidence v1 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — NY OSC REQUEST SUBMITTED; ACCESS INSTRUCTIONS PENDING | Gate 1 consumed after Product Owner-confirmed manual submission |

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

Selected:

`New York OSC Owner Name File`

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

## New York Source Contract / Privacy Gate

Completed offline:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

CI:

`35258809399` — SUCCESS.

The source remains disabled/unapproved and the first real schema discovery remains memory-only with raw owner-file and owner-row persistence forbidden.

## NY OSC Gate 1

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

Current state:

`CONSUMED / SINGLE USE / NON-REUSABLE`

On 2026-09-17 the Product Owner confirmed that the official request form had been manually submitted once. Requester contact values are not persisted in the repository.

## MVP-1 Critical Path

Current sequence:

`NY source contract/privacy gate — DONE`

`-> NY request-link authorization — CONSUMED`

`-> official request submission — PRODUCT OWNER CONFIRMED COMPLETE`

`-> receive access instructions — PENDING`

`-> determine observable download constraints without processing file contents`

`-> define explicit max_download_bytes`

`-> HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

`-> exactly one bounded first-file memory-only schema discovery`

`-> source/schema decision`

`-> insurance classification using observed mapping + NY authority semantics`

`-> candidate creation`

`-> provenance/evidence`

`-> economics`

`-> Streamlit reviewer`

`-> human continue/stop decision`

## Next Product Work

Execute exclusively:

`AWAIT_NY_OSC_ACCESS_INSTRUCTIONS`

Classification: `A — Product Critical / External Dependency`.

When instructions arrive, capture only non-content access/download constraints required to prepare Gate 2. Do not download or inspect the Owner Name File and do not process owner PII before separate Gate 2 authorization.
