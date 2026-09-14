# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | SOURCE GOVERNANCE + APPROVAL READINESS CANONICAL + CI VERIFIED — REAL ACQUISITION BLOCKED | SCO registry disabled/unapproved; policy `PROPOSED`; readiness evidence non-authorizing; canonical CI `34828513676` PASS |
| M3 Product Visibility — Operations Console | CANONICAL + CI VERIFIED + REMOTE/VISUAL SMOKE PASS + DEPLOY BRANCH ALIGNED | Streamlit Community Cloud confirmed by owner on `m2-state-governance-core`; prior remote functional/visual smoke PASS |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source represented in the registry as a disabled, not-approved candidate.
- Versioned `SourceAccessGovernance` contract implemented.
- SCO source-access policy is canonical in `PROPOSED`, explicitly non-authorizing state.
- Versioned `SourceApprovalReadiness` contract implemented.
- SCO approval-readiness evidence package is canonical and records only verified public facts plus
  explicitly unresolved controls.
- Contract tests prove that readiness evidence cannot claim completed acquisition, source approval or
  source enablement.
- No real source data has been downloaded, parsed or normalized.

## Product visibility state

Streamlit Community Cloud is the active M3 reviewer host. The owner confirmed the deployed app is
configured on canonical `m2-state-governance-core`. The reviewer remains synthetic/read-only and
fails closed on unsafe state. Vercel/Next.js remains rollback/history only.

## Verification

California SCO governance SHA:
`463c6d6c972fa955a8aa0d3c97208c3029e202a8`

Approval-readiness SHA:
`73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`

- Governance candidate CI `34825751270`: PASS.
- Governance canonical CI `34826353694`: PASS.
- Approval-readiness candidate CI `34827272138`: PASS.
- Approval-readiness canonical post-promotion CI `34828513676`: PASS.
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

## Next gate — transport-preflight proposal only

Prepare a bounded, isolated proposal describing the later California SCO transport preflight.

The proposal may define the checks that would be required to establish:

- exact download endpoint identity;
- redirect behavior;
- response/content-type metadata;
- size-bound evidence;
- timeout and maximum-byte controls;
- allowlisted host requirements;
- provenance fields for the transport observation.

The proposal itself must not:

- execute a request to a download endpoint;
- follow/download a real CSV;
- persist a real dataset artifact;
- mark the source approved or enabled;
- authorize a processing purpose, data categories/fields or real PII;
- infer CSV row layout;
- enable beneficiary matching or outreach.

Actual execution of the transport preflight requires a separate explicit owner gate.

## Still required before any real California acquisition

1. bounded transport-preflight proposal completed and CI verified;
2. separately authorized transport preflight establishing endpoint/redirect/content-type/size evidence;
3. production retention/privacy/data-minimization controls defined;
4. explicit human approval of a versioned real-source governance policy and registry activation;
5. bounded read-only retrieval implementation with transport/size/timeout/content validation;
6. a separately authorized California spike;
7. actual CSV layout verified from authorized evidence before A02 normalization;
8. beneficiary matching remains blocked until later privacy/legal/matching gates are satisfied.

## Out of scope until later gates

- transport preflight network execution without explicit owner approval;
- real California acquisition before explicit source/policy approval;
- real-data beneficiary matching;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access;
- promotion to `main` without a separate explicit stable-checkpoint gate.
