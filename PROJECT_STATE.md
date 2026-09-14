# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, California SCO source
governance, approval-readiness evidence, transport-preflight proposal/execution evidence, and the
non-authorizing source-approval readiness package are canonical and CI verified on
`m2-state-governance-core`.

Canonical HEAD before the current candidate:
`c832b447cbe37482fdc4273eb1b163ce9299edf3`.

A new isolated candidate branch, `m3-ca-sco-data-scope-inspection-proposal`, contains a strictly
non-authorizing California SCO data-scope inspection proposal. Functional candidate commit:
`2df97f9dbab16ba0e30ec07a590657b381eb8c8b`.

Candidate CI run `34855459255` passed both `quality` and `streamlit-candidate`.

No SCO network request or archive/body access occurred. The source remains `enabled: false` and
`approved_for_use: false`; the source-access policy remains `PROPOSED`; real acquisition, real PII
processing, beneficiary matching and outreach remain unauthorized.

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
- `Accept-Ranges: bytes` observed;
- response-body bytes read: `0`.

No ZIP/CSV body has been downloaded or opened. Archive contents, CSV fields, row layout and record
schema remain unverified.

## Current Candidate — Data-Scope Inspection Proposal

New artifacts:

- `schemas/common/source_data_scope_inspection_proposal.schema.json`;
- `schemas/examples/ca_sco_data_scope_inspection_proposal.examples.json`;
- `sources/proposals/ca_sco_unclaimed_property_bulk.data_scope_inspection.v1.json`;
- `tests/contract/test_ca_sco_data_scope_inspection_proposal.py`;
- `docs/audits/M3_CA_SCO_DATA_SCOPE_INSPECTION_PROPOSAL.md`.

The proposal is fixed to `PROPOSAL_ONLY_NOT_AUTHORIZED` with:

- source approved: `false`;
- source enabled: `false`;
- real acquisition authorized: `false`;
- network execution authorized: `false`;
- network request performed: `false`;
- body access performed: `false`;
- body bytes read: `0`;
- execution approval reference: `null`;
- next gate: `HUMAN_DATA_SCOPE_INSPECTION_EXECUTION`.

## Proposed Bounded Inspection

The proposal permits a later separately authorized execution to derive only archive/member structure
and CSV header-candidate evidence. CSV data rows and record values remain prohibited.

Project safety caps, explicitly not source facts:

- archive tail suffix: `131,072` bytes;
- central directory: max `4,194,304` bytes;
- maximum archive members: `10,000`;
- maximum CSV candidates: `10`;
- member response prefix: max `1,048,576` bytes each;
- decompressed prefix: max `65,536` bytes each;
- logical CSV records parsed: max `1` per member;
- data rows parsed: `0`;
- max range requests: `12`;
- max total source response-body bytes: `14,811,136`.

Transport proposal requires HTTPS, `claimit.ca.gov`, same-host redirects, 10-second per-request
network-inactivity timeout, `application/zip`, exact current content length, `Accept-Ranges: bytes`,
and HTTP range GET only. Full-body requests are prohibited.

Privacy controls require quarantine, in-memory-only source-byte handling, no temporary source files,
no raw ZIP/member/header persistence, no body/record values in logs, least privilege, access logging,
encryption at rest for any derived evidence, deletion of transient buffers, no export, no matching and
no outreach.

PII indicators, if a later execution is approved, may be derived from header labels only and are not a
legal determination. If a data row would be required, the inspection must stop.

## Verification Evidence

- Canonical source-approval package baseline: `41dfc61cd96d7573cdd67c37631567ef5343fcdd`.
- Canonical source-approval package CI `34853561664`: PASS.
- Canonical package promotion closure: `c832b447cbe37482fdc4273eb1b163ce9299edf3`.
- Data-scope proposal functional commit: `2df97f9dbab16ba0e30ec07a590657b381eb8c8b`.
- Data-scope proposal candidate CI `34855459255`: PASS.
- Pre-closure candidate compare: 1 commit ahead / 0 behind canonical with exact canonical merge-base.
- Exactly five proposal/test/audit files added before closure; no runtime/policy/registry changes.
- Ruff, mypy, contract tests, smoke tests, full pytest: PASS.
- Legacy frontend lint/typecheck/build: PASS.
- Streamlit safety/startup smoke: PASS.
- Approved real sources: `0`.
- Network requests in this proposal task: `0`.
- Source body bytes read in this proposal task: `0`.
- No real PII processed.

## Blocked / Not Authorized

- Execution of the data-scope inspection without a separate explicit owner gate.
- Any SCO range GET, ZIP/CSV body access or archive opening under the current proposal task.
- Source policy transition from `PROPOSED` to `APPROVED`.
- SCO registry activation for real use.
- CSV data-row or record-value access.
- Record-level field authorization before verified structure evidence exists.
- PII authorization before PII presence/necessity is determined.
- Beneficiary matching, identity resolution, outreach, claimant verification, fee agreements or claim submission.
- Promotion to `main` without a separate stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Remaining Readiness Gaps

- promotion of this non-authorizing proposal if owner approves;
- separately authorized bounded structure inspection;
- verified archive member names and CSV header/row-layout evidence;
- minimized record-level field whitelist;
- PII presence and necessity determination;
- selected production retention duration/policy;
- selected trusted project privacy policy;
- reviewed real-acquisition client implementation;
- explicit human source-approval reference;
- artifact hash/revision from a later separately authorized real acquisition;
- durable production audit persistence;
- physical retention enforcement and first PostgreSQL/Alembic application migration.

## Next Recommended Action

**Human promotion gate only:** decide whether to promote candidate branch
`m3-ca-sco-data-scope-inspection-proposal` into canonical `m2-state-governance-core`.

Promotion records only the non-authorizing inspection proposal. It must not run any request or body
inspection. After promotion, a separate human execution gate is still required before any bounded
range access can occur.
