# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-alternative-lawful-source-benchmark-offline`

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

Then inspect task-relevant artifacts below.

## California Path — Current State

D-010 remains accepted for the California source-specific path:

`ROW_DEFER_CONTINUE_METADATA_ONLY`

Latest California one-shot live execution:

`35255228459` — attempt `1` — SUCCESS.

Observed:

- HEAD: `1`;
- Range GET: `4`;
- source response bytes: `524288`;
- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- stop reason: `null`.

The associated execution/privacy approvals are consumed and non-reusable. The temporary workflow and trigger were removed.

California source activation remains:

`HELD / NOT YET APPROVED`

The source is not rejected, but the current California SCO `PROPERTY_TYPE` discovery path is frozen for MVP-1 pending genuinely new evidence. Do not repeat or merely widen the same scan.

## Completed Current Action

Executed:

`BENCHMARK_MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_OFFLINE`

Classification: `A — Product Critical`.

Audit:

`docs/audits/MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_BENCHMARK.md`

No real owner-level source file was requested or downloaded and no new real PII was processed.

## Benchmark Decision

Selected next source candidate:

`New York Office of the State Comptroller — Owner Name File`

Proposed source id:

`ny.osc.unclaimed_funds.owner_name_file`

Official authority references used in the benchmark:

- Owner Name File request: `https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form`
- Location Service Providers: `https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers`
- Location-service requirements: `https://www.osc.ny.gov/files/unclaimed-funds/resources/2025/pdf/aplsp-requirements-and-procedures-highlight-changes-1.pdf`
- Property Type Tables: `https://www.osc.ny.gov/files/unclaimed-funds/reporters/pdf/property-type-tables.pdf`
- Insurance reference sheet: `https://www.osc.ny.gov/files/unclaimed-funds/reporters/pdf/insurance-companies.pdf`

Officially observed facts relevant to MVP-1:

- OSC offers a requested owner list delivered as a zipped delimited text file through secure FTP;
- the list is updated quarterly;
- disclosed semantics include owner name, last-known address, nature of property, when reported and reporting organization;
- dollar values and taxpayer-identification numbers are not disclosed;
- the list excludes some records, including accounts under `$20`, foreign-address records, records without owner name/address and certain older book records;
- OSC explicitly publishes an Abandoned Property Location Service Provider framework;
- current published requirements state licensing/registration is not required, later representation requires direct contact and a compliant written/notarized agreement, and the fee may not exceed `15%`;
- New York authority-backed insurance property types include `IN03 — Proceeds Due Beneficiaries`.

Do **not** assume the real downloadable file's physical schema, column names, delimiter, encoding, property-code representation or Property ID presence until the first authorized file is actually obtained and inspected.

Because the owner list does not disclose amounts, any early economic assessment must represent monetary value as unsupported/unknown unless a later lawful evidence source establishes it.

## Other Benchmark Candidates

### Texas Comptroller SIFT

Disposition: `DEFER / SECONDARY`.

The Comptroller dataset page states that SIFT can provide secured datasets such as Unclaimed Property, but another current Open Records page does not enumerate Unclaimed Property in its SIFT list. Exact public access and fields are therefore not sufficiently resolved for immediate integration.

### Pennsylvania Treasury OpenBookPA

Disposition: `DEFER`.

Reviewed official downloadable data are county-level aggregate information, useful for market sizing but not an evidenced owner-level candidate feed.

### Illinois State Treasurer I-CASH

Disposition: `REJECT FOR BULK MVP-1 INGEST`.

Official FAQ states there are no bulk data files, database exports or API access to unclaimed-property records.

### Washington Department of Revenue

Disposition: `REJECT FOR COMMERCIAL LIST ACQUISITION`.

Washington identifies a public-record `Listing of Unclaimed Property`, but its official public-records page states that lists of individuals/taxpayers cannot be released when requested for a commercial purpose. This conflicts with the MVP-1 business model.

## Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- CA `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- New York OSC Owner Name File: `SELECTED CANDIDATE / NOT APPROVED / NOT ACQUIRED`;
- production insurance classification: inactive;
- real MVP-1 candidates: `0`.

## Task-Relevant Artifacts for Next Work

Inspect at least:

1. `docs/audits/MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_BENCHMARK.md`;
2. `sources/registry.yaml`;
3. `schemas/agents/a01_acquisition_request.schema.json`;
4. `schemas/agents/a01_acquisition_result.schema.json`;
5. `schemas/examples/a01_acquisition.examples.json`;
6. existing privacy/source-authorization patterns from the California work;
7. current New York OSC authority pages listed above.

## SINGLE NEXT ACTION

Execute exclusively:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

Classification: `A — Product Critical`.

Goal:

Prepare the minimum deterministic and versioned source candidate contract required before requesting/downloading the real New York Owner Name File.

The offline package must:

1. register or model the New York source as **candidate only**, disabled and not approved;
2. preserve only semantics actually disclosed by OSC without inventing physical file columns;
3. encode the current authority-backed New York insurance vocabulary needed for MVP-1, with `IN03` as the primary life-insurance target;
4. represent monetary value as `UNKNOWN_FROM_SOURCE` at this stage;
5. define raw-file and transient PII boundaries for owner name/address;
6. define a fail-closed first-real-file schema-discovery step;
7. define fresh single-use human gates for external file request/download and real PII processing;
8. use synthetic fixtures/tests only.

No New York Owner Name File request/download, real PII processing, outreach, representation, fee agreement or claim activity is authorized by this offline task.