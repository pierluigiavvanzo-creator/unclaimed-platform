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

## M3 A01 acquisition boundary

M3 adds version `1.0.0` contracts for the raw acquisition boundary without changing the existing M1
source or evidence contracts:

- `schemas/agents/a01_acquisition_request.schema.json`
- `schemas/agents/a01_acquisition_result.schema.json`

The acquisition request distinguishes `MOCK` from `REAL`. A `REAL` request is invalid unless an
explicit non-empty `approval_id` is present. This contract condition is necessary but not sufficient
for real access: the runtime adapter must also be configured as approved.

M3 acquisition is limited to `RAW_INGEST_ONLY`. The result records source authority, source URI,
acquisition method, terms-review reference, retrieval timestamp, immutable raw storage reference,
byte count, content type, and SHA-256 content hash.

`ACQUIRED` and `MOCKED` results require an immutable raw artifact. `MOCKED` artifacts must be marked
synthetic; `ACQUIRED` artifacts must not be synthetic. `BLOCKED` and `FAILED` results cannot carry an
artifact.

The contract deliberately does not define California CSV row columns. The official State Controller
download page establishes a public bulk CSV download, but does not provide a stable machine-readable
row schema on that page. Row parsing/normalization belongs to A02 after a bounded sample or official
layout is verified; inventing columns in A01 would violate the repository no-fabrication rule.
