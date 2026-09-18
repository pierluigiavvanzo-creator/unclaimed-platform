# NY MVP-1 Follow-Up Cost Measurement Contract — Offline Implementation

Date: 2026-09-18

Classification: `A — Product Critical`

## Objective

Implement the smallest deterministic, provenance-bearing contract needed to measure per-candidate follow-up cost for MVP-1 without inventing default money or time assumptions and without using any real owner data.

Required measured dimensions:

1. automated processing cost per candidate;
2. source/data cost per candidate;
3. human review time per candidate;
4. additional manual research time per candidate.

An optional documented human labor rate may be supplied later to convert measured human time into monetary cost. It is never inferred from time alone.

## Scope Boundary

This package is offline and synthetic/test-only for implementation verification.

It does not:

- download or inspect the New York OSC Owner Name File;
- process owner name, address or other real owner PII;
- perform identity resolution or beneficiary matching;
- contact an owner;
- create or execute a fee agreement;
- submit a claim;
- invent a per-candidate cost, hourly rate, or commercial threshold.

The contract explicitly requires `owner_pii_included = false`.

## Reuse Review

### Existing Pydantic + JSON Schema patterns — REUSE

The project already uses Pydantic v2 for deterministic typed domain models and JSON Schema draft 2020-12 for versioned machine contracts. Those patterns are reused directly.

### Existing `BudgetLedger` — REUSE CONCEPT, DO NOT REPURPOSE

`src/unclaimed_platform/core/budget_engine/model.py` already provides deterministic budget authorization and consumption accounting.

It is not reused as the follow-up cost measurement model because its semantic purpose is different:

- `BudgetLedger` answers whether spending is authorized against a limit;
- this new contract records what a candidate actually measured in cost/time.

Conflating the two would blur authorization and measurement.

### Existing Evidence / audit conventions — REUSE

The repository already requires provenance and auditability for material facts. This package therefore requires an `evidence_ref` and `observed_at` timestamp for every measured cost/time component.

No new dependency or external cost-accounting package is justified.

Decision:

`REUSE EXISTING TYPED + PROVENANCE PATTERNS > NEW DEPENDENCY`

## Contract

### Monetary components

`automated_processing`

Measured per-candidate automation/compute/tool cost in integer cents.

`source_data`

Measured or allocated per-candidate source/data cost in integer cents.

Each monetary component requires:

- `amount_cents`;
- currency (`USD`);
- measurement method;
- allocation basis;
- evidence reference;
- observation timestamp.

A documented zero direct cost is allowed only when both the measurement method and allocation basis explicitly identify zero direct cost, and `amount_cents = 0`.

### Human-effort components

`human_review`

Measured review duration in integer seconds.

`manual_research`

Measured additional manual research duration in integer seconds.

Each time component requires:

- `duration_seconds`;
- measurement method;
- evidence reference;
- observation timestamp.

### Optional human labor rate

`human_labor_rate` is optional.

If absent:

- human time remains measured;
- human labor cost is not computed;
- fully loaded follow-up cost remains `NOT_COMPUTABLE_NO_LABOR_RATE`.

If explicitly supplied with provenance:

- human labor cost is computed from total measured seconds and documented cents/hour;
- fully loaded follow-up cost becomes the sum of machine/data cost plus documented-rate human labor cost.

This keeps time measurement separate from compensation assumptions.

## Deterministic Output

The result exposes:

- automated processing cost cents;
- source/data cost cents;
- direct machine + data cost cents;
- human review seconds;
- manual research seconds;
- total human seconds;
- documented labor-rate state/value when present;
- computed human labor cost only when rate evidence is present;
- fully loaded follow-up cost only when all required monetary inputs exist;
- deduplicated evidence references;
- `owner_pii_included = false`;
- `no_commercial_recommendation = true`.

No continue/stop recommendation is produced.

## Test Fixtures

Synthetic fixture amounts/times exist only to exercise arithmetic and validation. They are not commercial assumptions, estimates, benchmarks or forecasts.

Tests cover:

- separate cost/time reporting with no labor rate;
- fully loaded calculation with an explicit documented labor rate;
- rejection of negative monetary measurement;
- rejection of inconsistent zero-cost markers;
- rejection of owner PII flag;
- rejection of inconsistent aggregate result;
- JSON Schema validation for input/output;
- rejection of missing evidence;
- rejection of a commercial-recommendation mutation.

## Product Contribution

This closes the current `NOT_MEASURED` implementation gap without manufacturing economics.

When a real candidate workflow becomes authorized, the platform can capture actual per-candidate machine/data costs and human effort with provenance. A fully loaded follow-up cost can then be supplied to the existing case-economics path only after a documented labor rate exists.

This directly supports the project metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`
