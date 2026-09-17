from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_PATH = (
    ROOT
    / "sources/evidence/"
    "ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json"
)
SCHEMA_PATH = (
    ROOT
    / "schemas/common/property_type_transport_archive_layout_revalidation_execution.v1.schema.json"
)
SEMANTIC_RUNNER_PATH = ROOT / "scripts/ca_sco_property_type_semantic_verification.py"


def _load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_semantic_runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "ca_sco_semantic_runner_post_structural_revalidation",
        SEMANTIC_RUNNER_PATH,
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_persisted_structural_revalidation_evidence_validates() -> None:
    schema = _load(SCHEMA_PATH)
    evidence = _load(EVIDENCE_PATH)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    ).validate(evidence)

    assert evidence["REVALIDATION_RESULT_STATUS"] == "CANDIDATE_BASELINE_ESTABLISHED"
    assert evidence["STOP_REASON"] is None
    assert evidence["CANONICAL_MEMBER_MATCH_STATUS"] == "ALL_CANONICAL_MEMBERS_UNIQUE"
    assert evidence["ADDITIONAL_MEMBER_COUNT"] == 0
    assert evidence["OBSERVED_CONTENT_LENGTH"] == 162560390
    assert evidence["OBSERVED_ETAG"] == '"222dd79f04c2a0a8fff166b01c8da746"'
    assert evidence["CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS"] == {
        "From_500_To_Beyond_1_of_4.csv": 0,
        "From_500_To_Beyond_2_of_4.csv": 59745428,
        "From_500_To_Beyond_3_of_4.csv": 96861315,
        "From_500_To_Beyond_4_of_4.csv": 134172553,
    }


def test_candidate_evidence_is_not_silently_adopted_by_semantic_runner() -> None:
    evidence = _load(EVIDENCE_PATH)
    runner = _load_semantic_runner()

    assert runner.EXPECTED_LENGTH == 162416884
    assert runner.EXPECTED_ETAG == '"b25b315b6cd8007624387c3a00d4b1fe"'
    assert [member.local_header_offset for member in runner.CANONICAL_MEMBERS] == [
        0,
        59747797,
        96862896,
        134174190,
    ]

    assert evidence["OBSERVED_CONTENT_LENGTH"] != runner.EXPECTED_LENGTH
    assert evidence["OBSERVED_ETAG"] != runner.EXPECTED_ETAG
    candidate_offsets = evidence["CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS"]
    assert isinstance(candidate_offsets, dict)
    assert list(candidate_offsets.values()) != [
        member.local_header_offset for member in runner.CANONICAL_MEMBERS
    ]
