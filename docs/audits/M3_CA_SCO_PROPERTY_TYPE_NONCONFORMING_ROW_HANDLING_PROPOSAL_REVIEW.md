# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Proposal Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS WITH MANDATORY POLICY-DECISION TIGHTENINGS — NO RUNTIME CHANGE AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- proposal branch: `m3-ca-sco-property-type-nonconforming-row-handling-proposal`
- proposal final HEAD: `9d5dc3feaa3a9fa63ce5af0dd2c3749a7bee7c87`
- proposal functional package checkpoint: `f29c4423c885d37956bea4aba02e4db241409452`
- proposal package CI: `35093840690` — SUCCESS
- proposal final CI: `35094071730` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling.v1.json`
- schema: `schemas/common/property_type_nonconforming_row_handling_proposal.schema.json`
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL.md`
- contract test: `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_proposal.py`

This review is repository-only. It performs no `claimit.ca.gov` request, no authority request, no real-row inspection, no hidden-value reconstruction, no privacy expansion and no runtime handling change.

## Decision

`PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS`

The proposal is accepted as a valid, fail-closed design comparison. It correctly keeps `selected_option: null`, preserves the unchanged validation rule, forbids silent correction/normalization/acceptance/continuation, and makes real-row retention or row-specific inspection a separately governed privacy expansion.

This PASS does **not** select any runtime handling policy and does not authorize implementation, real-source execution, source continuation, quarantine persistence, row-specific human inspection, source activation or production classification.

## Reviewed evidence boundary

The review remains bounded to the retained conclusion for one previously examined row:

1. strict full-row UTF-8 decoding succeeded;
2. strict stdlib CSV parsing succeeded;
3. exactly one canonical 25-column record was produced;
4. stdlib field index `1` agreed with the current custom projector PROPERTY_TYPE field;
5. that shared field failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The exact field value, token shape, frequency, cause and source intent remain unknown and must not be inferred.

## Proposal strengths accepted by review

The reviewed package machine-locks the following:

- exactly three design options are compared;
- no option is selected or authorized;
- current parser/projector remains unchanged;
- current regex remains unchanged;
- no trim, ASCII uppercasing or Unicode normalization is introduced;
- silent row skipping is forbidden;
- silent source continuation is forbidden;
- semantic acceptance/correction is forbidden;
- non-value-bearing status/reason codes are defined;
- exact/derived PROPERTY_TYPE and protected row/owner identifiers remain non-persistable;
- real-row quarantine retention is a future privacy expansion;
- row-specific human inspection is a future privacy expansion;
- all prior approvals remain consumed/non-reusable;
- source policy/registry/production/downstream gates remain closed.

The contract test also rejects silent policy selection, source continuation, real-row retention authorization, runtime authorization and regex relaxation.

## Mandatory tightenings for the next policy-decision artifact

The proposal is sufficient for comparison, but a later policy-decision artifact must remove the following ambiguity before any policy can be selected or implemented.

### T-1 — Separate control disposition from source continuation

The artifact must model two independent axes:

1. **control disposition** — what non-value-bearing control event/state is emitted when a nonconforming row is encountered;
2. **source continuation** — whether processing may proceed to later rows.

A human-review route or deferred status must not implicitly mean continuation, and a continuation decision must not be smuggled in through a status label.

### T-2 — Split metadata-only defer from real-row quarantine

`ROW_LEVEL_DEFER_OR_QUARANTINE` currently groups two materially different privacy states. The policy-decision artifact must distinguish:

- metadata-only defer, which retains no real row or field content; and
- real-row/field quarantine, which is a privacy/persistence expansion and remains unauthorized without a separate reviewed authorization path.

The word “quarantine” must not imply that real source content is already retained.

### T-3 — Keep human review metadata-only unless separately authorized

`HUMAN_REVIEW_ROUTE` may create only a non-value-bearing review event under the current boundary. Any row-specific human inspection that exposes or persists actual row/field content requires a separate privacy design/review/authorization path.

### T-4 — Preserve the existing fail-closed runtime until a later policy is explicitly approved

No new option is selected by this review. Until a later policy-decision artifact is separately reviewed and authorized, the existing behavior remains: stop on the nonconforming PROPERTY_TYPE condition rather than silently skip, continue, transform or accept it.

This is preservation of the current behavior, not selection of a new runtime policy.

### T-5 — Any future continuation policy must define completeness evidence

If a later artifact proposes source continuation after a nonconforming row, it must explicitly define non-value-bearing completeness/audit evidence sufficient to show that a row was deferred without silently disappearing. Any counters, identifiers or persistence fields must be specified and privacy-reviewed before implementation; no source-derived row content is authorized by this review.

### T-6 — Selection and implementation remain separate gates

A later design artifact may propose one deterministic handling policy, but policy selection must be explicit and human-reviewed. Runtime implementation, any real-source validation, any privacy expansion and source activation remain separate later gates.

## Assessment of the three current options

### `WHOLE_SOURCE_STOP`

Valid fail-closed design. It has the strongest semantic boundary and no new privacy exposure, but can block the source segment due to one row. This review does not select it as the future policy; it only recognizes that the existing runtime already stops at the mismatch.

### `ROW_LEVEL_DEFER_OR_QUARANTINE`

Valid comparison category but insufficiently granular for selection because metadata-only defer and real-row quarantine have different privacy consequences, and continuation is a separate policy decision. T-1, T-2 and T-5 are therefore mandatory before this path can be selected.

### `HUMAN_REVIEW_ROUTE`

Valid governance route as metadata-only escalation. It does not by itself resolve the unknown source semantics. Actual row/value inspection would cross a separate privacy boundary, so T-3 is mandatory before any row-specific review workflow can be proposed.

## Governance state after review

Unchanged and fail-closed:

- handling policy selected: `false`;
- runtime handling change authorized: `false`;
- real-source execution authorized: `false`;
- privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- source continuation after nonconformance authorized: `false`;
- parser/projector unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- all prior approval tokens consumed / non-reusable;
- source policy `PROPOSED`;
- registry disabled / not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission BLOCKED.

## Next single action

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL`

That artifact must incorporate T-1 through T-6 and may propose a single deterministic policy for subsequent human review, but must not implement it or authorize real-source execution.

No new source request, privacy expansion, runtime change, policy/registry activation or downstream work is authorized by this review.