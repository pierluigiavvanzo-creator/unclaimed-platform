#!/usr/bin/env python3
"""One-shot bounded CA SCO ZIP transport/archive-layout structural revalidation.

This verifier is intentionally structural-only. It observes transport metadata and
classic-ZIP EOCD / central-directory metadata. It never decompresses member payloads,
parses CSV, inspects records, or persists raw Range bytes.
"""

from __future__ import annotations

import argparse
import http.client
import json
import re
import ssl
import struct
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import urlparse

ENDPOINT = "https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip"
HOST = "claimit.ca.gov"
EXPECTED_MEDIA_TYPE = "application/zip"
EXPECTED_ACCEPT_RANGES = "bytes"
DEFAULT_TIMEOUT_SECONDS = 10

MAX_HEAD_REQUESTS = 1
MAX_RANGE_REQUESTS = 4
MAX_HTTP_REQUESTS = 5
MAX_RANGE_RESPONSE_BYTES = 131_072
MAX_TOTAL_SOURCE_BODY_BYTES = 524_288

EXECUTION_APPROVAL_REF = (
    "OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_"
    "EXECUTION_BOUNDED_B8F703DB"
)
STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF = (
    "OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_"
    "BOUNDED_B8F703DB"
)

CANONICAL_MEMBERS = (
    "From_500_To_Beyond_1_of_4.csv",
    "From_500_To_Beyond_2_of_4.csv",
    "From_500_To_Beyond_3_of_4.csv",
    "From_500_To_Beyond_4_of_4.csv",
)

EOCD_SIGNATURE = b"PK\x05\x06"
EOCD_STRUCT = struct.Struct("<4s4H2IH")
ZIP64_LOCATOR_SIGNATURE = b"PK\x06\x07"
CENTRAL_DIRECTORY_SIGNATURE = b"PK\x01\x02"
CENTRAL_DIRECTORY_STRUCT = struct.Struct("<4s6H3I5H2I")

STOP_REQUEST_OR_BYTE_CAP_EXCEEDED = "REQUEST_OR_BYTE_CAP_EXCEEDED"
STOP_EOCD_NOT_FOUND_OR_AMBIGUOUS = "EOCD_NOT_FOUND_OR_AMBIGUOUS"
STOP_ZIP64_DETECTED = "ZIP64_DETECTED"
STOP_MULTI_DISK_DETECTED = "MULTI_DISK_DETECTED"
STOP_ETAG_OR_LENGTH_OBJECT_DRIFT = "ETAG_OR_LENGTH_OBJECT_DRIFT"
STOP_CANONICAL_MEMBER_MISSING_OR_DUPLICATE = "CANONICAL_MEMBER_MISSING_OR_DUPLICATE"
STOP_LAYOUT_AMBIGUITY = "LAYOUT_AMBIGUITY_OR_UNRESOLVABLE_WITHIN_CAPS"

RESULT_CANDIDATE = "CANDIDATE_BASELINE_ESTABLISHED"
RESULT_STOPPED = "STOPPED_FAIL_CLOSED"
MATCH_ALL_UNIQUE = "ALL_CANONICAL_MEMBERS_UNIQUE"
MATCH_NOT_ESTABLISHED = "NOT_ESTABLISHED"


class RevalidationStop(RuntimeError):
    """Deterministic fail-closed stop carrying an approved reason code."""

    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


class RevalidationAuthorizationError(ValueError):
    """Raised before transport access when approval references are not exact."""


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
        etag: str,
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
    """Exact-host HTTPS transport with no redirect-following layer."""

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
                    "User-Agent": "unclaimed-platform-zip-structure-revalidation/1.0",
                    "Accept": "*/*",
                    "Connection": "close",
                },
            )
            response = connection.getresponse()
            return HeadObservation(
                status=response.status,
                headers={key.lower(): value for key, value in response.getheaders()},
            )
        finally:
            connection.close()

    def open_range(
        self,
        start: int,
        end: int,
        etag: str,
        timeout_seconds: int,
    ) -> RangeHandle:
        if start < 0 or end < start:
            raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
        connection = http.client.HTTPSConnection(
            HOST,
            timeout=timeout_seconds,
            context=ssl.create_default_context(),
        )
        connection.request(
            "GET",
            self._path,
            headers={
                "User-Agent": "unclaimed-platform-zip-structure-revalidation/1.0",
                "Accept": EXPECTED_MEDIA_TYPE,
                "Range": f"bytes={start}-{end}",
                "If-Match": etag,
                "Connection": "close",
            },
        )
        return _HttpRangeHandle(connection, connection.getresponse())


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def _header_value(headers: Mapping[str, str], name: str) -> str | None:
    target = name.casefold()
    for key, value in headers.items():
        if key.casefold() == target:
            return value
    return None


def _base_evidence() -> dict[str, Any]:
    return {
        "OBSERVED_CONTENT_LENGTH": None,
        "OBSERVED_ETAG": None,
        "OBSERVED_CONTENT_TYPE": None,
        "OBSERVED_ACCEPT_RANGES": None,
        "OBSERVED_LAST_MODIFIED": None,
        "OBSERVED_AT": _utc_now(),
        "CANONICAL_MEMBER_NAMES": list(CANONICAL_MEMBERS),
        "CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS": {
            name: None for name in CANONICAL_MEMBERS
        },
        "CANONICAL_MEMBER_MATCH_STATUS": MATCH_NOT_ESTABLISHED,
        "ADDITIONAL_MEMBER_COUNT": None,
        "REVALIDATION_RESULT_STATUS": RESULT_STOPPED,
        "STOP_REASON": STOP_LAYOUT_AMBIGUITY,
    }


def _require_approval_refs(
    execution_approval_ref: str,
    structural_byte_privacy_approval_ref: str,
) -> None:
    if execution_approval_ref != EXECUTION_APPROVAL_REF:
        raise RevalidationAuthorizationError("execution approval reference is not authorized")
    if structural_byte_privacy_approval_ref != STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF:
        raise RevalidationAuthorizationError(
            "structural-byte privacy approval reference is not authorized"
        )


def _observe_head(
    observation: HeadObservation,
    evidence: dict[str, Any],
) -> tuple[int, str]:
    content_length_raw = _header_value(observation.headers, "content-length")
    content_length = (
        int(content_length_raw)
        if content_length_raw is not None and content_length_raw.isdigit()
        else None
    )
    content_type = (_header_value(observation.headers, "content-type") or "").split(
        ";", 1
    )[0]
    content_type = content_type.strip().lower() or None
    accept_ranges = _header_value(observation.headers, "accept-ranges")
    etag = _header_value(observation.headers, "etag")
    last_modified = _header_value(observation.headers, "last-modified")

    evidence["OBSERVED_CONTENT_LENGTH"] = content_length
    evidence["OBSERVED_ETAG"] = etag
    evidence["OBSERVED_CONTENT_TYPE"] = content_type
    evidence["OBSERVED_ACCEPT_RANGES"] = accept_ranges
    evidence["OBSERVED_LAST_MODIFIED"] = last_modified

    if (
        observation.status != 200
        or content_length is None
        or content_length <= EOCD_STRUCT.size
        or etag is None
        or not etag.strip()
        or content_type != EXPECTED_MEDIA_TYPE
        or (accept_ranges or "").lower() != EXPECTED_ACCEPT_RANGES
    ):
        raise RevalidationStop(STOP_ETAG_OR_LENGTH_OBJECT_DRIFT)
    return content_length, etag


def _parse_content_range(value: str | None) -> tuple[int, int, int] | None:
    if value is None:
        return None
    match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)", value.strip())
    if match is None:
        return None
    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )


def _read_range(
    transport: Transport,
    start: int,
    end: int,
    observed_length: int,
    observed_etag: str,
    timeout_seconds: int,
    counters: dict[str, int],
) -> bytes:
    expected_size = end - start + 1
    if (
        start < 0
        or end < start
        or end >= observed_length
        or expected_size > MAX_RANGE_RESPONSE_BYTES
    ):
        raise RevalidationStop(STOP_REQUEST_OR_BYTE_CAP_EXCEEDED)
    if (
        counters["range_requests"] >= MAX_RANGE_REQUESTS
        or counters["http_requests_total"] >= MAX_HTTP_REQUESTS
    ):
        raise RevalidationStop(STOP_REQUEST_OR_BYTE_CAP_EXCEEDED)
    if counters["total_body_bytes"] + expected_size > MAX_TOTAL_SOURCE_BODY_BYTES:
        raise RevalidationStop(STOP_REQUEST_OR_BYTE_CAP_EXCEEDED)

    handle = transport.open_range(
        start,
        end,
        observed_etag,
        timeout_seconds,
    )
    counters["range_requests"] += 1
    counters["http_requests_total"] += 1
    try:
        if handle.status != 206:
            raise RevalidationStop(STOP_ETAG_OR_LENGTH_OBJECT_DRIFT)
        response_etag = _header_value(handle.headers, "etag")
        if response_etag != observed_etag:
            raise RevalidationStop(STOP_ETAG_OR_LENGTH_OBJECT_DRIFT)
        parsed_range = _parse_content_range(_header_value(handle.headers, "content-range"))
        if parsed_range != (start, end, observed_length):
            raise RevalidationStop(STOP_ETAG_OR_LENGTH_OBJECT_DRIFT)
        content_length_raw = _header_value(handle.headers, "content-length")
        if (
            content_length_raw is not None
            and (
                not content_length_raw.isdigit()
                or int(content_length_raw) != expected_size
            )
        ):
            raise RevalidationStop(STOP_ETAG_OR_LENGTH_OBJECT_DRIFT)

        body = handle.read(expected_size + 1)
        if len(body) != expected_size:
            raise RevalidationStop(STOP_ETAG_OR_LENGTH_OBJECT_DRIFT)
        counters["total_body_bytes"] += len(body)
        if counters["total_body_bytes"] > MAX_TOTAL_SOURCE_BODY_BYTES:
            raise RevalidationStop(STOP_REQUEST_OR_BYTE_CAP_EXCEEDED)
        return body
    finally:
        handle.close()


@dataclass(frozen=True)
class EocdMetadata:
    absolute_offset: int
    total_entries: int
    central_directory_size: int
    central_directory_offset: int


def _find_eocd(tail: bytes, tail_start: int) -> EocdMetadata:
    candidates: list[tuple[int, tuple[Any, ...]]] = []
    position = 0
    while True:
        position = tail.find(EOCD_SIGNATURE, position)
        if position < 0:
            break
        if position + EOCD_STRUCT.size <= len(tail):
            values = EOCD_STRUCT.unpack_from(tail, position)
            comment_length = values[-1]
            if position + EOCD_STRUCT.size + comment_length == len(tail):
                candidates.append((position, values))
        position += 1

    if len(candidates) != 1:
        raise RevalidationStop(STOP_EOCD_NOT_FOUND_OR_AMBIGUOUS)

    position, values = candidates[0]
    (
        _signature,
        disk_number,
        central_directory_disk,
        entries_on_disk,
        total_entries,
        central_directory_size,
        central_directory_offset,
        _comment_length,
    ) = values

    if (
        total_entries == 0xFFFF
        or entries_on_disk == 0xFFFF
        or central_directory_size == 0xFFFFFFFF
        or central_directory_offset == 0xFFFFFFFF
    ):
        raise RevalidationStop(STOP_ZIP64_DETECTED)

    if position >= 20 and tail[position - 20 : position - 16] == ZIP64_LOCATOR_SIGNATURE:
        raise RevalidationStop(STOP_ZIP64_DETECTED)
    if (
        disk_number != 0
        or central_directory_disk != 0
        or entries_on_disk != total_entries
    ):
        raise RevalidationStop(STOP_MULTI_DISK_DETECTED)

    absolute_offset = tail_start + position
    if (
        central_directory_size <= 0
        or central_directory_offset < 0
        or central_directory_offset + central_directory_size != absolute_offset
    ):
        raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)

    return EocdMetadata(
        absolute_offset=absolute_offset,
        total_entries=total_entries,
        central_directory_size=central_directory_size,
        central_directory_offset=central_directory_offset,
    )


def _contains_zip64_extra(extra: bytes) -> bool:
    position = 0
    while position < len(extra):
        if position + 4 > len(extra):
            raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
        header_id, data_size = struct.unpack_from("<HH", extra, position)
        position += 4
        if position + data_size > len(extra):
            raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
        if header_id == 0x0001:
            return True
        position += data_size
    return False


def _read_central_directory(
    transport: Transport,
    metadata: EocdMetadata,
    tail: bytes,
    tail_start: int,
    observed_length: int,
    observed_etag: str,
    timeout_seconds: int,
    counters: dict[str, int],
) -> bytes:
    cd_start = metadata.central_directory_offset
    cd_end = cd_start + metadata.central_directory_size
    if cd_start < 0 or cd_end > metadata.absolute_offset or cd_end > observed_length:
        raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)

    tail_end = tail_start + len(tail)
    if cd_start >= tail_start and cd_end <= tail_end:
        return tail[cd_start - tail_start : cd_end - tail_start]

    prefix_end = min(cd_end, tail_start)
    chunks: list[bytes] = []
    cursor = cd_start
    while cursor < prefix_end:
        end = min(prefix_end - 1, cursor + MAX_RANGE_RESPONSE_BYTES - 1)
        chunks.append(
            _read_range(
                transport,
                cursor,
                end,
                observed_length,
                observed_etag,
                timeout_seconds,
                counters,
            )
        )
        cursor = end + 1

    if cursor < prefix_end:
        raise RevalidationStop(STOP_REQUEST_OR_BYTE_CAP_EXCEEDED)

    if cd_end > tail_start:
        suffix_start = max(cd_start, tail_start)
        suffix_end = cd_end
        if suffix_start < tail_start or suffix_end > tail_end:
            raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
        chunks.append(tail[suffix_start - tail_start : suffix_end - tail_start])

    data = b"".join(chunks)
    if len(data) != metadata.central_directory_size:
        raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
    return data


def _parse_central_directory(
    data: bytes,
    metadata: EocdMetadata,
    observed_length: int,
) -> tuple[dict[str, int], int]:
    canonical_counts = {name: 0 for name in CANONICAL_MEMBERS}
    canonical_offsets: dict[str, int] = {}
    position = 0
    entries_seen = 0

    while position < len(data):
        if position + CENTRAL_DIRECTORY_STRUCT.size > len(data):
            raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
        values = CENTRAL_DIRECTORY_STRUCT.unpack_from(data, position)
        (
            signature,
            _version_made_by,
            _version_needed,
            _flags,
            _compression,
            _mtime,
            _mdate,
            _crc32,
            compressed_size,
            uncompressed_size,
            filename_length,
            extra_length,
            comment_length,
            disk_start,
            _internal_attributes,
            _external_attributes,
            local_header_offset,
        ) = values
        if signature != CENTRAL_DIRECTORY_SIGNATURE:
            raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
        if (
            compressed_size == 0xFFFFFFFF
            or uncompressed_size == 0xFFFFFFFF
            or local_header_offset == 0xFFFFFFFF
            or disk_start == 0xFFFF
        ):
            raise RevalidationStop(STOP_ZIP64_DETECTED)
        if disk_start != 0:
            raise RevalidationStop(STOP_MULTI_DISK_DETECTED)

        variable_start = position + CENTRAL_DIRECTORY_STRUCT.size
        name_end = variable_start + filename_length
        extra_end = name_end + extra_length
        entry_end = extra_end + comment_length
        if entry_end > len(data):
            raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)

        raw_name = data[variable_start:name_end]
        extra = data[name_end:extra_end]
        if _contains_zip64_extra(extra):
            raise RevalidationStop(STOP_ZIP64_DETECTED)
        entries_seen += 1
        canonical_name = next(
            (
                name
                for name in CANONICAL_MEMBERS
                if raw_name == name.encode("ascii")
            ),
            None,
        )
        if canonical_name is not None:
            canonical_counts[canonical_name] += 1
            if local_header_offset >= observed_length:
                raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
            canonical_offsets[canonical_name] = local_header_offset

        position = entry_end

    if position != len(data) or entries_seen != metadata.total_entries:
        raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
    if any(count != 1 for count in canonical_counts.values()):
        raise RevalidationStop(STOP_CANONICAL_MEMBER_MISSING_OR_DUPLICATE)

    additional_member_count = entries_seen - len(CANONICAL_MEMBERS)
    if additional_member_count < 0:
        raise RevalidationStop(STOP_LAYOUT_AMBIGUITY)
    return canonical_offsets, additional_member_count


def execute(
    execution_approval_ref: str,
    structural_byte_privacy_approval_ref: str,
    transport: Transport,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    """Perform one bounded structural revalidation using the supplied transport."""
    _require_approval_refs(
        execution_approval_ref,
        structural_byte_privacy_approval_ref,
    )
    if not 1 <= timeout_seconds <= 30:
        raise ValueError("timeout_seconds must be between 1 and 30")

    evidence = _base_evidence()
    counters = {
        "head_requests": 0,
        "range_requests": 0,
        "http_requests_total": 0,
        "total_body_bytes": 0,
    }

    try:
        if counters["head_requests"] >= MAX_HEAD_REQUESTS:
            raise RevalidationStop(STOP_REQUEST_OR_BYTE_CAP_EXCEEDED)
        counters["head_requests"] += 1
        counters["http_requests_total"] += 1
        head = transport.head(timeout_seconds)
        observed_length, observed_etag = _observe_head(head, evidence)

        tail_size = min(observed_length, MAX_RANGE_RESPONSE_BYTES)
        tail_start = observed_length - tail_size
        tail = _read_range(
            transport,
            tail_start,
            observed_length - 1,
            observed_length,
            observed_etag,
            timeout_seconds,
            counters,
        )
        metadata = _find_eocd(tail, tail_start)
        central_directory = _read_central_directory(
            transport,
            metadata,
            tail,
            tail_start,
            observed_length,
            observed_etag,
            timeout_seconds,
            counters,
        )
        offsets, additional_count = _parse_central_directory(
            central_directory,
            metadata,
            observed_length,
        )
        evidence["CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS"] = {
            name: offsets[name] for name in CANONICAL_MEMBERS
        }
        evidence["CANONICAL_MEMBER_MATCH_STATUS"] = MATCH_ALL_UNIQUE
        evidence["ADDITIONAL_MEMBER_COUNT"] = additional_count
        evidence["REVALIDATION_RESULT_STATUS"] = RESULT_CANDIDATE
        evidence["STOP_REASON"] = None
        return evidence
    except RevalidationStop as exc:
        evidence["REVALIDATION_RESULT_STATUS"] = RESULT_STOPPED
        evidence["STOP_REASON"] = exc.reason
        return evidence
    except Exception:
        evidence["REVALIDATION_RESULT_STATUS"] = RESULT_STOPPED
        evidence["STOP_REASON"] = STOP_LAYOUT_AMBIGUITY
        return evidence


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--approval-ref", required=True)
    parser.add_argument("--structural-byte-privacy-approval-ref", required=True)
    parser.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--live-network",
        action="store_true",
        help=(
            "Use the fixed CA SCO endpoint. This flag does not grant project "
            "execution or privacy approval."
        ),
    )
    args = parser.parse_args(argv)
    if not 1 <= args.timeout_seconds <= 30:
        parser.error("--timeout-seconds must be between 1 and 30")
    if not args.live_network:
        parser.error(
            "no synthetic CLI transport is configured; live network requires the "
            "separately authorized one-shot workflow"
        )
    return args


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    try:
        evidence = execute(
            execution_approval_ref=args.approval_ref,
            structural_byte_privacy_approval_ref=(
                args.structural_byte_privacy_approval_ref
            ),
            transport=HttpTransport(),
            timeout_seconds=args.timeout_seconds,
        )
    except RevalidationAuthorizationError as exc:
        print(f"REVALIDATION_AUTHORIZATION_ERROR={type(exc).__name__}", file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(evidence, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "STRUCTURAL_REVALIDATION_SUMMARY="
        + json.dumps(
            {
                "result_status": evidence["REVALIDATION_RESULT_STATUS"],
                "stop_reason": evidence["STOP_REASON"],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
