# M3 Immutable Raw Storage / Provenance / Privacy Gates

Date: 2026-09-13

Class: **A — Product Critical**

Status: **IMPLEMENTED + CI VERIFIED ON CANDIDATE — PENDING HUMAN PROMOTION GATE**

Candidate branch: `m3-raw-storage-privacy-gates`

Verified implementation/test head: `f42d8aa2daadcc83ff799150c039117755d8717a`

Base commit: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`

## Scope

This bounded M3 block establishes the persistence and governance boundary required before A01 may ever acquire a real raw source artifact.

Implemented:

- SHA-256 content-addressed immutable raw-byte persistence;
- deterministic immutable provenance records, separately hash-addressed from raw bytes;
- append-only provenance behavior for repeated acquisitions of identical raw bytes;
- integration with the existing M2 `AuditEventWriter` SHA-256 hash chain;
- versioned machine contract for the persisted raw/provenance record;
- trusted privacy/data-minimization policy separated from caller-supplied acquisition context;
- fail-closed source approval, purpose, retention, data-scope, field-scope and PII gates;
- synthetic-only unit, contract and smoke coverage;
- CI and PowerShell test harness alignment for the new boundary.

Not implemented:

- any California SCO network download;
- any real-source approval;
- any California CSV row interpretation or normalization;
- beneficiary matching;
- production object storage or WORM backend selection;
- durable database persistence for the existing in-memory audit writer.

`sources/registry.yaml` remains intentionally without an approved real source.

## REUSE FIRST result

The detailed evaluation is in `docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md`.

Summary:

- HashFS was not selected because the required behavior is small, security-sensitive, and the available package is not a sufficiently strong production dependency choice for this boundary;
- fsspec is mature but solves filesystem abstraction rather than project-specific immutability/provenance/governance; it remains a possible future backend abstraction;
- pymerkle was rejected because it would introduce a parallel cryptographic audit model and an unnecessary GPL dependency while the project already has a verified audit hash chain;
- SQLAlchemy/Alembic are already available and remain the preferred future database-layer tools, but application migration work is not yet ready and was deliberately kept out of this bounded task.

No new third-party runtime dependency was introduced.

## Persistence model

### Raw bytes

Raw bytes are addressed by SHA-256:

```text
raw/sha256/<first-2>/<next-2>/<content-hash>
```

The adapter uses exclusive-create semantics and refuses to replace bytes at an existing address. Reads recalculate SHA-256 and byte count to detect mutation/corruption.

### Provenance record

Each acquisition/provenance record is canonicalized deterministically and assigned a separate SHA-256 `record_hash`:

```text
provenance/sha256/<first-2>/<next-2>/<content-hash>/<record-hash>.json
```

This allows identical raw bytes to retain multiple immutable acquisition/provenance records without changing the raw artifact. Re-persisting an identical raw/provenance pair is idempotent.

The record includes:

- immutable storage reference;
- content SHA-256;
- provenance record reference/hash;
- byte count;
- content type;
- source ID and URI;
- authority;
- acquisition method;
- retrieval timestamp when applicable;
- source revision when available;
- approval reference when required;
- terms-review reference;
- retention-policy reference;
- processing purpose;
- governance policy ID/version;
- data categories;
- requested field scope;
- additional provenance metadata;
- synthetic/real marker;
- immutable marker.

The raw storage reference remains sufficient to retrieve the original bytes so normalized/derived data can later be rebuilt from raw evidence.

## Privacy / data-minimization model

`RawDataGovernancePolicy` is trusted configuration supplied separately from `RawDataGovernanceContext`. The acquisition request therefore cannot grant its own authorization.

The gate fails closed with deterministic reason codes when applicable requirements are absent or invalid, including:

- trusted privacy policy missing;
- source-policy mismatch;
- real data blocked by a synthetic-only policy;
- provenance missing/incomplete;
- required retrieval timestamp missing;
- explicit source approval missing for real data or policy-required sources;
- processing purpose not authorized;
- retention policy missing or not authorized;
- data category outside authorized scope;
- requested field outside minimized scope;
- PII not authorized;
- PII present but unnecessary for the authorized purpose;
- synthetic/real marker mismatch.

No policy authorizing a real source is introduced by this task.

## Audit integration

A new raw/provenance persistence appends `RAW_ARTIFACT_PERSISTED` through the existing M2 `AuditEventWriter`. Re-persisting an identical pair does not append a duplicate event.

The existing hash-chain model was reused rather than replaced or silently modified.

The immutable provenance record is durable in the bounded filesystem adapter. The existing audit writer itself remains the verified M2 in-memory implementation; durable production audit persistence is a separate later persistence concern.

## Acceptance-test coverage

Automated tests cover:

- deterministic SHA-256/content reference;
- immutable raw storage;
- raw mutation/corruption detection and rewrite rejection;
- provenance-record mutation/rewrite rejection;
- multiple append-only provenance records for identical raw bytes;
- byte-count validation;
- content-type validation;
- required provenance;
- missing trusted privacy policy;
- missing real-source approval;
- synthetic-only policy rejecting a real marker;
- synthetic/real marker mismatch;
- missing/unapproved retention policy;
- unauthorized processing purpose;
- unauthorized dataset/data category;
- field-scope/data-minimization failure;
- unauthorized/unnecessary PII;
- synthetic happy path;
- existing audit-chain append behavior;
- idempotent duplicate persistence;
- deterministic failure results;
- versioned JSON Schema contract;
- synthetic smoke path.

## CI evidence

GitHub Actions run: `34766966136`

Head: `f42d8aa2daadcc83ff799150c039117755d8717a`

Result: **PASS**

Executed gates:

- Ruff: PASS — `All checks passed!`;
- mypy: PASS — `Success: no issues found in 16 source files`;
- contract tests: PASS — `17 passed`;
- smoke tests: PASS — `2 passed`;
- full pytest: PASS — `51 passed`, `2 warnings`.

Warnings are the already-known non-blocking FastAPI/Starlette/AnyIO deprecations. GitHub Actions also emits the known upstream Node runtime deprecation notice for the current checkout/setup-python actions.

Earlier candidate CI runs exposed lint-only issues (B904 exception chaining, then one E501 line-length violation). They were repaired before the successful verification run; no failing run is being represented as VERIFIED.

## Risks / limitations

1. Filesystem immutability is application-enforced through content addressing, exclusive creation and integrity verification. It is not equivalent to provider-level WORM/object-lock retention.
2. The filesystem adapter is a bounded development/test implementation behind `ImmutableRawStore`, not the selected production storage backend.
3. The existing audit writer is hash-chained but in-memory; durable production audit-event persistence is still outstanding.
4. Retention is policy-gated and recorded, but physical lifecycle enforcement/deletion/hold behavior is not implemented in this block.
5. No real-source governance policy exists; therefore real acquisition remains blocked by design.

These limitations do not authorize expanding the scope of this task into production storage, database migration or real acquisition.

## Rollback

Before promotion, rollback is simply to abandon/delete candidate branch `m3-raw-storage-privacy-gates`; `main` and `m2-state-governance-core` remain unchanged.

After any later approved promotion, rollback should use normal history-preserving revert commits for the promoted candidate changes. Do not force-push or rewrite historical decisions.

## Human gate

Do not promote this candidate to `m2-state-governance-core` or `main` until the owner reviews:

- candidate branch and final HEAD;
- changed files and diff/stat;
- CI/test evidence;
- risks/limitations;
- rollback plan;
- proposed next action.

Real California acquisition remains a separate later human-gated decision.