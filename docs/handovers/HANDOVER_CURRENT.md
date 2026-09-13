# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

This is the authoritative restart point for the next project chat. Do not restart from M0 and do not reconstruct state from memory. Read the governance files and this handover before making changes.

## Repository

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Visibility: private
- Current development branch: `m2-state-governance-core`
- M2 is VERIFIED on both GitHub CI and the owner's Windows environment.
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
10. `docs/audits/M2_REUSE_FIRST.md`
11. this handover

## Product mission

Build a traceable, human-gated platform for identifying potential beneficiaries of unclaimed life-insurance policies using lawful public or authorized data sources.

Governance boundaries must remain deterministic, provenance must be preserved, uncertain or missing policy must fail closed, and humans remain in control of legally or operationally sensitive decisions.

## Non-negotiable architecture

```text
Reviewer UI
   |
FastAPI application layer
   |
A00 Orchestrator + State Machine + Governance Gates
   |
Domain agents A01-A23
   |
Contracts + Policy Engine + Budget Engine
   |
Repositories / Adapters / Source Clients
   |
PostgreSQL + immutable raw storage + append-only audit
```

Agents may propose actions but cannot bypass deterministic state, policy, budget or audit gates. External LLM/provider SDKs remain behind adapters.

## Completed milestones

### M0 — Repository & Development Harness — VERIFIED

Implemented Python 3.11 project skeleton, FastAPI `/health`, PostgreSQL dev service, PowerShell bootstrap/test/smoke scripts, Ruff, mypy, pytest, GitHub Actions, repository structure and ADR-0001.

### M1 — Machine Contracts — VERIFIED

Implemented JSON Schema draft 2020-12 contracts for Case, Evidence, Hypothesis, AgentMessage, Decision, AuditEvent, Source, SourceRegistry and AgentRegistry; canonical A00-A23 registry; positive/negative fixtures; contract tests; ADR-0002.

Windows verification on Python 3.11.9:

- Ruff: PASS
- mypy: PASS
- pytest: 12 passed
- smoke: 2 passed
- GitHub Actions: PASS

### M2 — State & Governance Core — VERIFIED

Implemented:

- versioned deterministic workflow state whitelist;
- deterministic state-machine model;
- A00 orchestrator skeleton;
- fail-closed policy engine;
- budget ledger with explicit exhaustion behavior;
- append-only SHA-256 audit chain writer;
- tests for allowed/forbidden transitions, missing policy, budget exhaustion and audit chaining;
- REUSE-FIRST audit;
- ADR-0003.

Workflow states:

```text
NEW
 ├──> PROCESSING
 ├──> HUMAN_REVIEW
 └──> STOPPED

PROCESSING
 ├──> HUMAN_REVIEW
 ├──> STOPPED
 └──> COMPLETED

HUMAN_REVIEW
 ├──> PROCESSING
 ├──> STOPPED
 └──> COMPLETED

STOPPED    [terminal]
COMPLETED  [terminal]
```

Unknown or non-whitelisted transitions fail closed.

## M2 verification evidence

GitHub CI:

- Ruff: PASS
- mypy: PASS on 13 source files
- pytest: 24 passed
- workflow: SUCCESS

Owner Windows PowerShell validation:

- `scripts/test.ps1`: PASS
- Ruff: `All checks passed!`
- mypy: `Success: no issues found in 13 source files`
- pytest: `24 passed, 2 warnings`
- `scripts/smoke.ps1`: `2 passed, 2 warnings`

The two warnings are known non-blocking dependency deprecations from FastAPI/Starlette/AnyIO test tooling.

## Important M2 CI history

The first M2 CI attempt failed only on two Ruff `UP037` annotation-style violations. The issue was corrected without changing architecture or functional behavior. Subsequent CI passed Ruff, mypy and the full test suite.

Do not erase this history; failures and fixes are part of the project audit trail.

## REUSE-FIRST result

`pytransitions/transitions` and `fgmacedo/python-statemachine` were evaluated. Neither was adopted for M2 because the current need is a small deterministic/versioned whitelist and the external framework overhead was not justified.

Re-evaluate if later workflow complexity requires hierarchical states, concurrency, richer callbacks or visualization.

## Known technical debt

- Two non-blocking FastAPI/Starlette/AnyIO test deprecation warnings.
- PostgreSQL/Alembic initial application migration not yet implemented.
- `scripts/handover.ps1` still embeds M0-specific text and is not authoritative; this file is authoritative.
- No production authentication/deployment yet.

## Safety boundaries still in force

Do not enable without later explicit legal/compliance gates:

- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or access to restricted sources.

No unnecessary real PII should be introduced during the next spike.

## Owner environment

- Local repository: `C:\Users\NITRO\source\unclaimed-platform`
- Python: 3.11.9
- Shell/orchestration: PowerShell

## SINGLE NEXT ACTION

Begin the **M3 California Data Spike readiness gate**, not real scraping or beneficiary matching.

The next chat must first:

1. inventory candidate California sources;
2. verify source authority and permitted access method;
3. document provenance, terms and access constraints;
4. determine which sources can be mocked and which can be accessed for real;
5. define acquisition contracts/adapters;
6. only then run a bounded California spike with no unnecessary PII;
7. preserve raw immutable evidence and append-only audit records.

M3 real acquisition remains blocked until this readiness gate is satisfied.

## Files likely to be touched next

- `PROJECT_STATE.md`
- `ROADMAP.md`
- potentially `DECISIONS.md`
- `sources/registry.yaml`
- `src/unclaimed_platform/adapters/sources/`
- `mocks/`
- `tests/integration/`
- `tests/contract/`
- `docs/audits/`
- California source/policy documentation as approved

## Git discipline

- Do not modify `main` directly.
- Keep milestone work isolated and reviewable.
- Never claim tests passed without evidence.
- Record failures and fixes.
- Do not silently rewrite architectural decisions.

## Restart prompt

> Continue the Unclaimed Insurance Platform from `docs/handovers/HANDOVER_CURRENT.md` in `pierluigiavvanzo-creator/unclaimed-platform`. Read `AGENTS.md`, `PROJECT_STATE.md`, `ROADMAP.md`, `DECISIONS.md`, the ADRs and the handover before changing anything. M0, M1 and M2 are VERIFIED. Start only the M3 California source/legal readiness gate; do not begin real scraping or beneficiary matching until source authority and permitted access are documented.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M2 GitHub CI: PASS
M2 Windows test.ps1: PASS — 24 passed
M2 Windows smoke.ps1: PASS — 2 passed
M3: READINESS GATE ONLY
NEXT: California source/legal readiness inventory
```
