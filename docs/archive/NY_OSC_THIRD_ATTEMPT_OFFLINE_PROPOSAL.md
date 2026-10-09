# NY OSC Third Bounded Attempt — Offline Proposal

Date: 2026-09-18

Classification: `A — Product Critical / Human Authorization Gate`

Status: `PROPOSED_NOT_AUTHORIZED / REPOSITORY_ONLY / ZERO_SOURCE_ACCESS`

## Purpose

Define the smallest bounded proposal that could permit a separately authorized third NY OSC
Owner Name File schema-discovery attempt after the second attempt stopped fail-closed.

This artifact is a proposal only. It does not grant execution, transient-local retention,
transient-PII processing, portal access, or a download.

## Verified starting point

- integrated repair branch: `mvp1-ny-second-attempt-approved-ready-execution`;
- integrated merge checkpoint: `85d5f0c1101e5d66add27b9e1f445e7bba54a3b0`;
- repair head: `fc6f159d4569989aeaa57028089de0c0b32f2f41`;
- pull request: `#2`;
- verification CI: `35381899112 — SUCCESS`;
- verified jobs: `quality`, `streamlit-candidate`.

No real owner file was used to create or verify the repair.

## Second-attempt final state

The second attempt is consumed and non-reusable:

- execution result: `BLOCKED / UNEXPECTED_DATA_FIELD_COUNT`;
- transient-local approval: consumed, single-use, non-reusable;
- transient-PII approval: consumed, single-use, non-reusable;
- retry under those approvals: forbidden;
- raw ZIP: logically deleted;
- physical secure erasure: not claimed;
- owner values persisted or returned: none.

## Proposed third-attempt bounds

The proposal does not widen the prior envelope:

- downloads maximum: `1`;
- retries maximum: `0`;
- compressed bytes maximum: `450,000,000`;
- uncompressed bytes maximum: `2,000,000,000`;
- archive members maximum: `1`;
- text members required exactly: `1`;
- documented structural fields: `14`;
- delimiter: pipe;
- automatic widening: forbidden;
- automatic retry: forbidden.

## Privacy boundary

If separately authorized later, the proposal would allow only transient processing required
for deterministic schema discovery. It would continue to forbid durable raw persistence,
repository/cloud/chat copies, owner-row persistence, owner-field logging, row-specific human
inspection, identity resolution, beneficiary matching, outreach, representation, fee
agreements, and claim activity.

Only derived non-PII structural metadata may be persisted.

## Required future gates

Before any implementation can become executable:

1. the Product Owner must review this proposal;
2. two new, attempt-specific approval artifacts must be created only after explicit approval;
3. neither second-attempt approval or runner may be reused;
4. the third-attempt runner must be independently verified by CI;
5. the remote listing must be freshly checked immediately before execution;
6. any listing drift stops before download and requires a refreshed proposal.

The approval phrases defined in the machine proposal are not granted by the instruction to
prepare this offline proposal.

## Work performed

Repository-only work:

- proposal JSON;
- strict proposal schema;
- contract tests;
- project-state, roadmap, handover, and changelog updates.

No portal access, network request to NY OSC, source download, file opening, or owner-PII
processing occurred.
