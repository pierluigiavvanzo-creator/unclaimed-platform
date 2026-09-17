#!/usr/bin/env python3
"""Bounded CA SCO MVP-1 PROPERTY_TYPE validation with metadata-only row defer.

This product-validation runner reuses the already reviewed transport/archive and
CSV projection primitives. It does not normalize or persist nonconforming
PROPERTY_TYPE values. It continues after an unclassifiable row and persists only
aggregate completeness counters plus exact authority-backed insurance codes.
Real network use remains separately approval-gated.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# When this file is invoked directly (``python scripts/<file>.py``), Python puts
# the scripts directory rather than the repository root on sys.path. Add the
# repository root explicitly so the existing ``scripts`` namespace and project
# package imports resolve identically in GitHub Actions and unit-test imports.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import ca_sco_property_type_semantic_verification as legacy
from unclaimed_platform.adapters.sources.california_property_type import (
    PropertyTypeDisposition,
    classify_property_type,
)

EXECUTION_ID = "ca.sco.unclaimed_property.bulk.500_plus.mvp1.property_type.validation"
POLICY_ID = "ROW_DEFER_CONTINUE_METADATA_ONLY"


def _process_member(
    member: legacy.CanonicalMember,
    body: bytes,
) -> tuple[dict[str, int], set[str], int]:
    compressed_prefix = legacy._parse_local_member_prefix(body, member)
    records, uncompressed_bytes = legacy._collect_first_records(compressed_prefix)
    legacy._parse_header(records[0])

    counters = {
        "rows_examined": 0,
        "nonconforming_rows_deferred": 0,
        "shape_valid_non_target_rows": 0,
        "insurance_rows": 0,
        "mvp1_primary_rows": 0,
    }
    insurance_codes: set[str] = set()

    for record in records[1:]:
        property_type, column_count = legacy._project_property_type(record)
        if column_count != len(legacy.CANONICAL_HEADER):
            raise legacy.RunnerStop("ROW_COLUMN_COUNT_MISMATCH")

        counters["rows_examined"] += 1
        classification = classify_property_type(property_type)
        if classification.disposition is PropertyTypeDisposition.DEFER_UNCLASSIFIABLE:
            counters["nonconforming_rows_deferred"] += 1
            continue
        if classification.disposition is PropertyTypeDisposition.INSURANCE:
            counters["insurance_rows"] += 1
            insurance_codes.add(property_type)
            if classification.mvp1_primary_target:
                counters["mvp1_primary_rows"] += 1
            continue
        counters["shape_valid_non_target_rows"] += 1

    if counters["rows_examined"] != legacy.MAX_ROWS_PER_MEMBER:
        raise legacy.RunnerStop("ROW_SAMPLE_INCOMPLETE_WITHIN_MEMBER_PREFIX_CAP")
    return counters, insurance_codes, uncompressed_bytes


def _base_result(execution_approval_ref: str, privacy_approval_ref: str) -> dict[str, Any]:
    result = legacy._base_result(execution_approval_ref, privacy_approval_ref)
    result["schema_version"] = "1.0.0"
    result["execution_id"] = EXECUTION_ID
    result["proposal_id"] = "ca.sco.mvp1.property_type.authority_row_defer"
    result["policy_id"] = POLICY_ID
    result["sample_summary"] = {
        "sample_rows_examined": 0,
        "rows_examined_per_member": legacy._empty_rows_by_member(),
        "nonconforming_rows_deferred_count": 0,
        "shape_valid_non_target_rows_count": 0,
        "insurance_rows_count": 0,
        "mvp1_primary_rows_count": 0,
        "distinct_insurance_codes": [],
    }
    result["control_disposition"] = None
    result["semantic_result_status"] = "STOPPED_FAIL_CLOSED"
    result["stop_reason"] = "RUNNER_INTERNAL_ERROR"
    return result


def execute(
    execution_approval_ref: str,
    privacy_approval_ref: str,
    transport: legacy.Transport,
    timeout_seconds: int = legacy.DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    legacy._require_approval_refs(execution_approval_ref, privacy_approval_ref)
    if not 1 <= timeout_seconds <= 30:
        raise ValueError("timeout_seconds must be between 1 and 30")

    result = _base_result(execution_approval_ref, privacy_approval_ref)
    total_uncompressed = 0
    insurance_codes: set[str] = set()

    try:
        result["requests_summary"]["head_requests"] = 1
        result["requests_summary"]["http_requests_total"] = 1
        head = transport.head(timeout_seconds)
        legacy._verify_head(head, result)

        for member in legacy.CANONICAL_MEMBERS:
            body = legacy._read_exact_range(transport, member, timeout_seconds, result)
            counters, member_insurance, uncompressed_bytes = _process_member(member, body)
            total_uncompressed += uncompressed_bytes
            if total_uncompressed > legacy.MAX_UNCOMPRESSED_BYTES_TOTAL:
                raise legacy.RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")

            summary = result["sample_summary"]
            summary["rows_examined_per_member"][member.name] = counters["rows_examined"]
            summary["sample_rows_examined"] += counters["rows_examined"]
            summary["nonconforming_rows_deferred_count"] += counters[
                "nonconforming_rows_deferred"
            ]
            summary["shape_valid_non_target_rows_count"] += counters[
                "shape_valid_non_target_rows"
            ]
            summary["insurance_rows_count"] += counters["insurance_rows"]
            summary["mvp1_primary_rows_count"] += counters["mvp1_primary_rows"]
            insurance_codes.update(member_insurance)

        summary = result["sample_summary"]
        if summary["sample_rows_examined"] > legacy.MAX_ROWS_TOTAL:
            raise legacy.RunnerStop("ROW_LIMIT_EXCEEDED")
        summary["distinct_insurance_codes"] = sorted(insurance_codes)

        if summary["mvp1_primary_rows_count"]:
            result["semantic_result_status"] = "MVP1_PRIMARY_IN03_OBSERVED"
        elif summary["insurance_rows_count"]:
            result["semantic_result_status"] = "INSURANCE_CODE_OBSERVED_NO_IN03"
        else:
            result["semantic_result_status"] = "NO_INSURANCE_CODE_OBSERVED_IN_BOUNDED_SAMPLE"
        result["stop_reason"] = None
        return result
    except legacy.RunnerStop as exc:
        result["sample_summary"]["distinct_insurance_codes"] = sorted(insurance_codes)
        result["semantic_result_status"] = "STOPPED_FAIL_CLOSED"
        result["stop_reason"] = exc.reason
        return result
    except Exception:
        result["sample_summary"]["distinct_insurance_codes"] = sorted(insurance_codes)
        result["semantic_result_status"] = "STOPPED_FAIL_CLOSED"
        result["stop_reason"] = "RUNNER_INTERNAL_ERROR"
        return result


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--approval-ref", required=True)
    parser.add_argument("--privacy-approval-ref", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout-seconds", type=int, default=legacy.DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--live-network", action="store_true")
    args = parser.parse_args(argv)
    if not args.live_network:
        parser.error("live network requires a separately approved one-shot execution gate")
    return args


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result = execute(
            execution_approval_ref=args.approval_ref,
            privacy_approval_ref=args.privacy_approval_ref,
            transport=legacy.HttpTransport(),
            timeout_seconds=args.timeout_seconds,
        )
    except legacy.RunnerAuthorizationError as exc:
        print(f"RUNNER_AUTHORIZATION_ERROR={type(exc).__name__}", file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = result["sample_summary"]
    print(
        "CA_SCO_MVP1_PROPERTY_TYPE_SUMMARY="
        + json.dumps(
            {
                "result_status": result["semantic_result_status"],
                "stop_reason": result["stop_reason"],
                "sample_rows_examined": summary["sample_rows_examined"],
                "nonconforming_rows_deferred_count": summary[
                    "nonconforming_rows_deferred_count"
                ],
                "insurance_rows_count": summary["insurance_rows_count"],
                "mvp1_primary_rows_count": summary["mvp1_primary_rows_count"],
                "distinct_insurance_codes": summary["distinct_insurance_codes"],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
