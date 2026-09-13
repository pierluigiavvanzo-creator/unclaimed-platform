# ADR-0003 — M2 deterministic state and governance core

## Status
Accepted for M2.

## Context
M2 needs a state transition whitelist, A00 skeleton, policy gate, budget control and append-only audit
writer. The platform requires fail-closed behavior and direct auditability of material transitions.

## Decision
- Use a versioned JSON whitelist for lifecycle transitions.
- Keep state validation custom and small rather than adding a general state-machine dependency.
- Missing policy routes to `HUMAN_REVIEW`.
- Budget exhaustion returns `STOP` without consuming additional budget.
- Invalid transitions raise before budget consumption.
- Audit events form an append-only SHA-256 hash chain in M2; persistent storage is deferred to the
  database/migration milestone.

## State model v1
`NEW`, `PROCESSING`, `HUMAN_REVIEW`, `STOPPED`, `COMPLETED`.

`STOPPED` and `COMPLETED` are terminal. The model deliberately avoids outreach/claim states before
legal readiness.

## Consequences
The workflow core remains explicit and testable. If workflow complexity later requires hierarchical or
concurrent states, the reuse decision must be revisited and this ADR superseded rather than silently
expanding the custom engine.
