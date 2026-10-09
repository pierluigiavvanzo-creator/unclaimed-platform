# NY MVP-1 REAL P1 — CONTROLLER / LEGAL BASIS / TRANSPARENCY READINESS REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Mode: OFFLINE / DESIGN-REVIEW ONLY

Version: 1.1 — bifurcated US-controller vs EU-controller analysis

Result:

BIFURCATED_READY_FOR_CONTROLLER_OPERATING_MODEL_FACTS_NOT_READY_FOR_REAL_P1

This document is a software/privacy control review. It is not a legal opinion and does not replace qualified legal review.

## 1. Why the review was reformulated

The first version correctly treated GDPR applicability as unresolved because the repository does not identify the controller.

The Product Owner then raised a material operating-model question:

What changes if the Location Service Provider and platform owner is a US company serving the US market?

That question materially changes the territorial-scope analysis.

The correct project design is therefore not:

ASSUME GDPR

and not:

ASSUME NO GDPR.

It is:

SELECT CONTROLLER OPERATING MODEL -> VERIFY FACTS -> APPLY THE CORRECT LEGAL TRACK.

## 2. Baseline

Verified main checkpoint before this review:

cf00481f2824d163f9e325faf66482243ebc2024

Main CI:

36000390328 — SUCCESS

Canonical P1 architecture:

- PRODUCT_STRATEGY_MVP1 v3.0;
- D-012 Targetable Opportunity policy;
- D-013 two-pass P1 runner;
- seven fresh P1 gate templates, all NOT_GRANTED.

No source access, preflight, download, real PII processing or P1 execution occurred.

## 3. Controller identity remains a factual blocker

The canonical repository still contains no declaration of:

- exact controller legal name;
- entity type;
- incorporation/formation jurisdiction;
- principal establishment;
- privacy contact;
- EU establishment;
- EU targeting;
- EU monitoring;
- EU processor/contractor access to real owner PII.

Those facts cannot be inferred from:

- Product Owner identity;
- GitHub account;
- personal residence;
- developer location;
- ownership of the source code;
- intended corporate structure.

The controller is determined by who actually decides the purposes and essential means of the processing.

## 4. Track A — US controller / US market

### Proposed MVP hypothesis

The preferred simplification hypothesis is:

US LEGAL ENTITY
-> owns/operates the platform
-> acts as the Location Service Provider
-> determines purposes and essential means
-> contracts with US customers
-> receives the service fee
-> targets the US market
-> does not target or monitor people in the EU
-> has no EU establishment whose activities are connected to P1.

If those facts are true, the US controller is likely outside GDPR controller scope under Article 3.

This is not yet a legal determination because the entity and operational facts do not yet exist in the repository.

### Consequence if Track A is confirmed

The following GDPR-controller items would no longer be blockers merely for this P1 processing:

- Article 6 legal basis;
- Article 14 controller transparency;
- Article 21 controller objection mechanism;
- GDPR ROPA;
- GDPR DPIA.

US / New York legal, privacy, security and consumer-protection review would still remain required.

The project must not interpret "GDPR outside scope" as "data unrestricted".

## 5. Track B — EU controller or relevant EU establishment

If the controller is established in the EU, GDPR Article 3(1) applies to processing in the context of that establishment regardless of where the processing physically occurs.

The US source does not remove GDPR applicability.

The fact that the data subjects are in the US does not remove Article 3(1) when the processing occurs in the context of an EU establishment.

The same track can become relevant where a US controller has an EU establishment and the P1 processing is sufficiently connected to the activities of that establishment.

If Track B is triggered, the previous blockers remain:

- Article 6 basis;
- LIA if Article 6(1)(f) is selected;
- full-file necessity/minimisation;
- Article 14 path;
- Article 21 process if legitimate interests is used;
- ROPA by project policy;
- DPIA screen by project policy.

## 6. Track C — non-EU controller targeting or monitoring the EU

A non-EU controller may still enter GDPR scope under Article 3(2) if its processing relates to:

- offering goods or services to data subjects in the EU; or
- monitoring their behaviour in the EU.

Current MVP intent is:

NO EU TARGETING
NO EU MONITORING
US MARKET ONLY.

That intent must become an operational constraint if the US-controller track is selected.

## 7. Important distinction — EU processor is not automatically an EU establishment of the US controller

EDPB Guidelines 3/2018 require controller and processor territorial scope to be assessed separately.

An EU processor does not become an establishment of a non-EU controller merely because it processes data on that controller's behalf.

Therefore:

US CONTROLLER + EU PROCESSOR

does not automatically mean:

US CONTROLLER SUBJECT TO GDPR CONTROLLER OBLIGATIONS UNDER ARTICLE 3(1).

However:

- the EU processor may itself be subject to GDPR processor obligations;
- controller/processor roles and contract must be reviewed;
- the factual relationship must remain genuinely processor-like;
- an EU entity/person that actually determines purposes or essential means may not be only a processor.

## 8. Preferred MVP privacy architecture

To keep the US-controller hypothesis factually clean and reduce cross-jurisdiction complexity, the proposed MVP architecture is:

### Controller plane

US LSP/controller owns and operates the platform for the US market.

### Production PII plane

US-hosted and US-operated by default.

### EU development plane

Synthetic or non-PII data only by default.

### Live owner PII access from the EU

PROHIBITED BY DEFAULT.

Any future exception requires a separate review of:

- role;
- territorial scope;
- processor/controller status;
- contract;
- security;
- access necessity.

### Market boundary

No EU customer targeting.

No EU data-subject monitoring.

This architecture is a project-risk control.

It must not be used as a nominal arrangement whose operational reality is different.

## 9. New York / US track still requires real legal readiness

A confirmed US-controller track does not eliminate the legal work.

The project must still address at least:

- NY OSC Location Service Provider rules;
- ABP §1416 agreement requirements and fee cap;
- GBS §393-e direct-free-claim disclosure;
- NY security/disposal obligations where applicable;
- provider/data-source terms;
- FCRA/consumer-report status before using external identity tools;
- outreach-channel law before outreach;
- security/minimisation for the full Owner Name File;
- corporate authority and customer contracting.

The exact complete US-law inventory must be reviewed for the final entity and workflow before real P1.

## 10. Full Owner Name File remains a material privacy/security event on either track

Even if GDPR controller scope is ultimately outside Track A, the project should not downgrade full-file acquisition.

P1 may acquire a source containing millions of names and last-known addresses to identify one candidate.

Therefore project policy remains:

- bounded acquisition;
- transient local handling;
- no repository persistence;
- no cloud sync;
- strict access control;
- logical deletion;
- no raw-row output;
- one candidate maximum;
- necessity/minimisation review.

These safeguards remain economically and operationally valuable even if GDPR is not the governing controller regime.

## 11. L1 direct-PII issue remains cross-track

The real runner can decode Owner Name, Property ID and Holder Name at L1.

If L2-A is not authorized, L1 itself does not use those identifiers for targetability research.

Therefore:

L1_ONLY_DIRECT_PII_NECESSITY = NOT ESTABLISHED.

Preferred design remains:

A. no-direct-PII L1 where technically sufficient;

or

B. pre-authorized L1 + L2-A so direct PII is opened only for an approved targetability purpose.

No runtime modification is authorized by this review.

## 12. Operating-model decision matrix

| Fact pattern | GDPR controller track |
|---|---|
| Genuine US controller, no relevant EU establishment, US-only market, no EU targeting/monitoring | Likely outside GDPR controller scope, subject to factual/legal confirmation |
| EU controller | GDPR Article 3(1) track |
| US controller with relevant EU establishment tied to P1 | Potential Article 3(1) track |
| Non-EU controller targeting/monitoring people in EU | Article 3(2) track |
| US controller using EU processor only | Does not automatically bring US controller into Article 3(1); EU processor may have own GDPR obligations |

## 13. Required facts before selecting a track

The Product Owner must supply or formally select:

1. operating model: US controller, EU controller, or other;
2. exact controller legal name;
3. entity type;
4. formation/incorporation jurisdiction;
5. principal business/establishment address;
6. whether any EU branch, office, employee, agent or other stable arrangement is involved in P1;
7. whether any EU person/entity will access real Owner Name File PII;
8. who signs LSP customer agreements;
9. who receives the LSP fee;
10. confirmation that MVP1 targets the US market only and does not monitor people in the EU;
11. privacy contact if defined.

If the US company has not yet been formed, that fact should be recorded explicitly rather than inventing a controller.

## 14. Fail-closed state

No real P1 may start while any of these remain unresolved:

- operating model;
- legal controller identity;
- establishment facts;
- EU establishment relevance;
- EU targeting/monitoring;
- EU live-PII access;
- selected legal track;
- US/NY legal signoff or GDPR-track readiness as applicable;
- L1 direct-PII necessity;
- final legal review.

All seven P1 gates remain NOT_GRANTED.

## 15. Updated result

The correct result is no longer a single GDPR-centric failure.

It is:

BIFURCATED_READY_FOR_CONTROLLER_OPERATING_MODEL_FACTS_NOT_READY_FOR_REAL_P1

Meaning:

- the US-controller/US-market model is a credible simplification path;
- GDPR controller obligations should not be imposed by default if that track is factually true;
- the EU-controller/GDPR path remains available and fully specified;
- no track can be finalized until the actual controller and operational facts are supplied.

## 16. Human review gate

Review phrase remains:

APPROVE_NY_MVP1_CONTROLLER_LEGAL_BASIS_TRANSPARENCY_READINESS_FINDINGS_V1

Approval means:

- accept the bifurcated US/EU framework;
- accept US-controller/US-market as the preferred MVP hypothesis pending facts;
- accept EU-production PII segregation by default;
- accept that no real P1 gate may yet be granted.

Approval does NOT:

- form a US company;
- declare the controller;
- determine GDPR definitively;
- approve source access;
- approve PII processing;
- approve any P1 execution grant.

## 17. Next action after approval

HUMAN_SELECT_P1_CONTROLLER_OPERATING_MODEL_AND_SUPPLY_ENTITY_FACTS

If the intended path is US-controller/US-market, the factual record must identify the real US legal entity and confirm the conditions listed above.

Only after those facts exist should the project complete the track-specific legal readiness review.
