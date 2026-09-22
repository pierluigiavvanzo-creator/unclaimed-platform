from __future__ import annotations

import importlib.util
import io
import struct
import sys
import zipfile
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "scripts/ca_sco_transport_archive_layout_revalidation.py"


def _load_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_structural_revalidation_test", RUNNER_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class _RangeHandle:
    def __init__(
        self,
        body: bytes,
        start: int,
        end: int,
        total: int,
        etag: str,
        *,
        response_etag: str | None = None,
    ) -> None:
        self.status = 206
        self.body = body
        self.headers = {
            "content-range": f"bytes {start}-{end}/{total}",
            "content-length": str(len(body)),
            "etag": response_etag or etag,
        }

    def read(self, max_bytes: int) -> bytes:
        return self.body[:max_bytes]

    def close(self) -> None:
        return None


class _FakeTransport:
    def __init__(
        self,
        module: ModuleType,
        archive: bytes,
        *,
        wrong_range_etag: bool = False,
    ) -> None:
        self.module = module
        self.archive = archive
        self.etag = '"synthetic-etag"'
        self.wrong_range_etag = wrong_range_etag
        self.range_requests: list[tuple[int, int, str]] = []

    def head(self, timeout_seconds: int):
        assert 1 <= timeout_seconds <= 30
        return self.module.HeadObservation(
            status=200,
            headers={
                "content-length": str(len(self.archive)),
                "content-type": "application/zip",
                "accept-ranges": "bytes",
                "etag": self.etag,
                "last-modified": "Thu, 17 Sep 2026 00:00:00 GMT",
            },
        )

    def open_range(self, start: int, end: int, etag: str, timeout_seconds: int):
        assert etag == self.etag
        assert 1 <= timeout_seconds <= 30
        self.range_requests.append((start, end, etag))
        return _RangeHandle(
            self.archive[start : end + 1],
            start,
            end,
            len(self.archive),
            self.etag,
            response_etag='"different-etag"' if self.wrong_range_etag else None,
        )


def _archive(
    module: ModuleType,
    *,
    omit_last: bool = False,
    extra: bool = True,
) -> tuple[bytes, dict[str, int]]:
    output = io.BytesIO()
    with zipfile.ZipFile(
        output,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        allowZip64=False,
    ) as archive:
        names = module.CANONICAL_MEMBERS[:-1] if omit_last else module.CANONICAL_MEMBERS
        for index, name in enumerate(names):
            archive.writestr(name, f"synthetic-{index}\n")
        if extra:
            archive.writestr("noncanonical-aggregate-only.txt", "synthetic\n")
        offsets = {info.filename: info.header_offset for info in archive.infolist()}
    return output.getvalue(), offsets


def test_structural_revalidation_derives_canonical_offsets_without_payload_parsing() -> None:
    runner = _load_runner()
    archive, expected_offsets = _archive(runner)
    transport = _FakeTransport(runner, archive)

    evidence = runner.execute(
        runner.EXECUTION_APPROVAL_REF,
        runner.STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF,
        transport,
    )

    assert evidence["REVALIDATION_RESULT_STATUS"] == "CANDIDATE_BASELINE_ESTABLISHED"
    assert evidence["STOP_REASON"] is None
    assert evidence["CANONICAL_MEMBER_MATCH_STATUS"] == "ALL_CANONICAL_MEMBERS_UNIQUE"
    assert evidence["ADDITIONAL_MEMBER_COUNT"] == 1
    assert evidence["CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS"] == {
        name: expected_offsets[name] for name in runner.CANONICAL_MEMBERS
    }
    assert len(transport.range_requests) == 1


def test_structural_revalidation_fails_closed_on_object_identity_drift() -> None:
    runner = _load_runner()
    archive, _ = _archive(runner)
    transport = _FakeTransport(runner, archive, wrong_range_etag=True)

    evidence = runner.execute(
        runner.EXECUTION_APPROVAL_REF,
        runner.STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF,
        transport,
    )

    assert evidence["REVALIDATION_RESULT_STATUS"] == "STOPPED_FAIL_CLOSED"
    assert evidence["STOP_REASON"] == "ETAG_OR_LENGTH_OBJECT_DRIFT"


def test_structural_revalidation_fails_closed_when_canonical_member_is_missing() -> None:
    runner = _load_runner()
    archive, _ = _archive(runner, omit_last=True, extra=False)
    transport = _FakeTransport(runner, archive)

    evidence = runner.execute(
        runner.EXECUTION_APPROVAL_REF,
        runner.STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF,
        transport,
    )

    assert evidence["REVALIDATION_RESULT_STATUS"] == "STOPPED_FAIL_CLOSED"
    assert evidence["STOP_REASON"] == "CANONICAL_MEMBER_MISSING_OR_DUPLICATE"


def test_structural_revalidation_rejects_zip64_sentinel() -> None:
    runner = _load_runner()
    archive, _ = _archive(runner, extra=False)
    mutable = bytearray(archive)
    eocd = mutable.rfind(runner.EOCD_SIGNATURE)
    assert eocd >= 0
    struct.pack_into("<H", mutable, eocd + 10, 0xFFFF)
    transport = _FakeTransport(runner, bytes(mutable))

    evidence = runner.execute(
        runner.EXECUTION_APPROVAL_REF,
        runner.STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF,
        transport,
    )

    assert evidence["REVALIDATION_RESULT_STATUS"] == "STOPPED_FAIL_CLOSED"
    assert evidence["STOP_REASON"] == "ZIP64_DETECTED"


def test_wrong_approval_refs_fail_before_transport_access() -> None:
    runner = _load_runner()

    class _NoTransport:
        def head(self, timeout_seconds: int):
            raise AssertionError("network/transport must not be reached")

    try:
        runner.execute(
            "WRONG",
            runner.STRUCTURAL_BYTE_PRIVACY_APPROVAL_REF,
            _NoTransport(),
        )
    except runner.RevalidationAuthorizationError:
        pass
    else:
        raise AssertionError("wrong approval must fail before transport")
