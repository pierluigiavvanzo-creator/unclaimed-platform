# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-synthetic-vertical-slice-offline`

Latest product-critical lifecycle:

`NY_OSC_SELECTED -> NY_SOURCE_CONTRACT_READY -> NY_GATE1_GRANTED_NOT_CONSUMED -> REQUESTER_CONTACT_INPUTS_UNAVAILABLE -> SYNTHETIC_DOWNSTREAM_VERTICAL_SLICE_READY -> RECOVERABLE_VALUE_EVIDENCE_PATH_NEXT`

Classification: `A — Product Critical`.

Implementation audit:

`docs/audits/MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE.md`

Stable implementation checkpoint before canonical documentation updates:

`caedbb67c3077a654533a5c96dab42cbfa4e0cf3`

Implementation CI:

`35263620224` — SUCCESS.

## California State

California source remains `HELD / NOT YET APPROVED`; the current CA SCO `PROPERTY_TYPE` discovery path remains frozen for MVP-1 absent genuinely new evidence.

Latest bounded California live evidence remains run `35255228459`: `1024` rows examined, `1024` deferred, `0` recognized insurance rows, `0` IN03, under the same `524288` source-response-byte envelope.

## New York OSC Source State

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

State:

- registered: yes;
- enabled: false;
- approved for use: false;
- acquired: false;
- physical file schema: `UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE`;
- source dollar value: `UNKNOWN_FROM_SOURCE`;
- production parser/classification: inactive.

Primary MVP-1 insurance target remains:

`IN03 — Proceeds Due Beneficiaries`

## Gate 1 — Request Link

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

State:

`GRANTED_SINGLE_USE_NOT_CONSUMED_PENDING_REQUESTER_CONTACT_DATA`

No OSC request has been submitted. Required requester values remain unavailable:

- name;
- company;
- phone;
- email.

Those values must not be invented or inferred.

Gate 1 does not authorize Owner Name File download or real owner PII processing.

Gate 2 remains not granted and requires an explicit `max_download_bytes` after access instructions are obtained.

## Synthetic MVP-1 Downstream Slice

Completed offline without real source access or PII:

`SYNTHETIC_POST_SCHEMA_MAPPING -> exact NY insurance classification -> IN03 candidate -> economics -> reviewer`

Implemented:

- exact-code deterministic NY insurance classifier for the recorded vocabulary;
- only exact `IN03` creates the narrow MVP-1 synthetic candidate;
- deterministic synthetic case id;
- no identity resolution or beneficiary matching;
- economics preserves `UNKNOWN_FROM_SOURCE` and refuses invented amounts/thresholds;
- API endpoint `GET /api/reviewer/mvp1/synthetic-case`;
- Streamlit MVP-1 case/economics section;
- versioned JSON Schema and unit/contract/smoke tests.

Reviewer decision produced by the synthetic case:

`CONTINUE_VALUE_RESEARCH_OR_STOP`

Required economic evidence identified:

- recoverable value evidence;
- expected follow-up cost;
- lawful fee basis.

## Verification

CI `35263620224` passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety/startup;
- frontend lint/typecheck/build.

## Current Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- NY source: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: `GRANTED / NOT CONSUMED`;
- NY request submitted: no;
- NY real owner PII processed: no;
- NY Gate 2: not granted;
- synthetic IN03 candidate-to-review path: `READY / VERIFIED`;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`BENCHMARK_NY_MVP1_RECOVERABLE_VALUE_EVIDENCE_PATHS_OFFLINE`

Classification: `A — Product Critical`.

Goal:

Identify and compare lawful, evidence-backed ways to obtain or estimate the recoverable monetary value and expected follow-up cost for a future New York `IN03` candidate without inventing source amounts and without requiring the currently unavailable OSC requester contact inputs.

The benchmark should prefer official/public/authorized sources and reusable capabilities, and must distinguish exact value evidence from proxies or market-level estimates.

No real owner PII, outreach, representation, fee agreement or claim activity is authorized by this offline action. Gate 1 remains parked and unconsumed until explicit requester contact values become available.
