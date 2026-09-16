# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | TRANSPORT + ARCHIVE-LAYOUT BASELINE REFRESH PROPOSAL PREPARED; HUMAN REVIEW NEXT | v1.2 one-shot drift evidence accepted; no rebaseline or retry; bounded structural design only |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- runner output contract remains `1.2.0`;
- authorized v1.2 one-shot execution performed exactly once;
- result: `STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`;
- one-shot evidence human-reviewed and accepted;
- consumed execution/privacy approvals remain non-reusable;
- no retry authorized;
- no source body or row was read in the stopped execution;
- semantic compatibility remains unresolved.

## Baseline Refresh Proposal

Completed:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

Proposal branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`

Base checkpoint:

`9dbdc3c6f1ef05c577c26c9e3524ba74fdbfda56`

Base CI:

`35125609902` — **SUCCESS**

Artifacts:

- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`;
- `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`;
- `schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`;
- `tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`.

Status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

## Proposal Decision Map

Rejected by design:

- `HEAD_ONLY_TRANSPORT_REFRESH` — cannot establish member offsets;
- `ARITHMETIC_MEMBER_OFFSET_REBASE` — unsupported inference;
- `FULL_ARCHIVE_DOWNLOAD_AND_INSPECTION` — scope too broad.

Proposed for human review:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

The later design would use:

1. one HEAD observation for transport identity;
2. bounded tail/EOCD/central-directory Range reads for structural ZIP metadata only.

No decompression, CSV parsing, row/field inspection, full archive download, automatic widening or automatic retry is allowed.

## Preserved Request / Byte Caps

- HEAD requests max: `1`;
- Range requests max: `4`;
- HTTP requests max total: `5`;
- Range response max each: `131072` bytes;
- source response-body max total: `524288` bytes.

Failure to resolve a classic ZIP central directory within these limits must stop fail-closed and cannot trigger an implicit larger read.

## Candidate Baseline Boundary

Observed one-shot drift values remain evidence only:

- observed content length: `162560390`;
- observed ETag: `"222dd79f04c2a0a8fff166b01c8da746"`.

Historical pinned values remain stale for future execution planning, not proven invalid:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- member offsets: `0`, `59747797`, `96862896`, `134174190`.

Replacement values are all still `null` and no baseline has been adopted.

## Authorization / Privacy Boundary

The proposal itself performs no network request and grants no approval.

Any later structural revalidation requires fresh single-use:

- execution approval;
- structural-byte privacy approval.

Structural bytes must remain memory-only with zero retention. Raw Range bytes may not persist; compressed payload may not be decompressed or interpreted; CSV rows and protected fields may not be inspected.

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

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

The review is repository-only. It must not perform network/source access, grant fresh approvals, create a network workflow, retry the prior run, update runner constants or adopt candidate baseline values.
