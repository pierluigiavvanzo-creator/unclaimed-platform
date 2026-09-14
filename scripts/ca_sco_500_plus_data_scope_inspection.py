#!/usr/bin/env python3
"""Bounded HTTP Range structure inspection for the CA SCO $500+ ZIP.

The runner verifies exact transport metadata, reads only bounded byte ranges,
never downloads the full archive, never persists raw source bytes, and never
parses CSV data rows. It emits derived ZIP/member metadata and, only when
strictly header-like, the first logical CSV record as header labels.
"""

from __future__ import annotations

import argparse
import csv
import http.client
import json
import re
import ssl
import struct
import sys
import zlib
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ENDPOINT = "https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip"
HOST = "claimit.ca.gov"
EXPECTED_LENGTH = 162_416_884
EXPECTED_ETAG = '"b25b315b6cd8007624387c3a00d4b1fe"'
EXPECTED_MEDIA_TYPE = "application/zip"
EXPECTED_ACCEPT_RANGES = "bytes"
TAIL_BYTES = 131_072
CENTRAL_DIRECTORY_MAX_BYTES = 4_194_304
MAX_ARCHIVE_MEMBERS = 10_000
MAX_CSV_CANDIDATES = 10
MAX_MEMBER_RESPONSE_BYTES = 1_048_576
ACTUAL_MEMBER_PROBE_BYTES = 65_536
MAX_UNCOMPRESSED_HEADER_BYTES = 65_536
MAX_RANGE_REQUESTS = 12
MAX_TOTAL_RESPONSE_BYTES = 14_811_136
USER_AGENT = "unclaimed-platform-data-scope-inspection/1.0 bounded-range"
HEADER_TERMS = {
    "owner",
    "property",
    "amount",
    "holder",
    "report",
    "name",
    "address",
    "city",
    "state",
    "zip",
    "postal",
    "type",
    "date",
    "id",
    "code",
    "number",
}
PII_TERMS = {
    "name",
    "owner",
    "address",
    "city",
    "state",
    "zip",
    "postal",
    "ssn",
    "social security",
    "dob",
    "birth",
    "phone",
    "email",
}
SAFE_HEADER_RE = re.compile(r"^[A-Za-z][A-Za-z0-9 _./()#&'\-]{0,127}$")


class InspectionStop(RuntimeError):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def _path() -> str:
    parsed = urlparse(ENDPOINT)
    if parsed.scheme != "https" or parsed.hostname != HOST:
        raise InspectionStop("TRANSPORT_METADATA_DRIFT")
    return parsed.path


def _head(timeout: int) -> dict[str, Any]:
    connection = http.client.HTTPSConnection(
        HOST,
        timeout=timeout,
        context=ssl.create_default_context(),
    )
    try:
        connection.request(
            "HEAD",
            _path(),
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "*/*",
                "Connection": "close",
            },
        )
        response = connection.getresponse()
        headers = {key.lower(): value for key, value in response.getheaders()}
        # Deliberately do not call response.read().
        return {"status": response.status, "headers": headers}
    finally:
        connection.close()


def _verify_head(observation: dict[str, Any]) -> dict[str, Any]:
    status = observation["status"]
    headers = observation["headers"]
    content_length_raw = headers.get("content-length")
    content_length = (
        int(content_length_raw)
        if content_length_raw and content_length_raw.isdigit()
        else None
    )
    media_type = (headers.get("content-type") or "").split(";", 1)[0].strip().lower()
    observed = {
        "head_status": status,
        "content_length": content_length,
        "content_type": media_type or None,
        "accept_ranges": headers.get("accept-ranges"),
        "etag": headers.get("etag"),
        "last_modified": headers.get("last-modified"),
    }
    if (
        status != 200
        or content_length != EXPECTED_LENGTH
        or media_type != EXPECTED_MEDIA_TYPE
        or (headers.get("accept-ranges") or "").lower() != EXPECTED_ACCEPT_RANGES
        or headers.get("etag") != EXPECTED_ETAG
    ):
        raise InspectionStop("TRANSPORT_METADATA_DRIFT")
    return observed


def _range_get(
    start: int,
    end: int,
    timeout: int,
    purpose: str,
) -> tuple[bytes, dict[str, Any]]:
    if start < 0 or end < start or end >= EXPECTED_LENGTH:
        raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
    expected_bytes = end - start + 1
    if expected_bytes > MAX_MEMBER_RESPONSE_BYTES and purpose == "MEMBER_PREFIX":
        raise InspectionStop("MEMBER_PREFIX_LIMIT_EXCEEDED")

    connection = http.client.HTTPSConnection(
        HOST,
        timeout=timeout,
        context=ssl.create_default_context(),
    )
    try:
        connection.request(
            "GET",
            _path(),
            headers={
                "User-Agent": USER_AGENT,
                "Accept": EXPECTED_MEDIA_TYPE,
                "Range": f"bytes={start}-{end}",
                "If-Match": EXPECTED_ETAG,
                "Connection": "close",
            },
        )
        response = connection.getresponse()
        headers = {key.lower(): value for key, value in response.getheaders()}
        if response.status != 206:
            # Never consume an unexpected full-body/non-partial response.
            raise InspectionStop("RANGE_RESPONSE_NOT_PARTIAL")
        content_range = headers.get("content-range")
        expected_content_range = f"bytes {start}-{end}/{EXPECTED_LENGTH}"
        if content_range != expected_content_range:
            raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
        body = response.read(expected_bytes + 1)
        if len(body) != expected_bytes:
            raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
        meta = {
            "purpose": purpose,
            "range_start": start,
            "range_end": end,
            "http_status": response.status,
            "content_range": content_range,
            "bytes_read": len(body),
        }
        return body, meta
    finally:
        connection.close()


def _find_eocd(tail: bytes, tail_start: int) -> dict[str, int]:
    signature = b"PK\x05\x06"
    index = tail.rfind(signature)
    if index < 0 or index + 22 > len(tail):
        raise InspectionStop("TAIL_STRUCTURE_NOT_FOUND_WITHIN_LIMIT")
    (
        _signature,
        disk_no,
        cd_disk_no,
        entries_disk,
        entries_total,
        cd_size,
        cd_offset,
        comment_len,
    ) = struct.unpack_from("<4s4H2IH", tail, index)
    if disk_no != 0 or cd_disk_no != 0 or entries_disk != entries_total:
        raise InspectionStop("UNSUPPORTED_ZIP_STRUCTURE")
    if entries_total == 0xFFFF or cd_size == 0xFFFFFFFF or cd_offset == 0xFFFFFFFF:
        raise InspectionStop("UNSUPPORTED_ZIP64")
    if index + 22 + comment_len > len(tail):
        raise InspectionStop("TAIL_STRUCTURE_NOT_FOUND_WITHIN_LIMIT")
    if entries_total > MAX_ARCHIVE_MEMBERS:
        raise InspectionStop("ARCHIVE_MEMBER_LIMIT_EXCEEDED")
    if cd_size > CENTRAL_DIRECTORY_MAX_BYTES:
        raise InspectionStop("CENTRAL_DIRECTORY_TOO_LARGE")
    if cd_offset + cd_size > EXPECTED_LENGTH:
        raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
    return {
        "entries_total": entries_total,
        "central_directory_size": cd_size,
        "central_directory_offset": cd_offset,
        "eocd_offset": tail_start + index,
    }


def _decode_zip_name(raw: bytes, flags: int) -> str:
    encoding = "utf-8" if flags & 0x0800 else "cp437"
    try:
        return raw.decode(encoding, errors="strict")
    except UnicodeDecodeError as exc:
        raise InspectionStop("UNSAFE_MEMBER_PATH") from exc


def _safe_member_name(name: str) -> bool:
    if not name or name.startswith(("/", "\\")):
        return False
    normalized = name.replace("\\", "/")
    parts = normalized.split("/")
    return all(part not in {".", ".."} for part in parts if part)


def _parse_central_directory(
    data: bytes,
    expected_entries: int,
) -> list[dict[str, Any]]:
    members: list[dict[str, Any]] = []
    pos = 0
    fixed = struct.Struct("<4s6H3I5H2I")
    while pos < len(data):
        if len(data) - pos < fixed.size:
            raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
        values = fixed.unpack_from(data, pos)
        if values[0] != b"PK\x01\x02":
            raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
        (
            _signature,
            _version_made,
            _version_needed,
            flags,
            compression,
            _mtime,
            _mdate,
            _crc,
            compressed_size,
            uncompressed_size,
            filename_len,
            extra_len,
            comment_len,
            disk_start,
            _internal_attr,
            _external_attr,
            local_offset,
        ) = values
        total_len = fixed.size + filename_len + extra_len + comment_len
        if pos + total_len > len(data):
            raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
        raw_name = data[pos + fixed.size : pos + fixed.size + filename_len]
        name = _decode_zip_name(raw_name, flags)
        if not _safe_member_name(name):
            raise InspectionStop("UNSAFE_MEMBER_PATH")
        if disk_start != 0:
            raise InspectionStop("UNSUPPORTED_ZIP_STRUCTURE")
        if (
            compressed_size == 0xFFFFFFFF
            or uncompressed_size == 0xFFFFFFFF
            or local_offset == 0xFFFFFFFF
        ):
            raise InspectionStop("UNSUPPORTED_ZIP64")
        encrypted = bool(flags & 0x0001)
        if encrypted:
            raise InspectionStop("ENCRYPTED_MEMBER")
        if compression not in {0, 8}:
            raise InspectionStop("UNSUPPORTED_COMPRESSION")
        members.append(
            {
                "name": name,
                "compressed_size": compressed_size,
                "uncompressed_size": uncompressed_size,
                "compression_method": "STORED" if compression == 0 else "DEFLATED",
                "encrypted": False,
                "local_header_offset": local_offset,
            }
        )
        pos += total_len
    if len(members) != expected_entries:
        raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
    return members


def _append_record_byte(
    output: bytearray,
    value: int,
    state: dict[str, bool],
) -> bool:
    output.append(value)
    if len(output) > MAX_UNCOMPRESSED_HEADER_BYTES:
        raise InspectionStop("HEADER_NOT_COMPLETE_WITHIN_LIMIT")

    if state["pending_quote"]:
        if value == 0x22:
            state["pending_quote"] = False
            return False
        state["quoted"] = False
        state["pending_quote"] = False

    if value == 0x22:
        if state["quoted"]:
            state["pending_quote"] = True
        else:
            state["quoted"] = True
        return False
    return value == 0x0A and not state["quoted"]


def _decompress_first_record(compressed: bytes, method: str) -> bytes:
    output = bytearray()
    state = {"quoted": False, "pending_quote": False}
    if method == "STORED":
        for value in compressed:
            if _append_record_byte(output, value, state):
                return bytes(output)
        raise InspectionStop("HEADER_NOT_COMPLETE_WITHIN_LIMIT")

    decompressor = zlib.decompressobj(-15)
    pending = b""
    for value in compressed:
        pending += bytes([value])
        while pending:
            chunk = decompressor.decompress(pending, max_length=1)
            pending = decompressor.unconsumed_tail
            if chunk and _append_record_byte(output, chunk[0], state):
                return bytes(output)
            if not chunk and not pending:
                break
    raise InspectionStop("HEADER_NOT_COMPLETE_WITHIN_LIMIT")


def _parse_header_candidate(record_bytes: bytes) -> dict[str, Any]:
    try:
        text = record_bytes.decode("utf-8-sig", errors="strict")
    except UnicodeDecodeError as exc:
        raise InspectionStop("HEADER_ENCODING_UNRESOLVED") from exc
    text = text.rstrip("\r\n")
    delimiters = [",", "\t", "|", ";"]
    counts = {delimiter: text.count(delimiter) for delimiter in delimiters}
    delimiter = max(counts, key=counts.get)
    if counts[delimiter] == 0:
        raise InspectionStop("HEADER_AMBIGUOUS")
    try:
        rows = list(csv.reader([text], delimiter=delimiter, strict=True))
    except csv.Error as exc:
        raise InspectionStop("HEADER_AMBIGUOUS") from exc
    if len(rows) != 1:
        raise InspectionStop("HEADER_AMBIGUOUS")
    labels = [cell.strip() for cell in rows[0]]
    if not 2 <= len(labels) <= 256:
        raise InspectionStop("HEADER_AMBIGUOUS")
    if any(not label or not SAFE_HEADER_RE.fullmatch(label) for label in labels):
        raise InspectionStop("HEADER_AMBIGUOUS")
    normalized = [label.casefold() for label in labels]
    if len(set(normalized)) != len(normalized):
        raise InspectionStop("HEADER_AMBIGUOUS")
    term_hits = sum(
        1
        for label in normalized
        if any(term in label for term in HEADER_TERMS)
    )
    if term_hits < min(3, len(labels)):
        raise InspectionStop("HEADER_AMBIGUOUS")
    potential_pii = [
        label
        for label in labels
        if any(term in label.casefold() for term in PII_TERMS)
    ]
    return {
        "labels": labels,
        "delimiter": "\\t" if delimiter == "\t" else delimiter,
        "encoding": "utf-8",
        "column_count": len(labels),
        "header_confidence": "HIGH_DETERMINISTIC_LABEL_HEURISTIC",
        "potential_pii_labels": potential_pii,
    }


def _inspect_member(
    member: dict[str, Any],
    timeout: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    local_offset = member["local_header_offset"]
    end = min(
        local_offset + ACTUAL_MEMBER_PROBE_BYTES - 1,
        EXPECTED_LENGTH - 1,
    )
    probe, request_meta = _range_get(
        local_offset,
        end,
        timeout,
        "MEMBER_PREFIX",
    )
    if len(probe) < 30 or probe[:4] != b"PK\x03\x04":
        raise InspectionStop("UNEXPECTED_RESPONSE_BODY_BEHAVIOR")
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
    ) = struct.unpack_from("<4s5H3I2H", probe, 0)
    if flags & 0x0001:
        raise InspectionStop("ENCRYPTED_MEMBER")
    if compression not in {0, 8}:
        raise InspectionStop("UNSUPPORTED_COMPRESSION")
    data_start = 30 + filename_len + extra_len
    if data_start >= len(probe):
        raise InspectionStop("MEMBER_PREFIX_LIMIT_EXCEEDED")
    compressed_prefix = probe[data_start:]
    record = _decompress_first_record(
        compressed_prefix,
        member["compression_method"],
    )
    header = _parse_header_candidate(record)
    return header, request_meta


def _base_result(approval_ref: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "execution_id": "ca.sco.unclaimed_property.bulk.500_plus.data_scope.2026-09-14",
        "source_id": "ca.sco.unclaimed_property.bulk",
        "source_segment_id": "ca.sco.unclaimed_property.bulk.500_plus",
        "jurisdiction": "CA",
        "execution_approval_ref": approval_ref,
        "executed_at": _utc_now(),
        "target": {
            "endpoint": ENDPOINT,
            "expected_content_length": EXPECTED_LENGTH,
            "expected_etag": EXPECTED_ETAG,
            "expected_media_type": EXPECTED_MEDIA_TYPE,
            "expected_accept_ranges": EXPECTED_ACCEPT_RANGES,
        },
        "controls": {
            "request_mode": "HTTP_RANGE_GET_ONLY",
            "full_body_request_allowed": False,
            "tail_bytes_max": TAIL_BYTES,
            "central_directory_bytes_max": CENTRAL_DIRECTORY_MAX_BYTES,
            "member_response_bytes_max_each": MAX_MEMBER_RESPONSE_BYTES,
            "actual_member_probe_bytes_each": ACTUAL_MEMBER_PROBE_BYTES,
            "uncompressed_header_bytes_max_each": MAX_UNCOMPRESSED_HEADER_BYTES,
            "range_requests_max": MAX_RANGE_REQUESTS,
            "total_response_body_bytes_max": MAX_TOTAL_RESPONSE_BYTES,
            "csv_data_rows_allowed": 0,
            "record_values_persistence_allowed": False,
        },
        "transport_verification": {},
        "range_requests": [],
        "archive": {
            "parse_status": "NOT_ATTEMPTED",
            "zip64": False,
            "member_count": None,
            "csv_candidate_count": None,
            "members": [],
        },
        "csv_header_candidates": [],
        "total_response_body_bytes_read": 0,
        "safety_state": {
            "full_archive_downloaded": False,
            "raw_body_persisted": False,
            "temporary_source_files_created": False,
            "csv_data_rows_parsed": 0,
            "record_values_persisted": False,
            "real_pii_processing_authorized": False,
            "identity_resolution_performed": False,
            "beneficiary_matching_performed": False,
            "outreach_performed": False,
            "source_approved": False,
            "source_enabled": False,
        },
        "result_status": "FAILED",
        "stop_reason": None,
    }


def execute(approval_ref: str, timeout: int) -> dict[str, Any]:
    result = _base_result(approval_ref)
    try:
        result["transport_verification"] = _verify_head(_head(timeout))

        tail_start = max(0, EXPECTED_LENGTH - TAIL_BYTES)
        tail, tail_meta = _range_get(
            tail_start,
            EXPECTED_LENGTH - 1,
            timeout,
            "TAIL",
        )
        result["range_requests"].append(tail_meta)
        result["total_response_body_bytes_read"] += len(tail)

        eocd = _find_eocd(tail, tail_start)
        cd_start = eocd["central_directory_offset"]
        cd_end = cd_start + eocd["central_directory_size"] - 1
        if cd_start >= tail_start and cd_end < EXPECTED_LENGTH:
            offset = cd_start - tail_start
            central = tail[offset : offset + eocd["central_directory_size"]]
        else:
            central, cd_meta = _range_get(
                cd_start,
                cd_end,
                timeout,
                "CENTRAL_DIRECTORY",
            )
            result["range_requests"].append(cd_meta)
            result["total_response_body_bytes_read"] += len(central)

        members = _parse_central_directory(
            central,
            eocd["entries_total"],
        )
        csv_members = [
            member
            for member in members
            if member["name"].lower().endswith(".csv")
        ]
        if not csv_members:
            raise InspectionStop("NO_CSV_MEMBER")
        if len(csv_members) > MAX_CSV_CANDIDATES:
            raise InspectionStop("CSV_MEMBER_LIMIT_EXCEEDED")

        result["archive"] = {
            "parse_status": "PARSED",
            "zip64": False,
            "member_count": len(members),
            "csv_candidate_count": len(csv_members),
            "members": members,
        }

        for member in csv_members:
            if len(result["range_requests"]) >= MAX_RANGE_REQUESTS:
                raise InspectionStop("RANGE_REQUEST_BUDGET_EXCEEDED")
            header, request_meta = _inspect_member(member, timeout)
            result["range_requests"].append(request_meta)
            result["total_response_body_bytes_read"] += request_meta["bytes_read"]
            if result["total_response_body_bytes_read"] > MAX_TOTAL_RESPONSE_BYTES:
                raise InspectionStop("TOTAL_BYTE_BUDGET_EXCEEDED")
            result["csv_header_candidates"].append(
                {
                    "member_name": member["name"],
                    **header,
                }
            )

        result["result_status"] = "SUCCEEDED_STRUCTURE_ONLY"
        return result
    except InspectionStop as exc:
        if result["archive"]["parse_status"] == "NOT_ATTEMPTED":
            result["archive"]["parse_status"] = "BLOCKED"
        result["result_status"] = "BLOCKED"
        result["stop_reason"] = exc.reason
        return result
    except Exception as exc:  # fail closed; never serialize raw source values
        result["result_status"] = "FAILED"
        result["stop_reason"] = f"UNEXPECTED_{type(exc).__name__}"
        return result


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--approval-ref", required=True)
    parser.add_argument("--timeout-seconds", type=int, default=10)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if not 1 <= args.timeout_seconds <= 30:
        parser.error("--timeout-seconds must be between 1 and 30")
    return args


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    result = execute(args.approval_ref, args.timeout_seconds)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = {
        "result_status": result["result_status"],
        "stop_reason": result["stop_reason"],
        "member_count": result["archive"]["member_count"],
        "csv_candidate_count": result["archive"]["csv_candidate_count"],
        "header_candidates": result["csv_header_candidates"],
        "range_request_count": len(result["range_requests"]),
        "total_body_bytes_read": result["total_response_body_bytes_read"],
    }
    print(
        "DATA_SCOPE_SUMMARY="
        + json.dumps(summary, sort_keys=True, separators=(",", ":"))
    )
    if result["result_status"] in {"SUCCEEDED_STRUCTURE_ONLY", "BLOCKED"}:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
