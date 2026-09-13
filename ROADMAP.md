# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Windows Ruff/mypy green, 12 tests passed, smoke green, GitHub CI green |
| M2 — State & Governance Core | VERIFIED | GitHub CI green; Windows Ruff/mypy green; 24 tests passed; smoke 2 passed |
| M3 — California Data Spike | READINESS GATE | Real acquisition blocked pending source/legal readiness |

## M2 verified scope

- versioned state transition whitelist;
- A00 deterministic orchestrator skeleton;
- policy engine skeleton with fail-closed missing policy behavior;
- budget engine skeleton with explicit exhaustion behavior;
- append-only audit event writer skeleton;
- unit tests for allowed and forbidden transitions;
- governance tests for missing policy, budget exhaustion and audit chaining.

## M2 exit evidence

- GitHub Actions: PASS;
- Ruff: PASS;
- mypy: PASS on 13 source files;
- pytest: 24 passed;
- Windows PowerShell `scripts/test.ps1`: PASS;
- Windows PowerShell `scripts/smoke.ps1`: 2 passed;
- two known FastAPI/Starlette dependency deprecation warnings remain non-blocking.

## M3 readiness gate

Before real California acquisition:

- inventory candidate sources;
- verify source authority and permitted access method;
- document provenance and terms/constraints;
- decide what is mocked versus accessed for real;
- define acquisition contracts/adapters;
- preserve raw immutable evidence and append-only audit.

## Still out of scope until later gates

- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.
