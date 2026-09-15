# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | SECOND v1.1 REAL ATTEMPT EXECUTED ONCE; STOPPED FAIL-CLOSED ON DECODED SHAPE MISMATCH | run `34995672539`; schema `1.1.0`; stop `PROPERTY_TYPE_FORMAT_UNEXPECTED`; one-shot workflow removed |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; Vercel runtime integration decommissioned |

## Completed M3 Work

- California source/legal inventory complete.
- A01 acquisition contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` bounded transport and structure evidence canonicalized.
- Four CSV members and identical 25-label header verified.
- First-purpose persisted scope minimized.
- `PROPERTY_TYPE` semantic proposal, runner design and synthetic/mock implementation CI verified.
- Historical first owner-authorized real semantic attempt executed once and stopped fail-closed under schema v1.0.0.
- Offline diagnosis established that v1.0 conflated invalid UTF-8 and decoded shape mismatch.
- v1.1 diagnostic remediation implemented, reviewed and promoted to canonical.
- Second bounded execution proposal prepared and CI verified.
- Second proposal human review: PASS.
- Fresh second-run execution/privacy authorization package CI verified.
- Second owner-authorized bounded real semantic attempt executed exactly once.
- Second evidence validated against schema v1.1.0 and hard caps.
- Second one-shot workflow removed immediately after the run.
- Workflow logs verified to contain no source row or `PROPERTY_TYPE` values.

## First Real Semantic Attempt — Historical

Run `34965097988`; schema `1.0.0`; result `STOPPED_FAIL_CLOSED`; stop
`PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Actual budget: 1 HEAD; 1 Range GET; 2 HTTP requests; 131072 source-body bytes;
0 accepted/examined rows; no retry; no widening.

Its root cause remains unresolved because v1.0 did not distinguish encoding
failure from decoded-shape failure.

## Second Real Semantic Attempt — v1.1

Run: `34995672539`  
Execution SHA: `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`  
Result: `STOPPED_FAIL_CLOSED`  
Stop: `PROPERTY_TYPE_FORMAT_UNEXPECTED`

Actual budget: 1 HEAD; 1 Range GET; 2 HTTP requests; 131072 source-body bytes;
0 accepted/examined rows; no retry; no widening.

v1.1 interpretation:
- not the invalid-UTF-8 stop class;
- successfully decoded, non-empty projected `PROPERTY_TYPE`;
- failed unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

This is diagnostic progress, not source compatibility. The offending source
value remains intentionally unknown/unpersisted.

Fresh second-run execution and privacy approvals are CONSUMED and cannot be
reused.

One-shot workflow steady state: ABSENT.  
Workflow-removal SHA: `d6e83a44b2069a2fa746c09d1ae33622654e5d43`.

## Current Safety State

- stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- canonical development branch: `m2-state-governance-core`
- source policy: `PROPOSED`
- real acquisition authorization: false
- registry: disabled/unapproved
- approved real sources: `0`
- semantic compatibility: unresolved
- production classification: inactive
- one-shot workflow: absent
- identity resolution: BLOCKED
- genealogy: BLOCKED
- beneficiary matching: BLOCKED
- outreach: BLOCKED

## Next Product Work

1. Perform `HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`.
2. Review only the derived v1.1 evidence, execution audit and privacy/log verification.
3. Decide whether an **offline** diagnostic change is justified by the narrowed decoded-shape failure.
4. Do not normalize, trim, uppercase or relax the regex without separate evidence and review.
5. Do not perform another SCO request without a new proposal and fresh execution/privacy approvals.
6. Source approval/registry activation, A02 normalization, identity, genealogy, matching and outreach remain independent later gates.

## Out of Scope Until Later Gates

- automatic retry or third SCO request;
- reuse of either consumed second-run approval;
- wider byte/request/row budgets without separate evidence and approval;
- persistence of raw rows or offending values;
- source-value trimming, uppercasing or normalization without evidence;
- regex relaxation without evidence;
- source approval or registry activation;
- production insurance classification;
- identity resolution, beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
