# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary, but semantic compatibility with the live source remains unresolved.

The bounded diagnostic/remediation evidence proposal has been prepared, CI-verified and human-reviewed **PASS**.

Proposal branch:
`m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal`

Proposal package checkpoint SHA:
`020044d3013449fabe566c5164b8f99f9d8cc9ab`

Proposal package CI:
`35015429439` — SUCCESS

Final proposal branch HEAD reviewed:
`847cdf5daaa1834c3ce11fc3d6f29e2bbc36b4b4`

Final proposal branch CI:
`35015731733` — SUCCESS

Review branch:
`m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal-review`

Review gate:
`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

Review decision:
`PASS`

Review audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW.md`

### Verified basis

The second bounded semantic execution remains the latest real PROPERTY_TYPE source execution:

- run `34995672539`;
- schema `1.1.0`;
- result `STOPPED_FAIL_CLOSED`;
- stop `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- the observed mismatch was a decoded, non-empty PROPERTY_TYPE that failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- exact offending value, bytes, hash, length, fragments and codepoints were not retained and must not be reconstructed or inferred from historical evidence.

The completed authority provenance review established that the current regex is not contradicted by the archived authority and did not authorize trimming, casing, normalization, parser change or regex relaxation.

### Accepted proposal boundary — still not authorized for execution

If a later separate execution/authorization artifact is approved with fresh execution/privacy approvals, the diagnostic may be bounded to:

- exact existing endpoint and pinned source identity;
- first canonical member only;
- at most 4 transient data rows;
- stop at the first reproduced format mismatch;
- 1 HEAD maximum;
- 1 Range GET maximum;
- 2 HTTP requests maximum total;
- 131072 source response-body bytes maximum total;
- no retry, redirect, extra range, full-body fallback or automatic widening.

Only a fixed coarse diagnostic class plus bounded counters/safety flags may be persisted. Exact source values, bytes, hashes, lengths, fragments, codepoints, transformed values, full rows, raw bodies, PROPERTY_ID and owner/holder values remain forbidden from persistence/logging.

No diagnostic class automatically authorizes remediation.

### Mandatory execution-stage tightening

Before any real diagnostic request, the separate execution/authorization artifact must contract-test:

- fixed classification precedence;
- exact ASCII-only `a-z` -> `A-Z` case-probe semantics;
- exact disallowed ASCII control-code set;
- bounded enumerated fail-closed reason codes and explicit null/absent semantics for diagnostic class on failure;
- synthetic classifier tests for all classes, precedence collisions, boundary cases and non-persistence/non-logging.

These tightenings may not widen members, rows, requests, byte budgets, endpoints, privacy scope or persistence fields.

### Governance remains fail-closed

- proposal review PASS does not authorize source access;
- diagnostic execution authorized: `false`;
- transient-row privacy exposure authorized: `false`;
- network workflow authorized: `false`;
- runtime change authorized: `false`;
- remediation authorized: `false`;
- no approval token was created by the review;
- previous semantic execution/privacy approvals remain CONSUMED + NON-REUSABLE;
- authority archival approval remains CONSUMED + NON-REUSABLE;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Prepare only a **separate diagnostic execution/authorization artifact offline**.

It must pin the proposal review PASS, preserve or tighten all boundaries, define fresh execution and transient-row privacy approval placeholders, and remain NOT AUTHORIZED until the owner explicitly grants those approvals.

Do not access SCO/`claimit.ca.gov` and do not perform the diagnostic while preparing that artifact.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
