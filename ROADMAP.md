# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | ONE-SHOT PROPERTY_TYPE DIAGNOSTIC COMPLETED; HUMAN EVIDENCE REVIEW REQUIRED | run `35019840276`; class `ASCII_STRUCTURAL_MISMATCH` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` previously stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority does not contradict the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- diagnostic/remediation evidence proposal review: `PASS`;
- diagnostic execution/authorization review: `PASS`;
- both fresh execution/privacy approvals were explicitly granted, pinned to package `daeaa7bfb7f7d73a61f011d394cc88393625866c`, then consumed before source access;
- one-shot diagnostic run `35019840276`: SUCCESS;
- source identity verified;
- exactly 1 HEAD + 1 Range GET, 2 HTTP requests total;
- exactly 131072 source response-body bytes read;
- 1 transient data row examined;
- result `DIAGNOSTIC_CLASSIFIED`;
- diagnostic class `ASCII_STRUCTURAL_MISMATCH`;
- one-shot workflow removed after execution;
- no exact source value or protected derivative persisted;
- no remediation performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Bounded Interpretation — Pending Human Review

Within the fixed deterministic classifier, `ASCII_STRUCTURAL_MISMATCH` is reached only after the mismatch is not explained solely by:

- surrounding ASCII SPACE/TAB;
- ASCII case;
- surrounding ASCII SPACE/TAB plus ASCII case;
- non-ASCII or disallowed ASCII control content.

This classification does not reveal the actual PROPERTY_TYPE value and does not itself authorize any regex/parser/runtime change.

## Next Product Work

Perform only:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`

The review must determine what the coarse evidence justifies while preserving privacy and fail-closed governance. No remediation is automatic.

## Still Out of Scope

- reuse of either diagnostic approval or any historical consumed approval;
- reconstruction/inference of the unretained PROPERTY_TYPE value;
- exact source-value hashing, exact-length capture, fragments or codepoints;
- parser or regex changes;
- trimming, casing or normalization runtime changes;
- Unicode normalization probes;
- automatic remediation;
- additional source requests without a separate gate;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
