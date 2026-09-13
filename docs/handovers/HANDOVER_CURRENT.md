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
- Main reconciliation commit: `b65e02f455c5a4c9bef6c77237ec5fefc6c315d3`
- Branch policy is recorded in `DECISIONS.md` as D-005.
- Do not develop directly on `main`; use bounded feature/candidate branches and promote verified milestone checkpoints with owner approval.

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

## Known technical debt

- Two non-blocking FastAPI/Starlette/AnyIO deprecation warnings.
- GitHub Actions upstream Node runtime deprecation warnings for current checkout/setup-python actions; workflow passes.
- PostgreSQL/Alembic initial application migration not yet implemented.
- `main` currently has no enforced branch protection; rely on the explicit human gate until repository protection is configured.
- `scripts/handover.ps1` should be reviewed later because its text may lag the current milestone model.

## SINGLE NEXT ACTION

Define immutable raw-storage/provenance persistence and privacy/data-minimization gates for M3 before implementing any real California SCO retrieval.

Acceptance direction for the next task:

1. contract/storage boundary first;
2. synthetic/mock tests first;
3. immutable raw artifact reference + SHA-256 + source/provenance metadata;
4. explicit data-minimization rules;
5. fail closed if source approval or required provenance is missing;
6. no real network retrieval during this task unless a later explicit owner gate authorizes it.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal inventory: COMPLETE
M3 acquisition contracts/adapters: IMPLEMENTED + CI VERIFIED
main reconciliation: COMPLETE
main CI run 34764546636: PASS
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
NEXT: immutable raw storage/provenance + privacy/data-minimization gates
```
