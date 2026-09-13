# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | GOVERNANCE/RAW STORAGE VERIFIED ON CANONICAL — REAL ACQUISITION BLOCKED | Source readiness, A01 acquisition contracts, raw persistence/privacy promoted and CI green |
| M3 Product Visibility — Operations Console | CANONICAL + CI VERIFIED — VERCEL PREVIEW CREATED, VERIFICATION BLOCKED BY SCOPE AUTH | Next.js reviewer UI canonical; preview deployment accepted by Vercel; deployment inspection returns HTTP 403 until Vercel scope is re-authorized |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- California SCO public bulk CSV identified only as a future bounded candidate; it is not approved for acquisition.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented and promoted to canonical.
- No real-source policy or real-source registry entry exists.

## M3 product visibility — promoted canonical slice

The historical candidate `m3-operations-console` added and has now promoted to canonical:

1. versioned read-only operations-console JSON Schema v1.0.0;
2. FastAPI reviewer endpoint as authoritative backend boundary;
3. Next.js App Router + TypeScript console;
4. visible M0-M3 status, source registry `0`, raw/provenance synthetic metadata, privacy gates, audit health and platform status;
5. explicit real-acquisition and beneficiary-matching blocked states;
6. frontend lint/type/build in GitHub CI and PowerShell test harness;
7. ADR-0004 for Next.js/Vercel/Supabase boundary;
8. Vercel deploy readiness;
9. Supabase readiness placeholders without SDK/database/project creation.

Promoted implementation head: `308a5f5f71d12378e190398b0e81fbabc28d6aa1`.
Canonical post-promotion CI run `34774600910`: PASS — Ruff, mypy, 18 contract tests, 3 smoke tests, 53 full tests, frontend lint/type/build.
Canonical documentation-closure CI run `34774757492`: PASS on `c6e8a9e25676853f8eb91652e27d0584c35ae3bb`.

## Vercel preview gate

Owner authorization: explicit on 2026-09-13.

Deployment created:

- deployment ID: `dpl_8YLYX5gUtUu67feZd9mgemWNmFtL`;
- preview URL: `https://unclaimed-reviewer-console-5vf7znh1f-pierluigiavvanzo-8728.vercel.app`;
- target: preview;
- create response: `INITIALIZING`;
- bundled content: canonical `apps/reviewer-console` frontend only;
- Supabase: untouched, zero projects observed.

Verification is not complete. The connected Vercel session is not authorized to read scope `pierluigiavvanzo-8728` / team `team_l4XAWc1rSwVdJWzlv5ZIirsJ` and returns HTTP 403 when querying the deployment. The preview must not be marked verified until the Vercel connection is re-authorized and status/build/page checks pass.

## Next gate

- Keep `main` unchanged unless separately approved under the stable-checkpoint policy.
- Re-authorize/connect the Vercel session to scope `pierluigiavvanzo-8728`.
- Verify deployment `dpl_8YLYX5gUtUu67feZd9mgemWNmFtL`: READY status, successful build logs, rendered page, no framework error overlay.
- Do not redeploy unless verification shows that the current deployment failed or a code/config fix is required.
- Supabase project/database/Auth/Storage work requires a separate bounded architecture + organization/cost gate.
- Frontend deployment does not authorize any real California acquisition.

## Still required before any real California acquisition

1. explicitly approve a versioned real-source governance policy and California SCO source entry through a separate human gate;
2. define production raw-storage/audit durability requirements;
3. implement bounded read-only retrieval with transport, redirect, size, timeout and content validation;
4. execute only a separately authorized bounded California spike with no unnecessary PII;
5. verify actual CSV layout from authorized evidence before A02 row normalization;
6. keep beneficiary matching blocked until later matching/privacy/legal gates are satisfied.

## Out of scope until later gates

- real California acquisition before explicit source/policy approval;
- real-data beneficiary matching;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.
