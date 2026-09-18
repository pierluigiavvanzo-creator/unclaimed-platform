# HANDOVER_CURRENT.md

Last updated: 2026-09-18

## Superseding Event — Second NY Attempt Consumed Fail-Closed

Inspected repository package checkpoint:

`61a533e035dfba45d0c1359b8eee0fdbba41d7d8`

The second bounded execution was performed once and stopped fail-closed:

`BLOCKED / UNEXPECTED_DATA_FIELD_COUNT`

Observed non-PII metadata:

- archive bytes: `409,477,526`;
- archive members: `1`;
- selected text member uncompressed bytes: `1,939,569,781`;
- local file logically deleted: yes;
- no owner values or raw path returned.

Both second-attempt approvals are now
`CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO RETRY`. Do not run
`scripts/ny_osc_gate2_retry_transient_local.ps1` again.

An offline repair candidate adds byte-level quote-aware pipe parsing, non-PII blocked
diagnostics, synthetic regression coverage, persisted execution evidence and a PowerShell
consumption precheck that runs before any download prompt. The real-file cause remains a
bounded hypothesis because the source row was not retained.

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ny-gate2-approved-ready-execution`

Latest verified product implementation checkpoint:

`688469e87fc39da20b7906b3825c81367a594b16`

Product implementation CI:

`35359065170` — SUCCESS.

The branch HEAD can advance when canonical state files are refreshed; always verify remote HEAD before modifying.

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Canonical Read Order

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect task-relevant artifacts.

## California Path

Latest bounded live run:

`35255228459` — SUCCESS.

Result:

- rows examined: `1024`;
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- source response bytes: `524288`.

California remains `HELD / NOT YET APPROVED`, not rejected. The current CA `PROPERTY_TYPE` path is frozen for MVP-1 absent genuinely new evidence.

## New York Real-Source Track

Selected source:

`ny.osc.unclaimed_funds.owner_name_file`

State:

`REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`

Physical schema:

`UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE`

Primary target:

`IN03 — Proceeds Due Beneficiaries`

### Gate 1

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

State:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

The Product Owner confirmed one manual official-form submission on 2026-09-17. This is recorded as Product Owner attestation, not independent repository verification. Requester contact values are not persisted.

Latest Gmail check on 2026-09-18 found no matching OSC access-instructions email.

### External dependency

`AWAIT_NY_OSC_ACCESS_INSTRUCTIONS`

When instructions arrive, inspect only what is needed to determine non-content access/download constraints. Do not download or inspect the Owner Name File under Gate 1.

### Gate 2

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

State:

`NOT GRANTED / NOT READY`

Prerequisites:

1. access instructions received;
2. non-content download constraints observed;
3. explicit `max_download_bytes` defined;
4. separately reviewed single-use transient-PII authorization.

No real owner PII, raw file persistence, identity resolution, beneficiary matching, outreach, representation, fee agreement or claim activity is currently authorized.

## Completed Offline Product Work

### 1. Synthetic downstream MVP-1 slice

Reused the already verified implementation from `mvp1-synthetic-vertical-slice-offline` rather than rewriting it.

Integrated files include:

- `src/unclaimed_platform/domain/mvp1_vertical_slice.py`;
- `schemas/ui/mvp1_synthetic_case_review.schema.json`;
- reviewer API route;
- Streamlit MVP-1 case surface;
- unit/contract/smoke tests;
- `docs/audits/MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE.md`.

Path:

`SYNTHETIC_POST_SCHEMA_MAPPING -> exact NY insurance classification -> IN03 candidate -> economics -> reviewer`

Integration commit:

`75156c5419616b67eff658c8c3c8d6775849546c`

CI:

`35317313977` — SUCCESS.

No real source or PII was accessed.

### 2. NY recoverable-value / fee / cost evidence benchmark

Audit:

`docs/audits/NY_MVP1_RECOVERABLE_VALUE_EVIDENCE_BENCHMARK_OFFLINE.md`

Official-source conclusion encoded in the product:

- Owner Name File does not disclose exact item amount;
- exact recoverable value remains unknown pre-claim-review;
- APL §1416 15% location-service figure is represented only as a statutory maximum for its scoped rule and is not an assumed actual revenue rate;
- actual fee requires explicit evidence and legal-scope confirmation;
- expected follow-up cost remains unmeasured until evidence exists;
- pre-contact commercial actionability is therefore `NOT_COMPUTABLE_PRE_CONTACT`.

Implemented:

- `src/unclaimed_platform/domain/ny_mvp1_value_evidence.py`;
- `schemas/economics/ny_mvp1_precontact_evidence.schema.json`;
- `schemas/economics/ny_mvp1_explicit_case_economics_input.schema.json`;
- `schemas/economics/ny_mvp1_explicit_case_economics_result.schema.json`;
- unit + contract tests.

Explicit later calculations use integer cents and basis points plus evidence refs. They perform arithmetic only and return no commercial recommendation.

A transient CI failure `35317731747` was caused solely by duplicate Python test-module basenames. The contract test was renamed; repair CI `35317814189` was SUCCESS.

### 3. Economics reviewer integration

Added:

- `GET /api/reviewer/mvp1/economics/precontact`;
- fail-closed Streamlit economics adapter;
- `NY PRE-CONTACT ECONOMICS` reviewer card;
- API and Streamlit smoke coverage.

Latest cumulative CI:

`35318092067` — SUCCESS.

Verified:

- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- Streamlit safety smoke PASS;
- Streamlit startup smoke PASS;
- frontend lint PASS;
- frontend typecheck PASS;
- frontend build PASS.

### 4. Follow-up cost measurement contract

Completed:

`IMPLEMENT_NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE`

Implemented measured fields:

- automated processing cost per candidate;
- source/data cost per candidate;
- human review duration;
- manual research duration.

All monetary amounts use integer cents and all human durations use integer seconds. Each component requires provenance via evidence reference plus observation timestamp.

An optional documented human labor rate can convert measured time into human labor cost. If no documented rate exists, fully loaded follow-up cost remains `NOT_COMPUTABLE_NO_LABOR_RATE`.

Files:

- `src/unclaimed_platform/domain/ny_mvp1_follow_up_cost.py`;
- `schemas/economics/ny_mvp1_follow_up_cost_measurement_input.schema.json`;
- `schemas/economics/ny_mvp1_follow_up_cost_measurement_result.schema.json`;
- unit + contract tests;
- `docs/audits/NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE.md`.

Verified checkpoint:

`e9c1bc0e310f1b7b65f4153c90d5efb5d812caa0`

CI:

`35321285527` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety/startup;
- frontend lint/typecheck/build.

Patch-loop note:

After two failed corrective commits on the same Ruff/test-file issue, development stopped for the required root-cause audit. The defect was a literal escaped newline inserted by connector-side patching, not domain logic. Audit:

`docs/audits/NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_RUFF_ROOT_CAUSE.md`

### 5. Follow-up cost → case economics integration

Completed:

`INTEGRATE_NY_MVP1_FOLLOW_UP_COST_WITH_CASE_ECONOMICS_OFFLINE`

Implemented additive bridge:

- `src/unclaimed_platform/domain/ny_mvp1_case_economics_integration.py`;
- integration input JSON Schema;
- integration result JSON Schema;
- unit tests;
- contract tests;
- technical audit.

Critical fail-closed rule:

`COMPUTED_FROM_MEASURED_COMPONENTS -> may populate measured_follow_up_cost_cents`

Any other follow-up cost state:

`-> BLOCKED_FOLLOW_UP_COST_UNAVAILABLE`

The bridge explicitly does not substitute `direct_machine_and_data_cost_cents` when the fully loaded cost is unavailable.

Provenance retained:

- candidate case id;
- follow-up cost measurement id;
- component cost evidence refs;
- value evidence ref;
- fee evidence ref.

Verified checkpoint:

`65748470ca69b71afd859d411a7f5673bb7bd823`

CI:

`35336436604` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety/startup;
- frontend lint/typecheck/build.

First run `35336348948` failed on one contract test because the JSON Schema allowed a blocked state with a non-null cost even though the Pydantic model already rejected it. The result schema was tightened with conditional `if/then` constraints. No Python domain logic changed.

Audit:

`docs/audits/NY_MVP1_FOLLOW_UP_COST_CASE_ECONOMICS_INTEGRATION_OFFLINE.md`

### 6. Integrated case economics reviewer exposure

Completed:

`EXPOSE_NY_MVP1_INTEGRATED_CASE_ECONOMICS_IN_REVIEWER_OFFLINE`

Added:

- `GET /api/reviewer/mvp1/economics/integrated`;
- typed deterministic ready/blocked reviewer snapshot;
- safe Streamlit adapter validation;
- two Streamlit integrated-economics cards;
- UI JSON Schema;
- contract + API/Streamlit smoke tests;
- technical audit.

Ready state:

`READY_WITH_DOCUMENTED_LABOR_RATE -> READY_FOR_EXPLICIT_ECONOMICS`

Blocked state:

`BLOCKED_WITHOUT_DOCUMENTED_LABOR_RATE -> BLOCKED_FOLLOW_UP_COST_UNAVAILABLE`

The blocked UI exposes machine/data direct cost only as educational context and labels it `NOT FULLY LOADED`; it does not populate the integrated follow-up cost or compute explicit economics.

Both states preserve evidence refs and show no automatic commercial recommendation.

Verified checkpoint:

`8274660554733d39e7dc7c522676bc709fb90214`

CI:

`35339962098` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety/startup;
- frontend lint/typecheck/build.

First run `35339876798` failed only because mypy rejected dictionary literals passed where existing typed measurement components were required. The fixture was changed to use the existing Pydantic component models. No domain behavior changed.

Audit:

`docs/audits/NY_MVP1_INTEGRATED_CASE_ECONOMICS_REVIEWER_OFFLINE.md`

### 7. MVP-1 Streamlit deployment candidate

Completed:

`PREPARE_NY_MVP1_REVIEWER_DEPLOYMENT_CANDIDATE_OFFLINE`

Candidate status:

`READY_OFFLINE_NOT_REMOTELY_DEPLOYED`

Deployment coordinates:

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- branch: `mvp1-ny-reviewer-deployment-candidate-offline`;
- entrypoint: `apps/reviewer-streamlit/streamlit_app.py`;
- Python: `3.11`;
- secrets: none.

Runtime pins:

- Streamlit 1.63.0;
- FastAPI 0.141.1;
- Pydantic 2.13.5.

Product-facing UI now says `MVP-1 Reviewer Console` and has a visible synthetic/test-only deployment-candidate banner. Ready and blocked monetary demonstrations remain explicitly synthetic/test-only; machine/data cost in the blocked state remains `NOT FULLY LOADED`.

Checklist:

`apps/reviewer-streamlit/DEPLOYMENT_CANDIDATE.md`

Audit:

`docs/audits/NY_MVP1_REVIEWER_DEPLOYMENT_CANDIDATE_OFFLINE.md`

Verified checkpoint:

`2a4c4bc6e3103bc7d5800facd0fbe4d8a01c2e16`

CI:

`35344178149` — SUCCESS.

Passed:

- pinned requirements install;
- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety smoke;
- Streamlit startup health;
- frontend lint/typecheck/build.

Initial run `35344088288` failed only on two line-length lint errors in display copy. No safety or product semantics changed in the fix.

Rollback:

`6b14edfa39aab0c9bfe7be840820859075c7a708`

Remote deployment is not yet claimed and no current MVP-1 `streamlit.app` URL is recorded.

### 8. Remote Streamlit deployment verification

Completed:

`VERIFY_NY_MVP1_STREAMLIT_REMOTE_DEPLOYMENT`

Verified remote URL:

`https://unclaimed-platform-mvp1-reviewer.streamlit.app/`

Evidence:

- Product Owner supplied screenshots of the live deployed page;
- deployment-trigger GitHub CI `35345560301` — SUCCESS.

Remote screenshots confirm:

- `MVP-1 Reviewer Console`;
- `Synthetic/test-only deployment candidate`;
- `MVP-1 SYNTHETIC CASE`;
- `NY PRE-CONTACT ECONOMICS`;
- READY integrated economics card;
- FAIL-CLOSED integrated economics card;
- READY state `READY FOR EXPLICIT ECONOMICS`;
- blocked state `BLOCKED FOLLOW UP COST UNAVAILABLE`;
- direct machine/data cost remains `NOT FULLY LOADED`;
- `NONE — HUMAN DECISION REQUIRED`;
- approved real sources `0`;
- real acquisition `BLOCKED`;
- beneficiary matching `BLOCKED`;
- governance `PASS SYNTHETIC ONLY`;
- PII mode `NO REAL PII`;
- no visible runtime error.

Deployment status:

`VERIFIED_REMOTE_SYNTHETIC_ONLY`

Non-blocking presentation debt:

- `synthetic:m3-operations-console-demo` remains visible in the synthetic raw-artifact card;
- historical M3 milestone remains visible.

These are legacy synthetic labels/history only and do not invalidate the MVP-1 deployment.

### 9. NY first schema-discovery harness — offline

Completed:

`IMPLEMENT_NY_OSC_FIRST_SCHEMA_DISCOVERY_HARNESS_OFFLINE`

Official non-secret instruction facts incorporated:

- archive name `NYSFINDERS.ZIP`;
- pipe delimiter;
- documented 14-field KAPS layout;
- `Property Type Code` at zero-based position 1;
- secure-transfer listing includes a pre-download Size column.

The historical size shown in OSC documentation is not used as current-size evidence.

Implementation:

- transient archive bytes are never serializable;
- max download bytes checked before ZIP parsing;
- max uncompressed bytes and max archive members required explicitly;
- one text member required;
- owner name/address columns never decoded, logged or returned;
- exact documented header names are persisted only if exact header bytes are observed;
- otherwise no row is promoted to a header;
- output is aggregate/non-PII schema metadata only.

Checkpoint:

`9885377addec66d2802f58f6fa7184c2cd8ffdb1`

CI:

`35353395811` — SUCCESS.

Audit:

`docs/audits/NY_OSC_OWNER_NAME_FILE_FIRST_SCHEMA_DISCOVERY_HARNESS_OFFLINE.md`

Gate 2 remains ungranted; no OSC network access or real owner PII occurred.

### 10. Current listing metadata and Gate 2 bounded proposal

Product Owner supplied current OSC outbound-listing evidence:

- remote name `FINDERS.zip`;
- displayed size `390.51 MB`;
- last modified `9/16/2026, 1:33:31 PM`.

No Owner Name File download occurred.

Derived bounds:

- decimal-MB interpretation: `390,510,000` bytes;
- binary-MiB equivalent ceiling: `409,479,414` bytes;
- proposed `max_download_bytes = 450,000,000`;
- proposed `max_uncompressed_bytes = 2,000,000,000`;
- proposed `max_archive_members = 1`;
- downloads max = 1;
- retries max = 0.

Preflight must match remote name, displayed size and last-modified value exactly; drift stops before download.

Artifacts:

- `sources/evidence/ny_osc_owner_name_file_current_listing_metadata.v1.json`;
- `sources/proposals/ny_osc_owner_name_file_first_download_transient_pii_authorization.v1.json`;
- `docs/audits/NY_OSC_GATE2_BOUNDED_FIRST_DOWNLOAD_PROPOSAL.md`.

Execution transport is not yet compliant: official OSC browser instructions save the ZIP to local disk, while current policy requires memory-only/no raw-file persistence. Proposal review can proceed, but execution remains blocked until transport policy is resolved.

### 11. Transient local-file runner — offline verified

Product Owner authorization:

`APPROVO NY OSC FIRST DOWNLOAD TRANSIENT LOCAL FILE BOUNDED ONCE`

State:

`GRANTED_NOT_CONSUMED`

This authorization is only a local-retention exception and does not itself grant Gate 2.

Implemented:

- `src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution.py`;
- `scripts/ny_osc_gate2_transient_local.ps1`;
- runtime authorization/result schemas;
- local-retention approval schema/evidence;
- unit + contract tests;
- `docs/audits/NY_OSC_TRANSIENT_LOCAL_FILE_RUNNER_OFFLINE.md`.

Verified behavior:

- both approvals required;
- dedicated OS-temp path required;
- `FINDERS.zip` required;
- Gate 2 byte bounds reused;
- ZIP read into memory;
- existing schema-discovery harness reused;
- raw local file logically deleted in `finally`;
- deletion failure stops fail-closed;
- no raw path or owner values returned;
- physical secure erasure is not claimed.

Checkpoint:

`688469e87fc39da20b7906b3825c81367a594b16`

CI:

`35359065170` — SUCCESS.

No real download or real owner PII processing occurred.

### 12. First real bounded execution — consumed fail-closed

Executed once.

Result:

`BLOCKED_FAIL_CLOSED / PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`

Persisted non-PII metadata:

- compressed archive bytes: `409,477,526`;
- archive members: `1`;
- selected text member uncompressed bytes: `1,939,569,781`;
- local raw file logically deleted: yes;
- no owner values returned or persisted.

Approvals consumed:

- Gate 2 v1: `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- transient-local v1: `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- v1 retry: not authorized.

Offline remediation checkpoint:

`151f3a2f16c74f604fa72cc1284b2f9cd2e73f52`

CI:

`35363685148` — SUCCESS.

### 13. Second bounded attempt proposal

Prepared:

`sources/proposals/ny_osc_owner_name_file_second_bounded_attempt_authorization.v1.json`

Runner:

`scripts/ny_osc_gate2_retry_transient_local.ps1`

Remediation checkpoint:

`151f3a2f16c74f604fa72cc1284b2f9cd2e73f52`

CI:

`35363685148 — SUCCESS`

No bounds are increased. A fresh listing check and two new single-use approvals are required before execution.

### 14. Second-attempt approvals granted

Product Owner granted both fresh v2 approvals.

Local retention:

`OWNER_APPROVAL_2026-09-18_NY_OSC_SECOND_TRANSIENT_LOCAL_FILE_BOUNDED_ONCE_8D2E1F64`

Transient PII:

`OWNER_APPROVAL_2026-09-18_NY_OSC_SECOND_BOUNDED_TRANSIENT_PII_ATTEMPT_ONCE_C41B7E93`

State:

`GRANTED_NOT_CONSUMED / SINGLE USE / ZERO RETRY`

Fresh preflight remains mandatory before the second download.

### 15. Second-attempt execution package verified

Checkpoint:

`d157046c9cdf375fe88918ddaf41f97422de70a4`

CI:

`35364955860 — SUCCESS`

Execution script:

`scripts/ny_osc_gate2_retry_transient_local.ps1`

Both v2 approvals are granted/not consumed. Fresh listing preflight is mandatory; any drift stops before download.

## 16. Third bounded attempt — offline proposal only

Prepared:

`sources/proposals/ny_osc_owner_name_file_third_bounded_attempt_authorization.v1.json`

Schema:

`schemas/common/ny_osc_third_attempt_authorization_proposal.schema.json`

Audit:

`docs/audits/NY_OSC_THIRD_ATTEMPT_OFFLINE_PROPOSAL.md`

State:

`PROPOSED_NOT_AUTHORIZED / REPOSITORY_ONLY / ZERO_SOURCE_ACCESS`

The proposal references integrated repair checkpoint
`85d5f0c1101e5d66add27b9e1f445e7bba54a3b0` and CI
`35381899112 — SUCCESS`. Bounds remain one download, zero retries and unchanged caps.
Both second-attempt approvals remain consumed and non-reusable. No third-attempt runner or
granted approval artifacts exist.

## 17. Third-attempt execution package — offline candidate

Runner:

`scripts/ny_osc_gate3_transient_local.ps1`

Approval templates:

- `sources/evidence/ny_osc_owner_name_file_third_attempt_transient_local_approval.v1.json`;
- `sources/evidence/ny_osc_owner_name_file_third_attempt_transient_pii_approval.v1.json`.

State:

`IMPLEMENTED_OFFLINE / CI_PENDING / BOTH APPROVALS NOT_GRANTED`

The runtime bridge now supports exact attempt-number binding. The historical second runner
binds to attempt 2 and the new runner binds to attempt 3. The third runner checks both grants,
attempt number, exact phrases, single-use/no-reuse/no-retry policy, and successful runner CI
before creating a temp directory.

No source access, listing preflight, download, owner-file opening, or PII processing occurred.

## Current Product State

- approved real sources: `0`;
- CA source: `HELD`;
- NY source: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: consumed/non-reusable;
- NY access instructions: `RECEIVED / REVIEWED NON-CONTENT ONLY`;
- NY Gate 2 v1: `CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO RETRY`;
- NY transient-local-file approval v1: `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- NY transient-local runner: `READY / VERIFIED OFFLINE`;
- NY bounded first schema-discovery harness: `READY / VERIFIED OFFLINE`;
- synthetic IN03 classification-to-reviewer path: `READY / VERIFIED`;
- NY pre-contact economics contract + reviewer exposure: `READY / VERIFIED`;
- follow-up cost measurement contract: `READY / VERIFIED`;
- follow-up cost → case economics integration: `READY / VERIFIED`;
- integrated economics reviewer/API/Streamlit: `READY / VERIFIED`;
- Streamlit deployment candidate: `DEPLOYED / VERIFIED_REMOTE_SYNTHETIC_ONLY`;
- current MVP-1 remote URL: `https://unclaimed-platform-mvp1-reviewer.streamlit.app/`;
- remote evidence: `PRODUCT_OWNER_SCREENSHOTS + CI_35345560301_SUCCESS`;
- real measured candidate costs: `0`;
- real MVP-1 candidates: `0`.

## Parallel Critical Paths

External:

`OSC email -> download constraints -> max_download_bytes -> Gate 2 -> bounded schema discovery`

Offline:

`synthetic downstream slice DONE -> value-evidence contract DONE -> follow-up cost measurement DONE -> economics integration DONE -> integrated reviewer exposure DONE -> deployment candidate DONE -> remote deploy VERIFIED`

## SINGLE NEXT ACTION

Execute exclusively:

`REVIEW_AND_INTEGRATE_NY_OSC_THIRD_ATTEMPT_RUNNER_OFFLINE`

Classification:

`A — Product Critical / Offline Safety Implementation`

Run CI and review the package. Do not grant approvals or access the source.
