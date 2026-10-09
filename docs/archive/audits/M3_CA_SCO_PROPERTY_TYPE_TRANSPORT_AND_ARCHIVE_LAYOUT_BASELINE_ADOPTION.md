# M3 California SCO — PROPERTY_TYPE Transport + Archive-Layout Baseline Adoption

Date: 2026-09-17

Status: **IMPLEMENTATION COMPLETED — REVIEWED BASELINE ADOPTED — CI GREEN — REPOSITORY ONLY — NO SOURCE REQUEST**

## Action

`IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`

Classification:

`A/B — MVP-1 critical-path enabler`

MVP-1 blocker addressed:

`FIRST_APPROVED_REAL_SOURCE -> reviewed current transport/archive-layout values were not yet active in the semantic runner`

## Authoritative basis

Human evidence review:

`PASS_CANDIDATE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_EVIDENCE_ACCEPTED_FOR_SEPARATE_ADOPTION_IMPLEMENTATION`

Review checkpoint:

- HEAD `008c1290b867abcfe30447c9dad326e1676d5570`;
- CI `35200127505` — **SUCCESS**;
- audit `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW.md`.

Persisted reviewed evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`

## Implementation checkpoint

Branch:

`m3-ca-sco-transport-archive-layout-baseline-adoption`

Verified implementation HEAD before this closure record:

`1eb8f79bac3024c7b69785663e3102a0fe83f8fd`

GitHub Actions CI:

`35208763198` — **SUCCESS**

The branch is seven commits ahead of the reviewed evidence checkpoint and zero commits behind it.

## Adopted runtime pins

The semantic runner now uses exactly the human-reviewed structural evidence:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- `From_500_To_Beyond_1_of_4.csv` -> `0`;
- `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
- `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
- `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

The contract regression now asserts that the semantic runner pins equal the persisted reviewed candidate evidence.

## Scope preservation

Unchanged:

- runtime contract `1.2.0`;
- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP` behavior;
- request/byte caps;
- source policy;
- registry state;
- production classification state;
- downstream identity/genealogy/matching/outreach/claim gates.

The additional schema/contract-test adjustments on the implementation branch preserve historical execution evidence and align the existing v1.2 proposal/execution contract with the explicit baseline adoption. They do not widen source access, privacy, parsing or continuation behavior.

## Network / approval boundary

This adoption action is repository-only.

It performs no California SCO request, no HEAD, no Range GET, no source-body access and no row/field inspection.

The previously consumed approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No approval is reused and no fresh network/privacy approval is granted by this action.

## Product state

- transport/archive-layout baseline adopted: `true`;
- approved real sources: `0`;
- semantic compatibility: unresolved;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification: inactive;
- real MVP-1 candidate cases: `0`.

The transport/archive-layout blocker is therefore closed at runtime. The shortest safe path now returns to a fresh bounded v1.2 real-source semantic verification.

## Why the old execution proposal cannot be reused unchanged

The historical machine proposal still pins the old canonical offsets `0`, `59747797`, `96862896`, `134174190`. It is therefore provenance, not a valid frozen boundary for a new execution after this baseline adoption.

No new transport diagnostic is needed. The next work should minimally refresh that existing v1.2 execution proposal to the adopted pins while preserving its already reviewed sample, D-008, privacy and request-cap design.

## DECISIONS.md assessment

No new architecture, policy or product-strategy decision was introduced. `DECISIONS.md` remains unchanged.

## Next single action

Execute exclusively:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification:

`A — Product Critical`

The refresh must be repository-only and should change only the stale transport/archive-layout binding and provenance needed to bind a future one-shot execution to the newly adopted baseline. It must reuse the existing v1.2 sample plan, D-008 behavior, privacy boundary and hard caps; it must not access California SCO, grant approvals, create a network workflow, change parser/projector/regex/normalization, or activate source/downstream gates.
