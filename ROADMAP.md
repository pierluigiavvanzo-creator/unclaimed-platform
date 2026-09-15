# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` REAL ATTEMPT STOPPED FAIL-CLOSED + OFFLINE DIAGNOSIS CI VERIFIED — REMEDIATION REVIEW REQUIRED | Run `34965097988`; diagnosis SHA `1405d33b...`; diagnostic CI `34968418681` SUCCESS; network workflow absent |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; Vercel runtime integration decommissioned |

## Completed M3 Readiness Work

- California source/legal inventory complete.
- A01 acquisition contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` transport and bounded structure evidence canonicalized.
- Four CSV members and identical 25-label header verified.
- First-purpose persisted scope reduced to `PROPERTY_ID` + `PROPERTY_TYPE`.
- `HOLDER_NAME` and identity/address fields prohibited for first triage.
- Transient CSV exposure isolated as a separate privacy boundary.
- `PROPERTY_TYPE` semantic-verification proposal canonical + CI verified.
- Bounded semantic runner design canonical + CI verified.
- Bounded semantic runner implementation canonical + synthetic/mock CI verified.
- One owner-authorized bounded real semantic execution completed once and stopped fail-closed.
- Execution evidence persisted as derived summary only.
- One-shot network workflow removed immediately after the run.
- Offline evidence review and synthetic parser diagnosis completed + CI verified.

## Real Semantic Attempt

Execution candidate:
`m3-ca-sco-property-type-semantic-execution`

Evidence closure SHA:
`3ca12f17c0a16ca49205b4d17117f3b41b6efd58`

One-shot run:
`34965097988`

Semantic result:
`STOPPED_FAIL_CLOSED`

Persisted stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Observed budget usage:
- 1 HEAD;
- 1 Range GET;
- 2 HTTP requests total;
- 131,072 source-body bytes;
- 0 accepted/examined rows;
- no retry;
- no extra Range;
- no budget widening.

The offending value is not persisted or logged and must not be inferred.

Steady-state CI after evidence closure:
`34965713695` — SUCCESS.

Network one-shot workflow:
ABSENT.

The execution approval was consumed by run `34965097988`.

## Offline Diagnosis

Branch:
`m3-ca-sco-property-type-offline-diagnosis`

Base:
`3ca12f17c0a16ca49205b4d17117f3b41b6efd58`

Diagnostic SHA:
`1405d33b7c09373f738dc87f6c93b05a0c342461`

Diagnostic CI:
`34968418681` — SUCCESS.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_OFFLINE_DIAGNOSIS.md`

Regression tests:
`tests/unit/test_ca_sco_property_type_offline_diagnosis.py`

Diagnosis:
- the current runner maps both UTF-8 decode failure and decoded-value regex mismatch to `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- current historical evidence therefore cannot distinguish those two causes;
- the custom projector matches Python `csv.reader(..., strict=True)` for the committed synthetic standard-CSV edge matrix;
- no standard-CSV projection defect was reproduced by that matrix;
- the real root cause remains unresolved because the offending bytes/value were intentionally not retained;
- no evidence supports relaxing or normalizing the regex.

No SCO network/body access occurred during diagnosis. No runner/schema/regex/source-policy/registry/network-workflow change was made.

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

## Current Safety State

- source policy `PROPOSED`;
- source-level real acquisition authorization false;
- registry disabled/unapproved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- network workflow absent;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Next Product Work

1. Human decision at `HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_REVIEW`.
2. If approved, perform offline-only contract/runner remediation to distinguish encoding failure from decoded-format failure.
3. Preserve historical evidence and current regex semantics.
4. Do not add raw source values or privacy-expanding diagnostics.
5. Keep network workflow absent.
6. Any second bounded real execution requires new explicit execution + transient-row privacy authorization.
7. Source approval/registry activation, A02 normalization, identity, matching and outreach remain later independent gates.

## Out of Scope Until Later Gates

- automatic retry of the semantic run;
- a second SCO network request under the consumed authorization;
- wider byte/request/row budgets;
- persisting raw row/value evidence;
- silently trimming/normalizing source values;
- relaxing the `PROPERTY_TYPE` regex without evidence;
- source approval or registry activation;
- production insurance classification;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.