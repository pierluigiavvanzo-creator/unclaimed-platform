# ADR-0007 — Product-value-first sequencing and MVP-1 commercial validation

**Date:** 2026-09-17  
**Status:** Accepted  
**Decision owner:** Product Owner

## Context

M0, M1 and M2 are verified and the M3 California work has established strong deterministic governance, provenance, privacy boundaries and fail-closed behavior. The latest bounded real-source execution correctly stopped on `TRANSPORT_METADATA_DRIFT` before body access.

At the same time, the product has `0` approved real sources, production classification is inactive, downstream case workflows are blocked, and the minimum economics/normalization/insurance-classification agent implementations remain incomplete. The dominant project risk has therefore shifted from foundational engineering to product/economic validation.

Continuing to optimize diagnostic/governance depth as an end in itself would create increasing engineering activity without proving that the system can produce a real case worth pursuing commercially.

## Decision

Adopt `PRODUCT_STRATEGY.md` as the canonical priority source for product sequencing and resource allocation.

Make `MVP-1 — First Economically Actionable Case` the primary product milestone. Work is prioritized by its contribution to the minimum vertical slice:

`authorized real source → bounded real ingestion → normalization → insurance relevance/classification → real candidate → evidence/provenance → economic screen → reviewer case card → human decision`.

Classify significant work A/B/C/D. Class D diagnostic/technical work is undertaken only when it protects or unblocks an A-class product/legal/privacy/safety risk.

The prior California transport/archive-layout baseline refresh remains a valid possible task, but it is no longer an objective by itself or an automatically exclusive next step. It should be pursued only if the MVP-1 gap/reuse audit shows that it is the smallest safe route to a usable authorized real source.

Before substantial new implementation, apply repository-first/reuse-first benchmarking. Do not expand full identity, genealogy, outreach, claim automation or multi-state infrastructure before upstream commercial evidence exists.

## Safety and governance boundary

This decision changes **priority and sequencing only**.

It does not:

- weaken D-008 or other accepted fail-closed decisions;
- authorize any network request, source continuation or PII access;
- reactivate or reuse consumed approvals;
- approve California SCO or any other real source;
- authorize outreach, claim submission or automated legal/commercial action;
- alter parser, projector, regex or normalization semantics.

All applicable source, privacy, legal and security gates remain in force.

## Alternatives considered

1. Continue the existing M3 diagnostic/governance sequence until California is exhaustively resolved before doing product work.
2. Implement the complete A01-A23 target architecture before commercial validation.
3. Begin downstream identity/genealogy automation using synthetic data while leaving real-source economics untested.

These alternatives were rejected for sequencing because they increase time and engineering surface before validating the project's core economic proposition.

## Consequences

- `PRODUCT_STRATEGY.md` becomes mandatory reading immediately after `AGENTS.md` for product work.
- The immediate next task is `MVP1_VERTICAL_SLICE_GAP_AND_REUSE_AUDIT`, repository-only and non-networked.
- Every substantial work package must state class A/B/C/D, MVP-1 stage, expected product/economic contribution, user-time impact and reuse decision.
- Infrastructure, tests and governance remain necessary when they protect the minimum real vertical slice, but no longer count as product progress by themselves.
- Commercial thresholds will be evidence-based; this ADR invents no monetary cutoff.
- The Product Owner remains the gate for genuinely material legal/privacy/source-access/architecture/commercial decisions, not repetitive technical QA.
