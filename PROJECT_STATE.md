# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California remains active only as the minimum critical-path enabler required to reach one lawful approved real source.

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Working Checkpoint

Current branch:

`m3-ca-sco-transport-archive-layout-baseline-adoption`

Completed action:

`IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`

Human evidence-review checkpoint:

`008c1290b867abcfe30447c9dad326e1676d5570`

Human evidence-review CI:

`35200127505` — **SUCCESS**

Verified implementation checkpoint before closure-state update:

`1eb8f79bac3024c7b69785663e3102a0fe83f8fd`

Implementation CI:

`35208763198` — **SUCCESS**

Adoption audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION.md`

## Adopted Transport / Archive-Layout Baseline

The semantic runner now uses the human-reviewed current structural evidence:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- offsets `0`, `59745428`, `96861315`, `134172553` for the four canonical members.

Candidate replacement baseline established: `true`.

Human evidence review accepted: `true`.

Candidate baseline adopted: `true`.

Contract regression verifies that the adopted runtime pins equal the persisted structural revalidation evidence.

## Runtime / D-008 State

Unchanged except for the explicit reviewed transport/archive-layout pin adoption:

- semantic runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- parser/projector unchanged;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` unchanged;
- trimming/casing/normalization unchanged;
- D-008 `WHOLE_SOURCE_STOP` unchanged;
- request/byte caps unchanged.

## Authorization / Privacy State

Structural revalidation execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Current state of both:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Historical v1.2 real-source execution/privacy approvals are also consumed and non-reusable.

This adoption action performs no source/network request and grants no replacement approval.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout baseline adopted: `true`;
- semantic compatibility resolved: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

The transport/archive-layout runtime blocker is closed. The next useful product move is to rebind the existing bounded v1.2 real-source execution proposal to the adopted baseline and proceed toward fresh single-use authorization and one real semantic verification.

## Next Recommended Action

Execute exclusively:

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification:

`A — Product Critical`

This action is repository-only. Reuse the existing v1.2 proposal design and update only the stale baseline/provenance binding required by the adopted pins. Perform no California SCO request, grant no approval, create no network workflow, and do not change parser/projector/regex/normalization, D-008, source policy, registry or downstream gates.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
