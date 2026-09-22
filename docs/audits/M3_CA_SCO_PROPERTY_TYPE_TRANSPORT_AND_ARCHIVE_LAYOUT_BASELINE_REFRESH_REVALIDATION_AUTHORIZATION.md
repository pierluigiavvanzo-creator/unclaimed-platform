# M3 California SCO — PROPERTY_TYPE Transport + Archive-Layout Revalidation Authorization

Date: 2026-09-17

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — PASS — FRESH SINGLE-USE STRUCTURAL REVALIDATION EXECUTION + STRUCTURAL-BYTE PRIVACY APPROVALS GRANTED — EXECUTION NOT PERFORMED**

## Authorization gate

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

Classification:

`A/B — MVP-1 critical-path enabler`

MVP-1 blocker addressed:

`FIRST_APPROVED_REAL_SOURCE -> transport/archive-layout baseline unresolved after fail-closed TRANSPORT_METADATA_DRIFT`

## Authoritative checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- authorization base branch: `m3-unified-mvp1`;
- authorization base HEAD: `3d4d8a76e47d88eca77ca6d899b85341ba8beaf2`;
- authorization base CI: `35195330933` — **SUCCESS**;
- accepted review branch: `m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal-review`;
- accepted review HEAD: `b8f703db18207661cd799b0baf1f0dac1bfdc398`;
- accepted review CI: `35187432747` — **SUCCESS**;
- reviewed proposal branch: `m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`;
- reviewed proposal HEAD: `359b1c1a86d34edabcd028e5e5fbb6fc3acba781`;
- reviewed proposal CI: `35139290645` — **SUCCESS**;
- accepted review result: `PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`;
- selected strategy: `BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`.

The owner instructed the system to execute the canonical `SINGLE NEXT ACTION`. Consistent with the repository's prior authorization pattern, that instruction is interpreted only as approval to complete this authorization gate. It does **not** perform the separately gated California SCO network execution.

## Decision

`PASS_FRESH_SINGLE_USE_STRUCTURAL_REVALIDATION_EXECUTION_AND_STRUCTURAL_BYTE_PRIVACY_APPROVALS_GRANTED_EXECUTION_NOT_PERFORMED`

The accepted bounded classic-ZIP structural revalidation path is authorized for exactly one future network invocation under the frozen proposal/review boundary.

## Fresh approval references

Execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Both approvals are:

- `GRANTED_NOT_CONSUMED`;
- fresh;
- single-use;
- non-reusable;
- bound to reviewed proposal HEAD `359b1c1a86d34edabcd028e5e5fbb6fc3acba781`;
- bound to accepted review HEAD `b8f703db18207661cd799b0baf1f0dac1bfdc398`;
- bound to authorization base HEAD `3d4d8a76e47d88eca77ca6d899b85341ba8beaf2`;
- bound to the exact endpoint and caps below;
- not substitutes for, and not derived from, any historical approval.

The consumed v1.2 approvals remain `CONSUMED_SINGLE_USE_NON_REUSABLE` and are not reused.

The two fresh approvals are consumed on the **first authorized California SCO network request** of the later execution task. Repository-only implementation/CI that occurs before any source request does not consume them. Once the first request occurs, no automatic retry is authorized regardless of outcome.

## Exact endpoint / transport binding

Authorized endpoint:

`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Binding:

- HTTPS only;
- exact host `claimit.ca.gov`;
- one HEAD observation before structural Range reads;
- Range reads must remain on the same observed object via ETag / `If-Match`;
- `Content-Range` total must equal the HEAD-observed content length.

No redirect broadening, alternate host, alternate segment or alternate source is authorized.

## Hard request / byte caps

The later one-shot structural revalidation is limited to:

- HEAD requests max: `1`;
- Range requests max: `4`;
- HTTP requests max total: `5`;
- response bytes/range max: `131072`;
- source response-body bytes total max: `524288`;
- full-body fallback: `false`;
- automatic widening: `false`;
- automatic retry: `false`.

No cap may be widened inside the execution task.

## Structural scope

The authorization permits only the accepted classic-ZIP metadata path:

`HEAD -> ZIP tail -> classic EOCD -> bounded Central Directory -> canonical relative local-header offsets`

Required canonical members:

1. `From_500_To_Beyond_1_of_4.csv`;
2. `From_500_To_Beyond_2_of_4.csv`;
3. `From_500_To_Beyond_3_of_4.csv`;
4. `From_500_To_Beyond_4_of_4.csv`.

Constraints:

- classic ZIP EOCD required;
- ZIP64 unsupported;
- multi-disk unsupported;
- central-directory metadata only;
- no decompression;
- no CSV parsing;
- no row/field inspection;
- no arithmetic rebasing from historical offsets;
- canonical member names must be unique;
- candidate offsets must come from central-directory metadata;
- candidate offsets must fall within the observed archive length.

Fail closed on cap exhaustion, missing/ambiguous EOCD, ZIP64, multi-disk, object identity drift, missing/duplicate canonical members, or any layout ambiguity/unresolvable condition.

## Structural-byte privacy authorization

The fresh privacy approval authorizes only the transient structural bytes strictly required to locate and parse classic ZIP EOCD / central-directory metadata inside the approved Range windows.

Privacy boundary:

- memory-only structural bytes;
- retention `0` days;
- immediate disposal;
- raw Range bytes not persisted;
- compressed payload not parsed or decompressed;
- CSV rows not parsed;
- no row or protected field inspected;
- no `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder or other record value observed;
- noncanonical member names not persisted.

Only these bounded derived fields may persist:

- `OBSERVED_CONTENT_LENGTH`;
- `OBSERVED_ETAG`;
- `OBSERVED_CONTENT_TYPE`;
- `OBSERVED_ACCEPT_RANGES`;
- `OBSERVED_LAST_MODIFIED`;
- `OBSERVED_AT`;
- `CANONICAL_MEMBER_NAMES`;
- `CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS`;
- `CANONICAL_MEMBER_MATCH_STATUS`;
- `ADDITIONAL_MEMBER_COUNT`;
- `REVALIDATION_RESULT_STATUS`;
- `STOP_REASON`.

No privacy expansion is authorized.

## Candidate-evidence / adoption separation

A successful later revalidation may establish only a **candidate** transport/archive-layout baseline.

This authorization does **not** permit:

- adoption of a content length;
- adoption of an ETag;
- adoption of canonical member offsets;
- modification of `EXPECTED_LENGTH`;
- modification of `EXPECTED_ETAG`;
- modification of canonical member offsets in the semantic runner.

Any candidate evidence must stop at a separate human evidence-review gate. Runner-constant adoption requires a later separate implementation gate after that review.

## Runtime / source governance non-impact

This gate makes no change to:

- `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP`;
- source policy;
- source registry;
- production classification.

The following remain closed:

- approved real sources: `0`;
- semantic compatibility: unresolved;
- production classification: inactive;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

## Repository-only evidence produced by this gate

This gate adds:

- this authorization audit;
- machine-readable authorization evidence;
- a versioned authorization schema;
- contract tests pinning the authorization boundary;
- persistent project-state / roadmap / handover updates.

It performs no external request.

## Explicitly not performed

This task did **not**:

- request California SCO or any other external source;
- perform HEAD;
- perform Range GET;
- download source bytes;
- read CSV records;
- reuse consumed approvals;
- perform structural revalidation;
- establish or adopt a candidate baseline;
- change runner constants;
- change parser/projector/regex/normalization;
- activate source policy or registry;
- start identity resolution, genealogy, matching, outreach or claim submission.

## DECISIONS.md assessment

No new decision entry is required. This gate grants a bounded, one-shot operational authorization under the already accepted review and existing deterministic/fail-closed architecture. It introduces no new architecture, policy or product strategy.

## Next single action

Execute exclusively:

`EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`

That later task must remain a distinct action. It may implement/CI-validate the smallest repository-local verifier/workflow needed to exercise the already accepted design, then perform at most one authorized network invocation using exactly the two fresh refs above.

It must consume both refs on the first California SCO network request, must not retry or widen, may persist only the approved derived candidate evidence, and must stop at a separate human candidate-evidence review before any baseline adoption or runner mutation.
