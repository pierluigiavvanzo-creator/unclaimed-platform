# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | POLICY-DECISION PROPOSAL PREPARED; HUMAN REVIEW NEXT | proposal `WHOLE_SOURCE_STOP`; package `33abf635...fcb8`; CI `35095481531` SUCCESS; not runtime-authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- first bounded diagnostic run `35019840276`: `ASCII_STRUCTURAL_MISMATCH`;
- source-format one-shot execution run `35090057224`: SUCCESS;
- source-format class: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- all historical execution/privacy approvals consumed and non-reusable;
- nonconforming-row handling proposal and human review completed;
- handling review decision: `PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS`;
- policy-decision proposal package: `33abf635dc2b3f3893300b5e6adf3e35abeefcb8`;
- package CI `35095481531`: SUCCESS;
- proposed policy: `WHOLE_SOURCE_STOP`;
- proposal status: `PROPOSAL_ONLY_NOT_AUTHORIZED`;
- no runtime policy selected or implemented;
- no remediation performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Proposed Policy Contract

The policy-decision proposal separates:

### Control disposition

- `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- metadata-only;
- no real row/field retention.

### Source continuation

- continuation after trigger: `false`;
- later rows after trigger: `false`;
- silent skip/continuation: `false`.

The proposal therefore formalizes the safest current fail-closed shape for later review without changing runtime behavior.

## T-1…T-6 State

All six mandatory tightenings are now machine-locked in the proposal/schema/contract test:

1. disposition and continuation are separate axes;
2. metadata defer is separate from real-row quarantine;
3. row-specific human review remains separately privacy-gated;
4. current STOP behavior remains until explicit approval;
5. future continuation requires a separate completeness/audit and privacy-reviewed design;
6. policy selection and implementation remain separate gates.

## Next Product Work

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW`

The review may accept, reject or require remediation of the proposed `WHOLE_SOURCE_STOP` policy decision. It must not implement runtime behavior or authorize real-source execution merely by reviewing the proposal.

## Still Out of Scope

- runtime handling-policy implementation;
- another real source execution without a new reviewed authorization path;
- reuse of consumed approvals;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- source continuation after the nonconforming row;
- real-row quarantine persistence;
- row-specific human inspection without separate privacy authorization;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
