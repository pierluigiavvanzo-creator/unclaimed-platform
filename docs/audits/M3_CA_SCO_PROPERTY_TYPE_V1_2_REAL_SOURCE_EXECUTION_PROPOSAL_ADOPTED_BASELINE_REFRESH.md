# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution Proposal Adopted-Baseline Refresh

Date: 2026-09-17

Status: **PROPOSAL REFRESH IMPLEMENTED — REPOSITORY ONLY — HUMAN REVIEW REQUIRED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Action

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification: `A — Product Critical`.

## Product purpose

This closes the stale-proposal binding that prevented the already reviewed v1.2 semantic verification design from being safely reused after transport/archive-layout baseline adoption. It shortens the path to the first approved real source without reopening transport diagnostics.

## Authoritative base

- branch: `m3-ca-sco-transport-archive-layout-baseline-adoption`;
- HEAD: `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28`;
- CI: `35210199280` — **SUCCESS**;
- baseline adoption: complete;
- runtime contract: `1.2.0`;
- D-008 policy: `WHOLE_SOURCE_STOP`.

## Reuse decision

`REUSE` was selected over redesign.

The existing v1.2 proposal remains the design source. The refresh changes only the stale transport/archive-layout binding and current provenance. No external component is required for this repository-only contract refresh.

The historical proposal is intentionally preserved unchanged as provenance:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Refreshed proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`

## Refreshed binding

The proposal is now bound to:

- expected length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- canonical offsets `0`, `59745428`, `96861315`, `134172553`;
- current CI-green adopted-baseline checkpoint `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28` / CI `35210199280`.

A contract test compares these proposal values directly with the active semantic runner.

## Preserved design boundary

Unchanged:

- four canonical members;
- max 4 data rows/member and 16 total;
- max 1 HEAD, 4 Range and 5 HTTP requests;
- per-range/body/transient/logical-record byte caps;
- no additional range, full-body fallback, widening or automatic retry;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no trimming, uppercasing or normalization;
- parser/projector unchanged;
- D-008 fail-closed control disposition;
- memory-only transient-row privacy boundary;
- no row/value persistence or row-specific inspection;
- source policy `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Authorization state

All prior execution/privacy approvals remain consumed and non-reusable.

The refreshed proposal grants no approval. It explicitly requires fresh single-use execution and transient-row privacy approvals before any later source execution.

No network workflow is created by this task.

## Explicitly not performed

This task did not:

- request California SCO;
- perform HEAD or Range requests;
- access source-body bytes or real rows/fields;
- create or trigger a network workflow;
- grant/reuse execution or privacy approvals;
- change runtime code, parser/projector, regex or normalization;
- change D-008;
- activate source policy, registry, production classification or downstream case work.

## Decision-file assessment

No new architecture, product strategy or policy decision is introduced. `DECISIONS.md` remains unchanged.

## Next gate

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

That review may accept or reject only the refreshed proposal boundary. A PASS must not itself perform source access, create a network workflow, or grant/reuse approvals. Fresh authorization remains a separate gate.
