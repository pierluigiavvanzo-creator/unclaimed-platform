# M3 California SCO Data-Scope Inspection Proposal

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANDIDATE PROPOSAL — NON-AUTHORIZING — NO NETWORK / NO BODY ACCESS**

## Objective

Define a bounded, machine-readable proposal for inspecting only enough of the California SCO bulk ZIP
to resolve archive structure and CSV header uncertainty before source approval.

This task does **not** execute the inspection. It performs no SCO network request, reads no archive
body bytes, downloads no ZIP/CSV data, processes no real PII, performs no identity resolution,
beneficiary matching or outreach, and does not change the source-access policy or registry.

## REUSE FIRST result

The repository already contains the authority and evidence needed to define the proposal:

- canonical `SourceApprovalPackage` v1;
- canonical SCO transport-preflight execution/evidence;
- canonical `PROPOSED` SCO source-access policy;
- disabled/not-approved SCO registry entry;
- deterministic privacy/data-minimization gates;
- versioned JSON Schema and contract-test conventions.

No new runtime dependency is introduced. This proposal deliberately stops before implementation of a
range client or ZIP parser. A future execution implementation must be reviewed separately after an
explicit owner execution gate.

## Why a separate proposal contract

The canonical source-approval package remains blocked because archive contents, CSV row layout,
record-level fields and PII necessity are unknown. It cannot truthfully authorize fields or PII.

The data-scope inspection proposal therefore carries only a proposed inspection envelope. Its schema
fixes all authorization flags to `false`, fixes body bytes read to `0`, and requires a future explicit
execution approval reference before any range request or body access can occur.

## Canonical evidence reused

Transport evidence:

`sources/evidence/ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json`

Facts reused without another source request:

- endpoint: `https://claimit.ca.gov/upd-property-records/00_All_Records.zip`;
- host: `claimit.ca.gov`;
- HTTPS;
- media type: `application/zip`;
- content length: `3,203,972,130` bytes;
- `Accept-Ranges: bytes` observed;
- prior request timeout control: 10 seconds;
- prior response-body bytes read: `0`.

The proposal requires these transport facts to match again at execution time. Endpoint, media type or
content-length drift blocks execution and requires review/new preflight rather than silently widening
scope.

## Inspection purpose

Purpose remains:

`SOURCE_STRUCTURE_VERIFICATION_ONLY`

Allowed evidence categories are limited to:

- archive member names;
- archive member structural metadata: name, size, compression, encryption indicator and offset;
- a first logical CSV record only when it can safely be treated as a header candidate without reading
  any subsequent data row;
- delimiter, encoding, column count and header-confidence metadata;
- potential PII-presence indicators derived **only from header labels**.

Explicitly prohibited:

- CSV data rows;
- record values;
- identity resolution;
- beneficiary matching;
- outreach;
- downstream record use;
- full-body download.

If verifying structure would require reading a data row, execution must stop with
`DATA_ROW_ACCESS_WOULD_BE_REQUIRED`.

## Bounded range plan

The numeric limits below are **project safety caps**, not observed facts about the source archive.
They intentionally bound a later structure-only execution and may cause fail-closed review if the
archive cannot be inspected within them.

### Archive tail probe

- suffix range maximum: `131,072` bytes (128 KiB);
- maximum requests: one;
- purpose: locate enough ZIP tail structure to identify central-directory location/size;
- if required tail structure is not found inside the cap: STOP.

### Central-directory probe

- maximum response bytes: `4,194,304` bytes (4 MiB);
- maximum requests: one;
- maximum archive members: `10,000`;
- only central-directory/member metadata may be derived;
- unsafe member paths, encrypted members or unsupported compression cause STOP.

Supported compression methods proposed for a later bounded implementation:

- `STORED`;
- `DEFLATED`.

Any other compression method remains unimplemented/unreviewed and therefore blocks.

### CSV member header probes

Candidate member extension:

`.csv`

Limits:

- maximum candidate CSV members: `10`;
- maximum response bytes per member probe: `1,048,576` bytes (1 MiB);
- maximum decompressed bytes per member: `65,536` bytes (64 KiB);
- maximum logical CSV records parsed per member: `1`;
- maximum data rows parsed: `0`.

The first logical record is an **observed header candidate**, not automatically a verified schema.
Header labels may be persisted as derived structure evidence only if deterministic inspection can
classify the record as header-like without accessing a following data row. If header status is
ambiguous, stop without persisting candidate values.

## Global byte/request budget

Maximum range requests:

`12`

Budget composition:

- 1 archive-tail request;
- 1 central-directory request;
- up to 10 CSV member-prefix requests.

Maximum total source response-body bytes:

`14,811,136`

This is exactly:

`131,072 + 4,194,304 + (10 × 1,048,576)`

The decompressed 64 KiB/member cap is an in-memory output cap and does not enlarge the network-body
budget.

If either request count or byte budget would be exceeded, STOP/HUMAN_REVIEW.

## Transport controls proposed for later execution

A later authorized execution must use:

- HTTPS only;
- host `claimit.ca.gov` only;
- same-host redirects only;
- `HTTP Range GET` only;
- no full-body GET;
- 10-second per-request network-inactivity timeout;
- exact expected media type `application/zip`;
- exact expected content length `3,203,972,130` before range inspection;
- `Accept-Ranges: bytes` required;
- partial/range semantics required; an unexpected full-body response blocks immediately.

The proposal does not create a network client or execution workflow.

## Privacy and quarantine controls

Any future authorized inspection must:

- operate in quarantine;
- process source body bytes in memory only;
- create no temporary source files;
- persist no raw ZIP/member/header bytes;
- persist no record values;
- keep source body bytes and record values out of logs;
- enforce least privilege and access logging;
- encrypt any derived evidence persisted at rest;
- delete transient buffers after inspection;
- permit no export, matching or outreach.

The only potentially persisted source-derived content is structure evidence such as archive member
names and safely classified header labels. If a candidate first record could instead be real record
values, those values must not be persisted.

## Proposed machine-readable outputs

A later execution result should contain only:

1. execution approval reference and observation timestamp;
2. requested byte ranges, response status/content-range and bytes read;
3. revalidated transport metadata;
4. archive member names;
5. structural member metadata: name, size, compression, encryption flag and offset only;
6. per-CSV-member header-candidate metadata: labels, delimiter, encoding, column count and
   header-confidence state, only under the header persistence rule;
7. potential PII indicators derived only from header labels;
8. stop reason when the bounded inspection cannot safely continue.

Raw source body bytes and record values are not output artifacts.

## PII handling semantics

The proposal does not declare that PII is present or absent. Current source-approval state remains:

`PII necessity = UNDETERMINED_BLOCKING`

A future structure-only inspection may emit only **potential header-label indicators**. Those indicators
are not a legal determination and do not authorize PII processing. No data-row values may be read to
confirm PII presence under this proposal.

## Stop conditions

Execution must fail closed on any of these conditions:

- transport metadata drift;
- byte ranges unsupported;
- a range request unexpectedly returns non-partial/full-body behavior;
- required ZIP tail structure not found inside the tail cap;
- central directory larger than 4 MiB;
- archive member count exceeds 10,000;
- unsafe member path;
- encrypted member;
- unsupported compression;
- no `.csv` member;
- more than 10 CSV candidates;
- member prefix/decompression cap exhausted;
- first logical record incomplete within the cap;
- header candidate ambiguous;
- data-row access would be required;
- total byte budget exceeded;
- range-request budget exceeded;
- any unexpected response-body behavior.

## Machine-readable artifacts

- `schemas/common/source_data_scope_inspection_proposal.schema.json`;
- `schemas/examples/ca_sco_data_scope_inspection_proposal.examples.json`;
- `sources/proposals/ca_sco_unclaimed_property_bulk.data_scope_inspection.v1.json`;
- `tests/contract/test_ca_sco_data_scope_inspection_proposal.py`.

The contract rejects attempts to authorize execution, body access or CSV data-row parsing.

## Canonical state intentionally unchanged

This proposal does not modify:

- `policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json`;
- `sources/registry.yaml`;
- any acquisition adapter;
- any workflow that can perform network access.

Therefore:

- source policy remains `PROPOSED`;
- real acquisition remains unauthorized;
- registry remains `enabled: false`;
- registry remains `approved_for_use: false`;
- approved real sources remain `0`.

## Acceptance criteria

The candidate is acceptable only if:

1. proposal and valid example validate against JSON Schema draft 2020-12;
2. attempts to authorize execution/body access/data rows are invalid;
3. endpoint/host/media type/content length/timeout/range support cross-check canonical evidence;
4. byte and request budgets are internally exact and bounded;
5. current source-approval blockers remain unchanged;
6. policy and registry remain fail closed;
7. no execution script or one-shot network workflow is introduced;
8. Ruff, contract tests, smoke tests, full pytest, frontend regression and Streamlit smoke pass;
9. no SCO network request or source-body access occurs during this task.

## Rollback

The candidate is additive. Rollback is deletion of the proposal schema, examples, proposal payload,
contract test and this audit before promotion. No migration, runtime change, policy change or registry
change is required.

## Stop condition for this task

Stop after candidate CI and persistent-state documentation at a **human promotion gate**.

Promotion, if later approved, makes only this non-authorizing proposal canonical. A subsequent
separate owner gate is still required before implementing/running any range request or archive/header
inspection.
