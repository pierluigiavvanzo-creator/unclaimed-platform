import zipfile

from unclaimed_platform.adapters.sources.ny_owner_name_p1_targetability_local import (
    _SelectedRecordCollector,
    RealP1TargetabilityEvidence,
    TransientSelectedCandidate,
    execute_real_p1_targetability_local,
)
from unclaimed_platform.domain.ny_mvp1_p1_authorization import (
    P1ExecutionAuthorization,
    ProviderBinding,
)

RUNNER_SHA = "a" * 40


def row(
    *,
    property_id="SYNTHETIC-PROP",
    property_type="IN03",
    owner_count="1",
    owner_name="SYNTHETIC-OWNER",
    address1="SYNTHETIC-ADDRESS",
    holder="SYNTHETIC-HOLDER",
    year="2025",
):
    fields = [
        property_id,
        property_type,
        "SYNTHETIC-DESCRIPTION",
        owner_count,
        owner_name,
        address1,
        "",
        "",
        "SYNTHETIC-CITY",
        "NY",
        "10001",
        "US",
        holder,
        year,
    ]
    return "|".join(fields)


def archive(tmp_path, rows):
    path = tmp_path / "FINDERS.zip"
    payload = ("\r\n".join(rows) + "\r\n").encode("ascii")
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("FINDERS.txt", payload)
    return path


def authorization(*, l2a=False, provider_id="synthetic-approved-provider"):
    binding = None
    kwargs = {}
    if l2a:
        binding = ProviderBinding(
            provider_id=provider_id,
            provider_terms_review_ref="synthetic:provider-terms-review",
        )
        kwargs = dict(
            l2a_pii_approval_ref="synthetic:l2a-pii",
            l2a_provider_budget_approval_ref="synthetic:l2a-provider-budget",
            l2a_execution_authorization_ref="synthetic:l2a-execution",
            provider_binding=binding,
        )
    return P1ExecutionAuthorization(
        runner_checkpoint=RUNNER_SHA,
        source_snapshot_ref="synthetic:snapshot",
        fresh_preflight_receipt_ref="synthetic:preflight",
        authorized_download_started_at_utc="2026-09-24T10:00:10Z",
        local_file_approval_ref="synthetic:local",
        l1_pii_approval_ref="synthetic:l1-pii",
        preflight_authorization_ref="synthetic:preflight-auth",
        l1_execution_authorization_ref="synthetic:l1-exec",
        l2a_enabled=l2a,
        **kwargs,
    )


class SyntheticProvider:
    provider_id = "synthetic-approved-provider"

    def __init__(self, *, seconds=120):
        self.seconds = seconds
        self.called = False

    def evaluate(
        self,
        candidate: TransientSelectedCandidate,
    ) -> RealP1TargetabilityEvidence:
        self.called = True
        assert candidate.owner_name == b"SYNTHETIC-OWNER-OLDEST"
        assert candidate.address_fields[0] == b"SYNTHETIC-ADDRESS-OLDEST"
        return RealP1TargetabilityEvidence(
            service_need_state="MATERIAL_EVIDENCE",
            resolvability_state="EASY",
            estate_path_state="NO_EVIDENCE",
            representative_path_state="NOT_EVALUATED",
            friction_lane="F1",
            evidence_refs=("synthetic:targetability-evidence",),
            manual_research_seconds=self.seconds,
            external_cash_spend_cents=0,
            targetability_decision_cost_state="MEASURING",
            source_type_categories=("PUBLIC_OFFICIAL",),
            non_pii_source_domains=("example.test",),
        )


class WrongProvider(SyntheticProvider):
    provider_id = "wrong-provider"


def test_l1_selects_oldest_report_year_then_source_order_and_returns_no_pii(tmp_path):
    path = archive(
        tmp_path,
        [
            row(
                property_id="SECRET-PROP-NEW",
                owner_name="SECRET-OWNER-NEW",
                address1="SECRET-ADDRESS-NEW",
                year="2025",
            ),
            row(
                property_id="SECRET-PROP-OLDEST",
                owner_name="SECRET-OWNER-OLDEST",
                address1="SECRET-ADDRESS-OLDEST",
                year="2001",
            ),
            row(
                property_id="SECRET-PROP-TIE",
                owner_name="SECRET-OWNER-TIE",
                address1="SECRET-ADDRESS-TIE",
                year="2001",
            ),
        ],
    )
    result = execute_real_p1_targetability_local(authorization(), path)

    assert result.status == "COMPLETED"
    assert result.reason_code == "L1_COMPLETED_L2A_NOT_AUTHORIZED"
    assert result.selection is not None
    assert result.selection.selected_source_record_ordinal == 2
    assert result.selection.selected_holder_report_year == 2001
    assert result.selection.owner_pii_decoded_for_ranking is False
    assert result.selection.owner_pii_buffered_for_ranking is False
    assert result.local_file_deleted is True
    assert not path.exists()

    serialized = result.model_dump_json()
    for secret in (
        "SECRET-PROP-OLDEST",
        "SECRET-OWNER-OLDEST",
        "SECRET-ADDRESS-OLDEST",
        "SYNTHETIC-HOLDER",
    ):
        assert secret not in serialized


def test_l1_only_selected_record_collector_buffers_no_direct_pii() -> None:
    payload = (
        row(
            property_id="SECRET-PROPERTY-ID",
            owner_name="SECRET-OWNER-NAME",
            address1="SECRET-ADDRESS",
            holder="SECRET-HOLDER",
            year="2000",
        )
        + "\r\n"
    ).encode("ascii")
    collector = _SelectedRecordCollector(
        1,
        include_direct_pii=False,
        include_address=False,
    )
    for value in payload:
        collector.consume(value)
    collector.finish()

    assert collector.selected_property_id_non_ws is True
    assert collector.selected is not None
    assert set(collector.selected) == {1, 3, 13}
    serialized = repr(collector.selected)
    assert "SECRET-PROPERTY-ID" not in serialized
    assert "SECRET-OWNER-NAME" not in serialized
    assert "SECRET-ADDRESS" not in serialized
    assert "SECRET-HOLDER" not in serialized


def test_l0_deferred_structural_record_does_not_block_later_candidate(tmp_path):
    malformed = "BROKEN|IN03|ONLY"
    path = archive(
        tmp_path,
        [
            malformed,
            row(owner_name="SYNTHETIC-OWNER-OLDEST", year="1999"),
        ],
    )
    result = execute_real_p1_targetability_local(authorization(), path)

    assert result.status == "COMPLETED"
    assert result.selection is not None
    assert result.selection.total_records == 2
    assert result.selection.structurally_deferred_records == 1
    assert result.selection.eligible_records_count == 1
    assert result.selection.selected_source_record_ordinal == 2


def test_no_eligible_candidate_stops_without_pii_output(tmp_path):
    path = archive(
        tmp_path,
        [
            row(property_type="IN01", owner_name="DO-NOT-RETURN-1"),
            row(owner_count="2", owner_name="DO-NOT-RETURN-2"),
            row(property_id="   ", owner_name="DO-NOT-RETURN-3"),
            row(year="not-a-year", owner_name="DO-NOT-RETURN-4"),
        ],
    )
    result = execute_real_p1_targetability_local(authorization(), path)

    assert result.status == "BLOCKED"
    assert result.reason_code == "NO_ELIGIBLE_SINGLE_OWNER_IN03_WITH_REPORT_YEAR"
    assert result.selection is not None
    assert result.selection.eligible_records_count == 0
    assert result.economic_case_ledger is None
    assert "DO-NOT-RETURN" not in result.model_dump_json()


def test_l2a_provider_can_classify_targetability_without_returning_pii(tmp_path):
    path = archive(
        tmp_path,
        [
            row(
                owner_name="SYNTHETIC-OWNER-OLDEST",
                address1="SYNTHETIC-ADDRESS-OLDEST",
                year="2000",
            )
        ],
    )
    provider = SyntheticProvider()
    result = execute_real_p1_targetability_local(
        authorization(l2a=True),
        path,
        l2a_provider=provider,
    )

    assert provider.called is True
    assert result.status == "COMPLETED"
    assert result.reason_code == "L2A_TARGETABILITY_CLASSIFIED"
    assert result.targetability is not None
    assert result.targetability.targetability_class == "T1_UNRESOLVED_BUT_LOCATABLE"
    assert result.economic_case_ledger is not None
    assert result.economic_case_ledger.current_discovery_stage == "L2A"
    assert result.economic_case_ledger.measured_human_seconds == 120
    assert result.economic_case_ledger.external_cash_spend_cents == 0
    assert "SYNTHETIC-OWNER-OLDEST" not in result.model_dump_json()
    assert "SYNTHETIC-ADDRESS-OLDEST" not in result.model_dump_json()


def test_l2a_manual_research_cap_is_fail_closed(tmp_path):
    path = archive(
        tmp_path,
        [
            row(
                owner_name="SYNTHETIC-OWNER-OLDEST",
                address1="SYNTHETIC-ADDRESS-OLDEST",
                year="2000",
            )
        ],
    )
    result = execute_real_p1_targetability_local(
        authorization(l2a=True),
        path,
        l2a_provider=SyntheticProvider(seconds=901),
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "L2A_MANUAL_RESEARCH_CAP_EXCEEDED"
    assert result.targetability is None
    assert result.economic_case_ledger is not None
    assert result.economic_case_ledger.measured_human_seconds == 901
    assert result.local_file_deleted is True


def test_l2a_provider_binding_must_match_approved_provider(tmp_path):
    path = archive(
        tmp_path,
        [
            row(
                owner_name="SYNTHETIC-OWNER-OLDEST",
                address1="SYNTHETIC-ADDRESS-OLDEST",
                year="2000",
            )
        ],
    )
    provider = WrongProvider()
    result = execute_real_p1_targetability_local(
        authorization(l2a=True),
        path,
        l2a_provider=provider,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "L2A_PROVIDER_BINDING_MISMATCH"
    assert provider.called is False


def test_l2a_authorized_without_bound_provider_stops(tmp_path):
    path = archive(
        tmp_path,
        [
            row(
                owner_name="SYNTHETIC-OWNER-OLDEST",
                address1="SYNTHETIC-ADDRESS-OLDEST",
                year="2000",
            )
        ],
    )
    result = execute_real_p1_targetability_local(
        authorization(l2a=True),
        path,
        l2a_provider=None,
    )

    assert result.status == "BLOCKED"
    assert result.reason_code == "L2A_PROVIDER_REQUIRED"
    assert result.local_file_deleted is True


def test_wrong_archive_name_fails_boundary_and_is_deleted(tmp_path):
    path = tmp_path / "unexpected.zip"
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("FINDERS.txt", row())

    result = execute_real_p1_targetability_local(authorization(), path)

    assert result.status == "BLOCKED"
    assert result.reason_code == "SOURCE_ARCHIVE_BOUNDARY_FAILED"
    assert result.local_file_deleted is True
    assert not path.exists()
