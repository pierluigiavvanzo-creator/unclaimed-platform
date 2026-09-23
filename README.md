# Unclaimed Insurance Platform

Traceable, human-gated platform for turning lawful unclaimed-life-insurance data into reviewable economic cases.

## Current product objective

The project is in **MVP-1 — First Economically Actionable Case**.

The governing product path is:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

Expanded vertical slice:

`AUTHORIZED REAL SOURCE`
`-> bounded acquisition`
`-> normalization`
`-> insurance classification`
`-> candidate case`
`-> provenance / evidence`
`-> case economics`
`-> reviewer`
`-> human GO / REVISE / STOP`

Tests, governance artifacts, source diagnostics and architecture are supporting controls, not product outcomes.

## Current status — 2026-09-22

The deterministic core, versioned contracts, source adapters, NY OSC real-capable runtime, Gate 7, reviewer API/Streamlit and synthetic MVP-1 slice are implemented and tested.

The current NY path has reached:

- synthetic RAW-literal runtime integration: **IMPLEMENTED + REVIEWED PASS**;
- seventh real-runtime package: **IMPLEMENTED + REVIEWED PASS**;
- seventh transient-local retention approval: **GRANTED_NOT_CONSUMED / SINGLE_USE / NON_REUSABLE**;
- seventh transient-PII approval: **GRANTED_NOT_CONSUMED / SINGLE_USE / NON_REUSABLE**;
- fresh listing preflight: **NOT YET AUTHORIZED / NOT PERFORMED**;
- final execution authorization: **NOT YET GRANTED**;
- real bounded execution: **NOT YET PERFORMED**;
- real candidate/economics/reviewer result: **NOT YET PRODUCED**.

No approval is inferred from another gate.

## Product-focus rule

Until MVP-1 is validated, new governance, source diagnostics, framework expansion, multi-state work, agent expansion, graph infrastructure and UI polish are **frozen by default**.

They may resume only when they directly unblock one of these outcomes:

1. authorize one real source lawfully and safely;
2. execute one bounded real acquisition;
3. carry the real output through classification/candidate/economics/reviewer;
4. produce a reviewable economic result or a documented zero-candidate full-pipeline result.

The optimization metric is:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Next critical gate

`HUMAN_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT_AUTHORIZATION`

Required Product Owner phrase:

`AUTHORIZE_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT`

That gate authorizes **preflight only**. It does not authorize download, owner-file open or final execution.

## Architecture boundaries that remain binding

- deterministic policy/state/budget/audit controls;
- versioned machine contracts;
- fail-closed behavior;
- explicit privacy/source authorization gates;
- single-use approvals where specified;
- no silent parser/normalization widening;
- no owner PII in logs or repository artifacts;
- no outreach, representation or claim activity without later explicit legal/product gates.

## Canonical project sources

Read in this order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

## Local setup

```powershell
git clone https://github.com/pierluigiavvanzo-creator/unclaimed-platform.git
cd unclaimed-platform
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\bootstrap.ps1
.\scripts\test.ps1
.\scripts\smoke.ps1
```

`main` is the canonical integration branch after the owner-authorized history-preserving reconciliation performed for the product-validation reset.
