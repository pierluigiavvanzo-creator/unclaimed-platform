# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Review Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-source-format-diagnostic-execution-authorization-review`
- authorization package branch: `m3-ca-sco-property-type-source-format-diagnostic-execution-authorization`
- authorization functional package checkpoint: `cd76250b9527be91e7e7ac4b3aa658c864cf9172`
- authorization package CI: `35082891083` — SUCCESS
- reviewed authorization final HEAD: `e73681941ef9794d54bef78b53361ea45baccbf9`
- reviewed authorization final CI: `35083155026` — SUCCESS
- artifact: `sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic_execution_authorization.v1.json`
- schema: `schemas/common/property_type_source_format_diagnostic_execution_authorization.schema.json`
- authorization audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION.md`
- authorization review audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW.md`
- source-format network workflow: ABSENT

## Human Review Result

Gate completed:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Decision:

`PASS`

Meaning:

- the bounded authorization contract is accepted;
- T-1 through T-5 are accepted as machine-locked execution semantics;
- no network access is granted by the review;
- no real full-row exposure is granted by the review;
- no approval token is granted or consumed by the review;
- no workflow creation/execution is authorized by the review;
- no parser/regex/runtime modification or remediation is authorized.

## Fresh Approvals — Required, Still Ungranted

The reviewed artifact defines exactly two fresh approval references:

1. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
2. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Current state for both:

- `single_use: true`;
- `reusable: false`;
- `granted: false`;
- separate approval evidence required;
- both required before any network request;
- each approval evidence must pin the exact reviewed functional package SHA:
  `cd76250b9527be91e7e7ac4b3aa658c864cf9172`.

At this checkpoint:

- execution approval evidence: ABSENT;
- full-row privacy approval evidence: ABSENT;
- source-format network workflow: ABSENT.

Do not interpret generic wording such as `procedi` or `vai avanti` as either approval.

All historical approvals remain consumed and permanently non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

## Reviewed Execution Boundary — Not Yet Authorized

A later one-shot execution may be no wider than:

- exact endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- pinned expected source identity;
- first canonical ZIP member only: `From_500_To_Beyond_1_of_4.csv`;
- maximum 4 transient rows while seeking the first reproduced `ASCII_STRUCTURAL_MISMATCH`;
- maximum 1 transient full-row independent cross-check on that mismatch row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- no redirects;
- no additional ranges;
- no full-body fallback;
- no automatic widening;
- no authority endpoint or other-source access;
- source identity drift or failure to reproduce the target mismatch within bound -> STOP fail-closed.

## T-1 through T-5 — Reviewed and Accepted

### T-1 — Fixed classifier precedence

First-match order exactly:

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

### T-2 — Same logical-row bytes

The comparator must use the exact same already-assembled in-memory logical-record bytes. No re-read or additional Range request.

### T-3 — Exact stdlib framing

Pinned to Python stdlib `csv.reader(strict=True)` with the reviewed dialect and text-stream framing equivalent to `io.StringIO(decoded_row, newline="")`.

Synthetic contract regressions cover embedded LF and CRLF in quoted fields.

### T-4 — Exactly one parsed record

Exactly one CSV record is required. Zero or multiple records stop fail-closed using:

`INDEPENDENT_PARSER_RECORD_COUNT_UNEXPECTED`

### T-5 — Enumerated fail-closed reasons

Non-classification failures are limited to enumerated non-source-bearing reason codes. Parser exception text and source-derived free text are forbidden.

## Full-Row Privacy Boundary — Still Blocked

Even if later explicitly approved:

- maximum one transient full-row cross-check;
- same in-memory logical-row bytes only;
- discard immediately after classification/fail-closed;
- no full row or field value persisted/logged;
- no PROPERTY_TYPE or protected derivative persisted;
- no PROPERTY_ID or owner/holder value persisted;
- no row hash or exact row length persisted;
- no parser exception text or source-derived free text persisted.

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

Wait for explicit owner grant of **both** exact tokens:

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Only after both exact tokens are supplied may the next task persist two separate approval evidence records pinned to:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Do not create a network workflow or execute the diagnostic until both valid approval evidence records exist. Generic approval language is insufficient.