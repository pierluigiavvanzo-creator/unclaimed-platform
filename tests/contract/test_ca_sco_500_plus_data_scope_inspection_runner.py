import importlib.util
import io
import struct
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[2]
SCRIPT = ROOT / "scripts" / "ca_sco_500_plus_data_scope_inspection.py"


def _module():
    spec = importlib.util.spec_from_file_location("ca_sco_range_inspection", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _synthetic_zip() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(
        buffer,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        archive.writestr(
            "data.csv",
            "Owner Name,Property ID,Amount\nJane Doe,123,700\n",
        )
    return buffer.getvalue()


def test_synthetic_zip_structure_parser_finds_csv_without_record_values() -> None:
    module = _module()
    payload = _synthetic_zip()
    tail_start = max(0, len(payload) - module.TAIL_BYTES)
    eocd = module._find_eocd(payload[tail_start:], tail_start)

    cd_start = eocd["central_directory_offset"]
    cd_end = cd_start + eocd["central_directory_size"]
    members = module._parse_central_directory(
        payload[cd_start:cd_end],
        eocd["entries_total"],
    )

    assert [member["name"] for member in members] == ["data.csv"]
    assert members[0]["compression_method"] == "DEFLATED"


def test_first_record_decompression_stops_before_synthetic_data_row() -> None:
    module = _module()
    payload = _synthetic_zip()
    local = struct.unpack_from("<4s5H3I2H", payload, 0)
    filename_len = local[-2]
    extra_len = local[-1]
    data_start = 30 + filename_len + extra_len

    record = module._decompress_first_record(
        payload[data_start:],
        "DEFLATED",
    )
    assert record == b"Owner Name,Property ID,Amount\n"
    assert b"Jane Doe" not in record

    header = module._parse_header_candidate(record)
    assert header["labels"] == ["Owner Name", "Property ID", "Amount"]
    assert header["potential_pii_labels"] == ["Owner Name"]


def test_data_like_first_record_is_rejected_as_ambiguous() -> None:
    module = _module()
    with pytest.raises(module.InspectionStop) as exc_info:
        module._parse_header_candidate(b"Jane Doe,123,700\n")
    assert exc_info.value.reason == "HEADER_AMBIGUOUS"
