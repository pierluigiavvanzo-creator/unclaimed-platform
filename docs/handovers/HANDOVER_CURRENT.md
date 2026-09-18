# HANDOVER_CURRENT.md

Last updated: 2026-09-18

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ny-integrated-economics-reviewer-offline`

Latest verified product implementation checkpoint:

`8274660554733d39e7dc7c522676bc709fb90214`

Product implementation CI:

`35339962098` — SUCCESS.

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

## Current Product State

- approved real sources: `0`;
- CA source: `HELD`;
- NY source: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: consumed/non-reusable;
- NY access instructions: pending;
- NY Gate 2: not granted;
- synthetic IN03 classification-to-reviewer path: `READY / VERIFIED`;
- NY pre-contact economics contract + reviewer exposure: `READY / VERIFIED`;
- follow-up cost measurement contract: `READY / VERIFIED`;
- follow-up cost → case economics integration: `READY / VERIFIED`;
- integrated economics reviewer/API/Streamlit: `READY / VERIFIED`;
- current MVP-1 remote deployment URL/evidence: `NOT RECORDED`;
- real measured candidate costs: `0`;
- real MVP-1 candidates: `0`.

## Parallel Critical Paths

External:

`OSC email -> download constraints -> max_download_bytes -> Gate 2 -> bounded schema discovery`

Offline:

`synthetic downstream slice DONE -> value-evidence contract DONE -> follow-up cost measurement DONE -> economics integration DONE -> integrated reviewer exposure DONE -> deployment candidate NEXT`

## SINGLE NEXT ACTION

Execute exclusively:

`PREPARE_NY_MVP1_REVIEWER_DEPLOYMENT_CANDIDATE_OFFLINE`

Classification:

`A — Product Critical`

Goal:

Prepare the verified integrated MVP-1 Streamlit reviewer for deployment without changing authorization state.

Required boundaries:

- validate Streamlit entrypoint/requirements/startup;
- keep synthetic/test-only values clearly labeled;
- align legacy M3-only display wording to MVP-1 reviewer language where this is presentation-only;
- document deployment checklist and rollback checkpoint;
- keep approved real sources at zero;
- keep Gate 2 ungranted;
- no Owner Name File download, real PII, outreach, fee agreement, representation or claim activity.

No remote deployment may be claimed until a real deployment URL is observed and remotely verified.
