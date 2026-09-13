# ADR-0004 — Reviewer frontend and managed platform boundary

Date: 2026-09-13
Status: Proposed on candidate; accept on human-approved promotion

## Context

The platform needs visible product progress without moving governance authority into the browser. The owner requested a frontend and asked to use Vercel and Supabase where useful. The current repository has no frontend, no connected Vercel team/project and no connected Supabase project.

## Decision

1. Use Next.js App Router + TypeScript for the reviewer frontend under `apps/reviewer-console`.
2. Keep FastAPI and versioned backend contracts authoritative; the frontend is a read-only consumer for the first slice.
3. Use Vercel as the preferred preview/hosting target once an account/project is connected. Preview must be validated before production promotion.
4. Evaluate Supabase as managed PostgreSQL/Auth/Storage behind existing repository/adapter boundaries. Do not create a parallel authoritative data plane and do not expose secret/service-role keys to the browser.
5. Keep the first M3 console synthetic/read-only. No source approval, real acquisition, beneficiary matching or real PII is enabled by this ADR.

## Alternatives considered

- Server-rendered templates inside FastAPI: rejected because it couples reviewer UI iteration to backend presentation concerns.
- Streamlit as primary production UI: useful for internal prototypes, but weaker fit than Next.js for the intended governed reviewer product and Vercel preview workflow.
- Direct browser-to-Supabase as the primary data path: rejected because it would bypass the deterministic FastAPI/domain governance boundary.

## Consequences

- Frontend has an independent lint/type/build gate.
- The backend publishes a versioned read contract for reviewer data.
- Vercel/Supabase resource creation remains separately human/cost gated.
- Supabase Auth/RLS design, production persistence and secret management remain future bounded decisions.
