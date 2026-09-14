# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | TRANSPORT PREFLIGHT EVIDENCE CANONICAL + CI VERIFIED — REAL ACQUISITION BLOCKED | Metadata-only `HEAD` preflight canonical; canonical CI `34840001821` PASS; registry disabled/unapproved; policy `PROPOSED` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + REPOSITORY-SIDE VERCEL INTEGRATION DECOMMISSIONED | Reviewer contract v2.0.0; Streamlit active; no Vercel runtime integration in repository |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source registered as disabled and not approved.
- Versioned `SourceAccessGovernance`, `SourceApprovalReadiness`,
  `SourceTransportPreflightProposal` and `SourceTransportPreflightExecution` contracts canonical.
- Owner-authorized metadata-only transport preflight executed after targeted tests passed.
- Exact transport observation promoted into canonical history.
- Temporary one-shot execution workflow removed after the observation.
- No response body, ZIP, CSV, or dataset artifact was downloaded/persisted/parsed.
- No real PII, beneficiary matching or outreach occurred.

## Canonical transport evidence

Promoted baseline:
`60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a`

Canonical post-promotion CI:
`34840001821` — PASS for `quality` and `streamlit-candidate`.

Observed transport facts:

- endpoint: `https://claimit.ca.gov/upd-property-records/00_All_Records.zip`;
- method: `HEAD`;
- HTTP `200`;
- final host `claimit.ca.gov`;
- redirects `0`;
- HTTPS;
- `Content-Type: application/zip`;
- `Content-Length: 3,203,972,130` bytes;
- `Accept-Ranges: bytes`;
- ETag `"0ce16eb75bbbe7018639c7a71e802008"`;
- Last-Modified `Wed, 09 Sep 2026 16:32:37 GMT`;
- response-body bytes read `0`.

The public source page describes downloadable CSV records, but the observed `All properties` resource
is currently a ZIP transport object. Its body was not opened, so archive contents, CSV layout, columns
and row schema remain unknown.

## Product visibility and deployment state

Streamlit Community Cloud remains the active M3 reviewer host on canonical
`m2-state-governance-core`. Repository-side Vercel deployment support remains decommissioned under
D-007. Reintroduction requires a new explicit owner decision.

## Verification

- SCO governance SHA `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO approval-readiness SHA `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- SCO transport-preflight proposal SHA `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`.
- SCO one-time preflight run `34838890387`: PASS.
- Candidate evidence CI `34839100497`: PASS.
- Candidate closure CI `34839373665`: PASS.
- Canonical post-promotion CI `34840001821`: PASS.
- Ruff, mypy, contract tests, smoke tests, full pytest: PASS.
- Legacy frontend lint/typecheck/build: PASS.
- Streamlit safety/startup smoke: PASS.
- real approved sources: `0`.
- real acquisition: BLOCKED.
- beneficiary matching: BLOCKED.

## Next product action — source-approval readiness package only

Create a new isolated candidate from canonical for a **non-authorizing California SCO source-approval
readiness package**. Reuse the canonical transport evidence and propose, without activating anything:

- explicit permitted processing purpose;
- permitted data categories;
- minimized allowed fields;
- PII necessity decision evidence;
- privacy and retention controls;
- safe maximum acquisition size;
- timeout/redirect/host/media-type transport policy;
- evidence required for an eventual approval reference.

The package must keep:

- source policy `PROPOSED`;
- registry `enabled: false` and `approved_for_use: false`;
- real acquisition unauthorized;
- network execution absent;
- ZIP/CSV body access absent;
- PII processing, beneficiary matching and outreach blocked.

After tests and CI pass, stop at an explicit human source-approval gate.

## Still required before any real California acquisition

1. transport-preflight proposal — DONE;
2. bounded metadata-only transport preflight — DONE;
3. canonical promotion of transport evidence — DONE;
4. non-authorizing source-approval readiness package — NEXT;
5. production retention/privacy/data-minimization controls defined and reviewed;
6. explicit owner approval of a versioned real-source governance policy and registry activation;
7. bounded read-only retrieval implementation with explicit size/content/timeout controls;
8. separately authorized California retrieval spike;
9. archive/CSV layout verified from authorized evidence before A02 normalization;
10. beneficiary matching remains blocked until later privacy/legal/matching gates.

## Out of scope until later gates

- any additional SCO download-endpoint request under the consumed preflight approval;
- real California acquisition before source/policy approval;
- ZIP/CSV download or parsing without a separate gate;
- real-data beneficiary matching;
- autonomous outreach;
- legal determinations;
- claimant verification, fee agreements or claim submission;
- unapproved scraping or restricted-source access;
- Vercel repository/runtime reintroduction without a new owner decision;
- promotion to `main` without a separate stable-checkpoint gate.
