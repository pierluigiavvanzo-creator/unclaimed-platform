# FRONTEND_PRODUCT_UX_V1_OFFLINE

Date: 2026-09-25

Status: OFFLINE / SYNTHETIC / HUMAN DESIGN REVIEW REQUIRED

## Objective

Produce three navigable product-interface alternatives without changing Stage B authorization, accessing real sources or exposing real owner PII.

The UX lab is a decision artifact, not the production UI.

## Product boundary

Long-term product:

NORTH AMERICA MULTI-REGISTRY UNCLAIMED-ASSET INTELLIGENCE AND RECOVERY OPERATING PLATFORM.

Current experiment:

ONE bounded NY OSC Stage B targetability experiment.

The UX must make that distinction visible.

## Reuse-first benchmark

### Existing Next.js reviewer console

Decision: REUSE.

Reason:

Already in the repository, TypeScript checked and production-build tested in CI. It is the lowest-risk base for a future product frontend.

### shadcn/ui official blocks

Reference:

https://ui.shadcn.com/blocks

Decision: DEFER FOR PRODUCTION SHELL AFTER CONCEPT SELECTION.

Fit:

Strong sidebar, dashboard, chart and data-table patterns. Appropriate candidate for a production design system without requiring a bespoke component framework.

### Tremor

Reference:

https://npm.tremor.so/

Decision: DEFER / POSSIBLE EXECUTIVE-ANALYTICS COMPONENT SOURCE.

Fit:

Useful dashboard/chart primitives, but adding it before a concept is selected would expand dependencies for throwaway mockups.

### Vercel Next.js templates

Reference:

https://vercel.com/templates/next.js

Decision: INSPIRE, DO NOT IMPORT WHOLESALE.

Fit:

Useful reference implementations, but wholesale template adoption would bring unrelated structure/auth/theme decisions into a governed repository.

## V1 dependency decision

Add no new frontend dependency.

Use:

- Next.js already present;
- React already present;
- TypeScript already present;
- CSS modules / existing CSS;
- synthetic local fixtures.

Reason:

The V1 goal is to select workflow and visual hierarchy, not to commit to a component vendor.

## Routes

- /ux-lab
- /ux-lab/concept-a
- /ux-lab/concept-b
- /ux-lab/concept-c

The existing M3 console remains available.

## Concept A — Intelligence Control Room

Primary user:

operations/reviewer.

Primary strengths:

- high information density;
- stable sidebar;
- targetability pipeline;
- source readiness;
- opportunity table;
- visible governance state.

Best candidate for:

permanent operating shell.

Risk:

can become too technical if every engineering metric is surfaced.

## Concept B — Executive Intelligence

Primary user:

Product Owner / management / investor-facing internal review.

Primary strengths:

- rapid business comprehension;
- funnel and economic hierarchy;
- clean light presentation;
- source expansion readiness;
- clear management exceptions.

Best candidate for:

executive dashboard / overview.

Risk:

too shallow for investigators if used as the only interface.

## Concept C — Evidence Investigation Workspace

Primary user:

reviewer / investigator / legal-compliance human gate.

Primary strengths:

- queue -> evidence -> decision flow;
- explicit provenance/evidence area;
- contradictions remain visible;
- targetability and economics sit next to the human decision boundary.

Best candidate for:

case detail workspace.

Risk:

higher learning curve.

## Recommended composition hypothesis

Do not force one concept to solve every job.

Candidate product composition:

A = permanent application shell / operations
B = executive dashboard route
C = case-detail investigation route

This is a hypothesis for human review, not an approved frontend architecture.

## Non-negotiable UX rules

1. Never imply that a future registry is already supported.
2. Always distinguish synthetic/demo metrics from measured production KPIs.
3. Do not turn a visual button into an authorization bypass.
4. Real write actions require deterministic backend authorization.
5. Before real PII web access, authentication/RBAC and durable access audit are prerequisites.
6. Evidence, contradictions, provenance and cost must remain inspectable.
7. Human-gated decisions must be visually distinct from automated observations.
8. Avoid NY-specific semantics in generic navigation and shared components.

## V1 acceptance criteria

- all three concepts are navigable;
- no remote API/source access is added;
- no real PII is embedded;
- future US/Canada sources are explicitly marked unsupported;
- no production KPI threshold is invented;
- existing reviewer console remains available;
- frontend lint, typecheck and build remain green;
- Python contract/smoke/full suite remains green through canonical CI.

## Human decision after V1

The Product Owner should select:

- preferred shell;
- preferred visual tone;
- whether executive view is a first-class route;
- whether case-detail should use the investigation workspace model.

Only after that decision should a permanent component library be added.
