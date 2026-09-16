# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The live-source mismatch chain remains bounded by the retained classes `ASCII_STRUCTURAL_MISMATCH` and `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`.

The nonconforming-row handling proposal completed human review with decision:

`PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS`

The required policy-decision proposal is now prepared and CI-green. It proposes exactly one deterministic policy for later human review:

`WHOLE_SOURCE_STOP`

Proposal status remains:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

The policy is **not selected, approved or implemented for runtime**. Existing fail-closed STOP behavior remains unchanged while semantic compatibility remains unresolved.

## Policy-Decision Proposal Checkpoint

Branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-decision-proposal`

Functional package checkpoint:

`33abf635dc2b3f3893300b5e6adf3e35abeefcb8`

Package CI:

`35095481531` — **SUCCESS**

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_decision.v1.json`

Schema:

`schemas/common/property_type_nonconforming_row_handling_policy_decision_proposal.schema.json`

Audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL.md`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_decision_proposal.py`

## Proposed Policy — Not Authorized

`WHOLE_SOURCE_STOP`

Control disposition and source continuation are explicitly separated.

Control disposition:

- status: `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- reason: `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- metadata-only: `true`;
- real row/field retained: `false`.

Source continuation:

- continue after nonconforming row: `false`;
- process later rows after trigger: `false`;
- silent row skip: `false`;
- silent continuation: `false`.

This proposal preserves the current fail-closed behavior and creates no new privacy boundary.

## T-1…T-6 Incorporated

The machine contract now locks all mandatory tightenings from the previous human review:

1. control disposition is independent from source continuation;
2. metadata defer is distinct from real-row quarantine;
3. row-specific human inspection remains a separate privacy expansion;
4. current STOP behavior remains in force until explicit later approval;
5. future continuation requires a separate completeness/audit and privacy-reviewed design;
6. policy selection and runtime implementation remain separate gates.

## Validation / Privacy Boundary

Unchanged validation rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, regex relaxation, alternate token acceptance or parser/projector change is authorized.

The proposal permits only non-value-bearing status/reason metadata as the eventual control vocabulary. It does not authorize persistence of exact/derived PROPERTY_TYPE, row/field content or hashes, exact lengths, PROPERTY_ID, owner/holder values or source-derived free text.

All historical execution/privacy/authority approvals remain consumed and non-reusable. No fresh approval token is defined by this proposal.

## Governance State

- policy proposed for human review: `WHOLE_SOURCE_STOP`;
- policy selected for runtime: `false`;
- policy approved for runtime: `false`;
- runtime implementation authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- remediation authorized: `false`;
- additional source execution authorized: `false`;
- source continuation authorized: `false`;
- additional privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW`

Review whether `WHOLE_SOURCE_STOP` should be accepted as the deterministic policy decision. Do not implement it, access the real source, expand privacy exposure, activate source/registry/production classification or enter downstream work during the review.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
