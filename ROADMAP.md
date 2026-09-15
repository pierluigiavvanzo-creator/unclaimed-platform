# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `$500+` STRUCTURE + TWO-FIELD PRIVACY READINESS CANONICAL — SOURCE APPROVAL BLOCKED | Canonical `9c2f5b6c...`; post-promotion CI `34940817455` SUCCESS; policy `PROPOSED`; registry disabled/unapproved |
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
- Field/privacy readiness reviewed against official SCO property-type codes and current privacy references.
- First-purpose persisted scope reduced to `PROPERTY_ID` + `PROPERTY_TYPE`.
- `HOLDER_NAME` removed from the first triage allowlist.
- Transient CSV prohibited-field exposure recorded as a separate privacy boundary.
- Unjustified 7-day projected-record retention candidate removed; projected retention remains unresolved.
- Candidate promoted by non-force fast-forward to canonical `m2-state-governance-core`.
- Canonical post-promotion CI is green.

## Canonical Two-Field Boundary

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Canonical proposed persisted/allowed scope:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

Optional fields: none.

`HOLDER_NAME` and owner/holder identity/address fields are prohibited for this first purpose.

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

## Canonical Verification

Promoted HEAD:
`9c2f5b6c82ed787bf0820bdd850e475775fc097c`.

Canonical CI:
`34940817455` — SUCCESS.

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

Create an isolated, non-authorizing **`PROPERTY_TYPE` semantic-verification proposal**.

The proposal must:
1. define the exact semantic question to verify;
2. use the existing `$500+` transport and structure evidence only as input;
3. define explicit row, request and byte caps before any execution;
4. define transient-buffer handling and immediate disposal;
5. prohibit raw ZIP/full-row persistence;
6. prohibit use/persistence of nonallowlisted values;
7. define deterministic stop conditions for malformed/unexpected rows, transport drift or privacy ambiguity;
8. remain non-executable and non-authorizing until a separate human gate.

No real row should be read merely to prepare this proposal.

## Still Required Before Real Acquisition

- trusted privacy policy;
- approved production retention policy;
- transient full-row privacy review;
- approved `PROPERTY_TYPE` semantic-verification plan;
- real-acquisition client review;
- explicit source-approval reference;
- source policy `APPROVED` under separate gate;
- registry activation under separate gate;
- separately authorized row-level acquisition;
- A02 normalization against approved fields only.

## Out of Scope Until Later Gates

- reading a real row now;
- using owner or holder identity/address data for first triage;
- beneficiary matching;
- genealogy;
- outreach;
- claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
