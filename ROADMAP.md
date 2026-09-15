# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` BOUNDED REAL SEMANTIC ATTEMPT STOPPED FAIL-CLOSED — EVIDENCE REVIEW REQUIRED | Run `34965097988`; 2 requests; 131072 body bytes; 0 accepted rows; stop `PROPERTY_TYPE_FORMAT_UNEXPECTED`; no retry |
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
- Owner-authorized bounded semantic execution and transient privacy approvals machine-recorded and CI verified.
- One bounded real execution performed once and stopped fail-closed.

## Canonical Runner

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Promoted functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`

Canonical CI:
`34961511401` — SUCCESS.

Canonical development HEAD before the execution candidate:
`c3f0dc7e374d21283358e4e1e8d403f078f08acb`.

## Execution Candidate

Branch:
`m3-ca-sco-property-type-semantic-execution`

Authorization package commit:
`6ba8d62824f0f0e8eaaa0eefbb8dc1bfdb58898e`

Authorization CI:
`34964924686` — SUCCESS.

One-shot commit:
`dd5dc80a22307586c341b703de8fe03d6861df29`

One-shot run:
`34965097988` — SUCCESS as an execution container; semantic result `STOPPED_FAIL_CLOSED`.

Stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Observed budget usage:
- 1 HEAD;
- 1 Range GET;
- 2 HTTP requests total;
- 131,072 source-body bytes;
- 0 accepted/examined rows;
- no retry;
- no extra Range;
- no budget widening.

## Evidence

Persisted derived evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Execution audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_EXECUTION.md`

Artifact provenance:
- artifact ID `10394467215`;
- ZIP digest `sha256:24a39a739872b0d9b3f0bff9a17c22f8ab1a443ddbcf82b7f9126d546ed1a66d`;
- JSON SHA-256 `790dabcf1c04946ad930de467f204cb0af6fe78c25bae86b1ca541e4fc07b96a`.

No offending `PROPERTY_TYPE` value is persisted or logged. No claim about that value is permitted from current evidence.

## Workflow Steady State

The temporary one-shot workflow was removed after the run at commit:
`bc1b0a955037d35dfa1a37b0c29497c219a04609`.

Steady-state one-shot workflow:
ABSENT.

The ordinary CI on the temporary-workflow commit (`34965098018`) failed three historical workflow-absence contract assertions, as expected. Those contracts remain unchanged and should pass again after workflow removal.

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
- full archive not downloaded;
- raw/full-row values not persisted;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

The single execution authorization has been consumed. It does not imply permission for another network attempt.

## Next Product Work

1. Human review at `HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`.
2. Diagnose `PROPERTY_TYPE_FORMAT_UNEXPECTED` from code/contracts and synthetic reproduction first, without another SCO request.
3. Do not infer the offending real value from the stop code.
4. Any second bounded real execution requires a new explicit human execution + privacy authorization.
5. Source approval/registry activation, A02 normalization, identity, matching and outreach remain later independent gates.

## Out of Scope Until Later Gates

- automatic retry of the semantic run;
- wider byte/request/row budgets;
- persisting raw row/value evidence;
- source approval or registry activation;
- production insurance classification from this failed sample;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
