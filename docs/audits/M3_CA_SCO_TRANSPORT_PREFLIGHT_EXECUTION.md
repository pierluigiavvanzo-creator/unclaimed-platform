# M3 California SCO Transport-Preflight Execution

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANDIDATE OBSERVATION CAPTURED — METADATA ONLY — NEW HUMAN GATE REQUIRED**

## Owner gate

The owner explicitly authorized proceeding with one bounded California SCO transport-preflight task
after confirming that the external Vercel account had been deleted.

Execution approval reference:

`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

This approval was limited to one transport metadata preflight. It did not approve the source, enable
the registry, authorize dataset acquisition, authorize response-body access, authorize PII processing,
beneficiary matching, outreach, or any downstream legal/commercial action.

## Starting point

- Canonical development branch before this candidate: `m2-state-governance-core`.
- Canonical parent SHA: `50887231d39eff793b1968b4a062292533205602`.
- Candidate branch: `m3-ca-sco-transport-preflight-execution`.
- Execution commit: `7d89ec664992a30b5270be8da4c2616254747e59`.
- Canonical proposal: `sources/proposals/ca_sco_unclaimed_property_bulk.transport_preflight.v1.json`.
- One-time workflow run: `34838890387`.

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

The one-time workflow ran targeted contract tests before the network job. The `validate` job completed
successfully. Only after that success did the `preflight` job start.

The first workflow attempt on commit `3c3dfe3fd15a65b96b9e4e55e6c518932bbba80d` created no jobs and
therefore performed no SCO download-endpoint request. The regular CI for that commit also stopped at
Ruff before tests. The corrected execution commit fixed only workflow/lint defects; the network safety
constraints were not relaxed.

## Observed transport evidence

At `2026-09-14T11:34:58.210154Z`, the runner extracted the `All properties` link from the official SCO
page and issued one `HEAD` request to the discovered HTTPS endpoint.

Observed endpoint:

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

The SCO public page describes the public records as downloadable CSV data, while the currently
observed `All properties` transport endpoint is a ZIP resource and advertises `application/zip`.
Because the archive body was not downloaded or opened, this task does not assert what files or row
layout are inside that ZIP.

Machine-readable candidate evidence:

`sources/evidence/ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json`

## Safety result

The observation explicitly records:

- `acquisition_performed = false`;
- `source_approved = false`;
- `source_enabled = false`;
- `response_body_bytes_read = 0`;
- no response-body persistence/parsing;
- no dataset artifact persistence;
- no real PII processed;
- no beneficiary matching;
- no outreach.

`sources/registry.yaml` remains `enabled: false` and `approved_for_use: false` for the SCO source.
The source-access policy remains `PROPOSED`, with real acquisition, matching, outreach and PII still
unauthorized.

## One-time execution closure

The temporary workflow `.github/workflows/ca-sco-transport-preflight-once.yml` is removed immediately
after capturing this observation. Contract tests require it to remain absent, preventing later pushes
from repeating the network call accidentally.

## What this establishes

The preflight resolves transport evidence only:

- exact current `All properties` endpoint identity;
- host and HTTPS scheme;
- direct 200 response with no redirect observed;
- actual advertised media type at the transport boundary;
- actual advertised content length at the observation time;
- selected cache/object metadata;
- bounded timeout/method/allowlist controls proven executable.

It does **not** establish or authorize:

- source approval or registry activation;
- a safe maximum acquisition size;
- a production retention/privacy/data-minimization policy;
- download or persistence of the ZIP;
- ZIP contents, CSV layout, column names, or row schema;
- real-data normalization;
- PII necessity or processing;
- beneficiary matching;
- outreach or claims activity.

## Stop condition

Stop at a new human gate after candidate CI verification. No further request to the observed download
endpoint is authorized by this execution approval. Any source approval, registry activation, bounded
real retrieval, archive inspection, row-layout verification, or downstream processing requires a new
explicit owner decision and the corresponding governance update.
