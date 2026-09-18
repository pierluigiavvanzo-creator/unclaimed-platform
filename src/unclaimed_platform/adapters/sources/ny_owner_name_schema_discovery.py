"""Bounded memory-only schema discovery for the NY OSC Owner Name File.

This module intentionally accepts archive bytes only as an in-memory function argument.
Raw archive bytes and owner-row values are never part of the serializable contracts.
"""

from __future__ import annotations

import io
import zipfile
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

NY_OWNER_NAME_SOURCE_ID = "ny.osc.unclaimed_funds.owner_name_file"
NY_FIRST_DOWNLOAD_GATE_ID = (
    "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION"
)
NY_DOCUMENTED_ARCHIVE_NAME = "NYSFINDERS.ZIP"
NY_DOCUMENTED_DELIMITER = "|"

NY_DOCUMENTED_FIELDS: tuple[str, ...] = (
    "Property ID",
    "Property Type Code",
    "Property Type Code Description",
    "Property Owner Count",
    "Owner Name",
    "Owner Address 1",
    "Owner Address 2",
    "Owner Address 3",
    "Owner City",
    "Owner Address State",
    "Owner Zip Code",
    "Owner Country Code",
    "Holder Name",
    "Holder Report Year",
)
NY_PROPERTY_TYPE_CODE_INDEX = 1


class NyOwnerNameSchemaDiscoveryAuthorization(BaseModel):
    """Non-content authorization envelope for one bounded in-memory discovery."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    mode: Literal["SYNTHETIC_TEST", "AUTHORIZED_TRANSIENT_MEMORY_ONLY"]
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OWNER_NAME_SOURCE_ID
    gate_id: Literal[
        "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION"
    ] = NY_FIRST_DOWNLOAD_GATE_ID
    approval_id: str = Field(min_length=1)
    max_download_bytes: int = Field(gt=0)
    max_uncompressed_bytes: int = Field(gt=0)
    max_archive_members: int = Field(gt=0)
    expected_archive_name: Literal["NYSFINDERS.ZIP"] = NY_DOCUMENTED_ARCHIVE_NAME
    expected_delimiter: Literal["|"] = NY_DOCUMENTED_DELIMITER
    persist_raw_bytes: Literal[False] = False
    persist_owner_rows: Literal[False] = False
    owner_field_logging: Literal[False] = False
    row_specific_human_inspection: Literal[False] = False


class NyOwnerNameSchemaDiscoveryResult(BaseModel):
    """Persistable non-PII output from bounded schema discovery."""

    model_config = ConfigDict(frozen=True)

    contract_version: Literal["1.0.0"] = "1.0.0"
    status: Literal["DISCOVERED", "BLOCKED"]
    reason_code: str = Field(min_length=3)
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = NY_OWNER_NAME_SOURCE_ID
    gate_id: Literal[
        "HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION"
    ] = NY_FIRST_DOWNLOAD_GATE_ID
    approval_id: str = Field(min_length=1)
    archive_byte_count: int = Field(ge=0)
    archive_member_count: int | None = Field(default=None, ge=0)
    member_names_persisted: Literal[False] = False
    selected_text_member_present: bool | None = None
    selected_member_uncompressed_bytes: int | None = Field(default=None, ge=0)
    observed_delimiter: Literal["|"] | None = None
    documented_layout_field_count: Literal[14] = len(NY_DOCUMENTED_FIELDS)
    observed_data_field_count: int | None = Field(default=None, ge=0)
    observed_header_state: Literal[
        "EXACT_DOCUMENTED_HEADER",
        "UTF8_BOM_DOCUMENTED_HEADER",
        "NO_HEADER_OBSERVED",
        "NOT_EVALUATED",
    ]
    physical_header_names: tuple[str, ...]
    aggregate_complete_record_count: int | None = Field(default=None, ge=0)
    property_type_code_column_index_zero_based: Literal[1] = NY_PROPERTY_TYPE_CODE_INDEX
    property_type_ascii_record_count: int | None = Field(default=None, ge=0)
    nature_of_property_mapping_state: Literal[
        "DETERMINISTIC_DOCUMENTED_POSITION_REQUIRES_LATER_CODE_VALIDATION",
        "NOT_CONFIRMED",
    ]
    encoding_state: Literal["NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY"]
    raw_file_persisted: Literal[False] = False
    owner_rows_persisted: Literal[False] = False
    owner_field_logging: Literal[False] = False
    row_specific_human_inspection: Literal[False] = False
    no_owner_values_returned: Literal[True] = True


def _blocked(
    auth: NyOwnerNameSchemaDiscoveryAuthorization,
    *,
    reason_code: str,
    archive_byte_count: int,
    archive_member_count: int | None = None,
    selected_text_member_present: bool | None = None,
    selected_member_uncompressed_bytes: int | None = None,
) -> NyOwnerNameSchemaDiscoveryResult:
    return NyOwnerNameSchemaDiscoveryResult(
        status="BLOCKED",
        reason_code=reason_code,
        approval_id=auth.approval_id,
        archive_byte_count=archive_byte_count,
        archive_member_count=archive_member_count,
        selected_text_member_present=selected_text_member_present,
        selected_member_uncompressed_bytes=selected_member_uncompressed_bytes,
        observed_header_state="NOT_EVALUATED",
        physical_header_names=(),
        nature_of_property_mapping_state="NOT_CONFIRMED",
        encoding_state="NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY",
    )


def discover_ny_owner_name_schema(
    authorization: NyOwnerNameSchemaDiscoveryAuthorization,
    archive_bytes: bytes,
) -> NyOwnerNameSchemaDiscoveryResult:
    """Inspect one ZIP entirely in memory and return only non-owner schema metadata.

    The archive byte cap is enforced before ZIP parsing. ZIP central-directory metadata
    is then used to enforce archive-member and uncompressed-size caps before any member
    is opened. Owner name/address fields are never decoded, logged, or returned.
    """

    archive_byte_count = len(archive_bytes)
    if archive_byte_count > authorization.max_download_bytes:
        return _blocked(
            authorization,
            reason_code="ARCHIVE_EXCEEDS_DOWNLOAD_CAP",
            archive_byte_count=archive_byte_count,
        )

    buffer = io.BytesIO(archive_bytes)
    if not zipfile.is_zipfile(buffer):
        return _blocked(
            authorization,
            reason_code="NOT_A_ZIP_ARCHIVE",
            archive_byte_count=archive_byte_count,
        )

    buffer.seek(0)
    with zipfile.ZipFile(buffer) as archive:
        file_members = [info for info in archive.infolist() if not info.is_dir()]
        member_count = len(file_members)

        if member_count == 0:
            return _blocked(
                authorization,
                reason_code="ARCHIVE_HAS_NO_FILES",
                archive_byte_count=archive_byte_count,
                archive_member_count=0,
            )

        if member_count > authorization.max_archive_members:
            return _blocked(
                authorization,
                reason_code="ARCHIVE_MEMBER_COUNT_EXCEEDS_CAP",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
            )

        text_members = [
            info for info in file_members if info.filename.lower().endswith(".txt")
        ]
        if len(text_members) != 1:
            return _blocked(
                authorization,
                reason_code="AMBIGUOUS_TEXT_MEMBER_LAYOUT",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
                selected_text_member_present=False,
            )

        selected = text_members[0]
        if selected.file_size > authorization.max_uncompressed_bytes:
            return _blocked(
                authorization,
                reason_code="UNCOMPRESSED_TEXT_EXCEEDS_CAP",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
                selected_text_member_present=True,
                selected_member_uncompressed_bytes=selected.file_size,
            )

        documented_header = NY_DOCUMENTED_DELIMITER.join(NY_DOCUMENTED_FIELDS).encode(
            "ascii"
        )
        expected_field_count = len(NY_DOCUMENTED_FIELDS)
        record_count = 0
        property_type_ascii_count = 0
        header_state: Literal[
            "EXACT_DOCUMENTED_HEADER",
            "UTF8_BOM_DOCUMENTED_HEADER",
            "NO_HEADER_OBSERVED",
        ] = "NO_HEADER_OBSERVED"
        observed_data_field_count: int | None = None
        first_nonblank_seen = False

        with archive.open(selected, "r") as stream:
            for raw_line in stream:
                line = raw_line.rstrip(b"\r\n")
                if not line:
                    continue

                if not first_nonblank_seen:
                    first_nonblank_seen = True
                    if line == documented_header:
                        header_state = "EXACT_DOCUMENTED_HEADER"
                        continue
                    if line.removeprefix(b"\xef\xbb\xbf") == documented_header:
                        header_state = "UTF8_BOM_DOCUMENTED_HEADER"
                        continue

                fields = line.split(b"|")
                field_count = len(fields)
                if observed_data_field_count is None:
                    observed_data_field_count = field_count

                if field_count != expected_field_count:
                    return _blocked(
                        authorization,
                        reason_code="UNEXPECTED_DATA_FIELD_COUNT",
                        archive_byte_count=archive_byte_count,
                        archive_member_count=member_count,
                        selected_text_member_present=True,
                        selected_member_uncompressed_bytes=selected.file_size,
                    )

                property_type_raw = fields[NY_PROPERTY_TYPE_CODE_INDEX]
                if property_type_raw and property_type_raw.isalnum():
                    property_type_ascii_count += 1

                record_count += 1

        if not first_nonblank_seen:
            return _blocked(
                authorization,
                reason_code="TEXT_MEMBER_EMPTY",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
                selected_text_member_present=True,
                selected_member_uncompressed_bytes=selected.file_size,
            )

        return NyOwnerNameSchemaDiscoveryResult(
            status="DISCOVERED",
            reason_code="DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED",
            approval_id=authorization.approval_id,
            archive_byte_count=archive_byte_count,
            archive_member_count=member_count,
            selected_text_member_present=True,
            selected_member_uncompressed_bytes=selected.file_size,
            observed_delimiter="|",
            observed_data_field_count=observed_data_field_count,
            observed_header_state=header_state,
            physical_header_names=(
                NY_DOCUMENTED_FIELDS
                if header_state
                in {"EXACT_DOCUMENTED_HEADER", "UTF8_BOM_DOCUMENTED_HEADER"}
                else ()
            ),
            aggregate_complete_record_count=record_count,
            property_type_ascii_record_count=property_type_ascii_count,
            nature_of_property_mapping_state=(
                "DETERMINISTIC_DOCUMENTED_POSITION_REQUIRES_LATER_CODE_VALIDATION"
            ),
            encoding_state="NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY",
        )
