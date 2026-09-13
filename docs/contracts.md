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

M3 adds version `1.0.0` contracts for the raw acquisition boundary without changing the existing M1 source or evidence contracts:

- `schemas/agents/a01_acquisition_request.schema.json`
- `schemas/agents/a01_acquisition_result.schema.json`

The acquisition request distinguishes `MOCK` from `REAL`. A `REAL` request is invalid unless an explicit non-empty `approval_id` is present. This contract condition is necessary but not sufficient for real access: the runtime adapter must also be configured as approved.

M3 acquisition is limited to `RAW_INGEST_ONLY`. The result records source authority, source URI, acquisition method, terms-review reference, retrieval timestamp, immutable raw storage reference, byte count, content type, and SHA-256 content hash.

`ACQUIRED` and `MOCKED` results require an immutable raw artifact. `MOCKED` artifacts must be marked synthetic; `ACQUIRED` artifacts must not be synthetic. `BLOCKED` and `FAILED` results cannot carry an artifact.

The contract deliberately does not define California CSV row columns. Row parsing/normalization belongs to A02 only after a bounded authorized sample or official layout is verified.

## M3 immutable raw persistence and provenance boundary

The A01 persistence boundary includes:

- `schemas/agents/a01_raw_artifact_record.schema.json`
- `src/unclaimed_platform/adapters/storage/raw.py`
- `src/unclaimed_platform/core/policy_engine/privacy.py`

Raw bytes are content-addressed by SHA-256; each acquisition/provenance record has its own deterministic hash and immutable record reference. Identical bytes may have multiple append-only provenance records, while an identical raw/provenance pair is idempotent. Mutation or corruption is detected deterministically.

Authorization is separated from caller context. `RawDataGovernancePolicy` supplies trusted purpose, data categories, field scope, retention rules, source approval requirements, PII rules and synthetic/real scope. Real data requires a policy that explicitly permits it; no such policy currently exists.

Successful new raw/provenance persistence appends `RAW_ARTIFACT_PERSISTED` to the existing M2 SHA-256 audit chain. The filesystem implementation remains a bounded replaceable adapter, not a production WORM-storage decision.

## M3 reviewer-console read contract

The frontend slice adds version `1.0.0` contract:

- `schemas/ui/m3_operations_console.schema.json`
- FastAPI endpoint `GET /api/reviewer/m3/operations`

The contract is intentionally `SYNTHETIC_READ_ONLY`. It exposes milestone state, source-registry state, one synthetic raw/provenance example, privacy/governance gate state, audit-chain status and platform readiness. It fixes approved real sources to `0`, real acquisition to `BLOCKED`, beneficiary matching to `BLOCKED`, and real-PII mode to disabled.

The reviewer UI consumes this contract; it is not an authorization surface and cannot approve a source, enable real acquisition, perform matching or write claimant data. FastAPI/domain governance remains authoritative.
