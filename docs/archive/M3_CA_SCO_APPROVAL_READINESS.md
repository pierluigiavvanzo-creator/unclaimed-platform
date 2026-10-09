# M3 California SCO Approval-Readiness Evidence

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANONICAL EVIDENCE — SOURCE NOT APPROVED**

## Objective

Create a versioned, machine-readable evidence package for the California State Controller (SCO)
public bulk candidate while preserving a strict separation between verified public facts and source
authorization.

This task performs no direct-file retrieval, no CSV download, no row parsing and no real PII
processing.

## REUSE FIRST result

The existing repository already has the required building blocks:

- JSON Schema draft 2020-12 contracts;
- `SourceAccessGovernance` v1;
- the disabled/not-approved SCO registry entry;
- the `PROPOSED` SCO source-access policy;
- contract-test infrastructure using `jsonschema` and PyYAML.

No third-party runtime dependency is required. A separate approval-readiness contract is preferable
to mutating the `PROPOSED` authorization policy because evidence and authority must remain distinct.

## Authoritative evidence reviewed

Official California State Controller pages reviewed on 2026-09-14:

1. `https://www.sco.ca.gov/upd_download_property_records.html`
   - states that all records in the Controller's public unclaimed-property database can be
     downloaded in `.CSV` format;
   - states that files are updated every Thursday;
   - displays the property-file download links on the `claimit.ca.gov` host.

2. `https://www.sco.ca.gov/eo_about_records.html`
   - states that public access to SCO records is subject to applicable conditions and the
     California Public Records Act.

3. `https://www.sco.ca.gov/eo_privacy.html`
   - states that personal-information use is constrained by stated purposes and law;
   - states that website information is public domain and may be copied/used as permitted by law.

4. `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.`
   - retained as a downstream legal-review reference for locator/recovery agreements;
   - not treated as source-acquisition authority.

No CSV link was followed and no dataset artifact was acquired while preparing this evidence package.

## Machine-readable evidence

Canonical artifacts:

- `schemas/common/source_approval_readiness.schema.json`;
- `schemas/examples/ca_sco_approval_readiness.examples.json`;
- `sources/evidence/ca_sco_unclaimed_property_bulk.approval_readiness.v1.json`;
- `tests/contract/test_ca_sco_approval_readiness.py`.

The schema forces these fail-closed invariants:

- `review_status = EVIDENCE_ONLY_NOT_APPROVED`;
- `acquisition_performed = false`;
- `source_approved = false`;
- `source_enabled = false`;
- transport verification flags remain false;
- data-scope/privacy/retention verification flags remain false.

The evidence artifact records only the advertised CSV format, Thursday update cadence, official
source page, advertised download-host relationship and authoritative references.

## Promotion evidence

Candidate branch: `m3-ca-sco-approval-readiness`.

Promoted SHA:
`73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`

Candidate GitHub Actions run `34827272138`: PASS.

After explicit owner approval, the candidate was promoted by clean fast-forward into canonical
`m2-state-governance-core` with no force update.

Canonical post-promotion GitHub Actions run `34828513676`: PASS, including `quality` and
`streamlit-candidate`.

Promotion of this evidence package does not constitute source approval.

## Intentionally unresolved

The artifact explicitly keeps unresolved:

- exact download URLs;
- redirect chain;
- actual HTTP media type;
- current file size;
- maximum byte budget;
- timeout policy;
- source revision;
- content hash;
- CSV row layout;
- authorized processing purpose;
- authorized data categories;
- allowed/minimized fields;
- PII necessity;
- retention policy;
- trusted project privacy policy;
- human approval reference.

These values must not be inferred from general knowledge or from the source page.

## Cross-check with canonical governance

Tests require the evidence to match the existing source identity and official page in:

- `sources/registry.yaml`;
- `policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json`.

They also assert that:

- registry `enabled` remains false;
- registry `approved_for_use` remains false;
- policy status remains `PROPOSED`;
- real acquisition authorization remains false;
- beneficiary matching remains false;
- outreach remains false;
- real PII remains unauthorized.

## Acceptance criteria

Verified:

1. the readiness schema is valid JSON Schema draft 2020-12;
2. the evidence artifact validates;
3. evidence claiming completed acquisition is rejected;
4. evidence claiming source approval is rejected;
5. evidence, registry and policy share the same source identity and official page;
6. unresolved controls remain explicitly unresolved;
7. existing repository quality/contract/smoke/full-test gates pass;
8. no real California artifact is downloaded.

## Safety boundary

This canonical evidence package does not authorize or perform:

- transport-preflight execution;
- real California acquisition;
- source approval or activation;
- CSV row parsing;
- beneficiary matching;
- real PII processing;
- outreach;
- claimant verification;
- fee agreements;
- claim submission.

## Next gate

Prepare a separate transport-preflight **proposal only** that defines the metadata checks and
fail-closed boundaries for a later authorized network preflight.

The proposal itself must execute no request to a download endpoint and acquire no real dataset.
Actual transport-preflight execution requires a separate explicit owner gate before any network
interaction with the download endpoint.
