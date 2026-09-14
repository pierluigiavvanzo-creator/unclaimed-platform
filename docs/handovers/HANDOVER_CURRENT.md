# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Current canonical HEAD before this handover-only closure: `b231a8ad44e0205484f60d386d601edaa29a41b8`
- Stable `main` HEAD: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Historical Vercel backend candidate: `m3-vercel-backend-preview`
- Historical Streamlit deployment candidate: `m3-streamlit-operations-console`
- Historical Streamlit visual-restyle candidate: `m3-streamlit-vercel-style-restyle`
- Base verified Streamlit implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`
- Final visual-restyle candidate SHA: `563128e3f37c14ec2715132ee14cf5813b057cba`
- Never develop directly on `main`; promote verified checkpoints only after explicit owner approval.

The visual-restyle candidate was promoted by fast-forward into `m2-state-governance-core` after explicit owner approval. Immediately before promotion it was 6 commits ahead and 0 behind canonical, with merge-base at canonical SHA `85bb7a71720c9cc3c3145762da8b6eb33e85283a`.

After promotion, canonical documentation was closed on `b231a8ad44e0205484f60d386d601edaa29a41b8`; GitHub Actions run `34818120304` passed on that exact SHA.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Streamlit M3 Operations Console CANONICAL + CI VERIFIED + REMOTE FUNCTIONAL SMOKE PASS + VISUAL SMOKE PASS.
- Vercel-style Streamlit restyle CANONICAL + CI VERIFIED + VISUAL SMOKE PASS.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- `sources/registry.yaml` has no approved real source.
- Supabase untouched.
- `main` unchanged at `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Deployment decision

On 2026-09-14 the owner explicitly directed the project to abandon Vercel and move to Streamlit. D-006 and ADR-0005 record the decision.

Reason: repeated Vercel connector/project/deployment visibility inconsistencies made the two-deployment preview path operationally expensive without improving product value.

The existing Next.js/Vercel implementation is retained as rollback/history and as the visual reference that informed the Streamlit restyle. It is no longer on the critical path.

## Canonical Streamlit reviewer

Canonical branch: `m2-state-governance-core`.
Base verified implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`.
Final visual-restyle SHA: `563128e3f37c14ec2715132ee14cf5813b057cba`.
Canonical documentation closure SHA: `b231a8ad44e0205484f60d386d601edaa29a41b8`.
Base GitHub Actions implementation run: `34812099385` — PASS.
Base GitHub Actions documentation run: `34812289869` — PASS.
Final restyle candidate GitHub Actions run: `34817694129` — PASS.
Canonical post-promotion GitHub Actions run: `34818120304` — PASS.
Remote URL: `https://unclaimed-platform-hlirhsqfxbfwjs7jhbsxn6.streamlit.app/`.
Remote functional/content smoke: PASS.
Final remote visual smoke: PASS based on owner-provided screenshot on 2026-09-14.

Canonical scope:

- `apps/reviewer-streamlit/streamlit_app.py` — Streamlit Community Cloud entrypoint and custom reviewer rendering;
- `apps/reviewer-streamlit/theme.css` — Vercel-style navy/turquoise/green/amber visual language;
- `apps/reviewer-streamlit/requirements.txt` — deployment dependencies with Streamlit 1.63.0 pinned;
- `src/unclaimed_platform/ui/streamlit_console.py` — typed fail-closed adapter over the existing M3 reviewer snapshot;
- smoke tests for safe state, unsafe real-source rejection, custom theme markers, `st.html()` renderer regression, compact title and hidden Streamlit chrome;
- GitHub Actions Streamlit startup smoke;
- ADR-0005 and REUSE FIRST audit.

No snapshot payload is duplicated in Streamlit. The app loads the existing typed Python reviewer read model and refuses to render if safety invariants are violated.

## Visual-restyle evidence

The owner requested that the Streamlit app adopt the look and colors of the earlier Vercel/Next.js console. The restyle intentionally reuses that visual language while retaining Streamlit as the runtime.

Verified final state from owner screenshot:

- navy/near-black background and radial navy gradient;
- turquoise product eyebrow/accent;
- dark bordered cards;
- green `VERIFIED`/positive pills;
- amber governance/blocking pills;
- compact single-line desktop title `M3 Operations Console`;
- `Data mode` card positioned in the hero;
- Governance renders as styled content, not raw HTML;
- Streamlit toolbar/status/deploy chrome hidden from the reviewer surface;
- `SYNTHETIC READ ONLY`, approved real sources `0`, and blocking safety state remain visible;
- no visible runtime error.

A previous intermediate screenshot exposed Governance markup as raw code. Root cause: the page HTML was sent through the Markdown parser. The fix switched page rendering to `st.html(page_html)` and added a regression smoke asserting the Markdown renderer is not used for the page HTML.

## CI evidence

GitHub Actions run `34817694129` on exact final visual-restyle SHA `563128e3f37c14ec2715132ee14cf5813b057cba`:

- job `quality`: PASS;
- job `streamlit-candidate`: PASS;
- Ruff: PASS;
- mypy: PASS;
- contract tests: PASS;
- smoke tests: PASS;
- full pytest: PASS;
- Streamlit safety smoke: PASS;
- Streamlit startup smoke: PASS using `/_stcore/health`;
- existing Next.js lint/type/build regression gates: PASS.

GitHub Actions run `34818120304` on canonical closure SHA `b231a8ad44e0205484f60d386d601edaa29a41b8` also passed both `quality` and `streamlit-candidate`, including the same Python, frontend-regression and Streamlit startup gates.

## Deployment-branch alignment still required

For visual testing, the existing Streamlit Community Cloud app was manually repointed from canonical to `m3-streamlit-vercel-style-restyle`. The exact visual-restyle code is now present on canonical `m2-state-governance-core`, but the remote app configuration is not yet verified to have been switched back.

Therefore do not state that the live deployment branch is canonical-aligned until the owner repoints the Streamlit app to `m2-state-governance-core` and confirms the same page still renders correctly.

This is an operational alignment check only; the code itself is already canonical and CI verified.

## Safety boundaries still in force

Do not enable without later explicit gates:

- real California acquisition;
- beneficiary matching on real data;
- real claimant/beneficiary/decedent/family PII;
- autonomous outreach;
- legal determinations;
- claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.

## SINGLE NEXT ACTION

First, verify that the existing Streamlit Community Cloud app is configured on canonical `m2-state-governance-core` and that the same final page renders correctly. If it is still on `m3-streamlit-vercel-style-restyle`, repoint it to canonical and perform one remote visual/content smoke.

After that deployment-alignment check, prepare the next bounded M3 source-governance proposal for the California SCO public bulk candidate. This later step is preparation only: do not approve a real source, do not acquire real data, and do not enable beneficiary matching or real PII.

Keep `main` untouched. A promotion to `main` remains a separate explicit stable-checkpoint gate.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 governance/raw persistence: CANONICAL + VERIFIED
Streamlit Operations Console: CANONICAL + CI VERIFIED + REMOTE FUNCTIONAL/VISUAL SMOKE PASS
Vercel-style Streamlit restyle SHA: 563128e3f37c14ec2715132ee14cf5813b057cba
Vercel-style Streamlit restyle CI: 34817694129 PASS
Canonical closure SHA: b231a8ad44e0205484f60d386d601edaa29a41b8
Canonical post-promotion CI: 34818120304 PASS
Visual-restyle promotion: COMPLETE
Live Streamlit deployment branch: NOT YET VERIFIED CANONICAL-ALIGNED
Vercel active path: ABANDONED BY OWNER
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: verify Streamlit app branch = m2-state-governance-core; then California SCO governance proposal only
CONTEXT HEALTH: coherent; repository is source of truth
```
