# NY OSC Sixth Attempt — Gate 6 Review Remediation Offline

Date: 2026-09-20

Classification: `A — Product Critical / Review Remediation`

## Requested action

`REMEDIATE_NY_OSC_SIXTH_ATTEMPT_RUNNER_AND_APPROVAL_CONTRACTS_OFFLINE`

## Canonical source of truth

- canonical branch: `mvp1-ny-second-attempt-approved-ready-execution`
- canonical HEAD: `fb9226392939d6e2a44129eae63ae7a70c51b098`
- proposal checkpoint: `ac5a84a9523c5e99c79f41d0203f349e41be56c7`
- proposal CI: `35531762748 — SUCCESS`

## Finding 1 remediation — runner self-binding

The previous candidate required approval records to agree on a runner checkpoint,
but it did not prove that the executing Gate 6 package matched that checkpoint.

The remediated approval schemas now accept a non-null runner checkpoint only when
it is a lower-case 40-character Git SHA.

Before creating any temp directory, Gate 6 now:

1. requires both approvals to carry the same granted runner checkpoint;
2. confirms the checkpoint exists locally as a Git commit;
3. resolves the expected Git blob for every protected Gate 6 path at that commit;
4. hashes the working-tree version of each protected path;
5. blocks if any blob differs.

Protected paths include the Gate 6 runner, proposal and proposal schema, both
sixth approval schemas, fresh-preflight receipt schema, line-local runtime and
schema-discovery modules, and all runtime/diagnostic machine contracts.

Approval artifacts themselves are intentionally not protected by this immutable
package check because they must transition from `NOT_GRANTED` to
`GRANTED_NOT_CONSUMED` in a later separately authorized step.

The mutable preflight receipt artifact is also excluded because it must transition
from `NOT_PERFORMED` to the actual source-facing result.

## Finding 2 remediation — machine-checkable fresh preflight

A new non-PII contract is added:

`ny_osc_sixth_fresh_listing_preflight_receipt.schema.json`

and an initial evidence artifact is committed as:

`NOT_PERFORMED`

The receipt is bound to attempt 6, the canonical proposal ref/checkpoint/CI and,
when performed, the exact runner checkpoint.

A valid `EXACT_MATCH` receipt requires:

- a non-empty separate preflight authorization reference;
- UTC performance timestamp;
- freshness window of 900 seconds;
- exact observed name `FINDERS.zip`;
- exact observed size display `390.51 MB`;
- exact observed last-modified display `9/16/2026, 1:33:31 PM`;
- no download performed;
- no Owner Name File opened;
- no owner PII processed;
- explicit `contains_owner_pii = false`.

Gate 6 refuses to create a temp directory unless the receipt is `EXACT_MATCH`,
is bound to the same runner checkpoint and proposal, and is no more than
900 seconds old.

`DRIFTED` is a valid evidence state but can never pass Gate 6.

The 900-second window is an implementation bound introduced
by this remediation to make the proposal's "fresh/immediately before" requirement
machine-checkable. It does not authorize source access.

## Finding 3 remediation — complete approval state tests

Contract tests now cover:

- `NOT_GRANTED` positive state;
- `GRANTED_NOT_CONSUMED` positive state;
- successful construction of runtime authorization 1.1 from a granted pair;
- `CONSUMED_SINGLE_USE_NON_REUSABLE` positive schema state;
- consumed approvals rejected by the runtime builder;
- malformed runner checkpoint rejected;
- grant/consumption data rejected while `NOT_GRANTED`.

Preflight tests cover:

- initial `NOT_PERFORMED`;
- valid `EXACT_MATCH`;
- listing drift rejected as exact match;
- valid `DRIFTED`;
- false `DRIFTED` with exact metadata rejected;
- malformed runner checkpoint and empty preflight authorization ref rejected.

Gate 6 tests cover:

- Git protected-package self-binding;
- missing fabricated commit rejection;
- modified runner blob detection;
- machine-checkable preflight before temp creation;
- continued absence of network clients.

## Preserved boundaries

No parser change.
No runtime v1.2 change.
No proposal mutation.
No repository mutation.
No approval grant.
No source access.
No actual preflight.
No download.
No Owner Name File opening.
No PII processing.
No sixth execution.
No retry.

## State

`GATE6_REMEDIATION_OFFLINE / TARGETED_VALIDATION_PASS / REVIEW_PENDING`

## Next gate

`HUMAN_REVIEW_NY_OSC_SIXTH_ATTEMPT_GATE6_REMEDIATION_OFFLINE`
