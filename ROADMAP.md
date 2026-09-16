# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | SOURCE-FORMAT PROPOSAL REVIEW PASS; EXECUTION AUTHORIZATION ARTIFACT NEXT | proposal checkpoint `d8dc240b...18b2`; proposal CI `35060253297` SUCCESS; review PASS |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` previously stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- one-shot diagnostic run `35019840276`: SUCCESS;
- diagnostic result `DIAGNOSTIC_CLASSIFIED`;
- diagnostic class `ASCII_STRUCTURAL_MISMATCH`;
- diagnostic evidence review decision: `PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`;
- source-format diagnostic proposal prepared offline;
- source-format proposal package checkpoint `d8dc240bd74e271f88b2ef4583f6b79e533918b2`;
- source-format proposal CI `35060253297`: SUCCESS;
- source-format proposal human review completed;
- review decision: `PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`;
- no execution/full-row privacy approval granted;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Source-Format Proposal Review

The proposal design is accepted for progression to preparation of a separate execution/authorization artifact only.

The explicit future one-row full-row transient privacy expansion is accepted as a design boundary because it remains:

- limited to the first reproduced mismatch row;
- in-memory only;
- non-persistent and non-logged;
- separately gated by fresh execution and full-row transient privacy approvals;
- bounded by the same request/row/byte envelope already reviewed.

No network access or full-row exposure is authorized by the review.

## Mandatory Execution-Artifact Tightenings

The next artifact must hard-lock:

1. exact first-match precedence for the five diagnostic classes;
2. reuse of the exact same in-memory logical-row bytes with no re-read;
3. deterministic stdlib newline/multiline framing, including explicit `StringIO(..., newline="")`-equivalent behavior;
4. exactly one parsed CSV record, with zero/multiple records fail-closed;
5. enumerated non-source-bearing fail-closed reason codes and no free-text/parser exception persistence.

These requirements must not widen source access, privacy exposure or runtime scope.

## Reviewed Future Bounds — Still Not Authorized

- exact pinned source endpoint and identity;
- first canonical member only;
- maximum 4 transient rows while reproducing the target mismatch;
- maximum 1 full-row independent cross-check;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retry/redirect/additional range/full-body fallback/automatic widening.

No exact source value, row/field content, hash, exact length, fragment, codepoint, transformed value, PROPERTY_ID, owner/holder value, parser exception text or source-derived free text may persist or be logged.

## Next Product Work

Prepare only, offline:

`PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_ARTIFACT`

The artifact must incorporate all mandatory tightenings and must not itself perform network access or real full-row exposure. Any future execution/full-row privacy tokens introduced by the artifact must remain ungranted until a separate human authorization gate.

## Still Out of Scope

- reuse of any consumed approval;
- source or authority network access during artifact preparation;
- real full-row exposure before fresh explicit privacy approval;
- source-value reconstruction or inference;
- parser or regex changes;
- trimming, casing or normalization runtime changes;
- Unicode normalization;
- automatic remediation;
- new authority retrieval at this checkpoint;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.