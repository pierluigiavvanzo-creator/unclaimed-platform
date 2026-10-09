# MVP-1 Synthetic Vertical Slice — Offline Audit

Date: 2026-09-17

Classification: `A — Product Critical`

## Objective

Reduce the distance from an eventual approved New York OSC Owner Name File to the first economically reviewable case without waiting for requester contact data and without accessing any real owner data.

Validated downstream path:

`synthetic post-schema record -> exact insurance classification -> narrow IN03 candidate -> economics -> reviewer`

This package does not claim that the real New York physical file schema has been observed.

## Source / Privacy Boundary

The New York source remains:

`REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`

Gate 1 approval remains granted but unconsumed while requester contact data are unavailable. This package did not submit the OSC form, request or download an owner file, process real owner PII, perform identity resolution, beneficiary matching, outreach, representation or claim activity.

The synthetic input is explicitly positioned after a hypothetical successful schema mapping and is labeled:

`SYNTHETIC_POST_SCHEMA_MAPPING`

It contains only synthetic references and synthetic reporting labels.

## Reuse Review

### Existing project stack — REUSE

Reused directly:

- Pydantic v2 for typed deterministic read models;
- JSON Schema draft 2020-12 for a versioned reviewer contract;
- FastAPI reviewer routing;
- the existing Streamlit reviewer surface and visual language;
- existing deterministic/fail-closed governance conventions.

### `venmo/business-rules` — DEFER / NOT ADOPTED

Observed:

- MIT licensed;
- Python DSL for configurable business rules;
- established adoption signal;
- latest repository push observed: 2024-08-13.

Not adopted because the current slice needs only a handful of exact deterministic decisions; a separate rule DSL would add dependency and integration surface without reducing material product work.

### `gorules/zen` — DEFER / NOT ADOPTED

Observed:

- MIT licensed;
- active multi-language business-rules engine;
- repository activity observed in 2026;
- Python support among several runtimes.

Not adopted because it is materially broader than the current requirement and would add runtime/integration complexity before there is evidence that rules need non-code authoring or a larger policy graph.

Decision:

`REUSE EXISTING STACK > ADD NEW RULE ENGINE`

## Implemented Product Path

### Classification

Only exact recorded New York insurance codes are recognized. No trim, uppercase, repair, inference or pattern-based promotion is performed.

- exact `IN03` -> `MVP1_PRIMARY_INSURANCE`;
- another exact recorded NY insurance code -> `INSURANCE_OTHER`;
- unknown code -> `NO_AUTHORITY_BACKED_INSURANCE_MATCH`.

### Candidate creation

Only exact `IN03` creates the narrow synthetic MVP-1 candidate. The case identifier is deterministic from source id + synthetic record reference.

Candidate creation does not imply identity resolution or beneficiary matching.

### Economics

Because the OSC Owner Name File does not disclose dollar value, the synthetic case preserves:

- `recoverable_value_state = UNKNOWN_FROM_SOURCE`;
- `source_amount_available = false`;
- `fee_basis_state = NOT_COMPUTABLE_FROM_SOURCE`;
- `commercial_threshold_applied = false`;
- `invented_amounts = false`.

Required next evidence:

- recoverable value evidence;
- expected follow-up cost;
- lawful fee basis.

Reviewer decision:

`CONTINUE_VALUE_RESEARCH_OR_STOP`

## Reviewer Surface

The existing Streamlit M3 console remains intact and now includes a synthetic MVP-1 case/economics section.

Read-only API endpoint:

`GET /api/reviewer/mvp1/synthetic-case`

## Contract and Tests

Added:

- `src/unclaimed_platform/domain/mvp1_vertical_slice.py`;
- `schemas/ui/mvp1_synthetic_case_review.schema.json`;
- `tests/unit/test_mvp1_synthetic_vertical_slice.py`;
- `tests/contract/test_mvp1_synthetic_case_review.py`;
- API and Streamlit smoke coverage.

Tests reject:

- promotion of unknown `IN99` into the NY insurance vocabulary;
- creation of the primary candidate from non-primary `IN01`;
- economics on a non-created candidate;
- contract mutation indicating real source access;
- contract mutation indicating invented monetary amounts;
- reviewer mutation indicating real source access.

## Verification

Stable implementation checkpoint before canonical documentation updates:

`caedbb67c3077a654533a5c96dab42cbfa4e0cf3`

GitHub Actions:

`35263620224` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety smoke;
- Streamlit startup smoke;
- frontend lint;
- frontend typecheck;
- frontend build.

The preceding run `35263474623` failed only on import ordering in one new contract test; commit `caedbb67...` corrected that formatting-only issue without changing product logic.

## Economic / Product Contribution

This removes downstream construction from the critical path of the first real New York case. Once a lawful real source and deterministic physical-to-semantic mapping exist, an exact `IN03` record can enter an already exercised candidate/economics/reviewer path.

It also exposes the next commercial blocker early: the Owner Name File alone cannot make a case economically actionable because recoverable value is absent. The next product-critical offline question is therefore how a candidate can obtain lawful, reproducible value/cost/fee-basis evidence before expensive downstream investigation.
