# MVP-1 Synthetic Vertical Slice — Offline Audit

Date: 2026-09-17

Classification: `A — Product Critical`

## Objective

Reduce the distance from an eventual approved New York OSC Owner Name File to the first economically reviewable case without waiting for requester contact data and without accessing any real owner data.

This package validates the downstream product path with synthetic data only:

`synthetic post-schema record -> exact insurance classification -> narrow IN03 candidate -> economics -> reviewer`

It does not claim that the real New York physical file schema has been observed.

## Source / Privacy Boundary

The New York source remains:

`REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`

Gate 1 approval remains granted but unconsumed while requester contact data are unavailable. This package does not submit the OSC form, request a file, download a file, process real owner PII, perform identity resolution, beneficiary matching, outreach, representation or claim activity.

The synthetic input is explicitly positioned after a hypothetical successful schema mapping and is labeled:

`SYNTHETIC_POST_SCHEMA_MAPPING`

It contains only synthetic references and synthetic reporting labels.

## Reuse Review

### Existing project stack — REUSE

Reused directly:

- Pydantic v2 for typed deterministic read models;
- JSON Schema draft 2020-12 for a versioned UI/reviewer contract;
- FastAPI reviewer routing;
- the existing Streamlit reviewer surface and visual language;
- existing deterministic/fail-closed governance conventions.

This covers the current need without adding a new runtime dependency.

### `venmo/business-rules` — DEFER / NOT ADOPTED

Observed benchmark facts:

- MIT licensed;
- Python DSL for configurable business rules;
- established adoption signal;
- latest repository push observed: 2024-08-13.

Reason not adopted now:

The current MVP-1 slice needs only a handful of exact, source-specific deterministic decisions. Introducing a separate rule DSL would increase dependency and integration surface without reducing material product work.

### `gorules/zen` — DEFER / NOT ADOPTED

Observed benchmark facts:

- MIT licensed;
- active open-source multi-language business rules engine;
- repository activity observed in 2026;
- supports Python among several runtimes.

Reason not adopted now:

The engine is materially broader than the present requirement and would add runtime/integration complexity before there is evidence that rules need non-code authoring, large policy graphs or business-user configuration.

Reuse decision:

`REUSE EXISTING STACK > ADD NEW RULE ENGINE`

Reconsider an external engine only if rule count/complexity, non-developer authoring or cross-runtime policy execution becomes a measured blocker.

## Implemented Product Path

### Classification

Only exact authority-backed New York insurance codes are recognized. No trim, uppercase, repair, inference or pattern-based promotion is performed.

- exact `IN03` -> `MVP1_PRIMARY_INSURANCE`;
- another exact recorded NY insurance code -> `INSURANCE_OTHER`;
- unknown code -> `NO_AUTHORITY_BACKED_INSURANCE_MATCH`.

### Candidate creation

For this narrow first slice, only exact `IN03` creates a synthetic candidate.

The case identifier is deterministic from source id + synthetic record reference.

No identity resolution or beneficiary matching is implied by candidate creation.

### Economics

Because the selected OSC Owner Name File does not disclose dollar value, the synthetic case preserves:

- `recoverable_value_state = UNKNOWN_FROM_SOURCE`;
- `source_amount_available = false`;
- `fee_basis_state = NOT_COMPUTABLE_FROM_SOURCE`;
- `commercial_threshold_applied = false`;
- `invented_amounts = false`.

The product therefore exposes the next commercial evidence need rather than inventing a score:

- recoverable value evidence;
- expected follow-up cost;
- lawful fee basis.

Reviewer decision requested:

`CONTINUE_VALUE_RESEARCH_OR_STOP`

## Reviewer Surface

The existing Streamlit M3 console is retained and extended with an additional synthetic MVP-1 case section. The existing no-real-source/no-real-PII safety banner and M3 read model remain intact.

A dedicated read-only API endpoint exposes the synthetic case contract:

`GET /api/reviewer/mvp1/synthetic-case`

## Contract and Tests

Added:

- `src/unclaimed_platform/domain/mvp1_vertical_slice.py`;
- `schemas/ui/mvp1_synthetic_case_review.schema.json`;
- `tests/unit/test_mvp1_synthetic_vertical_slice.py`;
- `tests/contract/test_mvp1_synthetic_case_review.py`;
- API and Streamlit smoke coverage.

Tests specifically reject:

- promotion of unknown `IN99` into the NY insurance vocabulary;
- creation of the primary candidate from non-primary `IN01`;
- economics on a non-created candidate;
- contract mutation indicating real source access;
- contract mutation indicating invented monetary amounts;
- reviewer read model mutation indicating real source access.

## Economic / Product Contribution

This work removes downstream construction from the critical path of the first real New York case. Once a lawful real source and deterministic physical-to-semantic mapping exist, the first exact `IN03` record can target an already exercised path through candidate creation, economics and reviewer presentation.

The slice also establishes an important commercial fact early: the selected Owner Name File alone cannot make a case economically actionable because recoverable value is absent. The next commercial research problem after candidate discovery is therefore value evidence / cost / lawful fee basis, not merely additional classification code.

## Verification

GitHub Actions verification is required before this package is considered complete. Final CI run and conclusion will be recorded after the implementation branch reaches a stable green checkpoint.
