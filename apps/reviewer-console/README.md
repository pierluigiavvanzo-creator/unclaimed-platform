# M3 Operations Console

Read-only Next.js reviewer surface for the M3 governance/provenance slice.

## Local

```bash
npm install
npm run lint
npm run typecheck
npm run build
npm run dev
```

Set `REVIEWER_API_BASE_URL` to the FastAPI service to consume the authoritative endpoint. Without it, the app intentionally renders a typed synthetic fallback so build/preview remains safe and deterministic.

## Vercel readiness

When a Vercel team/project is connected, configure the project root as `apps/reviewer-console`. Preview deployment is preferred before any production promotion. No Vercel team/project is connected in the current project state.

## Supabase readiness

No Supabase SDK or project is required for this slice. Future integration must use a publishable browser key only on the frontend, keep secret/service-role keys server-side, and preserve FastAPI/domain contracts as the authoritative governance boundary. `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY` are reserved placeholders only.
