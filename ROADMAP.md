# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | SOURCE-FORMAT AUTHORIZATION REVIEW PASS; OWNER APPROVALS NEXT | authorization package `cd76250b...9172`; package CI `35082891083` SUCCESS; review PASS |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- bounded diagnostic execution `35019840276`: SUCCESS;
- diagnostic class: `ASCII_STRUCTURAL_MISMATCH`;
- diagnostic evidence review justified a separate source-format diagnostic proposal;
- source-format proposal package `d8dc240bd74e271f88b2ef4583f6b79e533918b2`: CI SUCCESS;
- source-format proposal review: `PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`;
- source-format execution/authorization package `cd76250b9527be91e7e7ac4b3aa658c864cf9172`: CI `35082891083` SUCCESS;
- authorization final state `e73681941ef9794d54bef78b53361ea45baccbf9`: CI `35083155026` SUCCESS;
- authorization human review: `PASS`;
- no fresh source-format approval granted;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Reviewed Source-Format Execution Contract

The reviewed future execution remains bounded to:

- exact pinned source endpoint and identity;
- first canonical ZIP member only;
- maximum 4 transient rows;
- maximum 1 transient full-row cross-check;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retry/redirect/additional range/full-body fallback/automatic widening.

T-1 through T-5 are machine-locked. No exact source values, full row, field content, hashes, exact lengths, parser exception text or source-derived free text may persist or be logged.

## Owner Approval Gate

Execution remains blocked until the owner explicitly grants both exact fresh tokens:

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Both must be single-use/non-reusable and their future evidence must pin:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Generic wording must not be interpreted as approval.

## Still Out of Scope

- reuse of any consumed approval;
- source or authority network access before both fresh approvals;
- real full-row exposure before the fresh privacy approval;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- new authority retrieval;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.