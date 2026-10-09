# NY OSC Fifth Bounded Attempt — Offline Proposal

Date: 2026-09-19

## Status

`PROPOSED_NOT_AUTHORIZED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

This document proposes a possible fifth bounded schema-discovery attempt. It is not an
execution authorization and does not create a runner, approval artifacts, remote preflight,
download or owner-file access.

## Canonical baseline

Branch: `mvp1-ny-second-attempt-approved-ready-execution`

Checkpoint: `326b2ba91f30adb80faf816d85a5d707fde4eaee`

PR #13 canonical-state reconciliation CI: `35459156574 — SUCCESS`.

## Preceding attempt

The fourth attempt executed once and stopped fail-closed with
`BLOCKED / UNEXPECTED_DATA_FIELD_COUNT`.

Persisted non-PII evidence: 14 documented fields, 13 observed structural fields, 213,454
complete records before block, 213,454 ASCII-valid Property Type Code records, 409,477,526
archive bytes, 1,939,569,781 selected-member bytes, logical raw-ZIP deletion, no owner values
returned or persisted.

Both fourth-attempt approvals are consumed, single-use, non-reusable and authorize zero retry.

The fourth receipt predates the structural-diagnostic execution bridge, so it contains no
raw/structural/suppressed-pipe diagnostic. That is the evidence gap the fifth proposal targets.

## Verified diagnostic capability

PR #12 merge checkpoint:
`dc603d68ff6aeb234c2ad793b85fa1bb2f4805c8`

Final verified PR CI:
`35446925652 — SUCCESS`

Required future execution contracts:

- transient-local execution result `v1.1.0`;
- structural diagnostic result `v1.0.0`.

The remediation was verified with synthetic fixtures only and used no real owner file.

## Diagnostic objective

Primary question:

`RAW_DELIMITER_SHORTAGE_VS_QUOTE_SUPPRESSED_DELIMITER`

If a future separately authorized fifth attempt again stops on
`UNEXPECTED_DATA_FIELD_COUNT`, the execution receipt must contain the sanitized structural
diagnostic.

The four classifications remain descriptive evidence only. None authorizes automatic row
repair, row skip, parser widening, source acceptance or retry.

## Proposed bounds

No execution limit is widened:

- attempt 5;
- downloads max 1;
- retries max 0;
- compressed bytes max 450,000,000;
- uncompressed bytes max 2,000,000,000;
- archive members max 1;
- exactly one text member;
- delimiter `|`;
- documented fields 14;
- parser chunk 65,536 bytes;
- execution receipt v1.1.0;
- structural diagnostic v1.0.0 on field-count block;
- automatic widening forbidden;
- automatic retry forbidden.

A fresh exact listing preflight remains mandatory immediately before any future execution.
Listing drift stops before download and requires proposal refresh.

## Privacy scope

The existing transient-local exception is preserved. No durable raw persistence, repository
raw persistence, cloud sync, chat upload, owner-row persistence, owner-field
decoding/buffering/logging or row-specific human inspection is allowed. Only derived non-PII
schema metadata and structural diagnostics may persist. Physical secure erasure is not claimed.

## Required future gates

Two new explicit, single-use, non-reusable approvals would be required:

- `APPROVO NY OSC FIFTH TRANSIENT LOCAL FILE BOUNDED ONCE`
- `APPROVO NY OSC OWNER NAME FILE FIFTH BOUNDED TRANSIENT PII ATTEMPT ONCE`

Both remain `NOT_GRANTED`.

A fifth-attempt runner and attempt-5 approval templates must first be prepared offline and
independently verified. The fourth runner and fourth approvals may not be reused. The shared
schema-discovery parser and verified v1.1 execution bridge may be reused.

Fresh listing preflight and one-time execution authorization remain later, separate human gates.

## Activity performed

No NY OSC network access, remote preflight, download, owner-file opening or owner-PII
processing occurred.

## Next action

`HUMAN_REVIEW_NY_OSC_FIFTH_BOUNDED_ATTEMPT_PROPOSAL`
