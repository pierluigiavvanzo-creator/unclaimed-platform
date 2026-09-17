# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution Evidence Review / Source Decision — 2026-09-17

Date: 2026-09-17

Status: **EVIDENCE ACCEPTED — CURRENT SOURCE REJECTED FOR MVP-1 UNDER EXISTING CONTRACT — NO FURTHER CA RETRY AUTHORIZED**

## Gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

Classification: `A — Product Critical`.

## Reviewed evidence

Execution run:

`35222675324`

Trigger commit:

`d826492735b6f6665d59ab875e470074005a8191`

Artifact digest:

`sha256:3e52cdff838de4dfa73bf62b0361af6938be73f2aa381c68ecaf8bc1b1d37fe9`

Persisted machine evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_2026_09_17.json`

## Evidence review result

`PASS_EXECUTION_EVIDENCE_ACCEPTED`

The evidence validates against execution contract `1.2.0`, stayed inside all request/byte/sample caps, used the approved fresh refs exactly once, retained all safety flags as `false`, and contains only the already reviewed derived evidence boundary.

Transport verification matched the adopted source baseline exactly. Therefore the stop was not caused by transport/archive drift.

The live run produced:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- D-008 control status `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- D-008 reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

No exact hidden PROPERTY_TYPE value is available or required for this decision.

## Source decision

`REJECT_CA_SCO_500_PLUS_AS_APPROVED_MVP1_SOURCE_UNDER_CURRENT_V1_2_CONTRACT`

Meaning:

- this is **not** a claim that the California source is invalid;
- this is **not** a permanent ban on the source;
- it means the source cannot lawfully/deterministically continue through the current MVP-1 pipeline while D-008 `WHOLE_SOURCE_STOP` and the unchanged validation boundary remain in force.

Current source state remains:

- source policy: `PROPOSED`;
- registry enabled: `false`;
- registry approved: `false`;
- approved real sources: `0`;
- semantic compatibility resolved for current contract: `false / nonconforming bounded evidence`;
- production classification: inactive;
- downstream identity/genealogy/beneficiary/outreach/claim work: blocked.

## Approval state

Both fresh approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry, widening, normalization, regex change, parser/projector change or privacy expansion is authorized by this review.

## Product / commercial decision

The MVP-1 strategy requires minimizing distance to the first economically actionable case. The current California source has now produced direct real evidence of a contract-level stop after transport readiness was solved.

Therefore the default commercial path is:

`FREEZE_CURRENT_CA_SOURCE_UNDER_EXISTING_CONTRACT -> SELECT_ALTERNATE_REAL_SOURCE_FOR_MVP1`

Reopening California should require an explicit Product Owner decision to redesign the PROPERTY_TYPE semantic contract, because another identical execution cannot create new decision value.

## Next single action

`SELECT_ALTERNATE_REAL_SOURCE_FOR_MVP1`

Selection must optimize for:

1. lawful/public or otherwise authorized access;
2. explicit provenance and source terms;
3. data shape compatible with the existing acquisition/normalization/classification vertical slice with minimal custom work;
4. insurance-relevant signal sufficient to reach case economics;
5. low Product Owner manual burden;
6. shortest credible time to one approved real source.

Use `REUSE > WRAP > INSPIRE > CUSTOM`; do not add platform infrastructure before a concrete source candidate requires it.