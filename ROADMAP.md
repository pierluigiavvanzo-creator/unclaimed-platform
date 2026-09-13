# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | GOVERNANCE/RAW STORAGE VERIFIED ON CANONICAL — REAL ACQUISITION BLOCKED | Source readiness, A01 acquisition contracts, raw persistence/privacy promoted and CI green |
| M3 Product Visibility — Operations Console | IMPLEMENTED + CI VERIFIED + CANONICAL — DEPLOYMENT GATE PENDING | Next.js reviewer UI, read-only FastAPI contract, frontend lint/type/build green on canonical |

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
8. Vercel deploy readiness without creating a project;
9. Supabase readiness placeholders without SDK/database/project creation.

Promoted implementation head: `308a5f5f71d12378e190398b0e81fbabc28d6aa1`.
Canonical post-promotion CI run `34774600910`: PASS — Ruff, mypy, 18 contract tests, 3 smoke tests, 53 full tests, frontend lint/type/build.

## Next gate

- Keep `main` unchanged unless separately approved under the stable-checkpoint policy.
- Separately connect/expose an authorized Vercel team/project and obtain explicit owner approval before preview deployment.
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
