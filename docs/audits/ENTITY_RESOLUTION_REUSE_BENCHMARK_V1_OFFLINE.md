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

Economic ranking is allowed only for candidates that meet both synthetic safety
constraints:

- auto-match precision >= 98%;
- unsafe automatic case rate <= 2%.

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
