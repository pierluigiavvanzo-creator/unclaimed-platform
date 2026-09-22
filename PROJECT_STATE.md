# PROJECT_STATE.md

Last updated: 2026-09-22

## Authoritative product state

The project is in **PRODUCT VALIDATION MODE**.

Primary objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

Governance and source diagnostics are no longer roadmap objectives. They remain supporting controls and are frozen unless they directly block the real MVP-1 slice.

## Canonical integration branch

`main`

`main` is the canonical source-of-truth integration branch after the owner-authorized history-preserving reconciliation completed on 2026-09-22.

## Real-source readiness

NY OSC attempt 7 is the current real-source path.

Completed:

- synthetic RAW-literal runtime integration: IMPLEMENTED + REVIEWED PASS;
- real-capable authorization v1.3 / Gate 7 / runtime v1.4 / result v1.4: IMPLEMENTED + REVIEWED PASS;
- transient-local approval artifact: `GRANTED_NOT_CONSUMED`;
- transient-PII approval artifact: `GRANTED_NOT_CONSUMED`;
- both approvals are SINGLE_USE / NON_REUSABLE / ZERO RETRY;
- no source access or download has been performed under those grants.

Still ungranted/unperformed:

- fresh listing preflight authorization;
- fresh listing preflight receipt;
- final execution authorization;
- real download/execution;
- real candidate/economics/reviewer result.

## Current single next action

`HUMAN_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT_AUTHORIZATION`

Required exact Product Owner phrase:

`AUTHORIZE_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT`

That authorization is preflight-only. It must not be interpreted as download authority, owner-file-open authority or final execution authority.

## Product exit criteria

Current status:

- one authorized real source: IN PROGRESS;
- one bounded real acquisition: NOT DONE;
- real normalization/classification: NOT DONE;
- real candidate or documented zero-candidate full-pipeline result: NOT DONE;
- real provenance/evidence package: NOT DONE;
- reproducible real case economics: NOT DONE;
- reviewer case with human GO / REVISE / STOP: NOT DONE;
- commercial baseline: NOT DONE.

## Frozen until the real slice requires them

Do not prioritize:

- new source-diagnostic programs;
- new parser experiments;
- additional governance layers or micro-gates beyond legally/privacy-required controls;
- multi-state expansion;
- new agent frameworks;
- graph infrastructure;
- broad genealogy automation;
- UI polish unrelated to the first real reviewer result;
- refactors without direct MVP-1 value.

## Existing capabilities to reuse

- deterministic core and fail-closed policy/state/budget/audit controls;
- versioned machine contracts;
- NY OSC bounded real-capable runtime and Gate 7;
- synthetic MVP-1 vertical slice;
- FastAPI reviewer endpoints;
- Streamlit reviewer;
- candidate/economics/provenance contracts and tests.

After a successful bounded real acquisition, move directly downstream into the existing MVP-1 product slice rather than opening another source-diagnostic phase unless the real result proves a concrete blocker.
