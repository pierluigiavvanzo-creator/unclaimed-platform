# NY MVP-1 REAL P1 — CONTROLLER / LEGAL BASIS / TRANSPARENCY READINESS REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Mode: OFFLINE / DESIGN-REVIEW ONLY

Result:

CONDITIONAL_FAIL_NOT_READY_FOR_REAL_P1

This document is a software/privacy control review. It is not a legal opinion and does not replace qualified legal review.

## 1. Baseline

Canonical main checkpoint verified before this review:

cf00481f2824d163f9e325faf66482243ebc2024

Main CI:

36000390328 — SUCCESS

Canonical P1 architecture:

- PRODUCT_STRATEGY_MVP1 v3.0;
- D-012 Targetable Opportunity policy;
- D-013 two-pass P1 runner;
- seven fresh P1 gate templates, all NOT_GRANTED.

No source access, preflight, download, real PII processing or P1 execution occurred during this review.

## 2. Repository finding — controller identity is absent

A repository search found no canonical declaration for:

- data controller / titolare del trattamento;
- legal entity operating P1;
- controller establishment;
- privacy contact;
- DPO;
- joint-controller allocation.

This is blocking.

Under GDPR Article 4(7), the controller is the natural or legal person, authority, agency or other body which determines the purposes and means of processing.

The project cannot safely infer a controller from the Product Owner identity, repository owner name, account name, developer identity, business idea or geographic location.

Required fields before real execution:

- legal name;
- entity type;
- jurisdiction;
- establishment country/address;
- privacy contact;
- controller role;
- processor inventory;
- joint-controller status;
- DPO requirement assessment;
- EU representative assessment if applicable.

## 3. GDPR territorial scope

Article 3(1) GDPR applies to processing in the context of the activities of an establishment of a controller or processor in the Union, regardless of whether the processing itself takes place in the Union.

Therefore:

- US source data is not automatically outside GDPR;
- US data subjects are not automatically outside GDPR where Article 3(1) applies;
- public availability is not a general GDPR exemption.

If the actual controller is not established in the Union, Article 3(2) requires a separate assessment of whether processing relates to offering goods/services to data subjects in the Union or monitoring their behaviour there.

Current conclusion:

GDPR_APPLICABILITY = UNRESOLVED

because controller identity and establishment are unresolved.

Official source:

https://eur-lex.europa.eu/eli/reg/2016/679/

## 4. Important scope correction — the whole file is part of the processing

The current P1 technical design selects only one candidate, but the real source workflow first acquires the Owner Name File.

Attempt 11 established a source population of:

14,994,489 physical records.

OSC states that the downloadable list includes names and last-known addresses of persons or entities that may be entitled to unclaimed funds.

Therefore, where those fields are personal data under applicable law:

DOWNLOAD + TRANSIENT LOCAL STORAGE + STREAMING

are themselves processing operations.

It is not sufficient to reason only about the one selected candidate.

The fact that L0 does not use Owner Name/address for ranking is an important safeguard, but it does not transform the complete downloaded file into non-personal data.

This materially changes the legal-readiness question:

CAN THE CONTROLLER LAWFULLY AND NECESSARILY ACQUIRE THE FULL OWNER FILE TO SELECT ONE TARGET CASE?

Official OSC source:

https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers

## 5. New York source / location-service framework

Official NY OSC materials support all of the following:

- direct OSC claim processing is free;
- OSC recognizes Abandoned Property Location Service Providers;
- OSC provides a downloadable list to support research;
- that list contains names, last-known addresses, property nature, reporter and reporting time;
- OSC does not disclose claim amount or taxpayer identification number in the list;
- a provider agreement is required for the service-provider claim path.

New York Abandoned Property Law §1416:

- regulates fee-based abandoned-property location services;
- requires specified agreement disclosures;
- caps the applicable fee at 15 percent of recoverable property.

New York General Business Law §393-e requires the direct-free-claim disclosure in solicitation and agreements.

These provisions support the existence of the business/service framework.

They do NOT by themselves establish:

- an EU GDPR Article 6 basis;
- a blanket right to enrich owner data;
- a blanket right to contact anyone by any channel;
- a privacy exception for all downstream processing.

Official sources:

https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers

https://www.nysenate.gov/legislation/laws/ABP/1416

https://www.nysenate.gov/legislation/laws/GBS/393-E

## 6. New York data-security laws — narrower than project policy

NY GBL §899-aa defines personal information broadly but defines the separate category private information through specified sensitive combinations; lawfully public government-record information is excluded from that statutory private-information definition.

NY GBL §899-bb imposes reasonable safeguards on businesses owning or licensing computerized data containing private information of New York residents.

NY GBL §399-h separately regulates disposal of records containing specified personal identifying information.

The current OSC source is intentionally treated more strictly by project policy than the narrow statutory private-information category.

Project rule remains:

OWNER NAME / LAST-KNOWN ADDRESS / PROPERTY IDENTIFIER = OWNER PII FOR GOVERNANCE PURPOSES.

No project privacy control is relaxed merely because information is publicly available.

Official sources:

https://www.nysenate.gov/legislation/laws/GBS/899-AA

https://www.nysenate.gov/legislation/laws/GBS/899-BB

https://www.nysenate.gov/legislation/laws/GBS/399-H

## 7. Article 6 legal-basis assessment if GDPR applies

No final legal basis is selected by this review.

### Consent — not suitable for pre-contact P1

Pre-contact discovery occurs before the potential customer has provided consent.

Result:

NOT CURRENTLY SUITABLE.

### Contract / pre-contract request — not suitable for pre-contact P1

P1 is not initiated at the request of the candidate and there is no existing contract with that person.

Result:

NOT CURRENTLY SUITABLE.

### Legal obligation

No controller-specific legal obligation requiring this P1 processing has been identified.

Result:

NOT ESTABLISHED.

### Vital interests

Commercial targetability research is not designed to protect a vital interest.

Result:

NOT CURRENTLY SUITABLE.

### Public task / official authority

The project has not established that the controller is vested with a public task or official authority.

Result:

NOT ESTABLISHED.

### Legitimate interests — plausible candidate only

Article 6(1)(f) is the only currently plausible pre-contact candidate in this design if GDPR applies.

It is NOT approved by this review.

EDPB Guidelines 1/2024 describe three cumulative conditions:

1. a lawful, clearly articulated, real and present legitimate interest;
2. necessity of the processing for that interest, including consideration of less intrusive means;
3. a balancing exercise showing the data subject's interests/fundamental rights do not override the interest.

The proposed interest to test is:

LAWFUL COMMERCIAL INTEREST IN IDENTIFYING AND EVALUATING POTENTIAL NY UNCLAIMED-PROPERTY LOCATION-SERVICE CASES WHERE ASSISTANCE MAY CREATE REAL SERVICE VALUE.

A documented LIA must answer at minimum:

- Is that interest lawful, specific, real and present?
- Is acquiring the whole Owner Name File necessary?
- Can substantially equivalent P1 evidence be obtained by a less intrusive source or source-side filter?
- What would a person reasonably expect from publication in the OSC list?
- What impact can selection, identity research and possible future contact have?
- What safeguards materially reduce that impact?
- What happens on objection?

EDPB source:

https://www.edpb.europa.eu/public-consultations/guidelines-12024-on-processing-of-personal-data-based-on-article-61f-gdpr_en

GDPR source:

https://eur-lex.europa.eu/eli/reg/2016/679/

## 8. Data minimisation / necessity — current blocking issue

GDPR Article 5 requires data minimisation and storage limitation.

Article 25 requires protection by design/default so that, by default, only data necessary for each purpose are processed.

Current design has a material mismatch:

BUSINESS EXPERIMENT:

one P1 candidate.

SOURCE ACQUISITION:

potentially millions of identifiable source records.

Transient deletion reduces duration and exposure, but does not eliminate the processing.

Before real acquisition, one of these must be supported:

A. documented necessity/proportionality showing that full-file acquisition is reasonably necessary for the one-candidate selection purpose;

or

B. a technically and commercially viable less-intrusive acquisition method.

This review does not assert that a source-side filter exists.

Current state:

BLOCKING_ASSESSMENT_REQUIRED.

## 9. Article 14 transparency

If GDPR applies, the Owner Name File data are not obtained from the data subject.

Article 14 therefore becomes the default transparency framework.

Article 14 ordinarily requires information including:

- controller identity/contact;
- purpose/legal basis;
- categories of personal data;
- recipients/categories;
- retention period or criteria;
- legitimate interest where relied upon;
- rights;
- right to complain;
- source and whether publicly accessible;
- automated-decision information where applicable.

Timing is ordinarily:

- within a reasonable period, no later than one month after obtaining data;
- at the latest at first communication if the data are used to communicate;
- at the latest at first disclosure if data are disclosed first.

Article 14(5) contains exceptions, including where providing information proves impossible or would involve disproportionate effort under the conditions stated there.

This project MUST NOT assume the exception.

Current design has a conflict:

- L1 prohibits outreach;
- L1 has no transparency-notice mechanism;
- full-file acquisition may involve millions of data subjects;
- same-session deletion does not itself create an Article 14 exception.

Therefore:

ARTICLE_14_PATH = UNRESOLVED_BLOCKING_IF_GDPR_APPLIES.

Permissible future outcomes require human legal review:

1. a direct Article 14 notice design where legally/operationally appropriate;
2. a specifically documented Article 14(5) exception analysis with required safeguards/public information;
3. a redesign that materially changes the processing so the obligation is addressed differently.

The project must not select one automatically.

Official GDPR source:

https://eur-lex.europa.eu/eli/reg/2016/679/

Transparency guidance:

https://www.edpb.europa.eu/system/files/2023-09/wp260rev01_en.pdf

## 10. Article 21 objection

If Article 6(1)(f) is ultimately selected, Article 21 gives the data subject a right to object on grounds relating to their particular situation.

The controller must be able to stop processing unless it can demonstrate the grounds allowed by Article 21.

At first communication, the right to object must be brought explicitly to the data subject's attention.

Current project state:

OBJECTION PROCESS = NOT IMPLEMENTED.

This is blocking before any outreach and must be part of legal readiness if legitimate interests is chosen.

## 11. Accountability / records

If GDPR applies, the design must support:

- Article 5 principles/accountability;
- Article 24 controller accountability;
- Article 25 privacy by design/default;
- data-subject rights handling;
- incident-response ownership;
- access-control ownership;
- retention schedule.

The project will require a Record of Processing Activities entry before real P1 as a governance rule, even if a controller later believes an Article 30 small-organisation exception could technically apply.

This is deliberately stricter and removes ambiguity.

## 12. DPIA screening

Article 35 requires a DPIA where the contemplated processing is likely to result in high risk, considering nature, scope, context and purpose.

This review does not make a final legal conclusion that a DPIA is mandatory.

However, the project has several risk drivers:

- millions of identifiable source records in the acquired file;
- commercial targetability selection;
- intended identity/contactability research at L2-A;
- planned repeated use if the pilot succeeds.

Project decision proposed:

DPIA_SCREEN_REQUIRED_BEFORE_REAL_P1_IF_GDPR_APPLIES.

The controller must also check the applicable supervisory authority's Article 35 list once establishment is known.

If the screen is positive:

FULL DPIA BEFORE PROCESSING.

## 13. Additional minimisation finding — real L1-only is weakly justified

The current runner can transiently decode:

- Property ID;
- Owner Name;
- Holder Name;

even when L2-A is not authorized.

For a real L1-only run, the project has not established that these direct identifiers are necessary, because L1 by itself does not perform targetability research.

This is a material privacy-by-design issue.

Preferred project constraint:

DO NOT EXECUTE REAL L1-ONLY WITH DIRECT OWNER PII UNLESS NECESSITY IS DOCUMENTED.

Preferred future architecture:

- either make real L1 no-direct-PII where possible;
- or authorize a legally-ready L1 + L2-A session in advance so direct PII is processed only when it serves an approved targetability purpose.

No runtime change is authorized by this review.

## 14. Readiness matrix

| Requirement | State |
|---|---|
| Controller legal identity | BLOCKING / UNKNOWN |
| Controller establishment | BLOCKING / UNKNOWN |
| Applicable law | BLOCKING / UNKNOWN |
| GDPR Article 6 basis | NOT SELECTED |
| Article 6(1)(f) LIA | NOT COMPLETED |
| Full-file necessity | NOT ESTABLISHED |
| Article 14 path | BLOCKING / UNRESOLVED if GDPR applies |
| Article 21 objection path | NOT IMPLEMENTED |
| ROPA | NOT CREATED |
| DPIA screen | NOT COMPLETED |
| Exact retention schedule | NEEDS LEGAL-READINESS RECORD |
| Data-subject rights procedure | NOT IMPLEMENTED |
| L1-only direct-PII necessity | NOT ESTABLISHED |
| Seven P1 execution gates | ALL NOT_GRANTED |

## 15. Fail-closed result

RESULT:

CONDITIONAL_FAIL_NOT_READY_FOR_REAL_P1

This means:

- the product direction is not rejected;
- the NY location-service business model is not rejected;
- legitimate interests is not rejected;
- P1 is not abandoned.

It means only that a real P1 must not be authorized yet.

The current legal/privacy design has four material blockers:

1. controller identity/establishment;
2. lawful-basis determination;
3. full-file necessity/minimisation;
4. Article 14 transparency path.

## 16. Human decision

Recommended human review phrase:

APPROVE_NY_MVP1_CONTROLLER_LEGAL_BASIS_TRANSPARENCY_READINESS_FINDINGS_V1

Approval means:

- accept the findings and fail-closed state;
- accept that no real P1 gate may yet be granted;
- accept that controller identity/establishment must be supplied explicitly;
- accept the need to resolve full-file minimisation and Article 14 before execution.

Approval does NOT mean:

- approve legitimate interests as the legal basis;
- approve an Article 14 exception;
- approve download;
- approve PII processing;
- approve outreach;
- approve any of the seven P1 grants.

## 17. Next action after review acceptance

Because controller identity cannot be invented from the repository, the next required human input is:

DEFINE_P1_CONTROLLER_IDENTITY_AND_ESTABLISHMENT

Required factual fields:

- exact controller legal name;
- entity type;
- country/jurisdiction of establishment;
- establishment/business address;
- privacy contact address/email if already defined.

After those facts exist, the project can execute:

COMPLETE_P1_APPLICABLE_LAW_LIA_TRANSPARENCY_AND_DPIA_SCREEN_OFFLINE

No source access is needed for either action.
