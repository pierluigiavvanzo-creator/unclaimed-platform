# M3 California SCO $500+ Data-Scope Inspection Contract

Date: 2026-09-14

Status: **PROPOSAL ONLY — NON-AUTHORIZING — RANGE EXECUTION SEPARATELY GATED**

## Purpose

Bind the already-approved M3 structure-inspection strategy to the observed official California SCO
`$500 and up` segment instead of the 3.2 GB `All properties` object.

## Evidence basis

The segment was discovered from the official SCO download page and observed by metadata-only `HEAD`
preflight under owner approval. Current transport evidence fixes:

- endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- HTTP status: `200`;
- content type: `application/zip`;
- content length: `162,416,884` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- response body bytes read: `0`.

The selected object is about 5.1% of the observed `All properties` byte size and is the smallest of the
four official value-segment ZIPs. Prioritizing it for the pilot is a product inference, not a claim by
SCO that every record is commercially viable or life-insurance related.

## Contract-first controls

New contracts:

- `schemas/common/source_data_scope_segment_inspection_proposal.schema.json`;
- `schemas/common/source_data_scope_inspection_execution.schema.json`;
- `sources/proposals/ca_sco_segment_500_plus.data_scope_inspection.v1.json`;
- `tests/contract/test_ca_sco_segment_500_plus_data_scope_contract.py`.

The proposal remains fixed to:

- source approved `false`;
- source enabled `false`;
- real acquisition authorized `false`;
- network execution authorized `false`;
- network request performed `false`;
- body access performed `false`;
- body bytes read `0`.

## Bounded execution design

A later explicitly approved execution may use only HTTP Range GET against the exact observed `$500+`
object. It may inspect ZIP central-directory structure and a bounded prefix of CSV candidate members.

Hard limits:

- 128 KiB archive-tail probe;
- 4 MiB maximum central-directory read;
- maximum 10 CSV candidates;
- 1 MiB absolute member-response cap;
- actual initial member probe only 64 KiB;
- 64 KiB maximum decompressed first-record output;
- maximum 12 range requests;
- maximum 14,811,136 response-body bytes across the execution.

The implementation must stop if transport metadata drifts, Range is ignored, ZIP64 is required,
archive paths are unsafe, encryption/unsupported compression appears, limits are exceeded, or a CSV
header cannot be established without progressing into a data row.

## Privacy boundary

Only derived structure metadata and high-confidence header-label candidates may be persisted. Source
body bytes remain in memory only. CSV data rows are fixed to zero. Record values, identity resolution,
beneficiary matching, export and outreach remain prohibited.

Potential PII indicators derived from field labels are classification hints only and are not a legal
or necessity determination.

## Stop condition

No Range GET is authorized by this proposal artifact itself. Execution requires the separately scoped
owner approval reference associated with the current strategy instruction and must remain within the
machine-enforced execution contract.
