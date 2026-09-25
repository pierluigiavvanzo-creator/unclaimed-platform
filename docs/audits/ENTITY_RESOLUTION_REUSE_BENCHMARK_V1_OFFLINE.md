# ENTITY_RESOLUTION_REUSE_BENCHMARK_V1_OFFLINE

Date: 2026-09-25

Status: EXECUTION_HARNESS / SYNTHETIC ONLY

## Purpose

Compare reusable entity-resolution candidates before custom A05/A19 development.

Candidates:

- Splink 4.0.17;
- Dedupe 3.0.3 with BTrees 6.4 compatibility pin;
- RapidFuzz 3.14.6 weighted baseline.

Compatibility note:

The first isolated run exposed a Dedupe transitive dependency break when a newer
BTrees removed the byValue method from the relevant float-value bucket family.
BTrees 6.4 is therefore pinned for the reproducible benchmark. This integration
risk is part of the reuse decision rather than being hidden.

The benchmark uses only deterministic synthetic records.

It does not:

- access NY OSC or any other registry;
- use real owner PII;
- change P1 gates;
- add a runtime production dependency;
- choose a production confidence threshold.

## Dataset

The harness generates two synthetic registries with:

- 160 true cross-registry matched identities;
- 20 unmatched records on the left;
- 20 unmatched records on the right;
- deterministic perturbations for casing, typos, abbreviations, missing postal codes,
  omitted unit information, initials and name reversal;
- overlapping names/locations among unmatched distractors.

Splits:

- 60 matched left records for Dedupe training labels;
- 60 validation cases, including unmatched records;
- 60 test cases, including unmatched records.

## Fairness constraints

- all engines receive the same structured fields;
- no production/source data is used;
- Dedupe receives only synthetic training labels from the training split;
- thresholds are selected on validation only;
- test metrics are not used to tune the engines;
- Splink remains unsupervised except for validation threshold selection;
- RapidFuzz is a deterministic weighted baseline.

## Metrics

Technical:

- runtime;
- auto-match precision;
- human-review rate;
- unsafe automatic decision rate;
- recoverable match recall after review;
- safe automatic decision rate.

Economic proxy:

- illustrative review labor cost per 1,000 cases;
- assumptions: 5 minutes/review and USD 60/hour loaded human cost.

No monetary error penalty is invented.

Economic ranking is allowed only for candidates that meet all synthetic
safety/usefulness constraints:

- auto-match precision >= 98%;
- unsafe automatic case rate <= 2%;
- safe automatic decision coverage >= 25%;
- recoverable match recall after human review >= 95%.

This prevents a model from "winning" economically merely by routing almost every
case to a human reviewer.

The synthetic leader is NOT a production selection.

## Normalization note

This V1 intentionally does not benchmark libpostal/usaddress/probablepeople in the
same run. Their inclusion would confound entity-resolution quality with parser
quality. Address/name normalization should be benchmarked as a separate layer after
the core entity-resolution comparison.

## Reproducibility

The isolated GitHub Actions workflow pins the candidate package versions and writes:

benchmarks/entity_resolution_v1/results.json

The workflow is restricted to the benchmark branch or manual dispatch.

## Product rule

A reusable library can only move from BENCHMARKED to ADOPTED after:

- synthetic benchmark passes;
- real P1/P2 produces labelled domain evidence;
- privacy/provenance constraints are preserved;
- human-review economics are measured on real workflow data.


## Executed result

Final benchmark checkpoint:

`66b93e4f63a56677ba252ddacb33b2bda8efbcfd`

GitHub Actions benchmark run:

`36128928676 — SUCCESS`

Persisted synthetic result:

`benchmarks/entity_resolution_v1/results.v1.json`

### Test metrics

| Candidate | Runtime | Auto-match precision | Human review | Unsafe auto cases | Recoverable match recall after review | Illustrative review labor / 1,000 |
|---|---:|---:|---:|---:|---:|---:|
| RapidFuzz weighted baseline | 0.104 s | 90.0% | 25.0% | 31.7% | 66.0% | $1,250 |
| Dedupe RecordLink | 4.950 s | 80.0% | 0.0% | 20.0% | 100.0% | $0 |
| Splink probabilistic linkage | 0.956 s | 93.75% | 21.7% | 41.7% | 52.0% | $1,083 |

All figures above are synthetic benchmark results, not production accuracy claims.

### Result

`NO_SAFE_SYNTHETIC_WINNER`

None of the candidates met all V1 constraints:

- auto-match precision >= 98%;
- unsafe automatic case rate <= 2%;
- safe automatic decision coverage >= 25%;
- recoverable match recall after review >= 95%.

## Economic interpretation

The benchmark demonstrates why raw human-review cost cannot be optimized in isolation.

Dedupe appears cheapest if only review labor is counted, because its learned threshold routed every test case to an automatic match. But 12 of 60 test cases were wrong automatic matches. That makes the apparent USD 0 review cost economically misleading.

Splink reduced review workload to 21.7%, but its current V1 configuration missed too many true matches below the review boundary. Its low review cost is therefore also not a valid economic win.

RapidFuzz was by far the fastest and simplest candidate, but it also failed the accuracy/safety gate. Its economic value is as a transparent similarity primitive, not as an autonomous identity-resolution authority.

Therefore the correct optimization order remains:

EXPECTED ERROR COST
-> SAFE MATCH PRECISION / RECALL
-> HUMAN MINUTES
-> COMPUTE / RUNTIME COST

The benchmark provides no evidence that auto-linking should be enabled.

## Reuse decisions after executed V1

### RapidFuzz

Decision:

`REUSE_AS_FEATURE_PRIMITIVE`

Reason:

- extremely low integration cost;
- fastest executed candidate;
- MIT;
- transparent string-similarity features;
- useful inside candidate generation/blocking/explainability;
- not sufficiently safe as an autonomous matcher.

### Splink

Decision:

`DEFER_AND_REBENCHMARK_WITH_DOMAIN_LABELS`

Reason:

- strongest architecture/maintainability fit among probabilistic linkage engines;
- mature repository and PostgreSQL path;
- explicit probabilistic record-linkage model;
- current synthetic configuration did not meet safety/recall requirements;
- should be benchmarked again only when real labelled P1/P2 identity examples exist and normalization is representative.

### Dedupe

Decision:

`DEFER_SECONDARY_CHALLENGER`

Reason:

- active-learning/human-labelled workflow is strategically interesting;
- test recall was high;
- automatic false-match rate was unacceptable;
- integration required an explicit BTrees 6.4 compatibility pin;
- this transitive compatibility burden raises maintenance cost.

### Custom A05/A19 entity-resolution model

Decision:

`REJECT_NOW`

Reason:

No evidence yet justifies custom model development ahead of reusable candidates plus better data normalization and real labels.

## What should happen next

Do not spend more Stage B time tuning synthetic thresholds.

The next identity-resolution benchmark should be triggered only after one of these becomes available:

1. real P1/P2 labelled identity-resolution examples;
2. a representative synthetic corpus built from observed non-sensitive field-shape/error patterns;
3. multi-registry source work that requires actual cross-registry matching.

At that point run V2 with:

- libpostal / address normalization;
- probablepeople or equivalent name normalization;
- RapidFuzz features;
- Splink;
- Dedupe;
- fixed labelled holdout set;
- false-positive cost and reviewer minutes measured from real workflow.

## Product decision

For current Unclaimed work:

`DETERMINISTIC GATES + HUMAN REVIEW`

remain authoritative.

RapidFuzz may be reused later as a feature primitive without changing that authority.

No entity-resolution package is adopted as the production matcher by this V1.

RESULT: PASS_WITH_NO_AUTO_LINKER_ADOPTION
