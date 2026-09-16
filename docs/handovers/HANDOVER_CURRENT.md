# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Proposal Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-source-format-diagnostic-proposal`
- diagnostic evidence review base HEAD: `9195d27e17b89703f7179a9db2ba5dccad43a75e`
- diagnostic evidence review CI: `35058889923` — SUCCESS
- source-format proposal package checkpoint: `d8dc240bd74e271f88b2ef4583f6b79e533918b2`
- source-format proposal package CI: `35060253297` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic.v1.json`
- schema: `schemas/common/property_type_source_format_diagnostic_proposal.schema.json`
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL.md`
- contract test: `tests/contract/test_ca_sco_property_type_source_format_diagnostic_proposal.py`
- network workflow for this proposal: ABSENT

## Prior Diagnostic Evidence

One-shot diagnostic run:
`35019840276` — SUCCESS

Persisted result:

- `diagnostic_result_status`: `DIAGNOSTIC_CLASSIFIED`
- `diagnostic_class`: `ASCII_STRUCTURAL_MISMATCH`
- source identity verified: `true`
- 1 HEAD + 1 Range GET
- 2 HTTP requests total
- 131072 source response-body bytes
- 1 transient data row examined

The exact observed PROPERTY_TYPE value, bytes, hash, exact length, fragments, codepoints and transformed form were not persisted and must not be reconstructed or inferred.

Human evidence review decision:

`PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`

## Proposal Status

`PROPOSAL_ONLY_NOT_AUTHORIZED`

Preparation was repository-only/offline. No source request, authority request, real full-row access, diagnostic execution, workflow creation, runner/parser/regex modification, normalization change, logging expansion, persistence expansion or remediation occurred.

## Proposed Future Source Boundary — Not Authorized

If a later execution artifact is separately reviewed and approved, it may be no wider than:

- exact current `claimit.ca.gov` endpoint and pinned source identity;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced target mismatch;
- maximum 1 full-row independent cross-check, only on that first mismatch row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- redirects forbidden;
- additional ranges forbidden;
- full-body fallback forbidden;
- automatic widening forbidden;
- source identity drift or target mismatch not reproduced within the bound -> fail closed.

The proposal itself grants no network permission.

## Independent Parser Design

A future comparator is pinned to:

- Python standard-library `csv.reader`;
- `strict=True`;
- delimiter `,`;
- quote character `"`;
- `doublequote=True`;
- no escape character;
- `skipinitialspace=False`;
- strict UTF-8 row decode;
- exactly 25 expected columns;
- PROPERTY_TYPE at zero-based index `1`.

The existing narrow projector stays unchanged. The current regex stays unchanged:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The independent parser is diagnostic-only and cannot replace, normalize or accept the source value.

## Explicit Full-Row Privacy Expansion

A real full-row `csv.reader` cross-check would transiently decode all fields in one row and may therefore expose personal data in memory. This is explicitly classified as a new privacy expansion.

Current state:

- full-row exposure authorized: `false`;
- source-format execution authorized: `false`;
- network workflow authorized: `false`;
- approval token defined by this proposal: `false`.

A future execution requires a new reviewed execution/authorization artifact plus:

1. fresh single-use execution approval;
2. separate fresh single-use full-row transient privacy approval;
3. both pinned to the exact reviewed execution artifact before any network request.

Even then, only one mismatch row may undergo the full-row comparator, and no row/field/source value or protected derivative may persist or be logged.

## Proposed Future Categorical Outcomes

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

These outcomes are non-value-bearing. None authorizes remediation automatically.

## Approval State

All prior approvals remain consumed and non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Do not infer or invent replacement approval tokens during proposal review.

## Governance State

Unchanged and fail-closed:

- parser unchanged;
- regex unchanged;
- trimming/casing/normalization unchanged;
- remediation authorized: `false`;
- additional authority retrieval authorized: `false`;
- source policy `PROPOSED`;
- registry disabled / not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission BLOCKED.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW`

Review the design and especially the explicit one-row full-row transient privacy expansion.

During review do **not**:

- access `claimit.ca.gov` or authority endpoints;
- inspect a real full row;
- reconstruct or infer the PROPERTY_TYPE value;
- create a network workflow;
- define or grant execution/privacy approval tokens;
- change parser, regex, trimming, casing, normalization, logging or persistence behavior;
- apply remediation;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.

A review PASS approves only the proposal design. It does not authorize execution or privacy exposure.
