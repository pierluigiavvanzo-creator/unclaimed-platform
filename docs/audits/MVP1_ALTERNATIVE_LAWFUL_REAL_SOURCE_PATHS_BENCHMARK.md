# MVP-1 Alternative Lawful Real-Source Paths Benchmark

Date: 2026-09-17

Status: **COMPLETE — NEW YORK OSC OWNER NAME FILE SELECTED AS NEXT MVP-1 SOURCE CANDIDATE**

Classification: `A — Product Critical`.

## Objective

Replace repeated California `PROPERTY_TYPE` diagnostics with the shortest credible lawful path to:

`approved real source -> deterministic insurance signal -> candidate -> economics -> reviewer`.

This work package is research/offline only. It made no new California request, submitted no external form, downloaded no owner-level source file, and processed no new real PII.

## Decision rule

Candidates were compared on:

1. authority/provenance;
2. insurance-specific signal available before identity work;
3. machine accessibility and stability;
4. privacy and commercial-use burden;
5. acquisition cost/friction;
6. update cadence;
7. integration effort/reuse potential;
8. expected time-to-first-candidate;
9. commercial fit with MVP-1.

The benchmark is an internal product-priority ranking, not a legal opinion. Any later real-source acquisition remains separately authorization-gated.

## Ranked result

### 1. New York Office of the State Comptroller — Owner Name File

**Decision: ADOPT AS NEXT MVP-1 SOURCE CANDIDATE**

Official evidence checked:

- Owner Name File request: https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form
- Location Service Providers: https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers
- Location-service requirements: https://www.osc.ny.gov/files/unclaimed-funds/resources/2025/pdf/aplsp-requirements-and-procedures-highlight-changes-1.pdf
- Property Type Tables: https://www.osc.ny.gov/files/unclaimed-funds/reporters/pdf/property-type-tables.pdf
- Insurance reference sheet: https://www.osc.ny.gov/files/unclaimed-funds/reporters/pdf/insurance-companies.pdf

Observed official facts:

- OSC provides a list of potential unclaimed-funds owners that can be requested and downloaded as a zipped delimited text file through a secure FTP link.
- The list includes owner name, last-known address, the nature of the property, when the property was reported, and by whom it was reported.
- The file is updated quarterly and can be retrieved again after access is granted.
- Dollar values and taxpayer-identification numbers are not disclosed.
- The downloadable list is not complete: exclusions include accounts without owner name/address, foreign addresses, accounts valued below $20, and certain pre-1985 book records.
- OSC expressly publishes procedures for Abandoned Property Location Service Providers. Its current requirements state that licensing/registration is not required, while later representation/claim activity requires direct contact, a compliant written/notarized agreement, and a fee no greater than 15%.
- New York publishes an authority-backed insurance property-type table. `IN03` is `Proceeds Due Beneficiaries`; the current insurance table also includes `IN01`, `IN02`, `IN04`, `IN05`, `IN06`, `IN07`, `IN12`, and `IN77` under the applicable New York abandoned-property framework.

MVP-1 implications:

- The source is designed for bulk research rather than only one-name-at-a-time manual search.
- `nature of property` plus reporting-organization information creates a credible pre-identity insurance-classification path.
- New York already recognizes the commercial/location-service role explicitly, reducing business-model ambiguity compared with states that prohibit commercial list use.
- The exact downloadable file schema/encoding and exact representation of `nature of property` are **not assumed**. They must be inspected fail-closed after a separately authorized acquisition.
- Because the list suppresses dollar value, case economics cannot rely on source amount at the first screen. MVP-1 must represent recoverable value as `UNKNOWN_FROM_SOURCE` until supported by later lawful evidence.

Overall: strongest combination of lawful bulk availability, insurance relevance, commercial fit and short integration path.

---

### 2. Texas Comptroller — SIFT Unclaimed Property dataset path

**Decision: DEFER / SECONDARY**

Official evidence checked:

- Dataset search: https://comptroller.texas.gov/transparency/open-data/search-datasets/
- Open Records / SIFT: https://comptroller.texas.gov/about/policies/open-records/
- Unclaimed Property program: https://comptroller.texas.gov/programs/unclaimed/

Observed official facts:

- The Comptroller dataset-search page states that SIFT can be used to download secured datasets such as Unclaimed Property.
- SIFT requires an account.
- A separate current Open Records page lists several SIFT dataset families but does not enumerate Unclaimed Property in that list.
- Texas publishes unclaimed-property reporting guidance and property-type codes, but the evidence reviewed does not establish the exact public SIFT owner-file schema or prove that an insurance property code is exposed in the downloadable dataset.

MVP-1 implication:

The path is plausible and authoritative but has unresolved access/schema friction. Do not spend integration work until availability, fields and permitted use are confirmed.

---

### 3. Pennsylvania Treasury — OpenBookPA / unclaimed-property data

**Decision: DEFER AS AGGREGATE-ONLY FOR CURRENT MVP-1 PURPOSE**

Official evidence checked:

- https://patreasury.gov/openbookpa/county-level-data.php

Observed official facts:

- Pennsylvania publishes downloadable CSV/XLSX unclaimed-property statistics and reports substantial unclaimed-property volume.
- The reviewed official dataset is county-level aggregate information, not an evidenced owner-level machine-readable candidate feed.

MVP-1 implication:

Useful for market sizing, not presently evidenced as the shortest path to one insurance candidate.

---

### 4. Illinois State Treasurer — I-CASH

**Decision: REJECT FOR BULK MVP-1 INGEST**

Official evidence checked:

- https://illinoistreasurer.gov/home/individuals/unclaimed-property/unclaimed-property-finder-applications/faq-unclaimed-property-finder-application/

Observed official fact:

- The Treasurer explicitly states that it does not provide bulk data files, database exports, or API access to unclaimed-property records.

MVP-1 implication:

A search/claim workflow may exist, but there is no supported bulk/API acquisition path for the platform vertical slice.

---

### 5. Washington Department of Revenue — Unclaimed Property public-record list

**Decision: REJECT FOR COMMERCIAL MVP-1 LIST ACQUISITION**

Official evidence checked:

- Public records index: https://dor.wa.gov/contact/e-mail/public-records-index-staff-manuals-and-information
- Public records policy: https://dor.wa.gov/contact/public-records
- UCP program: https://dor.wa.gov/about/unclaimed-property-ucp

Observed official facts:

- Washington identifies a `Listing of Unclaimed Property` containing names and last-known addresses as a public-record category.
- The same Department public-records page states that law prohibits releasing lists of individuals or taxpayers when the request is made for a commercial purpose.
- Unclaimed-property information also has specific confidentiality restrictions.

MVP-1 implication:

This conflicts directly with the platform's commercial sourcing objective. Do not pursue this list path for MVP-1.

## Product selection

Selected source candidate:

`NEW YORK OSC OWNER NAME FILE`

Proposed internal source id for the next implementation package:

`ny.osc.unclaimed_funds.owner_name_file`

Selection rationale:

- first-party government authority;
- explicit bulk download mechanism;
- quarterly refresh;
- source fields that can expose property nature and reporter before identity research;
- direct authority table for insurance property types including `IN03`;
- explicit location-service-provider framework compatible with a later commercial workflow;
- no source fee identified on the reviewed request page;
- lower semantic risk than the current California `PROPERTY_TYPE` feed.

Known constraints to preserve:

- no assumption about exact delimiter, columns or code representation until the real file is obtained;
- no amount is available from the public list;
- owner name/address are PII and require a fresh privacy gate before acquisition/processing;
- no outreach, representation, fee agreement or claim submission is authorized by source selection;
- no source/registry activation occurs from this benchmark alone.

## Reuse decision

`REUSE / WRAP` the existing A01 acquisition contracts, deterministic provenance controls, fail-closed parsing patterns, D-010 lessons on source-semantics discipline, and the existing reviewer/economics vertical-slice contracts.

Do not create a new generic ingestion framework before the New York file contract is known.

## Next action

Execute exclusively:

`IMPLEMENT_NY_OSC_OWNER_NAME_FILE_SOURCE_CONTRACT_AND_PRIVACY_GATE_OFFLINE`

Classification: `A — Product Critical`.

Goal:

Prepare the smallest versioned source contract and privacy/acquisition gate required to request and inspect the New York Owner Name File safely, using synthetic fixtures only. The implementation must not invent the real file schema: unknown real columns/delimiter/encoding must remain an explicit first-acquisition discovery gate.

The next package must define at minimum:

- source candidate identity and authority references;
- disclosed semantic fields (`owner name`, `last-known address`, `nature of property`, `reported when`, `reported by`) without inventing physical column names;
- NY authority-backed insurance vocabulary with `IN03` as the primary MVP-1 life-insurance target;
- `UNKNOWN_FROM_SOURCE` treatment for monetary value;
- raw-file/PII storage and transient-processing boundaries;
- fail-closed first-file schema discovery;
- exact fresh human authorization required before any request/download or real PII processing;
- synthetic contract tests only.

No Owner Name File request or download is authorized by this benchmark.