# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The retained live-source diagnostic chain remains bounded by `ASCII_STRUCTURAL_MISMATCH` and `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`.

The nonconforming-row policy decision completed human review with:

`PASS_POLICY_DECISION_ACCEPTED_AS_DESIGN_IMPLEMENTATION_NOT_AUTHORIZED`

Accepted design policy:

`WHOLE_SOURCE_STOP`

Decision record:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

The required implementation proposal is now prepared and CI-green. It remains design-only and does not authorize or perform any runtime change.

## Implementation Proposal Checkpoint

Branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-proposal`

Functional package checkpoint:

`56e82a2bde7c1d77ac197dc2ac21f84ecd1a930d`

Package CI:

`35097296456` — **SUCCESS**

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`

Schema:

`schemas/common/property_type_nonconforming_row_handling_policy_implementation_proposal.schema.json`

Audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL.md`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_implementation_proposal.py`

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

## Proposed Minimal Implementation — Not Authorized

Strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

The proposal identifies the smallest future implementation delta as:

1. modify only `scripts/ca_sco_property_type_semantic_verification.py`;
2. create a new execution contract `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
3. leave historical execution schema `1.1.0` immutable;
4. preserve the existing legacy result `STOPPED_FAIL_CLOSED` and legacy stop reason `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
5. add a nullable, metadata-only `control_disposition` in future schema `1.2.0`;
6. map only `PROPERTY_TYPE_FORMAT_UNEXPECTED` to:
   - status `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
   - reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
7. keep `control_disposition = null` for other stop reasons and successful results;
8. preserve existing fail-closed control flow so no later source member is processed after the trigger.

No existing result field is removed or reinterpreted.

## Current Runtime — Still Unchanged

Current runner remains schema version:

`1.1.0`

Current mismatch behavior remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- no `control_disposition` field exists in runtime output.

The historical v1.1 execution schema is unchanged. The proposed v1.2 execution schema has **not** been created.

## Regression / Rollback Design

Future implementation acceptance is proposed to use synthetic/offline regression coverage only, including:

- preservation of legacy mismatch status/reason;
- exact D-008 status/reason mapping;
- proof that no later member is requested after the trigger;
- null control disposition for unrelated stops and success;
- rejection of source-value-bearing control fields;
- immutability of historical v1.1 schema/evidence;
- unchanged regex/projector/no-normalization guards.

No real-source test is required to accept the code implementation. Any real-source execution remains a separate later gate.

Rollback requires only reverting the future implementation commit(s); no database, source-state or historical-evidence migration is required.

## Validation / Privacy Boundary

Unchanged validation rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

Only future non-value-bearing control `status_code` and `reason_code` are within the accepted design boundary. Exact/derived PROPERTY_TYPE, real row/field content, hashes, exact lengths, PROPERTY_ID, owner/holder values and source-derived free text remain outside persistence.

All historical execution/privacy/authority approvals remain consumed and non-reusable. No fresh approval token is defined or granted by this proposal.

## Governance State

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- implementation proposal prepared: `true`;
- implementation proposal human-reviewed: `false`;
- policy active in runtime: `false`;
- runtime implementation authorized: `false`;
- proposed execution schema v1.2 created: `false`;
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

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW`

Review the proposed additive v1.2 implementation design, backward compatibility, regression coverage, rollback, privacy and continuation boundaries. Do not modify runtime code, create the v1.2 execution schema, access the real source, grant execution/privacy approvals, activate source/registry/production classification or enter downstream work during this review.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
