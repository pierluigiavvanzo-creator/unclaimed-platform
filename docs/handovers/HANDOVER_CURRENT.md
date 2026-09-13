# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

Authoritative restart point for the next project chat. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Canonical development branch: `m2-state-governance-core`
- Current isolated M3 candidate branch: `m3-acquisition-contracts`
- Candidate implementation commit: `b6030f2f1a5f9c7bdbe656e9eacba0a2e5107885`
- Do not work directly on `main`.

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
12. this handover

## Verified milestones

- M0 — VERIFIED.
- M1 — VERIFIED.
- M2 — VERIFIED.

## M3 status

Source/legal readiness inventory is complete.

The preferred future real-data source is the California State Controller public unclaimed-property bulk CSV. No real source is yet approved for use and `sources/registry.yaml` remains intentionally without approved real sources.

On isolated branch `m3-acquisition-contracts`, the following are implemented:

- `schemas/agents/a01_acquisition_request.schema.json`;
- `schemas/agents/a01_acquisition_result.schema.json`;
- contract examples;
- fail-closed `CaliforniaSCOBulkAdapter` boundary;
- deterministic `DeferredMockSourceAdapter`;
- synthetic-only deferred-source fixture inventory;
- contract and unit tests;
- M3 acquisition-contract audit documentation.

A01 is intentionally limited to raw acquisition and provenance. It does not define California CSV row columns and does not perform normalization or beneficiary matching.

## Candidate CI evidence

GitHub Actions run: `34763952641`

- Python: 3.11.16
- Ruff: PASS — `All checks passed!`
- mypy: PASS — 13 source files
- pytest: 30 passed
- warnings: 2 known non-blocking FastAPI/Starlette/AnyIO dependency deprecations

Local candidate-only verification before push:

- 6 new tests passed
- `compileall`: PASS

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

## SINGLE NEXT ACTION

Review the isolated `m3-acquisition-contracts` candidate and, only with owner approval, promote it to the canonical development branch `m2-state-governance-core`.

After promotion, the next technical gate is to define immutable raw-storage/provenance persistence and privacy/data-minimization controls before implementing any real California SCO retrieval.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal inventory: COMPLETE
M3 acquisition contracts/adapters: IMPLEMENTED + GITHUB CI VERIFIED ON CANDIDATE
Candidate branch: m3-acquisition-contracts
Candidate commit: b6030f2f1a5f9c7bdbe656e9eacba0a2e5107885
GitHub CI: PASS — Ruff PASS / mypy PASS / pytest 30 passed
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
NEXT: owner review/approval to promote candidate
```
