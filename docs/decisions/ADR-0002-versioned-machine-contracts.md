# ADR-0002 — Versioned machine contracts

Status: Accepted

## Context

Multiple agents will be developed independently. Unversioned message shapes would allow silent drift
between agents, orchestration, persistence, and review tooling.

## Decision

Use JSON Schema draft 2020-12 as the canonical interchange contract. Every M1 entity carries an
explicit schema version where appropriate, rejects undeclared boundary fields, and is covered by
positive and negative contract fixtures. Workflow transition legality remains a separate M2 concern.

## Consequences

Agent implementations may vary internally, but boundary payloads must validate before orchestration
continues. Breaking contract changes require explicit versioning and migration work.
