# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | TRANSPORT PREFLIGHT EVIDENCE CANDIDATE + CI VERIFIED — REAL ACQUISITION BLOCKED | Canonical proposal remains non-authorizing; one metadata-only `HEAD` preflight completed; evidence candidate CI `34839100497` PASS; registry disabled/unapproved; policy `PROPOSED` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE + REPOSITORY-SIDE VERCEL INTEGRATION DECOMMISSIONED + CI VERIFIED | Reviewer contract v2.0.0; Streamlit active; no Vercel status reappeared on the SCO evidence commit |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented.
- California SCO public bulk source represented in the registry as a disabled, not-approved candidate.
- Versioned `SourceAccessGovernance`, `SourceApprovalReadiness`, and
  `SourceTransportPreflightProposal` contracts implemented and canonical.
- SCO source-access policy remains canonical in `PROPOSED`, explicitly non-authorizing state.
- Repository-side Vercel runtime/deployment support decommissioned and CI-guarded.
- Versioned `SourceTransportPreflightExecution` candidate contract implemented.
- Owner-authorized metadata-only preflight executed after targeted contract tests passed.
- Exact transport observation persisted as candidate evidence.
- Temporary one-shot execution workflow removed after the observation.
- No source body, dataset artifact, ZIP or CSV was downloaded/persisted/parsed.
- No real PII, beneficiary matching or outreach occurred.

## California SCO transport evidence candidate

Owner approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

Execution workflow run:
`34838890387` — PASS.

Execution commit:
`7d89ec664992a30b5270be8da4c2616254747e59`.

Evidence commit:
`2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`.

Evidence CI:
`34839100497` — PASS.

Observed transport facts:

- `All properties` endpoint: `https://claimit.ca.gov/upd-property-records/00_All_Records.zip`;
- method: `HEAD`;
- HTTP `200`;
- final host `claimit.ca.gov`;
- no redirect observed;
- HTTPS;
- `Content-Type: application/zip`;
- `Content-Length: 3,203,972,130` bytes;
- `Accept-Ranges: bytes`;
- ETag `"0ce16eb75bbbe7018639c7a71e802008"`;
- Last-Modified `Wed, 09 Sep 2026 16:32:37 GMT`;
- response-body bytes read `0`.

The public source page describes downloadable CSV records, but the observed `All properties` resource
is currently a ZIP transport object. Its body was not opened, so ZIP contents, CSV files, row layout,
columns and schema remain unverified.

## Product visibility and deployment state

Streamlit Community Cloud remains the active M3 reviewer host on canonical
`m2-state-governance-core`. Repository-side Vercel deployment support remains decommissioned under
D-007. The owner reported the Vercel account deleted before the transport task, and no external Vercel
commit status appeared on evidence commit `2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`.

## Verification

- SCO governance SHA `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO approval-readiness SHA `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- SCO transport-preflight proposal SHA `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`.
- Transport-preflight proposal canonical CI `34835032368`: PASS.
- Vercel decommission canonical CI `34836845879`: PASS.
- SCO one-time preflight run `34838890387`: PASS.
- SCO execution evidence candidate CI `34839100497`: PASS.
- Ruff PASS.
- mypy PASS.
- contract tests PASS.
- smoke tests PASS.
- full pytest PASS.
- legacy frontend lint/typecheck/build PASS.
- Streamlit safety/startup smoke PASS.
- real approved sources: `0`.
- real acquisition: BLOCKED.
- beneficiary matching: BLOCKED.

## Next gate — promote transport evidence candidate

The next action is a human promotion gate, not another network action.

The owner may approve or reject promotion of:

`m3-ca-sco-transport-preflight-execution` → `m2-state-governance-core`.

Promotion would carry the versioned execution contract, runner, tests, audit and observed metadata
evidence into canonical history. The one-shot workflow has already been removed and must remain absent.

Promotion does **not** authorize:

- another transport request;
- source policy `APPROVED` status;
- registry activation;
- a ZIP/CSV download;
- archive inspection;
- real-data parsing/normalization;
- PII processing;
- beneficiary matching or outreach.

## Still required before any real California acquisition

1. transport-preflight proposal completed and CI verified — DONE;
2. owner-authorized metadata-only transport preflight — DONE ON CANDIDATE;
3. promote verified transport evidence if owner approves — PENDING HUMAN GATE;
4. production retention/privacy/data-minimization controls defined;
5. explicit human approval of a versioned real-source governance policy and registry activation;
6. bounded read-only retrieval implementation with explicit maximum-size/content/timeout controls;
7. a separately authorized California retrieval spike;
8. archive/CSV layout verified from authorized evidence before A02 normalization;
9. beneficiary matching remains blocked until later privacy/legal/matching gates are satisfied.

## Out of scope until later gates

- any additional SCO download-endpoint request under the consumed preflight approval;
- real California acquisition before explicit source/policy approval;
- ZIP/CSV body download or parsing without a separate gate;
- real-data beneficiary matching;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access;
- reintroduction of Vercel repository/runtime support without a new owner decision;
- promotion to `main` without a separate stable-checkpoint gate.
