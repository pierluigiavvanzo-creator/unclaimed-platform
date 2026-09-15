# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | DIAGNOSTIC EXECUTION AUTHORIZATION REVIEW PASS; TWO FRESH OWNER APPROVALS REQUIRED | package `daeaa7bf...866c`; final authorization CI `35018090207`; review audit recorded |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second bounded semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- exact offending source content was intentionally not retained and must not be reconstructed or inferred from historical evidence;
- archived authority does not contradict the current shape regex;
- live source semantic compatibility remains unresolved;
- diagnostic/remediation evidence proposal human review: `PASS`;
- diagnostic execution/authorization package checkpoint: `daeaa7bfb7f7d73a61f011d394cc88393625866c`;
- package CI `35017854034`: SUCCESS;
- final authorization branch HEAD `de73b2d4d0fdcc236cbcfa3a0ad253c617919b28` passed CI `35018090207`;
- human gate `HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`: `PASS`;
- review PASS does not itself grant source access or transient-row privacy exposure;
- source policy remains `PROPOSED` and production classification remains inactive.

## Fresh Owner Approvals — Required Before Network

Both exact approvals must be granted explicitly and durably pin package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c`:

- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both are single-use and non-reusable. Neither is granted by the review PASS. No source request or diagnostic network workflow is authorized until both evidences are valid.

## Bounded Diagnostic Contract

After both approvals only:

- exact known endpoint and pinned source identity;
- first canonical ZIP member only;
- maximum 4 transient data rows;
- stop at first reproduced format mismatch;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes total;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries, redirects, additional ranges, full-body fallback or automatic widening;
- identity drift or mismatch not reproduced within the bound -> fail closed;
- deterministic five-class classifier with unchanged regex;
- only coarse categorical/counter/safety evidence may persist;
- no diagnostic class automatically authorizes remediation.

## Next Product Work

Obtain explicit owner authorization for **both** fresh approval references above.

Do not infer approval from generic wording. After both durable evidences exist and pin the reviewed package SHA, the project may enter:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

After any later diagnostic result, stop at:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`

## Still Out of Scope

- reuse of any consumed approval;
- source access before both fresh approvals are valid;
- approval inference from review PASS or generic wording;
- source-value reconstruction from historical evidence;
- exact source-value hashing, exact-length capture, fragments or codepoints;
- parser, regex, casing, trimming or normalization runtime changes;
- Unicode normalization probes;
- automatic remediation;
- source or registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
