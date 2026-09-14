# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before this documentation closure:
  `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`
- Stable `main` HEAD: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Historical Streamlit deployment candidate: `m3-streamlit-operations-console`
- Historical Streamlit visual-restyle candidate: `m3-streamlit-vercel-style-restyle`
- Promoted SCO governance candidate: `m3-ca-sco-source-governance`
- Promoted SCO approval-readiness candidate: `m3-ca-sco-approval-readiness`
- Never develop directly on `main`; promote verified checkpoints only after explicit owner approval.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Streamlit M3 reviewer CANONICAL + CI VERIFIED + REMOTE FUNCTIONAL/VISUAL SMOKE PASS.
- Streamlit Community Cloud branch confirmed by owner as canonical `m2-state-governance-core`.
- California SCO source governance CANONICAL + CI VERIFIED.
- California SCO approval-readiness evidence CANONICAL + CI VERIFIED.
- SCO source registry entry exists but is `enabled: false` and `approved_for_use: false`.
- SCO source-access policy status is `PROPOSED`; real acquisition authorization is `false`.
- Approval-readiness evidence enforces `acquisition_performed: false`, `source_approved: false`, and
  `source_enabled: false`.
- Approved real source count remains `0`.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

## California SCO source-governance promotion

Candidate branch: `m3-ca-sco-source-governance`.

Promoted SHA:
`463c6d6c972fa955a8aa0d3c97208c3029e202a8`

Candidate CI run `34825751270`: PASS.
Canonical post-promotion CI run `34826353694`: PASS.

## California SCO approval-readiness promotion

Candidate branch: `m3-ca-sco-approval-readiness`.

Promoted SHA:
`73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`

Immediately before promotion the candidate was 1 commit ahead and 0 behind canonical with merge-base
at `f4f03dc6340b169bfb2f7fc62f81a2177bf9898d`.

Owner explicitly approved promotion. The canonical branch was advanced without force to the candidate
SHA.

Candidate CI run `34827272138`: PASS.
Canonical post-promotion CI run `34828513676`: PASS.

Verified gates on the promoted SHA include:

- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- historical Next.js lint/typecheck/build regression gates PASS;
- Streamlit safety smoke PASS;
- Streamlit startup smoke PASS.

## Canonical SCO approval-readiness artifacts

- `schemas/common/source_approval_readiness.schema.json`
- `schemas/examples/ca_sco_approval_readiness.examples.json`
- `sources/evidence/ca_sco_unclaimed_property_bulk.approval_readiness.v1.json`
- `tests/contract/test_ca_sco_approval_readiness.py`
- `docs/audits/M3_CA_SCO_APPROVAL_READINESS.md`

The evidence contract deliberately separates verified facts from authorization. It cannot claim that
an acquisition occurred, that the source was approved, or that the source was enabled.

## Current authoritative public-source facts

Verified from official California State Controller pages on 2026-09-14 and recorded in the canonical
evidence package:

- the Controller publishes all records in its public unclaimed-property database in `.CSV` format;
- the official download page says the files are updated every Thursday;
- the download links displayed on the official SCO page point to `claimit.ca.gov`;
- SCO public-record access is subject to the California Public Records Act and applicable conditions;
- SCO privacy guidance states that personal-information use is constrained by stated purposes/law,
  while website information is public domain and may be copied/used as permitted by law;
- CCP §1582 is retained only as a downstream legal-review reference for locator/recovery agreements,
  not as source-acquisition authority.

These facts do not themselves approve source acquisition or downstream processing.

## Intentionally unresolved

Do not invent or silently fill:

- exact download URLs or redirect chain;
- actual HTTP content type;
- current file size or byte budget;
- timeout policy;
- downloaded artifact hash/revision;
- CSV row layout/field names;
- authorized processing purpose;
- data categories or minimized field scope;
- PII necessity;
- retention policy;
- source approval reference.

## Safety boundaries still in force

Do not enable without later explicit gates:

- execution of a transport preflight against download endpoints;
- real California acquisition;
- source policy `APPROVED` state;
- source registry `enabled` / `approved_for_use`;
- beneficiary matching on real data;
- real claimant/beneficiary/decedent/family PII;
- autonomous outreach;
- legal determinations;
- claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.

## SINGLE NEXT ACTION

Create an isolated candidate branch for a **California SCO transport-preflight proposal only**.

The bounded task must:

1. define a versioned machine-readable transport-preflight contract/proposal;
2. specify the metadata that a later authorized preflight may inspect: endpoint identity, redirect
   behavior, response/content-type metadata, size evidence, timeout/max-byte controls and provenance;
3. define fail-closed invariants proving that proposal creation performs no acquisition and grants no
   approval;
4. keep the existing SCO registry disabled/not approved and source-access policy `PROPOSED`;
5. add contract tests for the proposal;
6. perform no request to a download endpoint, no CSV download, no row parsing and no real PII
   processing;
7. keep beneficiary matching and outreach blocked;
8. keep `main` untouched.

After proposal tests/CI pass, stop at a human gate. Actual network execution of the transport preflight
requires separate explicit owner approval.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
M3 SCO approval readiness: CANONICAL + CI VERIFIED
SCO governance SHA: 463c6d6c972fa955a8aa0d3c97208c3029e202a8
SCO approval-readiness SHA: 73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6
SCO governance candidate CI: 34825751270 PASS
SCO governance canonical CI: 34826353694 PASS
SCO readiness candidate CI: 34827272138 PASS
SCO readiness canonical CI: 34828513676 PASS
SCO registry: DISABLED + NOT APPROVED
SCO policy: PROPOSED + NON-AUTHORIZING
Approved real sources: 0
Streamlit deployment branch: m2-state-governance-core (owner confirmed)
Real acquisition: BLOCKED
Transport preflight execution: BLOCKED PENDING EXPLICIT OWNER GATE
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: isolated M3 California SCO transport-preflight proposal only; no network execution
CONTEXT HEALTH: coherent; repository is source of truth
```
