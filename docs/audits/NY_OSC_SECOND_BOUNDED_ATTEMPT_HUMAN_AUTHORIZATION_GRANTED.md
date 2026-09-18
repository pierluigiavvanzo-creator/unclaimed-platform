# NY OSC Second Bounded Attempt — Human Authorization Granted

Date: 2026-09-18

Status: `GRANTED_NOT_CONSUMED_PENDING_FRESH_PREFLIGHT`

The Product Owner granted both required second-attempt approvals:

`APPROVO NY OSC SECOND TRANSIENT LOCAL FILE BOUNDED ONCE`

`APPROVO NY OSC OWNER NAME FILE SECOND BOUNDED TRANSIENT PII ATTEMPT ONCE`

Both approvals are:

- single-use;
- non-reusable;
- zero-retry.

The first-attempt approvals remain consumed and are not reused.

## Bounds

No bound is increased:

- compressed max: `450,000,000` bytes;
- uncompressed max: `2,000,000,000` bytes;
- archive members max: `1`;
- download count max: `1`;
- retry count max: `0`.

## Remediation basis

Checkpoint:

`151f3a2f16c74f604fa72cc1284b2f9cd2e73f52`

CI:

`35363685148 — SUCCESS`

## Mandatory fresh preflight

Before the single second download, verify the secure-transfer listing again.

If unchanged it should still show:

- `FINDERS.zip`;
- `390.51 MB`;
- `9/16/2026, 1:33:31 PM`.

Any drift stops before download.

No source activation, identity resolution, beneficiary matching, outreach, fee agreement, representation or claim activity is authorized.
