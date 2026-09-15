# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | DIAGNOSTIC EXECUTION AUTHORIZATION ARTIFACT VERIFIED; HUMAN AUTHORIZATION REVIEW REQUIRED | package `daeaa7bf...866c`; CI `35017854034` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second bounded semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- v1.1 separates UTF-8 encoding failure from decoded non-empty format mismatch;
- exact offending source content was intentionally not retained and must not be reconstructed or inferred from historical evidence;
- archived authority confirms `ZZZZ`, `IN01`-`IN08`, `IN99` and does not contradict the current shape regex;
- live source semantic compatibility remains unresolved;
- bounded diagnostic/remediation evidence proposal was human-reviewed `PASS`;
- separate diagnostic execution/authorization artifact is prepared on `m3-ca-sco-property-type-diagnostic-execution-authorization`;
- authorization package checkpoint `daeaa7bfb7f7d73a61f011d394cc88393625866c` passed CI `35017854034`;
- artifact status remains `PENDING_HUMAN_AUTHORIZATION`;
- package preparation performed no source request and created no network workflow;
- source policy remains `PROPOSED` and production classification remains inactive.

## Fresh Authorization Gates — Not Granted

The authorization artifact defines:

- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both approvals are single-use, non-reusable, must pin the reviewed authorization package SHA, and are required together before network execution.

Neither approval is currently granted. Prior consumed semantic/privacy/authority approvals remain non-reusable.

## Verified Future Diagnostic Boundary — Still Blocked

If and only if later human review passes and both fresh approvals are explicitly granted:

- exact known endpoint and pinned source identity only;
- first canonical ZIP member only;
- maximum 4 transient data rows;
- stop at first reproduced format mismatch;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes total;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retry, redirect, additional range, full-body fallback or automatic widening;
- source identity drift or non-reproduction within the bound -> fail closed.

The classifier is fully deterministic: fixed precedence, ASCII-only `a-z` -> `A-Z`, explicitly enumerated control-code set, fixed fail-closed reason codes and synthetic regression vectors.

Only bounded categorical/counter/safety evidence may persist. Exact source values and identifying/source-derived detail remain forbidden.

No diagnostic result automatically authorizes remediation.

## Next Product Work

Perform only:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Review the authorization artifact, schema, audit and contract tests. Do not access the source or create/execute a diagnostic network workflow during review.

A `PASS` at this review is not sufficient for execution. Both fresh approval evidences must then be explicitly granted by the owner and pin package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c` before the project can enter `ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`.

## Still Out of Scope

- reuse of any consumed approval;
- source access before both fresh approval evidences are valid;
- approval inference from a review PASS;
- network-workflow creation before authorization;
- source-value reconstruction from historical evidence;
- exact source-value hashing, exact-length capture, fragments or codepoints;
- real-row full-parser crosscheck under this artifact;
- parser, regex, casing, trimming or normalization runtime changes;
- Unicode normalization probes;
- automatic remediation;
- source or registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
