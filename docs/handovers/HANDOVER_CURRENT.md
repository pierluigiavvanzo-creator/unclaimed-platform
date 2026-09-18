# HANDOVER_CURRENT.md

Last updated: 2026-09-18

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ny-offline-vertical-slice-integrated`

Latest verified product implementation checkpoint:

`d94a86f8d774d40c9170f9da2234dd53eb3feff9`

Product implementation CI:

`35318092067` — SUCCESS.

Canonical documentation refresh CI:

`35318343802` — SUCCESS.

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

## Current Product State

- approved real sources: `0`;
- CA source: `HELD`;
- NY source: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: consumed/non-reusable;
- NY access instructions: pending;
- NY Gate 2: not granted;
- synthetic IN03 classification-to-reviewer path: `READY / VERIFIED`;
- NY pre-contact economics contract + reviewer exposure: `READY / VERIFIED`;
- real MVP-1 candidates: `0`.

## Parallel Critical Paths

External:

`OSC email -> download constraints -> max_download_bytes -> Gate 2 -> bounded schema discovery`

Offline:

`synthetic downstream slice DONE -> value-evidence contract DONE -> reviewer integration DONE -> measured follow-up-cost contract NEXT`

## SINGLE NEXT ACTION

Execute exclusively:

`IMPLEMENT_NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE`

Classification:

`A — Product Critical`

Goal:

Create a deterministic, provenance-bearing contract for the commercial measurements already required by MVP-1:

- automated processing cost per candidate;
- source/data cost per candidate where applicable;
- human review time per candidate;
- additional manual research effort.

Use synthetic/test inputs only. Do not invent default monetary/time assumptions. The contract may accept measured values later but must keep them absent/unknown until real measurement evidence exists.

Do not access the Owner Name File, process real owner PII, perform outreach, create fee agreements or submit claims.
