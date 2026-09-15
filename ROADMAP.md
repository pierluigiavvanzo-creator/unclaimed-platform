# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` RUNNER IMPLEMENTATION CANDIDATE + SYNTHETIC/MOCK CI VERIFIED — REAL EXECUTION BLOCKED | Candidate `d2b8977a...`; CI `34951460475` SUCCESS; workflow absent; policy `PROPOSED`; registry disabled |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; Vercel runtime integration decommissioned |

## Completed M3 readiness work

- California source/legal inventory complete.
- A01 contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` transport and bounded structure evidence canonicalized.
- Four CSV members and identical 25-label header verified with zero data rows sampled.
- First-purpose persisted scope reduced to `PROPERTY_ID` + `PROPERTY_TYPE`.
- `HOLDER_NAME` and identity/address fields prohibited for first triage.
- Transient CSV prohibited-field exposure isolated as a separate privacy boundary.
- `PROPERTY_TYPE` semantic-verification proposal canonical + CI verified.
- Bounded semantic runner design and execution evidence contract canonical + CI verified.
- Bounded runner implementation completed on isolated candidate and validated only with synthetic/mock transport.

## Current Candidate

Branch:
`m3-ca-sco-property-type-runner-implementation`

Functional HEAD before audit/docs closure:
`d2b8977a0fd34474ecb545c6ecfefc354b551b30`

Functional CI:
`34951460475` — SUCCESS.

At functional closure:
- ahead `3`;
- behind `0`;
- merge-base exactly canonical `6105c22a7d31df7afca00282eff7e9798e98b868`.

## Implementation Gate

Owner authorization:
`approvo implementazione bounded runner PROPERTY_TYPE con soli test synthetic/mock`

Allowed:
- runner implementation;
- synthetic/mock testing.

Still prohibited:
- real network execution;
- one-shot network workflow;
- real SCO row access;
- transient-row privacy exposure;
- source approval/registry activation.

## Implemented Runner

Path:
`scripts/ca_sco_property_type_semantic_verification.py`

The runner preserves the canonical sampling and transport budgets and is transport-injectable for offline/mock tests.

Network workflow remains absent:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`.

## Fixed Safety Caps

- 4 members;
- 4 rows/member;
- 16 rows total;
- 1 HEAD;
- 4 Range GET;
- 5 HTTP requests total;
- 131,072 body bytes/Range;
- 524,288 body bytes total;
- 262,144 uncompressed transient bytes/member;
- 1,048,576 uncompressed transient bytes total;
- 32,768 bytes/logical record;
- no additional Range;
- no full-body fallback;
- no automatic cap widening.

Ignored Range/non-206 causes STOP before the unexpected body is consumed.

## Synthetic / Mock Test Coverage

- official insurance code sample -> compatible success;
- no insurance code -> inconclusive;
- unknown `IN` code -> fail closed;
- non-206 Range -> stop without body read;
- header mismatch -> fail closed;
- row column-count mismatch -> fail closed;
- missing execution/privacy approval -> fail before transport;
- execution evidence remains derived-summary only;
- live CLI path is explicit opt-in;
- network one-shot workflow remains absent.

Final CI `34951460475` passed Ruff, mypy, contract, smoke, full pytest, frontend lint/typecheck/build, and Streamlit smoke.

## Current Safety State

- source policy `PROPOSED`;
- real acquisition false;
- registry disabled/unapproved;
- approved real sources `0`;
- runner implementation authorized only for synthetic/mock;
- real semantic execution false;
- transient-row privacy approval absent;
- CSV real-row access BLOCKED;
- PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

No new SCO network/body access occurred during runner implementation.

## Next Product Work

1. Human decision on `HUMAN_PROPERTY_TYPE_RUNNER_CANDIDATE_PROMOTION`.
2. If approved, fast-forward `m3-ca-sco-property-type-runner-implementation` into `m2-state-governance-core` after ancestry verification.
3. Verify canonical CI after promotion.
4. Keep network workflow absent and real execution blocked.
5. Actual bounded SCO row sampling requires a later separate explicit execution approval **plus** transient-row privacy approval.
6. Source approval/registry activation, A02 normalization, identity, matching and outreach remain later independent gates.

## Out of Scope Until Later Gates

- real semantic sampling now;
- any real CSV row read;
- creation/execution of the one-shot network workflow;
- automatic budget widening;
- full-body fallback;
- source approval or registry activation;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
