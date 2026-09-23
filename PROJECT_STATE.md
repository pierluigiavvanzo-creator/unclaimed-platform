# PROJECT_STATE.md

Last updated: 2026-09-23

## Authoritative product state

The project is in **PRODUCT VALIDATION MODE**.

Primary objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

Governance and source diagnostics remain frozen unless a real execution proves a concrete blocker.

## Canonical integration branch

`main`

`main` remains the canonical integration branch. Product-critical milestone branches are temporary and must not be merged without the Product Owner's explicit authorization.

## Real-source evidence — NY OSC Attempt 9

Attempt 9 executed once and is `CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO_RETRY`.

Authoritative non-PII evidence:

`sources/evidence/ny_osc_owner_name_file_ninth_attempt_execution_result.v1.json`

Observed aggregate result:

- status `BLOCKED`;
- reason `TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED`;
- archive bytes `409477526`;
- physical records `14994489`;
- exactly-14-pipe records `12`;
- records ending with `|`: `0`;
- non-empty data after the 14th pipe: `12`;
- records with any other pipe count: `14994477`;
- no owner/raw values returned.

The empty-terminal-field hypothesis is rejected. The `14994477` aggregate bucket must not be interpreted as all 13-pipe records.

## Real-source evidence — NY OSC Attempt 10

Attempt 10 received fresh exact-match metadata and one bounded execution authorization. One manual download occurred, but the product slice did not start.

Authoritative non-PII evidence:

`sources/evidence/ny_osc_owner_name_file_tenth_attempt_execution_result.v1.json`

Result:

- status `BLOCKED`;
- reason `AUTHORIZED_DOWNLOAD_START_OUTSIDE_FRESH_PREFLIGHT_WINDOW`;
- failure stage `BUILD_REAL_EXECUTION_AUTHORIZATION_V1_6`;
- the runner had already confirmed `FINDERS.zip` existed before invoking Python;
- classification did not start;
- no candidate/zero-candidate result was produced;
- no owner values or raw path were returned;
- authorization is treated as `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- zero retry;
- runner cleanup was attempted, but physical secure erasure is not guaranteed.

Root cause: Gate 10 depended on the operator pressing Enter to capture the download-start marker. That marker was recorded after the 900-second preflight deadline.

## Completed product-critical milestone — NY OSC Attempt 11

Branch:

`mvp1-ny-eleventh-auto-start-detection-offline`

Historical PR:

`#29 — MERGED`

Canonical integration PR:

`#30 — MERGED INTO main`

Main integration commit:

`c5a56be629b7a684666a8fc5ee57fec24ff734c4`

Attempt 11 reuses the Attempt-10 product slice unchanged and modifies only the freshness handoff.

Proposal checkpoint:

`270de2f6e79b7c654052519adc446fe76b811771`

Runner/code checkpoint:

`bac89609e9069efc98fcd0866b89ee4ee16f1689`

CI:

`35859448715 — SUCCESS`

Passed: Ruff, mypy, contract tests, smoke tests, full pytest suite, Streamlit safety/startup, frontend lint/typecheck/build.

Gate 11 behavior:

- requires at least `180` freshness seconds remaining before exposing the download instruction;
- creates a new dedicated empty OS temp directory;
- arms automatic detection before instructing the operator to start the manual download;
- polls the dedicated directory every `100 ms`;
- captures the authorized download-start marker at the first observation of any non-empty file in that previously empty directory;
- no operator Enter is used for the start marker;
- if no start is observed before the preflight deadline, execution stops fail-closed;
- completion confirmation remains one manual Enter after the same single download finishes;
- one download / one execution / zero retry;
- no direct network client in the runner;
- product slice remains: 13 pipes -> documented 14-field width -> Property Type Code index 1 -> exact authority-backed insurance classification -> aggregate IN03 candidate or zero-candidate result;
- all other physical shapes are deferred metadata-only;
- owner/candidate PII is not materialized by this package;
- recoverable value remains `UNKNOWN_FROM_SOURCE`.

No NY OSC access, fresh preflight, download, or PII processing occurred while preparing Attempt 11 offline.

## Real-source evidence — NY OSC Attempt 11

Attempt 11 completed the bounded real product slice once.

Authoritative result:

`sources/evidence/ny_osc_owner_name_file_eleventh_attempt_execution_result.v1.json`

Audit:

`docs/audits/NY_OSC_ELEVENTH_ATTEMPT_PRODUCT_SLICE_COMPLETED.md`

Result:

- status `COMPLETED`;
- reason `PRODUCT_SLICE_COMPLETED`;
- archive bytes `409477526`;
- total records `14994489`;
- structurally conforming records `14994477`;
- deferred structural records `12`;
- authority-backed insurance records `2792990`;
- primary `IN03` candidate records `203921`;
- other insurance records `2589069`;
- no authority-backed insurance match records `12201486`;
- unclassifiable Property Type Code records `1`;
- candidate outcome `CANDIDATES_PRESENT_AGGREGATE_ONLY`;
- candidate materialization `NOT_AUTHORIZED_AGGREGATE_ONLY`;
- economic actionability `VALUE_EVIDENCE_REQUIRED`;
- recoverable value `UNKNOWN_FROM_SOURCE`;
- owner/raw values returned: none;
- local archive logical deletion reported: true;
- physical secure erasure guarantee: false.

Authorized download start:

`2026-09-23T12:30:59.478237Z`

Automatic start detection succeeded inside the fresh-preflight window.

All Attempt-11 single-use grants are now treated as:

`CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO_RETRY`

No Attempt-11 authorization may be reused.

## Current product blocker

The parser/freshness blocker is closed for the current bounded slice.

The remaining MVP-1 gap is downstream:

`ONE LAWFULLY MATERIALIZED CANDIDATE -> VALUE/EVIDENCE -> CASE ECONOMICS -> REVIEWER DECISION`

Existing repository components already provide deterministic/fail-closed foundations for:

- candidate/classification contracts;
- pre-contact value-evidence state;
- measured follow-up cost;
- explicit case economics;
- reviewer surfaces.

Current real candidate materialization remains unauthorized, and the real source result does not provide supported recoverable-value evidence or a lawful fee basis.

Do not return to parser/timing diagnostics unless new evidence proves a concrete blocker.

## Economic feasibility audit — 2026-09-23

Whole-project audit:

`docs/audits/ECONOMIC_FEASIBILITY_AUDIT_2026-09-23.md`

Audit status:

`CONDITIONAL_CONTINUE_ECONOMIC_VALIDATION_NOT_SCALE`

Main conclusions:

- real candidate supply is proven at aggregate record level: `203921` primary `IN03` records;
- source screening/processing technical feasibility is proven;
- New York has an explicit commercial location-service-provider framework with a statutory maximum fee of 15% for the applicable scope;
- the owner can claim directly from OSC for free, so discovery alone is not a sufficient value proposition;
- OSC increasingly automates qualifying simple/low-value returns;
- case-level recoverable value is not available in the Owner Name File and remains unavailable before claim review/ownership verification;
- real unit economics, contact conversion, realized fee, collection rate and cycle time are not measured;
- lawyer-fee referral/revenue-share economics must not be assumed without specialized legal review;
- project-wide scale/architecture expansion is economically premature.

The economic bottleneck is now:

`CANDIDATE -> LAWFUL VALUE/CONTACT DISCOVERY -> MEASURED COST -> RECOVERY -> REALIZED FEE -> CONTRIBUTION`

## Current next action

Do not expand privacy scope or general architecture yet.

If the Product Owner accepts the audit conclusion, the next implementation task is Stage A only:

`IMPLEMENT_AND_REVIEW_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION`

using the already approved proposal:

`sources/proposals/ny_osc_one_candidate_value_evidence_offline_proposal.v1.json`

Stage A must remain synthetic-only and must not authorize source access, download, owner PII, identity resolution, beneficiary matching, outreach, value research, fee agreement, representation or claim activity.

Only after Stage A and an explicit legal/privacy review may a separate one-real-candidate economic-discovery execution be considered.

## Product exit criteria

Current status:

- authorized real source: ACHIEVED FOR BOUNDED EXECUTIONS;
- bounded real acquisition: ACHIEVED;
- whole-file structural evidence: ACHIEVED VIA ATTEMPT 9;
- real row-defer + insurance classification: ACHIEVED VIA ATTEMPT 11;
- real candidate or documented zero-candidate aggregate: ACHIEVED — `203921` aggregate primary `IN03` candidates;
- real candidate materialization: NOT AUTHORIZED / NOT DONE;
- real provenance/evidence package: PARTIAL;
- reproducible real case economics: BLOCKED UNTIL VALUE/FEE/COST EVIDENCE EXISTS;
- reviewer case with human GO / REVISE / STOP: NOT DONE;
- commercial baseline: PARTIAL — real funnel counts established, value/review-cost/revenue evidence still missing.
