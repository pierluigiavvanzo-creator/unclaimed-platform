# ROADMAP.md

Last updated: 2026-09-23

## Product validation critical path

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

No broad platform expansion is scheduled before this is complete.

## Stage 1 — Real-source evidence already established

Attempt 9 scanned the complete real archive under bounded authorization:

- `14994489` physical records;
- `12` records with exactly `14` pipes;
- `0` records ending with a terminal pipe;
- `12` records with non-empty bytes after the 14th pipe;
- `14994477` records with another pipe count;
- no owner/raw values returned;
- authorization consumed, zero retry.

The terminal-empty-field hypothesis is rejected.

Attempt 10 then attempted the first direct real product-slice execution. The manual download occurred, but the product slice did not start because the operator-captured download-start marker fell outside the 900-second fresh-preflight window. Attempt 10 is consumed/non-reusable/zero-retry.

## Stage 2 — Attempt 11 real product slice — COMPLETED

Historical branch:

`mvp1-ny-eleventh-auto-start-detection-offline`

Historical PR:

`#29 — MERGED`

Canonical integration:

`PR #30 — MERGED INTO main at c5a56be629b7a684666a8fc5ee57fec24ff734c4`

Protected runner checkpoint:

`bac89609e9069efc98fcd0866b89ee4ee16f1689`

Runner CI:

`35859448715 — SUCCESS`

Attempt 11 completed one bounded real execution with automatic download-start detection.

Authoritative result:

`sources/evidence/ny_osc_owner_name_file_eleventh_attempt_execution_result.v1.json`

Observed product result:

- `14994489` total records;
- `14994477` structurally conforming records;
- `12` deferred structural records;
- `2792990` authority-backed insurance records;
- `203921` primary `IN03` aggregate candidates;
- `2589069` other insurance records;
- `12201486` no-authority-match records;
- `1` unclassifiable Property Type Code record;
- `CANDIDATES_PRESENT_AGGREGATE_ONLY`;
- `VALUE_EVIDENCE_REQUIRED`.

No owner/raw values were returned or persisted by the result. The local archive was reported logically deleted; physical secure erasure is not guaranteed.

## Stage 3 — Attempt 11 human gates — CONSUMED

All Attempt-11 single-use gates required for the completed execution were exercised and are non-reusable:

1. transient local-file grant;
2. transient PII grant;
3. fresh-listing preflight authorization;
4. exact-match fresh receipt;
5. bounded execution authorization;
6. one manual download and one Gate-11 execution.

State:

`CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO_RETRY`

No Attempt-11 grant may be reused.

## Stage 4 — Immediate result consumption — ACTIVE

The real source produced `203921` aggregate primary `IN03` candidates.

Therefore the critical path moves downstream to:

`ONE LAWFULLY MATERIALIZED CANDIDATE -> VALUE/EVIDENCE -> CASE ECONOMICS -> REVIEWER DECISION`

Current blocker:

- candidate materialization is `NOT_AUTHORIZED_AGGREGATE_ONLY`;
- recoverable value is `UNKNOWN_FROM_SOURCE`;
- lawful fee basis is not established for a real case;
- measured follow-up cost for a real candidate is not yet available.

Existing repository components for candidate contracts, value evidence, follow-up-cost measurement, case economics and reviewer display must be reused before any new custom implementation.

Do not return to parser/timing diagnostics unless new evidence proves a concrete blocker.

A bounded repository-only proposal has now been prepared on branch `mvp1-ny-one-candidate-value-evidence-offline-proposal`:

`sources/proposals/ny_osc_one_candidate_value_evidence_offline_proposal.v1.json`

It proposes exactly one deterministic source-order candidate, exact `IN03`, single owner, non-empty Property ID, transient-only Owner Name/Property ID, no address scope, no durable owner PII, and fail-closed value evidence.

Human review result: `APPROVED_PROPOSAL_ONLY`. No real-source or candidate-PII operation is authorized by that approval. The next Product Owner-requested activity is a separate whole-project economic-feasibility audit before expanding privacy scope or implementing real candidate materialization.

## Stage 5 — Economic feasibility validation — ACTIVE

Whole-project economic audit completed:

`docs/audits/ECONOMIC_FEASIBILITY_AUDIT_2026-09-23.md`

Decision:

`CONDITIONAL_CONTINUE_ECONOMIC_VALIDATION_NOT_SCALE`

Real evidence now supports:

- large candidate supply;
- technically bounded source processing;
- authority-backed insurance classification;
- an official NY location-service-provider framework.

Still unproven:

- unique/contactable candidate rate;
- recoverable-value distribution;
- pre-contact value observability;
- agreement conversion;
- successful recovery rate;
- realized fee percentage;
- fee collection;
- full per-case cost;
- cycle time;
- contribution before overhead.

Next economic stage is deliberately narrow:

1. synthetic-only one-candidate transient materialization implementation and review;
2. explicit legal/privacy review for the minimum real-candidate scope;
3. one separately authorized real economic-discovery case;
4. measured economics package;
5. Product Owner decision on whether broader PII/contact/outreach investment is justified.

No scale build before those measurements.

## Frozen backlog before MVP-1

Unless a direct blocker is demonstrated: new broad diagnostics, governance layers, multi-state expansion, new agent frameworks, graph infrastructure, broad genealogy automation, outreach/contracts/claims automation, non-critical UI polish, and infrastructure refactors.

## Git health

`main` is canonical and contains the validated real-source stack through Attempt 11 via PR #30 at commit `c5a56be629b7a684666a8fc5ee57fec24ff734c4`. Historical stacked PRs must not be used to duplicate integration into `main`.
