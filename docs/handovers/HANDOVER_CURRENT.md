# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before this documentation closure:
  `463c6d6c972fa955a8aa0d3c97208c3029e202a8`
- Stable `main` HEAD: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Historical Streamlit deployment candidate: `m3-streamlit-operations-console`
- Historical Streamlit visual-restyle candidate: `m3-streamlit-vercel-style-restyle`
- Promoted SCO governance candidate: `m3-ca-sco-source-governance`
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
- California SCO source-governance proposal CANONICAL + CI VERIFIED.
- SCO source registry entry exists but is `enabled: false` and `approved_for_use: false`.
- SCO source-access policy status is `PROPOSED`; real acquisition authorization is `false`.
- Approved real source count remains `0`.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

## California SCO governance promotion

Candidate branch: `m3-ca-sco-source-governance`.

Promoted SHA:
`463c6d6c972fa955a8aa0d3c97208c3029e202a8`

Before promotion the branch was 1 commit ahead and 0 behind canonical with merge-base at
`381381286414da888575a5da5a84e42f4ef0572c`.

Owner explicitly approved the fast-forward. The canonical branch was advanced without force to the
candidate SHA.

Candidate CI run `34825751270`: PASS.

Canonical post-promotion CI run `34826353694`: PASS.

Verified gates on the promoted SHA include:

- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- historical Next.js lint/typecheck/build regression gates PASS;
- Streamlit safety smoke PASS;
- Streamlit startup smoke PASS.

## Canonical SCO governance artifacts

- `schemas/common/source_access_governance.schema.json`
- `schemas/examples/ca_sco_source_governance.examples.json`
- `policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json`
- `sources/registry.yaml`
- `tests/contract/test_ca_sco_source_governance.py`
- `docs/audits/M3_CA_SCO_SOURCE_GOVERNANCE_PROPOSAL.md`

The governance contract deliberately separates source registration, evidence and approval. A
`PROPOSED` policy cannot authorize real acquisition.

## Current authoritative public-source facts

Verified from official California State Controller pages on 2026-09-14:

- the Controller publishes all records in its public unclaimed-property database in `.CSV` format;
- the official download page says the files are updated every Thursday;
- the download links displayed on the official SCO page point to `claimit.ca.gov`;
- SCO public-record access is subject to the California Public Records Act and applicable conditions;
- SCO privacy guidance states that personal information use is constrained by stated purposes/law,
  while website information is public domain and may be copied/used as permitted by law;
- CCP §1582 imposes separate downstream requirements on agreements to locate/recover unclaimed
  property, including timing/disclosure/payment conditions and a 10% fee cap for agreements covered
  by the statute.

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

Create an isolated candidate branch for a **California SCO approval-readiness evidence package**.

The bounded task must:

1. introduce a versioned machine-readable evidence/readiness contract;
2. record only facts already verified from official public pages;
3. explicitly record unresolved transport/privacy/retention/data-minimization controls;
4. keep `acquisition_performed = false` and `source_approved = false` as fail-closed invariants;
5. cross-check the existing registry entry and `PROPOSED` source-access policy;
6. add contract tests proving the evidence artifact cannot claim approval or completed acquisition;
7. perform no CSV download, no direct-file retrieval, no row parsing and no real PII processing;
8. keep beneficiary matching and outreach blocked;
9. keep `main` untouched.

After tests pass, commit/push the candidate and use GitHub CI as the full regression gate.
Do not promote the candidate into canonical without a later explicit owner gate.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
SCO governance SHA: 463c6d6c972fa955a8aa0d3c97208c3029e202a8
SCO candidate CI: 34825751270 PASS
SCO canonical post-promotion CI: 34826353694 PASS
SCO registry: DISABLED + NOT APPROVED
SCO policy: PROPOSED + NON-AUTHORIZING
Approved real sources: 0
Streamlit deployment branch: m2-state-governance-core (owner confirmed)
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: isolated M3 California SCO approval-readiness evidence package only
CONTEXT HEALTH: coherent; repository is source of truth
```
