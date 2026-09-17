# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ny-osc-owner-file-source-contract-privacy-gate-offline`

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

## California Path

Latest California live run:

`35255228459` — attempt `1` — SUCCESS.

Result:

- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- source response bytes: `524288`;
- no stop.

California source remains `HELD / NOT YET APPROVED`, not rejected. The current CA SCO `PROPERTY_TYPE` discovery path is frozen for MVP-1 absent genuinely new evidence. Consumed CA approvals are non-reusable.

## Alternative Source Benchmark

Completed:

`BENCHMARK_MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_OFFLINE`

Audit:

`docs/audits/MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_BENCHMARK.md`

Selected next candidate:

`New York Office of the State Comptroller — Owner Name File`

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

## Completed Current Action

Executed:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

Classification: `A — Product Critical`.

Audit:

`docs/audits/MVP1_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_PRIVACY_GATE_OFFLINE.md`

Implementation commits:

- initial implementation: `967be6fa396136c267586811fecd3003abb73b91`;
- Ruff-only remediation: `29d91e3bb78838db9345991b3ade720283dc2440`.

Implementation CI:

`35258458704` — SUCCESS.

The first CI run `35258369752` failed only on four Ruff E501 line-length violations in the new NY adapter; no substantive test ran before that lint stop. Commit `29d91e3b...` wrapped those lines without changing logic. The succeeding run passed Ruff, mypy, contract tests, smoke tests, full pytest, Streamlit safety/startup, frontend lint/typecheck/build.

No New York request was submitted, no secure FTP link was obtained, no Owner Name File was downloaded, and no real owner PII was processed.

## New York Registry / Contract State

`sources/registry.yaml` now includes:

`ny.osc.unclaimed_funds.owner_name_file`

State:

- `enabled: false`;
- `approved_for_use: false`;
- provenance required;
- candidate only.

A01 was extended side-by-side rather than silently rewriting the historical California contract:

- `schemas/agents/a01_acquisition_request.v1.1.schema.json`;
- `schemas/agents/a01_acquisition_result.v1.1.schema.json`;
- `schemas/examples/a01_ny_owner_name_file.examples.json`.

A01 v1.1 accepts jurisdictions `CA` and `NY`, preserves `RAW_INGEST_ONLY`, and still requires an explicit approval reference for REAL mode. Historical A01 v1.0 remains unchanged.

## New York Machine Source / Privacy Policy

Policy:

`policies/states/NY/ny_osc_owner_name_file.v1.json`

Authority-disclosed semantic fields modeled:

- `owner_name` — PII;
- `last_known_address` — PII;
- `nature_of_property`;
- `reported_when`;
- `reported_by`.

Do not invent the real file's:

- physical column names;
- delimiter;
- encoding;
- archive layout;
- representation of `nature_of_property`;
- Property ID presence.

The policy therefore sets the physical file contract to:

`UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE`

and prohibits parser/classification activation before observed schema mapping.

Dollar value is not disclosed by the Owner Name File and is represented as:

`UNKNOWN_FROM_SOURCE`

No amount may be invented.

## New York Insurance Boundary

Current authority-index evidence records:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN12, IN77`

Primary MVP-1 target:

`IN03 — Proceeds Due Beneficiaries`

Important provenance limitation:

The official OSC Property Type Tables PDF URL was identified, but direct browser opening returned HTTP 403 in the research tooling. The machine policy therefore records:

`OFFICIAL_INDEX_TEXT_VERIFIED_PDF_DIRECT_OPEN_BLOCKED_403_IN_TOOLING`

Do not claim a visual PDF review unless later evidence establishes one.

## First Real File Privacy Design

First-file schema discovery mode:

`MEMORY_ONLY`

During first discovery:

- no raw Owner Name File persistence;
- no complete owner-row persistence;
- no owner name/address logging;
- no row-specific human inspection;
- derived non-PII schema metadata may persist;
- later raw persistence requires a separate trusted policy.

The fail-closed adapter:

`src/unclaimed_platform/adapters/sources/new_york_osc.py`

performs no network access and blocks even an approved boundary with `FIRST_FILE_SCHEMA_DISCOVERY_REQUIRED` until the separate first-file gate is completed.

## Two Distinct Human Gates

### Gate 1 — request access only

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

May authorize exactly one submission of the official OSC Owner Name File request to receive access instructions / secure-file-link information.

This gate does NOT authorize:

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

The official request form requires requester contact information including name, company, phone and email. Do not invent those values.

### Gate 2 — later bounded first download

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

This gate is not yet ready to execute. Before requesting it, obtain the access instructions/link and determine an explicit maximum download byte bound. The policy intentionally provides no default byte cap.

When later authorized, Gate 2 may cover exactly one bounded download plus memory-only schema discovery with transient owner PII. It remains single-use, non-reusable and no retry/rerun is implicitly authorized.

## Source / Product State

- approved real sources: `0`;
- California source: `HELD`;
- CA `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- NY OSC Owner Name File: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY request submitted: no;
- NY real PII processed: no;
- production parser/classification: inactive;
- real MVP-1 candidates: `0`.

## Task-Relevant Artifacts for Next Work

Inspect at least:

1. `docs/audits/MVP1_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_PRIVACY_GATE_OFFLINE.md`;
2. `policies/states/NY/ny_osc_owner_name_file.v1.json`;
3. `sources/registry.yaml`;
4. `schemas/agents/a01_acquisition_request.v1.1.schema.json`;
5. `schemas/agents/a01_acquisition_result.v1.1.schema.json`;
6. `src/unclaimed_platform/adapters/sources/new_york_osc.py`;
7. official OSC Owner Name File request page.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Classification: `A — Product Critical`.

A fresh explicit Product Owner authorization is required before submitting the official OSC request form or disclosing requester contact information to OSC.

The authorization scope must be request/access-instructions only. It must not be interpreted as approval to download the owner file or process owner PII.

After the request is submitted and access instructions are available:

`inspect access/download constraints without owner-file processing -> define explicit max_download_bytes -> HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION -> one bounded memory-only schema discovery -> source/schema decision -> insurance classification -> candidate -> economics -> reviewer`.