# Machine Contracts — M1

M1 establishes machine-readable boundaries before domain-agent implementation.

## Rules

- JSON Schema draft: 2020-12.
- Contract version: `1.0.0`.
- Objects reject undeclared fields with `additionalProperties: false` at the contract boundary.
- Decision status is limited to `CONTINUE`, `STOP`, `HUMAN_REVIEW`, `RETRY`, `DEFER`.
- Agent identifiers are limited to `A00` through `A23`.
- Evidence requires a SHA-256 content hash and explicit provenance.
- Source definitions must set `provenance_required: true`.
- Workflow-state legality is intentionally deferred to M2; M1 only defines the shape of `lifecycle_state`.
- No external source, endpoint, law, insurer, or claimant data is introduced by these fixtures.

## Compatibility policy

Within schema major version 1, producers must not remove required fields or change their meaning.
Breaking changes require a new major schema version and a migration/adapter decision.
