# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` REAL ATTEMPT STOPPED FAIL-CLOSED + OFFLINE DIAGNOSTIC REMEDIATION CI VERIFIED — HUMAN EVIDENCE REVIEW REQUIRED | Historical run `34965097988`; remediation SHA `ec688df6...`; CI `34969967725` SUCCESS; network workflow absent |
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
- `PROPERTY_TYPE` semantic proposal, runner design and synthetic/mock runner implementation CI verified.
- One bounded owner-authorized real semantic attempt completed once and stopped fail-closed.
- Derived execution evidence persisted; offending value/bytes intentionally not persisted.
- One-shot network workflow removed immediately after the run.
- Offline evidence review and synthetic diagnosis completed + CI verified.
- Offline diagnostic remediation implemented on isolated candidate + CI verified.

## Historical Real Semantic Attempt

Run:
`34965097988`

Result:
`STOPPED_FAIL_CLOSED`

Historical stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Budget actually used:
- 1 HEAD;
- 1 Range GET;
- 2 HTTP requests total;
- 131072 source-body bytes;
- 0 accepted/examined rows;
- no retry;
- no cap widening.

The historical stop reason remains intentionally uninterpreted because the prior runner conflated encoding and decoded-format failures.

The prior execution authorization has been consumed and cannot be reused.

## Offline Diagnosis

Diagnosis SHA:
`1405d33b7c09373f738dc87f6c93b05a0c342461`

Diagnosis CI:
`34968418681` — SUCCESS.

Finding:
- invalid UTF-8 and decoded regex mismatch previously produced the same stop code;
- custom field projection matched `csv.reader(..., strict=True)` on the committed synthetic standard-CSV edge matrix;
- no evidence justified trimming, normalization or regex relaxation.

## Offline Diagnostic Remediation

Candidate branch:
`m3-ca-sco-property-type-diagnostic-remediation`

Base diagnosis HEAD:
`8aa6c61594232b54b351d0a2063d9de2031a28f7`

Owner authorization:
`autorizzo remediation diagnostica offline`

Functional remediation SHA:
`ec688df61c56276c36facf2f598a1ad90b97fe5d`

CI:
`34969967725` — SUCCESS.

Remediation:
- UTF-8 decode failure -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded shape failure -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- existing regex unchanged;
- no source-value normalization;
- no raw values/bytes/hashes/lengths persisted or logged;
- execution schema enum extended backward-compatibly;
- historical execution evidence remains unchanged and valid;
- one-shot network workflow remains absent.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION.md`

## Current Safety State

- canonical development branch `m2-state-governance-core` remains at `c3f0dc7e374d21283358e4e1e8d403f078f08acb`;
- stable `main` remains at `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`;
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

1. Human review at `HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_REVIEW`.
2. If approved, promote the offline remediation through the normal candidate-to-canonical gate only; do not infer anything new about the historical real value.
3. Do not recreate a network workflow as part of promotion.
4. Any second bounded real execution requires new explicit semantic-execution + transient-row privacy authorization.
5. Source approval/registry activation, A02 normalization, identity, matching and outreach remain later independent gates.

## Out of Scope Until Later Gates

- automatic retry of the semantic run;
- another SCO request under the consumed authorization;
- wider byte/request/row budgets;
- persisting raw row/value evidence;
- trimming, uppercasing or normalizing source values;
- relaxing the `PROPERTY_TYPE` regex without evidence;
- source approval or registry activation;
- production insurance classification;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
