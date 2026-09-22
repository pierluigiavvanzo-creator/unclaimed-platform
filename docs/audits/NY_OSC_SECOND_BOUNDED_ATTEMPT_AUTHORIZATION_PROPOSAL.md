# NY OSC Second Bounded Attempt — Authorization Proposal

Date: 2026-09-18

Status: `PENDING_HUMAN_AUTHORIZATION_AND_FRESH_PREFLIGHT`

## Why a second attempt is proposed

The first authorized execution was consumed and stopped fail-closed on:

`PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`

The raw ZIP was logically deleted and no owner values were persisted or returned.

## Offline remediation evidence

Checkpoint:

`151f3a2f16c74f604fa72cc1284b2f9cd2e73f52`

CI:

`35363685148 — SUCCESS`

Synthetic-only remediation now handles:

- UTF-8 BOM on the first documented header field;
- one matching pair of quotes around documented header fields;
- harmless outer ASCII whitespace;
- one matching pair of quotes around Property Type Code.

The normalized Property Type Code must still be strict ASCII alphanumeric. Internal ambiguity such as `IN 03` remains blocked.

No real file was used to build or test the remediation.

## Proposed second-attempt bounds

No safety bound is increased:

- compressed max: `450,000,000` bytes;
- uncompressed max: `2,000,000,000` bytes;
- archive members max: `1`;
- downloads max: `1`;
- retries max: `0`.

## Fresh preflight

Immediately before any second download, the remote listing must be checked again.

If unchanged, the expected listing remains:

- `FINDERS.zip`;
- `390.51 MB`;
- `9/16/2026, 1:33:31 PM`.

Any difference stops the execution and requires proposal refresh.

## Human approvals required

A fresh second attempt requires both new single-use approvals:

`APPROVO NY OSC SECOND TRANSIENT LOCAL FILE BOUNDED ONCE`

and

`APPROVO NY OSC OWNER NAME FILE SECOND BOUNDED TRANSIENT PII ATTEMPT ONCE`

Preparing this proposal does not grant either approval.

## Not authorized

No source activation, production classification, identity resolution, beneficiary matching, outreach, fee agreement, representation or claim activity is authorized.
