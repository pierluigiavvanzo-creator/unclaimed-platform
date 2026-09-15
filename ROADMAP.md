# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | DIAGNOSTIC/REMEDIATION EVIDENCE PROPOSAL VERIFIED; HUMAN REVIEW REQUIRED | proposal CI `35015429439`; package `020044d3...c9ab` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- prior bounded semantic execution stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- the v1.1 runner already separates encoding failure from decoded format mismatch;
- second real run `34995672539` therefore narrowed the issue to a decoded, non-empty value failing the unchanged shape regex;
- exact offending source content was intentionally not retained and must not be reconstructed or inferred;
- one-shot California SCO authority archival completed successfully in run `35012019831`;
- authority archive provenance review established that `ZZZZ` and insurance codes `IN01`-`IN08`, `IN99` are supported and that the current shape regex is not contradicted by the authority;
- live source semantic compatibility remains unresolved;
- bounded diagnostic/remediation evidence proposal is prepared on `m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal`;
- proposal package checkpoint `020044d3013449fabe566c5164b8f99f9d8cc9ab` passed CI `35015429439`;
- proposal status is `PROPOSAL_ONLY_NOT_AUTHORIZED`;
- proposal preparation performed no source request and no runtime/parser/regex/normalization/logging/persistence change;
- source policy remains `PROPOSED` and production classification remains inactive.

## Next Product Work

Perform only:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

Review whether the proposed diagnostic evidence boundary is acceptable. The review itself must not access SCO/`claimit.ca.gov`, reconstruct the source value, change runtime semantics or execute a diagnostic.

If the proposal review is `PASS` and a real diagnostic is desired, prepare a **separate explicit diagnostic execution/authorization artifact** requiring fresh execution and transient-row privacy approvals. Do not perform source access merely because the proposal review passes.

## Proposed Future Diagnostic Boundary — Not Authorized Yet

If separately approved later:

- exact existing endpoint and pinned source identity only;
- first canonical member only;
- maximum 4 transient data rows;
- stop at first reproduced format mismatch;
- 1 HEAD + 1 Range GET maximum;
- 2 HTTP requests maximum total;
- 131072 source response-body bytes maximum total;
- zero retry, redirect, additional range, full-body fallback or automatic widening;
- persist only a fixed coarse diagnostic class, bounded counters and safety flags;
- do not persist/log exact value, bytes, hash, length, fragments, codepoints, transformed values, full row, raw body, PROPERTY_ID or owner/holder values;
- no diagnostic class automatically authorizes remediation.

## Still Out of Scope

- reuse of any consumed approval;
- diagnostic source access before a separate execution/privacy authorization gate;
- another authority retrieval without a separate proposal/gate;
- source-value reconstruction or inference;
- exact source-value hashing or length capture;
- real-row full-parser crosscheck under this proposal;
- parser, regex, casing, trimming or normalization changes;
- Unicode normalization probes;
- another real PROPERTY_TYPE semantic execution;
- source or registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
