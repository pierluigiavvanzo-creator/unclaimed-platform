# MVP1 COMPETITIVE MOAT GATE — 2026-09-24

Classification: A — Product Critical

Mode: rapid external competitive / prior-art review

Result:

PASS_WITH_REFRAME_CONTINUE_STAGE_B

## 1. Decision

The project MUST NOT claim:

- first AI unclaimed-property platform;
- no competitors;
- unique owner-location technology;
- unique unclaimed-property case prioritization;
- unique end-to-end recovery workflow.

Those claims are not supported.

The project MAY continue Stage B around a narrower moat hypothesis:

NY_IN03_VALUE_BLIND_TARGETABILITY_ENGINE

Definition:

select one persistent NY OSC IN03 beneficiary-proceeds opportunity without knowing recoverable value; determine MATERIAL SERVICE NEED and BOUNDED RESOLVABILITY at measured TARGETABILITY_DECISION_COST; stop when evidence/cost becomes unbounded; preserve a privacy-minimized audit trail before outreach/value research.

This is a differentiation hypothesis, not a proven moat.

## 2. Closest competitive evidence

### ClaimTrace — closest workflow competitor

Public documentation shows that ClaimTrace:

- imports California State Controller property data;
- vets/scores properties using recoverable value, owner tractability and risk signals;
- explicitly frames vetting as choosing which cases are worth working;
- performs owner/heir/contact research;
- has evidence-aware research agents;
- supports outreach, agreements, claim packets and payment ledger;
- enforces California-specific legal workflow gates.

Public sources:

https://claimtrace.tech/docs/how-it-works
https://claimtrace.tech/features
https://claimtrace.tech/docs/getting-started
https://claimtrace.tech/pricing
https://claimtrace.tech/docs/compliance-1582

Conclusion:

The broad idea "score/filter unclaimed-property cases before spending effort" is NOT unique.

Material difference from our current MVP:

ClaimTrace is currently California-specific and publicly describes recoverable-value/dollar-floor inputs. NY OSC's Owner Name File does not disclose recoverable value, so our P1 is intentionally value-blind and optimizes service need + resolvability + measured decision cost.

### Assethound.ai

Public site describes:

- 39+ official registries;
- AI confidence scoring;
- AI ranking/briefing of which leads to pursue;
- People Finder / skip trace;
- contract builder;
- fee calculator;
- CRM/claims workflow.

Source:

https://assethound.ca/

Conclusion:

AI lead ranking + owner research + recovery workflow is NOT unique.

### Heir Crown

Public site describes:

- AI and machine learning;
- asset discovery;
- proprietary software with humans in the loop to predict owners;
- public, private and deep-web data;
- heir/beneficiary location;
- contingency recovery workflow.

Source:

https://heircrown.com/

Conclusion:

AI/human-in-loop owner/heir resolution is NOT unique.

### Sparrow Claim

PCRA describes Sparrow as a technology-enabled asset recovery platform using proprietary technology and AI-powered research to identify owners of unclaimed funds. Sparrow also publicly offers multi-database search, claim assistance and future-property monitoring.

Sources:

https://pcrainc.com/member-profiles/sparrow-claim/
https://www.sparrowclaim.com/

Conclusion:

AI-enabled owner discovery plus claim handling is NOT unique.

### Linking Assets

Public site describes owner location, deceased-owner identification, foreign owners/beneficiaries, estate representatives, legal claimants and estate documentation.

Source:

https://www.linkingassets.com/services/

Conclusion:

estate/beneficiary resolution is an established service category.

### Ryan

Public materials describe public/proprietary data sources, owner location, deceased-owner/next-of-kin research, outreach and end-to-end asset recovery.

Sources:

https://www.ryan.com/about-ryan/press-room/2015/ryan-launches-new-abandoned-and-unclaimed-property-search-and-location-practice-will-mitigate-client-escheatment-and-reduce-administrative-burdens/
https://www.ryan.com/practice-areas/abandoned-and-unclaimed-property/

Conclusion:

technology-assisted owner research and asset recovery are established.

### ClaimFound

Public site describes centralized find/recover/monitor unclaimed money.

Source:

https://claimfound.com/

Conclusion:

consumer aggregation and automated monitoring are established.

### AssetFynd

Public site describes an AI-first global platform searching hundreds of sources, matching owners/assets, continuous monitoring and success-based recovery.

Sources:

https://www.assetfynd.com/about
https://www.assetfynd.com/solutions

Conclusion:

large-scale AI search/matching is established.

### Life-insurance beneficiary recovery specialists

Consumers Asset Recovery Services publicly describes investigations that locate beneficiaries unaware of old life-insurance proceeds and assist claims.

Source:

https://www.consumersassetrecoveryservices.com/

Conclusion:

life-insurance-beneficiary discovery/recovery itself is NOT unique.

## 3. Capability comparison

Legend:

YES = explicitly supported by public material.
PARTIAL = adjacent capability publicly supported.
NOT FOUND = not found in reviewed public material; this does NOT prove absence.

| Capability | Our MVP hypothesis | ClaimTrace | Assethound | Heir Crown | Sparrow | Linking Assets |
|---|---|---|---|---|---|---|
| State/public-file ingestion | YES | YES | YES | PARTIAL | YES | PARTIAL |
| AI/ML owner or lead research | future / bounded | YES | YES | YES | YES | NOT FOUND |
| Heir / estate path | T2 | YES | YES | YES | PARTIAL | YES |
| Case prioritization before outreach | YES | YES | YES | PARTIAL | NOT FOUND | PARTIAL |
| Explicit owner tractability/resolvability | YES | YES | PARTIAL | YES | PARTIAL | YES |
| Recoverable-value ranking | deliberately NO in NY P1 | YES | YES/estimates | NOT FOUND | NOT FOUND | NOT FOUND |
| Explicit measured pre-value decision cost | YES | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Explicit bounded STOP when research cost/scope becomes unbounded | YES | PARTIAL/gates | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Value-blind NY IN03 specialization | YES | NO/publicly CA-focused | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| L1 no-direct-PII materialization + transient PII policy | YES | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| Economic Case Ledger before outreach/value | YES | PARTIAL/payment/audit | PARTIAL | NOT FOUND | NOT FOUND | NOT FOUND |

## 4. What remains differentiated

The credible differentiator is NOT one isolated feature.

It is the combination:

1. NY OSC exact IN03 beneficiary-proceeds vertical;
2. value-blind selection because source amount is unavailable;
3. persistence-first deterministic candidate selection;
4. separate SERVICE NEED and RESOLVABILITY axes;
5. TARGETABILITY_DECISION_COST measured before value/outreach;
6. explicit bounded stop-loss when the next information step becomes unbounded or unauthorized;
7. privacy-minimized L0/L1 with no durable direct owner PII;
8. evidence/provenance and human gates before each scope expansion.

No reviewed competitor publicly presents this exact combination.

That statement is limited to reviewed public evidence and is NOT proof of global uniqueness.

## 5. Moat quality assessment

### Category moat

FAIL.

Unclaimed-property search, AI matching, heir research, recovery software and case prioritization already exist.

### Feature moat

WEAK TODAY.

Individual features are reproducible.

### Workflow moat

PLAUSIBLE BUT UNPROVEN.

The NY-IN03/value-blind targetability workflow is narrower and meaningfully different, but competitors could reproduce it.

### Data/economic moat

MOST PROMISING.

The defensible asset could become a proprietary empirical dataset linking:

- source persistence;
- service-need evidence;
- resolvability evidence;
- estate/representative path;
- targetability class;
- TARGETABILITY_DECISION_COST;
- later outreach conversion;
- later value/recovery evidence.

The moat exists only after real P1/P2/P3 outcomes are accumulated.

## 6. Prior-art screen

This is NOT a freedom-to-operate or patentability opinion.

Relevant prior art includes:

### US7054833B1

Method and system for processing unclaimed property information.

Priority 2000; granted 2006; current Google Patents status shown as expired.

It describes acquiring/unifying unclaimed-property data, automatically locating owners through public/private networks, notifying owners and supporting disbursement.

Source:

https://patents.google.com/patent/US7054833B1/en

### US20230351514A1

Apparatus and method for automatic unclaimed property search and processing.

Public record describes AI/ML used to generate/search unclaimed-property data. Google Patents shows abandoned status after final rejection/failure to respond.

Source:

https://patents.glgoo.top/patent/US20230351514A1/en

### US20220391904A1 / related international family

Automated systems and methods for electronic asset recovery.

The public patent family describes dormant-account/asset-owner processing, status determination, contact enrichment and recovery workflows.

Source:

https://patents.google.com/patent/US20220391904A1/en

Conclusion:

Broad claims around automating unclaimed-property search, owner identification and recovery are prior-art dense.

Do not spend on a broad "AI + unclaimed property" patent strategy before specialist patent counsel identifies a genuinely narrow claim set.

## 7. Competitive moat gate outcome

GATE_RESULT:

PASS_WITH_REFRAME_CONTINUE_STAGE_B

Killed hypotheses:

- WE_ARE_THE_FIRST_UNCLAIMED_AI_PLATFORM
- NO_DIRECT_COMPETITORS_EXIST
- CASE_PRIORITIZATION_ITSELF_IS_UNIQUE
- OWNER_LOCATION_AI_IS_THE_MOAT

Retained hypothesis:

NY_IN03_VALUE_BLIND_TARGETABILITY_ENGINE

Proof required:

P1/P2/P3 must show that the system can identify bounded, service-relevant opportunities at sufficiently low TARGETABILITY_DECISION_COST to justify later outreach/value stages.

If it cannot, the claimed differentiation has little commercial value.

## 8. LLC formation gate

Do NOT form an LLC because the category is unique. It is not.

If the Product Owner chooses to form an entity to enable real Stage B, the current bootstrap default remains:

WYOMING LLC

subject to US CPA/attorney review and New York nexus/foreign-qualification analysis.

Current official facts reviewed:

### Wyoming

- LLC filing fee: USD 100.
- annual report/license tax: minimum USD 60 or asset-based amount if higher.
- Wyoming Business Council states no Wyoming corporate or personal state income tax.

Sources:

https://sos.wyo.gov/Forms/Business/LLC/LLC-ArticlesOrganization.pdf
https://sos.wyo.gov/business/docs/businessfees.pdf
https://wyomingbusiness.org/why-wyoming/business-resources/

### Delaware

Current Delaware Code and current tax instructions state USD 400 annual LLC tax.

Sources:

https://delcode.delaware.gov/title6/c018/sc11/
https://corp.delaware.gov/alt-entitytaxinstructions/

Delaware is not preferred for this bootstrapped MVP solely for prestige.

### Florida

- required LLC formation filing + registered-agent designation: USD 125;
- annual report: USD 138.75.

Source:

https://dos.fl.gov/sunbiz/forms/fees/llc-fees

### Texas

- LLC formation fee: USD 300;
- 2026/2027 franchise-tax no-tax-due threshold: USD 2.65 million.

Sources:

https://www.sos.state.tx.us/corp/instructions/205.shtml
https://comptroller.texas.gov/taxes/franchise/

### New York

- domestic LLC filing fee: USD 200;
- foreign LLC Application for Authority: USD 250;
- NY publication requirements can apply to domestic/authorized foreign LLCs, generally once weekly for six successive weeks in two newspapers.

Sources:

https://dos.ny.gov/forming-limited-liability-company-new-york
https://dos.ny.gov/system/files/documents/2023/01/1361-f.pdf
https://dos.ny.gov/node/35461

Whether a Wyoming LLC must qualify in NY depends on the actual facts of doing business and must be reviewed before operations.

### Federal foreign-owner compliance

IRS Form 5472 rules can apply to a foreign-owned US disregarded entity.

The IRS states the failure-to-file penalty is USD 25,000, with additional continuation penalties possible.

Source:

https://www.irs.gov/instructions/i5472

Conclusion:

The federal compliance design is economically more important than saving a few hundred dollars in state filing fees.

## 9. Incorporation timing recommendation

LLC_FORMATION_TIMING:

JUST_IN_TIME_BEFORE_REAL_P1_FRESH_GATES

Reason:

- all remaining offline Stage B design is already substantially prepared;
- entity formation creates ongoing tax/compliance obligations;
- real P1 requires a genuine controller;
- the Competitive Moat Gate supports continuing to P1 but does not justify premature scale.

## 10. Return to Stage B

Competitive detour ends here.

Canonical next product objective returns to:

STAGE_B_PILOT_P1

Immediate dependency:

HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1

Preferred bootstrap hypothesis:

WYOMING LLC

Before formation:

US CPA / attorney should confirm:
- foreign-owned LLC federal tax treatment;
- Form 5472 / pro-forma Form 1120 obligations;
- beneficial-ownership/reporting obligations then applicable;
- NY foreign-qualification/nexus implications for the planned LSP workflow.

After formation:

bind controller facts -> prepare fresh single-use gates -> ONE REAL P1 -> human economic review.
