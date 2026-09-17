# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source:

`PRODUCT_STRATEGY_MVP1.md`

Governing decision:

`D-009 — MVP-1 commercial validation becomes the product-priority objective`

The guiding project metric is:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California source work remains active only as the current critical-path enabler to obtain an approved real source for MVP-1.

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

Commercial validation must be based on real execution evidence. No commercial threshold is invented in advance.

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

California SCO `PROPERTY_TYPE` handling remains governed by `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`, accepted policy `WHOLE_SOURCE_STOP`, implementation strategy `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`, and runner output contract `1.2.0`.

The v1.2 implementation, real-source execution proposal/review, fresh single-use authorization, one-shot real-source execution and human execution-evidence review are complete.

The one-shot execution result remains:

`STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`

Human evidence-review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

The evidence is accepted as valid proof that the runner failed closed before body access when the live HEAD metadata no longer matched the pinned transport identity. It provides no new `PROPERTY_TYPE` semantic evidence.

## Strategic Interpretation

This result is a technical success but not yet product/commercial validation.

Current product facts:

- approved real sources: `0`;
- semantic compatibility resolved: `false`;
- production classification active: `false`;
- real candidate cases through MVP-1 vertical slice: `0`;
- commercial baseline from real cases: not yet established.

Therefore the California transport/archive-layout blocker is classified as an `A/B` critical-path enabler only to the extent required to reach one approved real source. Open-ended diagnostic expansion is not a product objective.

## Review Checkpoint

Evidence-review branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-evidence-review`

Evidence-review HEAD:

`9dbdc3c6f1ef05c577c26c9e3524ba74fdbfda56`

Execution base CI:

`35124327126` — **SUCCESS**

Current strategy branch:

`strategy-mvp1-first-economically-actionable-case`

Human evidence-review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`

## Execution Evidence

Real execution trigger checkpoint:

`c32df1725390de8784e9bb2f29bea8b4f933abac`

One-shot workflow run:

`35123686954` — **SUCCESS**, attempt `1`

Cleanup/evidence checkpoint:

`448e209d7c8afaec4e0f4b6efc1e5598803d87e5`

Cleanup/evidence CI:

`35124024271` — **SUCCESS**

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`

Evidence contract test:

`tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`

## Single-Use Approval State

Execution approval ref:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval ref:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They were consumed when run `35123686954` invoked the authorized real-source runner. No retry is authorized and these refs must never be reused. All earlier execution/privacy approvals also remain consumed and non-reusable.

## Actual Bounded Execution Result

Actual request/data usage:

- HEAD requests: `1`;
- Range requests: `0`;
- total HTTP requests: `1`;
- source body bytes read: `0`;
- rows examined: `0`;
- `PROPERTY_TYPE` values observed: `0`.

Expected pinned transport metadata:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`.

Observed live HEAD metadata:

- HTTP status: `200`;
- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

The changed content length and ETag caused deterministic fail-closed stop reason `TRANSPORT_METADATA_DRIFT`. Because this was an unrelated transport stop, v1.2 correctly emitted `control_disposition = null`.

The D-008 `PROPERTY_TYPE_NONCONFORMING_STOPPED / PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE` mapping was not reached.

## Baseline Staleness / Archive Layout

The evidence review found that future execution planning cannot safely refresh only content length and ETag.

The current runner and reviewed sample plan also pin four ZIP local-header offsets:

- `From_500_To_Beyond_1_of_4.csv` → `0`;
- `From_500_To_Beyond_2_of_4.csv` → `59747797`;
- `From_500_To_Beyond_3_of_4.csv` → `96862896`;
- `From_500_To_Beyond_4_of_4.csv` → `134174190`.

Because the live ZIP identity changed, the old transport and archive-layout pins are treated as **stale for future execution planning**. They must not be blindly reused or arithmetically rebased without a separately reviewed verification path.

No new ETag, content length or member offset has been adopted.

## Baseline Refresh Proposal

Completed on the strategy branch:

`docs/audits/M3_CA_SCO_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`

Classification:

`A — Product Critical / MVP-1 critical-path enabler`

Recommended design:

`HEAD -> bounded ZIP tail -> EOCD -> exact Central Directory range -> canonical member local-header offsets`

The proposal intentionally rejects:

- probing around historical offsets;
- arithmetic rebasing;
- sequential archive scanning;
- full ZIP download.

Proposed later execution cap:

- `1` HEAD;
- at most `2` Range GETs;
- at most `3` HTTP requests total;
- at most `262144` response-body bytes total;
- no CSV decompression;
- no row/PII access;
- fail closed on ZIP64, structural ambiguity, cap excess or canonical-member mismatch.

Any resulting transport/layout values are only a `baseline candidate`; they are not automatically adopted into runtime constants.

No network request was performed while preparing this proposal.

## Proof Boundary

The prior execution/review establish only that:

- the live HEAD metadata differed from the pinned transport identity at execution time;
- the runner stopped fail-closed before body access;
- v1.2 evidence remained schema-conforming and privacy-safe;
- approvals were consumed and workflow/trigger were removed.

They do **not** establish whether source contents, ZIP member layout, CSV structure or `PROPERTY_TYPE` semantics changed.

The new proposal also establishes no live source fact; it is design-only.

Semantic compatibility remains unresolved.

## Source / Product Governance State

- D-008 accepted as design: `true`;
- D-009 MVP-1 priority accepted: `true`;
- v1.2 implementation completed and human-reviewed: `true`;
- one-shot real-source execution completed: `true`;
- execution evidence human-reviewed and accepted: `true`;
- transport/archive-layout refresh proposal prepared: `true`;
- refresh proposal human-reviewed: `false`;
- consumed approvals reusable: `false`;
- retry authorized: `false`;
- current transport/archive-layout baseline suitable for blind reuse: `false`;
- baseline refresh execution authorized: `false`;
- another network verification authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged: `true`;
- regex/normalization unchanged: `true`;
- semantic compatibility resolved: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## MVP-1 Commercial Measurements To Establish

Once a real vertical slice is lawfully available, capture at minimum:

- records examined;
- records surviving insurance classification;
- candidate cases produced;
- candidate-to-review conversion;
- human review time per candidate;
- automated processing cost per candidate;
- source/data cost per candidate where applicable;
- economically supportable recoverable-value or value-band evidence where available;
- economically and legally supportable fee/revenue basis where available;
- principal failure/drop-off reasons;
- false-positive or unresolved-case signals;
- additional manual research burden before commercial action.

These are measurement requirements, not predeclared success thresholds.

## Next Recommended Action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

This is a material human gate because the next stage could eventually authorize new source-body Range requests, even though only ZIP structural metadata is intended.

The review should decide whether to approve the Central Directory strategy as the bounded implementation basis. It must not itself perform network access, adopt live values, reuse consumed approvals or activate the source.

If approved, the next automated package should prepare the implementation, deterministic tests and one-shot execution contract; network execution would still require a fresh explicit single-use authorization.

After one approved real source exists, priority shifts immediately to the MVP-1 vertical slice rather than further infrastructure expansion.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
