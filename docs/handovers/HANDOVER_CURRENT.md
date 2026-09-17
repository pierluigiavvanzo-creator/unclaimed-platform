# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Branch

`m3-ca-sco-v1-2-real-source-execution-once-2026-09-17`

Always verify remote HEAD and latest CI before modifying the repository.

## Latest Completed Product-Critical Package

The owner explicitly authorized:

`APPROVO FRESH SINGLE-USE EXECUTION + TRANSIENT-ROW PRIVACY`

Authorization checkpoint:

`903c665af2641c56c85f1f57749ce6bd02e1b800`

Fresh refs:

- `OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_ED6A22A3`;
- `OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_ED6A22A3`.

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry is authorized.

## One-Shot Real Execution

Trigger commit:

`d826492735b6f6665d59ab875e470074005a8191`

Workflow run:

`35222675324` — **SUCCESS**, attempt `1`.

Artifact:

- id `10496599995`;
- digest `sha256:3e52cdff838de4dfa73bf62b0361af6938be73f2aa381c68ecaf8bc1b1d37fe9`.

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_2026_09_17.json`

## Real Result

Transport matched the adopted baseline exactly:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`.

Network use stayed bounded:

- HEAD `1`;
- Range `1`;
- HTTP total `2`;
- response body bytes `131072`.

Semantic outcome:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

This is the exact D-008 `WHOLE_SOURCE_STOP` result.

No exact PROPERTY_TYPE value or raw/personal row data was persisted. All safety flags remained false.

## Evidence Review / Source Decision

Evidence review result:

`PASS_EXECUTION_EVIDENCE_ACCEPTED`

Source decision:

`REJECT_CA_SCO_500_PLUS_AS_APPROVED_MVP1_SOURCE_UNDER_CURRENT_V1_2_CONTRACT`

Interpretation:

- the California source is not declared intrinsically invalid;
- under the current unchanged PROPERTY_TYPE contract + D-008 it cannot continue to MVP-1;
- repeating the same run is not authorized and is not commercially useful;
- California is frozen under the current contract unless a future explicit Product Owner decision redesigns the semantic boundary.

## Source / Product State

- approved real sources: `0`;
- CA `$500+` under current contract: not approved / frozen;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification: inactive;
- real MVP-1 candidate cases: `0`;
- commercial real-case baseline: not established;
- Streamlit reviewer: active;
- downstream identity/genealogy/beneficiary/outreach/claims: blocked until a source enters the authorized vertical slice.

## Runtime / Governance Boundary

Unchanged:

- runtime contract `1.2.0`;
- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008;
- request/byte caps;
- privacy/persistence boundary;
- no automatic retry/widening.

`DECISIONS.md` is unchanged: the run and source decision apply existing D-008 and MVP-1 strategy; no architecture or policy redesign occurred.

## Cleanup Requirement

The checkpoint containing this handover must remove:

- `.github/workflows/ca-sco-property-type-semantic-verification-once.yml`;
- `.github/ca-sco-property-type-semantic-verification-once.trigger.json`.

No one-shot retry path may remain after cleanup.

## Canonical Read Order Before Any New Change

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect the 2026-09-17 execution/evidence-review audits and machine evidence only if relevant.

## SINGLE NEXT ACTION

Execute:

`SELECT_ALTERNATE_REAL_SOURCE_FOR_MVP1`

Classification:

`A — Product Critical`

Objective: identify the next lawful real-source candidate with the lowest credible semantic/integration friction and the shortest path to one approved source and a real economically reviewable case.

Use `REUSE > WRAP > INSPIRE > CUSTOM`.

Do not reopen California transport diagnostics or perform another CA request under consumed approvals. Do not redesign the PROPERTY_TYPE contract unless the Product Owner explicitly chooses that route.

The source-selection package should minimize Product Owner work and should move directly from factual source comparison to a bounded verification proposal for the most suitable candidate.