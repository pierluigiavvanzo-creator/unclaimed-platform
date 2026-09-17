# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Milestone

`MVP-1 — First Economically Actionable Case`

Canonical product-priority source:

`PRODUCT_STRATEGY.md`

Accepted strategic decision:

`D-009 — Product-value-first sequencing and MVP-1 commercial validation`

Detailed decision:

`docs/decisions/ADR-0007-mvp1-product-value-first.md`

## Strategic State

M0, M1 and M2 remain **VERIFIED**. M3 has produced a strong deterministic source-governance/fail-closed foundation and an active Streamlit operations surface.

The project now treats **product/economic validation as the dominant risk**.

At the strategy pivot:

- approved real sources: `0`;
- production classification: inactive;
- California `PROPERTY_TYPE` semantic compatibility: unresolved;
- identity resolution: blocked;
- genealogy: blocked;
- beneficiary matching: blocked;
- outreach: blocked;
- claim submission: blocked;
- A02 normalization implementation: placeholder only;
- A03 insurance implementation: placeholder only;
- A15 economics implementation: placeholder only.

The repository contains foundation/core/source-governance/runtime components, but not yet the minimum real vertical slice needed to demonstrate a commercially actionable case.

## MVP-1 Required Vertical Slice

```text
REAL AUTHORIZED SOURCE
        ↓
BOUNDED REAL INGESTION
        ↓
NORMALIZATION
        ↓
INSURANCE RELEVANCE / CLASSIFICATION
        ↓
REAL CANDIDATE CASE
        ↓
EVIDENCE + PROVENANCE
        ↓
ECONOMIC SCREEN
        ↓
REVIEWER CASE CARD
        ↓
HUMAN DECISION
```

Full genealogy automation, outreach, claim submission, full multi-state coverage and completion of every A01-A23 module are outside the minimum MVP-1 requirement.

## Current Work Priority

All significant work must state:

- class `A | B | C | D`;
- MVP-1 stage affected;
- expected product/economic contribution;
- Product Owner time impact;
- reuse status/decision.

Class D diagnostics are subordinate to A-class product/legal/privacy/security blockers.

The previous next action, `PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`, remains a technically valid possible path but is **no longer automatically the exclusive next action**. It should be pursued only if the MVP-1 audit shows that refreshing/revalidating California is the smallest safe route to a usable authorized real source.

## Preserved M3 Technical Baseline

California SCO `PROPERTY_TYPE` handling remains governed by:

- `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`;
- accepted policy: `WHOLE_SOURCE_STOP`;
- implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- runner output contract: `1.2.0`.

The v1.2 implementation, real-source execution proposal/review, fresh single-use authorization, one-shot execution and human evidence review were completed before the strategy pivot.

Reviewed one-shot result:

`STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`

One-shot run:

`35123686954` — **SUCCESS**, attempt `1`

Actual bounded usage:

- HEAD requests: `1`;
- Range requests: `0`;
- total HTTP requests: `1`;
- source body bytes read: `0`;
- rows examined: `0`;
- `PROPERTY_TYPE` values observed: `0`.

The live content length and ETag differed from the pinned transport identity, so the runner correctly stopped before body access. The current transport/archive-layout baseline must not be blindly reused.

Historical evidence/review remains authoritative for that execution:

- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`;
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`;
- `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`.

## Approval / Safety State

The previously used execution and privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry is authorized. No existing consumed approval may be reused.

D-009 / MVP-1 changes priority and sequencing only. It grants no:

- source/network request;
- source approval;
- privacy expansion;
- parser/projector/regex relaxation;
- real-row persistence expansion;
- outreach;
- claim submission.

All legal, privacy, security and source-access gates remain in force.

## Current Product Blockers

1. No approved real source usable for a bounded MVP-1 pilot.
2. Minimum normalization path for the real vertical slice is not implemented as a completed product agent.
3. Minimum deterministic insurance relevance/classification path is not implemented as a completed product agent.
4. A15 economic screen / unit-economics output is not implemented.
5. The reviewer surface has not yet displayed a real source-derived case with economics and a governed human decision.

## Immediate Next Action

Execute exclusively:

`MVP1_VERTICAL_SLICE_GAP_AND_REUSE_AUDIT`

Classification: **A — Product Critical**.

Scope:

- repository-only inventory of existing versus missing MVP-1 components;
- reuse-first benchmark for the minimum A02/A03/A15/A16 path;
- identify the smallest lawful route to one usable real source;
- determine whether California baseline refresh remains the shortest route or source selection should be reopened;
- produce the minimum sequenced implementation plan to first commercial evidence.

This audit performs **no external source request, no PII access and no reuse of consumed approvals**.

Use `docs/handovers/HANDOVER_CURRENT.md` as the restart point after reading the canonical sources in their updated order.
