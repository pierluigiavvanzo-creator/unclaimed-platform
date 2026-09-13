# M3 Reviewer Console / Platform — REUSE FIRST

Date: 2026-09-13

Class: **A — Product Critical**

Status: **COMPLETE — IMPLEMENTATION NOT YET STARTED AT TIME OF REVIEW**

Candidate branch: `m3-operations-console-frontend`

Base branch: `m2-state-governance-core`

Base commit: `f518946c5e6fc4c816cfec54d4b5e1a7058c67d3`

## Product objective

Expose the already-verified M0–M3 backend/governance state through a real reviewer-facing surface without creating a second source of truth, weakening fail-closed controls, or introducing real claimant/beneficiary PII.

The first bounded slice is a read-only **M3 Operations Console** showing only governed/synthetic information.

## Existing repository assets to reuse

- FastAPI application layer already exists and remains the API authority.
- JSON Schema draft 2020-12 is already the canonical interoperable contract format.
- M2 deterministic state/policy/audit core already exists.
- M3 raw-artifact/provenance contract already exists.
- `sources/registry.yaml` is already the source-registry authority and contains zero approved real sources.
- GitHub Actions is already the canonical CI mechanism.

Decision: **REUSE** all of the above. Do not create a frontend-owned workflow state, policy engine, audit ledger or source registry.

## Candidate evaluation

### Next.js 16 App Router

- name: Next.js
- URL: official Next.js project/docs
- license: MIT
- maturity/adoption: very high; Next.js 16 is Active LTS as of this review
- fit: strong for a server-rendered reviewer console and Vercel preview workflow
- integration cost: low/moderate
- decision: **REUSE**
- reason: official React framework, first-class TypeScript/App Router support, strong Vercel integration, no need to invent routing/build infrastructure

### React

- name: React
- license: MIT
- maturity/adoption: very high
- fit: required by Next.js
- decision: **REUSE**

### Vercel

- name: Vercel
- role: preview/hosting target for the Next.js reviewer console
- maturity: production-grade managed platform
- fit: strong; Git-connected preview deployments are a natural human-review surface
- decision: **REUSE WHEN ACCOUNT/PROJECT IS AVAILABLE**
- current connection result: no Vercel teams/projects returned by the connected tool on 2026-09-13
- consequence: prepare a Vercel-compatible frontend now; do not invent project IDs or claim a deployment exists

### Supabase

- name: Supabase
- role considered: managed PostgreSQL, Auth and potentially Storage behind existing repository boundaries
- license/product model: open-source platform plus managed service
- maturity: high
- fit: potentially strong for managed PostgreSQL/Auth; must not replace deterministic backend governance or become an independent source of truth
- security notes: exposed tables require deliberate Data API grants/RLS; service-role/secret keys must never reach the browser; current Next.js SSR guidance uses `@supabase/ssr` for cookie-based sessions
- decision: **DEFER PACKAGE/SCHEMA INTEGRATION UNTIL A PROJECT AND A PRODUCT NEED EXIST**
- current connection result: no Supabase projects returned by the connected tool on 2026-09-13
- reason: adding unused SDKs/schema now would increase attack surface and maintenance without delivering user value; cloud project/branch creation may incur cost and requires a separate owner gate

### UI component frameworks

Candidates considered: shadcn/ui and larger dashboard/component kits.

Decision: **DEFER** for the first slice.

Reason: the first console needs a small number of status cards/tables. Native semantic React + CSS keeps dependency and supply-chain surface minimal. Reconsider when repeated interaction patterns justify reuse.

## Platform/version baseline

At review time:

- Next.js 16 is Active LTS;
- current stable Next.js package observed: `16.3.5`;
- current stable React/React DOM observed: `19.3.0`;
- Vercel supports Node.js 24 and makes 24.x the default for new projects;
- Next.js requires Node.js 20.9 or later.

The candidate will target Node.js `24.x` to avoid building a new surface on Node 20 shortly before its Vercel deprecation.

## Architecture choice

```text
Next.js reviewer console
        |
read-only versioned reviewer contract
        |
FastAPI application layer
        |
existing deterministic governance/domain layers
```

Supabase, when later introduced, must sit behind the existing persistence/auth boundaries. The browser must never receive privileged database credentials.

## Acceptance criteria before implementation

1. Work occurs only on `m3-operations-console-frontend`.
2. A versioned reviewer-summary JSON Schema exists before UI consumption.
3. FastAPI exposes a read-only reviewer summary endpoint using synthetic/governed information only.
4. Endpoint explicitly reports zero approved real sources while the registry is empty.
5. Endpoint explicitly reports real acquisition and beneficiary matching as blocked.
6. A deterministic synthetic raw-artifact/provenance example is permitted; no real California row layout is encoded.
7. Frontend renders milestone status, source-registry status, raw/provenance evidence, privacy/governance state and audit-chain status.
8. Frontend visibly labels itself synthetic/read-only.
9. Frontend has no mutation, approval, outreach, claimant-verification or claim-submission control.
10. Backend contract tests verify the reviewer payload against JSON Schema.
11. Frontend lint, TypeScript check and production build run in CI.
12. Existing Ruff/mypy/pytest/contract/smoke gates remain green.
13. No Vercel/Supabase deployment/project is claimed unless actually created and verified.
14. No secret/service-role key is committed or exposed.

## Files expected

- `docs/decisions/ADR-0004-reviewer-console-platform.md`
- `DECISIONS.md`
- `docs/contracts.md`
- `schemas/common/reviewer_operations_summary.schema.json`
- `src/unclaimed_platform/api/reviewer.py`
- `src/unclaimed_platform/api/app.py`
- backend contract/unit/smoke tests as needed
- `frontend/` Next.js application
- `.github/workflows/ci.yml`
- project-state/handover files after successful verification

## Test-first plan

Backend tests will be defined for:

- contract version and required fields;
- empty real-source registry state;
- synthetic marker;
- blocked real acquisition;
- blocked beneficiary matching;
- deterministic raw-artifact hash/reference example;
- privacy/audit status fields;
- GET-only/read-only endpoint behavior.

Frontend gates will be:

- ESLint with Next.js Core Web Vitals rules;
- `tsc --noEmit`;
- `next build`;
- a lightweight static assertion test for required operations-console labels/data states if practical without adding a test framework.

## Human/cloud gates

Code/CI work is authorized on the isolated branch.

Still requires a later explicit gate:

- promotion to canonical branch;
- Vercel project/deployment if account state or external state requires it;
- Supabase project/branch creation and any associated cost confirmation;
- any real data/source activation.
