# Reviewer Console

First product-facing UI slice for the Unclaimed Insurance Platform.

## Safety mode

This console is deliberately read-only and uses a governed synthetic preview when no FastAPI base URL is configured. It does not approve sources, download California data, perform beneficiary matching, or expose real claimant/beneficiary PII.

If `UNCLAIMED_API_BASE_URL` is configured, the server component requests the versioned FastAPI reviewer contract. If that configured backend is unavailable or returns an invalid payload, the UI fails closed instead of silently substituting the embedded preview.

## Windows development

From the repository root, start FastAPI in one PowerShell window:

```powershell
cd C:\Users\NITRO\source\unclaimed-platform
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = "src"
python -m uvicorn unclaimed_platform.api.app:app --reload
```

In another PowerShell window:

```powershell
cd C:\Users\NITRO\source\unclaimed-platform\frontend
Copy-Item .env.example .env.local -Force
npm install
npm run dev
```

Then open `http://localhost:3000`.

## Quality gates

```powershell
cd C:\Users\NITRO\source\unclaimed-platform\frontend
npm run lint
npm run typecheck
npm run verify:static
npm run build
```

## Vercel

The app is Vercel-compatible and targets Node.js 24.x. No Vercel project is assumed by this repository. A preview deployment must only be claimed after it is actually created and verified.

## Supabase

Supabase is intentionally not a runtime dependency in this first slice. It remains a candidate managed PostgreSQL/Auth/Storage provider behind the existing FastAPI/persistence boundaries. Do not expose service-role or secret credentials in browser code.
