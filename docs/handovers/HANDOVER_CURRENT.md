# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

Authoritative restart point for the next project chat. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Historical raw-storage/privacy candidate: `m3-raw-storage-privacy-gates`
- Historical M3 acquisition candidate: `m3-acquisition-contracts`
- Historical main-reconciliation branch: `integration-main-sync-m3`
- Historical checkpoint branch: `checkpoint-main-m3`
- Branch/integration policy is recorded in `DECISIONS.md` as D-005.
- Do not develop directly on `main`; use bounded feature/candidate branches and promote verified milestone checkpoints only after owner approval.

At every restart, verify remote branch HEADs and CI directly from GitHub. Do not assume a SHA in this handover is still current if later documentation or feature commits exist.

## Mandatory files to read first

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. this handover
6. `docs/architecture.md`
7. `docs/contracts.md`
8. `docs/decisions/ADR-0001-deterministic-core.md`
9. `docs/decisions/ADR-0002-versioned-machine-contracts.md`
10. `docs/decisions/ADR-0003-m2-governance-core.md`
11. `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`
12. `docs/audits/M3_ACQUISITION_CONTRACTS.md`
13. `docs/audits/MAIN_DIVERGENCE_RECONCILIATION.md`
14. `docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md`
15. `docs/audits/M3_RAW_STORAGE_PRIVACY_GATES.md`

## Verified milestones

- M0 — VERIFIED.
- M1 — VERIFIED.
- M2 — VERIFIED.
- M3 source/legal readiness inventory — COMPLETE.
- M3 acquisition contracts/adapters — IMPLEMENTED + CI VERIFIED + PROMOTED TO CANONICAL.
- M3 immutable raw-storage/provenance + privacy/data-minimization block — IMPLEMENTED + CI VERIFIED + PROMOTED TO CANONICAL.

## Raw-storage/privacy promotion closure

Candidate branch:

`m3-raw-storage-privacy-gates`

Candidate final HEAD approved by owner and promoted by fast-forward:

`1fbc74853385b6c6f92fb2c7d9b5b1df4ab0a10d`

Promotion target:

`m2-state-governance-core`

Post-promotion GitHub Actions run:

`34770452747`

Result: **PASS**

- Ruff: PASS;
- mypy: PASS on 16 source files;
- contract tests: PASS — 17 passed;
- smoke tests: PASS — 2 passed;
- full pytest: PASS — 51 passed with 2 known dependency warnings.

The promotion was history-preserving and non-forced. `main` was not modified by this promotion.

Subsequent documentation-only commits on `m2-state-governance-core` close the promotion gate in `PROJECT_STATE.md`, `ROADMAP.md`, and this handover. Verify their latest CI before treating the documentation closure as fully green.

## Current M3 capability

Implemented and promoted:

- trusted `RawDataGovernancePolicy` separated from caller-supplied acquisition context;
- deterministic fail-closed `RawDataGovernanceGate`;
- `ImmutableRawStore` protocol;
- bounded `FileSystemRawStore` adapter;
- SHA-256 content-addressed immutable raw-byte references;
- deterministic immutable provenance records with separate SHA-256 record hashes;
- append-only provenance history for repeated acquisitions of identical raw bytes;
- versioned `schemas/agents/a01_raw_artifact_record.schema.json` contract;
- integration with the existing M2 `AuditEventWriter` through `RAW_ARTIFACT_PERSISTED` events;
- idempotent duplicate persistence without duplicate audit events;
- corruption/mutation detection;
- synthetic unit, contract and smoke coverage;
- CI and PowerShell test harness coverage for storage, contracts and smoke paths.

## Privacy / safety state

Still enforced:

- `sources/registry.yaml` has no approved real source;
- no real California SCO download has occurred;
- no California CSV row layout is assumed or encoded;
- no real beneficiary, insured, decedent or family PII is introduced;
- beneficiary matching remains blocked;
- outreach remains blocked;
- claimant verification remains blocked;
- fee agreements remain blocked;
- claim submission remains blocked;
- unapproved scraping/restricted-source access remains blocked.

## Known limitations / technical debt

- Filesystem immutability is application-enforced, not provider-level WORM/object lock.
- `FileSystemRawStore` is a bounded adapter, not a production storage-backend selection.
- The M2 audit writer remains in-memory; durable production audit-event persistence is outstanding.
- Retention is required/authorized/recorded but physical lifecycle enforcement is not implemented.
- PostgreSQL/Alembic initial application migration is not yet implemented.
- Two known non-blocking FastAPI/Starlette/AnyIO deprecation warnings remain.
- GitHub Actions emits upstream Node runtime deprecation warnings for current checkout/setup-python actions; workflows pass.
- `main` has no enforced branch protection; continue using explicit human gates.

## Frontend/product-visibility directive

The owner explicitly requested that future development expose product progress through a frontend wherever practical, and asked to use Vercel and Supabase where they add value.

This does **not** authorize bypassing the existing architecture. The target remains:

```text
Reviewer UI
   |
FastAPI application layer
   |
A00 Orchestrator + State Machine + Gate Engine
   |
Domain agents / contracts / policy engine
   |
Repositories / adapters
   |
PostgreSQL + immutable raw storage + audit
```

Frontend rules for the next slice:

- backend deterministic contracts remain authoritative;
- UI must be read-only/synthetic for the first M3 operations-console slice;
- no real PII;
- no real acquisition;
- no source approval through a UI shortcut;
- no frontend-side service-role/secret keys;
- any material frontend/data-platform architecture decision must be recorded in an ADR before implementation;
- frontend lint/type/build checks must be part of CI;
- a Vercel preview is desirable after code verification, but deployment requires an available/connected Vercel account/project;
- Supabase may be evaluated as managed PostgreSQL/Auth/Storage behind existing boundaries, not as a parallel authoritative data plane.

## Vercel / Supabase account state observed on 2026-09-13

Using the connected platform tools:

- Vercel: no teams/projects were returned for the current connection;
- Supabase: no projects were returned for the current connection.

Therefore the next slice may prepare code/configuration for these platforms, but must not invent project IDs, URLs, keys or database resources. Creating a Supabase project/branch can incur cost and requires an explicit organization/cost confirmation gate. Cloud deployment is not a prerequisite for the first local/CI-verified frontend candidate.

Current Supabase guidance also requires using publishable frontend keys rather than service-role/secret keys, enabling RLS on exposed tables, and using current SSR packages/patterns if Auth is later introduced.

## SINGLE NEXT ACTION

Create an isolated candidate from the latest green `m2-state-governance-core` and implement the first **M3 Operations Console** frontend slice.

Before code:

1. verify latest canonical HEAD and CI after documentation closure;
2. create an isolated feature/candidate branch;
3. perform REUSE FIRST for Next.js/Vercel/Supabase and existing repository capabilities;
4. define acceptance criteria and a versioned read-only reviewer-console/backend contract;
5. create an ADR for the material frontend/platform choice.

Bounded implementation target:

- Next.js App Router + TypeScript frontend;
- visible M3 Operations Console;
- synthetic/read-only data only;
- milestone/status cards;
- source registry status (`0` approved real sources expected);
- raw artifact/provenance metadata example from synthetic fixtures/contracts;
- privacy/governance gate status;
- audit-chain health/status;
- clear blocked-state presentation for real acquisition and beneficiary matching;
- frontend lint/type/build gates in CI;
- no real network acquisition;
- no California row interpretation;
- no cloud-resource creation without separate authorization.

After implementation and green CI, present branch, HEAD, diff/stat, tests, risks, rollback and preview/deployment readiness, then stop at the human promotion/deployment gate.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal inventory: COMPLETE
M3 acquisition contracts/adapters: IMPLEMENTED + CI VERIFIED + CANONICAL
M3 immutable raw storage/provenance: IMPLEMENTED + CI VERIFIED + CANONICAL
M3 privacy/data-minimization gates: IMPLEMENTED + CI VERIFIED + CANONICAL
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Frontend next: M3 Operations Console candidate
Vercel connected projects/teams: NONE OBSERVED
Supabase connected projects: NONE OBSERVED
NEXT: isolated frontend candidate, contract/ADR first, synthetic/read-only console
CONTEXT HEALTH: coherent; repository remains the source of truth
```
