# Machine Contracts — M1

M1 establishes machine-readable boundaries before domain-agent implementation.

## Rules

- JSON Schema draft: 2020-12.
- Contract version: `1.0.0` for the original M1 contract family unless a later contract explicitly declares another version.
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

## M3 immutable raw persistence and provenance boundary

The next A01 persistence boundary adds:

- `schemas/agents/a01_raw_artifact_record.schema.json`
- `src/unclaimed_platform/adapters/storage/raw.py`
- `src/unclaimed_platform/core/policy_engine/privacy.py`

The immutable storage contract separates raw bytes from provenance records:

1. raw bytes are content-addressed by SHA-256 and receive a deterministic `storage_ref`;
2. each acquisition/provenance record receives its own deterministic `record_hash` and `record_ref`;
3. identical raw bytes may therefore have multiple append-only provenance records without rewriting
   the raw artifact;
4. an identical raw/provenance pair is idempotent and does not create a duplicate audit event;
5. any observed raw or provenance mutation is rejected/detected deterministically.

A raw provenance record persists at least:

- immutable raw storage reference;
- SHA-256 content hash;
- byte count and content type;
- source ID and source URI;
- authority and acquisition method;
- retrieval timestamp when required;
- source revision when available;
- approval reference when required;
- terms-review and retention-policy references;
- processing purpose;
- governance policy ID/version;
- declared data categories and requested field scope;
- additional provenance metadata;
- synthetic/real marker;
- immutable marker.

The persisted record is sufficient to locate the original raw bytes so normalized or derived data can
be rebuilt from the raw boundary rather than becoming the primary evidence source.

### Privacy and data-minimization gate

Authorization is deliberately separated from the acquisition request. The caller supplies acquisition
context; a separately supplied trusted `RawDataGovernancePolicy` supplies the allowed purpose, data
categories, field scope, retention policies, source approval rule, PII rule, and synthetic/real scope.
A request cannot authorize itself.

The gate fails closed if any applicable condition is missing or invalid, including:

- trusted privacy/data-minimization policy;
- source/provenance metadata;
- retrieval timestamp when required;
- source approval for real data or policy-required acquisition;
- authorized processing purpose;
- defined and authorized retention policy;
- authorized data category/dataset scope;
- minimized field scope;
- PII authorization and necessity.

Real data also requires a policy that explicitly permits non-synthetic artifacts. No such real-source
policy is introduced by this M3 block, and `sources/registry.yaml` remains without an approved real
source.

### Audit integration

Successful new raw/provenance persistence appends `RAW_ARTIFACT_PERSISTED` to the existing M2
`AuditEventWriter` SHA-256 hash chain. This reuses the verified audit model rather than introducing a
parallel ledger. The immutable provenance record itself is persisted by the storage adapter; durable
production persistence for the audit writer remains a separate later persistence concern.

The bounded filesystem adapter validates the contract with synthetic data and preserves the
`ImmutableRawStore` protocol boundary. It does not select the final production storage backend and it
does not implement any California network download.

## M3 reviewer-console read contract

The reviewer slice currently uses contract version `2.0.0`:

- `schemas/ui/m3_operations_console.schema.json`
- FastAPI endpoint `GET /api/reviewer/m3/operations`

Version `2.0.0` supersedes the original reviewer contract `1.0.0`. D-007 decommissioned the historical
repository-side deployment-provider integration and removed the provider-specific platform field from
the reviewer payload. Because that field was required in v1, removing it is a breaking shape change
and therefore correctly advances the major contract version rather than silently changing v1.

The v2 contract remains intentionally `SYNTHETIC_READ_ONLY`. It exposes milestone state,
source-registry state, one synthetic raw/provenance example, privacy/governance gate state,
audit-chain status, and provider-neutral platform readiness. It fixes approved real sources to `0`,
real acquisition to `BLOCKED`, beneficiary matching to `BLOCKED`, and real-PII mode to disabled.

The reviewer UI consumes this contract; it is not an authorization surface and cannot approve a
source, enable real acquisition, perform matching, or write claimant data. FastAPI/domain governance
remains authoritative. Repository-side deployment-provider configuration is separately protected by
`tests/contract/test_no_vercel_runtime_integration.py`.
