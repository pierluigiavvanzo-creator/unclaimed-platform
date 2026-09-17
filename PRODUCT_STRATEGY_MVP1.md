# PRODUCT_STRATEGY_MVP1.md

Version: 1.0  
Date: 2026-09-17  
Status: PRIORITY PRODUCT STRATEGY SOURCE  
Owner: Product Owner

## 1. Purpose

This document is a priority strategic source for the Unclaimed Insurance Platform.

Its purpose is to keep development aligned to economic validation and usable product value while preserving all existing legal, privacy, authorization, provenance and fail-closed controls.

It does not weaken or bypass any source, privacy, legal, security or human-approval gate.

## 2. Strategic objective

The project must contribute measurably to the broader objective of creating EUR 2,000,000 of additional economic/patrimonial value within 5 years.

The guiding optimization metric is:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

Code volume, test count, milestone count, infrastructure depth and diagnostic depth are not goals by themselves.

## 3. Product priority rule

Every substantial work package must state how it reduces the distance to the first economically actionable real case.

If a task does not materially improve at least one of the following, it should normally be deprioritized, frozen or stopped:

- expected economic contribution;
- usable product value;
- reliability strictly necessary for the product;
- reduction of Product Owner manual work;
- validated knowledge required for a Product Critical decision.

## 4. Work classification

All significant work is classified as:

- `A — Product Critical`
- `B — Material Upgrade`
- `C — Optimization`
- `D — Diagnostic / Technical`

Current project interpretation:

- first approved real source: `A`;
- first real ingestion through classification and economics: `A`;
- first economically actionable reviewer case: `A`;
- source/privacy/legal controls necessary to make those steps lawful and safe: `A/B`;
- additional governance, infrastructure or diagnostics not required for the vertical slice: `C/D`;
- repeated manual Product Owner involvement in technical diagnostics: disfavored unless required to control an `A` risk.

## 5. MVP-1 — First Economically Actionable Case

### Objective

Demonstrate that the platform can transform a lawful, approved real source into a human-reviewable case with enough provenance and economic information to decide whether further investigation is commercially justified.

### Minimum vertical slice

`APPROVED REAL SOURCE`

`-> bounded acquisition`

`-> normalization`

`-> insurance classification`

`-> candidate case creation`

`-> provenance / evidence package`

`-> case economics`

`-> reviewer console`

`-> human continue / stop decision`

### MVP-1 exit evidence

MVP-1 is not complete merely because tests pass. It requires evidence of all of the following:

1. at least one real source has passed the required source, legal/privacy and technical gates;
2. real source data has traversed the authorized vertical slice without bypassing deterministic controls;
3. at least one real candidate case can be rendered in the reviewer surface, or the real source produces a documented zero-candidate result through the complete pipeline;
4. provenance and relevant evidence are visible to the reviewer;
5. the case economics stage produces a reproducible economic assessment using explicit inputs and assumptions;
6. the Product Owner can make a bounded human decision without acting as repetitive QA, debugger or log transporter;
7. the following commercial measurements are captured from real execution where available.

## 6. Commercial measurements to collect

No commercial threshold is invented in advance. The first real vertical slice must collect enough evidence to establish a baseline for:

- records examined;
- records surviving insurance classification;
- candidate cases produced;
- candidate-to-review conversion rate;
- human review time per candidate;
- automated processing cost per candidate;
- data/source cost per candidate where applicable;
- estimated recoverable value or value band where lawfully and evidentially supportable;
- expected fee/revenue basis where legally supportable;
- principal failure/drop-off reasons;
- false-positive or unresolved-case signals discovered during review;
- additional manual research effort required before commercial action.

These measurements are intended to support a later explicit go / revise / stop commercial decision. They are not permission for outreach, claimant contact, legal representation, fee contracting or claim submission.

## 7. Critical-path interpretation of M3

The California M3 source work is retained only as a critical-path enabler to MVP-1.

The immediate purpose of transport/archive-layout work is therefore not to maximize diagnostic completeness. It is to establish the smallest safe, deterministic and reviewable path that can lead to one approved real source and then to the MVP-1 vertical slice.

The existing California controls remain unchanged unless separately reviewed and authorized:

- fail-closed behavior;
- D-008 `WHOLE_SOURCE_STOP` design;
- versioned contracts;
- consumed single-use approvals remain non-reusable;
- no unauthorized retry;
- no privacy expansion;
- no silent parser/projector/regex/normalization change;
- no source/registry activation without the required gate.

## 8. Repository-first / reuse-first

Before substantial custom implementation of downstream modules, perform explicit reuse scouting and record the outcome.

Preferred order:

`REUSE > WRAP > INSPIRE > CUSTOM`

For important capabilities such as entity resolution, record linkage, evidence graphs, genealogy support, orchestration and reviewer tooling, a candidate is not considered reused merely because it was listed.

Reuse state must progress through:

`DISCOVERED -> BENCHMARKED -> ADOPTED or REJECTED -> INTEGRATED -> USED`

Evaluation must include at least licensing/terms, maintenance, maturity, compatibility, security/privacy, integration cost and commercial fitness.

## 9. Product Owner role

The Product Owner is the approver and final product tester.

The workflow should minimize use of the Product Owner as:

- repetitive QA;
- log transporter;
- debugger;
- dataset annotator;
- executor of long technical command sequences.

Agents should operate in the largest safe bounded package practical:

`precheck -> backup/isolation -> implementation -> test -> diagnostic -> repair -> smoke -> report`

Escalate only material product, commercial, legal/privacy, security or irreversible architecture gates.

## 10. Anti-goals before MVP-1

Unless they are required to unblock an `A` risk, do not prioritize:

- broad platform expansion;
- full multi-state coverage;
- fully automated genealogy;
- automatic outreach;
- automatic claim submission;
- contracts automation;
- infrastructure refactors without vertical-slice benefit;
- additional agent complexity without demonstrated product need;
- repeated diagnostics that do not test a new hypothesis or unblock the real-source path.

## 11. Decision discipline

Before starting a substantial task, answer:

1. What class is this task: A, B, C or D?
2. What specific MVP-1 blocker or exit criterion does it address?
3. Can a mature external component remove or reduce custom work?
4. What evidence will show that the task materially advanced product or commercial validation?
5. What Product Owner involvement is truly necessary?

If these questions cannot be answered credibly, the task should not become the next priority.

## 12. Current strategic sequence

The intended sequence is:

1. resolve the current California transport/archive-layout blocker with the minimum bounded and safe work required;
2. obtain a separately reviewed and freshly authorized real-source verification path when required;
3. achieve one approved real source;
4. immediately shift from source/governance expansion to the MVP-1 vertical slice;
5. measure the commercial baseline from real execution;
6. make an explicit product/commercial decision using the measured evidence before broadening scope.

## 13. Source priority and precedence

For future project work, this document must be read immediately after `AGENTS.md` and before `PROJECT_STATE.md`.

Canonical read order becomes:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Precedence rule:

- law, privacy, security, source authorization and explicit safety controls always prevail;
- accepted architectural decisions and machine contracts remain binding unless explicitly superseded;
- within those constraints, this product strategy governs prioritization and definition of useful progress;
- project execution should optimize for the shortest safe path to MVP-1 rather than maximum infrastructure or governance completeness.
