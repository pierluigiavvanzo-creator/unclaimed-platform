#!/usr/bin/env python3
"""Deeper CA SCO insurance discovery using the already bounded Range prefixes.

The validator preserves the adopted network envelope (one HEAD plus four
131072-byte Range GETs) and the D-010 metadata-only defer policy. It increases
only the number of complete logical CSV rows inspected from those same bytes.
Real network use remains separately approval-gated.
"""

from __future__ import annotations

import argparse
import json
import sys
import zlib
from pathlib import Path
from typing import Any

from scripts import ca_sco_property_type_semantic_verification as legacy
from unclaimed_platform.adapters.sources.california_property_type import (
    PropertyTypeDisposition,
    classify_property_type,
)

EXECUTION_ID = (
    "ca.sco.unclaimed_property.bulk.500_plus.mvp1.property_type."
    "same_bytes_deeper_insurance_discovery"
)
POLICY_ID = "ROW_DEFER_CONTINUE_METADATA_ONLY"
SCAN_MODE = "SAME_BYTES_DEEPER_LOGICAL_ROWS"
MAX_DEEP_ROWS_PER_MEMBER = 256
MAX_DEEP_ROWS_TOTAL = MAX_DEEP_ROWS_PER_MEMBER * len(legacy.CANONICAL_MEMBERS)

ROW_CAP_REACHED = "ROW_CAP_REACHED"
PREFIX_EXHAUSTED_BEFORE_ROW_CAP = "PREFIX_EXHAUSTED_BEFORE_ROW_CAP"


def _collect_complete_records(
    compressed_prefix: bytes,
) -> tuple[list[bytes], int, bool]:
    """Collect complete logical records without reading beyond the prefix.

    A partial trailing logical record is intentionally ignored. The existing
    uncompressed-byte and logical-record-byte caps remain authoritative.
    """

    collector = legacy._RecordCollector(target_records=1 + MAX_DEEP_ROWS_PER_MEMBER)
    decompressor = zlib.decompressobj(-15)
    pos = 0

    try:
        while pos < len(compressed_prefix) and not collector.complete:
            chunk = compressed_prefix[pos : pos + 4096]
            pos += len(chunk)
            remaining = (
                legacy.MAX_UNCOMPRESSED_BYTES_PER_MEMBER - collector.total_uncompressed
            )
            output = decompressor.decompress(chunk, max_length=remaining + 1)
            if len(output) > remaining:
                raise legacy.RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")
            collector.feed(output)

            while decompressor.unconsumed_tail and not collector.complete:
                remaining = (
                    legacy.MAX_UNCOMPRESSED_BYTES_PER_MEMBER
                    - collector.total_uncompressed
                )
                output = decompressor.decompress(
                    decompressor.unconsumed_tail,
                    max_length=remaining + 1,
                )
                if len(output) > remaining:
                    raise legacy.RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")
                if not output and decompressor.unconsumed_tail:
                    raise legacy.RunnerStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
                collector.feed(output)
    except zlib.error as exc:
        raise legacy.RunnerStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR") from exc

    if not collector.records:
        raise legacy.RunnerStop("HEADER_MISMATCH")
    if len(collector.records) == 1:
        raise legacy.RunnerStop("NO_COMPLETE_DATA_ROWS_WITHIN_MEMBER_PREFIX")

    return collector.records, collector.total_uncompressed, collector.complete


def _process_member(
    member: legacy.CanonicalMember,
    body: bytes,
) -> tuple[dict[str, int], set[str], int, str]:
    compressed_prefix = legacy._parse_local_member_prefix(body, member)
    records, uncompressed_bytes, row_cap_reached = _collect_complete_records(
        compressed_prefix
    )
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

    if counters["rows_examined"] > MAX_DEEP_ROWS_PER_MEMBER:
        raise legacy.RunnerStop("ROW_LIMIT_EXCEEDED")

    scan_status = (
        ROW_CAP_REACHED if row_cap_reached else PREFIX_EXHAUSTED_BEFORE_ROW_CAP
    )
    return counters, insurance_codes, uncompressed_bytes, scan_status


def _base_result(
    execution_approval_ref: str,
    privacy_approval_ref: str,
) -> dict[str, Any]:
    result = legacy._base_result(execution_approval_ref, privacy_approval_ref)
    result["schema_version"] = "1.1.0"
    result["execution_id"] = EXECUTION_ID
    result["proposal_id"] = "ca.sco.mvp1.property_type.same_bytes_deeper_discovery"
    result["policy_id"] = POLICY_ID
    result["scan_mode"] = SCAN_MODE
    result["controls"]["rows_max_per_member"] = MAX_DEEP_ROWS_PER_MEMBER
    result["controls"]["rows_max_total"] = MAX_DEEP_ROWS_TOTAL
    result["controls"]["source_response_byte_budget_unchanged"] = True
    result["sample_summary"] = {
        "sample_rows_examined": 0,
        "rows_examined_per_member": legacy._empty_rows_by_member(),
        "scan_status_per_member": {
            member.name: None for member in legacy.CANONICAL_MEMBERS
        },
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
    """Run the deeper same-byte discovery scan using the supplied transport."""

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
            counters, member_insurance, uncompressed_bytes, scan_status = (
                _process_member(member, body)
            )
            total_uncompressed += uncompressed_bytes
            if total_uncompressed > legacy.MAX_UNCOMPRESSED_BYTES_TOTAL:
                raise legacy.RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")

            summary = result["sample_summary"]
            summary["rows_examined_per_member"][member.name] = counters["rows_examined"]
            summary["scan_status_per_member"][member.name] = scan_status
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
        if summary["sample_rows_examined"] > MAX_DEEP_ROWS_TOTAL:
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
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = result["sample_summary"]
    print(
        "CA_SCO_MVP1_SAME_BYTES_DEEPER_DISCOVERY_SUMMARY="
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
