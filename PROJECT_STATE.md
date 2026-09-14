# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, reviewer read contract,
California SCO source governance, California SCO approval-readiness evidence, and the California SCO
transport-preflight proposal are canonical and CI verified on `m2-state-governance-core`.

Streamlit Community Cloud is the active M3 reviewer deployment target under D-006 / ADR-0005.
The owner confirmed on 2026-09-14 that the deployed Streamlit app is configured on canonical
`m2-state-governance-core`; the previously verified functional/visual state remains the accepted
reviewer baseline.

The California SCO public bulk source is represented in `sources/registry.yaml` as
`ca.sco.unclaimed_property.bulk`, but it remains `enabled: false` and `approved_for_use: false`.
The source-access policy remains `PROPOSED` and explicitly non-authorizing. The approval-readiness
evidence enforces `acquisition_performed: false`, `source_approved: false`, and
`source_enabled: false`. The transport-preflight proposal additionally enforces
`network_execution_authorized: false`, `network_request_performed: false`,
`response_body_bytes_allowed: 0`, no response-body persistence/parsing, no dataset persistence,
no real PII processing, no beneficiary matching, and no outreach.

Candidate `m3-ca-sco-transport-preflight-proposal` commit
`171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3` passed GitHub Actions run `34832293876` and was
promoted by explicit owner approval through a clean fast-forward into canonical
`m2-state-governance-core`. Canonical post-promotion run `34835032368` passed both `quality` and
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
- Reviewer read contract and Streamlit reviewer surface canonical and verified.
- California SCO registry entry canonical, disabled and not approved.
- `SourceAccessGovernance` v1 contract canonical.
- California SCO policy canonical in `PROPOSED` / non-authorizing state.
- `SourceApprovalReadiness` v1 contract and SCO readiness evidence canonical.
- `SourceTransportPreflightProposal` v1 contract and SCO transport-preflight proposal canonical.
- Contract tests prove proposal creation cannot authorize network execution, claim a request or
  acquisition occurred, permit response-body bytes, approve/enable the source, process real PII,
  perform matching, or enable outreach.

## Verification Evidence

- SCO governance SHA: `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO approval-readiness SHA: `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- SCO transport-preflight proposal SHA: `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`.
- Transport-preflight proposal candidate CI `34832293876`: PASS.
- Transport-preflight proposal canonical CI `34835032368`: PASS.
- Ruff: PASS.
- mypy: PASS.
- contract tests: PASS.
- smoke tests: PASS.
- full pytest: PASS.
- frontend lint/typecheck/build regression gates: PASS.
- Streamlit safety/startup smoke: PASS.
- Source registry approved real sources: `0`.
- No real dataset retrieval or row parsing performed.
- No transport-preflight request to a download endpoint has been executed.

## Blocked / Not Authorized

- Executing a California SCO transport preflight without a separate explicit owner gate.
- Real California acquisition.
- Moving the California SCO source-access policy from `PROPOSED` to `APPROVED` without a separate
  human gate.
- Enabling the SCO registry entry for real use.
- Persisting or parsing any response body during a transport preflight.
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Unapproved scraping/restricted-source access.
- Promotion to `main` without a separate explicit stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Known Issues / Unresolved Readiness Items

- Exact SCO download endpoint remains unverified.
- Request method, timeout, redirect limit, approved host allowlist, execution approval reference,
  observed HTTP status, final host, content type and content length remain unresolved.
- No downloaded artifact hash/revision exists because no real artifact has been acquired.
- CSV row layout/field names remain unknown.
- Processing purpose, data categories, minimized fields, PII necessity and retention policy remain
  intentionally unresolved.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration are outstanding.
- Known non-blocking dependency/runtime deprecation warnings remain in CI.

## Next Recommended Action

**Human gate only:** decide whether to authorize one bounded California SCO transport-preflight
execution limited to metadata observation under the canonical proposal.

If the owner approves that execution, create a new isolated execution task/branch that must keep
`response_body_bytes_allowed = 0`, perform no body persistence or parsing, acquire no dataset artifact,
process no real PII, perform no beneficiary matching/outreach, and stop after recording only the
transport metadata/provenance explicitly allowed by the proposal.

Source approval, registry activation, real retrieval and California data processing remain separate
later gates even if the metadata-only preflight is authorized and succeeds.
