# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Diagnostic Execution Authorization Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-diagnostic-execution-authorization`
- base proposal-review HEAD: `06896084475f0f899fc3e002344e22fc49ffa54d`
- reviewed diagnostic proposal package: `020044d3013449fabe566c5164b8f99f9d8cc9ab`
- reviewed diagnostic proposal HEAD: `847cdf5daaa1834c3ce11fc3d6f29e2bbc36b4b4`
- diagnostic authorization package checkpoint SHA: `daeaa7bfb7f7d73a61f011d394cc88393625866c`
- diagnostic authorization package CI: `35017854034` — SUCCESS
- artifact: `sources/proposals/ca_sco_segment_500_plus.property_type_diagnostic_execution_authorization.v1.json`
- schema: `schemas/common/property_type_diagnostic_execution_authorization.schema.json`
- audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION.md`
- contract test: `tests/contract/test_ca_sco_property_type_diagnostic_execution_authorization.py`

## Verified Baseline

- M0: VERIFIED
- M1: VERIFIED
- M2: VERIFIED
- M3 authority target provenance: RESOLVED WITH BOUNDED AA99 INTERPRETATION
- M3 live PROPERTY_TYPE semantic compatibility: UNRESOLVED
- second bounded semantic run: `34995672539` -> `STOPPED_FAIL_CLOSED`
- second stop: `PROPERTY_TYPE_FORMAT_UNEXPECTED`
- current regex: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`
- diagnostic/remediation evidence proposal review: `PASS`
- prior semantic execution/privacy approvals: CONSUMED + NON-REUSABLE
- authority archival approval: CONSUMED + NON-REUSABLE
- source policy: `PROPOSED`
- registry: disabled / not approved
- approved real sources: `0`
- production classification: inactive
- identity/genealogy/beneficiary matching/outreach/claim submission: BLOCKED

## Authorization Artifact State

Artifact status:

`PENDING_HUMAN_AUTHORIZATION`

Current gate:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Preparation performed:

- no `claimit.ca.gov` request;
- no authority request;
- no transient real-row inspection;
- no diagnostic execution;
- no network workflow creation;
- no runner/parser/regex/normalization/logging/persistence modification.

## Fresh Approvals — Defined but Not Granted

Execution approval:

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`

Transient-row privacy approval:

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Rules for both:

- fresh;
- single-use;
- non-reusable;
- approval evidence must pin authorization package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c`;
- both are required before any source network request;
- neither is currently granted.

Intended evidence paths after explicit owner approval:

- `sources/evidence/ca_sco_property_type_diagnostic_execution_approval.v1.json`
- `sources/evidence/ca_sco_property_type_diagnostic_transient_row_privacy_approval.v1.json`

Do not infer either approval from a review `PASS` or from generic wording.

## Consumed Approvals — Never Reuse

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

## Exact Future Execution Boundary — Not Authorized Yet

Only after both fresh approvals are valid:

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

Case probing is ASCII-only: `U+0061-U+007A` maps to `U+0041-U+005A`; every other code point is unchanged. Locale-sensitive casing and Unicode normalization are forbidden.

Non-ASCII means any code point greater than `U+007F`.

The disallowed ASCII control set is exactly all code points `U+0000-U+001F` plus `U+007F`. Precedence means a boundary TAB that alone resolves the mismatch is classified as whitespace before the control-content predicate.

Synthetic/test-only vectors cover all five classes and precedence/boundary behavior. They are not evidence about any real source value.

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
- distinct code lists;
- source-derived free text.

For `STOPPED_FAIL_CLOSED`, `diagnostic_class` is null and an enumerated fail-closed reason code is mandatory.

No diagnostic class authorizes remediation.

## Current Authorization Boundary

- diagnostic execution authorized: `false`
- transient-row privacy exposure authorized: `false`
- network workflow creation authorized: `false`
- network execution authorized: `false`
- runtime change authorized: `false`
- remediation authorized: `false`
- third real execution authorized: `false`

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Review the verified authorization package and decide `PASS`, `FAIL`, or `NEEDS_REMEDIATION`.

During this review do **not**:

- access `claimit.ca.gov`;
- create or execute a diagnostic network workflow;
- inspect real source rows;
- grant either fresh approval implicitly;
- reconstruct the historical unretained PROPERTY_TYPE value;
- change parser, regex, trimming, casing or normalization;
- apply remediation.

If review is `PASS`, stop again for explicit owner authorization. Both fresh approval evidences must then be separately granted and pin package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c` before entering `ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`.

After any later diagnostic result, stop at `HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`.
