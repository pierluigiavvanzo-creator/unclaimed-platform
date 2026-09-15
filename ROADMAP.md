# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | AUTHORITY PROVENANCE REVIEW VERIFIED; LIVE SEMANTIC MISMATCH UNRESOLVED | review CI `35013841037`; authority SHA-256 `7884f765...721e5` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- prior bounded semantic execution stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- repository-only provenance review completed;
- one-shot California SCO authority archival completed successfully in run `35012019831`;
- authority archive is immutable at SHA-256 `7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5`;
- authority archive provenance review completed offline and CI-verified in run `35013841037`;
- `ZZZZ` is directly supported by the archived authority;
- California insurance codes `IN01`-`IN08` and `IN99` are directly supported by the archived authority;
- all authority-enumerated property type codes other than `ZZZZ` follow the two-uppercase-Latin-letter plus two-digit shape, with the explicit boundary that arbitrary `AA99` membership is not established;
- existing regex is not contradicted by the authority;
- the live source produced a decoded non-empty PROPERTY_TYPE that failed the unchanged shape regex, so semantic compatibility remains unresolved;
- no semantic/runtime change is justified or authorized by this review;
- source policy remains `PROPOSED` and production classification remains inactive.

## Next Product Work

Human decision only:

`DECIDE_WHETHER_TO_PREPARE_BOUNDED_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL`

If proposal preparation is authorized, it must be a separate fail-closed package defining the diagnostic evidence boundary before any new source access, source-value characterization, remediation logic, runtime modification, or third real semantic execution.

The completed provenance review does not define an approval token for that future package.

## Still Out of Scope

- reuse of the consumed authority archival approval;
- reuse of prior semantic execution/privacy approvals;
- another authority retrieval without a separate proposal/gate;
- SCO dataset or `claimit.ca.gov` access without a newly authorized bounded scope;
- reconstruction or inference of the unretained offending PROPERTY_TYPE value;
- parser, regex, casing, trimming or normalization changes;
- another real PROPERTY_TYPE semantic execution;
- source or registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
