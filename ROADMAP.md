# ROADMAP.md

Last updated: 2026-09-22

## Product validation critical path

The roadmap is intentionally narrow:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

No broad platform expansion is scheduled before this is complete.

## Stage 1 — Complete authorization for one real source

Current source path: NY OSC attempt 7.

Done:

- synthetic RAW-literal integration implemented and reviewed PASS;
- real-capable package reviewed PASS;
- local transient-retention approval granted and unconsumed;
- transient-PII approval granted and unconsumed.

Next:

`HUMAN_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT_AUTHORIZATION`

Required phrase:

`AUTHORIZE_NY_OSC_SEVENTH_FRESH_LISTING_PREFLIGHT`

Then, as separate gates only:

1. perform the fresh listing preflight;
2. require an `EXACT_MATCH` receipt within the configured freshness window;
3. obtain final single-use execution authorization.

Exit criterion: all legally/privacy-required execution prerequisites are satisfied without inferring one gate from another.

## Stage 2 — One bounded real execution

Use the existing reviewed Gate 7 package.

Constraints:

- one manual download maximum;
- zero retries;
- dedicated OS-temp file;
- documented byte/archive caps;
- no direct network client in Gate 7;
- `DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`;
- fail closed on unsupported structure;
- logical deletion after execution;
- no owner values/raw path in result artifacts.

Exit criterion: one real execution result exists, or a bounded documented failure provides a specific blocker that directly prevents the product slice.

## Stage 3 — Immediate downstream product slice

On successful acquisition, move directly to:

`real mapping -> normalization -> insurance classification -> candidate case -> provenance/evidence -> case economics -> reviewer`

Reuse the existing synthetic MVP-1 path and contracts. Do not create another source-diagnostic program unless the real result proves it necessary.

Exit criterion: at least one real reviewer case, or a documented zero-candidate full-pipeline result.

## Stage 4 — Economic baseline

Capture:

- records examined;
- records surviving insurance classification;
- candidates produced;
- candidate-to-review conversion;
- automated cost/candidate;
- source cost/candidate where applicable;
- human review time/candidate;
- recoverable value/value band where evidentially supportable;
- fee/revenue basis where legally supportable;
- unresolved/manual research burden;
- main drop-off reasons.

Exit criterion: one reproducible economic result visible to the Product Owner.

## Stage 5 — Product decision

Product Owner decision:

`GO / REVISE / STOP`

Only after this decision should the project consider multi-state expansion, graph infrastructure, broader agent automation, genealogy automation, additional source programs or major UI/infrastructure work.

## Frozen backlog before MVP-1

Unless a direct blocker is demonstrated:

- new governance layers;
- new source diagnostics;
- parser research beyond the active bounded execution;
- new agent frameworks;
- graph databases/evidence-graph infrastructure;
- multi-state expansion;
- broad genealogy automation;
- outreach/contracts/claims automation;
- non-critical UI polish;
- infrastructure refactors.

## Git health

`main` is the canonical integration branch. Verified product-critical milestone branches should return promptly to `main` after CI/review so product validation does not diverge into long-lived governance/source branches.
