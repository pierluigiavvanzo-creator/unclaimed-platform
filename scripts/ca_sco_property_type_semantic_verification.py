#!/usr/bin/env python3
"""Bounded PROPERTY_TYPE semantic verification runner for CA SCO $500+ ZIP.

This module implements the canonical bounded sampling design. The execution core
accepts an injected transport so unit tests can run without network access.
A real HTTP transport is provided for a later, separately authorized execution
gate; this repository task does not invoke it and does not create a network
workflow.
"""

from __future__ import annotations

import argparse
import csv
import http.client
import io
import json
import re
import ssl
import struct
import sys
import zlib
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import urlparse

ENDPOINT = "https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip"
HOST = "claimit.ca.gov"
EXPECTED_LENGTH = 162_416_884
EXPECTED_ETAG = '"b25b315b6cd8007624387c3a00d4b1fe"'
EXPECTED_MEDIA_TYPE = "application/zip"
EXPECTED_ACCEPT_RANGES = "bytes"
DEFAULT_TIMEOUT_SECONDS = 10

RANGE_RESPONSE_BYTES = 131_072
MAX_TOTAL_RESPONSE_BYTES = 524_288
MAX_UNCOMPRESSED_BYTES_PER_MEMBER = 262_144
MAX_UNCOMPRESSED_BYTES_TOTAL = 1_048_576
MAX_LOGICAL_RECORD_BYTES = 32_768
MAX_ROWS_PER_MEMBER = 4
MAX_ROWS_TOTAL = 16
MAX_HEAD_REQUESTS = 1
MAX_RANGE_REQUESTS = 4
MAX_HTTP_REQUESTS = 5

PROPERTY_TYPE_INDEX = 1
PROPERTY_TYPE_RE = re.compile(r"^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$")
OFFICIAL_INSURANCE_CODES = frozenset(
    {"IN01", "IN02", "IN03", "IN04", "IN05", "IN06", "IN07", "IN08", "IN99"}
)
CANONICAL_HEADER = (
    "PROPERTY_ID",
    "PROPERTY_TYPE",
    "CASH_REPORTED",
    "SHARES_REPORTED",
    "NAME_OF_SECURITIES_REPORTED",
    "NO_OF_OWNERS",
    "OWNER_NAME",
    "OWNER_STREET_1",
    "OWNER_STREET_2",
    "OWNER_STREET_3",
    "OWNER_CITY",
    "OWNER_STATE",
    "OWNER_ZIP",
    "OWNER_COUNTRY_CODE",
    "CURRENT_CASH_BALANCE",
    "NUMBER_OF_PENDING_CLAIMS",
    "NUMBER_OF_PAID_CLAIMS",
    "HOLDER_NAME",
    "HOLDER_STREET_1",
    "HOLDER_STREET_2",
    "HOLDER_STREET_3",
    "HOLDER_CITY",
    "HOLDER_STATE",
    "HOLDER_ZIP",
    "CUSIP",
)


@dataclass(frozen=True)
class CanonicalMember:
    name: str
    local_header_offset: int


CANONICAL_MEMBERS = (
    CanonicalMember("From_500_To_Beyond_1_of_4.csv", 0),
    CanonicalMember("From_500_To_Beyond_2_of_4.csv", 59_747_797),
    CanonicalMember("From_500_To_Beyond_3_of_4.csv", 96_862_896),
    CanonicalMember("From_500_To_Beyond_4_of_4.csv", 134_174_190),
)


class RunnerStop(RuntimeError):
    """Deterministic fail-closed stop with a schema-approved reason code."""

    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


class RunnerAuthorizationError(ValueError):
    """Raised before transport access when required approval references are absent."""


@dataclass(frozen=True)
class HeadObservation:
    status: int
    headers: Mapping[str, str]


class RangeHandle(Protocol):
    status: int
    headers: Mapping[str, str]

    def read(self, max_bytes: int) -> bytes: ...

    def close(self) -> None: ...


class Transport(Protocol):
    def head(self, timeout_seconds: int) -> HeadObservation: ...

    def open_range(
        self,
        start: int,
        end: int,
        timeout_seconds: int,
    ) -> RangeHandle: ...


class _HttpRangeHandle:
    def __init__(
        self,
        connection: http.client.HTTPSConnection,
        response: http.client.HTTPResponse,
    ) -> None:
        self._connection = connection
        self._response = response
        self.status = response.status
        self.headers = {key.lower(): value for key, value in response.getheaders()}

    def read(self, max_bytes: int) -> bytes:
        return self._response.read(max_bytes)

    def close(self) -> None:
        self._connection.close()


class HttpTransport:
    """Exact-host HTTPS transport. http.client does not auto-follow redirects."""

    def __init__(self) -> None:
        parsed = urlparse(ENDPOINT)
        if parsed.scheme != "https" or parsed.hostname != HOST:
            raise RuntimeError("fixed endpoint identity is invalid")
        self._path = parsed.path

    def head(self, timeout_seconds: int) -> HeadObservation:
        connection = http.client.HTTPSConnection(
            HOST,
            timeout=timeout_seconds,
            context=ssl.create_default_context(),
        )
        try:
            connection.request(
                "HEAD",
                self._path,
                headers={
                    "User-Agent": "unclaimed-platform-property-type-semantic/1.0",
                    "Accept": "*/*",
                    "Connection": "close",
                },
            )
            response = connection.getresponse()
            headers = {key.lower(): value for key, value in response.getheaders()}
            return HeadObservation(status=response.status, headers=headers)
        finally:
            connection.close()

    def open_range(
        self,
        start: int,
        end: int,
        timeout_seconds: int,
    ) -> RangeHandle:
        if start < 0 or end < start or end >= EXPECTED_LENGTH:
            raise RunnerStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
        connection = http.client.HTTPSConnection(
            HOST,
            timeout=timeout_seconds,
            context=ssl.create_default_context(),
        )
        connection.request(
            "GET",
            self._path,
            headers={
                "User-Agent": "unclaimed-platform-property-type-semantic/1.0",
                "Accept": EXPECTED_MEDIA_TYPE,
                "Range": f"bytes={start}-{end}",
                "If-Match": EXPECTED_ETAG,
                "Connection": "close",
            },
        )
        response = connection.getresponse()
        return _HttpRangeHandle(connection, response)


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def _empty_rows_by_member() -> dict[str, int]:
    return {member.name: 0 for member in CANONICAL_MEMBERS}


def _base_result(
    execution_approval_ref: str,
    privacy_approval_ref: str,
) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "execution_id": "ca.sco.unclaimed_property.bulk.500_plus.property_type.semantic",
        "proposal_id": "ca.sco.segment.500_plus.property_type_semantic_verification",
        "source_id": "ca.sco.unclaimed_property.bulk",
        "source_segment_id": "ca.sco.unclaimed_property.bulk.500_plus",
        "jurisdiction": "CA",
        "execution_approval_ref": execution_approval_ref,
        "privacy_approval_ref": privacy_approval_ref,
        "executed_at": _utc_now(),
        "target": {
            "endpoint": ENDPOINT,
            "expected_content_length": EXPECTED_LENGTH,
            "expected_etag": EXPECTED_ETAG,
            "expected_media_type": EXPECTED_MEDIA_TYPE,
            "expected_accept_ranges": EXPECTED_ACCEPT_RANGES,
        },
        "controls": {
            "rows_max_per_member": MAX_ROWS_PER_MEMBER,
            "rows_max_total": MAX_ROWS_TOTAL,
            "head_requests_max": MAX_HEAD_REQUESTS,
            "range_requests_max": MAX_RANGE_REQUESTS,
            "http_requests_max_total": MAX_HTTP_REQUESTS,
            "range_response_bytes_max_each": RANGE_RESPONSE_BYTES,
            "total_source_response_body_bytes_max": MAX_TOTAL_RESPONSE_BYTES,
            "uncompressed_transient_bytes_max_each": MAX_UNCOMPRESSED_BYTES_PER_MEMBER,
            "uncompressed_transient_bytes_max_total": MAX_UNCOMPRESSED_BYTES_TOTAL,
            "logical_record_bytes_max": MAX_LOGICAL_RECORD_BYTES,
            "full_body_fallback_allowed": False,
            "additional_range_allowed": False,
        },
        "transport_verification": {
            "head_performed": False,
            "head_status": None,
            "content_length": None,
            "content_type": None,
            "accept_ranges": None,
            "etag": None,
            "last_modified": None,
        },
        "requests_summary": {
            "head_requests": 0,
            "range_requests": 0,
            "http_requests_total": 0,
            "total_body_bytes_read": 0,
        },
        "sample_summary": {
            "sample_rows_examined": 0,
            "rows_examined_per_member": _empty_rows_by_member(),
            "distinct_property_type_codes": [],
            "distinct_insurance_codes": [],
        },
        "safety_state": {
            "full_archive_downloaded": False,
            "raw_body_persisted": False,
            "temporary_source_files_created": False,
            "full_rows_persisted": False,
            "property_id_persisted": False,
            "per_row_property_type_persisted": False,
            "owner_holder_values_persisted": False,
            "identity_resolution_performed": False,
            "beneficiary_matching_performed": False,
            "outreach_performed": False,
            "production_classification_activated": False,
        },
        "semantic_result_status": "STOPPED_FAIL_CLOSED",
        "stop_reason": "RUNNER_INTERNAL_ERROR",
    }


def _require_approval_refs(
    execution_approval_ref: str,
    privacy_approval_ref: str,
) -> None:
    if not execution_approval_ref.strip():
        raise RunnerAuthorizationError("execution approval reference is required")
    if not privacy_approval_ref.strip():
        raise RunnerAuthorizationError("privacy approval reference is required")


def _header_value(headers: Mapping[str, str], name: str) -> str | None:
    target = name.casefold()
    for key, value in headers.items():
        if key.casefold() == target:
            return value
    return None


def _verify_head(
    observation: HeadObservation,
    result: dict[str, Any],
) -> None:
    headers = observation.headers
    content_length_raw = _header_value(headers, "content-length")
    content_length = (
        int(content_length_raw)
        if content_length_raw is not None and content_length_raw.isdigit()
        else None
    )
    content_type = (_header_value(headers, "content-type") or "").split(";", 1)[0]
    content_type = content_type.strip().lower() or None
    accept_ranges = _header_value(headers, "accept-ranges")
    etag = _header_value(headers, "etag")
    last_modified = _header_value(headers, "last-modified")

    result["transport_verification"] = {
        "head_performed": True,
        "head_status": observation.status,
        "content_length": content_length,
        "content_type": content_type,
        "accept_ranges": accept_ranges,
        "etag": etag,
        "last_modified": last_modified,
    }
    if (
        observation.status != 200
        or content_length != EXPECTED_LENGTH
        or content_type != EXPECTED_MEDIA_TYPE
        or (accept_ranges or "").lower() != EXPECTED_ACCEPT_RANGES
        or etag != EXPECTED_ETAG
    ):
        raise RunnerStop("TRANSPORT_METADATA_DRIFT")


def _read_exact_range(
    transport: Transport,
    member: CanonicalMember,
    timeout_seconds: int,
    result: dict[str, Any],
) -> bytes:
    requests = result["requests_summary"]
    if requests["range_requests"] >= MAX_RANGE_REQUESTS:
        raise RunnerStop("REQUEST_LIMIT_EXCEEDED")
    if requests["http_requests_total"] >= MAX_HTTP_REQUESTS:
        raise RunnerStop("REQUEST_LIMIT_EXCEEDED")

    start = member.local_header_offset
    end = start + RANGE_RESPONSE_BYTES - 1
    if end >= EXPECTED_LENGTH:
        raise RunnerStop("BYTE_BUDGET_EXCEEDED")

    handle = transport.open_range(start, end, timeout_seconds)
    requests["range_requests"] += 1
    requests["http_requests_total"] += 1
    try:
        if handle.status != 206:
            raise RunnerStop("RANGE_RESPONSE_NOT_PARTIAL")

        content_range = _header_value(handle.headers, "content-range")
        expected_content_range = f"bytes {start}-{end}/{EXPECTED_LENGTH}"
        if content_range != expected_content_range:
            raise RunnerStop("CONTENT_RANGE_MISMATCH")

        content_length_raw = _header_value(handle.headers, "content-length")
        if (
            content_length_raw is not None
            and content_length_raw.isdigit()
            and int(content_length_raw) != RANGE_RESPONSE_BYTES
        ):
            raise RunnerStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")

        body = handle.read(RANGE_RESPONSE_BYTES + 1)
        if len(body) != RANGE_RESPONSE_BYTES:
            raise RunnerStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")

        requests["total_body_bytes_read"] += len(body)
        if requests["total_body_bytes_read"] > MAX_TOTAL_RESPONSE_BYTES:
            raise RunnerStop("BYTE_BUDGET_EXCEEDED")
        return body
    finally:
        handle.close()


def _parse_local_member_prefix(
    body: bytes,
    expected_member: CanonicalMember,
) -> bytes:
    if len(body) < 30 or body[:4] != b"PK\x03\x04":
        raise RunnerStop("CANONICAL_MEMBER_METADATA_MISMATCH")
    try:
        (
            _signature,
            _version_needed,
            flags,
            compression,
            _mtime,
            _mdate,
            _crc,
            _compressed_size,
            _uncompressed_size,
            filename_len,
            extra_len,
        ) = struct.unpack_from("<4s5H3I2H", body, 0)
    except struct.error as exc:
        raise RunnerStop("CANONICAL_MEMBER_METADATA_MISMATCH") from exc

    if flags & 0x0001 or compression != 8:
        raise RunnerStop("CANONICAL_MEMBER_METADATA_MISMATCH")

    name_start = 30
    name_end = name_start + filename_len
    data_start = name_end + extra_len
    if data_start >= len(body) or name_end > len(body):
        raise RunnerStop("CANONICAL_MEMBER_METADATA_MISMATCH")
    try:
        name = body[name_start:name_end].decode(
            "utf-8" if flags & 0x0800 else "cp437",
            errors="strict",
        )
    except UnicodeDecodeError as exc:
        raise RunnerStop("CANONICAL_MEMBER_METADATA_MISMATCH") from exc
    if name != expected_member.name:
        raise RunnerStop("CANONICAL_MEMBER_METADATA_MISMATCH")
    return body[data_start:]


class _RecordCollector:
    def __init__(self, target_records: int) -> None:
        self.target_records = target_records
        self.records: list[bytes] = []
        self.current = bytearray()
        self.in_quotes = False
        self.quote_pending = False
        self.total_uncompressed = 0

    @property
    def complete(self) -> bool:
        return len(self.records) >= self.target_records

    def feed(self, chunk: bytes) -> None:
        for value in chunk:
            if self.complete:
                return
            self.total_uncompressed += 1
            if self.total_uncompressed > MAX_UNCOMPRESSED_BYTES_PER_MEMBER:
                raise RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")
            self.current.append(value)
            if len(self.current) > MAX_LOGICAL_RECORD_BYTES:
                raise RunnerStop("LOGICAL_RECORD_LIMIT_EXCEEDED")

            if self.quote_pending:
                if value == 0x22:
                    self.quote_pending = False
                    continue
                self.in_quotes = False
                self.quote_pending = False

            if value == 0x22:
                if self.in_quotes:
                    self.quote_pending = True
                else:
                    self.in_quotes = True
                continue

            if value == 0x0A and not self.in_quotes:
                self.records.append(bytes(self.current))
                self.current.clear()


def _collect_first_records(compressed_prefix: bytes) -> tuple[list[bytes], int]:
    collector = _RecordCollector(target_records=1 + MAX_ROWS_PER_MEMBER)
    decompressor = zlib.decompressobj(-15)
    pos = 0
    try:
        while pos < len(compressed_prefix) and not collector.complete:
            chunk = compressed_prefix[pos : pos + 4096]
            pos += len(chunk)
            remaining = MAX_UNCOMPRESSED_BYTES_PER_MEMBER - collector.total_uncompressed
            output = decompressor.decompress(chunk, max_length=remaining + 1)
            if len(output) > remaining:
                raise RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")
            collector.feed(output)
            while decompressor.unconsumed_tail and not collector.complete:
                remaining = (
                    MAX_UNCOMPRESSED_BYTES_PER_MEMBER - collector.total_uncompressed
                )
                output = decompressor.decompress(
                    decompressor.unconsumed_tail,
                    max_length=remaining + 1,
                )
                if len(output) > remaining:
                    raise RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")
                if not output and decompressor.unconsumed_tail:
                    raise RunnerStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
                collector.feed(output)
    except zlib.error as exc:
        raise RunnerStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR") from exc

    if not collector.complete:
        raise RunnerStop("ROW_SAMPLE_INCOMPLETE_WITHIN_MEMBER_PREFIX_CAP")
    return collector.records, collector.total_uncompressed


def _parse_header(record: bytes) -> None:
    try:
        text = record.decode("utf-8-sig", errors="strict")
        rows = list(csv.reader(io.StringIO(text, newline=""), strict=True))
    except (UnicodeDecodeError, csv.Error) as exc:
        raise RunnerStop("HEADER_MISMATCH") from exc
    if len(rows) != 1 or tuple(rows[0]) != CANONICAL_HEADER:
        raise RunnerStop("HEADER_MISMATCH")


def _strip_record_terminator(record: bytes) -> bytes:
    if record.endswith(b"\r\n"):
        return record[:-2]
    if record.endswith(b"\n"):
        return record[:-1]
    return record


def _project_property_type(record: bytes) -> tuple[str, int]:
    data = _strip_record_terminator(record)
    field_index = 0
    capture = bytearray()
    in_quotes = False
    after_quote = False
    at_field_start = True
    index = 0

    while index < len(data):
        value = data[index]
        if in_quotes:
            if value == 0x22:
                if index + 1 < len(data) and data[index + 1] == 0x22:
                    if field_index == PROPERTY_TYPE_INDEX:
                        capture.append(0x22)
                    index += 2
                    continue
                in_quotes = False
                after_quote = True
                index += 1
                continue
            if field_index == PROPERTY_TYPE_INDEX:
                capture.append(value)
            index += 1
            continue

        if after_quote:
            if value == 0x2C:
                field_index += 1
                at_field_start = True
                after_quote = False
                index += 1
                continue
            raise RunnerStop("CSV_PARSE_ERROR")

        if at_field_start and value == 0x22:
            in_quotes = True
            at_field_start = False
            index += 1
            continue
        if value == 0x22:
            raise RunnerStop("CSV_PARSE_ERROR")
        if value == 0x2C:
            field_index += 1
            at_field_start = True
            index += 1
            continue
        if field_index == PROPERTY_TYPE_INDEX:
            capture.append(value)
        at_field_start = False
        index += 1

    if in_quotes:
        raise RunnerStop("CSV_PARSE_ERROR")
    column_count = field_index + 1
    try:
        property_type = bytes(capture).decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise RunnerStop("PROPERTY_TYPE_FORMAT_UNEXPECTED") from exc
    return property_type, column_count


def _process_member(
    member: CanonicalMember,
    body: bytes,
) -> tuple[list[str], int]:
    compressed_prefix = _parse_local_member_prefix(body, member)
    records, uncompressed_bytes = _collect_first_records(compressed_prefix)
    _parse_header(records[0])

    property_types: list[str] = []
    for record in records[1:]:
        property_type, column_count = _project_property_type(record)
        if column_count != len(CANONICAL_HEADER):
            raise RunnerStop("ROW_COLUMN_COUNT_MISMATCH")
        if property_type == "":
            raise RunnerStop("PROPERTY_TYPE_EMPTY")
        if PROPERTY_TYPE_RE.fullmatch(property_type) is None:
            raise RunnerStop("PROPERTY_TYPE_FORMAT_UNEXPECTED")
        if property_type.startswith("IN") and property_type not in OFFICIAL_INSURANCE_CODES:
            raise RunnerStop("UNRECOGNIZED_INSURANCE_PREFIX_CODE")
        property_types.append(property_type)

    if len(property_types) != MAX_ROWS_PER_MEMBER:
        raise RunnerStop("ROW_SAMPLE_INCOMPLETE_WITHIN_MEMBER_PREFIX_CAP")
    return property_types, uncompressed_bytes


def execute(
    execution_approval_ref: str,
    privacy_approval_ref: str,
    transport: Transport,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    """Run one bounded semantic sample using the supplied transport."""
    _require_approval_refs(execution_approval_ref, privacy_approval_ref)
    if not 1 <= timeout_seconds <= 30:
        raise ValueError("timeout_seconds must be between 1 and 30")

    result = _base_result(execution_approval_ref, privacy_approval_ref)
    distinct_codes: set[str] = set()
    distinct_insurance: set[str] = set()
    total_uncompressed = 0

    try:
        result["requests_summary"]["head_requests"] = 1
        result["requests_summary"]["http_requests_total"] = 1
        if result["requests_summary"]["head_requests"] > MAX_HEAD_REQUESTS:
            raise RunnerStop("REQUEST_LIMIT_EXCEEDED")
        head = transport.head(timeout_seconds)
        _verify_head(head, result)

        for member in CANONICAL_MEMBERS:
            body = _read_exact_range(transport, member, timeout_seconds, result)
            property_types, uncompressed_bytes = _process_member(member, body)
            total_uncompressed += uncompressed_bytes
            if total_uncompressed > MAX_UNCOMPRESSED_BYTES_TOTAL:
                raise RunnerStop("UNCOMPRESSED_TRANSIENT_LIMIT_EXCEEDED")

            rows_count = len(property_types)
            rows = result["sample_summary"]["rows_examined_per_member"]
            rows[member.name] = rows_count
            result["sample_summary"]["sample_rows_examined"] += rows_count
            if result["sample_summary"]["sample_rows_examined"] > MAX_ROWS_TOTAL:
                raise RunnerStop("ROW_LIMIT_EXCEEDED")

            distinct_codes.update(property_types)
            distinct_insurance.update(
                code for code in property_types if code in OFFICIAL_INSURANCE_CODES
            )

        result["sample_summary"]["distinct_property_type_codes"] = sorted(distinct_codes)
        result["sample_summary"]["distinct_insurance_codes"] = sorted(distinct_insurance)
        if distinct_insurance:
            result["semantic_result_status"] = "SAMPLE_COMPATIBLE_INSURANCE_CODE_OBSERVED"
        else:
            result["semantic_result_status"] = (
                "SAMPLE_CODE_SHAPE_COMPATIBLE_NO_INSURANCE_CODE_OBSERVED"
            )
        result["stop_reason"] = None
        return result
    except RunnerStop as exc:
        result["sample_summary"]["distinct_property_type_codes"] = sorted(distinct_codes)
        result["sample_summary"]["distinct_insurance_codes"] = sorted(distinct_insurance)
        result["semantic_result_status"] = "STOPPED_FAIL_CLOSED"
        result["stop_reason"] = exc.reason
        return result
    except Exception:
        result["sample_summary"]["distinct_property_type_codes"] = sorted(distinct_codes)
        result["sample_summary"]["distinct_insurance_codes"] = sorted(distinct_insurance)
        result["semantic_result_status"] = "STOPPED_FAIL_CLOSED"
        result["stop_reason"] = "RUNNER_INTERNAL_ERROR"
        return result


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--approval-ref", required=True)
    parser.add_argument("--privacy-approval-ref", required=True)
    parser.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--live-network",
        action="store_true",
        help=(
            "Use the real fixed CA SCO endpoint. This flag does not itself grant "
            "project execution/privacy approval."
        ),
    )
    args = parser.parse_args(argv)
    if not 1 <= args.timeout_seconds <= 30:
        parser.error("--timeout-seconds must be between 1 and 30")
    if not args.live_network:
        parser.error(
            "no synthetic CLI transport is configured; live network remains a later "
            "separately approved gate"
        )
    return args


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result = execute(
            execution_approval_ref=args.approval_ref,
            privacy_approval_ref=args.privacy_approval_ref,
            transport=HttpTransport(),
            timeout_seconds=args.timeout_seconds,
        )
    except RunnerAuthorizationError as exc:
        print(f"RUNNER_AUTHORIZATION_ERROR={type(exc).__name__}", file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = {
        "result_status": result["semantic_result_status"],
        "stop_reason": result["stop_reason"],
        "request_count": result["requests_summary"]["http_requests_total"],
        "body_bytes_read": result["requests_summary"]["total_body_bytes_read"],
        "sample_rows_examined": result["sample_summary"]["sample_rows_examined"],
        "rows_examined_per_member": result["sample_summary"]["rows_examined_per_member"],
        "distinct_property_type_codes": result["sample_summary"][
            "distinct_property_type_codes"
        ],
        "distinct_insurance_codes": result["sample_summary"][
            "distinct_insurance_codes"
        ],
    }
    print(
        "PROPERTY_TYPE_SEMANTIC_SUMMARY="
        + json.dumps(summary, sort_keys=True, separators=(",", ":"))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
