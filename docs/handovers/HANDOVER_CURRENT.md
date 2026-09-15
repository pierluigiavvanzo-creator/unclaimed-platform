# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Diagnostic Proposal Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal`
- base review HEAD: `961d6a908dd9656f5ce19823be074011010833bf`
- proposal package checkpoint SHA: `020044d3013449fabe566c5164b8f99f9d8cc9ab`
- proposal package CI: `35015429439` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_diagnostic_remediation_evidence.v1.json`
- schema: `schemas/common/property_type_diagnostic_remediation_evidence_proposal.schema.json`
- audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL.md`
- contract test: `tests/contract/test_ca_sco_property_type_diagnostic_remediation_evidence_proposal.py`

## Verified Baseline

- M0: VERIFIED
- M1: VERIFIED
- M2: VERIFIED
- M3 authority target provenance: RESOLVED WITH BOUNDED AA99 INTERPRETATION
- M3 live PROPERTY_TYPE semantic compatibility: UNRESOLVED
- second bounded semantic run: `34995672539` -> `STOPPED_FAIL_CLOSED`
- second stop: `PROPERTY_TYPE_FORMAT_UNEXPECTED`
- current runner/schema: v1.1 separates encoding failure from decoded format mismatch
- previous semantic execution/privacy approvals: CONSUMED + NON-REUSABLE
- authority archival approval: CONSUMED + NON-REUSABLE
- source policy: `PROPOSED`
- registry: disabled / not approved
- approved real sources: `0`
- production classification: inactive
- identity/genealogy/beneficiary matching/outreach/claim submission: BLOCKED

## What Is Already Proven

The second real run used the remediated v1.1 runner. Under that runner:

- invalid UTF-8 projection -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded, non-empty shape mismatch -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Because run `34995672539` stopped with `PROPERTY_TYPE_FORMAT_UNEXPECTED`, the observed live mismatch is narrowed to a decoded, non-empty projected PROPERTY_TYPE that failed the unchanged regex:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The exact offending value, bytes, hash, exact length, fragments and codepoints were intentionally not retained and must not be reconstructed or inferred.

The archived authority review separately established:

- `ZZZZ` is supported;
- `IN01` through `IN08` and `IN99` are supported;
- authority-enumerated non-`ZZZZ` property type codes use the observed two-uppercase-letter plus two-digit shape;
- arbitrary `AA99` membership is not established;
- the current regex is not contradicted by the authority;
- trimming, uppercasing, normalization, parser change and regex relaxation are not authorized.

## Prepared Diagnostic / Remediation Evidence Proposal

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

The proposal asks only whether a future **separately authorized** bounded diagnostic can classify the first reproduced format mismatch into one of five non-value-bearing categories:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

No class is an accepted source value and no class automatically authorizes remediation.

### Future diagnostic scope if separately approved

The proposal defines, but does not authorize:

- exact endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- pinned source content length / ETag / media type / byte-range support;
- first canonical member only: `From_500_To_Beyond_1_of_4.csv`;
- maximum 4 transient data rows;
- stop at first reproduced format mismatch;
- maximum 1 HEAD;
- maximum 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes total;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- redirects forbidden;
- additional range forbidden;
- full-body fallback forbidden;
- automatic widening forbidden;
- source identity drift -> fail closed;
- mismatch not reproduced inside boundary -> fail closed.

### Diagnostic derivation boundary

If separately authorized later, only fixed in-memory predicates may be used to derive the coarse class:

- surrounding ASCII space/tab removal match predicate;
- ASCII-only uppercase match predicate;
- combined surrounding ASCII space/tab removal + ASCII uppercase match predicate;
- non-ASCII/disallowed-control presence predicate.

Not included:

- Unicode normalization probe;
- real-row full `csv.reader` crosscheck;
- parser change;
- regex change/relaxation;
- treating a diagnostic transform as a runtime transform or accepted source value.

### Persistence / logging boundary

Even a future separately approved diagnostic must not persist or log:

- exact PROPERTY_TYPE;
- PROPERTY_TYPE bytes;
- hash;
- exact length;
- fragments/prefixes/suffixes;
- codepoints;
- transformed value;
- full row;
- raw response body;
- PROPERTY_ID;
- owner/holder values;
- source-derived free text;
- per-row values or distinct code lists.

Allowed future evidence is limited to a fixed categorical diagnostic result, source-identity verification state, bounded request/body/row counters and safety flags.

## Current Authorization Boundary

The user authorized **proposal preparation only**.

Current machine state:

- proposal preparation authorized: `true`
- diagnostic execution authorized: `false`
- transient-row privacy exposure authorized: `false`
- network workflow authorized: `false`
- runtime change authorized: `false`
- remediation authorized: `false`
- third semantic execution authorized: `false`
- approval token defined by proposal: `false`

Proposal preparation performed no source network access, no diagnostic execution and no runtime/parser/regex/normalization/logging/persistence change.

## Consumed Approvals — Do Not Reuse

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

All remain consumed and non-reusable.

## Current Safety Boundary

Do not:

- reuse any consumed approval;
- access SCO or `claimit.ca.gov` during proposal review;
- reconstruct or infer the unretained offending PROPERTY_TYPE;
- persist/hash/measure exact source value content;
- create a diagnostic network workflow before a separate explicit authorization artifact and fresh approvals;
- change parser, regex, trimming, casing or normalization;
- apply remediation from any proposed diagnostic class;
- perform a real-row full-parser crosscheck under this proposal;
- run another real PROPERTY_TYPE semantic execution;
- activate source policy, registry or production classification;
- perform identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

Review the proposal, schema, audit and contract test against the verified base evidence and decide `PASS`, `FAIL`, or `NEEDS_REMEDIATION`.

During this review do **not** access the source, retrieve the authority again, reconstruct the offending value, create a network workflow, modify runtime semantics or perform a diagnostic execution.

If the proposal review is `PASS` and the owner later wants the real bounded diagnostic, the next step is to prepare a **separate explicit diagnostic execution/authorization artifact**. That later artifact must define fresh execution and transient-row privacy approvals before any source request. This proposal intentionally defines no canonical approval token.
