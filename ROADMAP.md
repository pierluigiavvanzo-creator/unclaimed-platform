# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | DIAGNOSTIC EVIDENCE REVIEW PASS; SOURCE-FORMAT PROPOSAL NEXT | run `35019840276`; class `ASCII_STRUCTURAL_MISMATCH`; no remediation authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` previously stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- diagnostic/remediation evidence proposal review: `PASS`;
- diagnostic execution/authorization review: `PASS`;
- both fresh diagnostic execution/privacy approvals were explicitly granted, pinned to package `daeaa7bfb7f7d73a61f011d394cc88393625866c`, then consumed before source access;
- one-shot diagnostic run `35019840276`: SUCCESS;
- source identity verified;
- exactly 1 HEAD + 1 Range GET, 2 HTTP requests total;
- exactly 131072 source response-body bytes read;
- exactly 1 transient data row examined;
- result `DIAGNOSTIC_CLASSIFIED`;
- diagnostic class `ASCII_STRUCTURAL_MISMATCH`;
- one-shot workflow removed after execution;
- no exact source value or protected derivative persisted;
- no remediation performed;
- human diagnostic evidence review completed;
- review decision: `PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Reviewed Interpretation

Within the fixed deterministic classifier, `ASCII_STRUCTURAL_MISMATCH` means the mismatch was not explained solely by:

- surrounding ASCII SPACE/TAB;
- ASCII case;
- surrounding ASCII SPACE/TAB plus ASCII case;
- non-ASCII or disallowed ASCII control content.

The evidence does **not** identify the actual value or a positive root cause. It does not establish a parser defect, source schema change, alternate code shape, exact-length condition, prefix/suffix pattern or valid regex relaxation.

The authority branch is not the next justified investigation because the archived SCO authority has already resolved the targeted provenance questions and does not contradict the unchanged regex. The smallest justified next work is an offline source-format diagnostic proposal.

## Next Product Work

Prepare only:

`PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL`

The proposal must be offline/design-only and must not:

- access `claimit.ca.gov` or SCO authority endpoints;
- reconstruct or infer the unretained PROPERTY_TYPE value;
- persist exact/hash/length/fragments/codepoints of a source value;
- modify parser or regex;
- introduce trimming, casing or normalization runtime behavior;
- apply remediation;
- activate source policy, registry or production classification.

If a future proposal includes any further real-source inspection, it must define a new narrow privacy boundary and fresh single-use execution/privacy approvals pinned to the exact reviewed artifact.

## Still Out of Scope

- reuse of either diagnostic approval or any historical consumed approval;
- additional source requests without a new reviewed bounded gate;
- new authority retrieval at this checkpoint;
- source-value reconstruction or inference;
- exact source-value hashing, exact-length capture, fragments or codepoints;
- parser or regex changes;
- trimming, casing or normalization runtime changes;
- Unicode normalization probes;
- automatic remediation;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.