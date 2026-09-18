# NY OSC Second Schema Discovery Rerun Proposal

Date: 2026-09-18

Status: `PENDING_HUMAN_AUTHORIZATION`

## Why a new proposal is required

The first real bounded schema-discovery attempt stopped fail-closed with:

`PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`

That Gate 2 and the transient-local-file approval were single-use, non-reusable and zero-retry, so both are consumed.

A rerun therefore requires fresh human authorization.

## Remediation verified

Checkpoint:

`57c881aec082ebb2b7c187f7cb8e9d2a443e5e13`

CI:

`35362395868` — SUCCESS.

The remediation:

- recognizes the documented header with or without UTF-8 BOM;
- preserves fail-closed 14-field layout validation;
- treats Property Type Code shape as aggregate diagnostic only;
- defers semantic code validation;
- continues to return no owner values.

## Fresh preflight

Before any second download, the portal must still show:

- `FINDERS.zip`;
- `390.51 MB`;
- `9/16/2026, 1:33:31 PM`.

Any drift stops before download and requires fresh review.

## Proposed bounds

- compressed max: `450,000,000` bytes;
- uncompressed max: `2,000,000,000` bytes;
- archive members max: `1`;
- downloads max: `1`;
- retries max: `0`.

## Proposed fresh approvals

Local transient file:

`APPROVO NY OSC SECOND TRANSIENT LOCAL FILE BOUNDED ONCE`

Gate 2 rerun:

`APPROVO NY OSC SECOND SCHEMA DISCOVERY RERUN TRANSIENT PII BOUNDED ONCE`

Neither approval is granted by proposal preparation.

## Scope boundary

No source activation, production classification, beneficiary matching, identity resolution, outreach, fee agreement, representation or claim activity is included.
