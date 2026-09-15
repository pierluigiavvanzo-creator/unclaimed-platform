# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` SEMANTIC-VERIFICATION PROPOSAL CANONICAL + CI VERIFIED — EXECUTION BLOCKED | Promoted `06004c9c...`; canonical CI `34943657157` SUCCESS; policy `PROPOSED`; registry disabled/unapproved |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; repository-side Vercel integration decommissioned |

## Completed M3 readiness work

- California source/legal inventory complete.
- A01 contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` transport and bounded structure evidence canonicalized.
- Four CSV members and identical 25-label header verified with zero data rows sampled.
- First-purpose persisted scope reduced to `PROPERTY_ID` + `PROPERTY_TYPE`.
- `HOLDER_NAME` and identity/address fields prohibited for first triage.
- Transient CSV prohibited-field exposure isolated as a separate privacy boundary.
- `PROPERTY_TYPE` semantic-verification proposal created, contract-tested, promoted, and canonical CI verified without network/body access.

## Canonical Semantic Proposal

Promoted SHA:
`06004c9cb61b39692d153d9172c37cebf168ddc5`

Canonical CI:
`34943657157` — SUCCESS.

Canonical proposal files:
- `schemas/common/property_type_semantic_verification_proposal.schema.json`;
- `schemas/examples/ca_sco_500_plus_property_type_semantic_verification.examples.json`;
- `sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`;
- `tests/contract/test_ca_sco_property_type_semantic_verification_proposal.py`;
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL.md`;
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL_VERIFICATION.md`.

No execution runner or network workflow is present.

## Semantic Question

Future bounded check only:

> Are bounded sampled `PROPERTY_TYPE` values NAUPA-style code tokens, and is every observed
> `IN`-prefixed token one of the official SCO insurance codes `IN01-IN08` or `IN99`?

A successful sample does not prove the full dataset domain and does not enable production classification.

## Fixed Proposal Caps

- 4 canonical CSV members;
- first 4 complete data rows/member;
- 16 data rows maximum total;
- 1 HEAD maximum;
- 4 Range GET maximum;
- 5 HTTP requests maximum total;
- `131,072` response-body bytes maximum per Range;
- `524,288` response-body bytes maximum total;
- `1,048,576` uncompressed transient bytes maximum total;
- `32,768` bytes maximum per logical CSV record;
- no full-body request;
- no automatic cap widening.

## Privacy / Persistence Controls

- transient full-row exposure remains possible and separately gated;
- no temporary source files;
- raw ZIP/Range/full-row persistence prohibited;
- `PROPERTY_ID` persistence prohibited during semantic verification;
- nonallowlisted value use/persistence prohibited;
- per-row `PROPERTY_TYPE` persistence prohibited;
- derived `PROPERTY_TYPE` summary only;
- transient buffers retained `0 days` and disposed immediately;
- raw bytes and record values prohibited from logs.

## Current Safety State

- source policy `PROPOSED`;
- real acquisition false;
- registry disabled/unapproved;
- approved real sources `0`;
- semantic execution false;
- CSV row access BLOCKED;
- PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Next Product Work

1. `HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`.
2. Review/design a bounded runner against the canonical caps; do not read real rows during design.
3. Runner implementation, if accepted, must remain non-executing until a separate owner gate.
4. Actual one-shot row access requires separate explicit execution approval and transient-row privacy approval.
5. Source approval, registry activation, A02 normalization, identity, matching and outreach remain later independent gates.

## Out of Scope Until Later Gates

- executing the semantic sample now;
- reading any real row now;
- increasing row/request/byte caps automatically;
- persisting owner/holder values or full rows;
- source approval or registry activation;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
