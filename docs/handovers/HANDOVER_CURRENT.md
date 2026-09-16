# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Review Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-source-format-diagnostic-proposal-review`
- proposal branch final HEAD reviewed: `5e0aa6fa8bc9516c2cd8447e26e3b76b7485c4e9`
- proposal final CI: `35060418377` — SUCCESS
- proposal package checkpoint: `d8dc240bd74e271f88b2ef4583f6b79e533918b2`
- proposal package CI: `35060253297` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic.v1.json`
- proposal schema: `schemas/common/property_type_source_format_diagnostic_proposal.schema.json`
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL.md`
- proposal review audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW.md`
- source-format network workflow: ABSENT

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

Prior human evidence review decision:

`PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`

## Source-Format Proposal Human Review

Gate completed:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW`

Decision:

`PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`

Meaning:

- the proposal design is accepted only as the basis for preparing a separate execution/authorization artifact;
- no network access is authorized;
- no real full-row exposure is authorized;
- no workflow creation/execution is authorized;
- no parser/regex/runtime modification or remediation is authorized;
- no execution/privacy token is granted or consumed by this review.

## Reviewed Future Source Boundary — Still Not Authorized

A later execution artifact may be no wider than:

- exact current `claimit.ca.gov` endpoint and pinned source identity;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced target mismatch;
- maximum 1 full-row independent cross-check, only on that mismatch row;
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
- source identity drift or target mismatch not reproduced within bound -> fail closed.

## Full-Row Privacy Boundary — Accepted as Design Only

A future strict standard-library CSV cross-check would transiently decode all fields in one real logical row and may expose personal data in memory.

This privacy expansion remains:

- full-row transient rows max: `1`;
- authorized now: `false`;
- persistence/logging of row or fields: forbidden;
- fresh execution approval required before network: `true`;
- separate fresh full-row transient privacy approval required before network: `true`;
- approvals must be single-use/non-reusable and pinned to the exact reviewed execution artifact.

No approval token was defined or granted by this review.

## Mandatory Tightenings for Next Artifact

The future execution/authorization artifact must incorporate all of the following without widening scope:

### T-1 — Fixed classifier precedence

First-match order must be exactly:

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

### T-2 — Same logical-row bytes

The comparator must consume the exact same transient logical-record bytes already assembled in memory for the first reproduced `ASCII_STRUCTURAL_MISMATCH`. No source re-read or extra Range request is allowed.

### T-3 — Exact newline/multiline framing

The artifact must pin deterministic standard-library framing for embedded newline/CRLF handling. Use an explicit construction equivalent to `io.StringIO(decoded_row, newline="")` feeding `csv.reader` with the pinned dialect, or an equivalently explicit standard-library construction proven by synthetic regression tests.

### T-4 — Exactly one parsed record

The independent comparator must produce exactly one CSV record from that one transient logical row. Zero or multiple records must STOP fail-closed under an enumerated non-source-bearing reason code.

### T-5 — Enumerated fail-closed reasons

All non-classification fail-closed reason codes must be enumerated before execution, including source identity drift, target mismatch not reproduced within bound, and independent-parser framing/record-count failure. Parser exception text and source-derived free text remain forbidden.

## Independent Parser Role

The comparator remains diagnostic-only:

- Python standard-library `csv.reader`;
- `strict=True`;
- comma delimiter;
- quote character `"`;
- `doublequote=True`;
- no escape character;
- `skipinitialspace=False`;
- strict UTF-8 decode;
- canonical 25 columns;
- PROPERTY_TYPE at zero-based index `1`;
- current custom projector unchanged;
- current regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no normalization/value substitution/remediation.

## Approval State

All prior approvals remain consumed and permanently non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Do not infer or reuse any of them.

## Governance State

Unchanged and fail-closed:

- parser unchanged;
- regex unchanged;
- trimming/casing/normalization unchanged;
- source-format execution authorized: `false`;
- full-row transient privacy exposure authorized: `false`;
- network workflow authorized: `false`;
- remediation authorized: `false`;
- additional authority retrieval authorized: `false`;
- source policy `PROPOSED`;
- registry disabled / not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission BLOCKED.

## SINGLE NEXT ACTION

Prepare exclusively, offline, a separate:

`PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_ARTIFACT`

That artifact must incorporate T-1 through T-5 and must not:

- access `claimit.ca.gov` or authority endpoints during preparation;
- inspect a real full row;
- create or execute a network workflow;
- grant or consume execution/full-row privacy approvals;
- reconstruct or infer the PROPERTY_TYPE value;
- change parser, regex, trimming, casing, normalization, logging or persistence behavior;
- apply remediation;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.

If the artifact defines future execution/privacy approval tokens, they must remain explicitly ungranted until a later human authorization gate.

Stop after artifact preparation at its own human review gate; do not silently execute it.