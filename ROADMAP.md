# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `$500+` STRUCTURE CANONICAL; TWO-FIELD PRIVACY READINESS CANDIDATE VERIFIED — SOURCE APPROVAL BLOCKED | Candidate `648b81b9...`; CI `34939909880` SUCCESS; policy `PROPOSED`; registry disabled/unapproved |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; repository-side Vercel integration decommissioned |

## Completed M3 readiness work

- California source/legal inventory complete.
- A01 contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- Transport, approval-readiness, data-scope and segmented evidence contracts CI verified.
- `$500+` selected as initial value-segment pilot.
- Bounded structure inspection executed and canonicalized with zero CSV data rows sampled.
- 25 source labels verified across all four CSV members.
- Current field/privacy candidate reviewed against official SCO property-type codes and current CPPA references.

## Current Candidate — Key Result

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Proposed persisted/allowed scope reduced from three fields to two:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

`HOLDER_NAME` is prohibited for this first purpose.

Official SCO/NAUPA documentation defines insurance property codes `IN01-IN08` and `IN99`. The bulk CSV field is not yet assumed to use those values until a separately authorized bounded semantic check verifies row-level compatibility.

## Privacy / Retention Boundary

The source is CSV. There is no established server-side column projection, so any future row read may transiently expose prohibited owner/holder bytes before projection.

Therefore:
- row access remains BLOCKED;
- raw ZIP persistence prohibited;
- full-row persistence prohibited;
- nonallowlisted values may not be used or persisted;
- separate transient-row privacy review is required.

Retention:
- transient row buffers: `0 days`, immediate disposal;
- projected two-field triage retention: unresolved;
- no production duration is invented;
- retention policy remains unapproved.

Privacy policy remains draft/not trusted.

## Functional Verification

Candidate branch:
`m3-ca-sco-field-privacy-readiness`

Functional HEAD:
`648b81b973a4b169c14bcdfd76ac4fa71e76f2e9`

CI:
`34939909880` — SUCCESS.

Passed:
- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- frontend lint/typecheck/build;
- Streamlit safety/startup smoke.

## Current Safety State

- source policy `PROPOSED`;
- real acquisition false;
- registry disabled/unapproved;
- approved real sources `0`;
- CSV row access BLOCKED;
- PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Next Product Work

1. Human/legal review of the transient CSV processing boundary and the revised two-field minimization.
2. If accepted, promote the candidate to `m2-state-governance-core` as **non-authorizing**.
3. After a separate explicit gate, design a bounded `PROPERTY_TYPE` semantic-verification proposal; do not execute it automatically.
4. Only after privacy/retention/source approval gates are resolved, implement reviewed real acquisition and A02 normalization against approved fields.

## Still Required Before Real Acquisition

- trusted privacy policy;
- approved production retention policy;
- transient full-row privacy review;
- approved `PROPERTY_TYPE` semantic-verification plan;
- real-acquisition client review;
- explicit source-approval reference;
- source policy `APPROVED` under separate gate;
- registry activation under separate gate;
- separately authorized row-level acquisition.

## Out of Scope Until Later Gates

- reading a real row now;
- using owner or holder identity/address data for first triage;
- beneficiary matching;
- genealogy;
- outreach;
- claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
