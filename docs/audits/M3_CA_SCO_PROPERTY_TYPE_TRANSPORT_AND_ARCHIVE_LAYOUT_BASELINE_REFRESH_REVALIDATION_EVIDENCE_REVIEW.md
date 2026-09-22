# M3 California SCO — PROPERTY_TYPE Transport + Archive-Layout Revalidation Evidence Review

Date: 2026-09-17

Status: **HUMAN EVIDENCE REVIEW COMPLETED — PASS — CANDIDATE BASELINE EVIDENCE ACCEPTED FOR A SEPARATE REPOSITORY-ONLY ADOPTION IMPLEMENTATION — NO SOURCE REQUEST — NO BASELINE ADOPTED IN THIS REVIEW**

## Review gate

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`

Classification:

`A/B — MVP-1 critical-path enabler`

MVP-1 blocker addressed:

`FIRST_APPROVED_REAL_SOURCE -> current transport/archive-layout candidate required human acceptance before runtime adoption`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- branch: `m3-ca-sco-transport-archive-layout-revalidation-once`;
- reviewed HEAD: `ac7ced81299d5a563e4c4beeb74858ba28e2b50a`;
- reviewed CI: `35199132893` — **SUCCESS**;
- execution run: `35198720002` — **SUCCESS**, attempt `1`;
- execution job: `105128028851` — **SUCCESS**;
- persisted evidence: `sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`;
- execution audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EXECUTION.md`.

This review is repository-only. It performs no California SCO request and does not retry the consumed one-shot execution.

## Decision

`PASS_CANDIDATE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_EVIDENCE_ACCEPTED_FOR_SEPARATE_ADOPTION_IMPLEMENTATION`

The persisted evidence is sufficient to justify a later separate repository-only implementation gate that updates only the semantic runner transport/archive-layout pins.

This review does **not** itself adopt the candidate values and does not modify the semantic runner.

## Evidence sufficiency findings

PASS.

The persisted execution evidence validates against the existing versioned execution schema and records:

- `REVALIDATION_RESULT_STATUS = CANDIDATE_BASELINE_ESTABLISHED`;
- `STOP_REASON = null`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`;
- canonical member match status `ALL_CANONICAL_MEMBERS_UNIQUE`;
- additional member count `0`;
- candidate local-header offsets `0`, `59745428`, `96861315`, `134172553` for the four canonical members.

The values are internally consistent with the successful bounded classic-ZIP Central Directory revalidation and the accepted proposal/review design.

## Provenance review

PASS.

The execution audit pins the result to:

- authorization checkpoint `4079fb44b36699e9b05821761c222d063a89648d`;
- implementation preflight `e87e7d20d766ad06ca0feb8805ac00c4a6ed547c`;
- trigger checkpoint `de4c20e0a4158da0497d2ca9c2090589636b40e0`;
- one-shot workflow run `35198720002`, attempt `1`, **SUCCESS**;
- GitHub artifact id `10487072813`;
- artifact digest `sha256:2ed7f3e620a50f635f3eae7dad5efca80f3dc86d239c728dd12dfd23eda07e65`;
- extracted evidence SHA-256 `120f5ee2eef859578adb922f15138bab65cb19e7979274ed9360c24b9b071d64`.

No rerun is authorized or required by this review.

## Candidate-versus-adopted separation

PASS.

The existing contract test proves the candidate evidence has not been silently adopted. At the reviewed checkpoint the semantic runner still contains the historical pins:

- `EXPECTED_LENGTH = 162416884`;
- `EXPECTED_ETAG = "b25b315b6cd8007624387c3a00d4b1fe"`;
- offsets `0`, `59747797`, `96862896`, `134174190`.

The candidate evidence differs from those historical values for content length, ETag and three of the four offsets. Therefore adoption must remain explicit and isolated in the next implementation gate.

## Approval-state review

PASS with one important provenance clarification.

The historical authorization artifact intentionally records the pre-execution state `GRANTED_NOT_CONSUMED`. It is an immutable record of the authorization gate and must not be interpreted as current reusable approval state.

Current authoritative post-execution state is:

- execution approval `OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB` -> `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- structural-byte privacy approval `OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB` -> `CONSUMED_SINGLE_USE_NON_REUSABLE`.

This review grants no replacement network or privacy approval.

## Privacy / scope review

PASS.

The successful evidence contains only the previously authorized derived structural fields. No raw Range bytes, decompressed payload, CSV row, `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder value or noncanonical member name is persisted in the reviewed evidence.

No privacy expansion is requested or granted.

## Product interpretation

The transport/archive-layout uncertainty is now sufficiently resolved for explicit runtime pin adoption.

This is not yet an approved real source. After the repository-only adoption implementation is CI-green, a later real-source semantic verification will still require whatever fresh source/privacy authorization is then applicable.

The project should not add further transport diagnostics before that implementation unless new evidence invalidates this review.

## DECISIONS.md assessment

No new architecture, policy or product-strategy decision is introduced. `DECISIONS.md` remains unchanged.

## Next single action

Execute exclusively:

`IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`

Classification:

`A/B — MVP-1 critical-path enabler`

The next action is repository-only and may update only:

- `EXPECTED_LENGTH` to `162560390`;
- `EXPECTED_ETAG` to `"222dd79f04c2a0a8fff166b01c8da746"`;
- the four canonical member local-header offsets to `0`, `59745428`, `96861315`, `134172553`.

It must preserve parser/projector/regex/normalization, D-008 behavior, source policy, registry and downstream gates, add/update regression coverage as needed, run the full CI/smoke suite, and perform **no California SCO network request**.
