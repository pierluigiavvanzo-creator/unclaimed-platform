"""Bounded local-file runner for NY MVP-1 real P1 targetability.

No network client exists in this module. The caller must provide a local archive
plus a validated single-use authorization bundle. Owner PII is never returned.
"""

from __future__ import annotations

import shutil
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Protocol
from uuid import NAMESPACE_URL, UUID, uuid5

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from unclaimed_platform.domain.ny_mvp1_p1_authorization import P1ExecutionAuthorization
from unclaimed_platform.domain.ny_mvp1_targetable_opportunity import (
    SyntheticTargetabilityEvidence,
    TargetabilityDecision,
    classify_targetability,
)

SOURCE_ID = "ny.osc.unclaimed_funds.owner_name_file"
SELECTION_RULE_VERSION = "2.0.0"
SELECTION_BASIS = "PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER"
DOCUMENTED_FIELD_COUNT = 14
DOCUMENTED_PIPE_COUNT = 13
CHUNK_BYTES = 64 * 1024
MAX_BUFFERED_FIELD_BYTES = 4096

ServiceNeedState = Literal["UNKNOWN", "LOW_EVIDENCE", "MATERIAL_EVIDENCE"]
ResolvabilityState = Literal["UNKNOWN", "EASY", "BOUNDED", "UNBOUNDED"]
EstatePathState = Literal["NOT_EVALUATED", "NO_EVIDENCE", "EVIDENCE_PRESENT"]
RepresentativePathState = Literal[
    "NOT_EVALUATED",
    "IDENTIFIED",
    "BOUNDED_DISCOVERABLE",
    "NOT_BOUNDED",
]
FrictionLane = Literal["F0", "F1", "F2", "F3"]


class RealP1SelectionSummary(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    selection_rule_version: Literal["2.0.0"] = SELECTION_RULE_VERSION
    selection_basis: Literal[
        "PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER"
    ] = SELECTION_BASIS
    total_records: int = Field(ge=0)
    structurally_conforming_records: int = Field(ge=0)
    structurally_deferred_records: int = Field(ge=0)
    eligible_records_count: int = Field(ge=0)
    selected_source_record_ordinal: int | None = Field(default=None, ge=1)
    selected_holder_report_year: int | None = Field(default=None, ge=1)
    owner_pii_decoded_for_ranking: Literal[False] = False
    owner_pii_buffered_for_ranking: Literal[False] = False
    property_id_value_persisted: Literal[False] = False
    value_prediction_performed: Literal[False] = False
    persistence_interpretation: Literal[
        "REPORT_YEAR_IS_PERSISTENCE_SIGNAL_ONLY_NOT_AWARENESS_VALUE_DEATH_OR_CONTACTABILITY"
    ] = "REPORT_YEAR_IS_PERSISTENCE_SIGNAL_ONLY_NOT_AWARENESS_VALUE_DEATH_OR_CONTACTABILITY"

    @model_validator(mode="after")
    def validate_counts(self) -> "RealP1SelectionSummary":
        if (
            self.structurally_conforming_records + self.structurally_deferred_records
            != self.total_records
        ):
            raise ValueError("structural counts do not sum")
        if self.eligible_records_count == 0:
            if self.selected_source_record_ordinal is not None:
                raise ValueError("zero eligible records cannot have selection")
            if self.selected_holder_report_year is not None:
                raise ValueError("zero eligible records cannot have report year")
        else:
            if self.selected_source_record_ordinal is None:
                raise ValueError("eligible records require selected ordinal")
            if self.selected_holder_report_year is None:
                raise ValueError("eligible records require selected report year")
        return self


class RealP1TargetabilityEvidence(BaseModel):
    """Non-PII evidence returned by an explicitly bound L2-A provider."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    service_need_state: ServiceNeedState
    resolvability_state: ResolvabilityState
    estate_path_state: EstatePathState = "NOT_EVALUATED"
    representative_path_state: RepresentativePathState = "NOT_EVALUATED"
    friction_lane: FrictionLane | None = None
    evidence_refs: tuple[str, ...] = Field(min_length=1)
    manual_research_seconds: int = Field(ge=0)
    external_cash_spend_cents: Literal[0] = 0
    targetability_decision_cost_state: Literal[
        "NOT_MEASURED", "MEASURING", "MEASURED"
    ] = "MEASURING"
    targetability_decision_cost_cents: int | None = Field(default=None, ge=0)
    source_type_categories: tuple[
        Literal[
            "PUBLIC_OFFICIAL",
            "PUBLIC_RECORD_INDEX",
            "PUBLIC_WEB",
            "INTERNAL_DERIVED",
        ],
        ...,
    ] = ()
    non_pii_source_domains: tuple[str, ...] = ()
    awareness_state: Literal["UNKNOWN_UNTIL_OUTREACH"] = "UNKNOWN_UNTIL_OUTREACH"
    owner_pii_included: Literal[False] = False
    value_evidence_used: Literal[False] = False

    @field_validator("evidence_refs")
    @classmethod
    def validate_opaque_refs(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        for value in values:
            if not value or any(char.isspace() for char in value):
                raise ValueError("evidence refs must be opaque non-whitespace tokens")
            if "?" in value or "#" in value:
                raise ValueError("evidence refs cannot contain query/fragment material")
        return values

    @field_validator("non_pii_source_domains")
    @classmethod
    def validate_domains(cls, values: tuple[str, ...]) -> tuple[str, ...]:
        for value in values:
            if (
                not value
                or "/" in value
                or "?" in value
                or "#" in value
                or "@" in value
                or any(char.isspace() for char in value)
            ):
                raise ValueError("source domains must not contain paths, queries or PII")
        return values

    @model_validator(mode="after")
    def validate_cost_state(self) -> "RealP1TargetabilityEvidence":
        if self.targetability_decision_cost_state == "MEASURED":
            if self.targetability_decision_cost_cents is None:
                raise ValueError("MEASURED targetability cost requires cents")
        elif self.targetability_decision_cost_cents is not None:
            raise ValueError("cost cents require MEASURED targetability state")
        return self


@dataclass(slots=True, repr=False)
class TransientSelectedCandidate:
    """Ephemeral PII container. It must never be serialized or persisted."""

    property_id: bytes
    property_type_code: bytes
    property_owner_count: bytes
    owner_name: bytes
    holder_name: bytes
    holder_report_year: bytes
    address_fields: tuple[bytes, ...]

    def __repr__(self) -> str:
        return "TransientSelectedCandidate(<redacted>)"


class L2ATargetabilityProvider(Protocol):
    provider_id: str

    def evaluate(
        self,
        candidate: TransientSelectedCandidate,
    ) -> RealP1TargetabilityEvidence: ...


class RealP1EconomicLedger(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    case_id: UUID
    source_id: Literal["ny.osc.unclaimed_funds.owner_name_file"] = SOURCE_ID
    source_snapshot_ref: str = Field(min_length=1)
    source_record_ordinal: int = Field(ge=1)
    selection_rule_version: Literal["2.0.0"] = SELECTION_RULE_VERSION
    holder_report_year: int = Field(ge=1)
    persistence_signal: Literal["OLDER_REPORT_YEAR_SELECTED_WITHOUT_VALUE_INFERENCE"] = (
        "OLDER_REPORT_YEAR_SELECTED_WITHOUT_VALUE_INFERENCE"
    )
    current_discovery_stage: Literal["L1", "L2A"]
    service_need_state: ServiceNeedState
    resolvability_state: ResolvabilityState
    estate_path_state: EstatePathState
    representative_path_state: RepresentativePathState
    awareness_state: Literal["UNKNOWN_UNTIL_OUTREACH"] = "UNKNOWN_UNTIL_OUTREACH"
    targetability_state: Literal[
        "NOT_EVALUATED",
        "CLASSIFIED",
        "UNRESOLVED_REQUIRES_L2",
        "STOPPED",
    ]
    targetability_class: str | None = None
    friction_lane: FrictionLane | None = None
    targetability_decision_cost_state: Literal[
        "NOT_MEASURED", "MEASURING", "MEASURED"
    ]
    targetability_decision_cost_cents: int | None = Field(default=None, ge=0)
    pre_value_discovery_cost_state: Literal["MEASURING"] = "MEASURING"
    measured_machine_and_data_cost_cents: int | None = Field(default=None, ge=0)
    measured_human_seconds: int = Field(ge=0)
    external_cash_spend_cents: Literal[0] = 0
    value_evidence_state: Literal["UNKNOWN_PRE_CLAIM_REVIEW"] = (
        "UNKNOWN_PRE_CLAIM_REVIEW"
    )
    legal_privacy_scope_ref: Literal[
        "sources/proposals/ny_mvp1_real_p1_targetability_execution_scope.v1.json"
    ] = "sources/proposals/ny_mvp1_real_p1_targetability_execution_scope.v1.json"
    authorization_refs: tuple[str, ...] = Field(min_length=4)
    evidence_refs: tuple[str, ...] = ()
    stop_reason: str = Field(min_length=1)
    disposal_result: Literal["LOGICAL_DELETION_COMPLETED", "LOGICAL_DELETION_FAILED"]
    direct_owner_pii_included: Literal[False] = False
    owner_name_persisted: Literal[False] = False
    property_id_persisted: Literal[False] = False
    address_persisted: Literal[False] = False
    holder_name_persisted: Literal[False] = False
    raw_row_persisted: Literal[False] = False
    no_commercial_decision: Literal[True] = True


class RealP1RunSafety(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    direct_network_client_used: Literal[False] = False
    owner_pii_returned: Literal[False] = False
    owner_pii_persisted: Literal[False] = False
    raw_row_persisted: Literal[False] = False
    beneficiary_matching_performed: Literal[False] = False
    genealogy_performed: Literal[False] = False
    outreach_performed: Literal[False] = False
    value_research_performed: Literal[False] = False
    fee_agreement_performed: Literal[False] = False
    representation_performed: Literal[False] = False
    claim_activity_performed: Literal[False] = False
    physical_secure_erasure_guaranteed: Literal[False] = False


class RealP1RunResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    contract_version: Literal["1.0.0"] = "1.0.0"
    execution_mode: Literal["AUTHORIZED_REAL_LOCAL_FILE_ONCE"] = (
        "AUTHORIZED_REAL_LOCAL_FILE_ONCE"
    )
    status: Literal["COMPLETED", "BLOCKED"]
    reason_code: Literal[
        "L1_COMPLETED_L2A_NOT_AUTHORIZED",
        "L2A_TARGETABILITY_CLASSIFIED",
        "L2A_TARGETABILITY_UNRESOLVED",
        "NO_ELIGIBLE_SINGLE_OWNER_IN03_WITH_REPORT_YEAR",
        "SELECTED_RECORD_SECOND_PASS_MISMATCH",
        "L2A_PROVIDER_REQUIRED",
        "L2A_PROVIDER_BINDING_MISMATCH",
        "L2A_MANUAL_RESEARCH_CAP_EXCEEDED",
        "SOURCE_ARCHIVE_BOUNDARY_FAILED",
        "EXECUTION_ERROR",
        "DISPOSAL_FAILED",
    ]
    runner_checkpoint: str = Field(pattern=r"^[0-9a-f]{40}$")
    source_snapshot_ref: str = Field(min_length=1)
    fresh_preflight_receipt_ref: str = Field(min_length=1)
    selection: RealP1SelectionSummary | None
    economic_case_ledger: RealP1EconomicLedger | None
    targetability: TargetabilityDecision | None
    archive_byte_count: int = Field(ge=0)
    local_file_deleted: bool
    logical_deletion_only: Literal[True] = True
    safety: RealP1RunSafety = RealP1RunSafety()
    execution_authorization_consumed: Literal[True] = True
    reusable: Literal[False] = False
    retry_authorized: Literal[False] = False


class _SelectionScanner:
    MAX_SMALL_FIELD_BYTES = 16

    def __init__(self) -> None:
        self.total = 0
        self.conforming = 0
        self.deferred = 0
        self.eligible = 0
        self.best: tuple[int, int] | None = None
        self._pipe_count = 0
        self._field_index = 0
        self._property_id_non_ws = False
        self._property_type = bytearray()
        self._owner_count = bytearray()
        self._report_year = bytearray()
        self._overflow = False
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

    def _append_small(self, target: bytearray, value: int) -> None:
        if len(target) >= self.MAX_SMALL_FIELD_BYTES:
            self._overflow = True
            return
        target.append(value)

    def _consume_data(self, value: int) -> None:
        self._has_data = True
        if value == 124:
            self._pipe_count += 1
            self._field_index += 1
            return
        if self._field_index == 0:
            if value not in {9, 32}:
                self._property_id_non_ws = True
        elif self._field_index == 1:
            self._append_small(self._property_type, value)
        elif self._field_index == 3:
            self._append_small(self._owner_count, value)
        elif self._field_index == 13:
            self._append_small(self._report_year, value)

    def _finish_record(self) -> None:
        if not self._has_data:
            self._reset()
            return
        self.total += 1
        ordinal = self.total
        if self._pipe_count != DOCUMENTED_PIPE_COUNT:
            self.deferred += 1
            self._reset()
            return
        self.conforming += 1
        year = self._positive_decimal(self._report_year)
        eligible = (
            not self._overflow
            and self._property_type == b"IN03"
            and self._owner_count == b"1"
            and self._property_id_non_ws
            and year is not None
        )
        if eligible:
            assert year is not None
            self.eligible += 1
            key = (year, ordinal)
            if self.best is None or key < self.best:
                self.best = key
        self._reset()

    @staticmethod
    def _positive_decimal(value: bytearray) -> int | None:
        if not value:
            return None
        raw = bytes(value)
        if not all(48 <= item <= 57 for item in raw):
            return None
        parsed = int(raw.decode("ascii"))
        return parsed if parsed > 0 else None

    def _reset(self) -> None:
        self._pipe_count = 0
        self._field_index = 0
        self._property_id_non_ws = False
        self._property_type = bytearray()
        self._owner_count = bytearray()
        self._report_year = bytearray()
        self._overflow = False
        self._has_data = False


class _SelectedRecordCollector:
    L1_FIELDS = {0, 1, 3, 4, 12, 13}
    ADDRESS_FIELDS = {5, 6, 7, 8, 9, 10, 11}

    def __init__(self, target_ordinal: int, include_address: bool) -> None:
        self.target_ordinal = target_ordinal
        self.include_address = include_address
        self.current_ordinal = 0
        self.selected: dict[int, bytes] | None = None
        self._pipe_count = 0
        self._field_index = 0
        self._has_data = False
        self._pending_cr = False
        self._buffers: dict[int, bytearray] = {}
        self._overflow = False

    def consume(self, value: int) -> None:
        if self.selected is not None:
            return
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
        if self.selected is not None:
            return
        if self._pending_cr:
            self._pending_cr = False
            self._finish_record()
        elif self._has_data:
            self._finish_record()

    def _should_collect(self, field_index: int) -> bool:
        if field_index in self.L1_FIELDS:
            return True
        return self.include_address and field_index in self.ADDRESS_FIELDS

    def _consume_data(self, value: int) -> None:
        self._has_data = True
        if value == 124:
            self._pipe_count += 1
            self._field_index += 1
            return
        if self.current_ordinal + 1 != self.target_ordinal:
            return
        if not self._should_collect(self._field_index):
            return
        target = self._buffers.setdefault(self._field_index, bytearray())
        if len(target) >= MAX_BUFFERED_FIELD_BYTES:
            self._overflow = True
            return
        target.append(value)

    def _finish_record(self) -> None:
        if not self._has_data:
            self._reset_record()
            return
        self.current_ordinal += 1
        if self.current_ordinal == self.target_ordinal:
            if self._pipe_count != DOCUMENTED_PIPE_COUNT or self._overflow:
                self.selected = {}
            else:
                self.selected = {
                    index: bytes(value) for index, value in self._buffers.items()
                }
        self._reset_record()

    def _reset_record(self) -> None:
        self._pipe_count = 0
        self._field_index = 0
        self._has_data = False
        self._buffers = {}
        self._overflow = False


def _archive_member(
    archive_path: Path,
    authorization: P1ExecutionAuthorization,
) -> tuple[int, zipfile.ZipInfo]:
    if archive_path.name not in {"FINDERS.zip", "FINDERS.ZIP", "NYSFINDERS.ZIP"}:
        raise ValueError("unexpected local archive filename")
    archive_size = archive_path.stat().st_size
    if archive_size > authorization.max_download_bytes:
        raise ValueError("archive exceeds bounded download cap")
    if not zipfile.is_zipfile(archive_path):
        raise ValueError("not a ZIP archive")
    with zipfile.ZipFile(archive_path) as archive:
        members = [info for info in archive.infolist() if not info.is_dir()]
        if len(members) != authorization.max_archive_members:
            raise ValueError("archive member count mismatch")
        text_members = [
            info for info in members if info.filename.lower().endswith(".txt")
        ]
        if len(text_members) != 1:
            raise ValueError("expected exactly one TXT member")
        selected = text_members[0]
        if selected.file_size > authorization.max_uncompressed_bytes:
            raise ValueError("uncompressed TXT exceeds bounded cap")
        return archive_size, selected


def _scan_selection(
    archive_path: Path,
    authorization: P1ExecutionAuthorization,
) -> RealP1SelectionSummary:
    _, member = _archive_member(archive_path, authorization)
    scanner = _SelectionScanner()
    with zipfile.ZipFile(archive_path) as archive, archive.open(member, "r") as stream:
        while chunk := stream.read(CHUNK_BYTES):
            for value in chunk:
                scanner.consume(value)
        scanner.finish()
    selected_year: int | None = None
    selected_ordinal: int | None = None
    if scanner.best is not None:
        selected_year, selected_ordinal = scanner.best
    return RealP1SelectionSummary(
        total_records=scanner.total,
        structurally_conforming_records=scanner.conforming,
        structurally_deferred_records=scanner.deferred,
        eligible_records_count=scanner.eligible,
        selected_source_record_ordinal=selected_ordinal,
        selected_holder_report_year=selected_year,
    )


def _materialize_selected(
    archive_path: Path,
    authorization: P1ExecutionAuthorization,
    selection: RealP1SelectionSummary,
) -> TransientSelectedCandidate | None:
    ordinal = selection.selected_source_record_ordinal
    selected_year = selection.selected_holder_report_year
    if ordinal is None or selected_year is None:
        return None
    _, member = _archive_member(archive_path, authorization)
    collector = _SelectedRecordCollector(
        ordinal,
        include_address=authorization.l2a_enabled,
    )
    with zipfile.ZipFile(archive_path) as archive, archive.open(member, "r") as stream:
        while chunk := stream.read(CHUNK_BYTES):
            for value in chunk:
                collector.consume(value)
                if collector.selected is not None:
                    break
            if collector.selected is not None:
                break
        collector.finish()
    fields = collector.selected
    if not fields:
        return None
    property_id = fields.get(0, b"")
    property_type = fields.get(1, b"")
    owner_count = fields.get(3, b"")
    owner_name = fields.get(4, b"")
    holder_name = fields.get(12, b"")
    report_year = fields.get(13, b"")
    if not property_id.strip() or property_type != b"IN03" or owner_count != b"1":
        return None
    if not owner_name.strip():
        return None
    if not report_year or not all(48 <= item <= 57 for item in report_year):
        return None
    if int(report_year.decode("ascii")) != selected_year:
        return None
    address_fields: tuple[bytes, ...] = ()
    if authorization.l2a_enabled:
        address_fields = tuple(fields.get(index, b"") for index in range(5, 12))
    return TransientSelectedCandidate(
        property_id=property_id,
        property_type_code=property_type,
        property_owner_count=owner_count,
        owner_name=owner_name,
        holder_name=holder_name,
        holder_report_year=report_year,
        address_fields=address_fields,
    )


def _case_id(
    authorization: P1ExecutionAuthorization,
    selection: RealP1SelectionSummary,
) -> UUID:
    assert selection.selected_source_record_ordinal is not None
    identity = "|".join(
        (
            SOURCE_ID,
            authorization.source_snapshot_ref,
            str(selection.selected_source_record_ordinal),
            "IN03",
            SELECTION_RULE_VERSION,
        )
    )
    return uuid5(NAMESPACE_URL, identity)


def _authorization_refs(
    authorization: P1ExecutionAuthorization,
) -> tuple[str, ...]:
    refs = [
        authorization.local_file_approval_ref,
        authorization.l1_pii_approval_ref,
        authorization.preflight_authorization_ref,
        authorization.l1_execution_authorization_ref,
    ]
    if authorization.l2a_enabled:
        assert authorization.l2a_pii_approval_ref is not None
        assert authorization.l2a_provider_budget_approval_ref is not None
        assert authorization.l2a_execution_authorization_ref is not None
        refs.extend(
            (
                authorization.l2a_pii_approval_ref,
                authorization.l2a_provider_budget_approval_ref,
                authorization.l2a_execution_authorization_ref,
            )
        )
    return tuple(refs)


def _ledger(
    *,
    authorization: P1ExecutionAuthorization,
    selection: RealP1SelectionSummary,
    disposal_result: Literal[
        "LOGICAL_DELETION_COMPLETED", "LOGICAL_DELETION_FAILED"
    ],
    evidence: RealP1TargetabilityEvidence | None,
    targetability: TargetabilityDecision | None,
    stop_reason: str,
) -> RealP1EconomicLedger:
    assert selection.selected_source_record_ordinal is not None
    assert selection.selected_holder_report_year is not None
    if evidence is None:
        return RealP1EconomicLedger(
            case_id=_case_id(authorization, selection),
            source_snapshot_ref=authorization.source_snapshot_ref,
            source_record_ordinal=selection.selected_source_record_ordinal,
            holder_report_year=selection.selected_holder_report_year,
            current_discovery_stage="L1",
            service_need_state="UNKNOWN",
            resolvability_state="UNKNOWN",
            estate_path_state="NOT_EVALUATED",
            representative_path_state="NOT_EVALUATED",
            targetability_state="NOT_EVALUATED",
            targetability_decision_cost_state="NOT_MEASURED",
            measured_human_seconds=0,
            authorization_refs=_authorization_refs(authorization),
            stop_reason=stop_reason,
            disposal_result=disposal_result,
        )
    targetability_state: Literal[
        "NOT_EVALUATED",
        "CLASSIFIED",
        "UNRESOLVED_REQUIRES_L2",
        "STOPPED",
    ] = "UNRESOLVED_REQUIRES_L2"
    targetability_class: str | None = None
    if targetability is not None:
        targetability_state = targetability.state
        targetability_class = targetability.targetability_class
        if targetability.targetability_class == "T4_UNBOUNDED_OR_UNRESOLVED_STOP":
            targetability_state = "STOPPED"
    return RealP1EconomicLedger(
        case_id=_case_id(authorization, selection),
        source_snapshot_ref=authorization.source_snapshot_ref,
        source_record_ordinal=selection.selected_source_record_ordinal,
        holder_report_year=selection.selected_holder_report_year,
        current_discovery_stage="L2A",
        service_need_state=evidence.service_need_state,
        resolvability_state=evidence.resolvability_state,
        estate_path_state=evidence.estate_path_state,
        representative_path_state=evidence.representative_path_state,
        targetability_state=targetability_state,
        targetability_class=targetability_class,
        friction_lane=evidence.friction_lane,
        targetability_decision_cost_state=evidence.targetability_decision_cost_state,
        targetability_decision_cost_cents=evidence.targetability_decision_cost_cents,
        measured_human_seconds=evidence.manual_research_seconds,
        external_cash_spend_cents=evidence.external_cash_spend_cents,
        authorization_refs=_authorization_refs(authorization),
        evidence_refs=evidence.evidence_refs,
        stop_reason=stop_reason,
        disposal_result=disposal_result,
    )


def _classify(evidence: RealP1TargetabilityEvidence) -> TargetabilityDecision:
    compatible = SyntheticTargetabilityEvidence(
        service_need_state=evidence.service_need_state,
        resolvability_state=evidence.resolvability_state,
        estate_path_state=evidence.estate_path_state,
        representative_path_state=evidence.representative_path_state,
        friction_lane=evidence.friction_lane,
        evidence_refs=evidence.evidence_refs,
        targetability_decision_cost_state=evidence.targetability_decision_cost_state,
        targetability_decision_cost_cents=evidence.targetability_decision_cost_cents,
    )
    return classify_targetability(compatible)


def _delete_local_archive(archive_path: Path) -> bool:
    try:
        archive_path.unlink(missing_ok=True)
        parent = archive_path.parent
        if parent.name.startswith("unclaimed-ny-mvp1-p1-"):
            shutil.rmtree(parent, ignore_errors=False)
        return not archive_path.exists()
    except OSError:
        return False


def execute_real_p1_targetability_local(
    authorization: P1ExecutionAuthorization,
    archive_path: Path,
    *,
    l2a_provider: L2ATargetabilityProvider | None = None,
) -> RealP1RunResult:
    """Execute one bounded local P1. The archive is logically deleted after opening."""

    try:
        archive_size = archive_path.stat().st_size
    except OSError:
        archive_size = 0

    selection: RealP1SelectionSummary | None = None
    evidence: RealP1TargetabilityEvidence | None = None
    targetability: TargetabilityDecision | None = None
    reason: RealP1RunResult.__annotations__["reason_code"]  # type: ignore[assignment]
    status: Literal["COMPLETED", "BLOCKED"] = "BLOCKED"

    try:
        try:
            _archive_member(archive_path, authorization)
        except (OSError, ValueError, zipfile.BadZipFile):
            reason = "SOURCE_ARCHIVE_BOUNDARY_FAILED"
        else:
            selection = _scan_selection(archive_path, authorization)
            if selection.eligible_records_count == 0:
                reason = "NO_ELIGIBLE_SINGLE_OWNER_IN03_WITH_REPORT_YEAR"
            else:
                candidate = _materialize_selected(archive_path, authorization, selection)
                if candidate is None:
                    reason = "SELECTED_RECORD_SECOND_PASS_MISMATCH"
                elif not authorization.l2a_enabled:
                    reason = "L1_COMPLETED_L2A_NOT_AUTHORIZED"
                    status = "COMPLETED"
                elif l2a_provider is None:
                    reason = "L2A_PROVIDER_REQUIRED"
                elif authorization.provider_binding is None:
                    reason = "L2A_PROVIDER_REQUIRED"
                elif l2a_provider.provider_id != authorization.provider_binding.provider_id:
                    reason = "L2A_PROVIDER_BINDING_MISMATCH"
                else:
                    try:
                        evidence = l2a_provider.evaluate(candidate)
                    except Exception:
                        reason = "EXECUTION_ERROR"
                    else:
                        if (
                            evidence.manual_research_seconds
                            > authorization.provider_binding.approved_manual_research_cap_seconds
                        ):
                            reason = "L2A_MANUAL_RESEARCH_CAP_EXCEEDED"
                        else:
                            targetability = _classify(evidence)
                            if targetability.state == "CLASSIFIED":
                                reason = "L2A_TARGETABILITY_CLASSIFIED"
                            else:
                                reason = "L2A_TARGETABILITY_UNRESOLVED"
                            status = "COMPLETED"
    except Exception:
        reason = "EXECUTION_ERROR"

    deleted = _delete_local_archive(archive_path)
    disposal: Literal[
        "LOGICAL_DELETION_COMPLETED", "LOGICAL_DELETION_FAILED"
    ] = (
        "LOGICAL_DELETION_COMPLETED"
        if deleted
        else "LOGICAL_DELETION_FAILED"
    )
    if not deleted:
        reason = "DISPOSAL_FAILED"
        status = "BLOCKED"

    ledger: RealP1EconomicLedger | None = None
    if selection is not None and selection.eligible_records_count > 0:
        ledger = _ledger(
            authorization=authorization,
            selection=selection,
            disposal_result=disposal,
            evidence=evidence,
            targetability=targetability,
            stop_reason=reason,
        )

    return RealP1RunResult(
        status=status,
        reason_code=reason,
        runner_checkpoint=authorization.runner_checkpoint,
        source_snapshot_ref=authorization.source_snapshot_ref,
        fresh_preflight_receipt_ref=authorization.fresh_preflight_receipt_ref,
        selection=selection,
        economic_case_ledger=ledger,
        targetability=targetability,
        archive_byte_count=archive_size,
        local_file_deleted=deleted,
    )
