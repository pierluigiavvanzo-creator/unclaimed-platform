# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ny-osc-owner-file-source-contract-privacy-gate-offline`

Latest product-critical lifecycle:

`CA_PATH_FROZEN_FOR_MVP1 -> ALTERNATIVE_SOURCE_BENCHMARK_COMPLETE -> NY_OSC_SELECTED -> NY_SOURCE_CONTRACT_PRIVACY_GATE_OFFLINE_READY -> NY_REQUEST_LINK_HUMAN_GATE_NEXT`

Classification: `A — Product Critical`.

Implementation audit:

`docs/audits/MVP1_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_PRIVACY_GATE_OFFLINE.md`

Implementation checkpoint before canonical state updates:

`29d91e3bb78838db9345991b3ade720283dc2440`

Implementation CI:

`35258458704` — SUCCESS.

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

The source contract preserves only OSC-disclosed semantics:

- owner name;
- last-known address;
- nature of property;
- when reported;
- reporting organization.

Owner name and last-known address are treated as PII. Dollar amount is not disclosed by the source and is represented as:

`UNKNOWN_FROM_SOURCE`

Physical file facts remain deliberately unknown until the first separately authorized file:

- physical column names;
- delimiter;
- encoding;
- archive layout;
- representation of `nature_of_property`;
- presence of a property identifier.

No production parser or classification activation is allowed before fail-closed schema discovery.

## New York Insurance Boundary

Current authority-index evidence records the New York insurance vocabulary as:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN12, IN77`

Primary MVP-1 target:

`IN03 — Proceeds Due Beneficiaries`

The official property-type PDF could not be directly opened by the research tooling because OSC returned HTTP 403; the policy records this provenance limitation and does not claim visual PDF verification.

## Privacy / Authorization Boundary

First real file schema discovery is designed as:

`MEMORY_ONLY`

During that first discovery:

- raw owner file persistence: forbidden;
- owner-row persistence: forbidden;
- owner name/address logging: forbidden;
- row-specific human inspection: forbidden;
- derived non-PII schema metadata may persist.

Two separate single-use gates are defined:

1. `HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`
   - submit the official OSC request and receive access instructions only;
   - no Owner Name File download;
   - no real owner PII processing.

2. `HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`
   - later, exactly one bounded download and memory-only schema discovery;
   - requires an explicit `max_download_bytes` discovered/defined before authorization;
   - no default byte cap is invented.

## Contract / Test State

Added:

- `schemas/agents/a01_acquisition_request.v1.1.schema.json`;
- `schemas/agents/a01_acquisition_result.v1.1.schema.json`;
- `schemas/examples/a01_ny_owner_name_file.examples.json`;
- `policies/states/NY/ny_osc_owner_name_file.v1.json`;
- `src/unclaimed_platform/adapters/sources/new_york_osc.py`;
- NY unit and contract tests.

Historical A01 v1.0 California contracts remain unchanged. A01 v1.1 supports `CA` and `NY` while preserving REAL approval and raw-ingest-only controls.

CI `35258458704` passed Ruff, mypy, contract tests, smoke tests, full pytest, Streamlit safety/startup, frontend lint, typecheck and build.

## Current Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- California `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- New York OSC Owner Name File: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY request submitted: no;
- NY real owner PII processed: no;
- production insurance classification: inactive;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Classification: `A — Product Critical`.

This human gate may authorize exactly one submission of the official New York OSC Owner Name File request for the purpose of receiving access instructions / secure-file-link information.

It must **not** authorize Owner Name File download, real owner PII processing, raw persistence, schema parsing, identity resolution, beneficiary matching, outreach, representation, fee agreement or claim activity.

After access instructions are obtained, determine the observable download constraints and prepare the separate bounded `HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION` gate.