# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Proposal Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-decision-proposal`
- functional package checkpoint: `33abf635dc2b3f3893300b5e6adf3e35abeefcb8`
- package CI: `35095481531` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_decision.v1.json`
- schema: `schemas/common/property_type_nonconforming_row_handling_policy_decision_proposal.schema.json`
- audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL.md`
- contract test: `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_decision_proposal.py`
- proposal status: `PROPOSAL_ONLY_NOT_AUTHORIZED`

## Base Review

Previous completed gate:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW`

Decision:

`PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS`

Base review branch:

`m3-ca-sco-property-type-nonconforming-row-handling-proposal-review`

Base review HEAD:

`6ef0cbaed7536c61d00888644bc463d9894418f6`

Base review CI:

`35094679116` — SUCCESS

## Evidence Boundary

The retained evidence remains bounded to one previously examined row:

1. strict full-row UTF-8 decode succeeded;
2. strict stdlib CSV parse succeeded;
3. exactly one canonical 25-column record was produced;
4. stdlib field index `1` agreed with the custom projector PROPERTY_TYPE field;
5. that agreed field failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Do not infer the exact value, token shape, frequency, cause, source intent or correctness of any transformation.

## Proposed Policy — Human Review Only

`WHOLE_SOURCE_STOP`

Selection status:

`PROPOSED_FOR_HUMAN_REVIEW_NOT_AUTHORIZED`

The proposal chooses this as the single candidate for human policy-decision review because it preserves the existing fail-closed STOP behavior and requires neither source continuation nor real-row retention.

It is **not** selected, approved or implemented for runtime.

## T-1 — Separate Control Disposition and Source Continuation

Control disposition:

- status `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- metadata-only;
- no real row/field retention;
- no row-specific human inspection.

Source continuation:

- continue after the triggering row: `false`;
- process later rows after the trigger: `false`;
- silent row skip: `false`;
- silent source continuation: `false`.

## T-2 — Metadata Defer vs Real-Row Quarantine

The proposal does not select defer or quarantine. Real-row/field quarantine remains a separate privacy/persistence expansion and is unauthorized.

## T-3 — Human Review Boundary

The proposed policy does not require row-specific human inspection. Any future actual row/value exposure or retention requires a separate reviewed privacy authorization path.

## T-4 — Current STOP Preserved

Until the proposed policy completes later human review and a separate implementation gate, the existing runtime behavior remains unchanged: STOP on nonconforming PROPERTY_TYPE.

No skip, continuation, transformation, normalization or semantic acceptance is allowed.

## T-5 — Completeness / Audit

Because continuation is disabled, this proposal cannot create a hidden completeness gap by silently omitting the row and processing later rows.

Any future continuation proposal must separately define non-value-bearing completeness/audit evidence, and any counters/identifiers/persistence fields must be privacy-reviewed before implementation.

## T-6 — Selection and Implementation Remain Separate

This proposal performs only design preparation.

Still unauthorized:

- runtime policy selection/approval;
- runtime implementation;
- real-source validation/execution;
- source continuation;
- privacy expansion;
- real-row quarantine;
- row-specific human inspection;
- source/registry activation;
- production classification activation.

## Validation / Persistence Boundary

Unchanged validation rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, ASCII uppercase, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

The proposal allows only non-value-bearing status/reason codes in the future control contract. It does not authorize persistence of exact/derived PROPERTY_TYPE, row/field hashes or exact lengths, PROPERTY_ID, owner/holder values, source-derived free text or real row/field content.

No new approval token is defined or granted.

All historical approvals remain consumed and non-reusable.

## Runtime / Governance State

Unchanged and fail-closed:

- policy proposed for human review: `WHOLE_SOURCE_STOP`;
- policy selected for runtime: `false`;
- policy approved for runtime: `false`;
- runtime implementation authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- trimming/casing/normalization unchanged;
- remediation authorized: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- source policy `PROPOSED`;
- registry disabled / not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission BLOCKED.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW`

Review the proposed `WHOLE_SOURCE_STOP` policy decision against the retained evidence, T-1 through T-6, fail-closed behavior, completeness and privacy boundaries.

During this review do **not**:

- access `claimit.ca.gov` or authority endpoints;
- inspect or reconstruct the hidden PROPERTY_TYPE value;
- select or implement runtime behavior silently;
- reuse consumed approvals;
- change parser/projector or regex;
- introduce trim/case/Unicode normalization;
- persist/expose a real row or field;
- enable source continuation;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.

A PASS at this review may accept the policy decision as design, but runtime implementation and any real-source execution remain separate later gates.
