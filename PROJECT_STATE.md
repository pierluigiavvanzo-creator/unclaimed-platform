# PROJECT_STATE.md

Last updated: 2026-09-22

## Authoritative product state

The project is now in **PRODUCT VALIDATION MODE**.

Primary objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

Governance and source diagnostics are no longer roadmap objectives. They remain supporting controls and are frozen unless they directly block the real MVP-1 slice.

## Canonical integration branch

`main`

This work package performs the owner-authorized history-preserving reconciliation of the previously divergent `main` history with the verified development line.

Pre-reconciliation state:

- `main`: `b5a27ff1428b969286c798cc52385ced9fc59eda`;
- verified product branch: `ny-osc-seventh-transient-local-approval-grant-offline`;
- verified branch HEAD: `4cd3070a35bed3822922811422302aa145f37c34`;
- verified CI: `35692570391 — SUCCESS`;
- compare: product branch 675 commits ahead / 6 behind `main`;
- the six `main`-only commits have no net tree delta versus the common ancestor, so reconciliation is history-preserving rather than a choice between competing product trees.

## Real-source readiness

NY OSC attempt 7 is the current real-source path.

Completed:

- real-capable authorization v1.3 / Gate 7 / runtime v1.4 / result v1.4: IMPLEMENTED + REVIEWED PASS;
- transient-local approval artifact: GRANTED_NOT_CONSUMED;
- local approval semantics: SINGLE_USE / NON_REUSABLE / ZERO RETRY;
- no source access or download has been performed under that grant.

Still ungranted/unperformed:

- transient-PII approval;
- fresh listing preflight;
- final execution authorization;
- real download/execution;
- real candidate/economics/reviewer result.

## Current single next action

`HUMAN_NY_OSC_SEVENTH_TRANSIENT_PII_AUTHORIZATION`

Required exact Product Owner phrase:

`APPROVO NY OSC OWNER NAME FILE SEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE`

That approval must remain separate from preflight, download and final execution authority.

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

The next engineering work after a successful real acquisition should connect the real output to these existing product components rather than expand source governance.
