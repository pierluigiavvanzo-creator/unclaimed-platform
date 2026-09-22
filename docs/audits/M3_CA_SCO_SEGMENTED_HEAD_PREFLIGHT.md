# M3 California SCO Segmented HEAD Preflight

Date: 2026-09-14

Class: **A — Product Critical**

Status: **EXECUTED + METADATA ONLY — ZERO DATASET BODY BYTES — NON-AUTHORIZING**

## Objective

Reduce M3 pilot transfer cost before any archive inspection or real acquisition by measuring the four official California SCO value-segment ZIPs with bounded metadata-only `HEAD` requests.

Owner approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T17:21+02:00_SEGMENTED_HEAD_PREFLIGHT`.

## Official source structure

The official SCO download page exposes four segmented links plus the full archive:

- `$.00 to $9.99`;
- `$10 to $99.99`;
- `$100 to $499.99`;
- `$500 and up`;
- `All properties`.

The segmented endpoints were discovered from the official page HTML by the existing canonical preflight script. No endpoint was invented.

## REUSE FIRST

Reused:

- `scripts/ca_sco_transport_preflight.py`;
- `schemas/common/source_transport_preflight_execution.schema.json`;
- existing allowlist/HTTPS/redirect/body-zero controls;
- canonical full-archive transport evidence.

No new downloader or network client was introduced.

## Execution

GitHub Actions run:
`34862117709` — SUCCESS.

One-shot workflow commit:
`497c788d3bb39c59f140ff43f908285d17f55be9`.

The workflow ran four separately validated metadata-only preflights. Each target returned:

- HTTP `200`;
- `application/zip`;
- `Accept-Ranges: bytes`;
- zero redirects;
- `response_body_bytes_read = 0`;
- acquisition `false`;
- source approved `false`;
- PII processed `false`;
- matching/outreach `false`.

## Observed segment sizes

| Official segment | Endpoint suffix | Content-Length |
|---|---|---:|
| `$.00 to $9.99` | `01_From_0_To_Below_10.zip` | `1,321,027,390` bytes |
| `$10 to $99.99` | `02_From_10_To_Below_100.zip` | `1,261,492,445` bytes |
| `$100 to $499.99` | `03_From_100_To_Below_500.zip` | `459,105,796` bytes |
| `$500 and up` | `04_From_500_To_Beyond.zip` | `162,416,884` bytes |

Canonical `All properties` baseline:
`3,203,972,130` bytes.

The `$500 and up` object is about 5.1% of the observed full-archive byte size and is the smallest of the four official value-segment objects.

## Product inference / pilot selection

**Inference, not a source fact:** prioritize the official `$500 and up` segment for the first M3 structure-inspection and later pilot-acquisition path because it combines the highest value band exposed by SCO with the smallest observed transfer footprint.

This does not claim every `$500+` record is commercially viable, does not prove life-insurance relevance, and does not permanently exclude lower-value segments. A15 economics and later domain gates remain responsible for case-level value decisions.

`All properties` remains the completeness/reference source, not the initial operational transfer target.

## Safety state

This task did not:

- download any ZIP;
- read any dataset body byte;
- inspect archive members;
- parse CSV headers or rows;
- process real PII;
- approve the source;
- enable the registry;
- perform identity resolution, matching or outreach.

## Evidence files

- `sources/evidence/ca_sco_segment_00_to_9_99.transport_preflight.execution.v1.json`;
- `sources/evidence/ca_sco_segment_10_to_99_99.transport_preflight.execution.v1.json`;
- `sources/evidence/ca_sco_segment_100_to_499_99.transport_preflight.execution.v1.json`;
- `sources/evidence/ca_sco_segment_500_plus.transport_preflight.execution.v1.json`.

All validate against the existing `SourceTransportPreflightExecution` v1 contract.

## Next bounded action

Retarget the already-governed data-scope inspection concept to the observed `$500 and up` endpoint and perform only the separately approved HTTP Range structure inspection. Full-body download remains prohibited.
