# M3 Operations Console — REUSE FIRST

Date: 2026-09-13
Scope: first synthetic/read-only reviewer surface

## Existing repository capabilities

- FastAPI application layer already exists and remains authoritative.
- JSON Schema draft 2020-12 is already the canonical machine-contract mechanism.
- M2/M3 already expose deterministic state, provenance, privacy and audit concepts that the UI can represent without inventing new domain behavior.
- No frontend framework or JavaScript workspace existed on the canonical branch.

## External evaluation

### Next.js

- Candidate: Next.js App Router.
- Current npm stable observed during review: `next` 16.3.4; React 19.3.0.
- License: MIT.
- Adoption/maintenance: very high and actively maintained.
- Fit: strong for a production reviewer UI, server-rendered read model and Vercel previews.
- Decision: REUSE.

### Vercel

- Official Git integration provides preview deployments for branch/PR iteration.
- Current project connector returned no teams/projects, so deployment cannot be treated as configured.
- Decision: REUSE WHEN CONNECTED; prepare deploy-ready app now, no external project creation in this slice.

### Supabase

- Current project connector returned no projects.
- Current guidance favors publishable browser keys and secret server keys; exposed tables require deliberate API grants/RLS policy design.
- Fit: promising for managed PostgreSQL/Auth/Storage behind existing boundaries.
- Decision: DEFER ACTIVE INTEGRATION. Do not add SDK or create database resources until the persistence/auth slice is approved.

### Streamlit

- Fit: fast internal prototype/dashboard tooling.
- Decision: INSPIRE/DEFER. It does not match the chosen Vercel-first production reviewer surface as well as Next.js.

## Result

Use Next.js for the candidate reviewer console, FastAPI + JSON Schema for the authoritative read contract, Vercel as the future preview/hosting path, and Supabase only behind approved backend boundaries later. No cloud resource or real-data activation is part of this work.
