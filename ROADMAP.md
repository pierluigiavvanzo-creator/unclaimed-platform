# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | CRITICAL PATH TO MVP-1; CURRENTLY BLOCKED ON STALE TRANSPORT/ARCHIVE-LAYOUT BASELINE | safe path to one approved real source; no unauthorized retry or source activation |
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
- real-source execution proposal/review and fresh single-use authorization completed;
- authorized one-shot execution performed exactly once;
- one-shot evidence human-reviewed and accepted;
- both fresh approvals consumed and non-reusable;
- no retry authorized;
- source continuation remains `false`;
- semantic compatibility remains unresolved.

Human evidence-review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

## Reviewed One-Shot Result

Execution branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-once`

Execution final HEAD before review:

`05a475ef2ddd0ed86f4e934c919bb1d98c58d566`

Execution final CI:

`35124327126` — **SUCCESS**

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

## Transport / Archive-Layout Finding

Expected transport identity:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`.

Observed live HEAD:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- HTTP status `200`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

The runner also pins four ZIP local-header offsets used by the deterministic sample plan:

- `From_500_To_Beyond_1_of_4.csv` → `0`;
- `From_500_To_Beyond_2_of_4.csv` → `59747797`;
- `From_500_To_Beyond_3_of_4.csv` → `96862896`;
- `From_500_To_Beyond_4_of_4.csv` → `134174190`.

Because the live ZIP identity changed, a future path cannot safely update only content length and ETag while assuming the historical archive-layout offsets remain valid. The existing transport/archive-layout baseline is stale for future execution planning, but no new baseline values are adopted.

## Approval / Workflow State

Consumed execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain `CONSUMED_SINGLE_USE_NON_REUSABLE`.

The temporary one-shot workflow and trigger marker remain absent. No retry path remains.

## Privacy / Source Governance

No raw source body or row was read during the stopped execution. No protected source values were persisted.

No rebaseline, runtime modification, another network verification or approval grant is authorized by the evidence review.

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

### A/B — Product Critical / Material Enabler

Prepare:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

Purpose: define the smallest deterministic and safe path that can later support a freshly authorized source revalidation.

Constraints remain:

- repository-only and design-only;
- no source or authority access;
- no update of runner constants;
- no inferred/rebased offsets;
- no workflow creation;
- no reuse of consumed approvals;
- no parser/projector/regex/normalization change;
- no privacy widening;
- no source/registry/production activation.

### After The Blocker Is Removed

1. separately review any proposed network revalidation;
2. obtain fresh single-use authorization before the first request;
3. achieve one approved real source;
4. immediately move into the MVP-1 vertical slice;
5. collect commercial baseline measurements;
6. perform an explicit go / revise / stop product-commercial review before broadening scope.

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
