from __future__ import annotations

import csv
import io
import struct
import subprocess
import sys
import zlib
from pathlib import Path

from scripts import ca_sco_mvp1_same_bytes_deeper_insurance_discovery as deeper
from scripts import ca_sco_property_type_semantic_verification as legacy

ROOT = Path(__file__).resolve().parents[2]


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
        "<4s5H3I2H",
        b"PK\x03\x04",
        20,
        0x0800,
        8,
        0,
        0,
        0,
        0,
        0,
        len(filename),
        0,
    )
    body = local_header + filename + compressed
    assert len(body) < legacy.RANGE_RESPONSE_BYTES
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


def test_module_cli_boots_offline() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "scripts.ca_sco_mvp1_same_bytes_deeper_insurance_discovery",
            "--help",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert "--live-network" in completed.stdout
    assert "--approval-ref" in completed.stdout


def test_deeper_scan_finds_in03_after_legacy_four_row_boundary() -> None:
    codes = {
        member.name: ["BAD"] * 8 + ["IN03"] + ["AC01"] * 3
        for member in legacy.CANONICAL_MEMBERS
    }

    result = deeper.execute("EXECUTION_APPROVAL", "PRIVACY_APPROVAL", Transport(codes))

    assert result["semantic_result_status"] == "MVP1_PRIMARY_IN03_OBSERVED"
    assert result["stop_reason"] is None
    assert result["scan_mode"] == deeper.SCAN_MODE
    assert result["requests_summary"] == {
        "head_requests": 1,
        "range_requests": 4,
        "http_requests_total": 5,
        "total_body_bytes_read": 524288,
    }

    summary = result["sample_summary"]
    assert summary["sample_rows_examined"] == 48
    assert summary["nonconforming_rows_deferred_count"] == 32
    assert summary["shape_valid_non_target_rows_count"] == 12
    assert summary["insurance_rows_count"] == 4
    assert summary["mvp1_primary_rows_count"] == 4
    assert summary["distinct_insurance_codes"] == ["IN03"]
    assert set(summary["scan_status_per_member"].values()) == {
        deeper.PREFIX_EXHAUSTED_BEFORE_ROW_CAP
    }
    assert result["controls"]["rows_max_per_member"] == 256
    assert result["controls"]["rows_max_total"] == 1024
    assert result["controls"]["range_response_bytes_max_each"] == 131072
    assert result["controls"]["total_source_response_body_bytes_max"] == 524288
    assert result["controls"]["source_response_byte_budget_unchanged"] is True
    assert all(value is False for value in result["safety_state"].values())


def test_row_cap_is_hard_and_does_not_observe_row_257() -> None:
    codes = {
        member.name: ["BAD"] * deeper.MAX_DEEP_ROWS_PER_MEMBER + ["IN03"]
        for member in legacy.CANONICAL_MEMBERS
    }

    result = deeper.execute("EXECUTION_APPROVAL", "PRIVACY_APPROVAL", Transport(codes))

    assert result["semantic_result_status"] == "NO_INSURANCE_CODE_OBSERVED_IN_BOUNDED_SAMPLE"
    assert result["stop_reason"] is None
    summary = result["sample_summary"]
    assert summary["sample_rows_examined"] == deeper.MAX_DEEP_ROWS_TOTAL
    assert summary["nonconforming_rows_deferred_count"] == deeper.MAX_DEEP_ROWS_TOTAL
    assert summary["insurance_rows_count"] == 0
    assert summary["mvp1_primary_rows_count"] == 0
    assert summary["distinct_insurance_codes"] == []
    assert set(summary["rows_examined_per_member"].values()) == {
        deeper.MAX_DEEP_ROWS_PER_MEMBER
    }
    assert set(summary["scan_status_per_member"].values()) == {deeper.ROW_CAP_REACHED}


def test_exact_authority_insurance_code_without_in03_is_reported() -> None:
    codes = {
        member.name: ["BAD"] * 20 + ["IN01", "IN99"] + ["AC01"]
        for member in legacy.CANONICAL_MEMBERS
    }

    result = deeper.execute("EXECUTION_APPROVAL", "PRIVACY_APPROVAL", Transport(codes))

    assert result["semantic_result_status"] == "INSURANCE_CODE_OBSERVED_NO_IN03"
    assert result["stop_reason"] is None
    summary = result["sample_summary"]
    assert summary["insurance_rows_count"] == 8
    assert summary["mvp1_primary_rows_count"] == 0
    assert summary["distinct_insurance_codes"] == ["IN01", "IN99"]


def test_transport_metadata_drift_still_fails_closed_before_ranges() -> None:
    codes = {
        member.name: ["IN03"] * 10 for member in legacy.CANONICAL_MEMBERS
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

    result = deeper.execute("EXECUTION_APPROVAL", "PRIVACY_APPROVAL", transport)

    assert result["semantic_result_status"] == "STOPPED_FAIL_CLOSED"
    assert result["stop_reason"] == "TRANSPORT_METADATA_DRIFT"
    assert result["requests_summary"]["range_requests"] == 0
    assert result["requests_summary"]["total_body_bytes_read"] == 0
