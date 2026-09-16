# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal`

Created from human-reviewed v1.2 checkpoint:

`7b6397f0e89d8ee1640be2eea4f8651f6b74478c`

Base CI:

`35105522139` — **SUCCESS**

## Completed Action

Completed:

`PREPARE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL`

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

Functional proposal checkpoint:

`19c395a6f89dbec1941566366274070db98cacd0`

Functional CI:

`35106612846` — **SUCCESS**

CI markers:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

## Prepared Artifacts

- audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL.md`;
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`;
- proposal schema: `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`;
- contract test: `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py`.

## Canonical Read Order

Before any new change read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then read the four proposal artifacts above, followed as needed by:

- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_IMPLEMENTATION_REVIEW.md`;
- `scripts/ca_sco_property_type_semantic_verification.py`;
- `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
- historical v1.1 execution schema/evidence.

## Governing State

Decision:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Design:

`WHOLE_SOURCE_STOP`

Implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

Implementation review result:

`PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Current runner output contract remains `1.2.0`; proposal preparation did not modify runtime or the v1.2 execution schema.

Exact accepted mismatch behavior remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation after trigger = `false`.

Other stops and non-stopped outcomes retain `control_disposition = null`.

## Fresh Authorization State

All historical execution/privacy approvals remain consumed and non-reusable.

The proposal requires, but does not grant:

- fresh execution approval;
- fresh transient-row privacy approval;
- single-use authorization;
- later authorization for the one-shot workflow and real execution.

Current proposal state:

- execution approval: `REQUIRED_NOT_GRANTED`;
- execution approval ref: `null`;
- privacy approval: `REQUIRED_NOT_GRANTED`;
- privacy approval ref: `null`;
- workflow creation authorized: `false`;
- real-source execution authorized: `false`.

If the proposal later passes review, a separate authorization gate is defined as:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

That gate has not occurred.

## Frozen Boundaries

The proposal keeps existing sample/transport limits: 4 canonical members, max 4 rows/member and 16 total, max 1 HEAD + 4 range requests + 5 HTTP requests, max 524288 response bytes total, no full-body fallback, no additional range and no automatic widening.

Regex remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, parser/projector change or regex relaxation is proposed.

Privacy remains memory-only, immediate-disposal, zero-retention. No real row/value persistence, row quarantine or row-specific inspection is proposed. `control_disposition` remains limited to `status_code` and `reason_code`.

The proposal does not precommit, infer or predict the real-source outcome.

## Proposal Preparation Safety State

This task performed no request to the CA SCO source or any new authority source, no source-body or real-row access, no real execution, no workflow creation, no approval granting, no runtime/policy/registry modification, no privacy expansion, no continuation change and no downstream work.

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain `0`; semantic compatibility remains unresolved; production classification and downstream identity/genealogy/matching/outreach/claim gates remain closed.

`DECISIONS.md` is intentionally unchanged because no new accepted architecture/governance decision was introduced.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

This review may accept or reject only the proposal design. It must not grant fresh approvals, create the one-shot workflow, authorize execution or perform source access.

## Do Not Do During the Next Review

Do not access the real source or new authorities; do not infer the hidden source value; do not modify runtime/schema/parser/projector/regex/normalization; do not reuse or create approvals; do not create the network workflow; do not widen privacy or continuation; do not activate source/registry/production classification; do not begin downstream identity, genealogy, matching, outreach or claim work.

## Restart Instruction

1. verify remote HEAD of the current proposal branch;
2. verify latest CI for that exact HEAD;
3. read the five canonical files in order;
4. read proposal audit/proposal/schema/test;
5. execute only the `SINGLE NEXT ACTION`;
6. keep proposal review separate from authorization and real-source execution.
