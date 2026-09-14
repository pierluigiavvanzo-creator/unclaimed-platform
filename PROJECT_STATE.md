# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, reviewer read contract,
California SCO source governance, and the California SCO approval-readiness evidence package are
canonical and CI verified on `m2-state-governance-core`.

Streamlit Community Cloud is the active M3 reviewer deployment target under D-006 / ADR-0005.
The owner confirmed on 2026-09-14 that the deployed Streamlit app is configured on canonical
`m2-state-governance-core`; the previously verified functional/visual state remains the accepted
reviewer baseline.

The California SCO public bulk source is represented in `sources/registry.yaml` as
`ca.sco.unclaimed_property.bulk`, but it remains `enabled: false` and `approved_for_use: false`.
The versioned source-access policy is `PROPOSED` and explicitly non-authorizing. The canonical
approval-readiness evidence artifact also enforces `acquisition_performed: false`,
`source_approved: false`, and `source_enabled: false`.

Candidate `m3-ca-sco-source-governance` commit
`463c6d6c972fa955a8aa0d3c97208c3029e202a8` passed GitHub Actions run `34825751270` and was
promoted by clean fast-forward. Canonical post-promotion run `34826353694` passed.

Candidate `m3-ca-sco-approval-readiness` commit
`73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6` passed GitHub Actions run `34827272138` and was
promoted by explicit owner approval through a clean fast-forward into canonical
`m2-state-governance-core`. Canonical post-promotion run `34828513676` passed both `quality` and
`streamlit-candidate` on the same SHA.

`main` remains unchanged at `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.
Supabase remains untouched.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 versioned machine contracts and A00-A23 registry.
- M2 deterministic state/governance core, budget ledger and SHA-256 audit chain.
- M3 California source/legal readiness and fail-closed A01 acquisition boundary.
- M3 immutable SHA-256 raw persistence and deterministic provenance records.
- M3 privacy/data-minimization gate with trusted policy separated from caller context.
- Reviewer read contract `schemas/ui/m3_operations_console.schema.json` v1.0.0.
- FastAPI `GET /api/reviewer/m3/operations` synthetic/read-only endpoint.
- Streamlit reviewer canonical, CI verified and remotely validated.
- California SCO source registry candidate canonical, disabled and not approved.
- `SourceAccessGovernance` v1 contract canonical.
- California SCO policy canonical in `PROPOSED` / non-authorizing state.
- `SourceApprovalReadiness` v1 contract canonical.
- California SCO approval-readiness evidence canonical and explicitly non-authorizing.
- Governance/readiness regression tests prove that neither proposal nor evidence can claim real
  acquisition or source approval.

## Verification Evidence

- SCO governance SHA: `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO governance candidate CI `34825751270`: PASS.
- SCO governance canonical CI `34826353694`: PASS.
- SCO approval-readiness SHA: `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- Approval-readiness candidate CI `34827272138`: PASS.
- Approval-readiness canonical CI `34828513676`: PASS.
- Ruff: PASS.
- mypy: PASS.
- contract tests: PASS.
- smoke tests: PASS.
- full pytest: PASS.
- frontend lint/typecheck/build regression gates: PASS.
- Streamlit safety/startup smoke: PASS.
- Source registry approved real sources: `0`.
- No real dataset retrieval or row parsing performed.

## Blocked / Not Authorized

- Real California acquisition.
- Moving the California SCO source-access policy from `PROPOSED` to `APPROVED` without a separate
  human gate.
- Enabling the SCO registry entry for real use.
- Executing a transport preflight without a separate explicit owner gate.
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Unapproved scraping/restricted-source access.
- Promotion to `main` without a separate explicit stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Known Issues / Unresolved Readiness Items

- Exact SCO download URLs/redirect chain remain unverified.
- Actual HTTP media type, response size, timeout and maximum-byte policy remain unresolved.
- No downloaded artifact hash/revision exists because no real artifact has been acquired.
- CSV row layout/field names remain unknown.
- Processing purpose, data categories, minimized fields, PII necessity and retention policy remain
  intentionally unresolved.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration are outstanding.
- Known non-blocking dependency/runtime deprecation warnings remain in CI.

## Next Recommended Action

Prepare an isolated **California SCO transport-preflight proposal** only. The proposal must define
what a later network metadata preflight would be allowed to inspect, how redirects/headers/size bounds
would be recorded, and explicit zero-acquisition/no-row-parsing/no-PII constraints. Do not execute any
network request to a download endpoint as part of that proposal.

The actual transport preflight, source approval, registry activation and any retrieval remain separate
explicit owner gates.
