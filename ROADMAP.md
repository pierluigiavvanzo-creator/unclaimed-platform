# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | 12 local tests, Ruff/mypy green, smoke green, GitHub CI green |
| M2 — State & Governance Core | IMPLEMENTED | 12 new unit tests pass; CI and Windows validation pending |
| M3 — California Data Spike | BLOCKED | Requires source/legal readiness minimum before real acquisition |

## M2 scope

- versioned state transition whitelist;
- A00 deterministic orchestrator skeleton;
- policy engine skeleton with fail-closed missing policy behavior;
- budget engine skeleton with explicit exhaustion behavior;
- append-only audit event writer skeleton;
- unit tests for allowed and forbidden transitions;
- governance tests for missing policy, budget exhaustion and audit chaining.

## M2 exit gate remaining

- GitHub Actions green on the M2 branch;
- Windows PowerShell test and smoke scripts green.

## Out of scope for M2

- real external data acquisition;
- claimant/beneficiary identification;
- outreach;
- legal determinations;
- claim submission;
- production authentication or production deployment.
