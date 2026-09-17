from __future__ import annotations

import csv
import io
import struct
import zlib

from scripts import ca_sco_mvp1_property_type_validation as mvp1
from scripts import ca_sco_property_type_semantic_verification as legacy


def _row(property_type: str) -> list[str]:
    values = ["SYNTHETIC_VALUE"] * 25
    values[0] = "SYNTHETIC_ID"
    values[1] = property_type
    return values


def _member_prefix(member_name: str, codes: list[str]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\r\n")
    writer.writerow(legacy.CANONICAL_HEADER)
    for code in codes:
        writer.writerow(_row(code))
    raw = output.getvalue().encode("utf-8")
    compressor = zlib.compressobj(level=6, wbits=-15)
    compressed = compressor.compress(raw) + compressor.flush()
    filename = member_name.encode("utf-8")
    local_header = struct.pack(
        "<4s5H3I2H", b"PK\x03\x04", 20, 0x0800, 8, 0, 0, 0, 0, 0, len(filename), 0
    )
    body = local_header + filename + compressed
    return body + b"\x00" * (legacy.RANGE_RESPONSE_BYTES - len(body))


class RangeHandle:
    def __init__(self, body: bytes) -> None:
        self.status = 206
        self.headers: dict[str, str] = {}
        self.body = body

    def read(self, max_bytes: int) -> bytes:
        return self.body[:max_bytes]

    def close(self) -> None:
        return None


class Transport:
    def __init__(self, codes_by_member: dict[str, list[str]]) -> None:
        self.codes_by_member = codes_by_member

    def head(self, timeout_seconds: int) -> legacy.HeadObservation:
        return legacy.HeadObservation(
            status=200,
            headers={
                "content-length": str(legacy.EXPECTED_LENGTH),
                "content-type": legacy.EXPECTED_MEDIA_TYPE,
                "accept-ranges": legacy.EXPECTED_ACCEPT_RANGES,
                "etag": legacy.EXPECTED_ETAG,
            },
        )

    def open_range(self, start: int, end: int, timeout_seconds: int) -> RangeHandle:
        member = next(m for m in legacy.CANONICAL_MEMBERS if m.local_header_offset == start)
        handle = RangeHandle(_member_prefix(member.name, self.codes_by_member[member.name]))
        handle.headers = {
            "content-range": f"bytes {start}-{end}/{legacy.EXPECTED_LENGTH}",
            "content-length": str(legacy.RANGE_RESPONSE_BYTES),
        }
        return handle


def test_nonconforming_first_row_is_deferred_and_later_in03_is_observed() -> None:
    codes = {
        member.name: ["BAD", "IN03", "AC01", "IN01"]
        for member in legacy.CANONICAL_MEMBERS
    }
    result = mvp1.execute("EXECUTION_APPROVAL", "PRIVACY_APPROVAL", Transport(codes))

    assert result["semantic_result_status"] == "MVP1_PRIMARY_IN03_OBSERVED"
    assert result["stop_reason"] is None
    summary = result["sample_summary"]
    assert summary["sample_rows_examined"] == 16
    assert summary["nonconforming_rows_deferred_count"] == 4
    assert summary["insurance_rows_count"] == 8
    assert summary["mvp1_primary_rows_count"] == 4
    assert summary["shape_valid_non_target_rows_count"] == 4
    assert summary["distinct_insurance_codes"] == ["IN01", "IN03"]
    assert result["requests_summary"]["http_requests_total"] == 5
    assert result["requests_summary"]["total_body_bytes_read"] == 524288
    assert all(value is False for value in result["safety_state"].values())


def test_unknown_in_prefix_is_deferred_without_stopping_later_rows() -> None:
    codes = {
        member.name: ["IN10", "IN03", "ZZZZ", "AC01"]
        for member in legacy.CANONICAL_MEMBERS
    }
    result = mvp1.execute("EXECUTION_APPROVAL", "PRIVACY_APPROVAL", Transport(codes))

    assert result["semantic_result_status"] == "MVP1_PRIMARY_IN03_OBSERVED"
    assert result["sample_summary"]["nonconforming_rows_deferred_count"] == 4
    assert result["sample_summary"]["mvp1_primary_rows_count"] == 4
    assert result["sample_summary"]["distinct_insurance_codes"] == ["IN03"]


def test_transport_or_structural_failure_still_fails_closed() -> None:
    codes = {
        member.name: ["IN03", "AC01", "ZZZZ", "IN01"]
        for member in legacy.CANONICAL_MEMBERS
    }
    transport = Transport(codes)
    transport.head = lambda timeout_seconds: legacy.HeadObservation(  # type: ignore[method-assign]
        status=200,
        headers={
            "content-length": "1",
            "content-type": legacy.EXPECTED_MEDIA_TYPE,
            "accept-ranges": legacy.EXPECTED_ACCEPT_RANGES,
            "etag": legacy.EXPECTED_ETAG,
        },
    )
    result = mvp1.execute("EXECUTION_APPROVAL", "PRIVACY_APPROVAL", transport)
    assert result["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert result["stop_reason"] == "TRANSPORT_METADATA_DRIFT"
    assert result["requests_summary"]["range_requests"] == 0
