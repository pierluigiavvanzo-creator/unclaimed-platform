# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`mvp1-ca-property-type-row-defer-live-validation-once`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## D-010 Product Boundary

Accepted California MVP-1 policy:

`ROW_DEFER_CONTINUE_METADATA_ONLY`

Exact authority-backed insurance vocabulary:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN08, IN99`

Primary narrow MVP-1 target:

`IN03 — Proceeds Due Beneficiaries`

A nonconforming or unknown `INxx` value is deferred without normalization, repair, semantic inference, row/value persistence or row-specific inspection. Only aggregate deferred-row counts may persist. Later rows may continue.

Transport/header/CSV-column/hard-cap failures remain whole-source fail-closed.

## Owner Authorization Just Used

The Product Owner explicitly authorized:

`APPROVO D010 LIVE VALIDATION + TRANSIENT-ROW PRIVACY`

Fresh refs minted from that authorization:

Execution:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_BOUNDED_B2AF7877`

Transient-row privacy:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_TRANSIENT_ROW_PRIVACY_BOUNDED_B2AF7877`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Do not reuse or rerun them.

Machine approval record:

`sources/evidence/ca_sco_mvp1_property_type_row_defer_live_validation_approval.v1.json`

Authorization/execution audit:

`docs/audits/M3_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION.md`

## Authorization Checkpoint

- base branch: `mvp1-ca-property-type-authority-row-defer`;
- base HEAD: `a15346a95cc293a1db3cd849b852d5be8846538d`;
- base CI: `35234190191` — SUCCESS;
- isolated execution branch: `mvp1-ca-property-type-row-defer-live-validation-once`;
- authorization checkpoint: `17ec4183726844593c02d442516aef92bf07916c`;
- authorization-checkpoint CI: `35237433309` — SUCCESS.

The authorization pinned:

- D-010 runner blob `8e952a80105d56a8e84e6fb9feb5524dd01625d0`;
- classifier blob `05e8637e42070dd6f04218592d20d4a230ab948e`;
- policy blob `840d09d87187c53d26f4d562527dcb92d810a9f3`;
- legacy transport/CSV runner blob `706183d5425da16b25f8186574cc356135803326`.

## One-Shot Attempt

Trigger commit:

`6ea068cf24878482ed89ce9af2794461d3b705a9`

Workflow run:

`35237721059` — attempt `1` — **FAILURE BEFORE SCO NETWORK ACCESS**.

Preflight passed. The workflow then consumed both approval refs before network access and pushed:

`49f7e417ca0469f2a3a4e59aecb3d013376f9016` — `governance: consume D010 single-use live approvals`

The live execution process failed immediately at module import:

`ModuleNotFoundError: No module named 'scripts'`

The failing workflow command used direct file execution:

`python scripts/ca_sco_mvp1_property_type_validation.py ...`

Because import failed before `main()` and before `legacy.HttpTransport()` construction, the attempt performed:

- SCO HEAD requests: `0`;
- SCO Range GET requests: `0`;
- SCO response-body bytes: `0`;
- live rows examined: `0`;
- live semantic outcome: none.

This is an execution-packaging/launch failure, not evidence against the California source or D-010.

No evidence artifact was uploaded because the live step did not reach execution.

## Remediation

The D-010 runner was restored byte-for-byte to the originally reviewed/authorized blob:

`8e952a80105d56a8e84e6fb9feb5524dd01625d0`

The correct operational launch mode is now:

`python -m scripts.ca_sco_mvp1_property_type_validation ...`

`tests/unit/test_ca_sco_mvp1_property_type_validation.py` contains an offline subprocess regression test that boots the runner with exactly that module-mode invocation and `--help`, so no source access occurs.

D-010 semantics, classifier, authority vocabulary, transport/archive baseline, request/sample caps and privacy boundary are unchanged.

The temporary one-shot workflow and trigger were removed together after the failed attempt, preventing accidental re-execution.

## Source / Product State

- adopted transport/archive baseline: CONFIRMED from prior bounded executions;
- California authority semantics: RESOLVED;
- D-010 row-defer semantics: OFFLINE IMPLEMENTED;
- D-010 runtime semantic blob: UNCHANGED;
- first D-010 authorized attempt: ABORTED PRE-NETWORK;
- current execution/privacy refs: none fresh;
- approved real sources: `0`;
- production classification: inactive;
- real MVP-1 candidate cases: `0`.

Do not infer any semantic result from run `35237721059` because it accessed no California source data.

## Canonical Read Order Before Any New Change

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION.md`;
2. `sources/evidence/ca_sco_mvp1_property_type_row_defer_live_validation_approval.v1.json`;
3. `policies/states/CA/ca_sco_property_type_classification.v1.json`;
4. `src/unclaimed_platform/adapters/sources/california_property_type.py`;
5. `scripts/ca_sco_mvp1_property_type_validation.py`;
6. `tests/unit/test_ca_sco_mvp1_property_type_validation.py`;
7. D-010 in `DECISIONS.md`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_REAUTHORIZATION_AFTER_PRENETWORK_CLI_REMEDIATION`

Classification: `A — Product Critical`.

A new explicit Product Owner authorization is required because `B2AF7877` was consumed and is non-reusable even though no SCO request was reached.

The fresh authorization may mint exactly:

1. one new single-use bounded execution approval;
2. one new single-use transient-row memory-only privacy approval.

The next one-shot workflow must:

- pin the unchanged D-010 runner/classifier/policy and adopted transport baseline;
- invoke the runner with `python -m scripts.ca_sco_mvp1_property_type_validation`;
- reject `run_attempt != 1`;
- consume fresh refs before source access;
- preserve existing request/byte/sample caps;
- persist only D-010 allowed derived evidence;
- remove workflow/trigger immediately after execution;
- never reuse or rerun consumed refs.

After fresh explicit authorization, proceed directly:

`one module-mode bounded live D-010 validation -> evidence/source decision -> if supported, bounded California insurance activation -> MVP-1 candidate -> economics -> reviewer`

Do not reopen generic transport or PROPERTY_TYPE diagnostics absent new contradictory evidence.
