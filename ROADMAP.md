# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | TRANSPORT + ARCHIVE-LAYOUT REFRESH PROPOSAL REVIEW PASS; FRESH AUTHORIZATION NEXT | bounded classic-ZIP structural design accepted; network revalidation still not authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- runner output contract remains `1.2.0`;
- v1.2 one-shot execution performed exactly once;
- one-shot result: `STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`;
- one-shot evidence human-reviewed and accepted;
- consumed execution/privacy approvals remain non-reusable;
- no retry authorized;
- no source body or row was read during the stopped one-shot;
- semantic compatibility remains unresolved.

## Transport + Archive-Layout Proposal Review

Completed:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

Reviewed proposal branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`

Reviewed proposal HEAD:

`359b1c1a86d34edabcd028e5e5fbb6fc3acba781`

Reviewed proposal CI:

`35139290645` — **SUCCESS**

Review result:

`PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW.md`

## Accepted Design

Accepted for a later separately authorized gate:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

The design permits only:

1. one exact-endpoint HEAD observation;
2. bounded classic-ZIP tail/EOCD/central-directory metadata Range reads;
3. candidate derivation of canonical local-header offsets from central-directory metadata;
4. privacy-safe derived evidence persistence;
5. human evidence review before any baseline adoption.

Rejected:

- HEAD-only transport refresh;
- arithmetic member-offset rebasing;
- full archive download and inspection.

## Preserved Request / Byte Caps

- HEAD requests max: `1`;
- Range requests max: `4`;
- HTTP requests max total: `5`;
- Range response max each: `131072` bytes;
- source response-body max total: `524288` bytes;
- full-body fallback: `false`;
- automatic widening: `false`;
- automatic retry: `false`.

Classic ZIP only. ZIP64, multi-disk, missing/ambiguous EOCD, identity drift, missing/duplicate canonical members or inability to complete inside these caps must stop fail-closed.

## Baseline Boundary

Historical transport and member-offset pins remain stale for future execution planning but not proven invalid.

The one-shot observed content length `162560390` and ETag `"222dd79f04c2a0a8fff166b01c8da746"` remain evidence only.

Replacement content length, ETag and all four member offsets remain `null`. No baseline has been adopted.

## Authorization / Privacy Boundary

The review grants no approval and performs no source access.

Any later bounded structural revalidation requires fresh single-use:

- execution approval;
- structural-byte privacy approval.

Structural Range bytes must be memory-only with zero retention. No raw byte persistence, decompression, CSV parsing, row inspection or protected-field observation is allowed.

## Runtime / Source Governance

No change to:

- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- canonical member offsets;
- parser/projector;
- regex or normalization;
- D-008 handling;
- source policy;
- registry.

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain `0`; production classification and all identity/genealogy/matching/outreach/claim gates remain inactive.

## Next Product Work

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

That gate is repository-only and may decide whether to grant fresh single-use execution and structural-byte privacy approvals. It must remain separate from the network execution itself.
