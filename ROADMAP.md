# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | AUTHORITY PROVENANCE PROPOSAL HUMAN-REVIEWED PASS; RETRIEVAL STILL NOT AUTHORIZED | proposal package `963c205b...`; CI `35005451605` SUCCESS; review audit recorded |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second bounded PROPERTY_TYPE semantic execution completed once and stopped fail-closed;
- prior execution/privacy approvals are consumed and non-reusable;
- repository-only provenance review completed;
- retained provenance does not justify semantic/runtime change;
- bounded authority provenance acquisition proposal prepared and CI verified;
- human review of that proposal: `PASS`;
- authority retrieval/download remains unauthorized;
- semantic compatibility remains unresolved;
- production classification remains inactive.

## Authority Proposal Review

Review gate:
`HUMAN_PROPERTY_TYPE_AUTHORITY_PROVENANCE_ACQUISITION_PROPOSAL_REVIEW`

Decision:
`PASS`

Review audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_AUTHORITY_PROVENANCE_ACQUISITION_PROPOSAL_REVIEW.md`

The PASS approves only the bounded proposal design. It does not create a network execution authorization or permit semantic/runtime changes.

## Next Product Work

Prepare a separate one-shot authority archival execution/authorization artifact while remaining offline.

That artifact must define a fresh explicit human authorization gate before the first authority network request. No previous execution/privacy approval may be reused for that purpose.

## Still Out of Scope

- authority retrieval before the new execution gate;
- additional authority discovery;
- SCO dataset access for this authority task;
- parser, regex, casing, trimming or normalization changes;
- another semantic execution;
- source or registry activation;
- production classification activation.
