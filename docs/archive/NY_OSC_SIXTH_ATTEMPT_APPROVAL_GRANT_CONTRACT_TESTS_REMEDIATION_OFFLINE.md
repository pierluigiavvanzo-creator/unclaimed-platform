# NY OSC Sixth Attempt — Approval Grant Contract Tests Remediation Offline

State: `OFFLINE_REMEDIATION_PREPARED / REVIEW_PENDING`

## Trigger

Grant branch:
`ny-osc-sixth-approval-grants`

Grant branch HEAD:
`e8ad3068474ad6a71cb3e1b049889c760c8d866b`

Failed CI:
`35571712994`

Contract result:
`365 passed / 2 failed`

The two failures were caused by tests that treated the repository approval
artifacts themselves as permanently `NOT_GRANTED`.

The approval artifacts legitimately transitioned on the isolated branch to
`GRANTED_NOT_CONSUMED`, so those tests became state-stale.

## Remediation

Only:
`tests/contract/test_ny_osc_sixth_attempt_approvals.py`

is proposed for modification.

The remediated test design separates:

1. current repository artifact validation from
2. lifecycle-state contract fixtures.

Current approval artifacts are validated against their schemas without assuming
a particular lifecycle state.

Synthetic fixtures explicitly construct:
- `NOT_GRANTED`
- `GRANTED_NOT_CONSUMED`
- `CONSUMED_SINGLE_USE_NON_REUSABLE`

This preserves all previous negative/positive contract coverage while preventing
future valid lifecycle transitions from breaking tests solely because the
repository artifact moved state.

## Preserved checks

The remediation continues to verify:

- `NOT_GRANTED` is fail-closed;
- `GRANTED_NOT_CONSUMED` validates;
- runtime authorization 1.1 can be built from a valid granted pair;
- quote mode remains `LINE_LOCAL_ARBITRATION`;
- consumed approvals validate as historical records but cannot build runtime authorization;
- malformed non-Git runner checkpoint is rejected;
- grant data is rejected in a synthetic `NOT_GRANTED` state;
- consumption data is rejected in a synthetic `NOT_GRANTED` state.

## Explicit non-scope

No approval artifact modification.
No runner modification.
No schema modification.
No preflight receipt modification.
No repository mutation.
No commit/push/merge.
No OSC access.
No fresh preflight.
No download.
No PII processing.
No sixth execution.

## Local validation

Python syntax compilation: PASS.

Authoritative behavioral validation still requires GitHub CI after a separate
commit-and-CI authorization.

## Next gate

`HUMAN_REVIEW_NY_OSC_SIXTH_ATTEMPT_APPROVAL_GRANT_CONTRACT_TESTS_REMEDIATION_OFFLINE`
