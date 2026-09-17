# M3 California SCO — MVP-1 PROPERTY_TYPE Row-Defer Live Validation Authorization

Date: 2026-09-17

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — APPROVALS CONSUMED — LIVE RUN ABORTED BEFORE SCO NETWORK ACCESS — NON-REUSABLE**

## Authorization gate

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION`

## Owner authorization

The Product Owner explicitly authorized:

`APPROVO D010 LIVE VALIDATION + TRANSIENT-ROW PRIVACY`

The authorization was limited to exactly one bounded live validation of D-010.

## Authoritative base

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- base branch: `mvp1-ca-property-type-authority-row-defer`;
- base HEAD: `a15346a95cc293a1db3cd849b852d5be8846538d`;
- base CI: `35234190191` — SUCCESS;
- decision: `D-010 — ROW_DEFER_CONTINUE_METADATA_ONLY`;
- authorized runner blob: `8e952a80105d56a8e84e6fb9feb5524dd01625d0`;
- classifier blob: `05e8637e42070dd6f04218592d20d4a230ab948e`;
- policy blob: `840d09d87187c53d26f4d562527dcb92d810a9f3`.

## Fresh single-use approval references

Execution:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_BOUNDED_B2AF7877`

Transient-row privacy:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_TRANSIENT_ROW_PRIVACY_BOUNDED_B2AF7877`

Machine authorization artifact:

`sources/evidence/ca_sco_mvp1_property_type_row_defer_live_validation_approval.v1.json`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry or reuse is authorized.

## Attempt lifecycle

- authorization checkpoint: `17ec4183726844593c02d442516aef92bf07916c`;
- authorization-checkpoint CI: `35237433309` — SUCCESS;
- execution branch: `mvp1-ca-property-type-row-defer-live-validation-once`;
- trigger commit: `6ea068cf24878482ed89ce9af2794461d3b705a9`;
- one-shot workflow run: `35237721059`, attempt `1`;
- preflight: PASS;
- approval consumption: PASS;
- approval-consumption commit: `49f7e417ca0469f2a3a4e59aecb3d013376f9016`;
- live validation step: FAILED before transport construction;
- evidence validation/upload: skipped because the live step did not produce an execution artifact.

## Failure classification

The process terminated during Python module import:

`ModuleNotFoundError: No module named 'scripts'`

The failing statement was the top-level import in `scripts/ca_sco_mvp1_property_type_validation.py`. Because the module failed to import before `main()` ran, `legacy.HttpTransport()` was never constructed and no `HEAD` or `Range GET` to `claimit.ca.gov` was issued by this attempt.

Therefore:

- California SCO source requests performed by run `35237721059`: `0`;
- California SCO source response-body bytes read: `0`;
- real source rows examined: `0`;
- semantic result about live `PROPERTY_TYPE`: **none**;
- this failure is an execution-packaging/CLI-startup defect, not evidence against D-010 or the California source.

## Remediation

The direct-script startup defect was corrected after the consumed attempt by explicitly making the repository root importable before importing the `scripts` namespace.

A subprocess regression test now invokes the runner exactly as GitHub Actions did:

`python scripts/ca_sco_mvp1_property_type_validation.py --help`

This test is offline and performs no source access. The correction does not change D-010 semantics, the classifier, the authority vocabulary, transport/archive constants, request/sample caps, privacy rules, or source activation state.

## Authorized execution boundary (consumed, not reusable)

The consumed authorization had permitted at most:

- HEAD: `1`;
- Range GET: `4`;
- HTTP total: `5`;
- bytes per Range: `131072`;
- response-body bytes total: `524288`;
- sampled data rows: `4/member`, `16` total;
- no full-body fallback;
- no additional Range request;
- no retry/rerun under these refs.

None of the source-access allowance was exercised because execution failed before transport construction. This does **not** restore or recycle the consumed approval references.

## Privacy result

PASS for the failed attempt.

No source content was accessed or persisted. No raw body, row, `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder value, hash, exact length, source-derived free text, identity resolution, beneficiary matching, outreach or claim work occurred.

## Product/source state

This attempt does not approve or reject the California source and provides no new live semantic evidence. D-010 remains the selected source-specific remediation design and its synthetic tests remain valid. A new real validation requires a **fresh explicit Product Owner authorization** and fresh single-use execution/privacy references after the CLI-startup remediation is CI-green.
