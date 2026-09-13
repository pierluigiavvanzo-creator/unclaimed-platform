# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose of this handover

This document is the restart point for the next ChatGPT project chat. Do not reconstruct the project from memory and do not restart from M0. Read the repository governance files first, verify the branch/HEAD, then continue from the pending Windows validation of M2.

## Repository

- GitHub repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Repository visibility: private
- Current development branch: `m2-state-governance-core`
- M2 code/CI state commit before this handover: `95acc697c7f53ce06ac64f60a2d31f1f69cbb0bb`
- Previous verified rollback baseline: `m1-machine-contracts`, state-record commit `233930d177b6be485c44604447b58fc014358d93`
- Do not work directly on `main`.

## Mandatory files to read at session start

Read these before making architectural or code changes:

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

Build the Unclaimed Insurance Platform: a traceable, human-gated platform for identifying potential beneficiaries of unclaimed life-insurance policies using lawful public or authorized data sources.

The system must remain deterministic at governance boundaries, preserve provenance, fail closed, and keep humans in control of legally or operationally sensitive decisions.

## Non-negotiable architecture

The platform is not an uncontrolled mesh of AI agents.

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

Core rule: state transitions, policy gates, budgets and audit remain deterministic. Agents may propose actions but cannot bypass deterministic gates. External LLM/provider SDKs must remain behind adapters.

## Completed work

### M0 — Repository & Development Harness — VERIFIED

Implemented:

- Python 3.11 project skeleton.
- FastAPI application with `/health`.
- PostgreSQL development service through Docker Compose.
- PowerShell scripts:
  - `scripts/bootstrap.ps1`
  - `scripts/test.ps1`
  - `scripts/smoke.ps1`
  - `scripts/handover.ps1` (note: its embedded milestone text is stale and still references M0; do not use it as the authoritative M2 handover).
- Ruff, mypy, pytest.
- GitHub Actions CI.
- Source/domain/core/agent/test directory skeleton.
- A01-A23 agent placeholders.
- ADR-0001 deterministic orchestration core.

### M1 — Machine Contracts — VERIFIED

Implemented:

- JSON Schema draft 2020-12 contracts.
- Versioned contracts for:
  - Case
  - Evidence
  - Hypothesis
  - AgentMessage
  - Decision
  - AuditEvent
  - Source
  - SourceRegistry
  - AgentRegistry
- Canonical A00-A23 registry.
- Positive and negative contract fixtures.
- Contract validation tests.
- ADR-0002 versioned machine contracts.

Verified on the owner's Windows environment with Python 3.11.9:

- bootstrap: PASS
- Ruff: PASS
- mypy: PASS
- pytest: 12 passed
- smoke: 2 passed
- GitHub Actions: PASS

M1 persistent state was recorded in commit:

`233930d177b6be485c44604447b58fc014358d93`

### M2 — State & Governance Core — IMPLEMENTED, CI VERIFIED, WINDOWS VALIDATION PENDING

Branch:

`m2-state-governance-core`

Implemented:

- versioned deterministic workflow/state whitelist;
- deterministic state-machine model;
- A00 orchestrator skeleton;
- fail-closed policy engine skeleton;
- budget engine with explicit exhaustion behavior;
- append-only audit writer with SHA-256 event chaining;
- unit/governance tests for allowed and forbidden transitions;
- missing-policy behavior tests;
- budget exhaustion tests;
- audit-chain tests;
- REUSE-FIRST investigation;
- ADR-0003 M2 governance decision;
- `PROJECT_STATE.md`, `ROADMAP.md`, `DECISIONS.md`, and `CHANGELOG.md` updated.

Initial workflow states:

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

Unknown or non-whitelisted transitions must fail closed.

## M2 REUSE-FIRST decision

Two mature state-machine libraries were evaluated as inspiration/candidates:

- `pytransitions/transitions`
- `fgmacedo/python-statemachine`

Decision for M2: do not add either dependency yet. The current requirement is a small deterministic/versioned whitelist, and a third-party state-machine framework would add abstraction and dependency surface without a demonstrated need.

Re-evaluate this decision if the workflow later requires hierarchical states, concurrent regions, complex callbacks, visualization, or substantially more transition machinery.

## Important M2 CI history

The first M2 CI attempt on commit `35e7debae65962146c6f9b63d611aa766776e05d` failed at Ruff before mypy/pytest because of two `UP037` type-annotation style violations in `src/unclaimed_platform/core/state_machine/model.py`.

This was a lint/style failure, not a functional state-machine failure.

The annotations were corrected in commit:

`ab5e1fff5ae5103b895ed0dc4a13c4aa398936ac`

Final code CI then passed. A later documentation/state commit also passed CI.

Current M2 state commit before this handover:

`95acc697c7f53ce06ac64f60a2d31f1f69cbb0bb`

GitHub Actions result on that commit:

- Ruff: PASS
- mypy: PASS — 13 source files
- pytest: PASS — 24 passed
- warnings: 2 non-blocking FastAPI/Starlette dependency deprecation warnings
- workflow conclusion: SUCCESS

## Known warnings / technical debt

1. Two non-blocking test dependency deprecation warnings originate in FastAPI/Starlette/AnyIO integration. Do not treat them as an M2 failure.
2. PostgreSQL/Alembic initial application migration is not yet implemented.
3. `scripts/handover.ps1` still contains M0-specific embedded text and should eventually be made milestone-agnostic; this document is the authoritative current handover.
4. No production authentication/deployment exists yet.
5. No real claimant/beneficiary/insurer PII should be introduced at this stage.

## Safety / scope boundaries still in force

Do not enable or implement without the appropriate later legal/compliance gates:

- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or access to restricted data sources.

M3 remains blocked from real acquisition until source/legal readiness is established.

## Owner's local Windows environment

Known local repository path:

`C:\Users\NITRO\source\unclaimed-platform`

Known Python version from M1 validation:

`Python 3.11.9`

The owner uses PowerShell as the Windows bootstrap/test/orchestration layer.

## SINGLE NEXT ACTION — do this first in the next chat

Do not start M3 yet.

First complete the owner's Windows validation of M2.

Ask the owner to run exactly:

```powershell
cd C:\Users\NITRO\source\unclaimed-platform

git status --short
git fetch origin
git switch m2-state-governance-core
git pull --ff-only origin m2-state-governance-core

git branch --show-current
git log -5 --oneline

.\scripts\test.ps1
.\scripts\smoke.ps1
```

Expected results:

- branch: `m2-state-governance-core`
- Ruff: all checks passed
- mypy: no issues found
- pytest: 24 passed, with the two known non-blocking warnings acceptable
- smoke: 2 passed

If Windows validation passes:

1. update `PROJECT_STATE.md` to mark M2 VERIFIED;
2. update `ROADMAP.md` with M2 exit evidence;
3. record any material decision/failure in `DECISIONS.md` if needed;
4. only then begin the M3 readiness gate.

If Windows validation fails:

- do not start M3;
- capture the full failing command/output;
- fix M2 on `m2-state-governance-core` or a corrective branch as appropriate;
- rerun CI and Windows validation.

## M3 readiness gate — after M2 Windows verification only

The next substantive milestone is M3 — California Data Spike, but before implementing real ingestion the next chat must establish a source/legal readiness minimum.

The correct sequence is:

1. inventory candidate California sources;
2. verify source authority and permitted access method;
3. document provenance and source terms/constraints;
4. decide what can be mocked versus accessed for real;
5. define acquisition contracts/adapters;
6. run a bounded spike using no unnecessary PII;
7. preserve raw immutable evidence and append-only audit records.

Do not jump directly to scraping or beneficiary matching.

## Files likely to be touched next

After M2 Windows verification:

- `PROJECT_STATE.md`
- `ROADMAP.md`
- potentially `DECISIONS.md`
- `sources/registry.yaml`
- `src/unclaimed_platform/adapters/sources/`
- `mocks/`
- `tests/integration/`
- `tests/contract/`
- `docs/audits/` for M3 source/legal/reuse audit
- California policy/source documentation as approved

## Git discipline

- Do not modify `main` directly.
- Preserve `m1-machine-contracts` as rollback baseline for M2 until M2 is fully verified on Windows.
- Do not silently rewrite architectural decisions.
- Do not claim tests passed unless there is evidence.
- Record failures as well as successful fixes.
- Keep milestone changes isolated and reviewable.

## Restart prompt for the next ChatGPT chat

Use this message in the next chat if needed:

> Continue the Unclaimed Insurance Platform from `docs/handovers/HANDOVER_CURRENT.md` in `pierluigiavvanzo-creator/unclaimed-platform`. Read `AGENTS.md`, `PROJECT_STATE.md`, `ROADMAP.md`, `DECISIONS.md`, the ADRs and the handover before making changes. M0 and M1 are verified. M2 is implemented and GitHub CI is green, but owner Windows validation is still pending. First guide me through the M2 PowerShell validation; do not start M3 until it passes.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2 code: IMPLEMENTED
M2 GitHub CI: PASS
M2 Windows validation: PENDING
M3: DO NOT START YET
NEXT: Windows PowerShell validation of M2
```
