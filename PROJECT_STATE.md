# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, California SCO source
governance, approval-readiness evidence, transport-preflight proposal, and the bounded transport
preflight execution/evidence are now canonical and CI verified on `m2-state-governance-core`.

The verified transport-evidence baseline SHA is
`60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a`.
Canonical post-promotion CI run `34840001821` passed both `quality` and `streamlit-candidate`.

Streamlit Community Cloud remains the active reviewer deployment target. Repository-side Vercel
runtime/deployment integration remains decommissioned and CI guarded. The reviewer read contract is
provider-neutral version `2.0.0`.

The California SCO source remains `enabled: false` and `approved_for_use: false`. The source-access
policy remains `PROPOSED`; real acquisition, PII processing, beneficiary matching and outreach remain
unauthorized.

`main` remains unchanged at `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.
Supabase remains untouched.

## Canonical California SCO Transport Evidence

Owner execution approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

One-shot execution workflow run:
`34838890387` — targeted validation PASS, bounded metadata preflight PASS.

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

The public SCO page describes downloadable records as CSV data, but the observed `All properties`
transport object is currently a ZIP resource advertising `application/zip`. The archive body was not
downloaded or opened, so archive contents, CSV files, fields, row layout and schema remain unverified.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 versioned machine contracts and A00-A23 registry.
- M2 deterministic state/governance core, budget ledger and SHA-256 audit chain.
- M3 California source/legal readiness and fail-closed A01 acquisition boundary.
- M3 immutable SHA-256 raw persistence and deterministic provenance records.
- M3 privacy/data-minimization gate with trusted policy separated from caller context.
- Streamlit reviewer canonical, CI verified and remotely validated.
- California SCO source registry canonical, disabled and not approved.
- `SourceAccessGovernance` v1, `SourceApprovalReadiness` v1,
  `SourceTransportPreflightProposal` v1 and `SourceTransportPreflightExecution` v1 canonical.
- One bounded SCO metadata-only `HEAD` preflight completed with `0` response-body bytes.
- Machine-readable transport observation canonical.
- Temporary one-shot network workflow removed and guarded against reintroduction.
- Repository-side Vercel runtime/deploy configuration decommissioned and CI guarded.

## Verification Evidence

- SCO governance SHA: `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO approval-readiness SHA: `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- SCO transport-preflight proposal SHA: `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`.
- SCO execution commit: `7d89ec664992a30b5270be8da4c2616254747e59`.
- SCO evidence commit: `2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`.
- Promoted transport-evidence baseline: `60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a`.
- One-shot preflight run `34838890387`: PASS.
- Candidate evidence CI `34839100497`: PASS.
- Candidate closure CI `34839373665`: PASS.
- Canonical post-promotion CI `34840001821`: PASS.
- Ruff, mypy, contract tests, smoke tests, full pytest: PASS.
- Legacy frontend lint/typecheck/build: PASS.
- Streamlit safety/startup smoke: PASS.
- Approved real sources: `0`.
- No dataset body downloaded, persisted or parsed.
- No real PII processed.
- No beneficiary matching or outreach performed.

## Blocked / Not Authorized

- Any additional request to the SCO download endpoint under the consumed preflight approval.
- Real California acquisition or ZIP download.
- Source policy transition from `PROPOSED` to `APPROVED` without a separate owner gate.
- SCO registry activation for real use.
- ZIP/CSV inspection or parsing before a separately authorized retrieval gate.
- Invented California CSV field/row assumptions.
- Real PII processing, beneficiary matching or outreach.
- Claimant verification, fee agreements or claim submission.
- Reintroduction of Vercel repository/runtime deployment integration without a new owner decision.
- Promotion to `main` without a separate stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Remaining Readiness Gaps

- safe maximum bytes for any future real acquisition;
- production retention/privacy/data-minimization controls;
- authorized processing purpose;
- authorized data categories and minimized fields;
- PII necessity determination;
- explicit source-policy approval and registry activation;
- ZIP contents and actual CSV row/field layout;
- artifact hash/revision from a separately authorized real download;
- durable production audit persistence;
- physical retention enforcement and first PostgreSQL/Alembic application migration.

## Next Recommended Action

Create an isolated candidate for a **California SCO source-approval readiness package only**. Use the
canonical transport evidence to propose explicit purpose, data categories, minimized fields,
retention/privacy controls, maximum-size policy and transport controls. The candidate must remain
non-authorizing: no source approval, no registry enablement, no network request, no ZIP/CSV download,
no PII processing, no beneficiary matching and no outreach. Stop again at a human approval gate.
