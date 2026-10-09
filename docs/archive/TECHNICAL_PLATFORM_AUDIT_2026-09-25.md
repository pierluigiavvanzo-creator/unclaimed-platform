# TECHNICAL PLATFORM AUDIT — 2026-09-25

Status: OFFLINE TECHNICAL REVIEW

Baseline reviewed:

- repository: pierluigiavvanzo-creator/unclaimed-platform
- canonical branch: main
- reviewed HEAD: bd044185814c12d143f4cfcbef389b4a61037aa5
- latest verified post-merge CI before this audit: 36054428228 — SUCCESS

This audit evaluates architecture, implementation depth, tests, persistence, security boundaries and frontend structure. It does not authorize source access, PII processing or any P1 gate.

## Executive finding

The repository has a strong deterministic governance and contract foundation for product validation, but it is not yet a production-grade multi-user platform.

The principal gap is not current code fragility. It is the distance between:

GOVERNED BOUNDED MVP RUNTIME

and

DURABLE AUTHENTICATED PRODUCTION PLATFORM.

The project should not close every production gap before Stage B evidence. Consolidation should be triggered by evidence and by the point at which real PII or multi-user web access would otherwise cross an unsafe boundary.

## Verified strengths

### Deterministic governance core

Implemented code exists for:

- state-machine validation;
- policy evaluation with fail-closed missing-rule handling;
- budget ledger;
- orchestrator skeleton;
- append-only SHA-256 audit hash chain;
- privacy/data-minimization gates;
- immutable raw-storage adapter boundary.

### Contract discipline

The repository contains a large versioned schema/contract surface and extensive contract tests.

At audit time the recursive repository tree showed:

- 57 Python source files;
- 134 Python test files;
- 123 JSON Schema files.

### CI

Canonical CI runs:

- Ruff;
- strict mypy on core/API/storage/UI plus selected NY runtime;
- contract tests;
- smoke tests;
- full pytest;
- Next.js lint;
- TypeScript typecheck;
- Next.js build;
- Streamlit safety/startup smoke.

### Source/runtime evidence

NY and California source-adapter/runtime work is concrete and test-backed. Stage B remains intentionally narrow on the already-developed NY path.

## Material gaps

### G1 — Production persistence is not implemented

Severity: POST-P1 / PRE-PRODUCTION

Evidence:

- SQLAlchemy, Alembic and psycopg are declared dependencies;
- Docker Compose declares PostgreSQL;
- repository search found no application usage of SQLAlchemy, psycopg, create_engine, Session or DATABASE_URL;
- migrations/versions contains only .gitkeep.

Implication:

The target PostgreSQL persistence layer remains architectural intent rather than an implemented production repository layer.

Trigger to close:

- after P1 when P2 continuation is approved, or
- earlier if any web workflow would need durable case state.

### G2 — Audit chain is in-memory

Severity: POST-P1 / PRE-PRODUCTION

Evidence:

AuditEventWriter explicitly stores events in an in-memory list.

Implication:

Good for deterministic tests and bounded execution; insufficient for durable multi-user production audit.

Trigger to close:

Before a production web workflow handles real case decisions or multiple operators.

### G3 — Authentication / RBAC / case authorization absent

Severity: PRE-REAL-PII-WEB

Evidence:

No OAuth, JWT, session middleware, authentication or application RBAC implementation was found in the current code search.

Implication:

Current synthetic/read-only reviewer surfaces are appropriate. A real-PII web surface must not be enabled without a real identity and authorization boundary.

Trigger to close:

BEFORE any real owner PII is exposed through FastAPI/Next.js/Streamlit or any write action is enabled.

### G4 — Agent directories are architectural placeholders

Severity: DEFER / NOT A CURRENT DEFECT

Evidence:

A01-A23 directories exist, but no substantive implementation files are present inside the agent folders. Current functionality lives primarily in core, domain, adapters and scripts.

Implication:

Do not equate directory count with agentic capability.

Decision:

Do not fill these directories for completeness. Implement/wrap agents only when a measured workflow need justifies them.

### G5 — Test pyramid is contract-heavy

Severity: POST-P1 / PRE-PRODUCTION

At audit time:

- unit Python test files: 36;
- contract: 94;
- smoke: 4;
- integration: 0;
- golden: 0;
- adversarial: 0;
- security: 0.

Implication:

Current contract coverage matches the project's governance-first history, but production confidence will require integration, security and adversarial coverage.

Trigger to close:

- integration tests when durable persistence is introduced;
- security/adversarial tests before real-PII web access;
- golden cases after real P1/P2 evidence exists.

### G6 — Two frontend paths are diverging

Severity: NOW — PRODUCT ARCHITECTURE DECISION

Evidence:

- Next.js reviewer-console exists and is CI-built;
- Streamlit reviewer candidate exists and currently exposes a richer MVP-1 synthetic/economics surface.

Decision for FRONTEND_PRODUCT_UX_V1_OFFLINE:

- Next.js = candidate permanent product frontend;
- Streamlit = internal diagnostic / engineering / safe reviewer candidate until superseded.

Do not maintain two equivalent product UIs indefinitely.

### G7 — Dependency resolution is not locked

Severity: PRE-PRODUCTION

Evidence:

- no Python lockfile found;
- no npm/yarn/pnpm lockfile found;
- Python project dependencies use compatible ranges;
- CI uses npm install.

Trigger to close:

Before reproducible production release/deployment becomes a requirement.

### G8 — Historical NY runtime versions create maintenance surface

Severity: POST-P1

Evidence:

Multiple versioned NY transient-local runtime implementations and historical gate scripts remain in the source tree.

Implication:

They preserve provenance and should not be deleted casually, but the active production path should ultimately sit behind one stable interface.

Trigger to close:

After P1 identifies the final runtime behavior worth preserving.

### G9 — Canonical documentation is uneven

Severity: NOW / LOW RISK

Evidence:

PROJECT_STATE, ROADMAP and HANDOVER reflect the current product direction, while README and docs/architecture.md still contain older milestone framing.

Decision:

Reconcile documentation as part of the next safe documentation milestone; do not let it displace P1.

## Consolidation trigger — when to tell the Product Owner

The assistant must explicitly tell the Product Owner that consolidation is now the next product-critical step if any of the following becomes true:

1. P1 produces a reviewable real targetability result and the Product Owner wants to proceed to P2.
2. A web UI is about to display real owner PII.
3. A web UI is about to perform a material write/approval action.
4. More than one human operator needs durable case state or audit history.
5. A second registry must share generic case/evidence/economics state with NY.
6. Historical NY runtime variants start causing duplicated fixes or ambiguity about the active path.
7. Production deployment requires deterministic dependency reproduction.

At that point the consolidation package should prioritize:

AUTHENTICATION/RBAC
-> DURABLE DATABASE
-> DURABLE AUDIT
-> STABLE REPOSITORY/SERVICE INTERFACES
-> INTEGRATION/SECURITY/ADVERSARIAL TESTS
-> DEPENDENCY LOCKING
-> HISTORICAL RUNTIME FACADE/CLEANUP

Do not preemptively build all of this before the trigger.

## Current recommendation

Continue Stage B and FRONTEND_PRODUCT_UX_V1_OFFLINE in parallel because the UX work is synthetic, reversible and does not expand P1 authorization.

Do not connect the UX lab to real PII or production writes.
