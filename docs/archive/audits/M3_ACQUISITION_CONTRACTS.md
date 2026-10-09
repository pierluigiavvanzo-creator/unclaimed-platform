# M3 Acquisition Contracts and Adapter Boundary

Date: 2026-09-13

## Scope

Class: **A — Product Critical**

This task defines the contract-first boundary for California M3 acquisition. It does not download
real California data and does not perform beneficiary matching.

## Source selected for the future bounded real spike

`ca.sco.unclaimed_property.bulk`

Authority: California State Controller's Office (SCO), Unclaimed Property Division.

Official access page:

- https://www.sco.ca.gov/upd_download_property_records.html

The official page states that the Controller's public unclaimed-property database is downloadable in
CSV format and that files are updated every Thursday. The related SCO database-search FAQ also
directs users to the bulk CSV download.

## Contract decision

A01 owns acquisition of a raw artifact and its provenance, not interpretation of California-specific
rows.

The M3 boundary therefore records:

- request identity and source identity;
- `MOCK` versus `REAL`;
- explicit approval identifier for `REAL`;
- `RAW_INGEST_ONLY` scope;
- byte budget;
- expected media types;
- result status and reason code;
- immutable raw storage reference;
- SHA-256 content hash;
- byte count and content type;
- source URI and authority;
- acquisition method;
- retrieval time and source revision when available;
- reference to the terms/readiness review.

A01 does **not** infer or invent CSV columns. Row parsing belongs to A02 after a bounded sample or
official record layout has been independently verified.

## California SCO adapter boundary

`CaliforniaSCOBulkAdapter` is intentionally fail-closed.

It rejects or blocks:

1. a request addressed to another source;
2. a non-`REAL` request for the real SCO adapter;
3. any scope other than `RAW_INGEST_ONLY`;
4. missing source approval or missing request `approval_id`;
5. network acquisition even after those checks, because network retrieval is not implemented in this
   readiness task.

This final block is intentional. A later task must separately implement bounded download, immutable
raw persistence, size enforcement, transport validation, and privacy/data-minimization controls.

## Deferred-source mocks

The following California sources remain synthetic/mock-only for this task:

- `ca.sco.estates`
- `ca.cdi.company_profiles`
- `ca.cdi.naic_policy_locator`
- `ca.cdph.death_records`
- `ca.courts.probate`

`mocks/sources/ca_deferred_sources.json` records this list. `DeferredMockSourceAdapter` produces only
deterministic synthetic artifacts and blocks real mode.

## Privacy and safety

No real claimant, owner, beneficiary, decedent, insurer record, address, death record, court record,
or other PII is included in the fixtures.

No outreach, claimant verification, legal determination, fee agreement, or claim submission is
enabled.

## Reuse-first note

No third-party acquisition framework is added. The M3 boundary is a small Protocol/dataclass layer
using the Python standard library. Existing project dependencies already provide HTTP capability
(`httpx`) for a later retrieval implementation, so introducing an additional downloader or scraping
framework at this stage would add no product value.

## Acceptance evidence for the candidate

Local candidate-only checks:

- 6 new tests passed;
- Python `compileall` passed;
- no real network access was performed.

Full repository Ruff/mypy/pytest verification must be performed by GitHub CI on the isolated
candidate branch before this change can be promoted to the canonical development branch.
