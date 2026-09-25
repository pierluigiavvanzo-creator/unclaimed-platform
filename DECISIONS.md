# DECISIONS.md

## D-001 — PowerShell Windows orchestration

Date: 2026-09-13

Status: Accepted

Decision:
Use PowerShell as the Windows bootstrap/orchestration layer.

Reason:
The initial development and testing environment is Windows-based.

Alternatives considered:
- Python
- Bash
- Make

Consequences:
PowerShell scripts must remain idempotent, explicit on failure and free of secrets.

---

## D-002 — Deterministic governance core

Date: 2026-09-13

Status: Accepted

Context:
State transitions, policy gates, budgets and audit must be reproducible and must not depend on probabilistic model behavior.

Decision:
Keep state machine, policy gates, budget controls and audit in deterministic core modules. Domain agents can propose actions but cannot bypass core gates.

Reason:
This preserves fail-closed behavior, auditability and testability.

Alternatives considered:
- Agent-owned workflow transitions
- LLM-directed orchestration

Consequences:
A00 coordinates agents but governance authority remains in deterministic code.

---

## D-003 — Versioned JSON Schema contracts

Date: 2026-09-13

Status: Accepted

Context:
Independent agents and adapters require stable boundaries.

Decision:
Use JSON Schema draft 2020-12 as the canonical machine interchange contract with explicit versions and contract tests.

Reason:
Prevents silent schema drift and supports independent module development.

Alternatives considered:
- Pydantic-only runtime contracts
- Unversioned Python dictionaries

Consequences:
Breaking changes require explicit schema versioning and migration/adapter work.

---

## D-004 — Explicit M2 workflow whitelist

Date: 2026-09-13

Status: Accepted

Context:
M2 requires a deterministic lifecycle state machine. Mature FSM libraries exist, but the initial need is a small versioned whitelist with fail-closed semantics.

Decision:
Implement the M2 workflow whitelist using standard-library code and versioned JSON configuration. Missing policy routes to HUMAN_REVIEW, budget exhaustion stops progression, and terminal states cannot transition outward.

Reason:
The critical behavior remains directly auditable and testable without introducing a broader state-machine dependency. Reuse must be reconsidered if hierarchical or concurrent state complexity appears.

Alternatives considered:
- python-statemachine
- transitions

Consequences:
M2 has a small custom state core; future expansion requires an explicit superseding decision rather than silent framework growth.

---

## D-005 — Canonical development branch and main integration policy

Date: 2026-09-13

Status: Accepted

Context:
`main` diverged from the verified development history after two direct commits created and then expanded a file named `root` whose contents were intended to act as `AGENTS.md`. Meanwhile the verified development branch contains the actual `AGENTS.md` plus the M0-M3 implementation and governance history.

Decision:
- Treat `m2-state-governance-core` as the current canonical development/integration branch until it is explicitly renamed or superseded.
- Treat `main` as the stable milestone/release branch, not as the day-to-day development branch.
- Promote feature/candidate branches into the canonical development branch only after the relevant tests and gates pass.
- Update `main` only at meaningful verified milestone or gate boundaries.
- Reconcile the existing divergence with a history-preserving merge commit that has both histories as parents.
- Keep the actual canonical `AGENTS.md` unchanged as the governing development contract; do not carry the misnamed `root` file into the reconciled tree.
- Avoid direct commits to `main` except deliberate owner-approved integration or emergency/hotfix work.

Reason:
This preserves all Git history without replacing the more specific verified governance contract or allowing `main` and the active development history to drift independently.

Alternatives considered:
- Force-reset `main` to the development branch
- Replace canonical `AGENTS.md` with the generic `root` content
- Keep the branches permanently divergent

Consequences:
The first reconciliation into `main` is a non-fast-forward merge by design. After reconciliation, milestone merges should remain simple provided direct development on `main` is avoided. The misnamed `root` file remains recoverable from Git history but is intentionally absent from the reconciled working tree.

---

## D-006 — Streamlit replaces Vercel on the M3 reviewer critical path

Date: 2026-09-14

Status: Accepted

Context:
The owner explicitly directed the project to abandon Vercel after repeated project/deployment visibility inconsistencies and move the reviewer surface to Streamlit.

Decision:
Use Streamlit Community Cloud as the active M3 reviewer deployment target. Preserve deterministic governance and the existing versioned/typed read model as authority. Keep the existing Next.js/Vercel implementation only as rollback/history until Streamlit is remotely verified.

Reason:
This materially reduces deployment complexity and removes the need for a separate preview backend plus `REVIEWER_API_BASE_URL` wiring while preserving the current synthetic/read-only scope.

Alternatives considered:
- Continue Vercel diagnostics
- FastAPI templates
- Gradio

Consequences:
ADR-0005 supersedes the Vercel deployment-target portion of ADR-0004. No real acquisition, beneficiary matching, source approval, real PII or Supabase integration is enabled by this decision.

---

## D-007 — Decommission repository-side Vercel runtime integration

Date: 2026-09-14

Status: Accepted

Context:
Streamlit is the verified reviewer deployment target, while the owner continues to receive failed-deployment notifications from the historical Vercel path. Repository-side provider configuration is no longer required and creates avoidable ambiguity.

Decision:
- Remove all active Vercel deployment configuration from the canonical repository tree.
- Remove provider-specific deployment instructions from active application documentation.
- Keep the legacy Next.js reviewer only as a provider-neutral local/regression artifact.
- Add a contract test that rejects reintroduction of Vercel-named files or textual Vercel references in active runtime surfaces (`.github`, `apps`, `scripts`, `src`, and root runtime configuration files).
- Preserve historical ADRs/audits as inert records; history is not executable configuration.
- Treat any external Vercel Git/project connection as a provider-side integration that must be disconnected separately from the repository contents.

Reason:
This prevents repository changes from intentionally invoking or configuring Vercel and makes Streamlit the only active reviewer deployment path represented by runtime configuration.

Alternatives considered:
- Keep `vercel.json` as dormant rollback configuration.
- Delete the entire legacy Next.js reviewer.
- Leave the repository unchanged and rely only on provider-side settings.

Consequences:
Vercel deployment is unsupported from the active repository tree. Reintroducing a Vercel runtime integration requires a new explicit owner decision and corresponding test/governance update. An already-installed external Git integration may still receive repository events until it is disconnected at the provider/GitHub integration layer.

---

## D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE

Date: 2026-09-16

Status: Superseded for the California SCO MVP-1 classification path by D-010; retained as historical fail-closed baseline

Context:
The bounded California SCO diagnostics established, for one examined row, that strict UTF-8 decoding and strict stdlib CSV parsing succeeded, the canonical 25-column shape was produced, stdlib field index `1` agreed with the custom projector's `PROPERTY_TYPE` field, and the shared field still failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`. The exact value, frequency, cause and source intent remain unknown. A reviewed handling proposal required disposition, continuation and privacy boundaries to remain separate.

Decision:
Accept `WHOLE_SOURCE_STOP` as the deterministic handling **design decision** for a canonical `PROPERTY_TYPE` that fails the unchanged validation boundary. The design emits only non-value-bearing control status/reason metadata and does not continue to later rows after the triggering condition.

This decision does not itself authorize or perform runtime implementation, another real-source execution, source activation, registry activation, privacy expansion, real-row quarantine, row-specific human inspection, parser/projector changes, regex changes, trimming/casing/normalization or semantic acceptance of the source value.

Reason:
This preserves the current fail-closed behavior without silently omitting rows, inventing source semantics, enabling continuation or introducing a new privacy/persistence boundary while semantic compatibility remains unresolved.

Alternatives considered:
- Row-level metadata defer with separately governed later continuation
- Real-row quarantine
- Metadata-only human-review route

Consequences:
- Runtime behavior remains unchanged until a separate implementation gate is reviewed and authorized.
- Source continuation after the nonconforming condition remains unauthorized under D-008 itself.
- The accepted historical control vocabulary is `PROPERTY_TYPE_NONCONFORMING_STOPPED` with reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.
- Exact/derived `PROPERTY_TYPE`, real row/field content, hashes, exact lengths, `PROPERTY_ID`, owner/holder values and source-derived free text remain outside the persistence boundary.
- D-010 changes only the source-specific MVP-1 continuation policy while preserving the no-normalization/no-value-persistence boundary.

---

## D-009 — MVP-1 commercial validation becomes the product-priority objective

Date: 2026-09-17

Status: Accepted

Context:
The project has a strong deterministic, contractual and fail-closed engineering foundation, but commercial/product validation remains materially behind the governance layer. At the time of this decision, approved real sources remain `0`, semantic compatibility is unresolved, production classification is inactive, and no real candidate has traversed the full product path into a commercially reviewable case.

Decision:
Adopt `MVP-1 — First Economically Actionable Case` as the priority product objective. `PRODUCT_STRATEGY_MVP1.md` becomes a priority project source and must be read immediately after `AGENTS.md`.

M3 California source work remains active only as the minimum critical-path enabler required to reach one lawful approved real source. Once a real source is approved, priority must shift immediately to the vertical slice:

`APPROVED REAL SOURCE -> bounded acquisition -> normalization -> insurance classification -> candidate case -> provenance/evidence -> case economics -> reviewer console -> human continue/stop decision`.

No commercial threshold is invented in advance; real execution must establish the baseline.

Reason:
The project should optimize `ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`, not code volume, test count, diagnostic depth or governance completeness as ends in themselves.

Consequences:
- substantial work must be classified `A/B/C/D` and tied to a specific MVP-1 blocker or exit criterion;
- diagnostic/infrastructure work that does not materially shorten the path to MVP-1 is deprioritized;
- Product Owner technical/manual involvement must be minimized except at material product, commercial, legal/privacy, security or irreversible architecture gates;
- repository-first/reuse-first is mandatory before substantial custom downstream capability;
- the canonical read order is `AGENTS.md`, `PRODUCT_STRATEGY_MVP1.md`, `PROJECT_STATE.md`, `ROADMAP.md`, `DECISIONS.md`, `docs/handovers/HANDOVER_CURRENT.md`;
- all existing legal, privacy, security, source-authorization, deterministic and fail-closed controls remain binding and take precedence over product acceleration.

---

## D-010 — Authority-backed row defer for California SCO MVP-1 PROPERTY_TYPE classification

Date: 2026-09-17

Status: Accepted; real-source validation still requires fresh single-use authorization

Context:
The adopted transport baseline was confirmed live. A one-shot real-source execution then reached a canonical `PROPERTY_TYPE` field that failed the unchanged structural boundary and correctly stopped under D-008. Earlier source-format diagnostics already established that strict UTF-8 and strict stdlib CSV parsing succeed, the row has the canonical 25-column shape, and stdlib field index `1` agrees with the custom projector. California SCO authority provenance is now resolved: the archived/current California NAUPA material enumerates insurance codes `IN01` through `IN08` plus `IN99`, and the current California Holder Handbook identifies `IN03` as `Proceeds Due Beneficiaries`.

Decision:
For the California SCO MVP-1 insurance-classification path, supersede D-008's whole-source continuation behavior with `ROW_DEFER_CONTINUE_METADATA_ONLY` while preserving its semantic and privacy safeguards.

A nonconforming `PROPERTY_TYPE`:
- is not normalized, trimmed, uppercased, repaired, regex-relaxed, inferred, or accepted;
- is not classified as non-insurance;
- is classified only as `DEFER_UNCLASSIFIABLE`;
- contributes only to a non-value-bearing aggregate deferred-row count;
- does not persist the source value, derivative, row content, `PROPERTY_ID`, owner/holder fields, hash, exact length, or source-derived free text;
- does not trigger row-specific human inspection;
- does not silently disappear: the defer count is part of completeness evidence;
- permits processing of later rows so exact authority-backed insurance codes can be found.

Exact California insurance codes `IN01`-`IN08` and `IN99` are recognized as insurance. For the first high-precision MVP-1 vertical slice, `IN03` is the primary target because the California authority description is `Proceeds Due Beneficiaries`. This is a product targeting rule, not an alteration of California semantics and not a claim that other insurance codes lack commercial value.

Reason:
A malformed/unclassified row does not justify inventing semantics, but stopping the entire public source prevents reaching later rows that may contain exact authority-backed insurance codes. Metadata-only row defer preserves uncertainty and privacy while removing a disproportionate blocker to the first economically actionable case.

Alternatives considered:
- Keep D-008 whole-source stop indefinitely
- Normalize or relax the malformed value
- Persist/quarantine the row for inspection
- Treat malformed values as non-insurance
- Abandon California SCO immediately

Consequences:
- the existing diagnostic runner remains historical evidence and need not be rewritten;
- the new source-specific classifier is the MVP-1 product classification boundary;
- exact authority-backed insurance codes can flow forward, with `IN03` as the first narrow target;
- nonconforming rows remain unresolved and auditable via aggregate count rather than silent omission;
- no privacy expansion or real-row persistence is introduced;
- source approval is not granted by this decision;
- a fresh bounded real-source execution must validate row-defer continuation and insurance discovery before source activation;
- after source approval, priority moves immediately to candidate generation, case economics and reviewer decision rather than further PROPERTY_TYPE diagnostics.


---

## D-011 — NY OSC quote interpretation statistical fallback policy

Date: 2026-09-21

Status: Accepted as Product Owner policy for the offline parser proposal; runtime implementation and source execution remain separately gated

Context:
NY OSC Owner Name File attempts 5 and 6 produced non-PII structural evidence showing that unrestricted multiline quote carry is unsafe and that raw-pipe and same-line quote-aware interpretations can diverge. The repository does not contain authoritative OSC documentation defining double-quote escaping or multiline record semantics. The reviewed documented-width proposal was therefore found to overstate schema conformity as dialect proof.

Decision:
Keep LF/CRLF as a hard physical-record boundary and separate structural classification from interpretation selection.

When authoritative OSC quote semantics remain unavailable:
- compare RAW pipe and the explicitly non-authoritative candidate same-line quote interpretation;
- treat only records where exactly one candidate has the documented 14-field width as dialect-discriminating evidence;
- use a Product Owner decision threshold of `0.66`;
- do not call a sample-derived frequency a source-dialect probability without adequate statistical support;
- use the Wilson two-sided 95% lower confidence bound as the conservative support check for the proposal;
- if one candidate's robust support exceeds `0.66`, that candidate may be proposed for a separate future implementation review;
- if the threshold is not robustly met, the Product Owner fallback is `RAW_PIPE_WITH_DOUBLE_QUOTE_LITERAL`.

Current retained discriminating evidence is one sixth-attempt record: RAW has 14 fields and the candidate quote-aware interpretation has 6. The point estimate is 1/1 RAW support, but the Wilson 95% lower bound is approximately `0.2065432915`, below the 0.66 threshold. Therefore the current proposal uses the Product Owner RAW-literal fallback while explicitly recording that this is not OSC source truth.

Reason:
This avoids silently using documented width as proof of quote semantics, preserves deterministic progress, and makes the unresolved source-authority gap explicit. The fallback favors a simple literal-character interpretation while still blocking rows whose RAW width does not match the documented 14-field layout.

Alternatives considered:
- Continue fail-closed on every raw/quote-aware divergence indefinitely.
- Automatically select whichever interpretation alone produces 14 fields.
- Treat same-line quote-aware parsing as authoritative without OSC documentation.
- Carry quote state across physical lines.
- Require a seventh real download before any further offline design.

Consequences:
- `"` literal / RAW is the current Product Owner fallback, not an OSC-documented fact.
- A RAW 14 / candidate quote-aware !=14 record may be proposed for acceptance under the owner fallback in a future separately reviewed implementation.
- A RAW !=14 / candidate quote-aware 14 record remains blocked under the current fallback unless later authoritative or statistically robust evidence changes the policy.
- A future non-PII full-file structural scan may be proposed to enlarge the discriminating sample, but no such scan is authorized by D-011.
- No parser/runtime/runner change, source access, retry, approval creation, seventh attempt, source activation, matching or outreach is authorized by this decision.


---

## D-012 — Targetable opportunity replaces first-source-order economic selection for Pilot P1

Date: 2026-09-24

Status: Accepted as Product Owner product-validation policy; real P1 execution remains separately gated

Context:
Attempt 11 proved substantial aggregate IN03 candidate supply, while the NY OSC Owner Name File does not disclose recoverable value. Stage A then proved synthetic one-candidate transient materialization using the first eligible source-order record. That Stage A rule was useful for deterministic technical validation but does not distinguish cases where a paid service creates material value from cases a person can likely resolve directly through the free OSC path.

Official NY OSC materials also establish that direct claims are free, Location Service Providers are recognized, the applicable provider fee is capped at 15 percent, qualifying simple payments may be expedited by OSC, and estate claims can require additional entitlement/court documentation.

Decision:
For future Pilot P1 economic discovery:

1. retain Stage A FIRST_ELIGIBLE_RECORD_IN_SOURCE_ORDER only as historical synthetic technical evidence;
2. use PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER as the proposed future P1 source-selection rule;
3. interpret Holder Report Year only as a persistence signal, never as evidence of value, awareness, death, contactability or willingness to pay;
4. introduce targetability as a separate product axis based on SERVICE NEED x RESOLVABILITY;
5. use evidence classes T0-T4 rather than a numeric score:
   - T0_SELF_SERVICE_LIKELY;
   - T1_UNRESOLVED_BUT_LOCATABLE;
   - T2_ESTATE_OR_REPRESENTATIVE_PATH;
   - T3_HARD_BUT_BOUNDED;
   - T4_UNBOUNDED_OR_UNRESOLVED_STOP;
6. preserve F0-F3 strictly as observed process-friction lanes and do not use them as targetability/value scores;
7. keep awareness UNKNOWN_UNTIL_OUTREACH until separately authorized contact produces evidence;
8. retain PRE_VALUE_DISCOVERY_COST as the umbrella metric and add TARGETABILITY_DECISION_COST as the primary P1 sub-metric;
9. set L1 maximum new external cash spend to USD 0.00; paid API/data use is excluded from L1;
10. leave L2 incremental budget UNSET_REQUIRES_PRODUCT_OWNER;
11. keep outreach, value research, fee agreement, representation and claim activity as separate human gates.

Reason:
The economically useful subset is not the highest theoretical value and not the highest difficulty. It is the subset with material service need, bounded resolvability and controlled pre-value cost. This directly tests whether the platform can create paid service value despite the free State claim path without inventing recoverable values or profitability.

Alternatives considered:
- keep selecting the first eligible IN03 record;
- rank candidates by guessed property value;
- equate F2/F3 friction with commercial attractiveness;
- introduce a weighted targetability score before real evidence exists;
- begin paid identity/data enrichment before proving targetability economics.

Consequences:
- PRODUCT_STRATEGY_MVP1 v3 governs prioritization;
- Stage A implementation remains preserved and backward-compatible;
- future real P1 must not use first-source-order selection as its economic targeting policy;
- no T class may be assigned when evidence is insufficient;
- no numeric targetability score is permitted in v1;
- P1 asks whether service need and bounded resolvability can be established at acceptable evidenced cost before value is known;
- this decision authorizes only offline/synthetic design and implementation, not source access or PII processing.


---

## D-013 — Real P1 uses two-pass local selection/materialization with pre-bound single-use gates

Date: 2026-09-24

Status: Accepted as Product Owner scope direction; runtime implementation verified offline; real execution remains separately gated

Context:
The Product Owner approved the fresh real P1 targetability execution scope after D-012 established targetability as MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE. The first real P1 must minimize owner-PII exposure while preserving persistence-first selection and bounded economics. A one-pass design that buffers owner data across many eligible rows would unnecessarily widen privacy exposure, while a post-L1 request for permission to continue would incentivize retaining the downloaded owner file while waiting for a new authorization.

Decision:
For the first real NY OSC P1:

1. selection and candidate materialization are two separate passes over the same already-authorized local archive;
2. L0 selection may derive only structural shape, exact IN03, owner-count=1, Property ID presence boolean, Holder Report Year and source ordinal;
3. Owner Name/address must not be decoded or buffered for L0 ranking;
4. selection is PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER, with no fixed age threshold and no value inference;
5. L1 second pass may transiently materialize only Property ID, Property Type Code, Property Owner Count, Owner Name, Holder Name and Holder Report Year for the selected ordinal;
6. no owner PII, Holder Name, raw row or address is durable at L1;
7. L1 new external cash spend remains USD 0.00;
8. L2-A is a separate optional extension and may share the same download only when every L2-A privacy/provider/budget/execution grant already exists before the download;
9. mid-session waiting for a new authorization while retaining the local owner file is prohibited;
10. proposed L2-A experiment bounds are USD 0.00 external paid spend and 900 seconds manual research, explicitly as a management experiment cap rather than a profitability threshold;
11. no L2-A provider is approved by default; the provider must be specifically bound to an approved provider/terms review;
12. the production CLI remains L1-only until a provider-specific review authorizes an L2-A adapter;
13. all seven P1 gates are fresh, single-use, non-reusable and zero-retry;
14. the local archive must be logically deleted after execution; physical secure erasure must not be claimed;
15. deletion failure is a fail-closed BLOCKED outcome.

Reason:
This architecture minimizes PII exposure, avoids redundant downloads when the entire L1/L2-A scope is already approved, prevents opportunistic retention while waiting for wider scope, and forces the first real pilot to measure targetability economics before value research or scale.

Alternatives considered:
- buffer owner PII for every eligible IN03 during the selection scan;
- select by Owner Name/address or other PII-based ranking;
- perform L1, retain the file, then request L2-A approval;
- add a generic people-search/data-broker integration immediately;
- allow paid API/data use in P1;
- use a one-pass raw-row materialization design;
- automatically retry after a blocked run.

Consequences:
- L0 and L1 can be tested independently and audited;
- a single authorized archive can support both passes without a second download;
- if L2-A is not pre-approved, P1 stops after L1 disposal;
- real L2-A requires a future provider-specific legal/privacy/terms review;
- no current repository artifact grants real execution;
- approval templates remain NOT_GRANTED until separately and explicitly granted by the Product Owner.


---

## D-014 — Product target expands to North America multi-registry operating platform

Date: 2026-09-24

Status: Accepted by Product Owner as product direction; implementation remains milestone-gated

Context:
The project began product validation on NY OSC because it provided a concrete, lawful source and a tractable path to test targetability economics. Competitive review established that unclaimed-property search, AI-assisted owner location, lead prioritization and recovery workflow products already exist. The Product Owner clarified that the intended product must not be limited to NY OSC or even one US state. The target market is the United States and Canada, and the product must ultimately operate as a multi-registry research, prioritization and recovery platform.

Decision:
1. define the long-term product geography as UNITED STATES + CANADA;
2. treat NY OSC as the first validated source adapter / Stage B pilot anchor, not as the permanent product boundary;
3. require a versioned multi-registry source-adapter architecture so additional US and Canadian registries can be added without rewriting generic downstream modules;
4. make the target product capabilities:
   - multi-registry acquisition/normalization;
   - cross-registry deduplication/linking;
   - evidence-aware AI confidence scoring;
   - lead prioritization;
   - people/owner/heir/representative finding;
   - case economics;
   - jurisdiction-specific compliance;
   - contract builder;
   - fee calculator;
   - CRM/case management;
   - outreach/claim workflow when separately authorized;
   - outcome learning/calibration;
5. keep automation evidence-based:
   - automate repetitive, high-confidence, reversible work;
   - semi-automate ambiguous/material decisions;
   - human-gate legal/privacy/identity-conflict/irreversible actions;
6. remove patentability/feature novelty as a primary strategic objective;
7. optimize instead for measured performance, reliability and efficiency:
   - useful-lead precision;
   - false-positive rate;
   - confidence calibration;
   - time to targetability;
   - targetability decision cost;
   - cost per targetable lead;
   - human minutes per case;
   - automation rate by stage;
   - human override rate;
   - identity-resolution success;
   - conversion across stages;
   - claim/recovery economics where later authorized;
8. do not invent numeric KPI thresholds until real P1/P2/P3 evidence exists;
9. preserve Stage B as a deliberately narrow experiment on the already-developed NY adapter;
10. after Stage B/P1/P2 support continuation, generalize the Source Adapter Contract and expand registries in evidence-backed priority order across USA and Canada;
11. do not hard-code NY-specific semantics into generic targetability, confidence, people-finder, economics, CRM, contract or fee modules.

Reason:
The product advantage should come from better operating performance, lower research/decision cost, higher useful-lead precision, broader verified registry coverage, stronger evidence/provenance and better workflow conversion — not from claiming category novelty or patentability. A narrow Stage B remains economically rational because it validates the engine before paying the integration cost of continent-wide registry coverage.

Alternatives considered:
- keep the product NY-only;
- expand immediately to many registries before P1;
- optimize for patents/novel features;
- build a broad generic CRM before validating targetability;
- hard-code each state/province as a separate end-to-end workflow.

Consequences:
- PRODUCT_STRATEGY_MVP1 v3.2 governs Stage B and the North America target;
- docs/NORTH_AMERICA_MULTI_REGISTRY_PRODUCT_TARGET_V1.md is the product-target companion document;
- the roadmap must distinguish PRODUCT TARGET from CURRENT EXPERIMENT;
- Stage B remains NY OSC bounded P1;
- post-Stage-B source expansion must be adapter-based and benchmarked;
- Canada is in product scope, but no Canadian registry is considered supported until source/legal/terms/schema readiness is verified;
- patent work is deferred unless later evidence shows a narrow, strategically valuable opportunity;
- performance and economic evidence are the primary product-selection criteria.

---

## D-015 — Product UX composition uses Control Room shell + Executive dashboard + Evidence workspace

Date: 2026-09-25

Status: Accepted by Product Owner

Context:
FRONTEND_PRODUCT_UX_V1_OFFLINE produced and CI-verified three navigable synthetic concepts:

- Concept A — Intelligence Control Room;
- Concept B — Executive Intelligence;
- Concept C — Evidence Investigation Workspace.

The Product Owner reviewed the proposed composition and explicitly approved using all three concepts as complementary product surfaces rather than forcing one interface to serve every user job.

Decision:
1. adopt Concept A as the permanent application shell / operations workspace;
2. adopt Concept B as a first-class executive dashboard route for business/economic visibility;
3. adopt Concept C as the case-detail investigation workspace for evidence, contradictions, provenance, targetability context and human review;
4. keep the frontend product base on the existing Next.js/React/TypeScript reviewer console;
5. keep Streamlit as an internal diagnostic / engineering / safe reviewer surface until a later superseding decision;
6. do not add a permanent component library solely because the UX composition is now selected;
7. apply REUSE-FIRST before production component adoption, benchmarking mature UI libraries/templates for sidebar, data table, charting, forms and accessible primitives;
8. preserve all UX safety rules from FRONTEND_PRODUCT_UX_V1_OFFLINE:
   - synthetic/demo values must remain distinguishable from measured production KPIs;
   - unsupported registries must never appear supported;
   - visual actions cannot bypass deterministic backend authorization;
   - real PII web access requires authentication/RBAC and durable access audit first;
   - evidence, contradictions, provenance and cost remain inspectable;
   - human-gated decisions remain visually distinct from automated observations.

Reason:
The three concepts serve different jobs well:
- A optimizes daily operations and situational awareness;
- B optimizes management comprehension of economics, throughput and source readiness;
- C optimizes evidence-heavy case review and human decision quality.

Combining them preserves role-specific clarity without duplicating three separate products.

Alternatives considered:
- choose only Concept A;
- choose only Concept B;
- choose only Concept C;
- keep all three as equal standalone applications;
- rebuild the frontend from scratch.

Consequences:
- future frontend consolidation should produce one coherent design system and navigation model;
- A becomes the shell into which B and C are integrated as routes/workspaces;
- the current UX Lab remains useful as historical/prototyping evidence until superseded;
- no real PII, production write path, P1 gate or source access is enabled by this decision;
- frontend consolidation remains parallel/non-critical and must not displace the Stage B controller/LLC blocker.

