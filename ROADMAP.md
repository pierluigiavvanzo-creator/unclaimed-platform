# ROADMAP.md

Last updated: 2026-09-17

## Product-priority roadmap

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | TECHNICAL BASELINE PRESERVED; SOURCE NOT YET USABLE | fail-closed real-source evidence accepted; current transport/archive-layout baseline stale; approved real sources remain 0 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| **MVP-1 — First Economically Actionable Case** | **ACTIVE — PRODUCT CRITICAL** | real authorized source → real candidate → insurance classification → economics → reviewer case card → human decision |

Canonical priority source: `PRODUCT_STRATEGY.md`.

Accepted decision: `D-009 — Product-value-first sequencing and MVP-1 commercial validation` / `docs/decisions/ADR-0007-mvp1-product-value-first.md`.

## MVP-1 stages

### P0 — Gap + reuse audit — ACTIVE

Task:

`MVP1_VERTICAL_SLICE_GAP_AND_REUSE_AUDIT`

Exit evidence:

- existing versus missing vertical-slice components identified;
- reuse options benchmarked before custom development;
- California continuation versus alternate-source selection compared as source-unblock strategies;
- smallest safe implementation sequence documented.

This stage is repository-only and does not authorize source/network/PII access.

### P1 — One usable real source

Goal: obtain one source that is lawful, authorized and technically usable for a bounded MVP-1 pilot.

Possible routes include California revalidation or another source if the audit shows that it provides a materially shorter/safer path. California is not privileged merely because prior engineering effort has already been spent on it.

Exit evidence:

- source terms/access boundary reviewed;
- required privacy/source approvals explicit;
- reproducible bounded acquisition succeeds;
- provenance and raw/evidence handling meet existing controls.

### P2 — Minimum real screening path

Goal:

`real ingestion → normalization → insurance relevance/classification → real candidate`

Build only what is needed for the first defensible real case. Apply repository-first/reuse-first before substantial A02/A03 implementation.

Exit evidence:

- real source-derived candidate;
- normalized record/representation sufficient for screening;
- reproducible insurance relevance/classification;
- evidence/provenance visible;
- no silent semantic inference.

### P3 — Minimum economics

Goal: implement A15 only to the depth required for a defensible economic screen.

Exit evidence:

- known values and/or explicit estimates/proxies separated;
- assumptions and uncertainty visible;
- machine/external costs captured or estimated;
- material human-time cost captured or estimated;
- economic result usable by a human reviewer;
- no invented commercial threshold.

### P4 — Reviewer case card + human decision

Reuse the active Streamlit reviewer path where possible.

Minimum case card:

- decision requested;
- facts;
- supporting and contradicting evidence;
- missing evidence;
- source/provenance;
- classification result;
- economic screen;
- assumptions/uncertainty;
- applicable policy;
- next action;
- governed human decision.

Exit evidence: at least one real source-derived candidate is reviewed through the product surface.

### P5 — MVP-1 evidence review

Measure:

- time to first actionable case;
- records examined;
- candidate yield;
- classifiable-candidate rate;
- machine/external cost per record/candidate;
- human minutes per candidate/actionable case;
- economic-value basis and expected contribution range when defensible;
- evidence completeness and stop reasons.

The Product Owner then decides continuation, source/market pivot or stop based on evidence. Downstream sophistication is not a prerequisite for this decision.

## Work-priority rule

Every substantial task must declare:

`CLASS → MVP-1 STAGE → ECONOMIC/PRODUCT CONTRIBUTION → USER-TIME IMPACT → REUSE DECISION`

Priority classes:

- A — Product Critical;
- B — Material Upgrade;
- C — Optimization;
- D — Diagnostic / Technical.

C/D work is deferred unless it protects or unblocks an A-class risk.

## Preserved California state

D-008 remains in force:

- accepted design: `WHOLE_SOURCE_STOP`;
- implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- runner output contract: `1.2.0`.

Reviewed one-shot execution:

- run `35123686954` — SUCCESS;
- result `STOPPED_FAIL_CLOSED`;
- reason `TRANSPORT_METADATA_DRIFT`;
- 1 HEAD request;
- 0 Range requests;
- 0 body bytes;
- 0 rows;
- no `PROPERTY_TYPE` value observed.

All approvals consumed by that run remain non-reusable. No retry, baseline update, source continuation or privacy expansion is authorized by the strategic pivot.

The earlier `PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL` is retained as a candidate P1 activity only if P0 demonstrates that it is the minimum-value path to a usable real source.

## Explicitly deferred until commercial evidence

Unless separately required by a safety/legal gate, do not prioritize:

- full A01-A23 implementation;
- complete genealogy automation;
- automated outreach;
- automated claim submission;
- broad multi-state expansion;
- infrastructure refactors without an MVP-1 dependency;
- additional diagnostic/governance chains without a new hypothesis and direct A-class unblock.
