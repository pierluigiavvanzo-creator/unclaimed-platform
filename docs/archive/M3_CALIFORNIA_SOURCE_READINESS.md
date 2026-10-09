# M3 California Source Readiness Inventory

Date checked: 2026-09-13

## Scope

Class: **A — Product Critical**

This document records the first M3 California source/legal readiness inventory required before any real acquisition, scraping, beneficiary matching, claimant verification, outreach, or claim activity.

This is a readiness artifact, not legal advice and not an approval to acquire real personal data.

## Gate rule

Real M3 acquisition remains **BLOCKED** until all of the following are explicitly satisfied for a source:

1. source authority is verified;
2. permitted access method is documented;
3. provenance requirements are defined;
4. terms, legal constraints and privacy constraints are documented;
5. the source is classified as real-access, mock-only or deferred;
6. the acquisition contract and adapter boundary are defined and tested;
7. use of real data is explicitly approved for the bounded spike.

No source in this inventory is yet marked `approved_for_use` in `sources/registry.yaml`.

## Candidate inventory

| Source | Authority | Verified access method | Proposed M3 treatment | Readiness status |
|---|---|---|---|---|
| California State Controller — Unclaimed Property public database | California State Controller's Office (SCO), Unclaimed Property Division | Official bulk `.CSV` download of the Controller's public database; files updated every Thursday | Preferred candidate for a future bounded, read-only real-data spike after contract/privacy approval | `CANDIDATE_REAL — APPROVAL PENDING` |
| California State Controller — Estates of Deceased Persons File | California State Controller's Office, Unclaimed Property Division | Free downloadable Microsoft Excel worksheet; updated first business day of April and October | Potential secondary source for estate/heir research; contains names and reported heirs, so real acquisition requires explicit privacy/data-minimization review | `DEFER — PRIVACY REVIEW` |
| California Department of Insurance — Insurance Company Profiles | California Department of Insurance (CDI) | Public web search by company name; profiles expose location, former names, service-of-process agent, license status, company type, domicile, authorized insurance lines and complaint history | Reference/manual verification source for insurer identity/status; do not automate until access terms and adapter method are separately approved | `REFERENCE — AUTOMATION NOT APPROVED` |
| NAIC Life Insurance Policy Locator via CDI | California Department of Insurance / National Association of Insurance Commissioners | Consumer locator workflow; insurers contact the requester only when a policy is found and requester is the designated beneficiary or authorized legal representative | Not suitable as an automated discovery source for M3; use mock contract only unless a later human/legal gate authorizes case-specific use | `MOCK / HUMAN_REVIEW` |
| California death records | California Department of Public Health — Vital Records (CDPH-VR) | Certified copies requested by mail, county office, or third-party electronic request; authorized and informational copies have different legal effects | Mock for M3. Any later real request must be case-specific and human-gated | `MOCK / DEFER` |
| California Superior Court electronic probate/case records | Judicial Branch of California / individual Superior Courts | Public courthouse access is required for electronic records; remote public access exists only where feasible and may be limited. Availability depends on court and case type | No statewide automated adapter for M3. A later county-specific pilot requires separate access/terms review | `MOCK / DEFER` |

## Source details and evidence

### CA-SCO-UPD-BULK — State Controller Unclaimed Property public database

**Authority**

California State Controller's Office, Unclaimed Property Division.

**Official source**

- https://www.sco.ca.gov/upd_download_property_records.html

**Verified access method**

The SCO page states that all unclaimed-property records in the Controller's public database can be downloaded in `.CSV` format. The page provides amount-segmented files and an `All properties` download. It states that the files are updated every Thursday.

The database includes categories such as bank accounts, uncashed checks, insurance benefits, wages, stocks, bonds and safe-deposit-box contents.

The same page states that, once downloaded, the data may be sorted using a local database/spreadsheet program and describes outreach to people and businesses who may not know they have unclaimed property.

**Website/privacy context**

- https://www.sco.ca.gov/eo_privacy.html
- https://www.sco.ca.gov/eo_about_records.html

The SCO privacy policy states that information on the SCO website is public domain and may be copied and used as permitted by law, except pictures and official symbols. Public-record access remains subject to applicable law and disclosure limitations.

**M3 constraint**

The existence of a public bulk download does **not** by itself approve the platform's later processing, matching, scoring, outreach, fee agreements or claims workflow. Those functions remain behind separate deterministic legal/privacy gates.

**Readiness decision**

`CANDIDATE_REAL — APPROVAL PENDING`.

This is the preferred first real source because it provides an explicit official bulk-download path, avoiding scraping of the search UI. No download is performed by this readiness task.

---

### CA-SCO-ESTATES — Estates of Deceased Persons File

**Authority**

California State Controller's Office, Unclaimed Property Division.

**Official source**

- https://sco.ca.gov/upd_estates_investigator.html

**Verified access method**

The SCO provides the Estates of Deceased Persons File as a free downloadable Microsoft Excel worksheet. The page states that the file contains estates remitted to the State of California and indexes records by State property ID, decedent name, reported heir(s) and available balance. It is updated on the first business day of April and October.

**M3 constraint**

Because the file directly contains decedent and reported-heir names, real acquisition is deferred until an explicit privacy/data-minimization review defines what fields are necessary for the bounded spike and how raw evidence is retained.

**Readiness decision**

`DEFER — PRIVACY REVIEW`.

---

### CA-CDI-COMPANY-PROFILES — Insurance Company Profiles

**Authority**

California Department of Insurance.

**Official source**

- https://www.insurance.ca.gov/01-consumers/120-company/01-coprof/

**Verified access method**

CDI provides a public company-profile search. The published profile information includes company location, former names, agent for service of process, license status, company type, domicile, authorized lines of insurance and complaint history.

**M3 constraint**

This is suitable as an authoritative reference for insurer verification, but this inventory does not establish an API or bulk-use permission. No automated adapter is approved yet.

**Readiness decision**

`REFERENCE — AUTOMATION NOT APPROVED`.

---

### CA-CDI-NAIC-LIPL — Life Insurance Policy Locator

**Authority**

California Department of Insurance references the National Association of Insurance Commissioners Life Insurance Policy Locator.

**Official source**

- https://www.insurance.ca.gov/01-consumers/105-type/6-lifeAnnuity/LocateLifeInsurancePolicy.cfm

**Verified access method and eligibility context**

CDI describes the service as a consumer locator for policies or annuity contracts of a deceased person. Participating companies search their records and contact the requester only if a policy is found and the requester is the designated beneficiary or authorized legal representative. CDI also instructs users to conduct a diligent search of the deceased person's records before using the service.

**M3 constraint**

This workflow is not treated as a bulk discovery endpoint or automated acquisition source. M3 may model its boundary synthetically, but no automated submissions or real claimant assertions are allowed.

**Readiness decision**

`MOCK / HUMAN_REVIEW`.

---

### CA-CDPH-DEATH — California death records

**Authority**

California Department of Public Health — Vital Records.

**Official sources**

- https://www.cdph.ca.gov/Programs/CHSI/Pages/Vital-Records-Obtaining-Certified-Copies-of-Death-Records.aspx
- https://www.cdph.ca.gov/Programs/CHSI/Pages/Authorized-Copy-vs--Informational-Copy.aspx

**Verified access method**

CDPH-VR states that it maintains a permanent public record of every death occurring in California since July 1905. Certified copies can be requested through defined mail, county/in-person and third-party electronic processes.

California distinguishes a certified authorized copy from a certified informational copy. An authorized copy may establish identity and is restricted to defined eligible requesters; an informational copy cannot be used to establish identity.

**M3 constraint**

There is no approved bulk death-record feed in this readiness task. Death evidence will be mocked for the California spike until a later case-specific access and legal basis is approved.

**Readiness decision**

`MOCK / DEFER`.

---

### CA-COURTS-PROBATE — Superior Court probate/case records

**Authority**

Judicial Branch of California and the individual California Superior Courts.

**Official source**

- https://courts.ca.gov/policy-administration/public-records/who-where-how-viewing-courts-electronic-case-records

**Verified access method**

The Judicial Branch states that electronic case records may be viewed at the courthouse and, where a court makes it available, through remote access. Public remote access can be limited; not every court is able to provide remote access, and access depends on the user's relationship to the case and the case type.

**M3 constraint**

No single statewide probate adapter is assumed. Any future real probate acquisition must select a specific county/court and separately verify that court's access method, terms and permissible automation.

**Readiness decision**

`MOCK / DEFER`.

## Material legal/commercial constraint identified

### California Code of Civil Procedure § 1582

Official text:

- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.

For property reported under CCP § 1530, § 1582 contains restrictions on agreements to locate, deliver, recover or assist in recovery of unclaimed property. Among other requirements, the statute provides that certain agreements are invalid during the report-to-delivery period, prohibits requiring compensation before Controller approval/payment, requires specified written disclosures for qualifying post-delivery agreements, and caps the agreed fee or compensation at 10 percent of recovered property under the covered provision.

The SCO's consumer guidance for investigators/heir finders also states that a disclosure contract is required and describes the 10 percent fee limit, subject to its stated exception for County Probated Estates:

- https://sco.ca.gov/upd_investigator_about.html

**Project implication**

This finding is recorded as a readiness constraint only. It is **not** yet encoded as a deterministic legal policy. Outreach, fee agreements and claim workflows remain out of scope and blocked pending later legal/compliance design and human approval.

## Provenance requirements for later acquisition

If any source is later approved for real acquisition, each acquired artifact must preserve at minimum:

- canonical source identifier;
- authoritative source URL;
- retrieval timestamp;
- acquisition method;
- raw immutable content or raw-file reference;
- SHA-256 content hash;
- source/version or publication/update date when available;
- access-policy/terms version or review date;
- transformation lineage for every normalized/derived record;
- append-only audit event linking acquisition to the source and raw artifact.

No inferred beneficiary or family relationship may be stored as a verified fact without independent evidence and the applicable human/governance gate.

## Readiness conclusion

The first California source inventory is complete.

**The M3 real-acquisition gate is NOT satisfied.**

Current classification:

- Preferred real-data candidate: `CA-SCO-UPD-BULK`, pending explicit contract/privacy approval.
- Privacy review required before real use: `CA-SCO-ESTATES`.
- Reference/manual source only for now: `CA-CDI-COMPANY-PROFILES`.
- Mock or deferred: `CA-CDI-NAIC-LIPL`, `CA-CDPH-DEATH`, `CA-COURTS-PROBATE`.

No scraping, bulk download, beneficiary matching, outreach, claimant verification, fee agreement or claim submission was performed as part of this task.

## Next recommended action

Define the M3 acquisition contract and adapter boundary for the preferred SCO bulk-download source, plus mock contracts for deferred sources. Only after those contracts, tests, privacy constraints and explicit source approval exist should a bounded real-data spike be considered.
