"""Bounded memory-only schema discovery for the NY OSC Owner Name File.

This module intentionally accepts archive bytes only as an in-memory function argument.
Raw archive bytes and owner-row values are never part of the serializable contracts.
"""

from __future__ import annotations

import io
import zipfile
from dataclasses import dataclass
from typing import BinaryIO, Iterator, Literal

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
_UTF8_BOM = b"\xef\xbb\xbf"


def _is_ascii_space(value: int) -> bool:
    return value in {9, 10, 11, 12, 13, 32}


def _is_ascii_alnum(value: int) -> bool:
    return (
        ord("0") <= value <= ord("9")
        or ord("A") <= value <= ord("Z")
        or ord("a") <= value <= ord("z")
    )


def _ascii_lower(value: int) -> int:
    if ord("A") <= value <= ord("Z"):
        return value + 32
    return value


class _NormalizedAsciiAlnumMatcher:
    """Validate a wrapped ASCII token without retaining its bytes."""

    def __init__(self) -> None:
        self._state = "LEADING"
        self._wrapper: int | None = None
        self._seen_alnum = False
        self._valid = True

    def consume(self, value: int) -> None:
        if not self._valid:
            return

        if self._state == "LEADING":
            if _is_ascii_space(value):
                return
            if value in {ord('"'), ord("'")}:
                self._wrapper = value
                self._state = "INNER_LEADING"
                return
            if _is_ascii_alnum(value):
                self._seen_alnum = True
                self._state = "TOKEN"
                return
            self._valid = False
            return

        if self._state == "INNER_LEADING":
            if _is_ascii_space(value):
                return
            if _is_ascii_alnum(value):
                self._seen_alnum = True
                self._state = "TOKEN"
                return
            self._valid = False
            return

        if self._state == "TOKEN":
            if _is_ascii_alnum(value):
                self._seen_alnum = True
                return
            if self._wrapper is not None and value == self._wrapper:
                self._state = "CLOSED"
                return
            if _is_ascii_space(value):
                self._state = (
                    "INNER_TRAILING"
                    if self._wrapper is not None
                    else "TRAILING"
                )
                return
            self._valid = False
            return

        if self._state == "INNER_TRAILING":
            if _is_ascii_space(value):
                return
            if value == self._wrapper:
                self._state = "CLOSED"
                return
            self._valid = False
            return

        if self._state in {"TRAILING", "CLOSED"}:
            if not _is_ascii_space(value):
                self._valid = False
            return

        self._valid = False

    def matches(self) -> bool:
        if not self._valid or not self._seen_alnum:
            return False
        if self._wrapper is None:
            return self._state in {"TOKEN", "TRAILING"}
        return self._state == "CLOSED"


class _ExpectedHeaderFieldMatcher:
    """Incrementally match one normalized documented header field."""

    def __init__(self, expected: bytes, *, allow_utf8_bom: bool) -> None:
        self._expected = expected.lower()
        self._expected_index = 0
        self._state = "LEADING"
        self._wrapper: int | None = None
        self._valid = True
        self._allow_utf8_bom = allow_utf8_bom

    def consume(self, value: int) -> None:
        if not self._valid:
            return

        if self._state == "BOM_2":
            if value == _UTF8_BOM[1]:
                self._state = "BOM_3"
            else:
                self._valid = False
            return

        if self._state == "BOM_3":
            if value == _UTF8_BOM[2]:
                self._state = "LEADING"
                self._allow_utf8_bom = False
            else:
                self._valid = False
            return

        if self._state == "LEADING":
            if _is_ascii_space(value):
                return
            if self._allow_utf8_bom and value == _UTF8_BOM[0]:
                self._state = "BOM_2"
                return
            self._allow_utf8_bom = False
            if value in {ord('"'), ord("'")}:
                self._wrapper = value
                self._state = "INNER_LEADING"
                return
            self._consume_expected(value)
            return

        if self._state == "INNER_LEADING":
            if _is_ascii_space(value):
                return
            self._consume_expected(value)
            return

        if self._state == "MATCHING":
            self._consume_expected(value)
            return

        if self._state == "AFTER_EXPECTED":
            if self._wrapper is not None and value == self._wrapper:
                self._state = "CLOSED"
                return
            if _is_ascii_space(value):
                return
            self._valid = False
            return

        if self._state == "CLOSED":
            if not _is_ascii_space(value):
                self._valid = False
            return

        self._valid = False

    def _consume_expected(self, value: int) -> None:
        if (
            self._expected_index >= len(self._expected)
            or _ascii_lower(value) != self._expected[self._expected_index]
        ):
            self._valid = False
            return

        self._expected_index += 1
        self._state = (
            "AFTER_EXPECTED"
            if self._expected_index == len(self._expected)
            else "MATCHING"
        )

    def matches(self) -> bool:
        if not self._valid or self._expected_index != len(self._expected):
            return False
        if self._wrapper is None:
            return self._state == "AFTER_EXPECTED"
        return self._state == "CLOSED"


@dataclass(frozen=True)
class _QuotedPipeRecordShape:
    field_count: int
    property_type_ascii: bool
    exact_documented_header: bool
    normalized_documented_header: bool
    observed_delimiter: Literal["|"] | None


class _MalformedQuotedRecordError(ValueError):
    def __init__(self, observed_delimiter: Literal["|"] | None) -> None:
        super().__init__("quoted record reached EOF before its closing quote")
        self.observed_delimiter = observed_delimiter


class _LogicalRecordScanner:
    """Collect structural state for one record without retaining owner fields."""

    def __init__(self, *, track_header: bool) -> None:
        self.track_header = track_header
        self.field_index = 0
        self.field_count = 1
        self.field_has_nonspace = False
        self.has_content = False
        self.has_pipe = False
        self._property_matcher = _NormalizedAsciiAlnumMatcher()
        self._property_type_ascii = False
        self._property_field_finished = False
        self._header_matches = True
        self._header_matcher = self._new_header_matcher()
        self._documented_header = NY_DOCUMENTED_DELIMITER.join(
            NY_DOCUMENTED_FIELDS
        ).encode("ascii")
        self._exact_header_index = 0
        self._exact_header_matches = track_header

    @property
    def observed_delimiter(self) -> Literal["|"] | None:
        return "|" if self.has_pipe else None

    def consume_field_byte(self, value: int) -> None:
        self.has_content = True
        if value == ord("|"):
            self.has_pipe = True
        if not _is_ascii_space(value):
            self.field_has_nonspace = True

        self._consume_exact_header_byte(value)
        if self._header_matcher is not None:
            self._header_matcher.consume(value)
        if self.field_index == NY_PROPERTY_TYPE_CODE_INDEX:
            self._property_matcher.consume(value)

    def consume_delimiter(self) -> None:
        self.has_content = True
        self.has_pipe = True
        self._consume_exact_header_byte(ord("|"))
        self._finish_field()
        self.field_index += 1
        self.field_count += 1
        self.field_has_nonspace = False
        self._header_matcher = self._new_header_matcher()

    def finish(self) -> _QuotedPipeRecordShape:
        self._finish_field()
        return _QuotedPipeRecordShape(
            field_count=self.field_count,
            property_type_ascii=(
                self._property_field_finished and self._property_type_ascii
            ),
            exact_documented_header=(
                self.track_header
                and self._exact_header_matches
                and self._exact_header_index == len(self._documented_header)
            ),
            normalized_documented_header=(
                self.track_header
                and self._header_matches
                and self.field_count == len(NY_DOCUMENTED_FIELDS)
            ),
            observed_delimiter=self.observed_delimiter,
        )

    def _new_header_matcher(self) -> _ExpectedHeaderFieldMatcher | None:
        if not self.track_header or self.field_index >= len(NY_DOCUMENTED_FIELDS):
            return None
        return _ExpectedHeaderFieldMatcher(
            NY_DOCUMENTED_FIELDS[self.field_index].encode("ascii"),
            allow_utf8_bom=self.field_index == 0,
        )

    def _consume_exact_header_byte(self, value: int) -> None:
        if not self._exact_header_matches:
            return
        if (
            self._exact_header_index >= len(self._documented_header)
            or value != self._documented_header[self._exact_header_index]
        ):
            self._exact_header_matches = False
            return
        self._exact_header_index += 1

    def _finish_field(self) -> None:
        if self._header_matcher is None or not self._header_matcher.matches():
            self._header_matches = False
        if (
            self.field_index == NY_PROPERTY_TYPE_CODE_INDEX
            and not self._property_field_finished
        ):
            self._property_type_ascii = self._property_matcher.matches()
            self._property_field_finished = True


class _QuotedPipeStreamScanner:
    """Scan fixed-size byte chunks into logical records with bounded state."""

    def __init__(self) -> None:
        self._track_header = True
        self._scanner = _LogicalRecordScanner(track_header=True)
        self._in_quotes = False
        self._pending_quote = False
        self._pending_cr = False

    @property
    def observed_delimiter(self) -> Literal["|"] | None:
        return self._scanner.observed_delimiter

    def consume(self, value: int) -> _QuotedPipeRecordShape | None:
        if self._pending_quote:
            self._scanner.consume_field_byte(ord('"'))
            self._pending_quote = False
            if value == ord('"'):
                self._scanner.consume_field_byte(value)
                return None
            self._in_quotes = False

        if self._pending_cr:
            self._pending_cr = False
            if value == ord("\n"):
                if self._in_quotes:
                    self._scanner.consume_field_byte(ord("\r"))
                    self._scanner.consume_field_byte(value)
                    return None
                return self._finish_boundary()
            self._scanner.consume_field_byte(ord("\r"))

        if value == ord("\r"):
            self._pending_cr = True
            return None

        if value == ord("\n"):
            if self._in_quotes:
                self._scanner.consume_field_byte(value)
                return None
            return self._finish_boundary()

        if value == ord('"'):
            if self._in_quotes:
                self._pending_quote = True
                return None

            can_open_quote = not self._scanner.field_has_nonspace
            self._scanner.consume_field_byte(value)
            if can_open_quote:
                self._in_quotes = True
            return None

        if value == ord("|") and not self._in_quotes:
            self._scanner.consume_delimiter()
            return None

        self._scanner.consume_field_byte(value)
        return None

    def finish(self) -> _QuotedPipeRecordShape | None:
        if self._pending_quote:
            self._scanner.consume_field_byte(ord('"'))
            self._pending_quote = False
            self._in_quotes = False

        if self._pending_cr:
            self._scanner.consume_field_byte(ord("\r"))
            self._pending_cr = False

        if self._in_quotes:
            raise _MalformedQuotedRecordError(self.observed_delimiter)

        if self._scanner.has_content:
            return self._finish_boundary()
        return None

    def _finish_boundary(self) -> _QuotedPipeRecordShape | None:
        if not self._scanner.has_content:
            return None

        record = self._scanner.finish()
        self._track_header = False
        self._scanner = _LogicalRecordScanner(track_header=self._track_header)
        return record


def _iter_quoted_pipe_record_shapes(
    stream: BinaryIO,
) -> Iterator[_QuotedPipeRecordShape]:
    """Yield logical record shapes without retaining owner fields or whole records."""

    scanner = _QuotedPipeStreamScanner()
    while chunk := stream.read(64 * 1024):
        for value in chunk:
            record = scanner.consume(value)
            if record is not None:
                yield record

    final_record = scanner.finish()
    if final_record is not None:
        yield final_record


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
        "NORMALIZED_DOCUMENTED_HEADER",
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
    observed_delimiter: Literal["|"] | None = None,
    observed_data_field_count: int | None = None,
    observed_header_state: Literal[
        "EXACT_DOCUMENTED_HEADER",
        "NORMALIZED_DOCUMENTED_HEADER",
        "NO_HEADER_OBSERVED",
        "NOT_EVALUATED",
    ] = "NOT_EVALUATED",
    physical_header_names: tuple[str, ...] = (),
    aggregate_complete_record_count: int | None = None,
    property_type_ascii_record_count: int | None = None,
) -> NyOwnerNameSchemaDiscoveryResult:
    return NyOwnerNameSchemaDiscoveryResult(
        status="BLOCKED",
        reason_code=reason_code,
        approval_id=auth.approval_id,
        archive_byte_count=archive_byte_count,
        archive_member_count=archive_member_count,
        selected_text_member_present=selected_text_member_present,
        selected_member_uncompressed_bytes=selected_member_uncompressed_bytes,
        observed_delimiter=observed_delimiter,
        observed_data_field_count=observed_data_field_count,
        observed_header_state=observed_header_state,
        physical_header_names=physical_header_names,
        aggregate_complete_record_count=aggregate_complete_record_count,
        property_type_ascii_record_count=property_type_ascii_record_count,
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

        expected_field_count = len(NY_DOCUMENTED_FIELDS)
        record_count = 0
        property_type_ascii_count = 0
        header_state: Literal[
            "EXACT_DOCUMENTED_HEADER",
            "NORMALIZED_DOCUMENTED_HEADER",
            "NO_HEADER_OBSERVED",
        ] = "NO_HEADER_OBSERVED"
        observed_data_field_count: int | None = None
        first_nonblank_seen = False

        try:
            with archive.open(selected, "r") as stream:
                for record in _iter_quoted_pipe_record_shapes(stream):
                    if not first_nonblank_seen:
                        first_nonblank_seen = True
                        if record.exact_documented_header:
                            header_state = "EXACT_DOCUMENTED_HEADER"
                            continue
                        if record.normalized_documented_header:
                            header_state = "NORMALIZED_DOCUMENTED_HEADER"
                            continue

                    field_count = record.field_count
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
                            observed_delimiter=record.observed_delimiter,
                            observed_data_field_count=field_count,
                            observed_header_state=header_state,
                            physical_header_names=(
                                NY_DOCUMENTED_FIELDS
                                if header_state
                                in {
                                    "EXACT_DOCUMENTED_HEADER",
                                    "NORMALIZED_DOCUMENTED_HEADER",
                                }
                                else ()
                            ),
                            aggregate_complete_record_count=record_count,
                            property_type_ascii_record_count=property_type_ascii_count,
                        )

                    if not record.property_type_ascii:
                        return _blocked(
                            authorization,
                            reason_code="PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED",
                            archive_byte_count=archive_byte_count,
                            archive_member_count=member_count,
                            selected_text_member_present=True,
                            selected_member_uncompressed_bytes=selected.file_size,
                            observed_delimiter=record.observed_delimiter,
                            observed_data_field_count=field_count,
                            observed_header_state=header_state,
                            physical_header_names=(
                                NY_DOCUMENTED_FIELDS
                                if header_state
                                in {
                                    "EXACT_DOCUMENTED_HEADER",
                                    "NORMALIZED_DOCUMENTED_HEADER",
                                }
                                else ()
                            ),
                            aggregate_complete_record_count=record_count,
                            property_type_ascii_record_count=property_type_ascii_count,
                        )

                    property_type_ascii_count += 1
                    record_count += 1
        except _MalformedQuotedRecordError as exc:
            return _blocked(
                authorization,
                reason_code="MALFORMED_QUOTED_RECORD",
                archive_byte_count=archive_byte_count,
                archive_member_count=member_count,
                selected_text_member_present=True,
                selected_member_uncompressed_bytes=selected.file_size,
                observed_delimiter=exc.observed_delimiter,
                observed_header_state=header_state,
                physical_header_names=(
                    NY_DOCUMENTED_FIELDS
                    if header_state
                    in {
                        "EXACT_DOCUMENTED_HEADER",
                        "NORMALIZED_DOCUMENTED_HEADER",
                    }
                    else ()
                ),
                aggregate_complete_record_count=record_count,
                property_type_ascii_record_count=property_type_ascii_count,
            )

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
                if header_state in {
                    "EXACT_DOCUMENTED_HEADER",
                    "NORMALIZED_DOCUMENTED_HEADER",
                }
                else ()
            ),
            aggregate_complete_record_count=record_count,
            property_type_ascii_record_count=property_type_ascii_count,
            nature_of_property_mapping_state=(
                "DETERMINISTIC_DOCUMENTED_POSITION_REQUIRES_LATER_CODE_VALIDATION"
            ),
            encoding_state="NOT_EVALUATED_BYTE_LEVEL_DISCOVERY_ONLY",
        )
