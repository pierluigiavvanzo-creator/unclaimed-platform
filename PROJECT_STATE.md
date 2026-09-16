# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance remains resolved only within the recorded proof boundary. The retained real-source diagnostic chain remains bounded by `ASCII_STRUCTURAL_MISMATCH` and `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`; semantic compatibility with the hidden source value remains unresolved.

The nonconforming-row handling design is governed by:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design policy:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

The v1.2 implementation is complete, CI-green and human-reviewed as conforming.

Implementation review result:

`PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

A non-executing proposal for a future bounded v1.2 real-source verification has now been prepared and validated in CI. It requires separate human proposal review and later fresh execution/privacy authorization before any source access.

Current proposal status:

`PROPOSAL_PREPARED_CI_GREEN_HUMAN_PROPOSAL_REVIEW_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

## Real-Source Execution Proposal Checkpoint

Proposal branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal`

Base human-review checkpoint:

`7b6397f0e89d8ee1640be2eea4f8651f6b74478c`

Base CI:

`35105522139` — **SUCCESS**

Functional proposal checkpoint:

`19c395a6f89dbec1941566366274070db98cacd0`

Functional proposal CI:

`35106612846` — **SUCCESS**

Proposal audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL.md`

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Proposal schema:

`schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py`

Functional CI markers:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

## Runtime Contract — v1.2 Remains Accepted and Unchanged

Current runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Current output contract version:

`1.2.0`

Current versioned contract:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

Historical immutable contract:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Reviewed v1.1 blob SHA:

`33c829116eea0b568cfe16c664ffbeee9d00e013`

For `PROPERTY_TYPE_FORMAT_UNEXPECTED`, the accepted runtime contract remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

Other stop reasons and successful/inconclusive outcomes retain:

`control_disposition = null`

Source continuation remains `false`.

## Proposed Future Real-Source Boundary

The proposal is explicitly:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

It does not precommit or infer a real-source outcome. It proposes only a future, separately authorized bounded verification using the existing reviewed v1.2 runner and unchanged sample/transport caps.

Fresh authorization remains required and not granted:

- execution approval status: `REQUIRED_NOT_GRANTED`;
- execution approval ref: `null`;
- transient-row privacy approval status: `REQUIRED_NOT_GRANTED`;
- transient-row privacy approval ref: `null`;
- network workflow creation authorized: `false`;
- real execution authorized: `false`;
- future approvals must be single-use.

All historical execution/privacy approvals remain consumed and non-reusable.

## Bounded Caps / Validation Boundary

The proposal preserves the existing bounded plan:

- max 4 canonical members;
- max 4 rows per member;
- max 16 rows total;
- max 1 HEAD request;
- max 4 range requests;
- max 5 HTTP requests total;
- max 131072 bytes per range;
- max 524288 source response-body bytes total;
- max 262144 transient uncompressed bytes per member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes per logical record;
- no additional range;
- no full-body fallback;
- no automatic widening.

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is proposed or authorized.

## Privacy / Persistence Boundary

The proposal requires fresh transient-row privacy approval before any future transient full-row observation.

The proposed future execution remains memory-only with immediate disposal and zero retention. It allows no raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact-length persistence, record values in logs, real-row quarantine or row-specific human inspection.

The v1.2 `control_disposition` remains limited to non-value-bearing:

- `status_code`;
- `reason_code`.

No privacy expansion is proposed.

## Preparation Safety State

This proposal-preparation task did not:

- access `claimit.ca.gov`;
- access a new authority source;
- perform any network request or real-source execution;
- access source-body bytes or a real row/field;
- reconstruct or infer the hidden `PROPERTY_TYPE` value;
- modify the reviewed v1.2 runtime or execution schema;
- modify source policy or registry;
- create the one-shot network workflow;
- create or grant an execution/privacy approval token;
- enable source continuation;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.

## Governance State

- D-008 accepted as design: `true`;
- v1.2 implementation completed: `true`;
- v1.2 implementation human-reviewed: `true`;
- real-source execution proposal prepared: `true`;
- proposal contract validation: `PASS`;
- real-source execution proposal human-reviewed: `false`;
- fresh execution approval granted: `false`;
- fresh privacy approval granted: `false`;
- network workflow creation authorized: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged: `true`;
- regex/normalization unchanged: `true`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

That gate reviews only the proposal design. It must not access the source, grant approval tokens, create the one-shot workflow, authorize execution, perform real-source execution or widen runtime/privacy/continuation/source/registry/downstream boundaries.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
