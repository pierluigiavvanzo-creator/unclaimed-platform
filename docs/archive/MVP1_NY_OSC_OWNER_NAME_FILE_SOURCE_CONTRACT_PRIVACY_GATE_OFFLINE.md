# MVP-1 New York OSC Owner Name File — Source Contract and Privacy Gate Offline

Date: 2026-09-17

Status: **IMPLEMENTED OFFLINE — REAL REQUEST/DOWNLOAD STILL HUMAN-GATED**

Classification: `A — Product Critical`.

## Scope

Implement exclusively:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

No Owner Name File request was submitted, no secure FTP link was obtained, no owner file was downloaded, and no real owner PII was processed.

## Product purpose

Move the selected New York source from `BENCHMARKED` to a deterministic `INTEGRATED CANDIDATE CONTRACT` without pretending that the physical file schema is already known.

The critical path remains:

`candidate contract -> request-link authorization -> first-download/transient-PII authorization -> fail-closed schema discovery -> source decision -> insurance classification -> candidate -> economics -> reviewer`.

## Official authority evidence used

- Owner Name File request: `https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form`
- Location Service Providers: `https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers`
- Property Type Tables: `https://www.osc.ny.gov/files/unclaimed-funds/reporters/pdf/property-type-tables.pdf`

Verified current HTML facts:

- the list can be requested and downloaded as a zipped delimited `.txt` file via a secure FTP link;
- disclosed semantics are owner name, last-known address, nature of property, when reported, and by whom reported;
- dollar values and taxpayer-identification numbers are not disclosed;
- the file is updated quarterly;
- the official request form asks for requester name, company, phone, and email.

Authority index text for the current New York property-type table exposes these insurance codes:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN12, IN77`.

`IN03` is `Proceeds Due Beneficiaries` and remains the narrow MVP-1 target.

Tooling limitation recorded: direct opening of the official Property Type Tables PDF returned HTTP `403` in the research browser. The contract therefore records the insurance vocabulary as `OFFICIAL_INDEX_TEXT_VERIFIED_PDF_DIRECT_OPEN_BLOCKED_403_IN_TOOLING`; it does not claim a visual PDF review in this package.

## Repository changes

### Candidate registry

`sources/registry.yaml`

Adds:

`ny.osc.unclaimed_funds.owner_name_file`

State remains:

- `enabled: false`;
- `approved_for_use: false`;
- provenance required.

Registration is not source activation.

### A01 contract extension

Added side-by-side schemas rather than mutating the historical California v1.0 contracts:

- `schemas/agents/a01_acquisition_request.v1.1.schema.json`
- `schemas/agents/a01_acquisition_result.v1.1.schema.json`

v1.1 allows jurisdictions `CA` and `NY`; all existing approval, raw-ingest-only and fail-closed requirements remain.

Existing v1.0 files remain unchanged and continue to represent the historical California contract.

Synthetic examples:

`schemas/examples/a01_ny_owner_name_file.examples.json`

The fixture's `max_bytes = 1` is deliberately non-executable contract data. It is not a proposed real byte limit. The real first-download maximum must be explicitly set in a later human authorization after the access path is known.

### Machine source/privacy policy

`policies/states/NY/ny_osc_owner_name_file.v1.json`

The policy records only authority-supported semantic fields and deliberately leaves the physical file contract unknown:

- physical column names unknown;
- delimiter unknown;
- encoding unknown;
- archive layout unknown;
- representation of `nature_of_property` unknown;
- Property ID presence unknown;
- parser activation forbidden;
- normalization forbidden;
- source activation forbidden before observed schema mapping.

Economics boundary:

`recoverable_value_state = UNKNOWN_FROM_SOURCE`

No amount may be invented from the owner list.

### Privacy boundary

The first real file schema-discovery design is:

`MEMORY_ONLY`

During that first discovery:

- raw file persistence: forbidden;
- owner-row persistence: forbidden;
- owner-name/address logging: forbidden;
- row-specific human inspection: forbidden;
- derived non-PII schema metadata may persist;
- any later raw persistence requires a separate policy.

Owner PII semantics are limited to the authority-disclosed owner name and last-known address; this does not assert that the unobserved physical file contains no other fields.

### Two fresh single-use human gates

Gate 1:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Scope: submit the official request and receive access instructions only. No owner file download.

Gate 2:

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

Scope: exactly one bounded first-file download plus memory-only schema discovery with transient real owner PII.

For Gate 2:

- explicit `max_download_bytes` is required;
- there is no default max byte value;
- retry/rerun is not authorized by default;
- the first gate does not implicitly authorize the second.

This separation avoids inventing a download bound before the secure file-access path is known.

### Fail-closed adapter

`src/unclaimed_platform/adapters/sources/new_york_osc.py`

The adapter performs no network activity. It blocks:

- wrong jurisdiction;
- non-REAL acquisition mode;
- scope expansion beyond `RAW_INGEST_ONLY`;
- acquisition while the source is unapproved;
- even an approved boundary until the first-file schema-discovery gate has been completed.

No parser or classifier for the raw Owner Name File is implemented because the property representation is not yet observed.

## Reuse-first result

Decision: `REUSE / WRAP`.

Reused:

- A01 request/result contract shape;
- existing acquisition dataclasses;
- fail-closed source-adapter pattern;
- repository provenance conventions;
- existing privacy/data-minimization principles;
- California lesson that authority semantics and physical source representation must remain separate.

No new dependency and no generic ingestion framework were introduced.

## Acceptance evidence

Synthetic/contract tests cover:

1. NY v1.1 A01 request validates only when REAL approval is present;
2. blocked NY result validates against A01 result v1.1;
3. registry keeps NY disabled and not approved;
4. policy contains only the five authority-disclosed semantic fields and marks owner name/address as PII;
5. all physical schema facts remain unknown until the first authorized file;
6. New York insurance vocabulary is source-specific and `IN03` is primary;
7. first-file discovery is memory-only and forbids raw/row persistence and PII logging;
8. request-link and first-download/transient-PII gates are distinct, single-use and non-reusable;
9. real byte cap has no invented default;
10. amount is `UNKNOWN_FROM_SOURCE`;
11. adapter remains fail-closed and cannot perform real acquisition.

## Not authorized by this package

- submission of the OSC request form;
- disclosure of Product Owner contact data to OSC;
- secure FTP access;
- Owner Name File download;
- real owner PII processing;
- raw owner-file persistence;
- production parser/classifier activation;
- identity resolution or beneficiary matching;
- outreach, representation, fee agreement or claim submission.

## Next gate after CI success

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

That gate should authorize one request submission only. After the access instructions/link are obtained, the repository must record the actual observable download constraints before asking for the separate first-download/transient-PII authorization.
