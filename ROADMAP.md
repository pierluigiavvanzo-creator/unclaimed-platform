# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | DATA-SCOPE INSPECTION PROPOSAL CANDIDATE + CI VERIFIED — EXECUTION BLOCKED | Candidate `2df97f9d...`; CI `34855459255` PASS; policy `PROPOSED`; registry disabled/unapproved |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + REPOSITORY-SIDE VERCEL INTEGRATION DECOMMISSIONED | Reviewer contract v2.0.0; Streamlit active; no Vercel runtime integration in repository |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source registered as disabled and not approved.
- `SourceAccessGovernance`, `SourceApprovalReadiness`, `SourceTransportPreflightProposal`,
  `SourceTransportPreflightExecution`, and `SourceApprovalPackage` contracts canonical.
- Owner-authorized metadata-only transport preflight executed and promoted.
- Exact transport observation is canonical.
- Non-authorizing source-approval readiness package is canonical and CI verified.
- No ZIP/CSV body, record values, PII, beneficiary matching or outreach has occurred.

## Current candidate — non-authorizing data-scope inspection proposal

Candidate branch:
`m3-ca-sco-data-scope-inspection-proposal`

Functional commit:
`2df97f9dbab16ba0e30ec07a590657b381eb8c8b`

Candidate CI:
`34855459255` — PASS for `quality` and `streamlit-candidate`.

Pre-closure compare against canonical:

- 1 commit ahead;
- 0 behind;
- exact merge-base `c832b447cbe37482fdc4273eb1b163ce9299edf3`;
- exactly five added proposal/test/audit files;
- no policy, registry, runtime adapter, script or network workflow modified/added.

The proposal defines a future separately authorized structure-only inspection with:

- purpose `SOURCE_STRUCTURE_VERIFICATION_ONLY`;
- archive member names/metadata allowed as derived structure evidence;
- CSV first logical record only as a header candidate;
- data rows allowed: `0`;
- record values allowed: `false`;
- PII indicators based on header labels only;
- identity resolution, matching, outreach and downstream record use prohibited;
- HTTP Range GET only; full-body request prohibited;
- quarantine and in-memory-only source-byte processing;
- no raw ZIP/member/header persistence;
- separate execution approval reference required before any body access.

Project safety caps, not source facts:

- tail suffix `131,072` bytes;
- central directory max `4,194,304` bytes;
- archive members max `10,000`;
- CSV candidates max `10`;
- member response prefix max `1,048,576` bytes each;
- decompressed prefix max `65,536` bytes each;
- max range requests `12`;
- max total source response-body bytes `14,811,136`.

The proposal is fail-closed on transport drift, unsupported ranges, unexpected full-body behavior,
structure exceeding caps, unsafe paths, encryption, unsupported compression, ambiguous/incomplete
header candidates, any need to read a data row, or byte/request-budget exhaustion.

## Current safety state

- source-access policy: `PROPOSED`;
- real acquisition authorized: `false`;
- registry `enabled`: `false`;
- registry `approved_for_use`: `false`;
- approved real sources: `0`;
- data-scope proposal execution authorized: `false`;
- execution approval reference: `null`;
- source body bytes read during proposal task: `0`;
- ZIP/CSV range access: BLOCKED;
- CSV data rows: BLOCKED;
- real PII: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED.

## Verification

- canonical source-approval package CI `34853561664`: PASS;
- canonical package closure commit `c832b447cbe37482fdc4273eb1b163ce9299edf3`;
- data-scope proposal candidate CI `34855459255`: PASS;
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- legacy frontend lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

## Next gate — candidate promotion only

The next action is a human promotion decision for:

`m3-ca-sco-data-scope-inspection-proposal` → `m2-state-governance-core`.

Promotion would make the proposal canonical. It does **not** authorize:

- an SCO request;
- a range GET;
- ZIP/CSV body access;
- archive/header inspection;
- source policy `APPROVED` status;
- registry activation;
- data-row or record-value processing;
- PII processing;
- identity resolution, beneficiary matching or outreach.

## Still required before source approval or real California acquisition

1. source-approval readiness package — DONE + CANONICAL;
2. non-authorizing data-scope inspection proposal — CANDIDATE + CI VERIFIED;
3. promotion of the proposal if owner approves;
4. separate owner authorization for bounded structure inspection;
5. verified archive member and CSV header/row-layout evidence;
6. minimized field whitelist selected from verified evidence;
7. PII presence/necessity determination;
8. production retention policy selected;
9. trusted project privacy policy selected;
10. real-acquisition client reviewed against final transport/privacy controls;
11. explicit human source-approval reference;
12. only then consider policy `APPROVED` + registry activation under a separate gate;
13. any real retrieval remains a separate authorization after approval.

## Out of scope until later gates

- executing the current proposal before a separate human gate;
- source approval before blockers are resolved;
- full California acquisition;
- CSV data-row access;
- real-data normalization/matching;
- autonomous outreach;
- claimant verification, fee agreements or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
