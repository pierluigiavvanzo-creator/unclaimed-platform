# NY OSC Runner Surface

**Date:** 2026-10-09  
**Status:** CURRENT OPERATING MAP  
**Authorization effect:** NONE

## Current active entrypoint

The only canonical PowerShell entrypoint for the current Stage B P1 is:

`scripts/ny_osc_gate.ps1`

It forwards to:

`scripts/ny_mvp1_p1_targetability_execute.py`

which uses:

`src/unclaimed_platform/adapters/sources/ny_owner_name_p1_targetability_local.py`

The compatibility wrapper:

`scripts/ny_mvp1_p1_targetability_local.ps1`

must forward to `scripts/ny_osc_gate.ps1`; it is not a second independent execution surface.

## Historical lineage

Gate 2–11 scripts and versioned transient-local runtime modules are retained because their paths/checkpoints are part of historical execution and approval provenance.

They are classified:

`HISTORICAL_CONSUMED_NON_REUSABLE`

Canonical metadata:

`src/unclaimed_platform/adapters/sources/ny_owner_name_runner_registry.py`

Historical files must not be selected as current execution entrypoints and their approvals must never be reused.

## Evolution rule

Future Stage B execution work should extend the current P1 contract/runner when the product boundary is unchanged.

Do not create a new numbered `ny_osc_gate12_...` or another version-suffixed transient runner merely as the default way to evolve the product.

A new execution surface is justified only by a materially new boundary and requires the normal Product Owner/legal/privacy review.

## Current authorization state

All seven real-P1 gates remain:

`NOT_GRANTED`

This runbook does not authorize preflight, download, source access, PII processing, external PII query, outreach, value research, representation or claim activity.
