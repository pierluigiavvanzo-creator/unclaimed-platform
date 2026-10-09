# M3 California SCO PROPERTY_TYPE Authority Archival Execution

Date: 2026-09-15

## Result

`SUCCESS_ONE_SHOT_ARCHIVED`

Execution branch:
`m3-ca-sco-property-type-authority-archival-execution-one-shot`

Execution workflow run:
`35012019831`

Authorization artifact package SHA:
`d20bc80f50af56c10085eec7123aa0691e26ea1a`

Fresh approval:
`APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

Approval state after execution:
`CONSUMED`

## Network boundary actually used

The execution performed exactly the reviewed authority retrieval shape:

- method: `GET`
- requested URL: `https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`
- final URL: identical to requested URL
- HTTP status: `200`
- redirects: `0`
- retries: `0`
- content type: `application/pdf`
- body bytes: `329585`
- project body cap: `16777216`
- PDF magic validation: passed

A prior local capability attempt failed at DNS resolution before any HTTP request was issued. It did not consume the one-shot approval. The actual approved authority GET was executed once in GitHub Actions run `35012019831` after the approval evidence had been marked consumed.

## Immutable archive

SHA-256:
`7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5`

Archive path:
`sources/authority/ca/sco/upd_naupa_ii_codes_dormancy_periods/7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5.pdf`

Provenance metadata:
`sources/evidence/ca_sco_property_type_authority_archive.v1.json`

Approval evidence:
`sources/evidence/ca_sco_property_type_authority_archival_execution_approval.v1.json`

## Semantic boundary

No semantic extraction or interpretation was performed during retrieval or archival.

The archive itself does not establish any PROPERTY_TYPE semantic claim. No parser, regex, trimming, casing, normalization, source-policy, registry or production-classification change is authorized by this execution.

## Next gate

Perform only:
`HUMAN_PROPERTY_TYPE_AUTHORITY_ARCHIVE_PROVENANCE_REVIEW`

That review may inspect the archived authority for the previously unresolved provenance questions. Until that review completes, semantic compatibility remains unresolved and all downstream gates remain closed.
