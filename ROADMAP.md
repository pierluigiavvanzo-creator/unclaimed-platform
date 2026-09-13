# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Windows Ruff/mypy green, 12 tests passed, smoke green, GitHub CI green |
| M2 — State & Governance Core | VERIFIED | GitHub CI green; Windows Ruff/mypy green; 24 tests passed; smoke 2 passed |
| M3 — California Data Spike | READINESS GATE — SOURCE INVENTORY COMPLETE | California source/legal inventory documented; real acquisition still blocked pending contracts, privacy constraints and explicit approval |

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

Completed in the current readiness step:

- candidate California sources inventoried;
- source authority and published access methods verified against official California government sources;
- provenance, access constraints and material legal/privacy constraints documented;
- sources classified as candidate-real, reference/manual, mock or deferred;
- `sources/registry.yaml` intentionally left without approved sources.

Evidence:

- `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`

Still required before any real California acquisition:

1. define the acquisition contract for the California State Controller public bulk CSV source;
2. define mock contracts for deferred sources;
3. define adapter boundaries without adding unapproved automation;
4. define raw immutable evidence and provenance handling;
5. define privacy/data-minimization constraints for the bounded spike;
6. explicitly approve the source for real use;
7. only then execute a bounded read-only California data spike with no unnecessary PII.

## Still out of scope until later gates

- beneficiary matching on real data before M3 readiness approval;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.
