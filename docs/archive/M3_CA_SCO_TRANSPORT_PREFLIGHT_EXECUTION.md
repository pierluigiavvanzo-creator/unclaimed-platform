# M3 California SCO Transport-Preflight Execution

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANONICAL + CI VERIFIED — METADATA ONLY — REAL ACQUISITION BLOCKED**

## Owner gate

The owner explicitly authorized one bounded California SCO metadata-only transport preflight after
confirming that the external Vercel account had been deleted.

Execution approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

The approval was limited to one transport metadata preflight. It did not approve the source, enable
the registry, authorize dataset acquisition, authorize response-body access, authorize PII processing,
beneficiary matching, outreach, or any downstream legal/commercial action.

## Promotion result

Candidate branch:
`m3-ca-sco-transport-preflight-execution`

Canonical parent before candidate:
`50887231d39eff793b1968b4a062292533205602`

Execution commit:
`7d89ec664992a30b5270be8da4c2616254747e59`

Evidence commit:
`2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`

Promoted transport-evidence baseline:
`60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a`

Canonical branch:
`m2-state-governance-core`

Promotion was a non-force fast-forward. Before promotion, candidate ancestry was verified as 4 commits
ahead, 0 behind, with merge base exactly equal to canonical parent
`50887231d39eff793b1968b4a062292533205602`.

Canonical post-promotion CI:
`34840001821` — PASS for both `quality` and `streamlit-candidate`.

## Controls fixed before network access

- official source page: `https://www.sco.ca.gov/upd_download_property_records.html`;
- target link label: `All properties`;
- endpoint discovery: exactly one matching HTML anchor on the official source page;
- allowlisted download host: `claimit.ca.gov` only;
- download-endpoint method: `HEAD` only;
- HTTPS only;
- timeout: 10 seconds per request;
- maximum redirects followed: 3;
- redirects outside HTTPS + `claimit.ca.gov` blocked fail-closed;
- response-body bytes allowed/read: `0`;
- no response-body persistence or parsing;
- no dataset artifact persistence;
- no real PII, beneficiary matching, or outreach.

## Test-first gate result

The one-time workflow ran targeted contract tests before the network job. Validation passed before the
preflight job started.

The first workflow attempt on commit `3c3dfe3fd15a65b96b9e4e55e6c518932bbba80d` created no jobs and
performed no SCO download-endpoint request. The corrected execution commit fixed workflow/lint defects
without relaxing network safety constraints.

One-shot workflow run:
`34838890387` — PASS.

## Observed transport evidence

At `2026-09-14T11:34:58.210154Z`, the runner extracted the `All properties` link from the official SCO
page and issued one `HEAD` request to:

`https://claimit.ca.gov/upd-property-records/00_All_Records.zip`

Observed metadata:

- final host: `claimit.ca.gov`;
- HTTP status: `200`;
- redirect count: `0`;
- TLS scheme: `https`;
- content type: `application/zip`;
- content length: `3,203,972,130` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"0ce16eb75bbbe7018639c7a71e802008"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:37 GMT`;
- response-body bytes read: `0`.

The SCO public page describes public records as downloadable CSV data, while the observed
`All properties` transport object is currently a ZIP resource advertising `application/zip`. Because
the archive body was not downloaded or opened, this audit makes no assertion about files, columns,
row layout or schema inside the ZIP.

Machine-readable evidence:
`sources/evidence/ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json`

## Safety result

Canonical evidence requires:

- `acquisition_performed = false`;
- `source_approved = false`;
- `source_enabled = false`;
- `response_body_bytes_read = 0`;
- no response-body persistence/parsing;
- no dataset artifact persistence;
- no real PII processed;
- no beneficiary matching;
- no outreach.

`sources/registry.yaml` remains `enabled: false` and `approved_for_use: false`.
The source-access policy remains `PROPOSED`, with real acquisition, matching, outreach and PII still
unauthorized.

## One-time execution closure

The temporary workflow `.github/workflows/ca-sco-transport-preflight-once.yml` was removed before
promotion. Contract tests require it to remain absent, preventing later pushes from repeating the
network call automatically.

## What this establishes

The preflight resolves transport evidence only:

- exact current `All properties` endpoint identity;
- host and HTTPS scheme;
- direct HTTP 200 with no redirect observed;
- actual advertised media type at the transport boundary;
- actual advertised content length at observation time;
- selected object metadata;
- bounded timeout/method/allowlist controls proven executable.

It does **not** establish or authorize:

- source approval or registry activation;
- safe maximum bytes for a future real acquisition;
- production retention/privacy/data-minimization policy;
- download or persistence of the ZIP;
- ZIP contents, CSV layout, column names or row schema;
- real-data normalization;
- PII necessity or processing;
- beneficiary matching;
- outreach or claims activity.

## Next gate

The next repository task may only prepare a non-authorizing California SCO source-approval readiness
package. It may reuse this canonical transport evidence but must perform no new network request and no
data retrieval. Any transition to `APPROVED`, registry activation, bounded real retrieval, archive
inspection, PII processing, matching or outreach requires a separate explicit owner gate.
