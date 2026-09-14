# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | SOURCE-APPROVAL READINESS PACKAGE CANONICAL + CI VERIFIED — SOURCE APPROVAL BLOCKED | Package baseline `41dfc61c...`; canonical CI `34853561664` PASS; policy `PROPOSED`; registry disabled/unapproved |
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
- No response body, ZIP, CSV or dataset artifact has been downloaded/persisted/parsed.
- No real PII, beneficiary matching or outreach has occurred.

## Canonical source-approval readiness package

Promoted package baseline:
`41dfc61cd96d7573cdd67c37631567ef5343fcdd`

Canonical post-promotion CI:
`34853561664` — PASS for `quality` and `streamlit-candidate`.

The package remains explicitly non-authorizing and proposes:

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
- endpoint/media-type/content-length drift requires new review.

The package decision remains `BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION` because ZIP/CSV row layout
is still unknown and the project cannot truthfully select a record-level field whitelist or determine
PII necessity yet.

## Current safety state

- source-access policy: `PROPOSED`;
- real acquisition authorized: `false`;
- registry `enabled`: `false`;
- registry `approved_for_use`: `false`;
- approved real sources: `0`;
- ZIP/CSV download: BLOCKED;
- real PII: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED.

## Verification

- canonical transport preflight CI `34840001821`: PASS;
- canonical transport closure CI `34840291103`: PASS;
- source-approval package candidate CI `34843714665`: PASS;
- source-approval package candidate closure CI `34843990986`: PASS;
- source-approval package canonical CI `34853561664`: PASS;
- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- legacy frontend lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

## Next product action — data-scope inspection proposal only

Create a new isolated candidate for a **non-authorizing California SCO data-scope inspection proposal**.
The proposal should define, without executing a request:

- the minimum archive/CSV structure evidence required to resolve row-layout uncertainty;
- exact byte/range/read limits and stop conditions;
- streaming/no-partial-artifact rules;
- quarantine/privacy controls;
- machine-readable outputs for internal file names, CSV headers/row layout and PII-presence indicators;
- explicit prohibition on matching, identity resolution, outreach and downstream use;
- a separate owner execution approval reference required before any body access.

After proposal tests and CI pass, stop at a human execution gate. Do not perform archive retrieval or
inspection as part of the proposal task.

## Still required before source approval or real California acquisition

1. source-approval readiness package — DONE + CANONICAL;
2. non-authorizing data-scope inspection proposal — NEXT;
3. separately authorized bounded structure inspection;
4. verified ZIP/CSV row layout;
5. minimized field whitelist selected from verified schema;
6. PII presence/necessity determination;
7. production retention policy selected;
8. trusted project privacy policy selected;
9. real-acquisition client reviewed against final transport/privacy controls;
10. explicit human source-approval reference;
11. only then consider policy `APPROVED` + registry activation under a separate gate;
12. any real retrieval remains a separate authorization after approval.

## Out of scope until later gates

- source approval before blockers are resolved;
- real California acquisition;
- ZIP/CSV body access without a separate explicit gate;
- real-data normalization/matching;
- autonomous outreach;
- claimant verification, fee agreements or claim submission;
- reintroduction of Vercel repository/runtime support without a new owner decision;
- promotion to `main` without a separate stable-checkpoint gate.
