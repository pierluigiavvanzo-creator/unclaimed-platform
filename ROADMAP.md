# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | SOURCE GOVERNANCE + APPROVAL READINESS + TRANSPORT PREFLIGHT PROPOSAL CANONICAL + CI VERIFIED — REAL ACQUISITION BLOCKED | SCO registry disabled/unapproved; policy `PROPOSED`; transport proposal non-authorizing; canonical CI `34835032368` PASS |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + REPOSITORY-SIDE VERCEL INTEGRATION DECOMMISSIONED + CI VERIFIED | Reviewer contract v2.0.0; decommission canonical CI `34836845879` PASS; Streamlit remains active reviewer target |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source represented in the registry as a disabled, not-approved candidate.
- Versioned `SourceAccessGovernance`, `SourceApprovalReadiness`, and
  `SourceTransportPreflightProposal` contracts implemented.
- SCO source-access policy remains canonical in `PROPOSED`, explicitly non-authorizing state.
- Proposal tests prove network execution remains unauthorized, response-body bytes remain zero, and
  source approval/enablement/PII/matching/outreach remain blocked.
- No real source data has been downloaded, parsed or normalized.
- No transport-preflight request has been executed against a download endpoint.

## Product visibility and deployment state

Streamlit Community Cloud is the active M3 reviewer host on canonical `m2-state-governance-core`.
Repository-side Vercel deployment support has been explicitly decommissioned under D-007:

- `apps/reviewer-console/vercel.json` removed;
- provider-specific deployment instructions removed from active app documentation;
- provider-specific platform field removed from API/JSON Schema/legacy frontend contract;
- reviewer read contract bumped to v2.0.0 because the field removal is a breaking contract change;
- legacy Next.js reviewer retained only as provider-neutral local/regression code;
- contract guardrail rejects future Vercel paths/references in active runtime/configuration surfaces.

The initial guardrail run `34836335576` failed as intended after finding residual references. Those
references were removed rather than exempted. Corrected candidate CI `34836721955` and canonical CI
`34836845879` both passed all gates.

An external Vercel Git/project connection is outside repository contents. If failed deployment
notifications continue, that external connection must be disconnected separately; no repository file
can revoke an account-level provider integration.

## Verification

- SCO governance SHA `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO approval-readiness SHA `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- SCO transport-preflight proposal SHA `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`.
- Transport-preflight proposal candidate CI `34832293876`: PASS.
- Transport-preflight proposal canonical CI `34835032368`: PASS.
- Vercel decommission corrected candidate CI `34836721955`: PASS.
- Vercel decommission canonical CI `34836845879`: PASS.
- Ruff, mypy, contract tests, smoke tests, full pytest: PASS.
- Legacy frontend lint/typecheck/build: PASS.
- Streamlit safety/startup smoke: PASS.
- real approved sources: `0`.
- real acquisition: BLOCKED.
- beneficiary matching: BLOCKED.

## Immediate operational gate — external deployment notification cleanup

Before resuming California transport execution, verify that failed-deployment notifications have
stopped. If they continue, disconnect any external Vercel project/Git integration associated with the
repository. This is an external provider/account action, not a repository code change.

## Next product gate — explicit owner decision on one metadata-only transport preflight

After the notification issue is resolved, the next product action remains a human gate. The owner may
approve or reject one bounded California SCO transport-preflight execution. If approved, the task must
remain within the canonical proposal constraints:

- metadata observation only;
- exact endpoint/method/timeout/redirect/allowlist values established explicitly for that task;
- `response_body_bytes_allowed = 0`;
- no response-body persistence or parsing;
- no dataset-artifact persistence;
- no real PII processing;
- no beneficiary matching or outreach;
- source remains unapproved/disabled unless a later separate gate changes that state.

A successful metadata-only preflight establishes transport evidence only. It does not approve the
source or authorize real acquisition.

## Still required before any real California acquisition

1. transport-preflight proposal completed and CI verified — DONE;
2. separately owner-authorized metadata-only transport preflight;
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
- reintroduction of Vercel repository/runtime deployment support without a new explicit owner decision;
- promotion to `main` without a separate explicit stable-checkpoint gate.
