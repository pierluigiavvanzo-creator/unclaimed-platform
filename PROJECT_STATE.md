# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ny-osc-request-submitted`

Latest product-critical lifecycle:

`CA_PATH_FROZEN_FOR_MVP1 -> ALTERNATIVE_SOURCE_BENCHMARK_COMPLETE -> NY_OSC_SELECTED -> NY_SOURCE_CONTRACT_PRIVACY_GATE_OFFLINE_READY -> NY_REQUEST_LINK_AUTHORIZATION_GRANTED -> NY_REQUEST_SUBMITTED_GATE1_CONSUMED -> AWAITING_NY_OSC_ACCESS_INSTRUCTIONS`

Classification: `A — Product Critical`.

Authorization evidence:

`sources/evidence/ny_osc_owner_name_file_request_link_authorization.v1.json`

Gate 1 approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

## California State

Latest California live run:

`35255228459` — attempt `1` — SUCCESS.

Observed:

- source bytes: `524288`;
- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- stop reason: none.

California source approval remains `HELD / NOT YET APPROVED`. The current California SCO `PROPERTY_TYPE` discovery path is frozen for MVP-1 pending genuinely new evidence.

## New York OSC Owner Name File

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

Registry state:

- registered: yes;
- enabled: false;
- approved for use: false;
- acquired: false;
- provenance required: true.

Physical file facts remain deliberately unknown until the first separately authorized file. No production parser or classification activation is allowed before fail-closed schema discovery.

## New York Insurance Boundary

Current authority-index evidence records the New York insurance vocabulary as:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN12, IN77`

Primary MVP-1 target:

`IN03 — Proceeds Due Beneficiaries`

## Privacy / Authorization Boundary

First real file schema discovery remains designed as `MEMORY_ONLY`.

During that first discovery:

- raw owner file persistence: forbidden;
- owner-row persistence: forbidden;
- owner name/address logging: forbidden;
- row-specific human inspection: forbidden;
- derived non-PII schema metadata may persist.

### Gate 1 — request-link authorization

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

State:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

On 2026-09-17 the Product Owner explicitly confirmed that the official OSC Owner Name File request form had been manually submitted once. This is a Product Owner attestation; the external OSC submission was not independently verified by repository tooling.

Requester contact values are intentionally not persisted in the repository.

Gate 1 does **not** authorize:

- Owner Name File download;
- real owner PII processing;
- raw persistence;
- schema parsing;
- identity resolution;
- beneficiary matching;
- outreach;
- representation;
- fee agreement;
- claim activity.

### Gate 2 — later first download

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

State:

`NOT GRANTED / NOT READY`

Before Gate 2 can be requested:

1. receive OSC access instructions;
2. determine observable download constraints without processing Owner Name File contents;
3. define an explicit `max_download_bytes`;
4. separately review and authorize the first bounded transient-PII download/schema-discovery action.

No default byte cap may be invented.

## Contract / Test State

Existing NY offline package remains verified by CI `35258809399`:

- Ruff: PASS;
- mypy: PASS;
- contract tests: PASS;
- smoke tests: PASS;
- full pytest: PASS;
- Streamlit safety/startup: PASS;
- frontend lint/typecheck/build: PASS.

The Gate 1 consumption update changes repository evidence/state only; it does not activate any production source or parser.

## Current Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- California `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- New York OSC Owner Name File: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1 authorization: `CONSUMED / NON-REUSABLE`;
- NY request submitted: yes, Product Owner confirmed manual submission;
- NY access instructions obtained: no;
- NY real owner PII processed: no;
- NY Gate 2 authorization: not granted;
- production insurance classification: inactive;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`AWAIT_NY_OSC_ACCESS_INSTRUCTIONS`

Classification: `A — Product Critical / External Dependency`.

When the OSC email/access instructions arrive, capture only the non-content access/download constraints needed to define a bounded first-download proposal. Do not download or inspect the Owner Name File and do not process owner PII until Gate 2 is separately reviewed and granted.
