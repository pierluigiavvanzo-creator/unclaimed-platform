# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ny-osc-request-link-authorization`

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

Product Owner authorization received on 2026-09-17:

`APPROVO NY OSC OWNER NAME FILE REQUEST-LINK ONLY`

Machine evidence:

`sources/evidence/ny_osc_owner_name_file_request_link_authorization.v1.json`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

Current approval state:

`GRANTED_SINGLE_USE_NOT_CONSUMED_PENDING_REQUESTER_CONTACT_DATA`

Single-use: yes. Reusable: no. Retry authorized: no.

### Gate 1 authorized scope

May perform exactly one official OSC Owner Name File request submission for the purpose of receiving access instructions / secure FTP link information.

May disclose the requester contact data only when those values are explicitly supplied for this request.

Gate 1 does NOT authorize:

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

Do not mark the approval consumed until the request has actually been submitted.

## Current External Form Facts

Official form:

`https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form`

The form currently requires exactly these requester contact values:

- Name;
- Company;
- Phone number;
- Email address.

OSC states that after receiving the request it will email a secure FTP link and instructions for downloading a zipped delimited `.txt` file.

The authorization message did not supply the four requester contact values. They must not be inferred from memory, Git metadata, account profile, prior conversations or other sources; obtain them explicitly from the Product Owner for this external disclosure.

No OSC form has been submitted yet. The Gate 1 approval remains unconsumed.

## Gate 2 — Later Bounded First Download

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

State:

`NOT GRANTED / NOT READY`

Before requesting Gate 2:

1. submit the authorized Gate 1 request;
2. receive access instructions;
3. determine observable download constraints without processing owner-file contents;
4. define explicit `max_download_bytes`.

No default byte cap may be invented.

When later separately authorized, Gate 2 may cover exactly one bounded download plus memory-only schema discovery with transient owner PII. It remains single-use, non-reusable and no retry/rerun is implicitly authorized.

## Source / Product State

- approved real sources: `0`;
- California source: `HELD`;
- CA `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- NY OSC Owner Name File: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: `GRANTED / NOT CONSUMED`;
- NY request submitted: no;
- NY access instructions obtained: no;
- NY real owner PII processed: no;
- NY Gate 2: not granted;
- production parser/classification: inactive;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`COLLECT_NY_OSC_REQUESTER_CONTACT_INPUTS_FOR_AUTHORIZED_REQUEST`

Classification: `A — Product Critical / Human Input Dependency`.

Required explicit Product Owner inputs:

1. Name
2. Company
3. Phone number
4. Email address

After all four values are supplied, use Gate 1 approval ref `OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71` for exactly one official request submission if an execution-capable browser/form surface is available. If the current chat surface cannot perform form submission, provide the official form and exact values to enter rather than claiming submission occurred.

After actual submission, mark Gate 1 consumed and update canonical state. Do not download the Owner Name File under Gate 1.
