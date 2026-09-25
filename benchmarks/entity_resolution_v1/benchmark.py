#!/usr/bin/env python
"""Synthetic entity-resolution benchmark for reuse decisions only.

This harness never reads project/source data. It generates deterministic synthetic
records, trains/evaluates reusable entity-resolution candidates and writes a JSON
result suitable for economic/human-review comparison.

Candidates:
- RapidFuzz weighted top-1 baseline
- Dedupe RecordLink with synthetic labelled training examples
- Splink probabilistic link-only model

The benchmark is NOT a production threshold-selection artifact.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import time
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REVIEW_MINUTES = 5.0
LOADED_HUMAN_COST_PER_HOUR_USD = 60.0
TARGET_AUTO_PRECISION = 0.98
SEED = 20260925

FIRST_NAMES = [
    "Avery",
    "Jordan",
    "Morgan",
    "Taylor",
    "Cameron",
    "Riley",
    "Quinn",
    "Parker",
    "Reese",
    "Casey",
    "Hayden",
    "Rowan",
    "Emerson",
    "Finley",
    "Dakota",
    "Skyler",
    "Robin",
    "Jules",
    "Kendall",
    "Blair",
]

LAST_NAMES = [
    "Anderson",
    "Bennett",
    "Carter",
    "Diaz",
    "Edwards",
    "Foster",
    "Garcia",
    "Harris",
    "Irwin",
    "Johnson",
    "Keller",
    "Lopez",
    "Martin",
    "Nguyen",
    "Owens",
    "Patel",
    "Quincy",
    "Roberts",
    "Singh",
    "Turner",
    "Underwood",
    "Vargas",
    "Walker",
    "Xu",
    "Young",
    "Zimmer",
    "Brooks",
    "Clark",
    "Davis",
    "Evans",
]

STREET_NAMES = [
    "Maple",
    "Oak",
    "Cedar",
    "Pine",
    "Lake",
    "Hill",
    "River",
    "Park",
    "Walnut",
    "Cherry",
    "Spruce",
    "Willow",
    "Sunset",
    "Highland",
    "Meadow",
    "Forest",
    "Washington",
    "Lincoln",
    "Jefferson",
    "Franklin",
]

LOCATIONS = [
    ("Albany", "NY", "12207"),
    ("Buffalo", "NY", "14202"),
    ("Rochester", "NY", "14604"),
    ("Syracuse", "NY", "13202"),
    ("Brooklyn", "NY", "11201"),
    ("San Diego", "CA", "92101"),
    ("Sacramento", "CA", "95814"),
    ("Oakland", "CA", "94607"),
    ("Fresno", "CA", "93721"),
    ("San Jose", "CA", "95113"),
    ("Austin", "TX", "78701"),
    ("Dallas", "TX", "75201"),
    ("Houston", "TX", "77002"),
    ("Miami", "FL", "33131"),
    ("Orlando", "FL", "32801"),
    ("Chicago", "IL", "60601"),
    ("Springfield", "IL", "62701"),
    ("Boston", "MA", "02108"),
    ("Seattle", "WA", "98101"),
    ("Denver", "CO", "80202"),
]

SUFFIXES = ["Street", "Avenue", "Road", "Boulevard", "Drive", "Lane"]
ABBREVIATIONS = {
    "Street": "St",
    "Avenue": "Ave",
    "Road": "Rd",
    "Boulevard": "Blvd",
    "Drive": "Dr",
    "Lane": "Ln",
}


@dataclass(frozen=True)
class Dataset:
    left: dict[str, dict[str, str]]
    right: dict[str, dict[str, str]]
    truth: dict[str, str | None]
    train_left_ids: tuple[str, ...]
    validation_left_ids: tuple[str, ...]
    test_left_ids: tuple[str, ...]


@dataclass(frozen=True)
class CandidateScore:
    right_id: str | None
    score: float


def _clean_text(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9 ]+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def _typo(value: str, seed: int) -> str:
    if len(value) < 4:
        return value
    rng = random.Random(seed)
    pos = rng.randrange(1, len(value) - 1)
    chars = list(value)
    chars[pos - 1], chars[pos] = chars[pos], chars[pos - 1]
    return "".join(chars)


def _drop_vowel(value: str) -> str:
    for index, char in enumerate(value):
        if index > 0 and char.lower() in "aeiou":
            return value[:index] + value[index + 1 :]
    return value


def _abbreviate_address(value: str) -> str:
    result = value
    for long_form, short_form in ABBREVIATIONS.items():
        result = result.replace(long_form, short_form)
    result = result.replace("Apartment", "Apt")
    return result


def _base_record(index: int) -> dict[str, str]:
    first = FIRST_NAMES[index % len(FIRST_NAMES)]
    last = LAST_NAMES[(index * 7 + 3) % len(LAST_NAMES)]
    street = STREET_NAMES[(index * 11 + 5) % len(STREET_NAMES)]
    suffix = SUFFIXES[(index * 5 + 2) % len(SUFFIXES)]
    city, state, postal_code = LOCATIONS[(index * 13 + 1) % len(LOCATIONS)]
    number = 100 + ((index * 37 + 19) % 8900)
    unit = f" Apartment {1 + index % 24}" if index % 5 == 0 else ""
    return {
        "first_name": first,
        "last_name": last,
        "address": f"{number} {street} {suffix}{unit}",
        "city": city,
        "state": state,
        "postal_code": postal_code,
    }


def _mutate_right(record: Mapping[str, str], index: int) -> dict[str, str]:
    result = dict(record)
    mode = index % 8

    if mode == 0:
        result["address"] = _abbreviate_address(result["address"]).upper()
        result["first_name"] = result["first_name"].upper()
    elif mode == 1:
        result["first_name"] = _typo(result["first_name"], index)
        result["address"] = _abbreviate_address(result["address"])
    elif mode == 2:
        result["last_name"] = _typo(result["last_name"], index + 1000)
        result["address"] = _abbreviate_address(result["address"])
    elif mode == 3:
        result["first_name"] = result["first_name"][0]
        result["address"] = result["address"].replace(" Apartment ", " Apt ")
    elif mode == 4:
        result["address"] = re.sub(r" Apartment \d+$", "", result["address"])
        result["city"] = _drop_vowel(result["city"])
    elif mode == 5:
        result["first_name"] = _drop_vowel(result["first_name"])
        result["last_name"] = result["last_name"].upper()
        result["postal_code"] = ""
    elif mode == 6:
        result["address"] = _typo(_abbreviate_address(result["address"]), index + 2000)
        result["city"] = result["city"].upper()
    else:
        result["first_name"], result["last_name"] = (
            result["last_name"],
            result["first_name"],
        )
        result["address"] = _abbreviate_address(result["address"])

    return result


def build_dataset() -> Dataset:
    matched_count = 160
    unmatched_left_count = 20
    unmatched_right_count = 20

    left: dict[str, dict[str, str]] = {}
    right: dict[str, dict[str, str]] = {}
    truth: dict[str, str | None] = {}

    for index in range(matched_count):
        left_id = f"L{index:04d}"
        right_id = f"R{index:04d}"
        base = _base_record(index)
        left[left_id] = base
        right[right_id] = _mutate_right(base, index)
        truth[left_id] = right_id

    for offset in range(unmatched_left_count):
        index = matched_count + offset
        left_id = f"L{index:04d}"
        record = _base_record(index + 500)
        # Keep locations/names intentionally overlapping with matched data.
        if offset % 2 == 0:
            record["last_name"] = LAST_NAMES[offset % len(LAST_NAMES)]
        left[left_id] = record
        truth[left_id] = None

    for offset in range(unmatched_right_count):
        index = matched_count + offset
        right_id = f"R{index:04d}"
        record = _base_record(index + 900)
        if offset % 2 == 0:
            record["last_name"] = LAST_NAMES[(offset + 1) % len(LAST_NAMES)]
        right[right_id] = _mutate_right(record, index + 900)

    train_left_ids = tuple(f"L{i:04d}" for i in range(60))
    validation_left_ids = tuple(
        [f"L{i:04d}" for i in range(60, 110)]
        + [f"L{i:04d}" for i in range(160, 170)]
    )
    test_left_ids = tuple(
        [f"L{i:04d}" for i in range(110, 160)]
        + [f"L{i:04d}" for i in range(170, 180)]
    )

    return Dataset(
        left=left,
        right=right,
        truth=truth,
        train_left_ids=train_left_ids,
        validation_left_ids=validation_left_ids,
        test_left_ids=test_left_ids,
    )


def _top_by_left(
    pairs: Iterable[tuple[str, str, float]],
    left_ids: Iterable[str],
) -> dict[str, CandidateScore]:
    top = {left_id: CandidateScore(None, 0.0) for left_id in left_ids}
    for left_id, right_id, raw_score in pairs:
        score = float(raw_score)
        current = top.get(left_id)
        if current is not None and score > current.score:
            top[left_id] = CandidateScore(right_id, max(0.0, min(1.0, score)))
    return top


def rapidfuzz_scores(dataset: Dataset) -> dict[str, CandidateScore]:
    from rapidfuzz.fuzz import WRatio

    def similarity(left: Mapping[str, str], right: Mapping[str, str]) -> float:
        weights = {
            "first_name": 0.22,
            "last_name": 0.30,
            "address": 0.30,
            "city": 0.08,
            "state": 0.04,
            "postal_code": 0.06,
        }
        score = 0.0
        for field, weight in weights.items():
            left_value = _clean_text(left[field])
            right_value = _clean_text(right[field])
            if not left_value or not right_value:
                continue
            score += weight * (WRatio(left_value, right_value) / 100.0)
        return score

    output: dict[str, CandidateScore] = {}
    for left_id, left_record in dataset.left.items():
        best = CandidateScore(None, 0.0)
        for right_id, right_record in dataset.right.items():
            # Cheap deterministic blocking keeps the baseline economically realistic.
            if left_record["state"] != right_record["state"]:
                continue
            score = similarity(left_record, right_record)
            if score > best.score:
                best = CandidateScore(right_id, score)
        output[left_id] = best
    return output


def dedupe_scores(dataset: Dataset) -> dict[str, CandidateScore]:
    import dedupe

    fields = [
        dedupe.variables.String("first_name", has_missing=True),
        dedupe.variables.String("last_name", has_missing=True),
        dedupe.variables.String("address", has_missing=True),
        dedupe.variables.String("city", has_missing=True),
        dedupe.variables.String("state", has_missing=True),
        dedupe.variables.String("postal_code", has_missing=True),
    ]
    linker = dedupe.RecordLink(fields, num_cores=0, in_memory=True)
    linker.prepare_training(dataset.left, dataset.right, sample_size=5000)

    match_pairs: list[tuple[dict[str, str], dict[str, str]]] = []
    distinct_pairs: list[tuple[dict[str, str], dict[str, str]]] = []

    for left_id in dataset.train_left_ids[:40]:
        right_id = dataset.truth[left_id]
        assert right_id is not None
        match_pairs.append((dataset.left[left_id], dataset.right[right_id]))

    train_ids = list(dataset.train_left_ids)
    for offset in range(100):
        left_id = train_ids[offset % len(train_ids)]
        true_right = dataset.truth[left_id]
        candidate_index = (offset * 17 + 11) % 60
        candidate_id = f"R{candidate_index:04d}"
        if candidate_id == true_right:
            candidate_id = f"R{(candidate_index + 1) % 60:04d}"
        distinct_pairs.append((dataset.left[left_id], dataset.right[candidate_id]))

    linker.mark_pairs({"match": match_pairs, "distinct": distinct_pairs})
    linker.train(recall=0.95, index_predicates=False)

    links = linker.join(
        dataset.left,
        dataset.right,
        threshold=0.0,
        constraint="many-to-many",
    )
    pairs = (
        (str(left_right[0]), str(left_right[1]), float(score))
        for left_right, score in links
    )
    return _top_by_left(pairs, dataset.left)


def splink_scores(dataset: Dataset) -> dict[str, CandidateScore]:
    import pandas as pd
    import splink.comparison_library as cl
    from splink import DuckDBAPI, Linker, SettingsCreator, block_on

    left_rows = [
        {"unique_id": left_id, **record}
        for left_id, record in dataset.left.items()
    ]
    right_rows = [
        {"unique_id": right_id, **record}
        for right_id, record in dataset.right.items()
    ]
    left_df = pd.DataFrame(left_rows)
    right_df = pd.DataFrame(right_rows)

    settings = SettingsCreator(
        link_type="link_only",
        unique_id_column_name="unique_id",
        probability_two_random_records_match=160 / (180 * 180),
        blocking_rules_to_generate_predictions=[
            block_on("state"),
            block_on("postal_code"),
        ],
        comparisons=[
            cl.NameComparison("first_name"),
            cl.NameComparison("last_name"),
            cl.JaroWinklerAtThresholds("address", [0.95, 0.85, 0.70]),
            cl.JaroWinklerAtThresholds("city", [0.95, 0.80]),
            cl.ExactMatch("state").configure(term_frequency_adjustments=True),
            cl.DamerauLevenshteinAtThresholds("postal_code", [1, 2]),
        ],
    )

    linker = Linker(
        [left_df, right_df],
        settings,
        db_api=DuckDBAPI(),
        input_table_aliases=["left_registry", "right_registry"],
    )
    linker.training.estimate_u_using_random_sampling(max_pairs=50_000)
    linker.training.estimate_parameters_using_expectation_maximisation(
        block_on("state", "last_name")
    )
    linker.training.estimate_parameters_using_expectation_maximisation(
        block_on("state", "first_name")
    )
    linker.training.estimate_parameters_using_expectation_maximisation(
        block_on("postal_code")
    )

    predictions = linker.inference.predict(
        threshold_match_probability=0.0
    ).as_pandas_dataframe()

    pairs = (
        (
            str(row.unique_id_l),
            str(row.unique_id_r),
            float(row.match_probability),
        )
        for row in predictions.itertuples()
    )
    return _top_by_left(pairs, dataset.left)


def _binary_metrics(
    top: Mapping[str, CandidateScore],
    truth: Mapping[str, str | None],
    left_ids: Iterable[str],
    threshold: float,
) -> dict[str, float]:
    tp = fp = fn = tn = 0
    for left_id in left_ids:
        candidate = top[left_id]
        actual = truth[left_id]
        predicted = candidate.right_id if candidate.score >= threshold else None
        if actual is None:
            if predicted is None:
                tn += 1
            else:
                fp += 1
        elif predicted == actual:
            tp += 1
        else:
            fn += 1
            if predicted is not None:
                fp += 1

    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0
    )
    return {
        "tp": float(tp),
        "fp": float(fp),
        "fn": float(fn),
        "tn": float(tn),
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def select_thresholds(
    top: Mapping[str, CandidateScore],
    dataset: Dataset,
) -> tuple[float, float, dict[str, Any]]:
    validation_ids = dataset.validation_left_ids
    candidates = sorted(
        {
            0.0,
            1.0,
            *[
                round(top[left_id].score, 6)
                for left_id in validation_ids
            ],
        }
    )

    best_f1_threshold = 0.5
    best_f1 = -1.0
    for threshold in candidates:
        metrics = _binary_metrics(top, dataset.truth, validation_ids, threshold)
        if metrics["f1"] > best_f1:
            best_f1 = metrics["f1"]
            best_f1_threshold = threshold

    auto_candidates: list[tuple[float, float, float, int]] = []
    for threshold in candidates:
        metrics = _binary_metrics(top, dataset.truth, validation_ids, threshold)
        predicted_count = int(metrics["tp"] + metrics["fp"])
        if predicted_count >= 5 and metrics["precision"] >= TARGET_AUTO_PRECISION:
            auto_candidates.append(
                (
                    metrics["recall"],
                    metrics["precision"],
                    -threshold,
                    predicted_count,
                )
            )

    if auto_candidates:
        _, _, negative_threshold, _ = max(auto_candidates)
        auto_threshold = -negative_threshold
    else:
        auto_threshold = 1.000001

    review_threshold = min(best_f1_threshold, auto_threshold)
    validation = {
        "auto_threshold": auto_threshold,
        "review_threshold": review_threshold,
        "best_f1": best_f1,
        "best_f1_threshold": best_f1_threshold,
        "target_auto_precision": TARGET_AUTO_PRECISION,
    }
    return auto_threshold, review_threshold, validation


def evaluate_three_way(
    top: Mapping[str, CandidateScore],
    dataset: Dataset,
    auto_threshold: float,
    review_threshold: float,
) -> dict[str, Any]:
    total = len(dataset.test_left_ids)
    true_matches = sum(
        1 for left_id in dataset.test_left_ids if dataset.truth[left_id] is not None
    )

    auto_match = auto_match_correct = wrong_auto_match = 0
    human_review = 0
    auto_no_match = auto_no_match_correct = missed_true_match = 0

    for left_id in dataset.test_left_ids:
        candidate = top[left_id]
        actual = dataset.truth[left_id]

        if candidate.score >= auto_threshold:
            auto_match += 1
            if candidate.right_id == actual and actual is not None:
                auto_match_correct += 1
            else:
                wrong_auto_match += 1
        elif candidate.score >= review_threshold:
            human_review += 1
        else:
            auto_no_match += 1
            if actual is None:
                auto_no_match_correct += 1
            else:
                missed_true_match += 1

    auto_match_precision = (
        auto_match_correct / auto_match if auto_match else 1.0
    )
    human_review_rate = human_review / total
    unsafe_auto_case_rate = (wrong_auto_match + missed_true_match) / total
    safe_auto_decision_rate = (
        auto_match_correct + auto_no_match_correct
    ) / total
    review_cost_per_1000 = (
        human_review_rate
        * 1000
        * REVIEW_MINUTES
        / 60.0
        * LOADED_HUMAN_COST_PER_HOUR_USD
    )
    recoverable_match_recall = (
        (true_matches - missed_true_match) / true_matches if true_matches else 1.0
    )

    return {
        "test_cases": total,
        "true_matches": true_matches,
        "auto_match_cases": auto_match,
        "auto_match_correct": auto_match_correct,
        "wrong_auto_match_cases": wrong_auto_match,
        "human_review_cases": human_review,
        "auto_no_match_cases": auto_no_match,
        "auto_no_match_correct": auto_no_match_correct,
        "missed_true_match_cases": missed_true_match,
        "auto_match_precision": auto_match_precision,
        "human_review_rate": human_review_rate,
        "unsafe_auto_case_rate": unsafe_auto_case_rate,
        "safe_auto_decision_rate": safe_auto_decision_rate,
        "recoverable_match_recall_after_review": recoverable_match_recall,
        "illustrative_review_labor_cost_per_1000_cases_usd": review_cost_per_1000,
        "economic_assumptions": {
            "review_minutes_per_case": REVIEW_MINUTES,
            "loaded_human_cost_per_hour_usd": LOADED_HUMAN_COST_PER_HOUR_USD,
            "error_cost_not_monetized": True,
        },
    }


def run_candidate(
    name: str,
    scorer: Callable[[Dataset], dict[str, CandidateScore]],
    dataset: Dataset,
) -> dict[str, Any]:
    started = time.perf_counter()
    top = scorer(dataset)
    runtime_seconds = time.perf_counter() - started

    auto_threshold, review_threshold, validation = select_thresholds(top, dataset)
    metrics = evaluate_three_way(
        top,
        dataset,
        auto_threshold=auto_threshold,
        review_threshold=review_threshold,
    )
    return {
        "candidate": name,
        "runtime_seconds": runtime_seconds,
        "validation": validation,
        "test": metrics,
    }


def choose_synthetic_leader(results: list[dict[str, Any]]) -> dict[str, Any]:
    # This is deliberately conservative: economics only ranks candidates that
    # keep auto-match precision high and unsafe automatic decisions low.
    eligible = [
        result
        for result in results
        if result["test"]["auto_match_precision"] >= TARGET_AUTO_PRECISION
        and result["test"]["unsafe_auto_case_rate"] <= 0.02
    ]
    if not eligible:
        return {
            "status": "NO_SAFE_SYNTHETIC_WINNER",
            "reason": "No candidate met both synthetic safety constraints.",
        }

    winner = min(
        eligible,
        key=lambda result: (
            result["test"][
                "illustrative_review_labor_cost_per_1000_cases_usd"
            ],
            result["runtime_seconds"],
        ),
    )
    return {
        "status": "SYNTHETIC_ECONOMIC_LEADER",
        "candidate": winner["candidate"],
        "selection_basis": (
            "Among candidates meeting >=98% auto-match precision and <=2% "
            "unsafe automatic case rate, minimize illustrative human-review "
            "labor cost, then runtime."
        ),
        "not_a_production_selection": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("benchmarks/entity_resolution_v1/results.json"),
    )
    args = parser.parse_args()

    random.seed(SEED)
    dataset = build_dataset()

    candidates: list[
        tuple[str, Callable[[Dataset], dict[str, CandidateScore]]]
    ] = [
        ("rapidfuzz_weighted_baseline", rapidfuzz_scores),
        ("dedupe_recordlink", dedupe_scores),
        ("splink_probabilistic_linkage", splink_scores),
    ]

    results: list[dict[str, Any]] = []
    failures: list[dict[str, str]] = []

    for name, scorer in candidates:
        try:
            results.append(run_candidate(name, scorer, dataset))
        except Exception as exc:  # benchmark records failure instead of hiding it
            failures.append(
                {
                    "candidate": name,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )

    payload = {
        "benchmark_id": "ENTITY_RESOLUTION_REUSE_BENCHMARK_V1_OFFLINE",
        "synthetic_only": True,
        "contains_real_pii": False,
        "remote_source_access": False,
        "seed": SEED,
        "dataset": {
            "left_records": len(dataset.left),
            "right_records": len(dataset.right),
            "matched_entities": 160,
            "unmatched_left": 20,
            "unmatched_right": 20,
            "train_left_cases": len(dataset.train_left_ids),
            "validation_left_cases": len(dataset.validation_left_ids),
            "test_left_cases": len(dataset.test_left_ids),
        },
        "candidate_versions": {
            "splink": "4.0.17",
            "dedupe": "3.0.3",
            "btrees": "6.4",
            "rapidfuzz": "3.14.6",
            "pandas": "3.0.6",
        },
        "results": results,
        "failures": failures,
        "synthetic_leader": choose_synthetic_leader(results),
        "warnings": [
            "Synthetic results are not production accuracy evidence.",
            "Thresholds are selected only on the synthetic validation split.",
            "Error cost is intentionally not monetized without project evidence.",
            "No candidate may grant PII/source/outreach/claim authorization.",
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))

    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
