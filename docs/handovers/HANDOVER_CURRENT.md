# HANDOVER_CURRENT.md

Last updated: 2026-09-23

## AUTHORITATIVE CURRENT STATE — PRODUCT VALIDATION MODE

Repository: `pierluigiavvanzo-creator/unclaimed-platform`

Canonical integration branch: `main`

Objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

## Consumed real attempts relevant to current state

### Attempt 9

Consumed/non-reusable/zero-retry whole-file structural scan.

Authoritative evidence:

`sources/evidence/ny_osc_owner_name_file_ninth_attempt_execution_result.v1.json`

Key aggregate result: `14994489` physical records, terminal-empty-field hypothesis rejected, no owner/raw values returned.

### Attempt 10

Consumed/non-reusable/zero-retry.

Authoritative evidence:

`sources/evidence/ny_osc_owner_name_file_tenth_attempt_execution_result.v1.json`

Result:

- status `BLOCKED`;
- reason `AUTHORIZED_DOWNLOAD_START_OUTSIDE_FRESH_PREFLIGHT_WINDOW`;
- manual download had occurred;
- classification/product slice never started;
- no candidate/zero-candidate result;
- no owner values returned.

Root cause: Gate 10 captured the download-start marker only after the Product Owner pressed Enter, and that marker landed outside the 900-second fresh-preflight window.

Do not reuse any Attempt-10 grant.

## Attempt 11 package — COMPLETED AND INTEGRATED

Branch:

`mvp1-ny-eleventh-auto-start-detection-offline`

Historical PR:

`#29 — MERGED`

Canonical integration PR:

`#30 — MERGED INTO main`

Main integration commit:

`c5a56be629b7a684666a8fc5ee57fec24ff734c4`

Proposal checkpoint:

`270de2f6e79b7c654052519adc446fe76b811771`

Runner/code checkpoint:

`bac89609e9069efc98fcd0866b89ee4ee16f1689`

CI:

`35859448715 — SUCCESS`

All Python quality/tests, Streamlit checks and frontend lint/typecheck/build passed.

Purpose:

`REAL PHYSICAL RECORDS -> STRUCTURAL DEFER/ACCEPT -> PROPERTY TYPE CODE -> INSURANCE CLASSIFICATION -> AGGREGATE CANDIDATE OR ZERO-CANDIDATE -> ECONOMIC ACTIONABILITY`

The Attempt-10 product slice is reused unchanged.

Gate 11 freshness remediation:

- minimum `180` freshness seconds remaining before download instruction;
- new dedicated empty temp directory;
- automatic detector armed before operator download instruction;
- `100 ms` polling;
- first observed non-empty file in the dedicated directory captures the UTC download-start marker;
- no operator Enter is used to mark transfer start;
- no detected start before deadline -> fail closed;
- one manual completion confirmation after the same download finishes;
- one download / one Gate 11 execution / zero retry;
- no direct network client.

Product boundary remains:

- exactly `13` pipes -> classify documented 14-field record;
- all other shapes -> metadata-only defer;
- only Property Type Code index `1` is buffered/decoded;
- exact existing authority-backed insurance vocabulary;
- `IN03` primary target;
- aggregate result only;
- no candidate/owner PII materialization;
- economics remain `UNKNOWN_FROM_SOURCE`.

No NY OSC source access, preflight, download or real PII processing occurred during Attempt-11 offline preparation.

## Attempt 11 listing metadata drift — 2026-09-23

The Attempt-11 local-file and transient-PII grants are already `GRANTED_NOT_CONSUMED`.

A refresh-3 metadata-only fresh-preflight was authorized. The Product Owner then refreshed the authenticated NY OSC outbound listing and supplied a screenshot showing:

- `FINDERS.zip`
- `390.51 MB`
- `9/23/2026, 1:12:44 PM`

The prior expected last-modified value was `9/16/2026, 1:33:31 PM`, so the preflight correctly failed closed and no receipt was created.

Repository-only drift review accepted the new observation only as a **future listing-metadata identity snapshot**:

`sources/evidence/ny_osc_owner_name_file_current_listing_metadata.v2.json`

Audit:

`docs/audits/NY_OSC_ELEVENTH_LISTING_METADATA_DRIFT_REVIEW.md`

No archive-content equivalence is inferred. No download, Owner Name File open or owner PII processing was authorized or performed by this review.

## Attempt 11 refreshed-listing runner rebind

A subsequent authenticated-listing screenshot exactly matched:

`FINDERS.zip | 390.51 MB | 9/23/2026, 1:12:44 PM`

Before creating a fresh receipt, repository inspection found that the protected Gate-11 runner still required the prior `9/16/2026` last-modified value.

The minimal metadata binding was updated without changing product-slice, privacy, retry or network behavior.

New protected runner checkpoint:

`bac89609e9069efc98fcd0866b89ee4ee16f1689`

CI:

`35859448715 — SUCCESS`

Audit:

`docs/audits/NY_OSC_ELEVENTH_REFRESHED_LISTING_RUNNER_REBIND.md`

The prior Attempt-11 local-file, transient-PII and refresh-4 fresh-preflight grants were not consumed, but they are bound to the previous runner checkpoint `ce005f08a3bbd23eb8fac6088917109f7864e924` and cannot be reused for the new protected package.

No new fresh receipt was created from that screenshot.

## Attempt 11 refreshed-runner grants

The two Attempt-11 grants have been reissued and recorded against protected runner checkpoint:

`bac89609e9069efc98fcd0866b89ee4ee16f1689`

CI for the protected runner:

`35859448715 — SUCCESS`

Current states:

- transient local file: `GRANTED_NOT_CONSUMED`;
- transient PII: `GRANTED_NOT_CONSUMED`.

No download, fresh preflight or Owner Name File open was performed while recording these grants.

## Attempt 11 real execution — COMPLETED

Attempt 11 completed one authorized bounded real product-slice execution.

Authoritative result:

`sources/evidence/ny_osc_owner_name_file_eleventh_attempt_execution_result.v1.json`

Audit:

`docs/audits/NY_OSC_ELEVENTH_ATTEMPT_PRODUCT_SLICE_COMPLETED.md`

Execution identity:

- proposal checkpoint: `270de2f6e79b7c654052519adc446fe76b811771`;
- protected runner checkpoint: `bac89609e9069efc98fcd0866b89ee4ee16f1689`;
- runner CI: `35859448715 — SUCCESS`;
- fresh receipt: `PREFLIGHT_RECEIPT_2026-09-23T122619Z_NY_OSC_ELEVENTH_EXACT_MATCH_REFRESH5_BAC89609`;
- execution authorization: `OWNER_APPROVAL_2026-09-23T122809Z_NY_OSC_ELEVENTH_BOUNDED_EXECUTION_ONCE_BAC89609`;
- automatically detected download start: `2026-09-23T12:30:59.478237Z`.

Execution result:

- status: `COMPLETED`;
- reason: `PRODUCT_SLICE_COMPLETED`;
- archive bytes: `409477526`;
- total records: `14994489`;
- structurally conforming: `14994477`;
- deferred structural: `12`;
- authority-backed insurance: `2792990`;
- primary `IN03` aggregate candidates: `203921`;
- other insurance: `2589069`;
- no authority-backed insurance match: `12201486`;
- unclassifiable Property Type Code: `1`;
- candidate outcome: `CANDIDATES_PRESENT_AGGREGATE_ONLY`;
- candidate materialization: `NOT_AUTHORIZED_AGGREGATE_ONLY`;
- economic actionability: `VALUE_EVIDENCE_REQUIRED`;
- recoverable value: `UNKNOWN_FROM_SOURCE`.

Privacy / retention result:

- owner values buffered: false;
- owner rows persisted: false;
- owner field logging: false;
- row-specific human inspection: false;
- raw record returned: false;
- owner values returned: false;
- local archive deleted: true;
- deletion is logical only; physical secure erasure is not guaranteed.

## Attempt 11 authorization state

The Attempt-11 single-use chain is consumed.

State:

`CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO_RETRY`

The following may not be reused:

- transient local-file grant;
- transient PII grant;
- refresh-5 preflight grant;
- final execution authorization.

No retry or second Attempt-11 download is authorized.

## Product interpretation

The parser/freshness critical blocker is closed for the current bounded vertical slice.

The source has demonstrated a material real funnel:

`14994489 records -> 2792990 authority-backed insurance -> 203921 primary IN03 aggregate candidates`

The project must now move downstream rather than return to parser/timing diagnostics.

Remaining MVP-1 path:

`ONE LAWFULLY MATERIALIZED CANDIDATE -> VALUE/EVIDENCE -> CASE ECONOMICS -> REVIEWER DECISION`

Existing repository components already exist for:

- deterministic candidate/classification contracts;
- fail-closed NY pre-contact value evidence;
- measured follow-up-cost contracts;
- explicit case economics;
- reviewer surfaces.

They should be reused before new custom implementation.

Current real-data boundary remains strict: candidate materialization, identity resolution, beneficiary matching, outreach, representation, fee agreements and claim activity are not authorized.

## One-candidate materialization/value-evidence offline proposal

Branch:

`mvp1-ny-one-candidate-value-evidence-offline-proposal`

Proposal:

`sources/proposals/ny_osc_one_candidate_value_evidence_offline_proposal.v1.json`

Schema:

`schemas/common/ny_osc_one_candidate_value_evidence_offline_proposal.schema.json`

Contract test:

`tests/contract/test_ny_osc_one_candidate_value_evidence_offline_proposal.py`

Review:

`docs/audits/NY_OSC_ONE_CANDIDATE_VALUE_EVIDENCE_OFFLINE_PROPOSAL_REVIEW.md`

Design summary:

- at most one candidate;
- first eligible record in physical source order;
- documented 14-field physical shape;
- exact `IN03`;
- Property Owner Count exactly `1`;
- non-empty Property ID;
- no PII-based ranking or random selection;
- transient scope: Property ID, Property Type Code, Property Owner Count, Owner Name, Holder Name, Holder Report Year;
- address fields excluded;
- Owner Name and Property ID not persisted;
- raw row and owner-row hash not persisted;
- persistent candidate envelope contains no owner PII;
- existing fail-closed value-evidence, follow-up-cost and economics components are reused;
- reviewer remains synthetic-only until a separately reviewed real-safe adapter exists.

No source access, download, candidate PII processing or value research occurred while preparing this proposal.

## Whole-project economic feasibility audit — 2026-09-23

Audit branch:

`audit-economic-feasibility-2026-09-23`

Audit:

`docs/audits/ECONOMIC_FEASIBILITY_AUDIT_2026-09-23.md`

Baseline:

`main @ 9873005e61a088f718aeb3093fdb57ac6827ab44`

Status:

`CONDITIONAL_CONTINUE_ECONOMIC_VALIDATION_NOT_SCALE`

Key finding:

The project has proven real candidate supply and technical screening, but has not yet proven unit economics. The primary economic risk is that exact case value is unavailable before claim review/ownership verification while customer acquisition/research/contact costs may occur earlier.

Current strategic rule:

`BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE`

Do not expand multi-agent architecture, multi-state sources, graph infrastructure, durable PII, genealogy or outreach systems until one real case produces measured value/cost/conversion evidence.

## ECONOMIC-FINANCIAL DEVELOPMENT DOCTRINE — BINDING FOR NEXT MVP-1 WORK

This section translates the 2026-09-23 economic-feasibility audit into concrete development priorities.

Primary rule:

`BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE`

The project has already proven candidate supply. From this point, development value is measured by how much a task reduces uncertainty about:

1. `VALUE`;
2. `PRE_VALUE_DISCOVERY_COST`;
3. `CONVERSION`;
4. `TIME_TO_CASH`;
5. `LEGAL_MONETIZATION`.

If a proposed implementation does not reduce at least one of those uncertainties and is not required for privacy/security/compliance, it is frozen by default.

### Economic objective

The technical funnel proven by Attempt 11 is:

`14994489 records -> 2792990 authority-backed insurance -> 203921 primary IN03 aggregate candidates`

The economic funnel to be measured is:

`SOURCE CANDIDATE`
`-> UNIQUE / ELIGIBLE CASE`
`-> IDENTIFIABLE`
`-> CONTACTABLE`
`-> CONTACTED`
`-> AGREEMENT`
`-> VALUE KNOWN`
`-> ECONOMICALLY VIABLE`
`-> CLAIM / RECOVERY`
`-> FEE BILLED`
`-> FEE COLLECTED`

No step may be treated as economically proven until measured on real cases with provenance.

## Lane model — allocate research cost by friction, not by guessed value

The Owner Name File does not expose exact property value. Therefore cases must not be ranked as "high-value" using unsupported proxies.

The initial commercial segmentation is based on **operational friction**, because friction determines both willingness to pay and expected service cost.

### Lane F0 — Easy / self-service dominant

Definition:

- owner appears straightforward to identify/contact;
- no obvious estate/deceased/complex-document condition;
- case appears likely to be serviceable directly through OSC with low friction;
- no evidence justifies material research spend.

Economic posture:

`MINIMUM_OR_ZERO_INCREMENTAL_SPEND`

Purpose:

avoid burning research cost on cases where the free State alternative is likely to dominate perceived value.

Allowed next step:

only low-cost automated screening and explicit defer/stop.

Do not perform expensive identity, genealogy, legal or manual research solely to rescue an F0 case.

Commercial hypothesis:

low priority for direct owner-paid service unless later evidence shows a low-cost assistance product with positive contribution.

### Lane F1 — Identifiable owner / assistance case

Definition:

- identity/contact path appears relatively simple;
- candidate may still benefit from process assistance, documentation coordination or convenience;
- no complex estate/legal condition is yet evidenced.

Economic posture:

`LOW_TOUCH / AUTOMATION_FIRST`

Goal:

test whether a low-cost location-service workflow can create sufficient convenience to overcome the free OSC alternative.

Measure:

- cost to confirm identity/contactability;
- contact success;
- agreement conversion;
- value-known rate;
- claim completion cost;
- fee collection.

Commercial hypothesis:

direct owner-paid location service may work only if acquisition/research/service cost is very low relative to realized fee.

### Lane F2 — Hard-to-identify / hard-to-contact candidate

Definition:

- stale/incomplete contact information;
- identity ambiguity;
- contact path requires additional lawful research;
- no full estate/court process is yet established.

Economic posture:

`BOUNDED_RESEARCH_WITH_STOP_LOSS`

Goal:

determine whether additional research buys enough information to justify the next spend.

Every F2 case must have:

- a current discovery stage;
- accumulated `PRE_VALUE_DISCOVERY_COST`;
- a next-information objective;
- a maximum incremental research budget;
- a stop reason if the next information cannot be obtained economically.

Commercial hypothesis:

potentially attractive only if research can be automated/standardized or recovered values are sufficiently high.

Do not build full genealogy/identity infrastructure before measured F2 cases demonstrate that this is the bottleneck and that solving it creates positive expected contribution.

### Lane F3 — Estate / deceased owner / complex documentation / professional-support case

Definition:

- deceased owner or estate path;
- heir/representative issues;
- court-appointed representative or significant documentation complexity may be required;
- the case has materially greater operational friction than F1/F2.

Economic posture:

`PREMIUM_COMPLEX_CASE / HUMAN_OR_PROFESSIONAL_SUPPORT`

Goal:

measure whether complexity creates enough willingness to pay and/or expected recovery contribution to support higher service cost.

Required measurements:

- legal/notary/external cost;
- internal research time;
- identity/estate documentation burden;
- time to value evidence;
- time to recovery;
- realized fee / collection;
- partner cost where applicable.

Commercial hypothesis:

this lane may create the strongest service value because the State self-service route is harder to execute, but it can also become the most expensive lane.

Important monetization boundary:

do not model nonlawyer platform revenue as a percentage of lawyer legal fees without specialized legal review. The platform may test owner-paid location-service economics or non-contingent B2B/software/service pricing separately.

### Lane assignment principle

Lane assignment is not a value prediction.

Never assert:

`F3 = HIGH VALUE`

or:

`F0 = LOW VALUE`.

Allowed interpretation:

`F3 = HIGHER OBSERVED PROCESS FRICTION`

and:

`F0 = LOWER OBSERVED PROCESS FRICTION`.

Any later value-based prioritization requires evidence-backed value or a separately validated lawful proxy.

## Economic Case Ledger — mandatory unit-economics evidence record

Every future real candidate experiment must produce one `Economic Case Ledger` keyed by non-PII `case_id`.

The ledger is the canonical economic evidence record for the case.

It must not become a parallel owner-PII database.

### Identity / provenance fields

Record at minimum:

- `case_id`;
- source ID;
- source snapshot / acquisition evidence ref;
- deterministic selection-rule version;
- physical source record ordinal or other approved non-owner provenance pointer;
- initial lane `F0/F1/F2/F3`;
- lane-change events with reason/evidence;
- timestamps for every economic stage transition.

### Cost ledger

Record actual measured amounts, never invented defaults:

- automated compute/tool cost;
- external API/data cost;
- human review seconds/minutes;
- manual research seconds/minutes;
- contact-channel cost;
- document/notary cost;
- professional/legal/external cost where applicable;
- fee-collection cost;
- other explicitly evidenced direct case cost.

Human labor cost may be computed only when a documented labor-rate evidence ref exists.

### Funnel-event ledger

Record:

- candidate selected;
- identity work started;
- identity sufficiently established: yes/no;
- contactability established: yes/no;
- contact attempts count;
- contact success: yes/no;
- agreement offered: yes/no;
- agreement signed: yes/no;
- realized fee rate, only with evidence;
- value-known state;
- value evidence ref;
- claim/recovery started: yes/no;
- recovery success: yes/no;
- recovered amount, only with evidence;
- fee billed;
- fee collected;
- collection timestamp;
- stop/pause reason.

### Time ledger

Record timestamps sufficient to derive:

- time from selection to identifiable;
- time from selection to contactable;
- time to contact;
- time to agreement;
- time to value known;
- time to recovery;
- time to fee collection.

Primary metric:

`DAYS_TO_CASH = fee_collected_at - candidate_selected_at`

when fee is actually collected.

### Derived economic metrics

The system should derive, not manually guess:

- `COST_PER_SCREENED_CANDIDATE`;
- `COST_PER_IDENTIFIABLE_CANDIDATE`;
- `COST_PER_CONTACTABLE_CANDIDATE`;
- `COST_PER_VALUE_KNOWN_CANDIDATE`;
- `COST_PER_SUCCESSFUL_RECOVERY`;
- identifiable rate;
- contactable rate;
- contact success rate;
- agreement-signing rate;
- value-known rate;
- successful-recovery rate;
- realized fee rate;
- fee-collection rate;
- failed-case fully loaded cost;
- successful-case fully loaded cost;
- gross fee per successful case;
- contribution before overhead per case.

No project-level ROI/CAC/LTV forecast is authoritative until these metrics exist on real cases.

## PRE_VALUE_DISCOVERY_COST — primary MVP economic metric

Definition:

`PRE_VALUE_DISCOVERY_COST` is the fully evidenced cost accumulated before the platform knows enough about the case value to make a rational continue/stop decision.

It includes only costs incurred before the value-decision point, including where applicable:

`automation/compute`
`+ data/API`
`+ human research`
`+ identity/contactability work`
`+ contact cost`
`+ preliminary document/notary cost`
`+ preliminary external/professional cost`

It excludes costs that occur only after the case has already crossed the value/economic decision gate.

Required states:

- `NOT_STARTED`;
- `MEASURING`;
- `VALUE_KNOWN`;
- `VALUE_STILL_UNKNOWN_STOPPED`;
- `VALUE_REQUIRES_UNAUTHORIZED_SCOPE`.

Required output:

- accumulated pre-value cost;
- evidence refs for each component;
- elapsed time;
- exact stage at which value became known, if it did;
- stop reason if it did not;
- privacy/legal scope required to move further.

### Why this metric controls scale

The source exposes candidate supply but not value.

Therefore the business cannot safely optimize only:

`COST_PER_CANDIDATE`.

It must optimize:

`COST_TO_LEARN_IF_THE_CANDIDATE_IS WORTH FURTHER SPEND`.

If `PRE_VALUE_DISCOVERY_COST` becomes too high before useful value evidence appears, the direct-to-owner model can become irrational even when successful cases occasionally have high values.

## Economic Discovery Ladder — spend incrementally to buy information

Every real case must progress through bounded stages.

Each stage requires:

1. an information objective;
2. an incremental budget;
3. the expected decision unlocked by that information;
4. a fail-closed stop condition;
5. explicit approval before privacy/legal scope expansion.

### Ladder L0 — Source-only qualification

Inputs:

non-PII / already-authorized source classification data.

Objective:

determine whether the record qualifies for the one-candidate experiment and assign an initial friction lane without using unsupported value guesses.

Spend posture:

`NEAR_ZERO_INCREMENTAL_COST`.

Stop if:

candidate fails deterministic eligibility.

### Ladder L1 — Transient one-candidate materialization

Objective:

materialize exactly one approved candidate transiently under the approved proposal and confirm minimum case structure.

Measure:

machine cost, operator time, transient-processing duration.

No address persistence, outreach, identity resolution or value research.

Stop if:

privacy scope is insufficient or candidate fails materialization rules.

### Ladder L2 — Minimal identity / contactability discovery

Requires separate legal/privacy authorization before real execution.

Objective:

answer only:

`CAN THIS OWNER / AUTHORIZED REPRESENTATIVE BE IDENTIFIED AND CONTACTED AT ACCEPTABLE COST?`

Measure all incremental data/API/human cost.

Do not perform broad genealogy or expensive manual research without a bounded incremental budget.

Stop if:

incremental cost exceeds the Product Owner-approved discovery budget without materially improving case information.

### Ladder L3 — Minimal contact / service-fit discovery

Requires separate outreach authorization.

Objective:

measure actual contactability, response, willingness to engage, agreement conversion and any lawful path toward value evidence.

Measure:

contact attempts, channel cost, human time, agreement status.

Stop if:

free OSC alternative eliminates willingness to pay or acquisition cost becomes economically disproportionate.

### Ladder L4 — Value-evidence discovery

Objective:

obtain evidence-backed recoverable value when lawfully possible, or establish why it remains unknown.

Output must be one of:

- `VALUE_EVIDENCE_OBTAINED`;
- `UNKNOWN_PRE_CLAIM_REVIEW`;
- `STOP_PRIVACY_SCOPE_INSUFFICIENT`;
- `STOP_REQUIRES_CLAIM_IDENTITY_OR_LEGAL_ACTION`;
- `STOP_PRE_VALUE_DISCOVERY_COST_TOO_HIGH`.

No value may be invented.

### Ladder L5 — Explicit case economics

Only after evidence exists.

Compute:

`GROSS_FEE = RECOVERED_VALUE x REALIZED_FEE_RATE`

and:

`CONTRIBUTION_BEFORE_OVERHEAD = GROSS_FEE - FULLY_LOADED_CASE_COST`

with provenance for value, fee and cost.

Human Product Owner decides:

`GO / REVISE / STOP`.

The software must not silently convert arithmetic into an automatic commercial decision.

## Stop-loss / budget discipline

No fixed dollar stop-loss threshold is currently evidence-backed.

Therefore the first real cases must not hard-code arbitrary profitability thresholds.

Instead each ladder stage must receive an explicit bounded incremental budget from the Product Owner.

The first experiments are designed to **measure** where rational thresholds should be set.

After evidence exists, candidate-stage stop rules can be based on measured expected contribution.

Illustrative economics logic only:

`EXPECTED_GROSS_FEE = P(success) x EXPECTED_RECOVERY x REALIZED_FEE_RATE`

`EXPECTED_CONTRIBUTION = EXPECTED_GROSS_FEE - EXPECTED_FULLY_LOADED_COST`

Do not operationalize those formulas with invented probabilities or recovery values.

## Pilot sequence for economic learning

These are management gates, not statistically validated sample-size claims.

### Pilot P1 — one real case

Purpose:

prove the economic-discovery process end to end and identify the exact point where value, privacy and cost become binding.

Success is not necessarily a recovery.

A valid result can be:

`STOP — PRE_VALUE_DISCOVERY_COST OR REQUIRED_SCOPE MAKES CASE IRRATIONAL`.

### Pilot P2 — approximately five bounded cases

Only after P1 review.

Purpose:

identify repeated failure modes and lane differences.

Questions:

- where does cost accumulate?
- which lane is most expensive?
- which steps repeat?
- what can be automated safely?
- does the value-known point occur consistently?

Five is a management-learning batch, not a statistical guarantee.

### Pilot P3 — approximately 20–30 bounded cases

Only if P2 evidence supports continuation.

Purpose:

obtain an initial empirical distribution for conversion/cost/time/value-known outcomes sufficient for a Product Owner scale/pivot decision.

Do not treat this as statistically representative without formal analysis.

## Pivot framework — what to do if PRE_VALUE_DISCOVERY_COST is excessive

The project must not keep adding automation merely to defend the original direct-to-owner thesis.

### Scenario A — Low discovery cost + positive real contribution

Signal:

- identity/contactability inexpensive;
- value can be reached before excessive spend;
- agreement/recovery/collection path works;
- contribution before overhead is positive.

Action:

`CONTINUE_DIRECT_OWNER_LOCATION_SERVICE`

Invest selectively in the bottleneck demonstrated by real cases.

### Scenario B — Moderate/high discovery cost, but professional operators value the tooling

Signal:

- per-case direct-to-owner economics are weak or volatile;
- the platform still materially reduces research time for attorneys, investigators, location-service providers or estate professionals;
- customer discovery shows willingness to pay for workflow/software/research tooling independent of legal-fee sharing.

Action:

`PIVOT_OR_ADD_B2B_SOFTWARE_SERVICE_MODEL`

Potential monetization to validate:

- subscription;
- seat-based pricing;
- case-processing fee;
- fixed research/service fee;
- enterprise workflow licensing.

Do not build B2B features before willingness-to-pay evidence exists.

### Scenario C — Complex F3 cases carry value but professional/legal cost dominates

Signal:

- high-friction cases appear economically attractive before external cost;
- lawyer/estate/notary expense absorbs most expected contribution;
- monetization would depend on sharing legal fees or referral economics that are legally uncertain.

Action:

`RESTRUCTURE_PARTNERSHIP_AND_PRICING_BEFORE_SCALE`

Possible directions for legal review:

- owner-paid location-service fee separate from legal engagement;
- non-contingent platform/software/service fee;
- professional-user subscription.

Do not assume a share of lawyer legal fees.

### Scenario D — Discovery cost high + value arrives too late + no B2B willingness to pay

Signal:

- `PRE_VALUE_DISCOVERY_COST` repeatedly high;
- many cases stop before value known;
- free State alternative suppresses conversion;
- successful-case contribution does not cover failed-case burn;
- no professional customer demonstrates willingness to pay for the tooling/data workflow.

Action:

`FREEZE_OR_STOP_NY_DIRECT_MODEL`

Do not respond by building more architecture.

Preserve reusable source/economics/privacy assets and evaluate another source, jurisdiction or business model only through a new Product Owner decision.

## Governance-to-economics rule

Further governance is justified only when it is:

- necessary to lawfully run the next economic experiment;
- necessary to protect PII/security;
- necessary to preserve reproducibility/provenance;
- directly required by a demonstrated economic bottleneck.

Freeze by default:

- generic new agent frameworks;
- broad A01–A23 implementation;
- graph infrastructure;
- multi-state expansion;
- generalized genealogy platform;
- mass outreach automation;
- large durable PII architecture;
- non-critical UI polish;
- parser diagnostics without a real blocker.

Preferred allocation during economic-validation mode:

approximately `70–80%` of effort toward experiments/instrumentation that generate economic evidence and approximately `20%` toward the minimum privacy/legal/governance required to run them safely.

This ratio is a Product Owner planning heuristic, not an externally validated economic constant.

## Mandatory next-stage acceptance criteria

The existing next implementation action remains:

`IMPLEMENT_AND_REVIEW_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION`

but it must now be reviewed also for economic instrumentation readiness.

Before any real-case authorization, the synthetic implementation/review must demonstrate that a future real case can produce, without storing owner PII in the economic ledger:

- lane assignment and lane-change provenance;
- stage timestamps;
- component cost evidence;
- human-time evidence;
- `PRE_VALUE_DISCOVERY_COST` state;
- economic-discovery-ladder stage;
- stop reason;
- value-evidence state;
- hooks into existing follow-up-cost and case-economics components.

Do not implement identity resolution, outreach, claim logic or broad durable PII merely to satisfy instrumentation.

## SINGLE NEXT ACTION

Economic-feasibility direction is accepted as the governing development frame for the next MVP-1 work.

Execute only:

`IMPLEMENT_AND_REVIEW_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION`

against the already approved proposal, with the additional mandatory economic-instrumentation acceptance criteria defined above.

The synthetic package must prepare the interfaces/contracts needed for:

- `Economic Case Ledger`;
- friction lane `F0/F1/F2/F3`;
- `PRE_VALUE_DISCOVERY_COST`;
- economic discovery ladder stage/state;
- bounded stop reason;
- existing follow-up-cost/value-evidence/economics integration.

It must remain synthetic-only.

It must not authorize or perform:

- source access;
- remote preflight;
- download;
- owner PII processing;
- real candidate materialization;
- identity resolution;
- beneficiary matching;
- address enrichment;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

After synthetic review PASS, the next human decision is whether the expected information gain from one real candidate justifies the exact minimum legal/privacy scope required for Pilot P1.

## Git health

Canonical integration branch:

`main`

Current canonical main checkpoint before economic-audit merge:

`9873005e61a088f718aeb3093fdb57ac6827ab44`

One-candidate offline proposal:

`PR #32 — MERGED INTO main`

Economic-feasibility audit branch:

`audit-economic-feasibility-2026-09-23`

Economic-feasibility audit PR:

`#33 — OPEN / NOT MERGED`

Current audit branch includes:

- whole-project economic feasibility audit;
- updated PROJECT_STATE / ROADMAP;
- this economic-financial HANDOVER;
- no runtime/source/PII behavior changes.

Do not merge PR #33 unless the Product Owner explicitly authorizes the audit/state integration.

## Context continuity rule

The conversation has completed multiple high-complexity milestones.

Before code or decision quality degrades, create a fresh handover and move to a new chat when:

- multiple new real-data gates accumulate;
- more than one new branch/milestone becomes active;
- the next implementation introduces several coupled contracts/modules;
- earlier facts require repeated re-verification because context is becoming hard to maintain.

The assistant must warn the Product Owner **before** visible context degradation, code inconsistency or authorization mistakes appear.
