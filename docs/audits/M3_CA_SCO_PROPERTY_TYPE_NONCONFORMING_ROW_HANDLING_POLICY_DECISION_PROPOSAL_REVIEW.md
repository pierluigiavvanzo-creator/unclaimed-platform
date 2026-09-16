# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy Decision Proposal Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS — POLICY DECISION ACCEPTED AS DESIGN — RUNTIME IMPLEMENTATION NOT AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- proposal branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-decision-proposal`
- proposal final HEAD: `5e6f538a03f0b5e61c4559a27431e9718b29e265`
- functional package checkpoint: `33abf635dc2b3f3893300b5e6adf3e35abeefcb8`
- package CI: `35095481531` — SUCCESS
- final proposal CI: `35095734936` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_decision.v1.json`
- schema: `schemas/common/property_type_nonconforming_row_handling_policy_decision_proposal.schema.json`
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL.md`
- contract test: `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_decision_proposal.py`

This review is repository-only. It performs no request to `claimit.ca.gov` or any authority endpoint, no real-row inspection, no hidden-value reconstruction, no approval-token reuse, no privacy expansion and no runtime modification.

## Decision

`PASS_POLICY_DECISION_ACCEPTED_AS_DESIGN_IMPLEMENTATION_NOT_AUTHORIZED`

The reviewed policy decision is accepted as the deterministic design decision for the already evidenced nonconforming `PROPERTY_TYPE` condition:

`WHOLE_SOURCE_STOP`

This decision is accepted **as design only**. It does not itself modify runtime behavior, authorize code changes, authorize a real-source execution, activate the source/registry, or resolve semantic compatibility.

Machine/governance state after this review must therefore distinguish:

- policy decision accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- policy selected/activated in runtime: `false`;
- runtime implementation authorized: `false`;
- real-source execution authorized: `false`.

## Evidence boundary reviewed

The review remains bounded to one previously examined row and supports only that:

1. strict full-row UTF-8 decoding succeeded;
2. strict stdlib CSV parsing succeeded;
3. exactly one canonical 25-column record was produced;
4. stdlib field index `1` agreed with the current custom projector `PROPERTY_TYPE` field;
5. that agreed field failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The exact field value, token shape, frequency, cause and source intent remain unknown and must not be inferred.

## Why `WHOLE_SOURCE_STOP` passes review

The accepted design preserves the strongest currently supported fail-closed boundary without introducing unsupported semantics:

- it does not transform or normalize the source value;
- it does not relax the regex;
- it does not change parser/projector behavior;
- it does not silently skip the nonconforming row;
- it does not process later rows after the trigger;
- it does not retain the real row or field;
- it does not require row-specific human inspection;
- it does not introduce a new privacy/persistence boundary;
- it is consistent with the current runtime already stopping on the nonconforming condition.

The review does **not** conclude that the source value is invalid in the source's own semantics; it only accepts a platform-side fail-closed handling policy while semantic compatibility remains unresolved.

## T-1 through T-6 review

### T-1 — disposition and continuation are independent

PASS. The proposal separately fixes a metadata-only control disposition and source continuation=`false`. The status code does not imply continuation.

### T-2 — metadata defer vs real-row quarantine

PASS. Neither is selected by `WHOLE_SOURCE_STOP`; real-row quarantine remains a separate privacy/persistence expansion.

### T-3 — human review boundary

PASS. The accepted design requires no row-specific human inspection. Any future actual row/value exposure remains separately privacy-gated.

### T-4 — current STOP preserved until implementation

PASS. This review accepts the design decision but makes no runtime change. Existing STOP behavior remains the current operational behavior until a later implementation gate completes.

### T-5 — completeness/audit

PASS for the accepted design. Continuation is disabled, so the design cannot silently omit the triggering row and continue with later rows. Any future continuation design remains separately governed.

### T-6 — decision and implementation remain separate

PASS. This review closes only the policy-decision design gate. Runtime implementation and any later real-source validation remain separate explicit gates.

## Accepted non-value-bearing control shape

For a future separately authorized implementation, the accepted design uses:

- status: `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- reason: `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation after trigger: `false`;
- later rows processed after trigger: `false`.

The design permits no persistence of exact/derived `PROPERTY_TYPE`, real row/field content, hashes, exact row/field lengths, `PROPERTY_ID`, owner/holder values or source-derived free text.

These fields are accepted as a design contract only; this review does not implement them.

## Validation boundary unchanged

The regex remains:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, ASCII case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

## Governance state after review

- policy decision accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- policy active in runtime: `false`;
- runtime implementation authorized: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- trimming/casing/normalization unchanged;
- all historical approvals consumed / non-reusable;
- source policy `PROPOSED`;
- registry disabled / not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission BLOCKED.

## Next single action

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL`

The implementation proposal must describe the smallest deterministic runtime/contract/test changes required to implement the accepted `WHOLE_SOURCE_STOP` design, including rollback and regression coverage, while preserving the validation and privacy boundaries above.

Preparing that artifact must **not** itself:

- modify runtime code;
- access a real source or authority endpoint;
- create or grant execution approval tokens;
- expose/retain a real row or field;
- enable source continuation;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.
