# M3 California SCO — MVP-1 PROPERTY_TYPE Row-Defer Live Validation Authorization

Date: 2026-09-17

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — FRESH SINGLE-USE EXECUTION + TRANSIENT-ROW PRIVACY GRANTED — NOT YET CONSUMED**

## Authorization gate

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION`

## Owner authorization

The Product Owner explicitly authorized:

`APPROVO D010 LIVE VALIDATION + TRANSIENT-ROW PRIVACY`

This authorization is limited to exactly one bounded live validation of D-010 using:

`scripts/ca_sco_mvp1_property_type_validation.py`

## Authoritative base

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- base branch: `mvp1-ca-property-type-authority-row-defer`;
- base HEAD: `a15346a95cc293a1db3cd849b852d5be8846538d`;
- base CI: `35234190191` — SUCCESS;
- decision: `D-010 — ROW_DEFER_CONTINUE_METADATA_ONLY`;
- runner blob: `8e952a80105d56a8e84e6fb9feb5524dd01625d0`;
- classifier blob: `05e8637e42070dd6f04218592d20d4a230ab948e`;
- policy blob: `840d09d87187c53d26f4d562527dcb92d810a9f3`.

## Fresh single-use approval references

Execution:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_BOUNDED_B2AF7877`

Transient-row privacy:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_TRANSIENT_ROW_PRIVACY_BOUNDED_B2AF7877`

Machine authorization artifact:

`sources/evidence/ca_sco_mvp1_property_type_row_defer_live_validation_approval.v1.json`

Both approvals are `single_use=true`, `reusable=false`, and authorize no retry.

## Authorized execution boundary

Maximum live-source use:

- HEAD: `1`;
- Range GET: `4`;
- HTTP total: `5`;
- bytes per Range: `131072`;
- response-body bytes total: `524288`;
- sampled data rows: `4/member`, `16` total;
- no full-body fallback;
- no additional Range request;
- no retry/rerun under these refs.

## Privacy boundary

Permitted persistence is limited to derived, non-row-bearing evidence already defined by D-010, including:

- aggregate deferred-row count;
- aggregate row/category counters;
- exact authority-backed insurance code set observed in the bounded sample;
- transport/request counters and control status.

Forbidden persistence remains:

- raw body or full row;
- malformed `PROPERTY_TYPE` value or derivative;
- per-row `PROPERTY_TYPE`;
- `PROPERTY_ID`;
- owner/holder values;
- row/field hash or exact length;
- source-derived free text;
- row-specific human inspection material.

## Execution lifecycle requirement

The execution workflow must:

1. verify the exact authorized runner/classifier/policy blobs;
2. reject `run_attempt != 1` before network access;
3. consume both approvals before the first network request;
4. perform exactly one bounded D-010 live validation;
5. persist only the allowed derived evidence;
6. remove the temporary execution workflow/trigger after the run;
7. mark both approvals `CONSUMED_SINGLE_USE_NON_REUSABLE` regardless of semantic outcome once network access begins.

This authorization does not itself approve the California source for production, activate registry/classification, create a candidate, perform identity/genealogy matching, outreach or claim work.
