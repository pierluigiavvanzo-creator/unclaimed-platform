# Legacy M3 Operations Console

Read-only Next.js reviewer surface retained for local regression and historical comparison only.
It is not an active deployment target. The active reviewer surface is the Streamlit application in
`apps/reviewer-streamlit`.

This legacy app must remain provider-neutral: do not add deployment-provider configuration, tokens,
hooks, project IDs, provider-specific CLI commands, or repository deployment instructions here.

## Local regression use

```bash
npm install
npm run lint
npm run typecheck
npm run build
npm run dev
```

Set `REVIEWER_API_BASE_URL` to the FastAPI service to consume the authoritative endpoint. Without it,
the app intentionally renders a typed synthetic fallback so local build/preview remains safe and
deterministic.

## Supabase readiness

No Supabase SDK or project is required for this slice. Future integration must use a publishable
browser key only on the frontend, keep secret/service-role keys server-side, and preserve
FastAPI/domain contracts as the authoritative governance boundary.
`NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY` are reserved placeholders only.
