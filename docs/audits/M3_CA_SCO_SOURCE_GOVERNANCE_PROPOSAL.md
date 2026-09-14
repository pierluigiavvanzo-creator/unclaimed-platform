# M3 California SCO Source Governance Proposal

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANDIDATE PROPOSAL ONLY — REAL ACQUISITION NOT AUTHORIZED**

## Objective

Prepare the smallest versioned governance package required to represent the California State
Controller (SCO) public unclaimed-property bulk dataset as a known candidate source without
approving it, downloading it, parsing California rows, enabling beneficiary matching, or processing
real PII.

## Authoritative source evidence

The official SCO download page states that all unclaimed-property records in the Controller's public
database are available in CSV format and that the files are updated every Thursday:

- https://www.sco.ca.gov/upd_download_property_records.html

The SCO public-records guidance states that public access is subject to applicable conditions and the
California Public Records Act:

- https://www.sco.ca.gov/eo_about_records.html

Existing repository readiness evidence remains authoritative for this candidate:

- `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`
- `docs/audits/M3_ACQUISITION_CONTRACTS.md`
- `docs/audits/M3_RAW_STORAGE_PRIVACY_GATES.md`

## Governance decision

Registration and approval are separate states.

This candidate adds `ca.sco.unclaimed_property.bulk` to `sources/registry.yaml` only as a disabled,
not-approved source. The registry entry therefore does not grant network access or processing
permission.

A new versioned `SourceAccessGovernance` contract records the controls that must exist before a real
source can ever be authorized. The California SCO policy instance is deliberately `PROPOSED` and
non-authorizing.

For `PROPOSED` status the schema requires:

- `real_acquisition_authorized: false`;
- no approval reference;
- no authorized processing purposes;
- no authorized data categories;
- no allowed row fields;
- `allow_pii: false`;
- no allowed download hosts;
- redirects blocked until approval;
- no network timeout or byte budget selected;
- no expected media types selected.

The contract also requires beneficiary matching and outreach to remain false in every status.

## Intentionally unresolved before any real retrieval

This proposal does not invent values that have not yet been verified. A later bounded retrieval
design must separately establish and test:

- direct download host allowlist and redirect behavior;
- exact transport content types;
- maximum byte budget;
- timeout policy;
- actual downloaded artifact characteristics;
- California CSV row layout and field names;
- necessary data categories and minimized field scope;
- whether any PII is necessary for the specifically approved purpose;
- a retention policy reference;
- a trusted privacy/data-minimization policy;
- the explicit human approval reference.

Until those items are resolved through later gates, the current A01 adapter must continue to block
real network acquisition.

## Runtime boundary retained

This candidate does not change the A01 runtime adapter. The existing
`CaliforniaSCOBulkAdapter` already fails closed when the source is not approved and still returns
`REAL_NETWORK_ACQUISITION_NOT_IMPLEMENTED` even when its local approval flag is supplied. Existing
regression tests remain responsible for that runtime boundary.

No source-access policy in this candidate is wired into runtime acquisition because doing so would
expand the task from governance preparation into real-retrieval implementation.

## Acceptance criteria

The candidate is acceptable only if tests prove that:

1. the governance schema is valid JSON Schema draft 2020-12;
2. the proposed California SCO policy validates;
3. a `PROPOSED` policy attempting to authorize real acquisition is rejected;
4. the source registry remains schema-valid;
5. the SCO candidate is disabled and not approved;
6. the number of approved real sources remains zero;
7. policy and registry use the same source identity and official source page;
8. the existing full repository test/quality gates remain green in CI.

No network retrieval is part of these tests.

## Safety boundary

This candidate does not authorize or perform:

- real California acquisition;
- beneficiary matching;
- real claimant/beneficiary/decedent/family PII processing;
- CSV row parsing or normalization;
- outreach;
- claimant verification;
- fee agreements;
- claim submission;
- unapproved scraping or restricted-source access.

## Rollback

Before promotion, rollback is to abandon/delete branch `m3-ca-sco-source-governance`.

After any later approved promotion, use a normal history-preserving revert. Do not force-push or
rewrite historical decisions.

## Next gate

After candidate tests and CI pass, the owner may review this governance proposal for promotion to the
canonical development branch. Promotion does not constitute approval of real acquisition.

Any future move from `PROPOSED` to an authorizing policy is a separate human gate and must define the
previously unresolved transport, privacy, retention, data-minimization, provenance and approval
controls before network code can be enabled.
