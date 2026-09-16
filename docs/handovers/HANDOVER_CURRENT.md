# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Authorization Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-source-format-diagnostic-execution-authorization`
- proposal review base HEAD: `2975eef60d9ece94a68ef2cd6f2a0707ccfa4083`
- source-format proposal package: `d8dc240bd74e271f88b2ef4583f6b79e533918b2`
- source-format proposal review decision: `PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`
- authorization functional package checkpoint: `cd76250b9527be91e7e7ac4b3aa658c864cf9172`
- authorization package CI: `35082891083` — SUCCESS
- artifact: `sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic_execution_authorization.v1.json`
- schema: `schemas/common/property_type_source_format_diagnostic_execution_authorization.schema.json`
- audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION.md`
- contract test: `tests/contract/test_ca_sco_property_type_source_format_diagnostic_execution_authorization.py`
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

The exact observed `PROPERTY_TYPE` value, bytes, hash, exact length, fragments, codepoints and transformed form were not persisted and must not be reconstructed or inferred.

## Authorization Artifact State

Status:
`PENDING_HUMAN_AUTHORIZATION`

Gate:
`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Artifact preparation was repository-only/offline. It performed no source or authority request, no real full-row access, no network workflow creation, no diagnostic execution and no parser/regex/runtime/remediation change.

## Fresh Approvals — Defined, Not Granted

The artifact defines two fresh approval references:

1. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
2. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Current state for both:

- `single_use: true`;
- `reusable: false`;
- `granted: false`;
- separate approval evidence required;
- approval evidence must pin the exact reviewed authorization-package SHA;
- both required before any network request.

At this checkpoint:

- execution approval evidence: ABSENT;
- full-row privacy approval evidence: ABSENT;
- source-format network workflow: ABSENT.

If the authorization review later passes and the owner explicitly grants the exact tokens, approval evidence must pin:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Do not interpret generic wording such as `procedi` or `vai avanti` as either token.

All historical approvals remain consumed and permanently non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

## Execution Boundary — Still Not Authorized

Any later one-shot execution may be no wider than:

- exact endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- pinned expected source identity;
- first canonical ZIP member only: `From_500_To_Beyond_1_of_4.csv`;
- maximum 4 transient rows while seeking the first reproduced `ASCII_STRUCTURAL_MISMATCH`;
- maximum 1 full-row independent cross-check on that mismatch row;
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
- authority endpoint access forbidden;
- other source/endpoint access forbidden;
- source identity drift -> STOP fail-closed;
- target mismatch not reproduced within bound -> STOP fail-closed.

## T-1 — Fixed Classifier Precedence

First-match order is exactly:

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

Reordering is forbidden and no class automatically authorizes remediation.

## T-2 — Same Logical-Row Bytes

The comparator must consume the exact same already-assembled in-memory logical-record bytes for the first reproduced mismatch.

Forbidden:

- source re-read;
- additional Range request;
- alternate network retrieval for comparator input.

## T-3 — Exact Stdlib Framing

The artifact pins:

- Python stdlib `csv.reader`;
- `strict=True`;
- delimiter `,`;
- quotechar `"`;
- `doublequote=True`;
- `escapechar=None`;
- `skipinitialspace=False`;
- strict UTF-8 decode;
- text-stream construction equivalent to `io.StringIO(decoded_row, newline="")`.

Synthetic contract regressions verify one-record behavior with embedded LF and CRLF inside quoted fields.

## T-4 — Exactly One Parsed Record

The independent comparator must produce exactly one CSV record.

Zero or multiple records stop fail-closed using:

`INDEPENDENT_PARSER_RECORD_COUNT_UNEXPECTED`

No parser exception text or source content may be persisted.

## T-5 — Enumerated Fail-Closed Reasons

The artifact enumerates non-classification fail-closed reason codes, including:

- approval evidence invalid/incomplete;
- source identity drift;
- bounded HEAD/Range failures;
- byte/logical-record budget failures;
- canonical-member/projection failures;
- target mismatch not reproduced within bound;
- independent-parser record-count/framing invariant failures;
- classifier/privacy/persistence/network invariant violations.

Free-text source-derived error output is forbidden.

## Full-Row Privacy Boundary — Still Not Authorized

The future strict stdlib comparator may transiently decode all fields in at most one real logical row. This remains a new privacy expansion and requires the distinct full-row privacy approval.

Even if later authorized:

- same in-memory logical-row bytes only;
- discard immediately after classification/fail-closed;
- persist no full row or row field value;
- persist no `PROPERTY_TYPE`, bytes, hash, exact length, fragments, codepoints or transformed value;
- persist no `PROPERTY_ID` or owner/holder value;
- persist no row hash or exact row length;
- log no source value;
- persist no parser exception text;
- persist no source-derived free text.

## Output Contract

A later separately authorized execution may persist only:

- `diagnostic_result_status`;
- `source_format_diagnostic_class`;
- `fail_closed_reason_code`;
- source identity boolean;
- bounded request/byte/row counters;
- `full_row_crosscheck_rows_examined`;
- safety flags.

Statuses are limited to:

- `SOURCE_FORMAT_CLASSIFIED`;
- `STOPPED_FAIL_CLOSED`.

## Governance State

Unchanged and fail-closed:

- parser unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
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

Perform exclusively:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Review artifact, schema, audit and contract test against the source-format proposal review and its T-1 through T-5 requirements.

During review do **not**:

- access `claimit.ca.gov` or authority endpoints;
- inspect a real full row;
- create or execute a network workflow;
- grant or consume either fresh approval;
- reconstruct or infer the source `PROPERTY_TYPE`;
- change parser, regex, trimming, casing, normalization, logging or persistence behavior;
- apply remediation;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.

A review PASS approves only the authorization contract. It does not itself grant execution or full-row privacy approval.
