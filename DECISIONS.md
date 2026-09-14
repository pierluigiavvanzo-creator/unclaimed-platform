# DECISIONS.md

## D-001 — PowerShell Windows orchestration

Date: 2026-09-13

Status: Accepted

Decision:
Use PowerShell as the Windows bootstrap/orchestration layer.

Reason:
The initial development and testing environment is Windows-based.

Alternatives considered:
- Python
- Bash
- Make

Consequences:
PowerShell scripts must remain idempotent, explicit on failure and free of secrets.

---

## D-002 — Deterministic governance core

Date: 2026-09-13

Status: Accepted

Context:
State transitions, policy gates, budgets and audit must be reproducible and must not depend on probabilistic model behavior.

Decision:
Keep state machine, policy gates, budget controls and audit in deterministic core modules. Domain agents can propose actions but cannot bypass core gates.

Reason:
This preserves fail-closed behavior, auditability and testability.

Alternatives considered:
- Agent-owned workflow transitions
- LLM-directed orchestration

Consequences:
A00 coordinates agents but governance authority remains in deterministic code.

---

## D-003 — Versioned JSON Schema contracts

Date: 2026-09-13

Status: Accepted

Context:
Independent agents and adapters require stable boundaries.

Decision:
Use JSON Schema draft 2020-12 as the canonical machine interchange contract with explicit versions and contract tests.

Reason:
Prevents silent schema drift and supports independent module development.

Alternatives considered:
- Pydantic-only runtime contracts
- Unversioned Python dictionaries

Consequences:
Breaking changes require explicit schema versioning and migration/adapter work.

---

## D-004 — Explicit M2 workflow whitelist

Date: 2026-09-13

Status: Accepted

Context:
M2 requires a deterministic lifecycle state machine. Mature FSM libraries exist, but the initial need is a small versioned whitelist with fail-closed semantics.

Decision:
Implement the M2 workflow whitelist using standard-library code and versioned JSON configuration. Missing policy routes to HUMAN_REVIEW, budget exhaustion stops progression, and terminal states cannot transition outward.

Reason:
The critical behavior remains directly auditable and testable without introducing a broader state-machine dependency. Reuse must be reconsidered if hierarchical or concurrent state complexity appears.

Alternatives considered:
- python-statemachine
- transitions

Consequences:
M2 has a small custom state core; future expansion requires an explicit superseding decision rather than silent framework growth.

---

## D-005 — Canonical development branch and main integration policy

Date: 2026-09-13

Status: Accepted

Context:
`main` diverged from the verified development history after two direct commits created and then expanded a file named `root` whose contents were intended to act as `AGENTS.md`. Meanwhile the verified development branch contains the actual `AGENTS.md` plus the M0-M3 implementation and governance history.

Decision:
- Treat `m2-state-governance-core` as the current canonical development/integration branch until it is explicitly renamed or superseded.
- Treat `main` as the stable milestone/release branch, not as the day-to-day development branch.
- Promote feature/candidate branches into the canonical development branch only after the relevant tests and gates pass.
- Update `main` only at meaningful verified milestone or gate boundaries.
- Reconcile the existing divergence with a history-preserving merge commit that has both histories as parents.
- Keep the actual canonical `AGENTS.md` unchanged as the governing development contract; do not carry the misnamed `root` file into the reconciled tree.
- Avoid direct commits to `main` except deliberate owner-approved integration or emergency/hotfix work.

Reason:
This preserves all Git history without replacing the more specific verified governance contract or allowing `main` and the active development history to drift independently.

Alternatives considered:
- Force-reset `main` to the development branch
- Replace canonical `AGENTS.md` with the generic `root` content
- Keep the branches permanently divergent

Consequences:
The first reconciliation into `main` is a non-fast-forward merge by design. After reconciliation, milestone merges should remain simple provided direct development on `main` is avoided. The misnamed `root` file remains recoverable from Git history but is intentionally absent from the reconciled working tree.

---

## D-006 — Streamlit replaces Vercel on the M3 reviewer critical path

Date: 2026-09-14

Status: Accepted

Context:
The owner explicitly directed the project to abandon Vercel after repeated project/deployment visibility inconsistencies and move the reviewer surface to Streamlit.

Decision:
Use Streamlit Community Cloud as the active M3 reviewer deployment target. Preserve deterministic governance and the existing versioned/typed read model as authority. Keep the existing Next.js/Vercel implementation only as rollback/history until Streamlit is remotely verified.

Reason:
This materially reduces deployment complexity and removes the need for a separate preview backend plus `REVIEWER_API_BASE_URL` wiring while preserving the current synthetic/read-only scope.

Alternatives considered:
- Continue Vercel diagnostics
- FastAPI templates
- Gradio

Consequences:
ADR-0005 supersedes the Vercel deployment-target portion of ADR-0004. No real acquisition, beneficiary matching, source approval, real PII or Supabase integration is enabled by this decision.

---

## D-007 — Decommission repository-side Vercel runtime integration

Date: 2026-09-14

Status: Accepted

Context:
Streamlit is the verified reviewer deployment target, while the owner continues to receive failed-deployment notifications from the historical Vercel path. Repository-side provider configuration is no longer required and creates avoidable ambiguity.

Decision:
- Remove all active Vercel deployment configuration from the canonical repository tree.
- Remove provider-specific deployment instructions from active application documentation.
- Keep the legacy Next.js reviewer only as a provider-neutral local/regression artifact.
- Add a contract test that rejects reintroduction of Vercel-named files or textual Vercel references in active runtime surfaces (`.github`, `apps`, `scripts`, `src`, and root runtime configuration files).
- Preserve historical ADRs/audits as inert records; history is not executable configuration.
- Treat any external Vercel Git/project connection as a provider-side integration that must be disconnected separately from the repository contents.

Reason:
This prevents repository changes from intentionally invoking or configuring Vercel and makes Streamlit the only active reviewer deployment path represented by runtime configuration.

Alternatives considered:
- Keep `vercel.json` as dormant rollback configuration.
- Delete the entire legacy Next.js reviewer.
- Leave the repository unchanged and rely only on provider-side settings.

Consequences:
Vercel deployment is unsupported from the active repository tree. Reintroducing a Vercel runtime integration requires a new explicit owner decision and corresponding test/governance update. An already-installed external Git integration may still receive repository events until it is disconnected at the provider/GitHub integration layer.
