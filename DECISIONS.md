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
