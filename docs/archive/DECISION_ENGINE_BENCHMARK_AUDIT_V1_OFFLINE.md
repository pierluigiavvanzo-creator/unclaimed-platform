# DECISION ENGINE BENCHMARK AUDIT V1 — OFFLINE

Date: 2026-09-25

Status: OFFLINE / REUSE-FIRST / NO RUNTIME INTEGRATION / NO REAL PII / NO PAID API CALLS

Baseline:

- canonical repository: pierluigiavvanzo-creator/unclaimed-platform
- canonical main at audit start: 5846f936abd495d4ab263e444a9f1e0ef3997399
- current product phase: Stage B / P1 blocked on genuine US controller formation
- all seven P1 gates remain outside this audit and are not changed

## 1. Executive result

Typed decision engines are strategically relevant to Unclaimed, but they must sit below the deterministic governance layer.

Recommended architecture:

EVIDENCE / CASE STATE
-> OPTIONAL TYPED DECISION ENGINE
-> PROBABILITIES / CONFIDENCE / TYPED SIGNALS
-> DETERMINISTIC POLICY + BUDGET + PRIVACY + HUMAN GATES
-> CONTINUE / HUMAN_REVIEW / STOP
-> AUDIT

Do not let Laya, Jev or an LLM directly grant source access, PII access, outreach, representation, fee, claim or legal/compliance authority.

### Current reuse decisions

| Candidate | Current decision | Why |
|---|---|---|
| Existing deterministic core | KEEP / AUTHORITATIVE | Required for hard policy, authorization and audit boundaries |
| TypeSafe Jev | DEFER_FOR_P1 / STRONG P2+ CANDIDATE | Extremely low variable cost and low operations burden; external provider/privacy review required |
| Laya | BENCHMARK / CONDITIONAL_WRAP | Open weights, Apache-2.0, local privacy/control and strong engineering signals; very young and domain/calibration risk remains |
| Open Jev typed decision engine | INSPIRE / BENCHMARK_ONLY | Interesting open local baseline and calibration research; much less mature production engineering |
| Laya -> Jev cascade | DEFER | Potential latency/privacy/scale benefit, but complexity is not economically justified before domain evidence |

## 2. What problem a typed decision engine could solve

Unclaimed already has deterministic logic for facts and authorization.

The missing future capability is not another free-form text generator. It is a bounded semantic signal for cases where evidence is present but the correct interpretation is not expressible as a simple exact rule.

Potential future tasks:

- evidence relevance;
- contradiction detection support;
- case routing;
- service-need evidence classification;
- bounded-resolvability support;
- human-review prioritization;
- source/document triage;
- confidence-aware queue ordering.

Not appropriate as final authority for:

- legal conclusions;
- privacy authorization;
- PII-access grants;
- source/download authorization;
- fee/statute application;
- outreach authorization;
- claimant/beneficiary legal status;
- representation;
- claim submission.

## 3. Sources reviewed

### Laya

Repository:

https://github.com/NandhaKishorM/laya

License:

Apache-2.0.

Repository creation date observed from GitHub API:

2026-09-18.

Observed GitHub adoption signal during this audit:

approximately 23.7k stars and 2.0k forks.

Do not treat rapid stars as maturity evidence.

Engineering evidence observed:

- Python package;
- Python 3.10-3.13 compatibility declared;
- 112 Python files;
- 50 Python test files under tests/;
- CI on Linux across Python 3.10-3.13;
- Windows CI;
- package build checks;
- separate security workflow;
- gitleaks;
- pip-audit;
- CodeQL;
- unsafe-deserialization checks;
- shell/dynamic-execution checks;
- benchmark scripts and raw-result artifacts.

Model/runtime claims and measured artifacts:

- typed question primitives: choice, score, noul;
- no free-form text generation;
- English checkpoint: ModernBERT-large, 421M;
- multilingual checkpoint: 322M;
- typed-decisions checkpoint: ModernBERT-large, 421M;
- measured T4 latency published by the project:
  - roughly 39.5 ms for one English question;
  - roughly 32.8 ms for one multilingual question;
  - batched throughput reported above 100 questions/sec;
- project publishes reproducible benchmark artifacts rather than only a marketing table.

Important limitations:

- repository is extremely new;
- package status is Beta;
- base checkpoints perform poorly on the typed-decisions benchmark unless specialized/fine-tuned;
- Laya's own benchmark reports meaningful calibration weaknesses before refitting;
- high-cardinality choice spaces are a documented weakness;
- independent small-domain evaluations found confident-and-wrong cases;
- third-party results do not consistently reproduce a universal advantage over Jev.

Primary public evidence:

- https://github.com/NandhaKishorM/laya
- https://github.com/NandhaKishorM/laya/blob/main/BENCHMARKS.md

### TypeSafe Jev

Official product sources:

- https://typesafe.ai/
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://api.typesafe.ai/docs
- https://typesafe.ai/legal/data-processing
- https://typesafe.ai/legal/mca

Observed characteristics:

- closed hosted API;
- typed choice / score / noul-like decisions;
- probabilities/confidence returned with typed results;
- official price currently published as USD 42 per billion input tokens, equivalent to USD 0.042 per million input tokens;
- output tokens are described as free / not metered;
- official published end-to-end latency range is approximately 70-500 ms depending on workload;
- TypeSafe launched Jev publicly on 2026-09-15;
- the API requires authentication;
- external processing therefore requires a provider/privacy/terms review before real Unclaimed owner PII could be submitted.

Important limitation:

Jev is also very new. Commercial availability and operational simplicity do not equal long production history.

### Independent Laya/Jev diagnostic

Repository:

https://github.com/yibie/laya-jev-lab

Observed benchmark:

40 Chinese support-ticket classification cases.

Reported:

- Jev: 31/40 = 78%, mean latency 588 ms;
- Laya local MLX: 23/40 = 57%, mean latency 7.6 ms;
- Laya -> Jev cascade at 0.60 threshold:
  - 78% accuracy;
  - 55% escalation to Jev;
  - 327 ms average latency.

The authors explicitly state the sample is small, domain-specific and insufficient for generalization.

Most important lesson:

confidence must be tested on the actual domain. A model can be confidently wrong.

### Open Jev typed decision engine

Repository:

https://github.com/intikhab49/open-jev-typed-decision-engine

Observed characteristics:

- Apache-2.0;
- Python;
- 150M encoder approach;
- public benchmark/evaluation scripts;
- published typed-decisions result below Jev but with stronger reported calibration in its own evaluation;
- one GitHub workflow;
- no conventional tests/ directory observed during this audit.

Decision:

useful research control, not a production dependency candidate today.

## 4. Benchmark evidence — do not over-read headline accuracy

### Published typed-decisions benchmark

Laya's current public benchmark reports, on 400 cases / 2,000 decisions:

| Model | Accuracy | Brier | ECE |
|---|---:|---:|---:|
| Laya typed-decisions | 0.766 | 0.061 | 0.213 |
| Jev 1.13 published reference | 0.727 | 0.148 | 0.144 |
| Laya base English | 0.361 | 0.316 | 0.175 |

Interpretation:

- fine-tuned Laya can outperform the published Jev top-1 number on that benchmark;
- base Laya cannot be assumed to be strong without domain specialization;
- Laya typed-decisions has better Brier in that table but worse ECE than the Jev reference;
- these numbers are not an Unclaimed benchmark;
- the Jev row is not measured by Laya in the same API run and must be treated as indicative.

Therefore:

NO ENGINE IS SELECTED FROM PUBLIC ACCURACY ALONE.

## 5. Economic model

The economically relevant metric for Unclaimed should be:

TOTAL_DECISION_COST
=
MODEL_VARIABLE_COST
+ ALLOCATED_INFRA_COST
+ ENGINEERING/OPS_COST
+ HUMAN_REVIEW_COST
+ EXPECTED_ERROR_COST

The dominant terms are expected to be human review and error cost, not raw inference price.

### 5.1 Jev variable-cost sensitivity

Current official input price used for this model:

USD 0.042 / 1,000,000 input tokens.

Illustrative cost per call:

| Average input tokens/call | Jev variable cost/call |
|---:|---:|
| 500 | $0.000021 |
| 1,000 | $0.000042 |
| 2,500 | $0.000105 |
| 5,000 | $0.000210 |
| 10,000 | $0.000420 |

Illustrative monthly variable cost:

| Decisions/month | 1k tokens/call | 5k tokens/call |
|---:|---:|---:|
| 10,000 | $0.42 | $2.10 |
| 100,000 | $4.20 | $21.00 |
| 1,000,000 | $42.00 | $210.00 |

This excludes taxes, plan/credit mechanics, network and any future pricing change.

Conclusion:

at MVP and early-scale volumes, Jev's inference price is economically negligible relative to human labor.

### 5.2 Local Laya fixed-infrastructure sensitivity

Current RunPod public price reference used only as an infrastructure proxy:

a Secure Cloud GPU can start at approximately USD 0.27/hour.

This is NOT a claim that the $0.27 GPU reproduces Laya's published T4 latency.

Always-on lower-bound infrastructure proxy:

- $0.27/hour;
- approximately $194.40 for a 30-day month;
- approximately $2,365.20/year.

Ignoring engineering/ops cost, Jev API spend equals $0.27/hour at approximately:

| Avg input tokens/call | Jev calls/hour equal to $0.27 |
|---:|---:|
| 500 | 12,857 |
| 1,000 | 6,429 |
| 2,500 | 2,571 |
| 5,000 | 1,286 |
| 10,000 | 643 |

Monthly break-even against a continuously running $0.27/hour GPU is approximately:

- 4.63 million decisions/month at 1k input tokens/call;
- 0.93 million decisions/month at 5k input tokens/call.

These are infrastructure-only break-even points.

They exclude:

- deployment engineering;
- monitoring;
- model downloads/storage;
- patching;
- security work;
- idle/warm-up/cold-start behavior;
- redundancy;
- availability;
- incident response;
- model calibration;
- staff time.

Therefore local Laya is not economically justified merely because the API fee is zero.

Local Laya becomes economically attractive when one or more of these are material:

- PII locality is strategically valuable;
- external-provider exposure is undesirable;
- very high sustained volume exists;
- owned hardware is already available;
- latency is economically material;
- model specialization materially reduces human review/error cost.

### 5.3 Human-review sensitivity

Illustrative only — NOT a project KPI or approved labor rate.

At a loaded human labor rate of $60/hour:

- 2-minute review = $2.00;
- 5-minute review = $5.00;
- 10-minute review = $10.00.

At 1,000 input tokens per Jev call:

- $2.00 equals roughly 47,619 Jev calls;
- $5.00 equals roughly 119,048 Jev calls;
- $10.00 equals roughly 238,095 Jev calls.

Meaning:

one avoided five-minute human review can economically outweigh approximately one hundred thousand 1k-token Jev calls.

Therefore model choice should optimize:

1. safe review deflection;
2. false-positive reduction;
3. calibrated confidence;
4. human minutes/case;

before optimizing fractions of a cent in model inference.

## 6. Economic feasibility ranking by phase

### Phase A — current P1

Winner:

DETERMINISTIC CORE + HUMAN REVIEW.

Reason:

- P1 scope currently allows no paid external L2-A provider spend;
- real P1 is not yet authorized;
- there is no domain evidence to justify an AI targetability score;
- adding Jev or Laya now would increase experimental variables without answering the current business question.

Laya may be used only for synthetic/offline benchmark work if separately implemented later.

Jev should not be called with real P1 data under the current gates.

### Phase B — early P2/P3, low-to-moderate volume

Economic preference if provider/privacy review passes:

JEV FIRST.

Reason:

- negligible variable inference cost at expected early volume;
- no GPU fleet/serving operations;
- typed probabilistic interface fits the architecture;
- easiest way to measure whether typed decisions actually save human time.

Primary risk:

external provider / privacy / vendor dependency.

Alternative when local processing is required:

LAYA CONDITIONAL WRAP.

### Phase C — larger validated volume

Re-evaluate:

LAYA LOCAL
vs
JEV
vs
LAYA -> JEV CASCADE.

The correct answer depends on measured:

- calls/month;
- input size;
- confidence calibration on Unclaimed;
- safe-auto decision coverage;
- human-review rate;
- false-positive/false-negative cost;
- infrastructure utilization;
- privacy/compliance overhead.

Do not select the cascade because it is technically elegant.

At Jev's current price, cascade savings on API spend are too small to justify extra architecture at low volume.

## 7. Recommended Unclaimed benchmark contract

Do not ask a decision engine for one opaque "targetability score".

Decompose it into typed, auditable questions.

Candidate synthetic benchmark dimensions:

### A. Evidence support

- does the evidence materially support service need?
- is the evidence internally contradictory?
- is a source statement direct evidence or only an inference?

### B. Resolvability support

- does the current evidence indicate a bounded next research step?
- is there insufficient evidence?
- does the case require human identity conflict resolution?

### C. Reviewer routing

- continue deterministic processing;
- queue human review;
- stop for insufficient evidence.

### D. Confidence behavior

Measure:

- accuracy;
- Brier score;
- ECE;
- risk/coverage curve;
- false-positive rate;
- false-negative rate;
- high-confidence wrong rate;
- option-order sensitivity;
- stability under paraphrase;
- latency;
- tokens/cost;
- human-review deflection.

The authoritative policy still decides what confidence band can be used for automation.

## 8. Domain benchmark prerequisite

No public benchmark can answer which engine is best for Unclaimed.

A future real selection requires a frozen, labelled Unclaimed decision dataset with:

- provenance;
- expected typed answer;
- ambiguity marker;
- human-review label;
- no unnecessary PII;
- separate validation and test partitions;
- no tuning on the final test partition.

Until sufficient real outcome data exists:

do not invent a production confidence threshold.

Synthetic fixtures may validate integration and failure behavior, but not commercial accuracy.

## 9. Security/privacy fit

### Jev

Advantages:

- no model hosting;
- minimal integration surface;
- official API contract;
- DPA and commercial terms are published.

Risks:

- external processing;
- provider dependency;
- PII transfer/security/legal review required before real owner data;
- model behavior/version can change under a hosted service.

### Laya

Advantages:

- Apache-2.0;
- open weights;
- can be self-hosted;
- local processing is compatible with stronger data-minimization/locality strategies;
- model/version can be pinned.

Risks:

- we own serving, patching, monitoring and incident handling;
- project is extremely new;
- model confidence cannot be trusted without domain calibration;
- model weights and ML supply chain add operational surface.

## 10. Final recommendation

### What is economically best now?

DO NOT INTEGRATE A DECISION ENGINE INTO REAL P1.

The current Stage B experiment should stay deterministic + human-gated.

### What should be benchmarked first after P1 supports continuation?

1. Jev as the lowest-operations economic baseline, subject to provider/privacy authorization.
2. Laya as the local/private open-weight challenger.
3. The existing deterministic rules as the mandatory hard-boundary baseline.
4. Open-Jev only as a research control.

### What is the most likely economically efficient production pattern?

At low/moderate volume:

DETERMINISTIC GATES
-> JEV SEMANTIC SIGNAL
-> HUMAN REVIEW FOR UNCERTAINTY.

At high volume or where PII locality has material value:

DETERMINISTIC GATES
-> CALIBRATED LAYA LOCAL
-> HUMAN REVIEW / OPTIONAL EXTERNAL ESCALATION.

A Laya -> Jev cascade should be considered only after measured Unclaimed traffic demonstrates that its saved latency/privacy/API exposure is worth the added operational complexity.

## 11. Reuse-first decisions

### Laya

decision: DEFER / CONDITIONAL_WRAP

reason:

Strong fit and strong engineering signal, but insufficient project age and no Unclaimed-domain calibration.

### Jev

decision: DEFER_FOR_P1 / BENCHMARK_FIRST_AFTER_P1

reason:

Best current low-volume economic profile if external processing is authorized, but cannot be introduced into current P1 scope without a fresh provider/privacy/budget decision.

### Open Jev

decision: INSPIRE / BENCHMARK_ONLY

reason:

Useful calibration and open-model research, insufficient production maturity.

### Custom decision engine

decision: REJECT_NOW

reason:

Existing reusable candidates are strong enough that building our own model would violate REUSE-FIRST before we have Unclaimed training/outcome data.

## 12. Next trigger

Do not implement adapters yet.

Trigger a real decision-engine integration benchmark only when:

- P1/P2 produces enough labelled decision examples to measure Unclaimed-domain error/calibration; and
- the Product Owner has decided whether an external provider may process the relevant data class.

Until then this audit is sufficient for architectural planning.

## 13. Economic decision summary

The main optimization order should be:

FALSE-POSITIVE / FALSE-NEGATIVE COST
-> HUMAN MINUTES SAVED
-> SAFE AUTOMATION COVERAGE
-> CALIBRATION
-> PRIVACY / PROVIDER COST
-> MODEL INFERENCE COST
-> LATENCY

Raw inference cost comes late because both Jev and local encoder inference are already cheap relative to human review.

RESULT: PASS_WITH_DEFERRED_INTEGRATION
