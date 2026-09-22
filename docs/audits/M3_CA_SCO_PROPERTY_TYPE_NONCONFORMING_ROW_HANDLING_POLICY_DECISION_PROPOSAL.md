# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy Decision Proposal

Date: 2026-09-16

Status: **PROPOSAL PREPARED — HUMAN REVIEW REQUIRED — NO RUNTIME POLICY SELECTED OR AUTHORIZED**

## Purpose

Prepare one deterministic policy candidate for the already reviewed condition that the canonical `PROPERTY_TYPE` field is structurally nonconforming under the unchanged validation rule.

This artifact is offline and design-only. It performs no source/authority request, no real-row access, no hidden-value reconstruction and no runtime modification.

## Base checkpoint

- review branch: `m3-ca-sco-property-type-nonconforming-row-handling-proposal-review`
- base HEAD: `6ef0cbaed7536c61d00888644bc463d9894418f6`
- base CI: `35094679116` — SUCCESS
- review decision: `PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS`
- review audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW.md`

## Evidence boundary

The proposal does not broaden the retained evidence. For one previously examined row only:

1. strict full-row UTF-8 decode succeeded;
2. strict stdlib CSV parse succeeded;
3. the canonical 25-column shape was produced;
4. stdlib field index `1` agreed with the current projector `PROPERTY_TYPE` field;
5. the agreed field failed `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The exact field value, derivatives, frequency, cause and source intent remain unknown.

## Proposed policy for human review

`WHOLE_SOURCE_STOP`

Status:

`PROPOSED_FOR_HUMAN_REVIEW_NOT_AUTHORIZED`

This is proposed because it preserves the existing fail-closed behavior and introduces none of the additional unresolved boundaries required by continuation or real-row quarantine.

It is **not** selected for runtime by this artifact.

## T-1 — Control disposition is separate from continuation

Control disposition:

- status: `PROPERTY_TYPE_NONCONFORMING_STOPPED`
- reason: `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`
- metadata-only: `true`
- real row/field retained: `false`

Source continuation:

- continue after triggering row: `false`
- process later rows after trigger: `false`
- silent skip: `false`
- silent continuation: `false`

The status code does not implicitly grant continuation.

## T-2 — Metadata defer vs real-row quarantine

The proposed policy does not defer or quarantine a real row. It retains only non-value-bearing status/reason codes.

`REAL_ROW_QUARANTINE` remains a separate future option requiring privacy/persistence review and is not proposed for selection now.

## T-3 — Human review boundary

The proposed policy does not require row-specific human inspection. Any future row/value exposure or retention for human review remains a separate privacy expansion.

## T-4 — Preserve current STOP until explicit approval

The repository currently stops at the nonconforming `PROPERTY_TYPE` condition. This artifact proposes formalizing that same behavior, but until a later human review explicitly approves a policy, the current behavior is merely preserved rather than newly selected.

## T-5 — Completeness and audit

Because source continuation is `false`, the proposed policy cannot create a hidden gap by skipping the nonconforming row and continuing downstream.

Any future policy that enables continuation must separately define non-value-bearing completeness/audit evidence and privacy-review every counter/identifier/persistence field before implementation.

## T-6 — Selection and implementation are separate gates

This artifact performs only proposal preparation.

Still separate and unauthorized:

- human policy selection/approval;
- runtime implementation;
- real-source validation;
- privacy expansion;
- source continuation;
- source/registry activation;
- production classification activation.

## Validation boundary unchanged

The machine-locked regex remains:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, ASCII uppercasing, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is proposed or authorized.

## Persistence boundary

Allowed by the proposed control contract only after later policy approval/implementation:

- non-value-bearing status code;
- non-value-bearing reason code.

Not allowed by this proposal:

- exact or transformed `PROPERTY_TYPE`;
- row/field hash or exact length;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No new logging or persistence implementation is performed now.

## Alternatives not proposed now

### Row-level metadata defer with later continuation

Not proposed because continuation would require a separately reviewed completeness/audit contract and additional governance before later rows could be processed.

### Real-row quarantine

Not proposed because retaining actual source content would cross a new privacy/persistence boundary.

### Metadata-only human-review route

Not proposed because metadata-only review cannot resolve the unknown source token semantics and is unnecessary merely to preserve the current fail-closed stop.

## Governance state

Unchanged:

- policy selected for runtime: `false`;
- policy approved for runtime: `false`;
- runtime implementation authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- real-source execution authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- normalization unchanged;
- source policy `PROPOSED`;
- registry disabled/unapproved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- downstream identity/genealogy/matching/outreach/claim gates closed.

## Durable package

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_decision.v1.json`

Schema:

`schemas/common/property_type_nonconforming_row_handling_policy_decision_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_decision_proposal.py`

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW`

A PASS at that future gate may approve the policy decision as design, but must not itself silently implement runtime behavior or authorize a real-source execution unless a later explicit gate says so.
