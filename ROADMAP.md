# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | SOURCE GOVERNANCE + APPROVAL READINESS + TRANSPORT PREFLIGHT PROPOSAL CANONICAL + CI VERIFIED — REAL ACQUISITION BLOCKED | SCO registry disabled/unapproved; policy `PROPOSED`; readiness evidence and transport proposal non-authorizing; canonical CI `34835032368` PASS |
| M3 Product Visibility — Operations Console | CANONICAL + CI VERIFIED + REMOTE/VISUAL SMOKE PASS + DEPLOY BRANCH ALIGNED | Streamlit Community Cloud confirmed by owner on `m2-state-governance-core`; prior remote functional/visual smoke PASS |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source represented in the registry as a disabled, not-approved candidate.
- Versioned `SourceAccessGovernance` contract implemented.
- SCO source-access policy is canonical in `PROPOSED`, explicitly non-authorizing state.
- Versioned `SourceApprovalReadiness` contract and SCO readiness evidence package implemented.
- Versioned `SourceTransportPreflightProposal` contract and SCO transport-preflight proposal implemented.
- Proposal tests prove network execution remains unauthorized, no request/acquisition is claimed,
  response-body bytes remain zero, and source approval/enablement/PII/matching/outreach remain blocked.
- No real source data has been downloaded, parsed or normalized.
- No transport-preflight request has been executed against a download endpoint.

## Product visibility state

Streamlit Community Cloud is the active M3 reviewer host. The owner confirmed the deployed app is
configured on canonical `m2-state-governance-core`. The reviewer remains synthetic/read-only and
fails closed on unsafe state. Vercel/Next.js remains rollback/history only.

## Verification

California SCO governance SHA:
`463c6d6c972fa955a8aa0d3c97208c3029e202a8`

Approval-readiness SHA:
`73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`

Transport-preflight proposal SHA:
`171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`

- Governance candidate CI `34825751270`: PASS.
- Governance canonical CI `34826353694`: PASS.
- Approval-readiness candidate CI `34827272138`: PASS.
- Approval-readiness canonical CI `34828513676`: PASS.
- Transport-preflight proposal candidate CI `34832293876`: PASS.
- Transport-preflight proposal canonical CI `34835032368`: PASS.
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

## Next gate — explicit owner decision on one metadata-only transport preflight

The next action is a human gate, not an automatic implementation step.

The owner may approve or reject one bounded California SCO transport-preflight execution. If approved,
the execution task must be isolated and must remain within the canonical proposal constraints:

- metadata observation only;
- exact endpoint/method/timeout/redirect/allowlist values established explicitly for that task;
- `response_body_bytes_allowed = 0`;
- no response-body persistence or parsing;
- no dataset-artifact persistence;
- no real PII processing;
- no beneficiary matching or outreach;
- source remains unapproved/disabled unless a later separate gate changes that state.

A successful metadata-only preflight would establish transport evidence only. It would not approve the
source or authorize real acquisition.

## Still required before any real California acquisition

1. transport-preflight proposal completed and CI verified — DONE;
2. separately owner-authorized metadata-only transport preflight establishing endpoint/redirect/
   content-type/size evidence;
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
