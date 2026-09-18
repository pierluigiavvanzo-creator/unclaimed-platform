# NY OSC Third Attempt Runner — Offline Technical Preparation

Date: 2026-09-18

Classification: `A — Product Critical / Offline Safety Implementation`

Status: `VERIFIED_OFFLINE / CI_SUCCESS / APPROVALS_NOT_GRANTED / ZERO_SOURCE_ACCESS`

## Authorization boundary

The Product Owner authorized preparation of the runner and contracts only and explicitly did
not authorize a download, remote preflight, or source access.

No NY OSC request, portal interaction, listing check, download, owner-file read, or PII
processing occurred.

## Reuse decision

The existing transient-local execution bridge and schema-discovery harness are reused. No new
runtime dependency is introduced.

The shared authorization builder is hardened to:

- bind local and transient-PII artifacts to the same attempt number;
- optionally require an exact expected attempt number;
- require distinct non-empty approval references;
- enforce single-download and zero-retry bounds;
- require matching compressed-byte caps across the two approvals.

The consumed second-attempt runner now passes expected attempt number `2`. The new runner
passes expected attempt number `3`.

## New approval templates

Two versioned artifacts exist with status `NOT_GRANTED`:

- transient-local retention;
- transient owner-PII processing.

Their human-authorization value, grant date, execution reference, verified runner checkpoint,
and runner CI reference are null. The contracts require those values only after a later
explicit grant and require `runner_ci_conclusion = SUCCESS`.

## Fail-closed ordering

The third-attempt PowerShell runner checks before creating a temp directory or showing a
download prompt:

1. both artifacts exist;
2. both have `GRANTED_NOT_CONSUMED`;
3. both bind to attempt `3`;
4. both contain the exact separate approval phrases;
5. both are single-use and non-reusable;
6. neither permits retries;
7. both reference successful runner CI.

The script contains no HTTP or download client. A later authorized human browser step would
remain subject to a fresh listing comparison and exact-match-or-stop behavior.

## Unchanged bounds

- one download maximum;
- zero retries;
- compressed bytes maximum `450,000,000`;
- uncompressed bytes maximum `2,000,000,000`;
- one archive member maximum;
- exactly one text member;
- 14 documented fields;
- no automatic widening or retry.

## Verification

- candidate checkpoint: `5aa606f9f79dc05508628d8a97f514cce7e4f770`;
- CI run: `35384965991 — SUCCESS`;
- Ruff: pass;
- mypy: pass;
- repository tests: pass;
- Streamlit candidate job: pass.

## Safety state after this change

The runner is technically present but not runnable because both approval templates are
`NOT_GRANTED`. No real attempt is authorized by code, documentation, this audit, or the
instruction that requested offline preparation.
