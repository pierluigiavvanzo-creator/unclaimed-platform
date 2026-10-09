# M3 California SCO PROPERTY_TYPE Authority Archival Execution Authorization

Date: 2026-09-15

## Status

`PENDING_HUMAN_AUTHORIZATION`

This artifact was prepared offline after the bounded authority provenance proposal review passed. No authority request, download, SCO dataset access, source-row access, or semantic execution was performed while preparing it.

## Fresh approval required

Gate:
`HUMAN_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_AUTHORIZATION_REVIEW`

Required approval reference:
`APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

The approval must be fresh, single-use, non-reusable, and must pin the CI-verified authorization-artifact SHA. Previous semantic execution/privacy approvals remain consumed and cannot be reused.

## Requested one-shot scope

If and only if a later human review grants the fresh approval, the execution may target only the single SCO authority PDF already present in the reviewed proposal. The reviewed boundary remains one exact HTTPS GET, no redirects, no retries, a 16 MiB project safety cap, HTTP 200, PDF content-type and PDF-magic validation, immutable raw archival, and SHA-256 provenance metadata.

No additional authority discovery, SCO dataset access, `claimit.ca.gov` access, source-row access, semantic extraction, parser/regex/normalization change, source approval, registry activation, production classification, or third semantic execution is included.

## Archive contract

Successful execution must archive the raw PDF unchanged at the content-addressed path defined by the reviewed proposal and write the versioned archive metadata artifact. The archive itself does not prove any semantic claim.

After a successful archive, the next gate is:
`HUMAN_PROPERTY_TYPE_AUTHORITY_ARCHIVE_PROVENANCE_REVIEW`

## Current non-authorization

The prepared artifact itself has `network_execution_authorized=false` and `workflow_creation_authorized=false`. No network workflow or approval evidence is created by this preparation step.
