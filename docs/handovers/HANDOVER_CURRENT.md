# HANDOVER_CURRENT.md

Last updated: 2026-09-23

## AUTHORITATIVE CURRENT STATE — PRODUCT VALIDATION MODE

Repository: `pierluigiavvanzo-creator/unclaimed-platform`

Canonical integration branch: `main`

Objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

## Consumed real attempts relevant to current state

### Attempt 9

Consumed/non-reusable/zero-retry whole-file structural scan.

Authoritative evidence:

`sources/evidence/ny_osc_owner_name_file_ninth_attempt_execution_result.v1.json`

Key aggregate result: `14994489` physical records, terminal-empty-field hypothesis rejected, no owner/raw values returned.

### Attempt 10

Consumed/non-reusable/zero-retry.

Authoritative evidence:

`sources/evidence/ny_osc_owner_name_file_tenth_attempt_execution_result.v1.json`

Result:

- status `BLOCKED`;
- reason `AUTHORIZED_DOWNLOAD_START_OUTSIDE_FRESH_PREFLIGHT_WINDOW`;
- manual download had occurred;
- classification/product slice never started;
- no candidate/zero-candidate result;
- no owner values returned.

Root cause: Gate 10 captured the download-start marker only after the Product Owner pressed Enter, and that marker landed outside the 900-second fresh-preflight window.

Do not reuse any Attempt-10 grant.

## Attempt 11 offline package

Branch:

`mvp1-ny-eleventh-auto-start-detection-offline`

PR:

`#29`

Proposal checkpoint:

`270de2f6e79b7c654052519adc446fe76b811771`

Runner/code checkpoint:

`ce005f08a3bbd23eb8fac6088917109f7864e924`

CI:

`35834948309 — SUCCESS`

All Python quality/tests, Streamlit checks and frontend lint/typecheck/build passed.

Purpose:

`REAL PHYSICAL RECORDS -> STRUCTURAL DEFER/ACCEPT -> PROPERTY TYPE CODE -> INSURANCE CLASSIFICATION -> AGGREGATE CANDIDATE OR ZERO-CANDIDATE -> ECONOMIC ACTIONABILITY`

The Attempt-10 product slice is reused unchanged.

Gate 11 freshness remediation:

- minimum `180` freshness seconds remaining before download instruction;
- new dedicated empty temp directory;
- automatic detector armed before operator download instruction;
- `100 ms` polling;
- first observed non-empty file in the dedicated directory captures the UTC download-start marker;
- no operator Enter is used to mark transfer start;
- no detected start before deadline -> fail closed;
- one manual completion confirmation after the same download finishes;
- one download / one Gate 11 execution / zero retry;
- no direct network client.

Product boundary remains:

- exactly `13` pipes -> classify documented 14-field record;
- all other shapes -> metadata-only defer;
- only Property Type Code index `1` is buffered/decoded;
- exact existing authority-backed insurance vocabulary;
- `IN03` primary target;
- aggregate result only;
- no candidate/owner PII materialization;
- economics remain `UNKNOWN_FROM_SOURCE`.

No NY OSC source access, preflight, download or real PII processing occurred during Attempt-11 offline preparation.

## SINGLE NEXT ACTION

Request the first two Attempt-11 grants together:

`APPROVO NY OSC ELEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE`

`APPROVO NY OSC OWNER NAME FILE ELEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE`

Only after those are registered may a separate fresh-preflight authorization be requested. Final execution authorization remains another separate gate.

## Expected real Attempt-11 output

Only non-owner aggregate product metrics:

- total records;
- structurally conforming/deferred counts;
- authority-backed insurance count;
- aggregate primary `IN03` candidate count;
- other insurance count;
- no-authority-match/unclassifiable counts;
- candidate-present or documented zero-candidate outcome;
- fail-closed economic actionability state.

If candidates are present, next step is evidence/value/economics required for reviewer actionability. If zero candidates, record the real zero-candidate result and reassess source/product fit.

## Safety boundaries

Attempt 11 does not authorize source activation, candidate PII persistence, identity resolution, beneficiary matching, outreach, fee agreement, representation or claim activity.

## Git health

`main` remains canonical. PR #29 is open and not merged. No merge is authorized.
