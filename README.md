# Unclaimed Insurance Platform

Traceable, human-gated platform for turning lawful unclaimed-asset data into reviewable targetability and economic decisions.

## Current product objective

The project is in **PRODUCT VALIDATION / STAGE B PILOT P1**.

Long-term target:

`UNITED STATES + CANADA MULTI-REGISTRY UNCLAIMED-ASSET INTELLIGENCE AND RECOVERY OPERATING PLATFORM`

Current Stage B experiment:

`ONE AUTHORIZED REAL SOURCE -> ONE TARGETABLE BOUNDED CASE -> ONE REVIEWABLE ECONOMIC RESULT`

New York OSC is the first validated source adapter / experiment anchor. It is not the permanent product boundary.

## Current status — 2026-10-09

The deterministic contracts, controller fact binder, two-pass bounded P1 runner, single-use authorization contracts, reviewer surfaces and synthetic tests are implemented.

Current factual state:

- U.S. controller entity: **NOT_YET_FORMED**;
- all seven real-P1 gates: **NOT_GRANTED**;
- real NY OSC preflight: **NOT AUTHORIZED / NOT PERFORMED**;
- real source download: **NOT AUTHORIZED**;
- real candidate materialization: **NOT AUTHORIZED**;
- real owner PII processing: **NOT AUTHORIZED**;
- real P1 result: **NOT YET PRODUCED**;
- commercial evidence: **C0 — HYPOTHESIS**.

No historical approval is reusable.

The current product-critical path is:

`FORM US CONTROLLER -> BIND FACTS -> PROFESSIONAL REVIEW -> FRESH 7-GATE PACKET -> ONE REAL P1 -> HUMAN ECONOMIC REVIEW -> C1 BUYER VALIDATION`

## Repository consolidation — 2026-10-09

Historical point-in-time audits/reviews now live under:

`docs/archive/`

`docs/audits/` is retired.

Current NY OSC execution surface:

`scripts/ny_osc_gate.ps1`
`-> scripts/ny_mvp1_p1_targetability_execute.py`
`-> src/unclaimed_platform/adapters/sources/ny_owner_name_p1_targetability_local.py`

Historical Gate 2–11 scripts and versioned transient runners are retained only because they are part of consumed historical provenance. They are **not current execution entrypoints and their approvals are not reusable**.

Canonical runner lineage metadata:

`src/unclaimed_platform/adapters/sources/ny_owner_name_runner_registry.py`

Shared governance:

`AGENTS_MASTER.md v2.2`

The project-specific `AGENTS.md` remains stricter where required, including the explicit instruction to use normal ChatGPT chat and not Work/Codex unless the Product Owner later changes that rule.

## Product-focus rule

Until P1 is completed and reviewed, new broad source integration, agent expansion, production persistence, generic CRM, paid identity-data stacks and non-critical UI expansion are frozen by default.

Work should directly reduce the time or risk to:

1. establish the real U.S. controller;
2. complete required professional legal/tax review;
3. prepare fresh single-use P1 approvals;
4. execute one bounded real P1;
5. measure `TARGETABILITY_DECISION_COST`;
6. convert the sanitized result into buyer-validation evidence.

The optimization metric is:

`ECONOMIC VALUE × USABLE PRODUCT VALUE / PRODUCT OWNER TIME`

## Safety boundaries

- deterministic policy/state/budget/audit controls;
- versioned machine contracts;
- fail-closed behavior;
- explicit privacy/source authorization gates;
- single-use approvals where specified;
- no silent parser/normalization widening;
- no owner PII in logs or public repository artifacts;
- no paid API/token spend without explicit approval;
- no outreach, representation or claim activity without later explicit legal/product gates.

## Canonical project sources

Read in this order:

1. `AGENTS_MASTER.md`
2. `AGENTS.md`
3. `PRODUCT_STRATEGY_MVP1.md`
4. `docs/NORTH_AMERICA_MULTI_REGISTRY_PRODUCT_TARGET_V1.md`
5. `PROJECT_STATE.md`
6. `ROADMAP.md`
7. `DECISIONS.md`
8. `docs/handovers/HANDOVER_CURRENT.md`

Historical audit/review artifacts under `docs/archive/` are supporting provenance, not current operating truth.

## Local setup

```powershell
git clone https://github.com/pierluigiavvanzo-creator/unclaimed-platform.git
cd unclaimed-platform
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\bootstrap.ps1
.\scripts\test.ps1
.\scripts\smoke.ps1
```

`main` is the canonical integration branch. Before any modification or real execution, verify live remote `main`, CI and the current gate state.
