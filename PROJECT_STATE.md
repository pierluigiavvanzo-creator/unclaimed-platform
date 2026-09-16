# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

California SCO `PROPERTY_TYPE` handling remains governed by `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`, accepted policy `WHOLE_SOURCE_STOP`, implementation strategy `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`, and runner output contract `1.2.0`.

The v1.2 implementation, one-shot real-source execution and human execution-evidence review remain complete. The one-shot result remains:

`STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`

The subsequent repository-only baseline-refresh proposal is now prepared and awaits human review.

## Current Proposal Checkpoint

Proposal branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`

Proposal base:

`9dbdc3c6f1ef05c577c26c9e3524ba74fdbfda56`

Base CI:

`35125609902` — **SUCCESS**

Completed action:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

Proposal artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`

Machine contract:

- `schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`
- `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`
- `tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

## Evidence Basis

Human evidence-review result remains:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

Persisted execution evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Execution result:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`;
- HEAD requests: `1`;
- Range requests: `0`;
- source body bytes read: `0`;
- rows examined: `0`.

Historical pinned transport identity:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- content type `application/zip`;
- Accept-Ranges `bytes`.

Observed one-shot HEAD evidence:

- HTTP `200`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Observed values remain evidence only and are not adopted as a replacement baseline.

## Historical Archive-Layout State

Historical canonical member offsets remain:

1. `From_500_To_Beyond_1_of_4.csv` → `0`;
2. `From_500_To_Beyond_2_of_4.csv` → `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` → `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` → `134174190`.

They remain `STALE_FOR_FUTURE_EXECUTION_PLANNING_NOT_PROVEN_INVALID`.

No current or proposed task has inferred, arithmetically rebased or adopted replacement offsets.

## Proposed Refresh/Revalidation Design

The proposal compares four strategies:

- HEAD-only transport refresh — rejected as insufficient to prove ZIP layout;
- arithmetic offset rebase — rejected as unsupported inference;
- full archive download — rejected as too broad;
- bounded ZIP central-directory metadata revalidation — **proposed for human review only**.

The proposed later path has two phases:

1. one same-endpoint HEAD observation for transport identity;
2. bounded ZIP tail/EOCD/central-directory metadata reads to derive candidate canonical member local-header offsets from ZIP metadata rather than from historical offsets.

Existing caps are preserved:

- HEAD requests max `1`;
- Range requests max `4`;
- HTTP requests max total `5`;
- Range response max each `131072` bytes;
- total source response-body max `524288` bytes;
- no full-body fallback;
- no automatic widening;
- no automatic retry.

The proposed structural verifier is classic-ZIP-only and fail-closed. ZIP64, multi-disk, missing/ambiguous EOCD, object identity drift during execution, missing/duplicate canonical members or inability to complete within the existing caps must stop without baseline adoption.

No central-directory/EOCD runtime implementation is added by this proposal.

## Candidate Baseline State

All replacement values remain unresolved:

- candidate content length: `null`;
- candidate ETag: `null`;
- candidate offset for member 1: `null`;
- candidate offset for member 2: `null`;
- candidate offset for member 3: `null`;
- candidate offset for member 4: `null`.

A later successful revalidation could produce candidate evidence only. Human evidence review and a separate implementation gate would still be required before updating runner constants.

## Authorization / Privacy State

Consumed v1.2 execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed v1.2 transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain `CONSUMED_SINGLE_USE_NON_REUSABLE`.

The new proposal grants no approval and performs no network request. A later structural revalidation would require:

- a fresh single-use execution approval;
- a fresh single-use structural-byte privacy approval.

The proposed privacy boundary is memory-only structural bytes, zero retention, no raw-byte persistence, no decompression, no CSV parsing, no row/protected-field observation and no persistence of noncanonical member names.

## Runtime / D-008 State

Unchanged:

- runner: `scripts/ca_sco_property_type_semantic_verification.py`;
- output contract: `1.2.0`;
- regex: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- trimming/casing/normalization;
- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- canonical member offsets.

The D-008 `PROPERTY_TYPE_NONCONFORMING_STOPPED / PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE` mapping remains unchanged and was not reached in the transport-drift execution.

`DECISIONS.md` remains unchanged because the baseline-refresh design is only a proposal pending human review.

## Source / Product Governance State

- baseline-refresh proposal prepared: `true`;
- proposal human-reviewed: `false`;
- network revalidation authorized: `false`;
- fresh execution approval granted: `false`;
- fresh structural-byte privacy approval granted: `false`;
- workflow creation authorized: `false`;
- retry authorized: `false`;
- current baseline suitable for blind reuse: `false`;
- candidate replacement baseline established: `false`;
- candidate baseline adopted: `false`;
- source continuation authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

The review must remain repository-only. It may accept, reject or require revision of the proposal, but it must perform no California SCO request, grant no execution/privacy approval, create no network workflow, update no runner constants and perform no baseline adoption.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
