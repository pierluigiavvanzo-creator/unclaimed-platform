# NY OSC Fourth Bounded Attempt — Offline Proposal

Date: 2026-09-19

## Status

`PROPOSED_NOT_AUTHORIZED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

This document proposes a possible fourth bounded schema-discovery attempt. It is not an
execution authorization and does not create a runner or approval artifacts.

## Preceding attempt

The third attempt executed once and stopped fail-closed with
`MALFORMED_QUOTED_RECORD`. Both third-attempt approvals are consumed, non-reusable and
authorize zero retry. The raw ZIP was logically deleted; no owner values were returned or
persisted.

## Verified remediation

The fixed-chunk byte-level streaming parser is integrated at:

`3e58eeb27b47ca89d01f6b45159c8a01bef94bf0`

Verification CI:

`35425632178 — SUCCESS`

Verified synthetic behavior includes LF/CRLF inside quoted fields, quoted pipes, doubled quotes,
following records, EOF-open-quote failure, invalid field count, invalid Property Type Code and
64 KiB chunk-boundary cases. The remediation used no real owner file.

## Proposed bounds

No execution limit is widened:

- attempt number: 4;
- downloads maximum: 1;
- retries maximum: 0;
- compressed bytes maximum: 450,000,000;
- uncompressed bytes maximum: 2,000,000,000;
- archive members maximum: 1;
- text members required exactly: 1;
- documented fields expected: 14;
- parser chunk size: 65,536 bytes;
- automatic widening: forbidden;
- automatic retry: forbidden.

A fresh exact listing preflight remains mandatory immediately before any future execution.
Listing drift must stop before download and require a refreshed proposal.

## Privacy scope

The proposed execution would retain the existing transient-local exception only:

- dedicated OS temporary directory;
- immediate logical deletion;
- no durable raw persistence;
- no repository persistence, cloud sync or chat upload;
- no owner-row persistence;
- no owner-field decoding, buffering or logging;
- no row-specific human inspection;
- non-PII aggregate metadata only;
- physical secure erasure not claimed.

## Required future gates

Two new explicit, single-use and non-reusable approvals would be required:

- `APPROVO NY OSC FOURTH TRANSIENT LOCAL FILE BOUNDED ONCE`
- `APPROVO NY OSC OWNER NAME FILE FOURTH BOUNDED TRANSIENT PII ATTEMPT ONCE`

Both remain `NOT_GRANTED`.

Before they could be considered, a fourth-attempt runner and approval templates would need to
be prepared offline and independently verified. The third runner and all prior approvals may
not be reused.

## Activity performed

This proposal involved no NY OSC network access, remote preflight, download, owner-file
opening or owner-PII processing.
