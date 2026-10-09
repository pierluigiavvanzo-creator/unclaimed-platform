# M3 California SCO — PROPERTY_TYPE Diagnostic Execution / Authorization Review

Date: 2026-09-15

Status: **HUMAN REVIEW COMPLETED — PASS — FRESH APPROVALS STILL NOT GRANTED**

## Review gate

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

## Reviewed checkpoint

Authorization branch:

`m3-ca-sco-property-type-diagnostic-execution-authorization`

Authorization branch final HEAD reviewed:

`de73b2d4d0fdcc236cbcfa3a0ad253c617919b28`

Authorization package checkpoint SHA:

`daeaa7bfb7f7d73a61f011d394cc88393625866c`

Package CI:

`35017854034` — SUCCESS

Final authorization-branch CI:

`35018090207` — SUCCESS

Reviewed artifacts:

- `sources/proposals/ca_sco_segment_500_plus.property_type_diagnostic_execution_authorization.v1.json`
- `schemas/common/property_type_diagnostic_execution_authorization.schema.json`
- `tests/contract/test_ca_sco_property_type_diagnostic_execution_authorization.py`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION.md`
- `PROJECT_STATE.md`
- `ROADMAP.md`
- `docs/handovers/HANDOVER_CURRENT.md`

## Review scope

Repository-only review. No request to California SCO or `claimit.ca.gov`, no transient real-row inspection, no diagnostic execution, no network workflow creation and no runtime/parser/regex/normalization/logging/persistence modification.

The historical unretained `PROPERTY_TYPE` value is not reconstructed, inferred, hashed, measured or otherwise recovered.

## Decision

**PASS**

The authorization package is acceptable as the bounded contract that may later be activated only after two fresh explicit owner approvals are durably recorded and both pin the exact reviewed package SHA.

This PASS does **not** grant either approval and does **not** authorize source network access or transient-row exposure by itself.

## Why the package passes

### 1. Review and proposal provenance are pinned

The artifact pins:

- proposal-review HEAD `06896084475f0f899fc3e002344e22fc49ffa54d`;
- reviewed proposal package `020044d3013449fabe566c5164b8f99f9d8cc9ab`;
- reviewed proposal HEAD `847cdf5daaa1834c3ce11fc3d6f29e2bbc36b4b4`;
- the completed proposal-review audit.

### 2. Two fresh approvals are independent and fail closed

The package defines, but does not grant:

- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`;
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`.

Both are single-use, non-reusable, must pin package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c`, and both are required before any network request.

Previous consumed approvals cannot satisfy these gates.

### 3. Execution boundary does not widen the reviewed proposal

The package remains bounded to:

- exact existing endpoint only;
- pinned source identity;
- first canonical member only;
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
- authority and other endpoint access forbidden;
- source identity drift and non-reproduction inside the bound fail closed.

The compare from proposal-review HEAD to package checkpoint changes only the four expected package files.

### 4. Classifier tightening is deterministic

The fixed precedence is:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

The current regex remains unchanged:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Diagnostic whitespace is exactly surrounding `U+0020` and `U+0009`; diagnostic case probing maps ASCII `a-z` to `A-Z` only; Unicode normalization and locale-sensitive casing are forbidden; non-ASCII and the exact ASCII control set are defined; precedence resolves boundary TAB collisions deterministically.

Synthetic regression vectors cover all five classes and precedence/boundary cases. They are test-only and are not evidence about a real source value.

### 5. Output and privacy boundaries are non-value-bearing

A successful diagnostic may persist only a coarse diagnostic class and bounded counters/safety metadata. A fail-closed result must use an enumerated reason code and null diagnostic class.

Persistence/logging remains forbidden for exact `PROPERTY_TYPE`, bytes, hash, exact length, fragments, codepoints, transformed value, full row, raw response body, `PROPERTY_ID`, owner/holder values, distinct source code lists and source-derived free text.

### 6. No remediation or runtime change is authorized

All runtime-transform acceptance and remediation flags remain false. No diagnostic class can directly authorize trimming, uppercasing, normalization, parser change or regex change.

### 7. Governance remains closed

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain 0; semantic compatibility remains unresolved; production classification remains inactive; downstream identity, genealogy, beneficiary matching, outreach and claim-submission gates remain closed.

## Authorization state after review

- review decision: `PASS`
- execution approval granted: `false`
- transient-row privacy approval granted: `false`
- diagnostic execution authorized: `false`
- transient-row privacy exposure authorized: `false`
- network workflow creation authorized: `false`
- network execution authorized: `false`
- runtime change authorized: `false`
- remediation authorized: `false`
- approval evidence created by this review: `false`

## Next action

Stop for explicit owner authorization.

Before any source request, the owner must explicitly grant **both** exact approval references:

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`

`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both durable approval evidence files must pin reviewed package SHA:

`daeaa7bfb7f7d73a61f011d394cc88393625866c`

Only after both are valid may the project prepare/enter the bounded one-shot execution gate:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

Do not infer either approval from this PASS or from generic wording such as `procedi`.
