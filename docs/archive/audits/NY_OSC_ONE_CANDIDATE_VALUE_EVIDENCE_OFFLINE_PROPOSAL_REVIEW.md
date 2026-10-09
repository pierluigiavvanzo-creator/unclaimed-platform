# NY OSC — One-Candidate Materialization / Value-Evidence Offline Proposal Review

Date: 2026-09-23

Status: `READY_FOR_HUMAN_REVIEW_PROPOSAL_ONLY`

Work class: `A_PRODUCT_CRITICAL`

## Product reason

Attempt 11 established a real aggregate funnel:

`14994489 records -> 2792990 authority-backed insurance -> 203921 primary IN03 aggregate candidates`

The remaining MVP-1 blocker is no longer parser/freshness work. It is:

`ONE LAWFULLY MATERIALIZED CANDIDATE -> VALUE/EVIDENCE -> CASE ECONOMICS -> REVIEWER DECISION`

This review therefore limits scope to the smallest proposal that can move one real aggregate candidate toward that downstream path.

## Authoritative proposal

`sources/proposals/ny_osc_one_candidate_value_evidence_offline_proposal.v1.json`

Schema:

`schemas/common/ny_osc_one_candidate_value_evidence_offline_proposal.schema.json`

Contract test:

`tests/contract/test_ny_osc_one_candidate_value_evidence_offline_proposal.py`

## Repository-first reuse result

No new general candidate, economics or reviewer subsystem is justified.

Reuse / adapt:

- `src/unclaimed_platform/domain/mvp1_vertical_slice.py` — ADAPT exact `IN03` semantics and deterministic candidate-id approach;
- `schemas/common/case.schema.json` — REUSE canonical case envelope;
- `schemas/common/evidence.schema.json` — REUSE provenance/evidence linkage;
- `src/unclaimed_platform/domain/ny_mvp1_value_evidence.py` — REUSE fail-closed value state and prohibition on invented amounts;
- `src/unclaimed_platform/domain/ny_mvp1_follow_up_cost.py` — REUSE measured machine/data/human cost model;
- `src/unclaimed_platform/domain/ny_mvp1_case_economics_integration.py` — REUSE explicit economics only after evidence exists;
- `src/unclaimed_platform/api/reviewer.py` — ADAPT later; current reviewer endpoints remain synthetic-only and must not receive real PII silently.

The A07/A08/A10/A11/A15/A16 agent package directories do not currently provide substantive reusable implementation beyond placeholders. Building them out now would expand architecture without shortening the current MVP-1 path.

External package/repository scouting is deferred until implementation is actually approved because this task creates no runtime code and introduces no new dependency. Before implementation, the mandatory reuse check must confirm that no added package is needed beyond the existing Pydantic/JSON-Schema/runtime stack.

## Deterministic candidate-selection proposal

Select exactly one candidate using only non-PII selection criteria:

1. physical source order;
2. structurally conforming documented 14-field record;
3. exact Property Type Code `IN03`;
4. Property Owner Count exactly `1`;
5. Property ID non-empty;
6. stop at first eligible record.

Forbidden:

- ranking by owner name or address;
- random choice;
- commercial cherry-picking;
- scoring by inferred wealth/value;
- selecting more than one candidate.

Reason: this creates a reproducible one-case sample, avoids selection on owner PII, reduces multi-owner ambiguity and minimizes user/manual work.

## Minimum field scope

Transient-only fields proposed:

- Property ID;
- Property Type Code;
- Property Owner Count;
- Owner Name;
- Holder Name;
- Holder Report Year.

Address fields are excluded from the initial scope.

Persistent output is non-owner-Pii only:

- case ID;
- source ID;
- source snapshot ref;
- source physical record ordinal;
- property type code;
- owner count;
- reported-by / holder context;
- reported-when / holder-report-year context;
- candidate state;
- value-evidence state.

Not persisted:

- raw row;
- Owner Name;
- Property ID;
- address fields;
- owner-row hash;
- owner-field values in logs.

The case ID is proposed as a deterministic UUID5 derived from source ID + source snapshot + physical record ordinal + `IN03`, explicitly excluding owner PII.

## Value-evidence boundary

The current NY Owner Name File contract says the source does not disclose dollar value.

The existing pre-contact economics component therefore remains authoritative:

`UNKNOWN_PRE_CLAIM_REVIEW`

The proposal does not invent amount, fee basis or commercial threshold.

The bounded value objective is:

`OBTAIN_EVIDENCE_BACKED_VALUE_OR_PRESERVE_EXPLICIT_UNKNOWN_PRE_CLAIM_REVIEW`

If obtaining value would require an unapproved claim submission, identity resolution, beneficiary matching, outreach or additional PII scope, execution must stop and return the explicit blocker instead of expanding silently.

## Privacy / retention design

Default design is transient PII with same-session disposal.

No durable owner PII is introduced by this proposal.

The design deliberately avoids inventing a long-term PII retention duration. If a later workflow requires durable owner identity or address storage, that becomes a separate legal/privacy decision and is outside this proposal.

## Fail-closed conditions

The proposal explicitly stops on:

- stale/non-exact source listing;
- unsupported record shape;
- non-`IN03` classification;
- multi-owner candidate;
- missing Property ID;
- more than one selected candidate;
- any owner PII persistence/logging attempt;
- downstream demand for address fields;
- value research requiring unapproved claim/identity/beneficiary actions;
- unsupported/invented amount or fee assumptions.

## What this proposal does NOT authorize

It does not authorize:

- runtime implementation;
- source access;
- remote preflight;
- download;
- Owner Name File opening;
- owner PII processing;
- candidate materialization;
- value research;
- identity resolution;
- beneficiary matching;
- outreach;
- fee agreement;
- representation;
- claim activity.

## Future bounded path if approved

Before any real execution:

1. approve this offline proposal;
2. implement and review a synthetic-only one-candidate transient materialization path;
3. perform explicit legal/privacy review of the transient PII scope;
4. obtain fresh single-use local-file approval;
5. obtain fresh single-use transient-PII approval;
6. obtain fresh listing exact-match preflight;
7. obtain explicit one-candidate execution authorization;
8. obtain separate value-evidence research authorization.

No previous Attempt-11 approval is reusable.

## Review result

`READY_FOR_HUMAN_REVIEW_PROPOSAL_ONLY`

Required Product Owner phrase:

`APPROVE_NY_OSC_ONE_CANDIDATE_VALUE_EVIDENCE_OFFLINE_PROPOSAL`

Approval of that phrase must mean proposal review only. It must not be interpreted as authorizing implementation, source access, download, PII processing or value research.
