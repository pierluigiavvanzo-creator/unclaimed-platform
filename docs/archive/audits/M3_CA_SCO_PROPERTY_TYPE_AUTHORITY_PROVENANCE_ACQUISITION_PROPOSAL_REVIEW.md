# M3 California SCO PROPERTY_TYPE Authority Provenance Acquisition Proposal Review

Date: 2026-09-15

## Scope

Review gate:
`HUMAN_PROPERTY_TYPE_AUTHORITY_PROVENANCE_ACQUISITION_PROPOSAL_REVIEW`

Reviewed package SHA:
`963c205b662cf56260ca7af14d71c65a6916c30f`

Reviewed artifacts:

- `schemas/common/property_type_authority_provenance_acquisition_proposal.schema.json`
- `sources/proposals/ca_sco_segment_500_plus.property_type_authority_provenance_acquisition.v1.json`
- `tests/contract/test_ca_sco_property_type_authority_provenance_acquisition_proposal.py`

Verified package CI:
`35005451605` — SUCCESS

This review was repository-only. No external authority content was retrieved or downloaded. No SCO dataset, `claimit.ca.gov`, source row, or source body was accessed.

## Decision

**PASS**

The bounded proposal is acceptable as a proposal for a later separately authorized one-shot authority archival execution.

This PASS does **not** authorize network retrieval, download, semantic extraction, source acquisition, runtime modification, or another semantic execution.

## Review Findings

### 1. Scope is narrow and pre-existing

The proposal contains exactly one authority target already retained in the repository:

`https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`

No authority discovery, crawling, link following, or second authority is permitted by the proposal.

### 2. Network boundary is bounded and fail-closed

If a later separate execution authorization is created, the proposal limits retrieval to:

- HTTPS;
- exact host `www.sco.ca.gov`;
- exact URL/path;
- one `GET` total;
- one PDF, all pages;
- no redirects;
- no retries;
- no query parameters;
- no authentication or cookies;
- maximum response body `16777216` bytes, explicitly a project safety cap;
- no SCO dataset host access;
- no `claimit.ca.gov` access;
- no source-data access.

The proposal itself keeps `authority_network_access_authorized_by_this_proposal=false`.

### 3. Archival provenance contract is adequate for proposal stage

The proposal requires:

- immutable raw authority document persistence if later approved;
- SHA-256 content addressing;
- deterministic archive and metadata paths;
- retrieval timestamp, requested/final URL, HTTP status, content type, byte count, hash, method and redirect count;
- PDF magic verification;
- no semantic extraction during retrieval;
- no runtime contract modification during retrieval;
- a separate post-archive human provenance review before semantic use.

The authority archive itself is explicitly not treated as proof of any semantic claim.

### 4. Legal/privacy boundary remains separated from personal-data acquisition

The proposal purpose is limited to archiving an official public authority document for provenance review. It does not authorize personal-record acquisition, unclaimed-property row access, property IDs, owner/holder values, beneficiary/claimant data, form submission, UI automation, or terms/privacy scope expansion.

### 5. Consumed approvals remain consumed

The previous execution and transient-row privacy approvals remain marked consumed and non-reusable. They are explicitly not used by authority acquisition.

### 6. Runtime semantics remain frozen

The proposal forbids runner, parser, regex, trimming, uppercasing, normalization, logging, privacy, source approval, registry activation and production-classification changes. It also forbids a third semantic execution.

### 7. Downstream gates remain closed

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain `0`; semantic compatibility remains unresolved; production classification, identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

## Execution-stage tightening required

This PASS approves the proposal design only. Any later one-shot authority archival execution/authorization artifact must remain at least as restrictive and should explicitly fail closed unless all execution-time checks required by the proposal are satisfied, including exact URL/host, no redirect, byte cap and PDF validation. It must not silently widen request count, retry behavior, document scope, authority set, semantic scope, or privacy scope.

## Explicit Non-Authorization

This review does not create an authority-execution approval token and does not authorize:

- retrieving or downloading the authority document;
- creating a network workflow;
- following redirects or links;
- accessing SCO data or `claimit.ca.gov`;
- reusing consumed semantic execution/privacy approvals;
- modifying parser/regex/runtime semantics;
- performing another real semantic execution;
- activating source, registry, classification, identity, genealogy, matching, outreach, or claims.

## Next Gate

The next bounded action, if the owner wishes to continue, is to prepare a **separate one-shot authority archival execution/authorization artifact**. That artifact must itself pass an explicit human authorization gate before any network request is performed.
