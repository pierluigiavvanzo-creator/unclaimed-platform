# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Diagnostic Authorization Review Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-diagnostic-execution-authorization-review`
- reviewed authorization branch: `m3-ca-sco-property-type-diagnostic-execution-authorization`
- authorization package checkpoint SHA: `daeaa7bfb7f7d73a61f011d394cc88393625866c`
- authorization package CI: `35017854034` — SUCCESS
- final authorization branch HEAD reviewed: `de73b2d4d0fdcc236cbcfa3a0ad253c617919b28`
- final authorization branch CI: `35018090207` — SUCCESS
- review gate: `HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`
- review decision: `PASS`
- review audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW.md`

## Verified Baseline

- M0: VERIFIED
- M1: VERIFIED
- M2: VERIFIED
- M3 authority target provenance: RESOLVED WITH BOUNDED AA99 INTERPRETATION
- M3 live PROPERTY_TYPE semantic compatibility: UNRESOLVED
- second bounded semantic run: `34995672539` -> `STOPPED_FAIL_CLOSED`
- second stop: `PROPERTY_TYPE_FORMAT_UNEXPECTED`
- current regex: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`
- diagnostic/remediation proposal review: `PASS`
- diagnostic execution/authorization review: `PASS`
- prior semantic execution/privacy approvals: CONSUMED + NON-REUSABLE
- authority archival approval: CONSUMED + NON-REUSABLE
- source policy: `PROPOSED`
- registry: disabled / not approved
- approved real sources: `0`
- production classification: inactive
- identity/genealogy/beneficiary matching/outreach/claim submission: BLOCKED

## Review Result

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW` completed with:

`PASS`

The PASS accepts the bounded authorization contract only. It does **not** grant either fresh approval and does not authorize a source request by itself.

The reviewed package changes only the expected four package files relative to proposal-review HEAD: machine artifact, schema, audit and contract test.

## Fresh Approvals — Defined but NOT Granted

Execution approval:

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`

Transient-row privacy approval:

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Rules for both:

- owner must grant each explicitly;
- fresh;
- single-use;
- non-reusable;
- durable approval evidence must pin package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c`;
- both are required before any `claimit.ca.gov` request;
- neither is granted by review PASS, `procedi`, or other generic wording.

Required evidence paths after explicit approval:

- `sources/evidence/ca_sco_property_type_diagnostic_execution_approval.v1.json`
- `sources/evidence/ca_sco_property_type_diagnostic_transient_row_privacy_approval.v1.json`

No approval evidence file was created by the review.

## Consumed Approvals — Never Reuse

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

## Exact Future Execution Boundary — Still Blocked Until Both Fresh Approvals

Only after both approval evidences are valid:

- endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- pinned source identity: content length `162416884`, ETag `"b25b315b6cd8007624387c3a00d4b1fe"`, media type `application/zip`, byte-range support `bytes`;
- canonical member: `From_500_To_Beyond_1_of_4.csv`;
- members maximum: `1`;
- transient data rows maximum: `4`;
- stop at first reproduced format mismatch;
- HEAD requests maximum: `1`;
- Range GET maximum: `1`;
- HTTP requests maximum total: `2`;
- source response-body bytes maximum total: `131072`;
- uncompressed transient bytes maximum: `262144`;
- logical record bytes maximum: `32768`;
- retries: `0`;
- redirects: forbidden;
- additional range: forbidden;
- full-body fallback: forbidden;
- automatic widening: forbidden;
- authority access: forbidden;
- any other source/endpoint: forbidden;
- source identity drift -> `STOP_FAIL_CLOSED`;
- mismatch not reproduced within boundary -> `STOP_FAIL_CLOSED`.

## Deterministic Classifier Contract

Fixed precedence:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

Surrounding diagnostic whitespace is exactly `U+0020` SPACE and `U+0009` TAB.

Case probing is ASCII-only: `a-z` -> `A-Z`; every other code point is unchanged. Locale-sensitive casing and Unicode normalization are forbidden.

Non-ASCII means any code point greater than `U+007F`. Disallowed ASCII control content is exactly `U+0000-U+001F` plus `U+007F`, subject to the fixed precedence for boundary TAB.

The current regex remains unchanged and diagnostic transforms cannot be accepted as runtime values.

## Output / Privacy Contract

Future persisted evidence may contain only:

- `diagnostic_result_status`;
- `diagnostic_class` or null;
- enumerated `fail_closed_reason_code` or null;
- source identity verification state;
- bounded request/body/row counters;
- safety flags.

Forbidden from persistence/logging:

- exact PROPERTY_TYPE;
- bytes;
- hash;
- exact length;
- fragments;
- codepoints;
- transformed value;
- full row;
- raw response body;
- PROPERTY_ID;
- owner/holder values;
- distinct source code lists;
- source-derived free text.

For `STOPPED_FAIL_CLOSED`, `diagnostic_class` is null and an enumerated fail-closed reason code is mandatory.

No diagnostic class authorizes remediation.

## Current Authorization State

- authorization review: `PASS`
- execution approval granted: `false`
- transient-row privacy approval granted: `false`
- diagnostic execution authorized: `false`
- transient-row privacy exposure authorized: `false`
- network workflow creation authorized: `false`
- network execution authorized: `false`
- runtime change authorized: `false`
- remediation authorized: `false`

The review performed no source network access, no transient-row inspection and no runtime change.

## SINGLE NEXT ACTION

Obtain explicit owner authorization for **both** exact approval references:

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Do **not** infer either approval from generic wording.

After the owner explicitly grants both, persist both approval evidences pinned to package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c` before creating or executing any network workflow.

Only then may the project enter:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

After any later diagnostic result, stop at:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`
