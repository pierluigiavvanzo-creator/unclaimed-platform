# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | COMPLETE FOR CURRENT MVP-1 HYPOTHESIS; CA PROPERTY_TYPE PATH FROZEN | run `35255228459` + derived evidence v1 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — NY OSC REQUEST AUTHORIZED; REQUESTER CONTACT INPUTS NEXT | Gate 1 evidence recorded; no request submitted yet |

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

Implemented without requesting/downloading the real file:

- NY candidate registered disabled and unapproved;
- A01 v1.1 CA+NY request/result contracts added alongside unchanged historical v1.0;
- physical file schema explicitly left unknown;
- New York insurance vocabulary recorded, with `IN03` primary;
- amount represented as `UNKNOWN_FROM_SOURCE`;
- first real schema discovery constrained to memory-only processing;
- raw file/owner-row persistence and owner-field logging forbidden for first discovery;
- request-link authorization separated from later first-download/transient-PII authorization.

## NY OSC Gate 1

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Authorization received:

`APPROVO NY OSC OWNER NAME FILE REQUEST-LINK ONLY`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

Current state:

`GRANTED / SINGLE USE / NOT CONSUMED`

No official form has been submitted yet because the required requester contact fields have not been supplied in the authorization input:

- name;
- company;
- phone;
- email.

These values must not be invented.

## MVP-1 Critical Path

Current sequence:

`NY source contract/privacy gate — DONE`

`-> NY request-link authorization — GRANTED, NOT CONSUMED`

`-> requester supplies name/company/phone/email`

`-> exactly one official request submission`

`-> receive access instructions`

`-> determine actual observable download constraints`

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

`COLLECT_NY_OSC_REQUESTER_CONTACT_INPUTS_FOR_AUTHORIZED_REQUEST`

Classification: `A — Product Critical / Human Input Dependency`.

No Owner Name File download or real owner PII processing is authorized by Gate 1.
