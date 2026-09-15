# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | AUTHORITY ARCHIVED; PROVENANCE REVIEW REQUIRED | run `35012019831`; archive SHA-256 `7884f765...721e5` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- prior bounded semantic execution stopped fail-closed;
- repository-only provenance review completed;
- retained provenance alone did not justify semantic/runtime change;
- authority provenance proposal human-reviewed `PASS`;
- one-shot archival authorization package verified;
- fresh one-shot approval granted, consumed and non-reusable;
- authority archival run `35012019831` completed successfully;
- archive stored with SHA-256 `7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5`;
- no semantic extraction performed during archival;
- semantic compatibility remains unresolved;
- production classification remains inactive.

## Next Product Work

Perform only:
`HUMAN_PROPERTY_TYPE_AUTHORITY_ARCHIVE_PROVENANCE_REVIEW`

Review the archived authority against the unresolved PROPERTY_TYPE provenance questions before any semantic/runtime change.

## Still Out of Scope

- another authority retrieval using the consumed approval;
- additional authority discovery without a new proposal/gate;
- SCO dataset or `claimit.ca.gov` access for this task;
- parser, regex, casing, trimming or normalization changes before provenance review;
- another semantic execution;
- source or registry activation;
- production classification activation.
