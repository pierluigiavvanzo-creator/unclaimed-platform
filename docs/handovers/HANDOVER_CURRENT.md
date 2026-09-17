# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-transport-archive-layout-baseline-adoption`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California is only a critical-path enabler for the first lawful approved real source. Avoid additional diagnostics/governance that do not shorten that path.

## Latest Completed Action

Completed:

`IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`

Classification:

`A/B — MVP-1 critical-path enabler`

Human evidence-review basis:

`PASS_CANDIDATE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_EVIDENCE_ACCEPTED_FOR_SEPARATE_ADOPTION_IMPLEMENTATION`

Review checkpoint:

- HEAD `008c1290b867abcfe30447c9dad326e1676d5570`;
- CI `35200127505` — **SUCCESS**.

Verified adoption checkpoint before closure-state update:

- HEAD `1eb8f79bac3024c7b69785663e3102a0fe83f8fd`;
- CI `35208763198` — **SUCCESS**.

Adoption audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION.md`

## Adopted Runtime Baseline

Semantic runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Runtime contract:

`1.2.0`

Adopted transport/archive-layout pins:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- `From_500_To_Beyond_1_of_4.csv` -> `0`;
- `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
- `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
- `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

The adoption regression contract asserts that these values equal the persisted human-reviewed structural revalidation evidence.

## Runtime Behavior Preserved

Unchanged:

- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP` semantics;
- deterministic sample limits;
- request/byte caps;
- source policy;
- registry;
- production/downstream gates.

The implementation branch also adjusted existing schema/contract regressions needed to distinguish immutable historical evidence from the new active baseline. No source-access or privacy scope was widened.

## Network / Approval State

This baseline-adoption action is repository-only and performed no California SCO request.

Structural revalidation approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Historical v1.2 real-source execution/privacy approvals also remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No fresh real-source execution or transient-row privacy approval currently exists.

## Source / Product State

- transport/archive-layout candidate established: `true`;
- human evidence review accepted: `true`;
- transport/archive-layout baseline adopted: `true`;
- approved real sources: `0`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- semantic compatibility: unresolved;
- production classification: inactive;
- real MVP-1 candidate cases: `0`;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Why the historical v1.2 execution proposal needs a minimal refresh

Historical proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

It still binds its sample plan to historical canonical offsets:

`0`, `59747797`, `96862896`, `134174190`.

Therefore it must not be reused unchanged for a fresh execution after baseline adoption.

The existing execution design itself remains the preferred path and should be reused: same four canonical members, same deterministic prefix sample, same D-008 mapping, same privacy constraints, same request/byte caps, same no-widening/no-retry behavior. Only stale baseline/provenance binding and strictly dependent assertions need refresh.

## Canonical Read Order Before Any New Change

Read in exact order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION.md`;
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW.md`;
3. `sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`;
4. `scripts/ca_sco_property_type_semantic_verification.py`;
5. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`;
6. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL.md`;
7. its proposal schema/contract test as needed.

## SINGLE NEXT ACTION

Execute exclusively:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification:

`A — Product Critical`

This next action is repository-only.

It must:

- reuse the existing v1.2 real-source execution proposal design;
- bind the proposal to the adopted baseline and current CI-green runner;
- replace the stale canonical offsets in the proposal with `0`, `59745428`, `96861315`, `134172553`;
- update provenance/base checkpoint and strictly dependent schema/contract assertions only where necessary;
- preserve the same deterministic sample, request/byte caps, privacy boundary, D-008 behavior and no-retry/no-widening rules;
- validate in CI.

It must not:

- perform any California SCO request;
- create/trigger a network workflow;
- grant execution/privacy approvals;
- reuse consumed approvals;
- change parser/projector/regex/trimming/casing/normalization;
- change D-008 semantics;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, beneficiary matching, outreach or claim submission.

After the refreshed proposal is CI-green, proceed through the minimum required human review and fresh single-use authorization to exactly one bounded real-source semantic execution. Do not reopen transport diagnostics without new contradictory evidence.
