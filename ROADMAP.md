# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | MVP-1 CRITICAL PATH; BASELINE-REFRESH PROPOSAL PREPARED; HUMAN REVIEW NEXT | bounded ZIP Central Directory refresh design prepared; no network execution authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | PRIORITY PRODUCT OBJECTIVE | approved real source -> acquisition -> normalization -> insurance classification -> candidate -> provenance/evidence -> case economics -> reviewer -> human continue/stop decision |

## Priority Strategy

Priority source:

`PRODUCT_STRATEGY_MVP1.md`

Governing decision:

`D-009 — MVP-1 commercial validation becomes the product-priority objective`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

All substantial work must identify its A/B/C/D class and the MVP-1 blocker or exit criterion it advances.

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- v1.2 implementation completed and human-reviewed;
- runner output contract remains `1.2.0`;
- authorized one-shot execution performed exactly once;
- one-shot evidence human-reviewed and accepted;
- both fresh approvals consumed and non-reusable;
- no retry authorized;
- source continuation remains `false`;
- semantic compatibility remains unresolved.

Human evidence-review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

## Reviewed One-Shot Result

One-shot run:

`35123686954` — **SUCCESS**, attempt `1`

Execution outcome:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

Actual usage:

- 1 HEAD request;
- 0 Range requests;
- 1 HTTP request total;
- 0 source body bytes read;
- 0 rows examined;
- no `PROPERTY_TYPE` value observed.

## Strategic Meaning Of M3

The M3 stop demonstrates correct fail-closed behavior, but it does not yet create usable product or commercial validation.

M3 is therefore retained only as the minimal safe route to the first approved real source. Additional governance or diagnostics are lower priority unless they are required to control an A-level risk or directly unblock that source.

## Baseline Refresh Proposal — Prepared

Artifact:

`docs/audits/M3_CA_SCO_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`

Classification:

`A — Product Critical / MVP-1 critical-path enabler`

Recommended method:

`HEAD -> bounded ZIP tail -> EOCD -> exact Central Directory range -> canonical member offsets`

Why this path:

- does not use historical offsets to find new offsets;
- does not arithmetically rebase;
- does not download the full ZIP;
- does not decompress CSV data;
- does not inspect rows or PII;
- produces the minimum structural evidence needed to evaluate a fresh baseline.

Proposed later cap:

- maximum 1 HEAD;
- maximum 2 Range GETs;
- maximum 3 HTTP requests;
- maximum 262144 body bytes total;
- fail closed on ZIP64/ambiguity/cap excess/canonical-set mismatch.

No network request was performed while preparing the proposal. No new baseline values are adopted.

## Approval / Workflow State

Consumed execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain `CONSUMED_SINGLE_USE_NON_REUSABLE`.

No refresh execution, semantic retry or other source request is authorized.

## Privacy / Source Governance

No raw source body or row was read during preparation of the new proposal. No protected source values were persisted.

Source policy remains `PROPOSED`. Registry remains disabled/unapproved. Approved real sources remain `0`. Production classification and all downstream identity/genealogy/matching/outreach/claim gates remain inactive.

## MVP-1 Exit Evidence

MVP-1 requires evidence of:

1. at least one approved real source;
2. lawful bounded real ingestion through the authorized vertical slice;
3. at least one human-reviewable real candidate case, or a documented zero-candidate result through the complete real pipeline;
4. visible provenance and relevant evidence;
5. reproducible case economics with explicit inputs/assumptions;
6. bounded Product Owner review rather than repetitive technical QA;
7. a measured commercial baseline from real execution where available.

Commercial measurements include records examined, classification survival, candidates produced, candidate-to-review conversion, review time, automated cost, source/data cost where applicable, supportable value/revenue basis, failure reasons, false-positive/unresolved signals and manual research burden.

No success threshold is invented before the first real evidence exists.

## Current Critical Path

### Human gate — next

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

The review should approve, amend or reject the bounded Central Directory strategy. It performs no network access and adopts no live values.

### If approved

The next automated package is:

1. implement the bounded structural refresh runner/contract;
2. add deterministic synthetic ZIP tests and hard-cap tests;
3. prepare one-shot execution evidence contract;
4. stop before network access;
5. request one fresh single-use authorization only when the implementation is ready and reviewed.

### After a coherent baseline is later reviewed/adopted

1. update the semantic runner pins in a separately reviewed repository task;
2. run deterministic tests;
3. obtain a fresh single-use authorization for the smallest real-source semantic verification;
4. seek one approved real source;
5. immediately enter the MVP-1 vertical slice;
6. collect the commercial baseline;
7. perform explicit product-commercial `GO / REVISE / STOP` review before broadening scope.

## Deferred Until MVP-1 Evidence

Unless needed to control an A-level risk, deprioritize:

- broad multi-state expansion;
- fully automated genealogy;
- automatic outreach;
- automatic claim submission;
- contracts automation;
- infrastructure refactors without vertical-slice benefit;
- additional agent complexity without demonstrated product need;
- repeated diagnostics without a new hypothesis or direct source-unblocking value.
