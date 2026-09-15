# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. Live-source semantic compatibility remains unresolved.

The bounded diagnostic/remediation evidence proposal was human-reviewed `PASS`. The separate diagnostic execution/authorization artifact was prepared offline, CI-verified, and has now also completed human authorization review with `PASS`.

Authorization package checkpoint SHA:
`daeaa7bfb7f7d73a61f011d394cc88393625866c`

Authorization package CI:
`35017854034` — SUCCESS

Final authorization branch HEAD reviewed:
`de73b2d4d0fdcc236cbcfa3a0ad253c617919b28`

Final authorization branch CI:
`35018090207` — SUCCESS

Review branch:
`m3-ca-sco-property-type-diagnostic-execution-authorization-review`

Review gate:
`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Review decision:
`PASS`

Review audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW.md`

## Fresh Approvals Defined — Still Not Granted

The review PASS does not grant either approval.

Required exact approval references:

- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both must be explicitly granted by the owner, single-use, non-reusable, and durably evidenced with package SHA:

`daeaa7bfb7f7d73a61f011d394cc88393625866c`

Both are required before any `claimit.ca.gov` request. No approval evidence file has been created by the review and no network workflow has been created.

Previously consumed approvals remain non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

## Verified Diagnostic Boundary — Still Not Authorized for Execution

Only after both fresh approvals are valid may the bounded diagnostic proceed, with:

- exact existing endpoint and pinned source identity only;
- first canonical ZIP member only;
- maximum 4 transient data rows;
- stop at first reproduced format mismatch;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes total;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries, redirects, additional ranges, full-body fallback or automatic widening;
- source identity drift or non-reproduction within the bound -> fail closed.

The classifier contract is deterministic and keeps the current regex unchanged. Diagnostic transforms are in-memory predicates only and cannot become runtime remediation.

Only coarse diagnostic class / fail-closed reason / bounded counters / safety flags may persist. Exact PROPERTY_TYPE content, bytes, hash, exact length, fragments, codepoints, transformed values, full rows, raw bodies, PROPERTY_ID, owner/holder values, distinct code lists and source-derived free text remain forbidden.

No diagnostic class automatically authorizes remediation.

## Governance Remains Fail-Closed

- diagnostic execution authorized: `false`;
- transient-row privacy exposure authorized: `false`;
- network workflow creation authorized: `false`;
- network execution authorized: `false`;
- runtime change authorized: `false`;
- remediation authorized: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- production classification: inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED.

## Next Recommended Action

Stop for explicit owner authorization.

The owner must explicitly provide **both** exact fresh approvals above. Do not infer either approval from `PASS`, `procedi`, or generic wording.

After both durable approval evidences exist and pin package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c`, the next bounded gate may be:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
