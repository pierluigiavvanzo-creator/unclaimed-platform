# NY OSC Line-Local Runtime Integration v1.2 — Offline Implementation

Date: 2026-09-20

Classification: A — Product Critical / Runtime Integration

## Requested action

IMPLEMENT_NY_OSC_LINE_LOCAL_RUNTIME_INTEGRATION_OFFLINE

## Canonical baseline

- repository: pierluigiavvanzo-creator/unclaimed-platform
- canonical branch: mvp1-ny-second-attempt-approved-ready-execution
- baseline HEAD: 66259cc79e5087f6e205344858f8ca471247e632

The fifth attempt is already reconciled as consumed, single-use,
non-reusable and zero-retry.

## Implementation

This branch adds a new explicit runtime path without changing historical
execution behavior.

Authorization contract 1.1.0 requires the explicit parser mode
LINE_LOCAL_ARBITRATION. There is no legacy default in that contract.

Execution result contract 1.2.0 adds the selected quote-dialect mode and a
bounded quote-dialect diagnostic. Structural and quote-dialect diagnostics
are mutually exclusive and reason-bound.

The new build_real_execution_authorization_v1_1() first preserves the existing
single-use/zero-retry checks, then requires explicit future approval bindings
for authorization 1.1.0, result 1.2.0, line-local arbitration and both
diagnostic contract versions. It also rechecks local-retention and PII
processing scope, including authorization to persist only the bounded
quote-dialect diagnostic.

The new execute_transient_local_file_discovery_v1_2() explicitly passes
LINE_LOCAL_ARBITRATION into schema discovery, collects the two diagnostic
types separately, rejects conflicting diagnostic emissions and preserves the
existing finally-block deletion behavior.

A separate v1.2 CLI module is added. No existing runner is retargeted.

## Pre-commit correction

Offline preparation exposed an implementation bug before repository write:
the first candidate builder referenced local scope before loading the local
approval object. The committed candidate loads both approval objects
explicitly. The v1.2 result invariant was also strengthened so DISCOVERED
cannot exist without a schema-discovery result.

## Historical isolation

Unchanged by this implementation:

- NyTransientLocalExecutionAuthorization 1.0.0
- NyTransientLocalExecutionResultV1_1
- build_real_execution_authorization()
- execute_transient_local_file_discovery()
- historical module main()
- scripts/ny_osc_gate5_transient_local.ps1
- all prior runners and consumed approval artifacts

Therefore this implementation does not activate line-local parsing in any
existing operational path.

## Explicit exclusions

No OSC access, listing preflight, download, real Owner Name File opening,
PII processing, retry, sixth-attempt proposal, sixth-attempt approvals,
sixth-attempt runner, matching or outreach occurred.

## State at commit

IMPLEMENTED_OFFLINE / NOT_RUNTIME_ACTIVATED / CI_PENDING
