# M3 California SCO Source Governance Proposal

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANONICAL GOVERNANCE PROPOSAL — REAL ACQUISITION NOT AUTHORIZED**

## Objective

Represent the California State Controller (SCO) public unclaimed-property bulk dataset as a known
candidate source without approving it, downloading it, parsing California rows, enabling beneficiary
matching, or processing real PII.

## Authoritative source evidence

The official SCO download page states that all unclaimed-property records in the Controller's public
database are available in CSV format and that the files are updated every Thursday:

- https://www.sco.ca.gov/upd_download_property_records.html

The SCO public-records guidance states that public access is subject to applicable conditions and the
California Public Records Act:

- https://www.sco.ca.gov/eo_about_records.html

The SCO privacy policy is also relevant to later purpose/privacy review:

- https://www.sco.ca.gov/eo_privacy.html

Existing repository readiness evidence remains authoritative:

- `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`
- `docs/audits/M3_ACQUISITION_CONTRACTS.md`
- `docs/audits/M3_RAW_STORAGE_PRIVACY_GATES.md`

## Governance decision

Registration and approval are separate states.

`ca.sco.unclaimed_property.bulk` is present in `sources/registry.yaml` only as a disabled,
not-approved source. The registry entry does not grant network access or processing permission.

`SourceAccessGovernance` records controls that must exist before a real source can ever be
authorized. The California SCO policy instance remains deliberately `PROPOSED` and non-authorizing.

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

Beneficiary matching and outreach remain false in every policy status.

## Promotion evidence

Candidate branch: `m3-ca-sco-source-governance`.

Promoted SHA:
`463c6d6c972fa955a8aa0d3c97208c3029e202a8`

Candidate GitHub Actions run `34825751270`: PASS.

After explicit owner approval, the candidate was promoted by clean fast-forward into
`m2-state-governance-core`. Canonical post-promotion GitHub Actions run `34826353694` passed both
`quality` and `streamlit-candidate`.

Promotion made the governance proposal canonical; it did **not** approve real acquisition.

## Intentionally unresolved before any real retrieval

Do not invent values not yet verified. Later gates must establish:

- exact direct download URLs and redirect behavior;
- actual transport content types;
- maximum byte budget;
- timeout policy;
- downloaded artifact characteristics;
- California CSV row layout and field names;
- necessary data categories and minimized field scope;
- whether any PII is necessary for a specifically approved purpose;
- retention policy reference;
- trusted privacy/data-minimization policy;
- explicit human approval reference.

Until those items are resolved through later gates, the A01 adapter must continue to block real
network acquisition.

## Runtime boundary retained

This proposal does not change the A01 runtime adapter. `CaliforniaSCOBulkAdapter` fails closed when
the source is not approved and still returns `REAL_NETWORK_ACQUISITION_NOT_IMPLEMENTED` even when
its local approval flag is supplied.

No source-access policy is wired into real retrieval.

## Verified acceptance criteria

Tests prove that:

1. the governance schema is valid JSON Schema draft 2020-12;
2. the proposed California SCO policy validates;
3. a `PROPOSED` policy attempting to authorize real acquisition is rejected;
4. the source registry remains schema-valid;
5. the SCO candidate is disabled and not approved;
6. the number of approved real sources remains zero;
7. policy and registry use the same source identity and official source page;
8. full repository quality/regression gates pass in CI.

No network retrieval was part of these tests.

## Safety boundary

This canonical proposal does not authorize or perform:

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

Use a normal history-preserving revert if this governance proposal ever needs to be removed from
canonical. Do not force-push or rewrite history.

## Next gate

Prepare a separate versioned **approval-readiness evidence package** that records verified official
facts without granting authority.

The next candidate may record the advertised CSV format, Thursday update cadence, official source
page, the advertised `claimit.ca.gov` download-host relationship, public-record/privacy references and
explicit unresolved controls.

It must not follow/download a CSV, approve/enable the source, infer row fields, authorize PII or
processing purposes, or enable beneficiary matching/outreach.
