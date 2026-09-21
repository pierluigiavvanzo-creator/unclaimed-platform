# NY OSC Seventh Bounded Attempt — Offline Proposal

Date: 2026-09-21

Classification: `A — Product Critical / Real-Source Attempt Proposal`

Status:

`PROPOSED_NOT_AUTHORIZED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

## Requested action

`PREPARE_NY_OSC_SEVENTH_ATTEMPT_OFFLINE_PROPOSAL`

## Canonical baseline

Branch:

`ny-osc-raw-literal-runtime-integration-synthetic-offline`

HEAD:

`c03f2af4a0fc97232ac5be0abcfe3dd6ae47340a`

CI:

`35642325234 — SUCCESS`

The immediately preceding human review returned:

`HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_SYNTHETIC_OFFLINE = PASS`

Verified synthetic package:

- authorization v1.2;
- result v1.3;
- runtime `execute_transient_local_file_discovery_v1_3`;
- parser mode `DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`;
- `SYNTHETIC_TEST` only;
- no CLI;
- no real authorization builder;
- no Gate 7.

## Why attempt 7 cannot reuse runtime v1.3 directly

The reviewed v1.3 package is deliberately synthetic-only.

Authorization v1.2 accepts only:

`SYNTHETIC_TEST`

and explicitly does not admit:

`AUTHORIZED_REAL_ONCE`.

The implementation review PASS does not authorize retargeting or widening that contract.

Therefore the seventh proposal is version-additive and requires a separate real-capable
runtime package before any seventh approval, listing preflight or execution.

## Proposed real runtime package

Before any seventh approval is grantable, a separately implemented and human-reviewed package
must provide:

- authorization contract v1.3;
- result contract v1.4;
- runtime `execute_transient_local_file_discovery_v1_4`;
- real authorization builder `build_real_execution_authorization_v1_3`;
- Gate 7 runner.

Authorization v1.3 is proposed to accept exactly:

`AUTHORIZED_REAL_ONCE`

for:

`attempt_number = 7`

and:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`.

It must not widen or mutate the synthetic v1.2 contract.

Result v1.4 is proposed to bind:

- execution mode `AUTHORIZED_REAL_ONCE`;
- attempt number 7;
- parser provenance `DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`;
- quote-dialect diagnostic required null;
- structural diagnostic required for unexpected field count;
- unknown reason codes fail closed.

No part of that real package is implemented in this task.

## Sixth-attempt evidence retained

The sixth attempt remains historical evidence:

- status: `BLOCKED`;
- reason: `QUOTE_DIALECT_AMBIGUOUS`;
- completed records before stop: 165,438;
- RAW fields at blocked record: 14;
- quote-aware fields: 6;
- RAW pipes: 13;
- quote-aware structural pipes: 5;
- quote bytes: 1;
- quote open events: 1;
- quote close events: 0;
- ended inside quote: true.

Archive evidence:

- compressed bytes: 409,477,526;
- archive members: 1;
- selected member uncompressed bytes: 1,939,569,781.

Both sixth approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

with retry unauthorized.

Neither Gate 6 nor sixth approvals may be reused for attempt 7.

## Policy basis

D-011 remains active.

The current Product Owner fallback is:

`RAW_PIPE_WITH_DOUBLE_QUOTE_LITERAL`

implemented as:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`.

This remains a Product Owner fallback, not a claim that OSC officially documents double quotes
as literal characters.

The proposed seventh objective is therefore narrowly factual:

> Does the real current owner file validate the documented 14-field layout under the reviewed
> RAW-literal policy?

Success is:

`DISCOVERED / DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED`.

Any unexpected width, Property Type Code shape failure or other non-success condition stops
fail-closed. Quote-specific reasons in a RAW-literal real runtime are integration errors.

## Proposed bounds

The proposal preserves the already-tested bounded envelope:

- attempt: 7;
- downloads maximum: 1;
- retries: 0;
- compressed bytes maximum: 450,000,000;
- uncompressed bytes maximum: 2,000,000,000;
- archive members maximum: 1;
- exactly one text member;
- delimiter: `|`;
- documented fields: 14;
- parser chunk: 65,536 bytes;
- no widening;
- no automatic retry.

The proposed real package versions are:

- authorization v1.3;
- result v1.4;
- structural diagnostic v1.0;
- RAW-literal parser mode.

## Privacy scope

The proposed seventh execution preserves:

- transient local file only;
- immediate logical deletion;
- no durable raw persistence;
- no repository persistence;
- no cloud sync;
- no chat upload;
- transient owner PII only in bounded memory;
- no owner-row persistence;
- no owner-field decoding or buffering;
- no owner-field logging;
- no row-specific human inspection;
- only non-PII schema metadata and structural diagnostics may persist;
- no physical secure erasure claim.

Quote-dialect diagnostics are not persistable because the RAW-literal runtime must not emit them.

## Fresh listing preflight

A new preflight remains mandatory immediately before any execution.

This proposal performs no preflight and grants no remote access.

The last retained listing is historical comparison evidence only:

- `FINDERS.zip`;
- `390.51 MB`;
- `9/16/2026, 1:33:31 PM`;
- sixth preflight performed at `2026-09-21T08:06:57Z`.

A seventh preflight must be separately authorized, fresh within 900 seconds, and return an
exact match. Any drift stops before download and requires proposal refresh/review.

## Human gate sequence

The proposal defines, but does not grant:

1. human review of this seventh proposal;
2. implementation + review of the real-capable seventh runtime package;
3. fresh seventh transient-local approval;
4. fresh seventh transient-PII approval;
5. fresh seventh listing-preflight authorization;
6. explicit single-use seventh execution authorization.

Approval phrases are proposal metadata only and remain `NOT_GRANTED`.

## Explicitly not created

This task does not create:

- authorization v1.3 runtime schema;
- result v1.4 runtime schema;
- runtime v1.4;
- real authorization builder;
- Gate 7 runner;
- seventh approval schemas;
- seventh approval artifacts;
- seventh preflight receipt;
- seventh execution receipt.

## Explicitly not authorized

No OSC access.
No preflight.
No download.
No real owner-PII processing.
No seventh execution.
No sixth retry.
No source activation.
No downstream identity resolution, beneficiary matching, outreach, contracting, representation
or claim activity.

## Artifacts

- `sources/proposals/ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json`;
- `schemas/common/ny_osc_seventh_attempt_authorization_proposal.schema.json`;
- `tests/contract/test_ny_osc_seventh_attempt_offline_proposal.py`;
- this audit.

## Next gate

`HUMAN_REVIEW_NY_OSC_SEVENTH_ATTEMPT_OFFLINE_PROPOSAL`
