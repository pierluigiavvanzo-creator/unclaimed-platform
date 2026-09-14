# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, California SCO source
governance, approval-readiness evidence, transport-preflight proposal, bounded transport evidence, and
the non-authorizing California SCO source-approval readiness package are canonical and CI verified on
`m2-state-governance-core`.

The promoted source-approval package baseline is:
`41dfc61cd96d7573cdd67c37631567ef5343fcdd`.

Canonical post-promotion CI:
`34853561664` — PASS for both `quality` and `streamlit-candidate`.

The California SCO source remains `enabled: false` and `approved_for_use: false`. The source-access
policy remains `PROPOSED`; real acquisition, real PII processing, beneficiary matching and outreach
remain unauthorized.

Streamlit Community Cloud remains the active reviewer deployment target. Repository-side Vercel
runtime/deployment integration remains decommissioned and CI guarded. `main` remains unchanged at
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`. Supabase remains untouched.

## Canonical California SCO Transport Evidence

Canonical transport observation remains:

- endpoint: `https://claimit.ca.gov/upd-property-records/00_All_Records.zip`;
- method used for preflight: `HEAD`;
- final host: `claimit.ca.gov`;
- HTTP status: `200`;
- redirects: `0`;
- TLS: `https`;
- content type: `application/zip`;
- content length: `3,203,972,130` bytes;
- response-body bytes read: `0`.

No ZIP/CSV body has been downloaded or opened. Archive contents, CSV fields, row layout and record
schema remain unverified.

## Canonical Source-Approval Readiness Package

Canonical artifacts:

- `schemas/common/source_approval_package.schema.json`;
- `schemas/examples/ca_sco_source_approval_package.examples.json`;
- `sources/proposals/ca_sco_unclaimed_property_bulk.source_approval_package.v1.json`;
- `tests/contract/test_ca_sco_source_approval_package.py`;
- `docs/audits/M3_CA_SCO_SOURCE_APPROVAL_PACKAGE.md`.

The package remains fixed to `READINESS_PROPOSAL_NOT_AUTHORIZED` with readiness decision
`BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION`.

It proposes only `SOURCE_STRUCTURE_VERIFICATION_ONLY` as the narrow processing purpose and the
high-level category `PUBLIC_UNCLAIMED_PROPERTY_BULK_ARCHIVE`. It does not invent record-level field
names: `proposed_allowed_fields` remains empty and field scope remains
`BLOCK_UNTIL_ROW_SCHEMA_VERIFIED`.

PII necessity remains `UNDETERMINED_BLOCKING` with `allow_pii = false`.

Proposed privacy prerequisites include quarantine, encryption at rest, least privilege, access
logging, no record-level processing, no export, no matching, no outreach, and delete-on-validation
failure. Production retention duration and trusted project privacy-policy references remain null and
blocking.

Proposed transport bounds reuse canonical evidence only:

- HTTPS only;
- host `claimit.ca.gov`;
- same-host redirects only;
- 10-second per-request network-inactivity timeout;
- expected media type `application/zip`;
- content length required;
- max bytes `3,203,972,130`, equal to the observed content length with no invented growth tolerance;
- endpoint/media-type/content-length drift blocks and requires new review.

## Verification Evidence

- Canonical transport-evidence baseline: `60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a`.
- Canonical transport post-promotion CI `34840001821`: PASS.
- Canonical transport closure CI `34840291103`: PASS.
- Source-approval package functional commit: `4250291d24286be2e0d4cb1a12de0960cc3faa90`.
- Source-approval package candidate closure: `41dfc61cd96d7573cdd67c37631567ef5343fcdd`.
- Candidate CI `34843714665`: PASS.
- Candidate closure CI `34843990986`: PASS.
- Canonical post-promotion CI `34853561664`: PASS.
- Ruff, mypy, contract tests, smoke tests, full pytest: PASS.
- Legacy frontend lint/typecheck/build: PASS.
- Streamlit safety/startup smoke: PASS.
- Approved real sources: `0`.
- Network requests in the source-approval package task: `0`.
- No real dataset body downloaded, persisted or parsed.
- No real PII processed.

## Blocked / Not Authorized

- Source policy transition from `PROPOSED` to `APPROVED`.
- SCO registry activation for real use.
- Any new SCO network request or ZIP/CSV download without a separate explicit owner gate.
- Record-level field authorization before verified row schema exists.
- PII authorization before PII presence/necessity is determined.
- Real acquisition before a production retention policy and trusted project privacy policy exist.
- Beneficiary matching, outreach, claimant verification, fee agreements or claim submission.
- Reintroduction of Vercel repository/runtime deployment integration without a new owner decision.
- Promotion to `main` without a separate stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Remaining Readiness Gaps

- verified ZIP contents and CSV row layout;
- minimized record-level field whitelist;
- PII presence and necessity determination;
- selected production retention duration/policy;
- selected trusted project privacy policy;
- reviewed real-acquisition client implementation;
- explicit human source-approval reference;
- artifact hash/revision from a separately authorized real download;
- durable production audit persistence;
- physical retention enforcement and first PostgreSQL/Alembic application migration.

## Next Recommended Action

Create an isolated **California SCO data-scope inspection proposal only**. The proposal should define a
bounded archive/CSV-structure inspection sufficient to verify internal file names, CSV headers/row
layout and PII presence indicators while remaining non-authorizing and performing no network request.
It must specify byte/range limits, streaming/no-partial-persistence rules, privacy quarantine, outputs,
stop conditions and a separate explicit owner execution gate. Do not retrieve or open the archive
until that later human gate is satisfied.
