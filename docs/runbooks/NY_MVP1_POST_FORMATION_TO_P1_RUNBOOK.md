# NY MVP-1 Post-Formation to Real P1 Runbook

Date: 2026-09-24

Status: OFFLINE_PREPARATION_ONLY

Purpose: minimize elapsed time from genuine US-controller formation to one authorized Stage B P1 targetability experiment while preserving all human/legal/privacy gates.

## Non-negotiable starting state

Before Step 1:

- a genuine controller entity exists;
- formation evidence exists outside the public repository;
- no entity fact is invented;
- current GitHub main/CI is re-verified;
- all seven P1 gates are still NOT_GRANTED.

If any condition fails, stop.

## Step 1 — Complete controlled Controller Fact Packet

Use docs/templates/NY_MVP1_CONTROLLER_FACT_PACKET_TEMPLATE.md.

Complete the real machine input outside the public repository unless explicit publication is approved.

No P1 authorization is created.

## Step 2 — Run Controller Fact Binder V1 offline

    python scripts/ny_mvp1_controller_fact_binder.py --input <CONTROLLED_LOCAL_CONTROLLER_FACTS.json> --output <NON_SENSITIVE_ASSESSMENT.json>

Accept only an output validating against schemas/common/ny_mvp1_stage_b_controller_fact_binding_assessment.schema.json.

Required invariants:

- real_p1_execution_allowed = false
- all_seven_p1_gates_state = NOT_GRANTED
- sensitive_or_identifying_values_persisted = false

## Step 3 — Route professional review

If BLOCKED_ENTITY_NOT_FORMED: stop and correct factual state.

If ROUTE_TO_HUMAN_LEGAL_PRIVACY_REVIEW: perform the required territorial/privacy review before any live PII step.

If FACTS_BOUND_US_TRACK_PENDING_PROFESSIONAL_REVIEW: use docs/checklists/NY_MVP1_US_CONTROLLER_CPA_ATTORNEY_QUESTIONS.md and obtain the fact-specific US tax / NY nexus / legal-readiness answers.

No AI-generated legal conclusion substitutes for professional review.

## Step 4 — Re-verify Stage B provider envelope

The currently accepted offline provider candidate is google-search-manual-us-v1.

Current bounds remain:

- authorized US controller operator only;
- manual browser;
- max 3 minimized queries;
- max 900 seconds;
- USD 0 external paid spend;
- no API/bot;
- no paid data broker;
- no consumer-report/FCRA product;
- no outreach;
- no value research;
- AI summaries are not evidence;
- underlying source page must be verified;
- no persisted query strings/URLs/screenshots/snippets containing owner PII.

Before real use, verify that provider/terms/legal basis remain current for the actual controller facts.

## Step 5 — Verify code checkpoint and CI

Before creating any fresh authorization packet:

- verify remote main HEAD;
- verify latest successful GitHub CI;
- verify the final runner checkpoint;
- verify no P1 gate has been granted/reused;
- verify controller assessment and professional-review evidence references are available.

Historical approvals are never reusable.

## Step 6 — Prepare fresh single-use P1 gate packet

Prepare, but do not grant, the seven gates:

1. transient local-file gate;
2. L1 transient-PII gate;
3. fresh-listing preflight gate;
4. L1 execution gate;
5. L2-A targetability-PII gate;
6. L2-A provider/budget gate;
7. L2-A execution gate.

Every gate must be bound to the then-current runner checkpoint and successful CI evidence required by its contract.

## Step 7 — Product Owner authorization

Present the complete packet to the Product Owner.

Without fresh explicit approval for the exact packet: STOP.

No remote preflight, download, real candidate materialization, real PII processing or external PII query occurs.

## Step 8 — Execute one bounded P1 only

Stage B question:

CAN THE CORE ENGINE TURN ONE AUTHORIZED REGISTRY RECORD INTO A RELIABLE TARGETABILITY DECISION AT CONTROLLED COST?

Allowed end states include an evidence-backed targetability decision or a bounded STOP.

Measure:

- TARGETABILITY_DECISION_COST;
- machine cost evidence;
- operator/reviewer time evidence;
- service-need state;
- resolvability state;
- targetability state/class when supportable;
- explicit stop reason when stopped.

P1 does not require outreach, known recoverable value, fee agreement, claim or recovery.

## Step 9 — Human economic review

After P1:

- review evidence;
- review TARGETABILITY_DECISION_COST;
- review operator time;
- review whether a bounded useful lead was produced;
- decide GO / REVISE / STOP for P2.

Do not expand to P2 automatically.

## Step 10 — Conditional P2 / North America expansion

Only if P1/P2 evidence supports continuation:

- approximately five bounded P2 cases;
- then, if justified, freeze generic Source Adapter Contract;
- prioritize additional US registries;
- prioritize Canadian registries;
- reuse registry-independent confidence/targetability/economics/CRM/contracts components.

Do not convert registry count into a vanity metric.

## Rollback / stop rule

At any unresolved legal/privacy/source/authorization conflict: STOP / HUMAN REVIEW.

No retry or workaround may silently expand the authorization envelope.
