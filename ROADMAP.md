# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | DIAGNOSTIC/REMEDIATION EVIDENCE PROPOSAL HUMAN-REVIEWED PASS; EXECUTION STILL NOT AUTHORIZED | proposal CI `35015731733`; review audit recorded |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- prior bounded semantic execution stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- v1.1 already separates encoding failure from decoded format mismatch;
- second real run `34995672539` narrowed the issue to a decoded, non-empty value failing the unchanged shape regex;
- exact offending source content was intentionally not retained and must not be reconstructed or inferred from historical evidence;
- one-shot California SCO authority archival completed successfully in run `35012019831`;
- authority archive provenance review established that `ZZZZ` and insurance codes `IN01`-`IN08`, `IN99` are supported and that the current shape regex is not contradicted by the authority;
- live source semantic compatibility remains unresolved;
- bounded diagnostic/remediation evidence proposal prepared on `m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal`;
- proposal package checkpoint `020044d3013449fabe566c5164b8f99f9d8cc9ab` passed CI `35015429439`;
- final reviewed proposal HEAD `847cdf5daaa1834c3ce11fc3d6f29e2bbc36b4b4` passed CI `35015731733`;
- human review gate `HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW` completed with `PASS`;
- review PASS accepts the bounded design only and does not authorize source access or remediation;
- source policy remains `PROPOSED` and production classification remains inactive.

## Next Product Work

Prepare only a **separate diagnostic execution/authorization artifact offline**.

That artifact must:

- pin the reviewed proposal and review PASS;
- preserve or tighten the one-member / one-range / max-four-row / 131072-byte boundary;
- explicitly define classification precedence;
- define ASCII-only `a-z` -> `A-Z` case-probe semantics;
- enumerate the exact disallowed ASCII control-code set;
- define bounded fail-closed reason codes and diagnostic-class null/absent semantics on failure;
- add synthetic classifier regression coverage;
- define fresh execution and transient-row privacy approval placeholders;
- remain NOT AUTHORIZED until the owner separately grants the fresh approvals.

Preparation of that artifact must perform no SCO/`claimit.ca.gov` request and create no live diagnostic execution.

## Accepted Future Diagnostic Boundary — Not Authorized Yet

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
- source-value reconstruction from historical evidence;
- exact source-value hashing or length capture;
- real-row full-parser crosscheck under the accepted proposal;
- parser, regex, casing, trimming or normalization changes;
- Unicode normalization probes;
- another real PROPERTY_TYPE semantic/diagnostic execution;
- source or registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
