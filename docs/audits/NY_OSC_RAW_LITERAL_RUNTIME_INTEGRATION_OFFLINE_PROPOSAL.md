# NY OSC RAW-Literal Runtime Integration — Offline Proposal

Date: 2026-09-21

Classification: `A — Product Critical / Runtime Integration Proposal`

Status:

`PROPOSED_NOT_IMPLEMENTED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

## Requested action

`PREPARE_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_OFFLINE_PROPOSAL`

## Baseline

Reviewed parser-mode branch:

`ny-osc-documented-width-raw-literal-policy-mode-offline`

Reviewed parser-mode HEAD:

`fc162aa0d938ec7a5560d115631bcc762694e244`

CI:

`35594727577 — SUCCESS`

Human review result:

`HUMAN_REVIEW_NY_OSC_DOCUMENTED_WIDTH_RAW_LITERAL_POLICY_MODE_OFFLINE = PASS`

Active Product Owner policy:

`D-011 — NY OSC quote interpretation statistical fallback policy`

Implemented and reviewed parser mode:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`

Official OSC quote semantics remain unknown. RAW-literal remains a Product Owner policy,
not a claim about source truth.

## Why a new runtime version is required

The currently integrated sixth-attempt runtime is deliberately bound to line-local
arbitration:

- authorization contract v1.1 requires `LINE_LOCAL_ARBITRATION`;
- result contract v1.2 records `LINE_LOCAL_ARBITRATION`;
- runtime function `execute_transient_local_file_discovery_v1_2` uses that authorization;
- Gate 6 requires `LINE_LOCAL_ARBITRATION`;
- sixth approvals are consumed and non-reusable.

Retargeting any of those historical artifacts would destroy provenance and could imply reuse
of consumed authorization. This proposal therefore uses version-additive integration.

## Proposed integration architecture

### Historical runtime — protected

Keep unchanged:

- `ny_transient_local_execution_authorization_v1_1.schema.json`;
- `ny_transient_local_execution_result_v1_2.schema.json`;
- `execute_transient_local_file_discovery_v1_2`;
- `scripts/ny_osc_gate6_transient_local.ps1`.

No historical contract is widened to include the new mode.

### Offline authorization contract v1.2 — synthetic only

Proposed future file:

`schemas/agents/ny_transient_local_execution_authorization_v1_2.schema.json`

Proposed contract version:

`1.2.0`

Required mode:

`SYNTHETIC_TEST` only.

Required parser mode:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`.

The existing byte/member/privacy/deletion bounds remain structurally equivalent to v1.1.

`AUTHORIZED_REAL_ONCE` is intentionally excluded from this first integration contract.
Therefore implementing the offline candidate cannot itself create a real execution path.

### Offline result contract v1.3

Proposed future file:

`schemas/agents/ny_transient_local_execution_result_v1_3.schema.json`

Proposed version:

`1.3.0`

Required parser-mode provenance:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`

The envelope keeps `quote_dialect_diagnostic` as a required field for compatibility but
requires it to be `null`. The RAW-literal parser does not perform quote arbitration.

The existing structural diagnostic v1.0 remains the diagnostic for
`UNEXPECTED_DATA_FIELD_COUNT`.

## Proposed reason-code surface

Allowed:

- `LOCAL_ARCHIVE_EXCEEDS_DOWNLOAD_CAP`;
- `LOCAL_ARCHIVE_READ_EXCEEDS_DOWNLOAD_CAP`;
- `ARCHIVE_EXCEEDS_DOWNLOAD_CAP`;
- `NOT_A_ZIP_ARCHIVE`;
- `ARCHIVE_HAS_NO_FILES`;
- `ARCHIVE_MEMBER_COUNT_EXCEEDS_CAP`;
- `AMBIGUOUS_TEXT_MEMBER_LAYOUT`;
- `UNCOMPRESSED_TEXT_EXCEEDS_CAP`;
- `UNEXPECTED_DATA_FIELD_COUNT`;
- `PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`;
- `TEXT_MEMBER_EMPTY`;
- `DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED`.

Explicitly forbidden as unreachable in RAW-literal mode:

- `QUOTE_DIALECT_AMBIGUOUS`;
- `MALFORMED_QUOTED_RECORD`.

If either quote-specific reason appears, or an unknown reason is emitted, the future runtime
contract must fail closed rather than silently accepting a widened result.

## Proposed runtime function

Future function:

`execute_transient_local_file_discovery_v1_3`

Input:

`NyTransientLocalExecutionAuthorizationV1_2`

Output:

`NyTransientLocalExecutionResultV1_3`

The future implementation may reuse:

- dedicated OS-temp path validation;
- byte-cap checks before and during read;
- immediate logical deletion in `finally`;
- schema-discovery authorization construction;
- structural diagnostic capture;
- privacy guarantees.

It must call schema discovery with exactly:

`quote_dialect_mode="DOCUMENTED_WIDTH_RAW_LITERAL_POLICY"`

or the equivalent value bound by the v1.2 synthetic authorization.

## Explicit non-wiring

The offline integration candidate must not:

- alter the current CLI entry point;
- modify Gate 6;
- create Gate 7;
- create a real authorization builder;
- accept `AUTHORIZED_REAL_ONCE`;
- parse sixth consumed approvals;
- create new approval artifacts;
- perform listing preflight;
- access OSC;
- download or open the real file.

This makes the proposed next implementation synthetic by construction.

## Synthetic acceptance matrix

The future implementation must verify:

1. sixth-shaped RAW-14 input reaches `DISCOVERED`;
2. RAW-15 quoted-pipe input blocks with `UNEXPECTED_DATA_FIELD_COUNT`;
3. RAW-13 input blocks with `UNEXPECTED_DATA_FIELD_COUNT`;
4. local archive cap blocks before schema discovery;
5. local file is logically deleted in all post-path-validation execution outcomes;
6. no raw path or owner value is returned;
7. quote-dialect diagnostic is always null;
8. real execution mode is rejected by the offline authorization contract.

Contract tests must also prove historical v1.1/v1.2 and Gate 6 remain line-local and do not
contain the new mode.

## Future real activation boundary

A later real attempt requires all of the following as separate gates:

1. review PASS for this proposal;
2. implementation and human review of the synthetic runtime integration;
3. separate seventh-attempt proposal;
4. fresh transient-local approval;
5. fresh transient-PII approval;
6. separately authorized fresh listing preflight;
7. explicit seventh execution authorization.

This proposal does not grant any of them.

## Repository artifacts

- `sources/proposals/ny_osc_raw_literal_runtime_integration_offline_proposal.v1.json`;
- `schemas/common/ny_osc_raw_literal_runtime_integration_offline_proposal.schema.json`;
- `tests/contract/test_ny_osc_raw_literal_runtime_integration_offline_proposal.py`;
- this audit.

No runtime schema v1.2/v1.3 or runtime implementation is created in this task.

## Next gate

`HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_OFFLINE_PROPOSAL`
