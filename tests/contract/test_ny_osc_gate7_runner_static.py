from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts/ny_osc_gate7_transient_local.ps1"

PROTECTED_PATHS = (
    "scripts/ny_osc_gate7_transient_local.ps1",
    "sources/proposals/ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json",
    "schemas/common/ny_osc_seventh_attempt_authorization_proposal.schema.json",
    "schemas/common/ny_osc_seventh_attempt_transient_local_approval.schema.json",
    "schemas/common/ny_osc_seventh_attempt_transient_pii_approval.schema.json",
    "schemas/common/ny_osc_seventh_fresh_listing_preflight_receipt.schema.json",
    "schemas/common/ny_osc_seventh_execution_authorization.schema.json",
    "schemas/agents/ny_transient_local_execution_authorization_v1_3.schema.json",
    "schemas/agents/ny_transient_local_execution_result_v1_4.schema.json",
    "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json",
    "src/unclaimed_platform/adapters/sources/ny_owner_name_schema_discovery.py",
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution.py",
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_4.py",
)


def test_gate7_checks_four_bound_artifacts_before_temp_creation() -> None:
    text = RUNNER.read_text(encoding="utf-8")
    temp_creation = text.index("New-Item -ItemType Directory")

    required = (
        "$LocalApproval",
        "$PiiApproval",
        "$FreshPreflightReceipt",
        "$ExecutionAuthorization",
        'status -ne "GRANTED_NOT_CONSUMED"',
        "Assert-CommonBinding -Record $LocalApprovalRecord",
        "Assert-CommonBinding -Record $PiiApprovalRecord",
        "Assert-CommonBinding -Record $ExecutionAuthorizationRecord",
        "Assert-FreshPreflightReceipt",
        "Assert-Gate7ProtectedPackage",
        "fresh_preflight_receipt_ref",
        "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP",
        "ONE_BOUND_GATE7_EXECUTION",
        "Select-Object -Unique",
    )
    for token in required:
        assert token in text
        assert text.index(token) < temp_creation


def test_gate7_self_binds_entire_real_runtime_package_before_temp_creation() -> None:
    text = RUNNER.read_text(encoding="utf-8")
    temp_creation = text.index("New-Item -ItemType Directory")

    for token in (
        "git -C $RepoRoot cat-file -e",
        'git -C $RepoRoot rev-parse "' + "$" + '{RunnerCheckpoint}:$RelativePath"',
        "git -C $RepoRoot hash-object -- $ActualPath",
        "Protected Gate 7 package differs from the approved runner checkpoint",
    ):
        assert token in text
        assert text.index(token) < temp_creation

    for path in PROTECTED_PATHS:
        assert path in text


def test_gate7_fresh_preflight_is_exact_and_bounded_before_download_path() -> None:
    text = RUNNER.read_text(encoding="utf-8")
    temp_creation = text.index("New-Item -ItemType Directory")

    for token in (
        'status -ne "EXACT_MATCH"',
        "remote_preflight_performed -ne $true",
        "freshness_window_seconds -ne $ExpectedPreflightFreshnessSeconds",
        "observed_listing.remote_name -ne \"FINDERS.zip\"",
        "observed_listing.size_display -ne \"390.51 MB\"",
        "observed_listing.last_modified_display -ne \"9/16/2026, 1:33:31 PM\"",
        "download_performed -ne $false",
        "owner_file_opened -ne $false",
        "owner_pii_processed -ne $false",
        "contains_owner_pii -ne $false",
        "$AgeSeconds -lt 0",
        "$AgeSeconds -gt $ExpectedPreflightFreshnessSeconds",
    ):
        assert token in text
        assert text.index(token) < temp_creation


def test_gate7_has_no_network_client_and_only_manual_download_instruction() -> None:
    text = RUNNER.read_text(encoding="utf-8")
    lower = text.lower()

    for token in (
        "invoke-webrequest",
        "invoke-restmethod",
        "start-bitstransfer",
        "curl.exe",
        "wget.exe",
    ):
        assert token not in lower

    assert "The execution authorization permits exactly one manual download." in text
    assert (
        "Press Enter only after the separately authorized single manual download finishes"
        in text
    )


def test_gate7_invokes_only_v1_4_runtime_after_archive_presence_check() -> None:
    text = RUNNER.read_text(encoding="utf-8")
    archive_check = text.index("FINDERS.zip not found")
    runtime_call = text.index("build_real_execution_authorization_v1_3")

    assert archive_check < runtime_call
    assert "execute_transient_local_file_discovery_v1_4" in text
    assert "ny_owner_name_transient_local_execution_v1_2" not in text
    assert "LINE_LOCAL_ARBITRATION" not in text
