"""Attempt-10 streaming NY OSC product slice.

Only the Property Type Code field is buffered. Owner name/address bytes are never
buffered, decoded, logged or returned. Physical records with exactly 13 pipe bytes
match the documented 14-field width; every other shape is deferred metadata-only.
"""

from __future__ import annotations

import zipfile
from pathlib import Path
from typing import Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

from unclaimed_platform.domain.mvp1_vertical_slice import (
    NY_INSURANCE_CODES,
    NY_MVP1_PRIMARY_CODE,
)


class NyOwnerNameProductSliceResultV1(BaseModel):
    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = (
        "ny.osc.unclaimed_funds.owner_name_file"
    )
    status: Literal["COMPLETED"] = "COMPLETED"
    total_records: int = Field(ge=0)
    structurally_conforming_records: int = Field(ge=0)
    deferred_structural_records: int = Field(ge=0)
    authority_backed_insurance_records: int = Field(ge=0)
    primary_in03_candidate_records: int = Field(ge=0)
    other_insurance_records: int = Field(ge=0)
    no_authority_backed_insurance_match_records: int = Field(ge=0)
    property_type_unclassifiable_records: int = Field(ge=0)
    candidate_outcome: Literal[
        "CANDIDATES_PRESENT_AGGREGATE_ONLY",
        "ZERO_CANDIDATE_DOCUMENTED",
    ]
    candidate_materialization_state: Literal[
        "NOT_AUTHORIZED_AGGREGATE_ONLY",
        "NOT_APPLICABLE_ZERO_CANDIDATE",
    ]
    recoverable_value_state: Literal["UNKNOWN_FROM_SOURCE"] = "UNKNOWN_FROM_SOURCE"
    source_amount_available: Literal[False] = False
    fee_basis_state: Literal["NOT_COMPUTABLE_FROM_SOURCE"] = (
        "NOT_COMPUTABLE_FROM_SOURCE"
    )
    economic_actionability: Literal[
        "VALUE_EVIDENCE_REQUIRED",
        "ZERO_CANDIDATE_NO_CASE_ECONOMICS",
    ]
    exact_authority_match_only: Literal[True] = True
    structural_defer_policy: Literal[
        "PIPE_COUNT_NOT_13_DEFER_METADATA_ONLY"
    ] = "PIPE_COUNT_NOT_13_DEFER_METADATA_ONLY"
    owner_values_buffered: Literal[False] = False
    owner_rows_persisted: Literal[False] = False
    owner_field_logging: Literal[False] = False
    row_specific_human_inspection: Literal[False] = False
    no_raw_record_returned: Literal[True] = True
    no_owner_values_returned: Literal[True] = True

    @model_validator(mode="after")
    def validate_counts(self) -> Self:
        structural_total = (
            self.structurally_conforming_records + self.deferred_structural_records
        )
        if structural_total != self.total_records:
            raise ValueError("structural counts do not sum to total records")
        classified = (
            self.authority_backed_insurance_records
            + self.no_authority_backed_insurance_match_records
            + self.property_type_unclassifiable_records
        )
        if classified != self.structurally_conforming_records:
            raise ValueError("classification counts do not sum to conforming records")
        insurance_total = (
            self.primary_in03_candidate_records + self.other_insurance_records
        )
        if insurance_total != self.authority_backed_insurance_records:
            raise ValueError("insurance subtype counts do not sum")
        has_candidates = self.primary_in03_candidate_records > 0
        expected_candidate_state = (
            self.candidate_outcome == "CANDIDATES_PRESENT_AGGREGATE_ONLY"
        )
        if has_candidates != expected_candidate_state:
            raise ValueError("candidate outcome mismatch")
        return self


class _ProductSliceCounter:
    MAX_PROPERTY_TYPE_BYTES = 32

    def __init__(self) -> None:
        self.total = 0
        self.conforming = 0
        self.deferred = 0
        self.insurance = 0
        self.primary = 0
        self.other_insurance = 0
        self.no_match = 0
        self.unclassifiable = 0
        self._pipe_count = 0
        self._field_index = 0
        self._property_type = bytearray()
        self._property_type_overflow = False
        self._has_data = False
        self._pending_cr = False

    def consume(self, value: int) -> None:
        if self._pending_cr:
            self._pending_cr = False
            if value == 10:
                self._finish_record()
                return
            self._consume_data(13)
        if value == 13:
            self._pending_cr = True
            return
        if value == 10:
            self._finish_record()
            return
        self._consume_data(value)

    def finish(self) -> None:
        if self._pending_cr:
            self._pending_cr = False
            self._finish_record()
        elif self._has_data:
            self._finish_record()

    def _consume_data(self, value: int) -> None:
        self._has_data = True
        if value == 124:
            self._pipe_count += 1
            self._field_index += 1
            return
        if self._field_index == 1:
            if len(self._property_type) < self.MAX_PROPERTY_TYPE_BYTES:
                self._property_type.append(value)
            else:
                self._property_type_overflow = True

    def _finish_record(self) -> None:
        if not self._has_data:
            self._reset()
            return
        self.total += 1
        if self._pipe_count != 13:
            self.deferred += 1
            self._reset()
            return
        self.conforming += 1
        if self._property_type_overflow or len(self._property_type) != 4:
            self.unclassifiable += 1
            self._reset()
            return
        try:
            code = bytes(self._property_type).decode("ascii", errors="strict")
        except UnicodeDecodeError:
            self.unclassifiable += 1
            self._reset()
            return
        if code not in NY_INSURANCE_CODES:
            self.no_match += 1
        else:
            self.insurance += 1
            if code == NY_MVP1_PRIMARY_CODE:
                self.primary += 1
            else:
                self.other_insurance += 1
        self._reset()

    def _reset(self) -> None:
        self._pipe_count = 0
        self._field_index = 0
        self._property_type = bytearray()
        self._property_type_overflow = False
        self._has_data = False


def run_ny_owner_name_product_slice(
    archive_path: Path,
    *,
    max_download_bytes: int = 450_000_000,
    max_uncompressed_bytes: int = 2_000_000_000,
    max_archive_members: int = 1,
) -> NyOwnerNameProductSliceResultV1:
    archive_size = archive_path.stat().st_size
    if archive_size > max_download_bytes:
        raise ValueError("archive exceeds bounded download cap")
    if not zipfile.is_zipfile(archive_path):
        raise ValueError("not a ZIP archive")
    with zipfile.ZipFile(archive_path) as archive:
        members = [info for info in archive.infolist() if not info.is_dir()]
        if len(members) != max_archive_members:
            raise ValueError("archive member count mismatch")
        text_members = [
            info for info in members if info.filename.lower().endswith(".txt")
        ]
        if len(text_members) != 1:
            raise ValueError("expected exactly one TXT member")
        selected = text_members[0]
        if selected.file_size > max_uncompressed_bytes:
            raise ValueError("uncompressed TXT exceeds bounded cap")
        counter = _ProductSliceCounter()
        with archive.open(selected, "r") as stream:
            while chunk := stream.read(64 * 1024):
                for value in chunk:
                    counter.consume(value)
            counter.finish()

    has_candidates = counter.primary > 0
    candidate_outcome = (
        "CANDIDATES_PRESENT_AGGREGATE_ONLY"
        if has_candidates
        else "ZERO_CANDIDATE_DOCUMENTED"
    )
    materialization_state = (
        "NOT_AUTHORIZED_AGGREGATE_ONLY"
        if has_candidates
        else "NOT_APPLICABLE_ZERO_CANDIDATE"
    )
    economic_actionability = (
        "VALUE_EVIDENCE_REQUIRED"
        if has_candidates
        else "ZERO_CANDIDATE_NO_CASE_ECONOMICS"
    )
    return NyOwnerNameProductSliceResultV1(
        total_records=counter.total,
        structurally_conforming_records=counter.conforming,
        deferred_structural_records=counter.deferred,
        authority_backed_insurance_records=counter.insurance,
        primary_in03_candidate_records=counter.primary,
        other_insurance_records=counter.other_insurance,
        no_authority_backed_insurance_match_records=counter.no_match,
        property_type_unclassifiable_records=counter.unclassifiable,
        candidate_outcome=candidate_outcome,
        candidate_materialization_state=materialization_state,
        economic_actionability=economic_actionability,
    )
