# PRODUCT_STRATEGY.md — Product Value & Commercial Validation

**Version:** 1.0  
**Date:** 2026-09-17  
**Status:** CANONICAL PRIORITY SOURCE — Product Owner Decision  
**Primary target:** `MVP-1 — First Economically Actionable Case`

---

## 1. Authority and precedence

This file is the canonical source for **product sequencing, work priority and resource allocation** in the Unclaimed Insurance Platform.

It does not weaken or replace legal, privacy, security, source-access or authorization controls. Precedence is:

1. applicable law, privacy/security obligations and explicit authorization boundaries;
2. accepted project policies and architectural decisions that protect those boundaries;
3. `AGENTS.md` for engineering discipline;
4. this file for product/economic priority and sequencing;
5. local implementation optimizations.

If a product objective conflicts with a safety, privacy, legal or authorization gate, the gate wins. If an engineering activity does not materially advance the product objective and is not needed to protect a Product Critical risk, it is deprioritized.

This decision supersedes prior sequencing in which completing an extended M3 diagnostic/governance chain could be treated as an objective by itself. It does **not** supersede D-008, does not reactivate consumed approvals and does not authorize source/network/PII access.

---

## 2. Strategic objective and governing metric

Every substantial work package must contribute measurably to the strategic objective of creating additional economic/strategic value, with the portfolio benchmark of **EUR 2,000,000 additional value/wealth within 5 years**.

The governing optimization metric is:

> **ECONOMIC VALUE × USABLE PRODUCT VALUE / USER TIME**

Code volume, test count, number of milestones, number of reviews and diagnostic depth are not progress by themselves.

---

## 3. Current product diagnosis

The engineering/governance foundation is strong: M0, M1 and M2 are verified, fail-closed controls are working, provenance is explicit and the Streamlit operations surface is active.

The dominant risk is now **product/economic validation**, not foundation engineering.

At adoption of this strategy:

- approved real sources: `0`;
- California semantic compatibility: unresolved;
- production classification: inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: blocked;
- `economics/` and A15 economics are placeholders;
- A02 normalization and A03 insurance agent implementation are placeholders;
- the latest bounded California execution stopped correctly before body access because of `TRANSPORT_METADATA_DRIFT` and therefore examined `0` rows.

Therefore the project must now optimize for reaching the **first defensible real case with an economic decision**, rather than maximizing additional governance artifacts around an otherwise blocked source.

---

## 4. Work classification

Every significant task must be classified before execution:

- **A — Product Critical:** directly unlocks or completes MVP-1, or protects a material legal/privacy/security risk that blocks MVP-1.
- **B — Material Upgrade:** materially improves reliability, reusability or operator usefulness of the MVP-1 path.
- **C — Optimization:** worthwhile but not required for first commercial evidence.
- **D — Diagnostic / Technical:** investigation, cleanup or infrastructure work with no direct product output.

Manual Product Owner work on class D activities is exceptional and must be justified by a class A risk.

If a task cannot state its MVP-1 stage, expected product/economic contribution and user-time impact, it is deferred by default.

---

## 5. MVP-1 — First Economically Actionable Case

### 5.1 Required vertical slice

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

MVP-1 does **not** require full genealogy automation, automatic outreach, claim submission, contracts automation, complete multi-state support or a fully implemented A01-A23 agent network.

### 5.2 Definition of an economically actionable case

A case qualifies only when all of the following are true:

1. it originates from a real source whose use for the bounded pilot is authorized;
2. source and transformation provenance are traceable;
3. the source-derived record/candidate is real, not synthetic;
4. insurance relevance/classification is supported by deterministic evidence or an explicitly bounded, reviewable classification method;
5. the system can produce a defensible economic screen using known values or clearly identified estimates/proxies with provenance and uncertainty;
6. machine/external cost and material human-time cost can be recorded or estimated transparently;
7. the reviewer can see facts, supporting/contradicting evidence, missing evidence, uncertainty, economics, applicable policy and next action;
8. a human can make a governed `CONTINUE`, `STOP`, `HUMAN_REVIEW` or other existing contract-valid decision.

If economic value cannot yet be estimated with defensible provenance, the record is useful technical evidence but is **not** an economically actionable case.

No arbitrary monetary threshold is invented here. Commercial thresholds must be derived from documented legal/commercial constraints and pilot evidence.

---

## 6. MVP-1 exit evidence

MVP-1 is reached only when the repository contains verifiable evidence of:

- at least one real authorized source usable for a bounded pilot;
- at least one real source-derived candidate processed through the minimum vertical slice;
- a reproducible insurance relevance/classification result;
- a reproducible economic screen with assumptions and uncertainty visible;
- a reviewer case card showing the evidence and economic decision context;
- a recorded human decision;
- measured or defensibly estimated user time, machine/external cost and case economics;
- complete provenance/audit trace sufficient to reproduce the decision path.

Passing technical tests without this product evidence does not satisfy MVP-1.

---

## 7. Commercial-validation metrics

Collect these metrics as soon as real pilot evidence permits:

- time to first economically actionable case;
- source records examined;
- source → insurance-relevant candidate yield;
- percentage of candidates classifiable with sufficient evidence;
- machine/external cost per examined record and per candidate;
- human minutes per candidate and per actionable case;
- estimated gross case value or documented value proxy;
- legally/commercially valid revenue basis when known;
- expected contribution margin/range, with uncertainty;
- evidence completeness / unresolved contradiction rate;
- stop/failure reasons and their frequency.

These metrics are evidence for product decisions, not targets to fabricate or optimize cosmetically.

---

## 8. Repository-first / reuse gate

Before substantial custom implementation for the MVP-1 path, evaluate existing repository components, mature libraries, APIs and products.

Track candidates through:

`DISCOVERED → BENCHMARKED → ADOPTED or REJECTED → INTEGRATED → USED`

A listed dependency is not counted as reuse until it is integrated and actually used.

For A02 normalization, A03 insurance classification, A15 economics and reviewer extensions, record at minimum: license/terms, maintenance, maturity, compatibility, security/privacy, integration cost and commercial fit.

Prefer actual reuse/wrapping of stable components over custom code unless a small deterministic project-specific implementation is materially safer, simpler or more auditable.

---

## 9. Diagnostic and governance budget

Diagnostics must be hypothesis-driven and bounded.

Do not repeat the same check without new evidence or a new hypothesis. Do not create chains of proposal → review → authorization → execution → evidence → review unless each additional layer is necessary to unlock an A-class product or safety gate.

The California transport/archive-layout issue remains relevant **only to the extent that resolving it is the smallest safe path to an authorized real source for MVP-1**. California is not automatically privileged over a materially easier lawful source.

---

## 10. Product Owner workload

The Product Owner is an approver and final product tester, not a repetitive QA operator, debugger or log courier.

Agents should autonomously execute the largest safe bounded package:

`precheck → backup/isolation → implementation → test → diagnostic → repair → smoke → report`

Escalate only at genuine legal/privacy/source-access/commercially irreversible or architecture-changing gates.

---

## 11. Immediate execution sequence

### A0 — MVP1_VERTICAL_SLICE_GAP_AND_REUSE_AUDIT

Repository-only. No external source request and no PII access.

Purpose:

- inventory what already exists versus what is missing for the MVP-1 chain;
- identify the minimum product-critical gaps;
- benchmark reuse options before custom implementation;
- determine whether California baseline refresh is the shortest safe source-unblock path or whether source selection should be reopened;
- produce the smallest implementation sequence that reaches real commercial evidence.

### A1 — REAL_SOURCE_UNBLOCK

Only after the audit. Select the minimum lawful route to one usable real source. Any network/PII step still requires the approvals applicable to that action.

### A2 — MINIMUM_REAL_VERTICAL_SLICE

Implement only the missing normalization → insurance screen → economic screen → reviewer-card path needed for one real candidate, reusing existing components where possible.

### A3 — MVP1_EVIDENCE_REVIEW

Measure the commercial-validation metrics and decide, with the Product Owner, whether evidence supports continuation, a source/market pivot or a stop. Do not build downstream sophistication first.

---

## 12. Pivot / stop discipline

Before expanding identity/genealogy/outreach/claim automation, obtain evidence that the upstream funnel can generate economically actionable cases.

If a bounded source search cannot produce a lawful technically usable source, pivot the source strategy before expanding software.

If bounded pilot evidence shows that case yield, human effort, data quality or unit economics are not credible for the business model, freeze downstream expansion and reassess the commercial thesis.

---

## 13. Definition of progress

A modification counts as progress only if it materially improves at least one of:

- expected economic contribution;
- usable product value;
- reliability necessary to reach/operate MVP-1;
- reduction of Product Owner workload;
- validated knowledge needed for an A-class product decision.

Everything else is support work and must remain subordinate to MVP-1.
