# NY OSC Synthetic One-Candidate Transient Materialization — Implementation Review

Date: 2026-09-23

Work class: `A — Product Critical`

Canonical repository baseline reviewed: `main @ c34c8f4ceb106bd5ac1b12e40fe6544f6469db63`

Requested action:

`IMPLEMENT_AND_REVIEW_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION`

Review status:

`CONDITIONAL_PASS_SYNTHETIC_CANDIDATE_READY_FOR_REPOSITORY_PR_CI`

## 1. Scope boundary

This candidate implementation is synthetic-only. It does not authorize or perform:

- source access;
- remote preflight;
- download;
- real owner PII processing;
- real candidate materialization;
- identity resolution;
- beneficiary matching;
- address enrichment;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

The implementation prepares only the contracts/interfaces needed to test future one-case economic instrumentation before any real-candidate privacy/legal expansion.

## 2. Repository-first reuse

The candidate reuses existing deterministic components rather than replacing them:

- `src/unclaimed_platform/domain/ny_mvp1_value_evidence.py` for fail-closed `UNKNOWN_PRE_CLAIM_REVIEW` value evidence;
- `src/unclaimed_platform/domain/ny_mvp1_follow_up_cost.py` for evidenced machine/data cost, human time and optional documented labor-rate aggregation;
- `src/unclaimed_platform/domain/ny_mvp1_case_economics_integration.py` as the explicit future integration target once value, fee and fully loaded cost evidence exist.

No new third-party runtime dependency or agent framework is introduced.

## 3. Candidate files

New candidate implementation files:

- `src/unclaimed_platform/domain/ny_osc_one_candidate_transient_materialization.py`;
- `schemas/common/ny_osc_synthetic_one_candidate_transient_materialization.schema.json`;
- `tests/unit/test_ny_osc_one_candidate_transient_materialization.py`;
- `tests/contract/test_ny_osc_synthetic_one_candidate_transient_materialization.py`.

This review file is the fifth proposed new repository file.

## 4. Deterministic candidate-selection behavior

The synthetic selector:

- requires source-record ordinals in strictly increasing order and fails closed instead of sorting/re-ranking;
- evaluates fixtures in supplied physical source order;
- selects the first eligible record only;
- requires the documented 14-field structural shape;
- requires exact `IN03`;
- requires Property Owner Count exactly `1`;
- requires a non-empty transient Property ID;
- stops after the first eligible record;
- emits an explicit zero-candidate stop if none qualifies;
- derives the persistent `case_id` only from non-owner provenance: source ID, source snapshot, source record ordinal, `IN03`, and the selection-rule version.

Owner Name and Property ID are not used in durable case identity.

## 5. Economic Case Ledger readiness

The synthetic non-PII ledger demonstrates interfaces for:

- non-PII `case_id` and source provenance;
- initial friction lane `F0/F1/F2/F3`;
- typed lane-change events with reason/evidence and `value_evidence_used=false`;
- current lane derived from contiguous lane history;
- explicit statement that lane assignment is friction segmentation, not a value prediction;
- `L0` and `L1` stage timestamps/evidence;
- measured automated-processing and source/data cost evidence;
- measured human-review and manual-research time evidence;
- optional labor cost only from a documented labor-rate evidence reference;
- `PRE_VALUE_DISCOVERY_COST` state and accumulated cost when computable;
- Product Owner-approved L1 incremental budget and budget evidence reference;
- bounded stop reason;
- fail-closed requirement for separate L2 privacy/legal scope;
- fail-closed `UNKNOWN_PRE_CLAIM_REVIEW` value-evidence state;
- hooks to existing follow-up-cost, value-evidence and case-economics components;
- no automatic commercial recommendation.

## 6. PRE_VALUE_DISCOVERY_COST behavior

The synthetic implementation does not invent a profitability threshold.

It uses the explicitly supplied L1 incremental budget only as a bounded experimental stop-loss:

- fully loaded cost unavailable because no documented labor rate -> `MEASURING` with explicit instrumentation stop reason;
- fully loaded pre-value cost above the approved L1 budget -> `VALUE_STILL_UNKNOWN_STOPPED`;
- cost within the approved L1 budget but value still requires later identity/contactability scope -> `VALUE_REQUIRES_UNAUTHORIZED_SCOPE`.

The implementation never interprets an F0–F3 lane as evidence of recoverable value.

## 7. Privacy / persistence review

The durable candidate envelope and Economic Case Ledger do not persist or return:

- Owner Name;
- Property ID;
- raw source row;
- address fields;
- owner-row hash.

The result records that transient values are not returned and that no real owner PII or real candidate was processed by this synthetic package.

## 8. Acceptance-criteria review

| Mandatory criterion | Candidate result |
|---|---|
| lane assignment | PASS — explicit F0/F1/F2/F3 friction lane |
| lane-change provenance | PASS — typed contiguous events with reason/evidence |
| stage timestamps | PASS — L0/L1 event contract |
| component cost evidence | PASS — reused measured-cost contracts |
| human-time evidence | PASS — reused measured-duration contracts |
| `PRE_VALUE_DISCOVERY_COST` state | PASS — required states represented for current L1 outcomes |
| economic discovery ladder stage | PASS — current `L1`, with L0/L1 provenance |
| bounded stop reason | PASS — budget/instrumentation/L2-scope reasons |
| value-evidence state | PASS — reused fail-closed `UNKNOWN_PRE_CLAIM_REVIEW` |
| follow-up-cost integration hook | PASS — existing measurement function actually executed |
| case-economics integration hook | PASS AS BLOCKED — interface identified; no calculation without value/fee evidence |
| no owner PII in ledger | PASS |
| no real source/PII/outreach/claim behavior | PASS by contract and targeted tests |

## 9. Local verification evidence

Isolated targeted verification executed against the candidate package:

- targeted unit + contract tests: `13 passed`;
- Python compile check for new Python files/tests: PASS;
- no lines above the repository 100-character Ruff line-length target in the new Python module/tests;
- generated JSON Schema validated against runtime output and rejected attempted owner-PII/authorization scope expansion.

Important limitation:

- the available isolated runtime is Python `3.13.5`, while repository `pyproject.toml` requires `>=3.11,<3.13`;
- Ruff and mypy are not installed in the isolated runtime;
- the complete repository test suite and frontend/Streamlit CI were not executed locally;
- therefore these local checks cannot substitute for canonical GitHub Actions CI on a repository branch.

## 10. Canonical baseline and post-merge CI verification

The remote `main` HEAD was re-verified as:

`c34c8f4ceb106bd5ac1b12e40fe6544f6469db63`

The post-merge `push` workflow was retrieved directly from the GitHub Actions run collection:

- workflow: `ci`;
- run: `35917183796`;
- event: `push`;
- head branch: `main`;
- head SHA: `c34c8f4ceb106bd5ac1b12e40fe6544f6469db63`;
- conclusion: `success`;
- `quality`: `success`;
- `streamlit-candidate`: `success`.

Baseline verification result:

`MAIN_HEAD_VERIFIED / POST_MERGE_CI_SUCCESS`

## 11. Review conclusion

The implementation candidate satisfies the requested synthetic design and economic-instrumentation acceptance criteria in targeted isolated tests and remains inside the approved privacy/product boundary.

It is **not yet a canonical repository PASS** because the proposed files have not been committed/pushed and GitHub Actions has not tested them in the repository-supported Python/CI environment.

Result:

`CONDITIONAL_PASS_SYNTHETIC_CANDIDATE_READY_FOR_REPOSITORY_PR_CI`

Next integration gate:

create one isolated branch from `main @ c34c8f4...`, add only the five candidate files, open a PR, and require the normal repository CI to pass. No merge, source access, real PII, or Pilot P1 authorization is implied by that integration step.