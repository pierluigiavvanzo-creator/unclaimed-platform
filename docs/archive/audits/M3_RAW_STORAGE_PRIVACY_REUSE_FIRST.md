# M3 Raw Storage / Provenance / Privacy — REUSE FIRST

Date: 2026-09-13

Class: **A — Product Critical**

## Objective

Select the smallest safe implementation boundary for immutable raw-artifact persistence, provenance persistence, and fail-closed privacy/data-minimization gates before any real source retrieval is enabled.

No real source acquisition is authorized by this document.

## Repository capabilities inspected

Already present:

- Python 3.11 standard library (`hashlib`, `pathlib`, atomic/exclusive file creation primitives);
- SQLAlchemy 2 / Alembic dependencies;
- versioned JSON Schema contracts;
- M2 `AuditEventWriter` with append-only SHA-256 hash-chain semantics;
- A01 acquisition request/result contracts and synthetic/deferred adapters;
- target architecture with an `adapters/storage` boundary.

Known repository constraint:

- the initial PostgreSQL/Alembic application migration is not yet implemented;
- real California acquisition remains blocked;
- `sources/registry.yaml` intentionally contains no approved real sources.

## External candidates

### HashFS

- URL: https://pypi.org/project/hashfs/
- License: MIT
- Maturity: PyPI classifies the project as Alpha; latest release is old relative to the current runtime baseline.
- Fit: directly provides content-addressed file placement.
- Decision: **REJECT for current production dependency; INSPIRE only**.
- Reason: the required M3 behavior is small, security-sensitive, and can be implemented with already available standard-library primitives while preserving an adapter boundary.

### fsspec

- URL: https://pypi.org/project/fsspec/
- License: BSD
- Maturity: active, mature filesystem abstraction with Python 3.11/3.12 support.
- Fit: useful for future backend portability across local/object storage.
- Decision: **DEFER**.
- Reason: it abstracts filesystems but does not itself establish the project's content-addressing, immutable metadata contract, privacy gate, or provenance rules. Adding it now increases dependency surface without materially reducing this bounded implementation.

### pymerkle

- URL: https://pypi.org/project/pymerkle/
- License: GPLv3+
- Maturity: Beta; provides inclusion/consistency proofs.
- Fit: cryptographic append-only proof structures.
- Decision: **REJECT**.
- Reason: the verified M2 audit writer already owns SHA-256 append-only chain semantics. A second cryptographic audit model would duplicate governance and introduce an incompatible/unnecessary dependency decision.

### SQLAlchemy 2 / Alembic

- URL: https://docs.sqlalchemy.org/en/20/
- License: MIT
- Maturity: mature and already a project dependency.
- Fit: durable metadata/audit persistence in the target PostgreSQL architecture.
- Decision: **DEFER database mapping, REUSE later**.
- Reason: the repository explicitly records the initial application migration as not yet implemented. This task should not silently expand into the database-migration milestone. The storage/provenance contract will remain backend-replaceable so a later SQLAlchemy repository can implement it without changing A01 semantics.

## Decision

Implement a bounded standard-library filesystem adapter under `src/unclaimed_platform/adapters/storage/` with:

- SHA-256 content addressing;
- exclusive-create semantics (no overwrite path);
- immutable JSON metadata manifest containing provenance and governance references;
- deterministic validation of byte count and content type;
- idempotent re-persist only when content and metadata are identical;
- corruption/mutation detection on read and on duplicate persistence;
- append of a `RAW_ARTIFACT_PERSISTED` event through the existing `AuditEventWriter`.

Implement a deterministic privacy/data-minimization gate in the core policy layer. The gate must fail closed before storage if source approval, provenance, authorized purpose/data scope, retention policy, or PII-necessity requirements are not satisfied.

This is an adapter-level implementation, not a commitment that local filesystem storage is the production backend.

## Acceptance criteria defined before implementation

1. Same bytes always produce the same SHA-256 and storage reference.
2. Persisted raw bytes and manifest cannot be overwritten through the adapter.
3. Existing artifact corruption or metadata mismatch is rejected deterministically.
4. Declared byte count and expected content type are validated before persistence.
5. Required provenance is complete before persistence.
6. A real artifact cannot pass without explicit source approval.
7. Missing retention policy blocks persistence.
8. Unauthorized processing purpose blocks persistence.
9. Unauthorized dataset/data category blocks persistence.
10. Requested fields outside the allowed/necessary set block persistence when field scope is declared.
11. Unnecessary PII blocks persistence.
12. Synthetic artifact happy path persists raw bytes + immutable provenance manifest.
13. Successful persistence appends an event to the existing audit hash-chain.
14. Re-persisting identical content/metadata is idempotent and does not append a duplicate audit event.
15. All failure reason codes are deterministic.
16. No real network access and no California CSV columns are introduced.
17. Ruff, mypy, pytest, contract tests, and synthetic smoke test pass before promotion.

## Files expected to be involved

- `src/unclaimed_platform/core/policy_engine/privacy.py`
- `src/unclaimed_platform/adapters/storage/__init__.py`
- `src/unclaimed_platform/adapters/storage/raw.py`
- `schemas/agents/a01_raw_artifact_record.schema.json`
- contract/unit/smoke tests for the new boundary
- `docs/contracts.md`
- `PROJECT_STATE.md`
- `ROADMAP.md` if milestone evidence changes
- `docs/handovers/HANDOVER_CURRENT.md`

No change to `sources/registry.yaml` is planned.