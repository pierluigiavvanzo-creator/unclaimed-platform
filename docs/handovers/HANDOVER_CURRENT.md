# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`strategy-mvp1-first-economically-actionable-case`

Created from prior evidence-review HEAD:

`9dbdc3c6f1ef05c577c26c9e3524ba74fdbfda56`

Prior execution-checkpoint CI:

`35124327126` — **SUCCESS**

## Priority Product Strategy

Priority source:

`PRODUCT_STRATEGY_MVP1.md`

Governing decision:

`D-009 — MVP-1 commercial validation becomes the product-priority objective`

Primary product objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

The project must optimize for the shortest lawful, privacy-safe, deterministic path to a real economically reviewable case rather than maximum infrastructure, governance or diagnostic completeness.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect the relevant M3 evidence/audit/runtime artifacts as needed.

Precedence:

- law, privacy, security, source authorization and explicit safety controls prevail;
- accepted architecture decisions and machine contracts remain binding unless explicitly superseded;
- within those constraints, `PRODUCT_STRATEGY_MVP1.md` governs work prioritization and definition of useful progress.

## Current Strategic Interpretation

The engineering/governance foundation is strong, but commercial validation remains incomplete.

Current facts:

- M0, M1 and M2: VERIFIED;
- Streamlit reviewer: ACTIVE;
- approved real sources: `0`;
- production classification: inactive;
- semantic compatibility: unresolved;
- real candidate cases through MVP-1: `0`;
- commercial baseline from real cases: not established.

Therefore M3 California work is retained only as a critical-path enabler to obtain the first approved real source.

## Completed M3 Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

Human review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`

## Reviewed Execution Evidence

One-shot execution run:

`35123686954` — **SUCCESS**, attempt `1`

Real execution trigger checkpoint:

`c32df1725390de8784e9bb2f29bea8b4f933abac`

Cleanup/evidence checkpoint:

`448e209d7c8afaec4e0f4b6efc1e5598803d87e5`

Cleanup/evidence CI:

`35124024271` — **SUCCESS**

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Machine result:

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

Actual usage:

- HEAD requests: `1`;
- Range requests: `0`;
- HTTP requests total: `1`;
- source body bytes read: `0`;
- rows examined: `0`;
- distinct `PROPERTY_TYPE` codes observed: none.

## Transport / Archive-Layout Blocker

Pinned expected transport identity:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type: `application/zip`;
- Accept-Ranges: `bytes`.

Observed live HEAD metadata from the consumed one-shot execution:

- HTTP status: `200`;
- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

The runner/sample plan also pins four ZIP local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` — `0`;
2. `From_500_To_Beyond_2_of_4.csv` — `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` — `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` — `134174190`.

Because live ZIP identity changed, transport identity and archive-layout assumptions must be refreshed/revalidated together. Historical offsets must not be blindly reused or arithmetically rebased.

## Approval State

Consumed execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry is authorized. No current network verification is authorized. No privacy expansion is authorized.

## Governing Runtime / D-008 State

Decision:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

Current runner output contract:

`1.2.0`

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

## Source / Downstream Governance

Current state:

- consumed approvals reusable: `false`;
- retry authorized: `false`;
- current transport/archive-layout baseline suitable for blind reuse: `false`;
- baseline refresh authorized: `false`;
- another network verification authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

## MVP-1 Target Vertical Slice

`APPROVED REAL SOURCE`

`-> bounded acquisition`

`-> normalization`

`-> insurance classification`

`-> candidate case creation`

`-> provenance / evidence package`

`-> case economics`

`-> reviewer console`

`-> human continue / stop decision`

MVP-1 must collect real commercial baseline measurements rather than assume commercial viability.

## Work Classification Rule

Every substantial task must state:

1. class `A/B/C/D`;
2. exact MVP-1 blocker or exit criterion addressed;
3. reuse-first outcome for nontrivial custom work;
4. evidence expected from completion;
5. minimum Product Owner involvement required.

Work that cannot credibly answer these points should not become the next priority.

## SINGLE NEXT ACTION

Prepare exclusively:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

Classification:

`A/B — MVP-1 critical-path enabler`

Purpose:

Define the smallest deterministic, privacy-safe and fail-closed method by which transport identity and ZIP archive-layout/member offsets could later be refreshed or revalidated together so that a fresh, separately authorized source verification can become possible.

This task is repository-only and design-only.

It must not:

- perform California SCO or other external requests;
- perform HEAD, Range GET or authority retrieval;
- reuse consumed approval refs;
- grant fresh approvals;
- create a network workflow;
- retry the prior execution;
- update `EXPECTED_LENGTH`, `EXPECTED_ETAG` or canonical member offsets;
- infer or arithmetically rebase offsets;
- modify runner/parser/projector/regex/normalization;
- widen privacy or source continuation;
- activate source policy, registry or production classification;
- begin identity resolution, genealogy, beneficiary matching, outreach or claim work.

The proposal must explicitly reject diagnostic work that does not materially improve the path to an approved real source.

## After The Current Blocker

The intended strategic sequence is:

1. human-review any later network revalidation design;
2. obtain fresh single-use authorization before the first request;
3. achieve one approved real source;
4. immediately shift to the MVP-1 vertical slice;
5. capture records examined, classification survival, candidate production, review time, automated/source cost, supportable value/revenue basis, failure reasons and manual research burden where available;
6. perform an explicit product-commercial `GO / REVISE / STOP` review before broadening scope.

No outreach, claimant contact, legal representation, fee contracting or claim submission is authorized merely by reaching MVP-1.

## Restart Instruction

1. verify remote HEAD of `strategy-mvp1-first-economically-actionable-case`;
2. verify CI for the latest relevant checkpoint when available;
3. read the six canonical sources in the order above;
4. execute only the `SINGLE NEXT ACTION`;
5. preserve all source/privacy/fail-closed boundaries;
6. optimize for MVP-1 product/commercial evidence, not governance volume.
