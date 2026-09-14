# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | SOURCE GOVERNANCE CANONICAL + CI VERIFIED — REAL ACQUISITION BLOCKED | SCO candidate registered disabled/unapproved; source-access policy `PROPOSED`; candidate run `34825751270` and canonical run `34826353694` PASS |
| M3 Product Visibility — Operations Console | CANONICAL + CI VERIFIED + REMOTE/VISUAL SMOKE PASS + DEPLOY BRANCH ALIGNED | Streamlit Community Cloud confirmed by owner on `m2-state-governance-core`; prior remote functional/visual smoke PASS |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source represented in the registry as a disabled, not-approved candidate.
- Versioned `SourceAccessGovernance` contract implemented.
- SCO source-access policy is canonical in `PROPOSED`, explicitly non-authorizing state.
- Contract tests prove that a proposed policy cannot authorize real acquisition and approved real
  source count remains zero.
- No real source data has been downloaded, parsed or normalized.

## Product visibility state

Streamlit Community Cloud is the active M3 reviewer host. The owner confirmed the deployed app is
configured on canonical `m2-state-governance-core`. The reviewer remains synthetic/read-only and
fails closed on unsafe state. Vercel/Next.js remains rollback/history only.

## Governance verification

California SCO governance SHA:
`463c6d6c972fa955a8aa0d3c97208c3029e202a8`

- Candidate GitHub Actions run `34825751270`: PASS.
- Canonical post-promotion run `34826353694`: PASS.
- Ruff PASS.
- mypy PASS.
- contract tests PASS.
- smoke tests PASS.
- full pytest PASS.
- frontend lint/typecheck/build PASS.
- Streamlit safety/startup smoke PASS.
- real approved sources: `0`.
- real acquisition: BLOCKED.
- beneficiary matching: BLOCKED.

## Next gate — approval-readiness evidence only

Build a bounded, machine-readable approval-readiness evidence package for
`ca.sco.unclaimed_property.bulk`.

It may record facts verified from official public pages, including:

- the official SCO bulk-download page;
- advertised `.CSV` format;
- advertised Thursday update cadence;
- the fact that the download links shown on the official SCO page point to `claimit.ca.gov`;
- public-records and SCO privacy-policy references;
- applicable downstream legal-review references.

It must explicitly record unresolved items and must not:

- follow or download a real CSV;
- mark the source approved or enabled;
- set an approval reference;
- authorize a processing purpose;
- authorize data categories/fields or real PII;
- infer CSV row layout;
- enable beneficiary matching or outreach.

## Still required before any real California acquisition

1. approval-readiness evidence package completed and CI verified;
2. exact transport behavior, content type, size bounds and redirect policy established through a
   separately authorized preflight;
3. production retention/privacy/data-minimization controls defined;
4. explicit human approval of a versioned real-source governance policy and registry activation;
5. bounded read-only retrieval implementation with transport/size/timeout/content validation;
6. a separately authorized California spike;
7. actual CSV layout verified from authorized evidence before A02 normalization;
8. beneficiary matching remains blocked until later privacy/legal/matching gates are satisfied.

## Out of scope until later gates

- real California acquisition before explicit source/policy approval;
- real-data beneficiary matching;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access;
- promotion to `main` without a separate explicit stable-checkpoint gate.
