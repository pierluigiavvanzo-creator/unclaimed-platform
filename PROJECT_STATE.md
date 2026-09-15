# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. Live-source semantic compatibility remains unresolved.

The bounded diagnostic/remediation evidence proposal was human-reviewed `PASS`. A separate diagnostic execution/authorization artifact has now been prepared offline and CI-verified.

Current branch:
`m3-ca-sco-property-type-diagnostic-execution-authorization`

Authorization package checkpoint SHA:
`daeaa7bfb7f7d73a61f011d394cc88393625866c`

Authorization package CI:
`35017854034` — SUCCESS

Artifact status:
`PENDING_HUMAN_AUTHORIZATION`

Artifact:
`sources/proposals/ca_sco_segment_500_plus.property_type_diagnostic_execution_authorization.v1.json`

Schema:
`schemas/common/property_type_diagnostic_execution_authorization.schema.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION.md`

Contract test:
`tests/contract/test_ca_sco_property_type_diagnostic_execution_authorization.py`

## Fresh Approvals Defined — Not Granted

The artifact defines two distinct fresh approvals:

- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both are single-use, non-reusable and must pin the reviewed authorization package SHA. Both are currently `granted: false`, and both are required before any diagnostic network access.

No approval evidence file exists and no diagnostic network workflow has been created by package preparation.

Previously consumed approvals remain non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

## Verified Diagnostic Boundary — Still Not Authorized

If later separately reviewed and both fresh approvals are explicitly granted, the diagnostic is bounded to:

- exact existing `claimit.ca.gov` endpoint and pinned source identity;
- first canonical member only;
- maximum 4 transient data rows;
- stop at first reproduced format mismatch;
- maximum 1 HEAD and 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes total;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- redirects forbidden;
- additional range forbidden;
- full-body fallback forbidden;
- automatic widening forbidden;
- source identity drift or non-reproduction inside the bound -> fail closed.

No other source/endpoint or authority access is allowed by this artifact.

## Deterministic Classifier Contract

The execution artifact locks classification precedence to:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

The regex remains unchanged:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

ASCII case probing maps only `a-z` to `A-Z`; all other code points remain unchanged. Locale-sensitive casing and Unicode normalization are forbidden.

The disallowed ASCII control set is explicitly `U+0000` through `U+001F` plus `U+007F`. Precedence ensures that a boundary TAB explaining the mismatch is classified as surrounding whitespace before the control-content class is considered.

Synthetic regression vectors cover all five classes, precedence collisions, boundary TAB behavior, non-ASCII/control content and ASCII structural mismatch.

## Persistence / Fail-Closed Contract

Only bounded status/class/reason-code/source-identity/counter/safety evidence may be persisted.

Exact PROPERTY_TYPE content, bytes, hash, exact length, fragments, codepoints, transformed values, full rows, raw bodies, PROPERTY_ID, owner/holder values, distinct code lists and source-derived free text remain forbidden.

When `STOPPED_FAIL_CLOSED`, `diagnostic_class` is null and a fixed enumerated fail-closed reason code is required. No diagnostic class authorizes remediation.

## Governance Remains Fail-Closed

- diagnostic execution authorized: `false`;
- transient-row privacy exposure authorized: `false`;
- network workflow creation authorized: `false`;
- network execution authorized: `false`;
- runtime change authorized: `false`;
- remediation authorized: `false`;
- third real execution authorized: `false`;
- source request performed during preparation: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- production classification: inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED.

## Next Recommended Action

Perform only:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Review the verified authorization artifact package. Do not access `claimit.ca.gov`, create a diagnostic network workflow, or treat either fresh approval as granted during this review.

A review `PASS` still requires the owner to explicitly grant both fresh approvals, with durable evidence pinned to package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c`, before any source request.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
