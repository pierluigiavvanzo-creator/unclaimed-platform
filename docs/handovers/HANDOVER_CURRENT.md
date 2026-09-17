# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ny-osc-request-submitted`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Canonical Read Order

Before any new change read, in order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

## California Path

Latest California live run:

`35255228459` — attempt `1` — SUCCESS.

Result:

- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- source response bytes: `524288`;
- no stop.

California source remains `HELD / NOT YET APPROVED`, not rejected. The current CA SCO `PROPERTY_TYPE` discovery path is frozen for MVP-1 absent genuinely new evidence. Consumed CA approvals are non-reusable.

## New York Source Selection / Offline Contract

Selected candidate:

`New York Office of the State Comptroller — Owner Name File`

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

Offline source-contract/privacy package:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

Implementation base checkpoint:

`198821ff41abb103b6c56876a075abb6c28c9c8f`

Base CI:

`35258809399` — SUCCESS.

Source remains:

`REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`

Physical schema remains `UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE`; production parser/classification remains inactive.

## Gate 1 — Request Access Only

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

Machine evidence:

`sources/evidence/ny_osc_owner_name_file_request_link_authorization.v1.json`

Current approval state:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Single-use: yes. Reusable: no. Retry authorized: no.

### Submission evidence

On 2026-09-17 the Product Owner explicitly confirmed in chat that the official OSC Owner Name File request form had been manually submitted once.

This repository records that Product Owner attestation. The external submission was not independently verified by repository tooling, and the exact external submit timestamp is not independently known.

Requester contact values are intentionally not persisted in GitHub.

### Gate 1 scope after consumption

Gate 1 is exhausted and cannot be reused. It does not authorize any additional request submission or retry.

Gate 1 never authorized and still does not authorize:

- Owner Name File download;
- processing of owner name/address or other real owner PII;
- raw file persistence;
- schema parsing;
- identity resolution;
- beneficiary matching;
- outreach;
- representation;
- fee agreement;
- claim activity.

## External Dependency — OSC Access Instructions

OSC states that after receiving the request it will email a secure FTP link and instructions for downloading a zipped delimited `.txt` file.

Current state:

- request submitted: yes, Product Owner confirmed;
- access instructions received: no;
- Owner Name File downloaded: no;
- real owner PII processed: no.

No polling or retry is authorized by the consumed Gate 1 approval.

## Gate 2 — Later Bounded First Download

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

State:

`NOT GRANTED / NOT READY`

Before requesting Gate 2:

1. receive OSC access instructions;
2. determine observable access/download constraints without processing Owner Name File contents;
3. define explicit `max_download_bytes`;
4. prepare a separately reviewed bounded first-download/transient-PII proposal.

No default byte cap may be invented.

When later separately authorized, Gate 2 may cover exactly one bounded download plus memory-only schema discovery with transient owner PII. It remains single-use, non-reusable and no retry/rerun is implicitly authorized.

## Source / Product State

- approved real sources: `0`;
- California source: `HELD`;
- CA `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- NY OSC Owner Name File: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: `CONSUMED / NON-REUSABLE`;
- NY request submitted: yes, Product Owner confirmed manual submission;
- NY access instructions obtained: no;
- NY real owner PII processed: no;
- NY Gate 2: not granted;
- production parser/classification: inactive;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`AWAIT_NY_OSC_ACCESS_INSTRUCTIONS`

Classification: `A — Product Critical / External Dependency`.

When the OSC email/access instructions arrive, provide or expose only the access instructions needed to determine non-content download constraints. Do not download or inspect the Owner Name File and do not process owner PII under the consumed Gate 1 approval.

After those non-content constraints are known, prepare the separate Gate 2 bounded first-download/transient-PII authorization proposal with an explicit `max_download_bytes`.
