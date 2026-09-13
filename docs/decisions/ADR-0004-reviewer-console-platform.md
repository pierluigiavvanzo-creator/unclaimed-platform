# ADR-0004 — Reviewer console platform boundary

## Status
Accepted for the first product-facing reviewer-console slice.

## Context

The platform has verified deterministic M0–M3 backend/governance capabilities but no product-facing UI. The owner requires frontend visibility to progress in parallel with backend work and asked to use Vercel and Supabase where they add value.

The existing architecture already defines `Reviewer UI -> FastAPI -> deterministic core -> adapters/storage`. Any frontend decision must preserve that authority chain and must not introduce a second policy engine, audit ledger, source registry or uncontrolled data path.

At decision time, the connected Vercel tooling returned no teams/projects and the connected Supabase tooling returned no projects. Therefore no cloud resource identifier, deployment or database may be assumed.

## Decision

1. Add the reviewer console as a repository-local `frontend/` application using **Next.js 16 App Router + TypeScript + React**.
2. Keep **FastAPI** as the authoritative application/API layer. The frontend consumes a versioned read-only reviewer contract.
3. Use **Vercel** as the preferred preview/hosting target when an account/project is connected and a deployment is explicitly authorized/possible.
4. Treat **Supabase** as a candidate managed PostgreSQL/Auth/Storage provider behind existing persistence/auth boundaries, not as an additional authoritative data plane.
5. Do not add Supabase SDKs, tables or Auth merely for architectural fashion. Introduce them only when a concrete product capability requires them and a real project exists.
6. Never expose Supabase service-role/secret credentials to the browser. If browser-accessible Supabase tables are later introduced, use publishable keys plus explicit grants and RLS appropriate to the access model.
7. The first reviewer-console slice is **synthetic/read-only**. It exposes no mutation, source approval, outreach, claimant verification, fee agreement or claim-submission action.
8. Pin the frontend to Node.js `24.x` for CI/deployment compatibility and to avoid starting new work on the Vercel-deprecating Node 20 runtime.
9. Include frontend lint, TypeScript and production-build gates in CI before promotion.

## Initial UI scope

The first M3 Operations Console must display:

- M0–M3 milestone state;
- approved real-source count and registry status;
- real-acquisition blocked state;
- beneficiary-matching blocked state;
- one deterministic synthetic raw/provenance example;
- privacy/data-minimization gate state;
- audit hash-chain state;
- explicit synthetic/read-only labeling.

## Consequences

### Positive

- Product progress becomes visible and reviewable without weakening backend governance.
- Vercel can later provide low-friction preview environments.
- Supabase remains available for managed PostgreSQL/Auth without prematurely coupling the domain to its SDK.
- The frontend can evolve independently behind a versioned contract.

### Costs / limitations

- The repository becomes polyglot (Python + TypeScript/Node), so CI gains a frontend toolchain.
- Until a Vercel account/project is connected, verification is local/CI only and no preview URL can be claimed.
- Until a Supabase project and concrete persistence/auth requirement exist, Supabase remains an evaluated provider rather than an active runtime dependency.
- The first console uses synthetic/read-only data and is not an operational authorization surface.

## Alternatives considered

### Python-rendered templates / HTMX

Rejected for the first product UI because Next.js gives a stronger long-term reviewer-console surface, mature TypeScript component ecosystem and direct Vercel preview path.

### Separate SPA (Vite/React)

Viable, but deferred because Next.js provides server components, routing and a natural future SSR/Auth path in one supported framework.

### Supabase-first direct browser data access

Rejected. It would risk bypassing FastAPI/deterministic governance and create two competing application boundaries.

### Full component/dashboard framework immediately

Deferred. Native semantic React/CSS is sufficient for the first bounded console and keeps dependency surface small.

## Supersession rule

If the reviewer console later requires a materially different hosting framework, direct database architecture, or browser-side authorization model, supersede this ADR explicitly rather than silently changing the authority chain.
