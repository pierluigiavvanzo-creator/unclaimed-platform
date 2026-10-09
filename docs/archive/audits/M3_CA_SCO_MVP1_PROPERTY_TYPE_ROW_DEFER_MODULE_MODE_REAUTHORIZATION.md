# M3 California SCO — MVP-1 PROPERTY_TYPE D-010 Module-Mode Reauthorization

Date: 2026-09-17

Status: **HUMAN/OWNER REAUTHORIZATION COMPLETED — FRESH SINGLE-USE EXECUTION + TRANSIENT-ROW PRIVACY GRANTED — NOT YET CONSUMED**

## Gate

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_REAUTHORIZATION_AFTER_PRENETWORK_CLI_REMEDIATION`

## Owner authorization

`APPROVO FRESH D010 MODULE-MODE LIVE VALIDATION + TRANSIENT-ROW PRIVACY`

This authorization grants exactly one bounded D-010 live validation after the prior pre-network CLI-launch failure.

## Fresh refs

Execution:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_REAL_SOURCE_VALIDATION_BOUNDED_C6D79506`

Transient-row privacy:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_MODULE_MODE_TRANSIENT_ROW_PRIVACY_BOUNDED_C6D79506`

Machine record:

`sources/evidence/ca_sco_mvp1_property_type_row_defer_live_validation_approval.v2.json`

Both refs are single-use, non-reusable, and authorize no retry.

## Binding checkpoint

- base branch: `mvp1-ca-property-type-row-defer-live-validation-once`;
- base HEAD: `3d697efc4612fac070014d81767985ad8300af3f`;
- base CI: `35238612548` — SUCCESS;
- execution branch: `mvp1-ca-property-type-row-defer-live-validation-module-once`.

Pinned code:

- D-010 runner blob: `8e952a80105d56a8e84e6fb9feb5524dd01625d0`;
- classifier blob: `05e8637e42070dd6f04218592d20d4a230ab948e`;
- policy blob: `840d09d87187c53d26f4d562527dcb92d810a9f3`;
- legacy transport/archive runner blob: `706183d5425da16b25f8186574cc356135803326`.

## Required invocation

The one-shot execution must run from repository root using:

`python -m scripts.ca_sco_mvp1_property_type_validation`

Direct file execution is not authorized for this run.

## Bounds

Maximum source use:

- HEAD: `1`;
- Range GET: `4`;
- HTTP total: `5`;
- bytes per Range: `131072`;
- source response-body bytes total: `524288`;
- rows: `4/member`, `16` total;
- no retry;
- no widening;
- no full-body fallback;
- no extra ranges.

## Privacy

Allowed persistence is limited to the existing D-010 derived evidence boundary, including aggregate deferred-row count, aggregate row/category counters, authority-backed insurance codes observed, request counters, transport verification and control outcome.

Forbidden persistence remains raw body/rows, malformed source value or derivative, per-row `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder fields, row-specific hashes/lengths/free text, identity/genealogy/beneficiary matching, outreach or claim work.

## Lifecycle

The one-shot workflow must:

1. verify exact branch ancestry and pinned blobs;
2. verify module-mode CLI startup offline before network;
3. reject `GITHUB_RUN_ATTEMPT != 1`;
4. consume both fresh refs before first source request;
5. execute exactly one bounded D-010 live validation;
6. validate that only privacy-safe derived evidence exists;
7. upload/persist only that derived evidence;
8. remove temporary workflow/trigger after the attempt;
9. never reuse the consumed refs regardless of semantic outcome.

This reauthorization does not itself approve the California source or activate production classification.
