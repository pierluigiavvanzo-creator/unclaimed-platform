# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

Authoritative restart point for the next project chat. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Historical M3 candidate branch: `m3-acquisition-contracts`
- Historical main-reconciliation branch: `integration-main-sync-m3`
- Historical checkpoint branch: `checkpoint-main-m3`
- Main reconciliation commit: `b65e02f455c5a4c9bef6c77237ec5fefc6c315d3`
- First aligned M0-M3 stable checkpoint before this handover refresh: `c7225a2382058d2b6af0e0fb49cad286f70360d8`
- Branch policy is recorded in `DECISIONS.md` as D-005.
- Do not develop directly on `main`; use bounded feature/candidate branches and promote verified milestone checkpoints with owner approval.

At the start of a new chat, verify the current remote heads instead of assuming the SHA above is still HEAD.

## Mandatory files to read first

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/architecture.md`
6. `docs/contracts.md`
7. `docs/decisions/ADR-0001-deterministic-core.md`
8. `docs/decisions/ADR-0002-versioned-machine-contracts.md`
9. `docs/decisions/ADR-0003-m2-governance-core.md`
10. `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`
11. `docs/audits/M3_ACQUISITION_CONTRACTS.md`
12. `docs/audits/MAIN_DIVERGENCE_RECONCILIATION.md`
13. this handover

## Verified milestones

- M0 — VERIFIED.
- M1 — VERIFIED.
- M2 — VERIFIED.
- M3 source/legal readiness inventory — COMPLETE and documented.
- M3 acquisition contracts/adapters — IMPLEMENTED and CI VERIFIED.

## M3 status

The preferred future real-data source is the California State Controller public unclaimed-property bulk CSV. No real source is yet approved for use and `sources/registry.yaml` remains intentionally without approved real sources.

Implemented and verified:

- `schemas/agents/a01_acquisition_request.schema.json`;
- `schemas/agents/a01_acquisition_result.schema.json`;
- acquisition contract examples;
- fail-closed `CaliforniaSCOBulkAdapter` boundary;
- deterministic `DeferredMockSourceAdapter`;
- synthetic-only deferred-source fixture inventory;
- contract and unit tests;
- M3 source-readiness and acquisition-contract audit documentation.

A01 is intentionally limited to raw acquisition and provenance. It does not define California CSV row columns and does not perform normalization or beneficiary matching.

## Main reconciliation status

The previous `main` branch diverged because two direct commits created and expanded a file named `root` whose contents were intended to act as `AGENTS.md`.

The divergence was reconciled with a history-preserving merge commit:

- merge commit: `b65e02f455c5a4c9bef6c77237ec5fefc6c315d3`;
- parent 1: verified M3 development baseline `757202bb079cfeb01d0e1c5648ab26c9095be89e`;
- parent 2: prior `main` `e694d8476b949384a108e08157074ad54d803717`;
- canonical root-level `AGENTS.md` preserved unchanged;
- misnamed `root` file intentionally omitted from the reconciled tree;
- old `root` contents remain recoverable from Git history;
- reconciliation decision and policy recorded as D-005.

After the reconciliation and checkpoint update, `main` and `m2-state-governance-core` were verified identical at commit `c7225a2382058d2b6af0e0fb49cad286f70360d8` before this handover-only refresh.

## CI evidence

M3 candidate and promoted development baseline:

- Ruff: PASS;
- mypy: PASS — 13 source files;
- pytest: 30 passed;
- warnings: 2 known non-blocking FastAPI/Starlette/AnyIO dependency deprecations.

Stable `main` checkpoint verification:

- GitHub Actions run: `34764546636`;
- branch: `main`;
- head at run: `b65e02f455c5a4c9bef6c77237ec5fefc6c315d3`;
- Ruff: PASS;
- mypy: PASS — 13 source files;
- pytest: 30 passed;
- result: PASS.

Documentation checkpoint verification:

- commit: `c7225a2382058d2b6af0e0fb49cad286f70360d8`;
- CI on isolated checkpoint branch: PASS;
- subsequently aligned to both `main` and `m2-state-governance-core`.

No real network acquisition occurred.

## Safety boundaries still in force

Do not enable without later explicit gates:

- real SCO download before source approval/privacy/storage controls;
- beneficiary matching on real data;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.

## Context health / chat rotation protocol

The assistant must monitor context quality during project work and warn the owner before context degradation becomes operationally risky.

Early warning signals include one or more of the following:

- uncertainty or confusion about the active branch, baseline, commit or milestone;
- repeated need to re-derive constraints already recorded in repository memory;
- accidental mixing of historical and current project states;
- repetition of previously rejected approaches;
- scope drift across multiple unrelated workstreams;
- increasing dependence on conversational memory instead of repository evidence;
- the owner having to correct the same rule or state more than once;
- a long implementation sequence where the next step would benefit from a clean restart.

When these signals appear, the assistant must not continue silently. It must:

1. explicitly warn the owner that context health is degrading or approaching a risky level;
2. finish or safely stop the current bounded task;
3. update `PROJECT_STATE.md`, `ROADMAP.md` when applicable, `DECISIONS.md` when applicable, and this handover;
4. report the exact branch/HEAD/test state;
5. recommend opening a new chat;
6. provide a ready-to-paste restart prompt.

The warning should happen before repeated mistakes or branch/state confusion occur, not after the context has already failed.

## Known technical debt

- Two non-blocking FastAPI/Starlette/AnyIO deprecation warnings.
- GitHub Actions upstream Node runtime deprecation warnings for current checkout/setup-python actions; workflow passes.
- PostgreSQL/Alembic initial application migration not yet implemented.
- `main` currently has no enforced branch protection; rely on the explicit human gate until repository protection is configured.
- `scripts/handover.ps1` should be reviewed later because its text may lag the current milestone model.

## SINGLE NEXT ACTION

Start the next bounded M3 task on a new feature/candidate branch: define immutable raw-storage/provenance persistence and privacy/data-minimization gates before implementing any real California SCO retrieval.

Acceptance direction for the next task:

1. read mandatory repository memory before editing;
2. verify `main` and canonical development branch heads;
3. create an isolated feature/candidate branch from the verified canonical development head;
4. perform REUSE FIRST before custom persistence implementation;
5. define contract/storage boundary before implementation;
6. use synthetic/mock tests first;
7. persist an immutable raw artifact reference with SHA-256, byte count, content type, source and provenance metadata;
8. define append-only provenance persistence/audit behavior;
9. define explicit privacy and data-minimization rules;
10. fail closed if source approval, required provenance or privacy gate is missing;
11. do not perform real network retrieval during this task;
12. run Ruff, mypy, pytest and relevant smoke/contract tests;
13. show state/test/diff and stop at the human promotion gate before moving verified work into canonical/main branches.

## Restart commands for the owner

Before local work in PowerShell:

```powershell
cd C:\Users\NITRO\source\unclaimed-platform

git status --short
git fetch origin
git switch m2-state-governance-core
git pull --ff-only origin m2-state-governance-core
git log -1 --oneline
```

If `git status --short` shows local changes, do not pull or switch blindly; inspect them first.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal inventory: COMPLETE
M3 acquisition contracts/adapters: IMPLEMENTED + CI VERIFIED
main reconciliation: COMPLETE
stable M0-M3 checkpoint: COMPLETE
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
NEXT: isolated M3 raw-storage/provenance + privacy/data-minimization gate task
CONTEXT HEALTH: monitor proactively; warn owner before degradation becomes risky
```