# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The live-source mismatch was classified by the prior bounded diagnostic as `ASCII_STRUCTURAL_MISMATCH`; human evidence review passed; the source-format diagnostic proposal and its human review are complete; and the separate source-format diagnostic execution/authorization artifact has now been prepared offline and CI-verified.

Semantic compatibility remains unresolved. No source-format execution, full-row privacy exposure or runtime remediation is authorized.

## Source-Format Execution Authorization Package

Branch:
`m3-ca-sco-property-type-source-format-diagnostic-execution-authorization`

Functional package checkpoint:
`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Package CI:
`35082891083` — SUCCESS

Artifact:
`sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic_execution_authorization.v1.json`

Schema:
`schemas/common/property_type_source_format_diagnostic_execution_authorization.schema.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION.md`

Contract test:
`tests/contract/test_ca_sco_property_type_source_format_diagnostic_execution_authorization.py`

Artifact status:
`PENDING_HUMAN_AUTHORIZATION`

Next human gate:
`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

## Mandatory Review Tightenings Implemented

The package machine-locks all five requirements from the prior human review:

1. `T-1` — first-match classifier precedence is fixed exactly as:
   - `FULL_ROW_UTF8_DECODE_FAILED`
   - `STDLIB_STRICT_CSV_PARSE_FAILED`
   - `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
   - `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
   - `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`
2. `T-2` — comparator input is the same already-assembled in-memory logical-row bytes; source re-read/additional Range requests are forbidden.
3. `T-3` — stdlib framing is pinned to `io.StringIO(decoded_row, newline="")`-equivalent semantics with the fixed `csv.reader(strict=True)` dialect; synthetic LF and CRLF multiline regression tests pass.
4. `T-4` — exactly one independent CSV record is required; zero/multiple records stop fail-closed using `INDEPENDENT_PARSER_RECORD_COUNT_UNEXPECTED`.
5. `T-5` — non-classification fail-closed reasons are enumerated; parser exception text and source-derived free text cannot persist.

## Fresh Approval State

Two new approval references are defined by the artifact but are **not granted**:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Both are single-use, non-reusable, and require separate approval evidence pinned to the exact reviewed authorization-package SHA before any network request.

Current state:

- execution approval granted: `false`;
- full-row transient privacy approval granted: `false`;
- approval evidence files: ABSENT;
- source-format network workflow: ABSENT.

The functional package checkpoint that future approval evidence must pin, if and only if the authorization review later passes and the owner explicitly grants the exact tokens, is:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

All historical execution/privacy/authority approvals remain `CONSUMED` and permanently non-reusable.

## Bounded Future Execution Contract — Still Not Authorized

- exact endpoint and pinned source identity only;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced target mismatch;
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
- source identity drift or target mismatch not reproduced within the bound -> STOP fail-closed.

## Full-Row Privacy Boundary — Still Not Authorized

A future comparator may transiently decode at most one real logical row and may use only the same logical-row bytes already in memory.

No full row, field value, `PROPERTY_TYPE`, bytes, hash, exact length, fragments, codepoints, transformed value, `PROPERTY_ID`, owner/holder value, row hash, row exact length, parser exception text or source-derived free text may persist or be logged.

## Safety / Governance State

- parser unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- source-format diagnostic execution authorized: `false`;
- full-row transient privacy exposure authorized: `false`;
- network workflow authorized: `false`;
- remediation authorized: `false`;
- additional authority retrieval authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Perform only:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

The review must decide `PASS`, `FAIL` or `NEEDS_REMEDIATION` on the authorization package and its privacy boundary. A PASS still does not grant either fresh approval and does not authorize network execution.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
