# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, California SCO source
governance, approval-readiness evidence, and the transport-preflight proposal are canonical and CI
verified on `m2-state-governance-core`.

Streamlit Community Cloud is the only active reviewer deployment target represented by repository
runtime configuration. Repository-side Vercel deployment integration is decommissioned under D-007.
The reviewer read contract is provider-neutral version `2.0.0`.

The external Vercel account was reported deleted by the owner before the SCO transport execution.
On the post-execution evidence commit GitHub reported no external commit-status contexts, so no Vercel
status reappeared during this candidate work.

A separately owner-authorized California SCO metadata-only transport preflight has now been executed
on candidate branch `m3-ca-sco-transport-preflight-execution`. The execution used `HEAD` only against
the discovered download endpoint, read `0` response-body bytes, persisted no dataset artifact, and
processed no real PII. The candidate observation is CI verified but is **not yet canonical**.

The California SCO source remains `enabled: false` and `approved_for_use: false`. The source-access
policy remains `PROPOSED`, with real acquisition, beneficiary matching, outreach and PII processing
unauthorized.

`main` remains unchanged at `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.
Supabase remains untouched.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 versioned machine contracts and A00-A23 registry.
- M2 deterministic state/governance core, budget ledger and SHA-256 audit chain.
- M3 California source/legal readiness and fail-closed A01 acquisition boundary.
- M3 immutable SHA-256 raw persistence and deterministic provenance records.
- M3 privacy/data-minimization gate with trusted policy separated from caller context.
- Streamlit reviewer canonical, CI verified and remotely validated.
- California SCO source registry canonical, disabled and not approved.
- `SourceAccessGovernance` v1, `SourceApprovalReadiness` v1 and
  `SourceTransportPreflightProposal` v1 canonical.
- Repository-side Vercel runtime/deploy configuration decommissioned and CI-guarded.
- Reviewer contract upgraded to v2.0.0 to remove provider-specific state.
- `SourceTransportPreflightExecution` v1 candidate contract implemented.
- One bounded SCO metadata-only preflight executed after targeted contract tests passed.
- Real transport observation persisted as candidate evidence.
- Temporary one-shot network workflow removed immediately after observation.
- Candidate contract tests prove the observation cannot claim response-body access, dataset
  acquisition, source approval/enablement, PII processing, matching, or outreach.

## California SCO Transport Observation

Owner execution approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

Execution workflow run:
`34838890387` — targeted validation PASS, one-time preflight PASS.

Execution commit:
`7d89ec664992a30b5270be8da4c2616254747e59`.

Evidence commit:
`2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`.

Evidence candidate CI:
`34839100497` — PASS (`quality` + `streamlit-candidate`).

Observed at `2026-09-14T11:34:58.210154Z`:

- official source page: `https://www.sco.ca.gov/upd_download_property_records.html`;
- selected link label: `All properties`;
- discovered endpoint: `https://claimit.ca.gov/upd-property-records/00_All_Records.zip`;
- method: `HEAD`;
- final host: `claimit.ca.gov`;
- HTTP status: `200`;
- redirects: `0`;
- TLS: `https`;
- content type: `application/zip`;
- content length: `3,203,972,130` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"0ce16eb75bbbe7018639c7a71e802008"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:37 GMT`;
- response-body bytes read: `0`.

The public SCO page describes the downloadable records as CSV data, but the current `All properties`
transport resource is a ZIP endpoint advertising `application/zip`. The ZIP body was not downloaded
or opened, so its contents, CSV layout, columns and row schema remain unverified.

## Verification Evidence

- SCO governance SHA: `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO approval-readiness SHA: `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- SCO transport-preflight proposal SHA: `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`.
- Transport-preflight proposal canonical CI `34835032368`: PASS.
- Vercel-decommission canonical CI `34836845879`: PASS.
- SCO preflight execution run `34838890387`: PASS.
- SCO execution evidence candidate CI `34839100497`: PASS.
- Ruff: PASS.
- mypy: PASS.
- contract tests: PASS.
- smoke tests: PASS.
- full pytest: PASS.
- legacy frontend lint/typecheck/build: PASS.
- Streamlit safety/startup smoke: PASS.
- Source registry approved real sources: `0`.
- No dataset body downloaded, persisted or parsed.
- No real PII processed.
- No beneficiary matching or outreach performed.

## Blocked / Not Authorized

- Promoting the SCO execution/evidence candidate into canonical without explicit owner approval.
- Any additional request to the observed SCO download endpoint under the consumed execution approval.
- Real California acquisition or ZIP download.
- Moving the SCO source-access policy from `PROPOSED` to `APPROVED` without a separate human gate.
- Enabling the SCO registry entry for real use.
- Inspecting or parsing ZIP/CSV contents before a separately authorized retrieval gate.
- Inventing California CSV row assumptions or field names.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Reintroducing Vercel repository/runtime deployment integration without a new explicit owner decision.
- Promotion to `main` without a separate stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Known Issues / Unresolved Readiness Items

Resolved by the candidate metadata preflight:

- exact current `All properties` endpoint;
- request method used for the bounded preflight;
- bounded timeout and redirect limit used for the preflight;
- preflight host allowlist;
- execution approval reference;
- observed HTTP status, final host, media type and content length.

Still unresolved:

- a safe/approved maximum size for any future real acquisition;
- production retention/privacy/data-minimization controls;
- authorized processing purpose, data categories and minimized fields;
- PII necessity determination;
- source policy approval and registry activation;
- ZIP contents and actual CSV row/field layout;
- artifact content hash/revision from an authorized real download;
- filesystem raw immutability is application-level, not provider WORM/object lock;
- durable production audit persistence;
- physical retention enforcement and first PostgreSQL/Alembic application migration;
- known non-blocking dependency/runtime deprecation warnings.

## Next Recommended Action

**Human gate:** decide whether to promote candidate branch
`m3-ca-sco-transport-preflight-execution` into canonical `m2-state-governance-core`.

Promotion would record the already-completed metadata observation only. It would **not** approve the
source or authorize a ZIP/CSV download. After any approved promotion, the next source-governance work
must remain proposal/readiness work until a separate owner gate explicitly authorizes source approval
and/or bounded real retrieval.
