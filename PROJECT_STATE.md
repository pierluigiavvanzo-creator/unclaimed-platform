# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-alternative-lawful-source-benchmark-offline`

Latest product-critical lifecycle:

`CA_D010_VALIDATED -> CA_DEEPER_LIVE_1024_ROWS_ZERO_INSURANCE -> CA_PROPERTY_TYPE_PATH_FROZEN_FOR_MVP1 -> ALTERNATIVE_SOURCE_BENCHMARK_COMPLETE -> NY_OSC_OWNER_NAME_FILE_SELECTED -> NY_SOURCE_CONTRACT_PRIVACY_GATE_NEXT`

Classification: `A — Product Critical`.

Latest benchmark:

`docs/audits/MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_BENCHMARK.md`

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

California source approval remains `HELD / NOT YET APPROVED` and the source is not rejected. The current California SCO `PROPERTY_TYPE` discovery path remains frozen for MVP-1 pending genuinely new evidence. Consumed approvals are non-reusable and no one-shot workflow remains armed.

## Alternative Source Benchmark Result

Selected next source candidate:

`New York Office of the State Comptroller — Owner Name File`

Proposed internal source id for the next package:

`ny.osc.unclaimed_funds.owner_name_file`

Why selected:

- first-party New York OSC authority;
- official request path for a zipped delimited owner file;
- file updated quarterly;
- officially disclosed semantics include owner name, last-known address, nature of property, when reported and reporting organization;
- New York publishes authority-backed insurance property types including `IN03 — Proceeds Due Beneficiaries`;
- OSC explicitly publishes a framework for Abandoned Property Location Service Providers, including a 15% maximum fee and no licensing/registration requirement under the current published requirements;
- materially lower semantic friction than the California feed.

Known constraints:

- the exact downloadable file delimiter, physical column names, encoding and code representation have not yet been observed and must not be invented;
- dollar values and taxpayer-identification numbers are not disclosed in the public list;
- the list omits some categories, including accounts under $20, foreign-address records and certain records without owner name/address;
- owner name/address are PII and require a fresh privacy authorization before real acquisition/processing;
- no source activation, outreach, representation, fee agreement or claim submission is authorized.

Other benchmark outcomes:

- Texas SIFT: `DEFER / SECONDARY` — official evidence indicates an Unclaimed Property SIFT path but access/schema evidence is not yet sufficiently consistent;
- Pennsylvania OpenBookPA: `DEFER` — reviewed data are aggregate rather than an evidenced candidate-level feed;
- Illinois I-CASH: `REJECT FOR BULK MVP-1 INGEST` — official FAQ states no bulk data/database export/API;
- Washington DOR: `REJECT FOR COMMERCIAL LIST ACQUISITION` — official public-records guidance prohibits releasing lists of individuals/taxpayers for commercial purpose.

## Current Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- California `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- New York OSC Owner Name File: `SELECTED CANDIDATE / NOT APPROVED / NOT ACQUIRED`;
- production classification: inactive;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

Classification: `A — Product Critical`.

Goal:

Create the smallest versioned source candidate contract, authority-backed insurance policy boundary and privacy/acquisition gate needed for a later authorized New York Owner Name File request and first-file inspection, using synthetic fixtures only.

Must not invent the real file schema. The first real file must enter a fail-closed schema-discovery step before production parsing.

No New York Owner Name File request/download or real PII processing is authorized by this offline action.