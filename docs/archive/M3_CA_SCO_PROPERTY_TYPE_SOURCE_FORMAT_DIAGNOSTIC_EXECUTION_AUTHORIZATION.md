# M3 California SCO — PROPERTY_TYPE Source-Format Diagnostic Execution Authorization

Date: 2026-09-16

Status: **PENDING HUMAN AUTHORIZATION — NO EXECUTION AUTHORIZED**

## Purpose

Prepare the smallest deterministic execution/authorization contract for a future one-shot source-format diagnostic after the human review decision:

`PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`

This task is artifact preparation only. It performs no source request, authority request, real full-row inspection, workflow creation or diagnostic execution.

## Verified base

- review branch: `m3-ca-sco-property-type-source-format-diagnostic-proposal-review`
- review HEAD: `2975eef60d9ece94a68ef2cd6f2a0707ccfa4083`
- proposal package: `d8dc240bd74e271f88b2ef4583f6b79e533918b2`
- reviewed proposal final HEAD: `5e0aa6fa8bc9516c2cd8447e26e3b76b7485c4e9`
- proposal review audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW.md`
- proposal review decision: `PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`

The exact observed `PROPERTY_TYPE` value and all protected derivatives remain unretained and must not be reconstructed or inferred.

## Artifact state

Machine artifact:

`sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic_execution_authorization.v1.json`

Schema:

`schemas/common/property_type_source_format_diagnostic_execution_authorization.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_source_format_diagnostic_execution_authorization.py`

Artifact status:

`PENDING_HUMAN_AUTHORIZATION`

Human gate:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

No approval is granted by artifact preparation.

## Fresh approvals defined but not granted

The artifact defines two new, distinct approvals:

1. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
2. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Both are:

- single-use;
- non-reusable;
- `granted: false` at this checkpoint;
- required before any future network request;
- required to pin the exact reviewed authorization-package SHA in separate approval evidence.

No approval evidence file exists at package-preparation time and no approval may be inferred from generic wording such as “procedi” or “vai avanti”.

All historical execution/privacy/authority approvals remain consumed and permanently non-reusable.

## Execution boundary — not yet authorized

A future execution may be no wider than:

- endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- expected content length: `162416884`;
- expected ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type: `application/zip`;
- byte ranges required;
- first canonical member only: `From_500_To_Beyond_1_of_4.csv`;
- local header offset: `0`;
- maximum transient data rows while seeking the target mismatch: `4`;
- maximum full-row cross-check rows: `1`;
- maximum HEAD requests: `1`;
- maximum Range GET requests: `1`;
- maximum HTTP requests total: `2`;
- maximum source response-body bytes: `131072`;
- maximum uncompressed transient bytes: `262144`;
- maximum logical-record bytes: `32768`;
- retries: `0`;
- redirects: forbidden;
- additional ranges: forbidden;
- full-body fallback: forbidden;
- automatic widening: forbidden;
- authority-network access: forbidden;
- any other source/endpoint: forbidden.

Source identity drift or failure to reproduce the target `ASCII_STRUCTURAL_MISMATCH` within the bound stops fail-closed.

## T-1 — fixed classifier precedence

The first-match precedence is machine-locked to exactly:

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

Reordering is forbidden. No class automatically authorizes remediation.

## T-2 — same logical-row bytes, no re-read

The independent comparator must consume exactly the same transient logical-record bytes already assembled in memory for the first row that reproduces `ASCII_STRUCTURAL_MISMATCH`.

It may not:

- issue an additional source request;
- issue an additional Range request;
- re-read the source by another mechanism;
- reconstruct comparator input from persisted source data.

## T-3 — exact newline / multiline framing

After strict UTF-8 decoding, the independent comparator is pinned to a standard-library text stream equivalent to:

`io.StringIO(decoded_row, newline="")`

That stream feeds `csv.reader` with:

- `strict=True`;
- delimiter `,`;
- quote character `"`;
- `doublequote=True`;
- `escapechar=None`;
- `skipinitialspace=False`.

Synthetic regression tests cover both embedded LF and embedded CRLF inside quoted fields and require exactly one record.

## T-4 — exactly one independent CSV record

The comparator input is exactly one preassembled logical record and must yield exactly one CSV record.

Zero records or more than one record stop fail-closed under:

`INDEPENDENT_PARSER_RECORD_COUNT_UNEXPECTED`

No source content, parser exception text or source-derived free text may be persisted in that failure path.

## T-5 — enumerated fail-closed reasons

The authorization artifact enumerates all permitted non-classification fail-closed reason codes. They include, at minimum:

- `APPROVAL_EVIDENCE_INVALID_OR_INCOMPLETE`;
- `SOURCE_IDENTITY_DRIFT`;
- bounded HEAD/Range failures;
- byte/record budget violations;
- canonical-member/projection failures;
- `TARGET_ASCII_STRUCTURAL_MISMATCH_NOT_REPRODUCED_WITHIN_BOUND`;
- `INDEPENDENT_PARSER_RECORD_COUNT_UNEXPECTED`;
- `INDEPENDENT_PARSER_FRAMING_INVARIANT_VIOLATION`;
- classifier/privacy/persistence/network invariant violations.

Free-text source-derived error persistence remains forbidden.

## Full-row transient privacy boundary

The future independent parse would transiently decode all fields in one real logical row and may expose personal data in memory. This remains an explicit privacy expansion.

The authorization artifact does **not** grant that exposure. The future privacy approval is separate from the future execution approval.

Even if later authorized:

- full-row cross-check maximum: `1` row;
- same in-memory logical-row bytes only;
- discard immediately after classification/fail-closed;
- no full row persisted;
- no field value persisted;
- no `PROPERTY_TYPE` value/bytes/hash/exact length/fragments/codepoints persisted;
- no transformed value persisted;
- no `PROPERTY_ID` or owner/holder value persisted;
- no row hash or exact row length persisted;
- no source value logged;
- no parser exception text persisted;
- no source-derived free text persisted.

## Output contract

Only the following durable fields may exist after a future separately authorized execution:

- `diagnostic_result_status`;
- `source_format_diagnostic_class`;
- `fail_closed_reason_code`;
- `source_identity_verified`;
- bounded request/byte/row counters;
- `full_row_crosscheck_rows_examined`;
- safety flags.

Result status is limited to:

- `SOURCE_FORMAT_CLASSIFIED`;
- `STOPPED_FAIL_CLOSED`.

A classified result has no fail-closed reason. A fail-closed result has no diagnostic class.

## What this artifact preparation does not authorize

It does not authorize:

- network access;
- real full-row exposure;
- network workflow creation;
- execution;
- parser replacement/change;
- regex change/relaxation;
- trim/case/Unicode normalization;
- logging or persistence expansion;
- remediation;
- authority retrieval;
- source approval;
- registry activation;
- production classification;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Governance state

Unchanged and fail-closed:

- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- authority provenance: resolved within recorded scope;
- semantic compatibility: unresolved;
- production classification: inactive;
- downstream gates: BLOCKED.

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

A human review may return `PASS`, `FAIL` or `NEEDS_REMEDIATION`. A PASS accepts only the authorization design. It does not grant either fresh approval and does not permit network execution until both exact approval tokens are later explicitly granted and pinned to the reviewed package SHA.
