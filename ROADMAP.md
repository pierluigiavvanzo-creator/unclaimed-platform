# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | SOURCE-APPROVAL PACKAGE CANDIDATE + CI VERIFIED — SOURCE APPROVAL BLOCKED | Candidate `4250291d...`; CI `34843714665` PASS; policy still `PROPOSED`; registry disabled/unapproved |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + REPOSITORY-SIDE VERCEL INTEGRATION DECOMMISSIONED | Reviewer contract v2.0.0; Streamlit active; no Vercel runtime integration in repository |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source registered as disabled and not approved.
- `SourceAccessGovernance`, `SourceApprovalReadiness`, `SourceTransportPreflightProposal` and
  `SourceTransportPreflightExecution` contracts canonical.
- Owner-authorized metadata-only transport preflight executed and promoted.
- Exact transport observation is canonical.
- Temporary one-shot execution workflow removed after the observation.
- No response body, ZIP, CSV or dataset artifact has been downloaded/persisted/parsed.
- No real PII, beneficiary matching or outreach has occurred.

## Current candidate — non-authorizing source-approval package

Candidate branch:
`m3-ca-sco-source-approval-package`

Functional commit:
`4250291d24286be2e0d4cb1a12de0960cc3faa90`

Candidate CI:
`34843714665` — PASS for `quality` and `streamlit-candidate`.

The package reuses canonical transport evidence and proposes, without activating anything:

- processing purpose `SOURCE_STRUCTURE_VERIFICATION_ONLY`;
- high-level category `PUBLIC_UNCLAIMED_PROPERTY_BULK_ARCHIVE`;
- no record-level fields until row schema is verified;
- PII necessity `UNDETERMINED_BLOCKING`, with `allow_pii = false`;
- quarantine, encryption-at-rest, least-privilege and access-logging prerequisites;
- no record-level processing, export, matching or outreach;
- retention policy and trusted project privacy policy required before approval;
- HTTPS-only transport to `claimit.ca.gov`;
- same-host redirects only;
- 10-second per-request network-inactivity timeout;
- expected media type `application/zip`;
- max bytes `3,203,972,130`, exactly the observed content length with no growth tolerance;
- endpoint/media-type/content-length drift requires a new preflight/review.

The package decision is deliberately
`BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION` because ZIP/CSV row layout is still unknown and the
project cannot truthfully select a field whitelist or determine PII necessity yet.

## Current safety state

- source-access policy: `PROPOSED`;
- real acquisition authorized: `false`;
- registry `enabled`: `false`;
- registry `approved_for_use`: `false`;
- approved real sources: `0`;
- new network requests during approval-package task: `0`;
- ZIP/CSV download: BLOCKED;
- real PII: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED.

## Verification

- canonical transport preflight CI `34840001821`: PASS;
- canonical transport closure CI `34840291103`: PASS;
- source-approval package candidate CI `34843714665`: PASS;
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- legacy frontend lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

## Next gate — candidate promotion only

The next action is a human promotion decision for:

`m3-ca-sco-source-approval-package` → `m2-state-governance-core`.

Promotion would make the readiness proposal canonical. It does **not** authorize:

- source policy `APPROVED` status;
- registry activation;
- a new network request;
- ZIP/CSV download or archive inspection;
- record-level processing;
- PII processing;
- beneficiary matching or outreach.

## Still required before source approval or real California acquisition

1. source-approval readiness package promotion if owner approves — PENDING HUMAN GATE;
2. verified ZIP/CSV row layout from separately authorized evidence;
3. minimized field whitelist selected from verified schema;
4. PII presence/necessity determination;
5. production retention policy selected;
6. trusted project privacy policy selected;
7. real-acquisition client reviewed against final transport/privacy controls;
8. explicit human source-approval reference;
9. only then consider policy `APPROVED` + registry activation under a separate gate;
10. any real retrieval remains a separate authorization after approval.

## Out of scope until later gates

- source approval before blockers are resolved;
- real California acquisition;
- ZIP/CSV body access without a separate explicit gate;
- real-data normalization/matching;
- autonomous outreach;
- claimant verification, fee agreements or claim submission;
- reintroduction of Vercel repository/runtime support without a new owner decision;
- promotion to `main` without a separate stable-checkpoint gate.
