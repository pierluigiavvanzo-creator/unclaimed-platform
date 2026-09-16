# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | SOURCE-FORMAT EXECUTION AUTHORIZATION PACKAGE PREPARED; HUMAN REVIEW REQUIRED | package `cd76250b...9172`; CI `35082891083` SUCCESS |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` previously stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- bounded diagnostic run `35019840276`: SUCCESS;
- diagnostic class: `ASCII_STRUCTURAL_MISMATCH`;
- diagnostic evidence review: `PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`;
- source-format proposal package: `d8dc240bd74e271f88b2ef4583f6b79e533918b2`;
- source-format proposal review: `PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`;
- source-format execution/authorization package: `cd76250b9527be91e7e7ac4b3aa658c864cf9172`;
- package CI `35082891083`: SUCCESS;
- no source-format execution approval granted;
- no full-row transient privacy approval granted;
- no source-format network workflow exists;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Authorization Package

Artifact status:
`PENDING_HUMAN_AUTHORIZATION`

Human gate:
`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Two fresh approval references are defined but ungranted:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Both are single-use/non-reusable and, if later explicitly granted after a review PASS, must be evidenced separately and pinned to package `cd76250b9527be91e7e7ac4b3aa658c864cf9172` before any network request.

## Mandatory Tightenings Implemented

The package locks:

1. exact five-class first-match precedence;
2. same in-memory logical-row bytes only, with no source re-read;
3. deterministic `io.StringIO(..., newline="")`-equivalent stdlib multiline framing;
4. exactly one parsed CSV record or enumerated fail-closed stop;
5. enumerated non-source-bearing fail-closed reasons with no parser exception/source-derived free text.

Synthetic regression coverage includes embedded LF, embedded CRLF and multi-record rejection.

## Future Bounds — Still Not Authorized

- exact pinned endpoint/source identity;
- first canonical member only;
- maximum 4 transient rows;
- maximum 1 full-row comparator row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retry/redirect/additional range/full-body fallback/automatic widening.

No source values, full row, field content, protected derivatives, parser exception text or source-derived free text may persist or be logged.

## Next Product Work

Perform only:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

A PASS approves only the authorization contract. It must not be treated as either execution approval or full-row transient privacy approval.

## Still Out of Scope

- reuse of any consumed approval;
- source or authority network access before fresh approvals;
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
