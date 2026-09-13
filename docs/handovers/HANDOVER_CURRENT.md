# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

Authoritative restart point for the next project chat. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Active candidate branch: `m3-raw-storage-privacy-gates`
- Candidate base commit: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Verified implementation/test head: `f42d8aa2daadcc83ff799150c039117755d8717a`
- Historical M3 acquisition candidate: `m3-acquisition-contracts`
- Historical main-reconciliation branch: `integration-main-sync-m3`
- Historical checkpoint branch: `checkpoint-main-m3`
- Branch/integration policy is recorded in `DECISIONS.md` as D-005.
- Do not develop directly on `main`; use bounded feature/candidate branches and promote verified milestone checkpoints only after owner approval.

The exact active candidate HEAD will be newer than the verified implementation head because project-state/audit/handover documentation is committed after functional verification. At the start of a new chat or immediately before promotion, verify the remote HEAD and CI rather than assuming a SHA from this file is still current.

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
- M3 source/legal readiness inventory — COMPLETE and documented.
- M3 acquisition contracts/adapters — IMPLEMENTED and CI VERIFIED on the canonical/stable baseline.
- M3 immutable raw-storage/provenance + privacy/data-minimization block — IMPLEMENTED and CI VERIFIED on candidate, pending human promotion gate.

## Baseline before current candidate

At task start, GitHub verification showed both `main` and `m2-state-governance-core` at:

`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`

Both branch CI baselines were successful. No newer repository change conflicted with the prior handover.

The current candidate was created from the canonical development branch at exactly that commit. `main` and the canonical branch were not modified during implementation.

## M3 raw-storage/privacy candidate

Implemented:

- `RawDataGovernancePolicy` as trusted authorization configuration separated from caller-supplied acquisition context;
- `RawDataGovernanceGate` with deterministic fail-closed reason codes;
- `ImmutableRawStore` protocol;
- bounded `FileSystemRawStore` implementation using standard-library primitives;
- SHA-256 content-addressed immutable raw-byte references;
- separate deterministic SHA-256 immutable provenance records;
- append-only provenance behavior allowing the same raw bytes to retain multiple acquisition records;
- immutable record fields for source, authority, acquisition method, retrieval time, source revision, approval reference, retention policy, purpose, governance policy version, data scope, field scope, synthetic/real marker and provenance metadata;
- versioned `schemas/agents/a01_raw_artifact_record.schema.json` contract;
- integration with the existing M2 `AuditEventWriter` through `RAW_ARTIFACT_PERSISTED` events;
- idempotent duplicate persistence without duplicate audit events;
- deterministic corruption/mutation detection;
- contract, unit and synthetic smoke coverage;
- CI and PowerShell test harnesses expanded so the new storage adapter is included in mypy and explicit contract/smoke gates.

The caller cannot self-authorize a processing purpose, data category, field scope, retention policy, PII or real-data access because authorization comes from the separately supplied trusted policy.

A synthetic-only policy rejects a real artifact. Even a real-capable policy still requires explicit source approval before real raw persistence.

## REUSE FIRST decision

Evaluated before custom persistence work:

- HashFS: not selected as a production dependency; maturity/current-maintenance fit was not strong enough for this security-sensitive boundary;
- fsspec: mature and potentially useful later for backend abstraction, but it does not itself implement the project's immutability/provenance/privacy semantics;
- pymerkle: rejected because it would duplicate the verified M2 audit model and introduce an unnecessary GPL dependency;
- SQLAlchemy/Alembic: already available and retained for later durable database persistence, but the initial application migration is not ready and was deliberately kept out of this bounded task.

No new third-party runtime dependency was added.

## CI evidence

Verified implementation/test head:

`f42d8aa2daadcc83ff799150c039117755d8717a`

GitHub Actions run:

`34766966136`

Result: **PASS**

- Ruff: PASS — all checks passed;
- mypy: PASS — 16 source files;
- contract tests: PASS — 17 passed;
- smoke tests: PASS — 2 passed;
- full pytest: PASS — 51 passed, 2 known dependency warnings.

Earlier candidate runs exposed lint-only issues (B904 exception chaining and one E501 line-length failure); both were repaired before the successful run. Do not represent the earlier failing runs as verified.

Documentation commits after the implementation/test head must have a final green CI result before promotion. The agent performing the human gate must verify that final result directly from GitHub.

No real network acquisition occurred.

## Privacy / safety state

Still enforced:

- `sources/registry.yaml` has no approved real source;
- no real California SCO download;
- no California CSV row layout is assumed or encoded;
- no real beneficiary, insured, decedent or family PII is introduced;
- beneficiary matching remains blocked;
- outreach remains blocked;
- claimant verification remains blocked;
- fee agreements remain blocked;
- claim submission remains blocked;
- unapproved scraping/restricted-source access remains blocked.

## Known limitations / technical debt

- Filesystem immutability is application-enforced through content addressing, exclusive create and integrity verification; it is not provider-level WORM/object-lock storage.
- `FileSystemRawStore` is a bounded adapter, not a production storage-backend selection.
- The existing M2 audit writer is hash-chained but remains in-memory; durable production audit-event persistence is still outstanding.
- Retention policy is required, authorized and recorded, but physical lifecycle enforcement is not part of this block.
- Two known non-blocking FastAPI/Starlette/AnyIO deprecation warnings remain.
- GitHub Actions emits upstream Node runtime deprecation warnings for current checkout/setup-python actions; workflow passes.
- PostgreSQL/Alembic initial application migration is not yet implemented.
- `main` currently has no enforced branch protection; rely on the explicit human gate until repository protection is configured.
- `scripts/handover.ps1` should be reviewed later because its generated text may lag the current milestone model.

## Architecture decision status

No new ADR was created for this block because the implementation stays within already documented architecture boundaries:

- A01 owns raw acquisition/provenance;
- `adapters/storage` already exists as the storage boundary;
- the verified M2 audit hash-chain is reused rather than changed;
- production storage technology remains undecided;
- database migration remains a separate later concern.

The bounded implementation decision and its limitations are documented in the M3 audit files rather than silently turning the local filesystem adapter into a production architecture decision.

## Context health / chat rotation protocol

The assistant must monitor context quality during project work and warn the owner before context degradation becomes operationally risky.

Early warning signals include:

- uncertainty or confusion about the active branch, baseline, commit or milestone;
- repeated need to re-derive constraints already recorded in repository memory;
- accidental mixing of historical and current project states;
- repetition of previously rejected approaches;
- scope drift across unrelated workstreams;
- increasing dependence on conversational memory instead of repository evidence;
- the owner having to correct the same rule/state more than once;
- a long implementation sequence where the next step would benefit from a clean restart.

When these signals appear, the assistant must:

1. warn the owner explicitly;
2. finish or safely stop the current bounded task;
3. update project memory and this handover;
4. report exact branch/HEAD/test state;
5. recommend a new chat;
6. provide a ready-to-paste restart prompt.

## SINGLE NEXT ACTION

**Human promotion gate only.**

Before changing either canonical branch:

1. verify the exact remote HEAD of `m3-raw-storage-privacy-gates`;
2. verify final CI on that exact HEAD is green;
3. compare the candidate against base `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` and report changed files/diff-stat;
4. verify `main` and `m2-state-governance-core` are still unchanged/coherent;
5. verify `sources/registry.yaml` still contains no approved real source;
6. present risks and rollback;
7. stop and obtain explicit owner approval before promotion.

Do **not** implement or execute a real California SCO download during this gate.

After owner approval, promote the verified candidate to the canonical development branch using history-preserving Git operations and re-run CI there. Promotion to `main` remains separately governed by the stable-checkpoint policy and owner approval.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal inventory: COMPLETE
M3 acquisition contracts/adapters: IMPLEMENTED + CI VERIFIED
M3 immutable raw storage/provenance: IMPLEMENTED + CI VERIFIED ON CANDIDATE
M3 privacy/data-minimization gates: IMPLEMENTED + CI VERIFIED ON CANDIDATE
Candidate: m3-raw-storage-privacy-gates
Verified implementation/test head: f42d8aa2daadcc83ff799150c039117755d8717a
Human promotion gate: PENDING
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
NEXT: verify final candidate HEAD/CI/diff and stop for owner promotion approval
CONTEXT HEALTH: coherent; repository remains the source of truth
```