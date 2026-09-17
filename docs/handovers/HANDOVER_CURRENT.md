# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-synthetic-vertical-slice-offline`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Canonical Read Order

Before any new change read, in order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect task-relevant artifacts.

## California Path

Latest bounded California live run remains:

`35255228459` — attempt `1` — SUCCESS.

Result:

- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- source response bytes: `524288`.

California remains `HELD / NOT YET APPROVED`, not rejected. The current CA SCO `PROPERTY_TYPE` discovery path is frozen for MVP-1 absent genuinely new evidence.

## New York Source Candidate

Selected:

`New York Office of the State Comptroller — Owner Name File`

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

State:

`REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`

Physical schema:

`UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE`

Dollar value:

`UNKNOWN_FROM_SOURCE`

Primary MVP-1 insurance target:

`IN03 — Proceeds Due Beneficiaries`

Production parser/classification remains inactive.

## Gate 1 — Request Access Only

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Owner authorization:

`APPROVO NY OSC OWNER NAME FILE REQUEST-LINK ONLY`

Evidence:

`sources/evidence/ny_osc_owner_name_file_request_link_authorization.v1.json`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

State:

`GRANTED_SINGLE_USE_NOT_CONSUMED_PENDING_REQUESTER_CONTACT_DATA`

No official OSC request has been submitted. Requester values are currently unavailable:

1. name;
2. company;
3. phone;
4. email.

Do not invent or infer them.

Gate 1 does NOT authorize Owner Name File download, real owner PII processing, schema parsing, identity resolution, beneficiary matching, outreach, representation, fee agreement or claim activity.

Gate 2 remains `NOT GRANTED / NOT READY` and requires an explicit `max_download_bytes` after access instructions are obtained.

## Completed Parallel Product Action

Because Gate 1 is parked on unavailable human contact inputs, downstream MVP-1 construction continued offline with synthetic data only.

Completed:

`MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE`

Classification:

`A — Product Critical`.

Audit:

`docs/audits/MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE.md`

Stable implementation checkpoint before canonical documentation updates:

`caedbb67c3077a654533a5c96dab42cbfa4e0cf3`

CI:

`35263620224` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety/startup;
- frontend lint/typecheck/build.

The preceding run `35263474623` failed only on Ruff import ordering in one new test and was corrected without product-logic change.

## Synthetic Downstream Path

Implemented path:

`SYNTHETIC_POST_SCHEMA_MAPPING -> exact NY insurance classification -> IN03 candidate -> economics -> reviewer`

Key behavior:

- exact `IN03` -> `MVP1_PRIMARY_INSURANCE`;
- another exact recorded NY insurance code -> `INSURANCE_OTHER`;
- unknown code -> `NO_AUTHORITY_BACKED_INSURANCE_MATCH`;
- no normalization, repair, inference or regex-like promotion;
- only exact `IN03` creates the narrow synthetic MVP-1 candidate;
- candidate id is deterministic;
- no identity resolution or beneficiary matching is performed;
- no real source or PII is accessed.

New files/surfaces include:

- `src/unclaimed_platform/domain/mvp1_vertical_slice.py`;
- `schemas/ui/mvp1_synthetic_case_review.schema.json`;
- `GET /api/reviewer/mvp1/synthetic-case`;
- Streamlit `MVP-1 SYNTHETIC CASE` and `CASE ECONOMICS` sections;
- unit, contract and smoke coverage.

## Economics Finding

The synthetic case deliberately preserves:

- `recoverable_value_state = UNKNOWN_FROM_SOURCE`;
- `source_amount_available = false`;
- `fee_basis_state = NOT_COMPUTABLE_FROM_SOURCE`;
- `commercial_threshold_applied = false`;
- `invented_amounts = false`.

Reviewer decision:

`CONTINUE_VALUE_RESEARCH_OR_STOP`

Required next evidence:

- recoverable value evidence;
- expected follow-up cost;
- lawful fee basis.

This is now the highest-value offline commercial blocker. The OSC Owner Name File may identify a candidate category, but by itself it does not establish recoverable amount.

## Reuse Decision

Existing Pydantic + JSON Schema + FastAPI + Streamlit stack was reused.

External rule engines benchmarked but not adopted:

- `venmo/business-rules` — MIT; Python DSL; excess abstraction for current exact-rule scope;
- `gorules/zen` — MIT; active multi-language engine; excess runtime/integration complexity for current scope.

Decision:

`REUSE EXISTING STACK > ADD NEW RULE ENGINE`

## Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- NY source: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: `GRANTED / NOT CONSUMED`;
- NY request submitted: no;
- NY access instructions obtained: no;
- NY real owner PII processed: no;
- NY Gate 2: not granted;
- synthetic IN03 classification-to-reviewer path: `READY / VERIFIED`;
- real MVP-1 candidates: `0`.

## Parallel Critical Paths

External source path:

`requester contact inputs -> one authorized OSC request -> access instructions -> download constraints -> Gate 2 -> bounded first-file memory-only schema discovery`

Offline product path:

`synthetic downstream slice — DONE -> recoverable-value evidence benchmark -> economics evidence contract -> real candidate integration when source becomes available`

Gate 1 remains parked and unconsumed while offline Product Critical work continues.

## Task-Relevant Artifacts for Next Work

Inspect at least:

1. `PRODUCT_STRATEGY_MVP1.md`;
2. `docs/audits/MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE.md`;
3. `src/unclaimed_platform/domain/mvp1_vertical_slice.py`;
4. `schemas/ui/mvp1_synthetic_case_review.schema.json`;
5. `policies/states/NY/ny_osc_owner_name_file.v1.json`;
6. `sources/registry.yaml`;
7. current official New York OSC/insurance/legal sources relevant to value evidence and location-service-provider economics.

## SINGLE NEXT ACTION

Execute exclusively:

`BENCHMARK_NY_MVP1_RECOVERABLE_VALUE_EVIDENCE_PATHS_OFFLINE`

Classification:

`A — Product Critical`.

Goal:

Identify and compare lawful, evidence-backed ways to obtain or estimate recoverable monetary value, expected follow-up cost and lawful fee basis for a future New York `IN03` candidate. Distinguish exact case-level evidence from proxies and market-level estimates. Prefer official/public/authorized sources and reusable capabilities.

No real owner PII, Owner Name File download, outreach, representation, fee agreement or claim activity is authorized by this offline action.
