# M3 California SCO — PROPERTY_TYPE Transport + Archive-Layout Baseline Refresh Proposal Review

Date: 2026-09-17

Status: **HUMAN REVIEW COMPLETED — PASS — BOUNDED STRUCTURAL REVALIDATION DESIGN ACCEPTED — FRESH AUTHORIZATION REQUIRED — NETWORK REVALIDATION NOT AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- proposal branch: `m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`;
- reviewed proposal HEAD: `359b1c1a86d34edabcd028e5e5fbb6fc3acba781`;
- reviewed proposal CI: `35139290645` — **SUCCESS**;
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`;
- machine proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`;
- proposal schema: `schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`;
- contract test: `tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`.

This review is repository-only. It performs no California SCO request, HEAD request, Range GET, source-body access, workflow creation, approval granting, retry, baseline mutation or runtime change.

## Decision

`PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`

The proposal is accepted as a bounded, deterministic, fail-closed and privacy-bounded design for a future separately authorized transport + classic-ZIP archive-layout revalidation.

This PASS does **not** authorize network execution, grant execution/privacy approval, create a workflow, adopt the one-shot observed ETag/content length, infer or update member offsets, modify the semantic runner, activate the source, or open any downstream gate.

## Evidence basis review

PASS.

The proposal is correctly pinned to the previously accepted v1.2 one-shot evidence and its human evidence review. The governing evidence remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`;
- HEAD requests = `1`;
- Range requests = `0`;
- HTTP requests total = `1`;
- source-body bytes read = `0`;
- rows examined = `0`.

Historical pinned transport remains:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- Accept-Ranges `bytes`.

The one-shot observation remains evidence only:

- HTTP `200`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

The review confirms that those observed values are not sufficient for baseline adoption.

## Archive-layout dependency review

PASS.

The semantic runner also depends on four historical ZIP local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` → `0`;
2. `From_500_To_Beyond_2_of_4.csv` → `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` → `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` → `134174190`.

The proposal correctly treats them as `STALE_FOR_FUTURE_EXECUTION_PLANNING_NOT_PROVEN_INVALID` rather than silently reusing, rejecting or arithmetically rebasing them.

All candidate replacement values remain unresolved (`null`).

## Strategy review

PASS.

The review accepts the proposal's strategy assessment:

- `HEAD_ONLY_TRANSPORT_REFRESH` — rejected because it cannot establish current ZIP member offsets;
- `ARITHMETIC_MEMBER_OFFSET_REBASE` — rejected because the archive-length delta does not establish byte placement;
- `FULL_ARCHIVE_DOWNLOAD_AND_INSPECTION` — rejected because it is broader than necessary;
- `BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION` — accepted as the bounded design for a later separately authorized gate.

The accepted design is limited to classic ZIP structural metadata. It does not accept ZIP64 or multi-disk layouts.

## Request / byte boundary

PASS; no widening.

A future separately authorized structural verifier remains bounded by:

- HEAD requests max: `1`;
- Range requests max: `4`;
- HTTP requests max total: `5`;
- Range response bytes max each: `131072`;
- total source response-body bytes max: `524288`;
- full-body fallback: `false`;
- automatic widening: `false`;
- automatic retry: `false`.

If classic EOCD or the needed central-directory metadata cannot be resolved inside these caps, the result must stop fail-closed and return to a new design/review gate.

## Same-object and structural consistency review

PASS.

The accepted future design requires:

- exact HTTPS endpoint / host binding;
- one transport HEAD observation before structural reads;
- Range requests bound to the same observed object through ETag / `If-Match` consistency;
- `Content-Range` total consistency with HEAD-observed content length;
- canonical member names unique;
- canonical local-header offsets taken from central-directory metadata, not historical offsets;
- offsets within the observed archive length;
- fail-closed stop on object identity drift, ambiguous EOCD, ZIP64, multi-disk, missing/duplicate canonical members or any unresolvable layout.

No historical offset may be used to discover or infer a candidate replacement offset.

## Privacy review

PASS with fresh approval still mandatory.

The proposed tail/central-directory Range windows may contain opaque compressed bytes adjacent to structural metadata. Therefore a future execution must require a fresh single-use structural-byte privacy approval in addition to a fresh single-use execution approval.

Accepted privacy boundary:

- structural Range bytes memory-only;
- retention `0` days;
- raw Range bytes not persisted;
- compressed payload not decompressed or interpreted;
- CSV not parsed;
- no row or protected field inspected;
- no `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder or other record value observed;
- noncanonical member names not persisted;
- only bounded derived transport/layout evidence may persist.

No existing or consumed privacy approval is reusable.

## Candidate evidence / adoption separation

PASS.

A successful future structural revalidation may create only a **candidate** transport/archive-layout baseline. It may not mutate the semantic runner in the same gate.

The required sequence remains:

1. fresh authorization;
2. separately authorized bounded structural revalidation;
3. privacy-safe candidate evidence persistence;
4. human candidate-evidence review;
5. separate implementation gate before updating `EXPECTED_LENGTH`, `EXPECTED_ETAG` or canonical member offsets;
6. CI-green verification of the later implementation.

No candidate value is adopted by this review.

## Runtime / D-008 non-impact

PASS and unchanged.

No change is authorized or made to:

- `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- canonical member offsets;
- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP` semantics.

The review makes no new semantic claim about `PROPERTY_TYPE`.

## Source / downstream governance

PASS and closed.

- proposal human-reviewed: `true`;
- proposal accepted as bounded design: `true`;
- network revalidation authorized: `false`;
- fresh execution approval granted: `false`;
- fresh structural-byte privacy approval granted: `false`;
- workflow creation authorized: `false`;
- retry authorized: `false`;
- candidate baseline established: `false`;
- candidate baseline adopted: `false`;
- source continuation authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## DECISIONS.md assessment

No new entry is required. This review accepts a bounded operational verification design under the existing deterministic, contract-first and fail-closed governance. It does not alter architecture, source policy, runtime semantics or D-008.

## CI evidence

Reviewed proposal CI `35139290645` is **SUCCESS** on exact reviewed HEAD `359b1c1a86d34edabcd028e5e5fbb6fc3acba781`.

The final reviewed run passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- frontend lint;
- frontend typecheck;
- frontend build;
- Streamlit safety smoke;
- Streamlit startup smoke.

## Next single action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

That gate may decide whether to grant fresh single-use execution and structural-byte privacy approvals for the already reviewed bounded revalidation design. It must remain repository-only and separate from execution itself.

It must not perform any California SCO request, create or trigger a network workflow, adopt baseline values, modify runner constants or open downstream gates.
