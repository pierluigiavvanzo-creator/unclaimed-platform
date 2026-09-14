# M3 California SCO $500+ Data-Scope Inspection — Execution Evidence

Date: 2026-09-14

Status: **EXECUTED + STRUCTURE-ONLY SUCCESS — NON-AUTHORIZING**

## Execution identity

- Branch: `m3-ca-sco-500-plus-range-inspection`
- One-shot workflow commit: `40c5ff8c78cdf03f60dcce73ad1c12c5f4466994`
- Workflow run: `34864433849`
- Workflow conclusion: `success`
- Artifact ID: `10356079506`
- Artifact digest: `sha256:606923fdcf0b3090b63203c321c3d899633d940c5d4ad1d3fd265b0acb8b94d6`
- Persisted evidence file:
  `sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`
- Evidence JSON SHA-256 before repository persistence:
  `d4faa41885901551da378318a368d0f92f8b55de745710dcf5faf5edc53bf947`

## Authorized boundary

Execution used the explicit owner approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T17:21+02:00_BOUNDED_DATA_SCOPE_INSPECTION`.

The execution was limited to structure verification against the observed `$500 and up` SCO ZIP.
It did not authorize source approval, real-data ingestion, PII processing, identity resolution,
beneficiary matching, outreach, export, or claim activity.

## Transport result

The target transport metadata matched the bounded contract:

- endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- HTTP HEAD status: `200`;
- content type: `application/zip`;
- content length: `162,416,884` bytes;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- `Accept-Ranges: bytes`;
- last modified: `Wed, 09 Sep 2026 16:32:34 GMT`.

Range execution used exactly five successful HTTP `206` responses:

1. one 131,072-byte archive-tail request;
2. four 65,536-byte member-prefix requests.

Total source response-body bytes read: **393,216 bytes**.
The full 162 MB ZIP was not downloaded.

## Archive structure observed

The bounded ZIP structure parser found four non-encrypted, DEFLATED CSV members:

- `From_500_To_Beyond_1_of_4.csv`;
- `From_500_To_Beyond_2_of_4.csv`;
- `From_500_To_Beyond_3_of_4.csv`;
- `From_500_To_Beyond_4_of_4.csv`.

ZIP64 was not required. No unsafe path or unsupported compression stop condition fired.

## Header evidence observed

All four CSV members produced the same high-confidence first-record header candidate with 25 labels:

`PROPERTY_ID`, `PROPERTY_TYPE`, `CASH_REPORTED`, `SHARES_REPORTED`,
`NAME_OF_SECURITIES_REPORTED`, `NO_OF_OWNERS`, `OWNER_NAME`, `OWNER_STREET_1`,
`OWNER_STREET_2`, `OWNER_STREET_3`, `OWNER_CITY`, `OWNER_STATE`, `OWNER_ZIP`,
`OWNER_COUNTRY_CODE`, `CURRENT_CASH_BALANCE`, `NUMBER_OF_PENDING_CLAIMS`,
`NUMBER_OF_PAID_CLAIMS`, `HOLDER_NAME`, `HOLDER_STREET_1`, `HOLDER_STREET_2`,
`HOLDER_STREET_3`, `HOLDER_CITY`, `HOLDER_STATE`, `HOLDER_ZIP`, `CUSIP`.

Observed delimiter: comma. Observed candidate encoding: UTF-8.

The runner classified several labels as potential PII indicators. That classification is a
structure-level heuristic only; it is **not** a legal determination, does not prove that every field
is populated, and does not authorize processing of any record value.

## Safety result

Machine result:
`SUCCEEDED_STRUCTURE_ONLY`.

Verified safety state:

- stop reason: `null`;
- full archive downloaded: `false`;
- raw body persisted: `false`;
- temporary source files created: `false`;
- CSV data rows parsed: `0`;
- record values persisted: `false`;
- real PII processing authorized: `false`;
- identity resolution performed: `false`;
- beneficiary matching performed: `false`;
- outreach performed: `false`;
- source approved: `false`;
- source enabled: `false`.

## What this evidence resolves

Resolved:

- actual `$500+` ZIP member count and names;
- compression/encryption structure for the four members;
- consistent 25-column header candidate across all four CSV members;
- structure-level presence of owner/holder/address-related field labels;
- proof that the structure can be inspected with ~384 KiB rather than downloading the full archive.

Not resolved:

- data-row consistency or actual record values;
- whether candidate PII fields are populated in any specific record;
- necessity and proportionality of each field for the intended processing purpose;
- minimized production field whitelist;
- production retention duration/policy;
- trusted project privacy policy;
- real acquisition approval;
- source registry activation;
- insurance-specific filtering logic.

## Cleanup

The network-capable workflow is removed in the same evidence-closure commit. Contract tests require
that `.github/workflows/ca-sco-500-plus-data-scope-once.yml` is absent after evidence capture.

## Next bounded product action

No additional source-body access is required for the next step.

Use the verified 25-label structure to prepare a **field-minimization + PII-necessity + retention/privacy
readiness proposal** for the `$500+` pilot. That proposal must remain non-authorizing and must select
only fields justified by the product purpose before any real row-level acquisition is considered.
