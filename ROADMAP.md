# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | COMPLETE FOR CURRENT MVP-1 HYPOTHESIS; CA PROPERTY_TYPE PATH FROZEN | run `35255228459` + derived evidence v1 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — SYNTHETIC DOWNSTREAM SLICE VERIFIED; VALUE-EVIDENCE BENCHMARK NEXT | CI `35263620224` SUCCESS |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Source Path

California remains held rather than rejected; repeating/widening the same CA `PROPERTY_TYPE` scan is not on the MVP-1 critical path without genuinely new evidence.

Selected alternative source candidate:

`New York OSC Owner Name File`

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

The NY source contract/privacy package is complete, but the source remains disabled, unapproved and unacquired. Physical schema remains unknown until a separately authorized first file.

## NY OSC Gate 1

Request-link authorization is:

`GRANTED / SINGLE USE / NOT CONSUMED`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

Submission is parked because required requester values are currently unavailable:

- name;
- company;
- phone;
- email.

The values must not be invented. No Owner Name File download or real owner PII processing is authorized by Gate 1.

## Synthetic Downstream Vertical Slice

Completed:

`SYNTHETIC_POST_SCHEMA_MAPPING -> exact IN03 classification -> candidate -> economics -> reviewer`

Audit:

`docs/audits/MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE.md`

CI:

`35263620224` — SUCCESS.

Delivered:

- exact-code NY insurance classification;
- narrow candidate creation only for `IN03`;
- deterministic synthetic case identifier;
- explicit no-identity-resolution / no-beneficiary-matching boundary;
- economics with `UNKNOWN_FROM_SOURCE`, no invented amount and no invented commercial threshold;
- reviewer decision `CONTINUE_VALUE_RESEARCH_OR_STOP`;
- read-only FastAPI endpoint;
- Streamlit MVP-1 case/economics view;
- versioned JSON Schema + unit/contract/smoke coverage.

This means the downstream product path no longer needs to be built after the first real source arrives; the real-data path can target an already exercised interface.

## Newly Exposed Commercial Blocker

The OSC Owner Name File does not disclose dollar value, so exact `IN03` discovery alone cannot make a case economically actionable.

The next critical evidence problem is:

- recoverable value evidence;
- expected follow-up cost;
- lawful fee basis.

Do not substitute a guessed amount or generic market average for case-level evidence.

## MVP-1 Critical Path

Two parallel paths now exist:

`EXTERNAL SOURCE PATH`

`NY Gate 1 — GRANTED/NOT CONSUMED -> requester contact inputs -> one OSC request -> access constraints -> Gate 2 -> first bounded memory-only schema discovery`

`OFFLINE PRODUCT PATH`

`synthetic downstream slice — DONE -> value-evidence benchmark -> economics evidence contract -> connect real candidate when source becomes available`

The external source path remains parked until requester contact inputs exist. Offline Product Critical work may continue without consuming Gate 1.

## Next Product Work

Execute exclusively:

`BENCHMARK_NY_MVP1_RECOVERABLE_VALUE_EVIDENCE_PATHS_OFFLINE`

Classification: `A — Product Critical`.

No real owner PII, outreach, representation, fee agreement or claim activity is part of that action.
