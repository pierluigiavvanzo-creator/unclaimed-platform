# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | ONE-SHOT AUTHORITY ARCHIVAL AUTHORIZATION ARTIFACT VERIFIED; HUMAN AUTHORIZATION REVIEW REQUIRED | package `d20bc80f...`; CI `35007468140` SUCCESS; network still unauthorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second bounded PROPERTY_TYPE semantic execution completed once and stopped fail-closed;
- prior execution/privacy approvals are consumed and non-reusable;
- repository-only provenance review completed;
- retained provenance does not justify semantic/runtime change;
- bounded authority provenance acquisition proposal prepared and human-reviewed `PASS`;
- separate one-shot authority archival execution/authorization artifact prepared offline and CI verified;
- artifact status is `PENDING_HUMAN_AUTHORIZATION`;
- authority retrieval/download remains unauthorized;
- semantic compatibility remains unresolved;
- production classification remains inactive.

## Fresh Authority Archival Authorization

Required review gate:
`HUMAN_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_AUTHORIZATION_REVIEW`

Required fresh approval ref if the review passes:
`APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

The approval must be single-use, non-reusable, and pin the verified authorization-artifact SHA. The prepared artifact itself keeps network execution and workflow creation unauthorized.

## Next Product Work

Perform only the human authorization review of the verified artifact package. Do not access or download the authority during that review.

Only a later explicit PASS may create the approval evidence needed for the one-shot archival execution.

## Still Out of Scope

- authority retrieval before the fresh authorization passes;
- additional authority discovery;
- SCO dataset or `claimit.ca.gov` access;
- parser, regex, casing, trimming or normalization changes;
- another semantic execution;
- source or registry activation;
- production classification activation.
