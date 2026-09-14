# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, reviewer read contract,
and the California SCO source-governance proposal are canonical and CI verified on
`m2-state-governance-core`.

Streamlit Community Cloud is the active M3 reviewer deployment target under D-006 / ADR-0005.
The owner confirmed on 2026-09-14 that the deployed Streamlit app is configured on canonical
`m2-state-governance-core`; the previously verified functional/visual state remains the accepted
reviewer baseline.

The California SCO public bulk source is now represented in `sources/registry.yaml` as
`ca.sco.unclaimed_property.bulk`, but it remains `enabled: false` and `approved_for_use: false`.
The versioned source-access policy is `PROPOSED` and explicitly non-authorizing:
real acquisition, beneficiary matching, outreach and real PII remain blocked.

Candidate `m3-ca-sco-source-governance` commit
`463c6d6c972fa955a8aa0d3c97208c3029e202a8` passed GitHub Actions run `34825751270`.
After explicit owner approval, the candidate was promoted by clean fast-forward into canonical
`m2-state-governance-core`. Canonical post-promotion run `34826353694` passed both `quality` and
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
- Vercel-style Streamlit restyle canonical, CI verified and visually validated.
- California SCO source registry candidate canonical, disabled and not approved.
- `SourceAccessGovernance` v1 contract canonical.
- California SCO policy canonical in `PROPOSED` / non-authorizing state.
- Governance regression tests prove a proposed policy cannot authorize real acquisition and the
  registry still contains zero approved real sources.

## Verification Evidence

- California SCO governance candidate SHA:
  `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- Candidate CI run `34825751270`: PASS.
- Canonical post-promotion CI run `34826353694`: PASS.
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
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Unapproved scraping/restricted-source access.
- Promotion to `main` without a separate explicit stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Known Issues / Unresolved Readiness Items

- Exact SCO download URLs/redirect chain have not been acquired or followed.
- The official download page advertises CSV files and links them on `claimit.ca.gov`, but exact
  transport content types, response sizes and redirect behavior remain unverified.
- A production timeout and maximum-byte policy have not been selected.
- Processing purpose, data categories, minimized row fields, PII necessity and retention policy are
  intentionally unresolved.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration are outstanding.
- Known non-blocking dependency/runtime deprecation warnings remain in CI.

## Next Recommended Action

Prepare a bounded M3 California SCO **approval-readiness evidence package** that records only
currently verified public facts and explicitly unresolved controls in a versioned machine-readable
contract. Do not follow/download the CSV links, do not approve or enable the source, do not infer row
layout, and do not authorize processing purposes, real PII, beneficiary matching or outreach.

The evidence package should keep evidence separate from authorization and should fail closed if any
readiness artifact claims that acquisition occurred or that the source was approved.
