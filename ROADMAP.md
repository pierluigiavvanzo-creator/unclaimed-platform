# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | GOVERNANCE/RAW STORAGE VERIFIED ON CANONICAL — REAL ACQUISITION BLOCKED | Source readiness, A01 acquisition contracts, raw persistence/privacy promoted and CI green |
| M3 Product Visibility — Operations Console | CANONICAL + CI VERIFIED + STREAMLIT REMOTE/VISUAL SMOKE PASS | Base Streamlit runs PASS; final Vercel-style restyle SHA `563128e3...` and run `34817694129` PASS; owner screenshot confirms final live visual state |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- California SCO public bulk CSV identified only as a future bounded candidate; it is not approved for acquisition.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented and promoted to canonical.
- No real-source policy or real-source registry entry exists.

## Product visibility transition

The historical Next.js Operations Console remains in the repository as rollback/history. The owner explicitly ended Vercel as the active deployment path on 2026-09-14.

Streamlit is canonical for the M3 reviewer surface. It:

1. reuses the existing typed M3 reviewer snapshot instead of duplicating payload data;
2. validates `SYNTHETIC_READ_ONLY`, source registry `0`, acquisition/matching `BLOCKED`, `NO_REAL_PII`, synthetic and immutable raw artifact before rendering;
3. fails closed on an unsafe snapshot;
4. uses Streamlit Community Cloud as the active host;
5. removes the separate backend-preview and `REVIEWER_API_BASE_URL` wiring from the critical path;
6. introduces no Supabase resource, real source, real acquisition or real PII;
7. now uses the historical Vercel visual language on Streamlit: navy background, turquoise accents, dark cards, green/amber pills and a compact responsive hero;
8. renders page HTML through `st.html()` with a regression smoke guarding against raw-HTML Markdown rendering;
9. hides nonessential Streamlit toolbar/status/deploy chrome in the reviewer surface.

## Verification

Base implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`
Base documentation closure SHA: `c75adff971da6132cbcc54fab185b2ff6470e047`
Base GitHub Actions runs: `34812099385`, `34812289869` — PASS.
Final visual restyle SHA: `563128e3f37c14ec2715132ee14cf5813b057cba`
Final restyle GitHub Actions run: `34817694129` — PASS.
Remote URL: `https://unclaimed-platform-hlirhsqfxbfwjs7jhbsxn6.streamlit.app/`
Remote functional/content smoke: PASS.
Final visual smoke: PASS based on owner-provided screenshot on 2026-09-14.

- Ruff PASS.
- mypy PASS.
- contract tests PASS.
- smoke tests PASS, including Streamlit safety and visual regression checks.
- full pytest PASS.
- Streamlit startup smoke PASS on `/_stcore/health`.
- Existing Next.js lint/type/build regression gates PASS.
- Remote page confirms `SYNTHETIC READ ONLY`, real sources `0`, acquisition/matching `BLOCKED`, `NO REAL PII`.
- Final screenshot confirms Governance renders normally, title is compact on one line, Vercel-style palette is active, and Streamlit toolbar/status chrome is hidden.
- Visual-restyle branch promoted to canonical by explicit owner approval after a clean 6-ahead/0-behind comparison.

## Next gate

- Repoint the Streamlit Community Cloud app from `m3-streamlit-vercel-style-restyle` to canonical `m2-state-governance-core` and confirm the same remote visual state.
- Then prepare the next bounded M3 source-governance proposal for the California SCO public bulk candidate.
- Do not approve the source or acquire real data as part of that preparation.
- Keep beneficiary matching and real PII blocked.
- Keep `main` unchanged until a separate explicit stable-checkpoint decision.

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
