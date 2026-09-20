from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts/ny_osc_gate6_transient_local.ps1"

PROTECTED_PATHS = (
    "scripts/ny_osc_gate6_transient_local.ps1",
    "sources/proposals/ny_osc_owner_name_file_sixth_bounded_attempt_authorization.v1.json",
    "schemas/common/ny_osc_sixth_attempt_authorization_proposal.schema.json",
    "schemas/common/ny_osc_sixth_attempt_transient_local_approval.schema.json",
    "schemas/common/ny_osc_sixth_attempt_transient_pii_approval.schema.json",
    "schemas/common/ny_osc_sixth_fresh_listing_preflight_receipt.schema.json",
    "schemas/agents/ny_transient_local_execution_authorization_v1_1.schema.json",
    "schemas/agents/ny_transient_local_execution_result_v1_2.schema.json",
    "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json",
    "schemas/agents/ny_owner_name_quote_dialect_diagnostic_result.schema.json",
    "src/unclaimed_platform/adapters/sources/ny_owner_name_schema_discovery.py",
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution.py",
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_2.py",
)


def _git(*args: str, input_bytes: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        input=input_bytes,
        capture_output=True,
        check=False,
    )


def test_sixth_runner_self_binds_protected_package_before_temp_creation() -> None:
    text = RUNNER.read_text(encoding="utf-8")
    temp_creation = text.index("New-Item -ItemType Directory")

    for token in (
        "Assert-Gate6ProtectedPackage",
        "git -C $RepoRoot cat-file -e",
        'git -C $RepoRoot rev-parse "${RunnerCheckpoint}:$RelativePath"',
        "git -C $RepoRoot hash-object -- $ActualPath",
        "Protected Gate 6 package differs from the approved runner checkpoint",
    ):
        assert token in text
        assert text.index(token) < temp_creation

    for path in PROTECTED_PATHS:
        assert path in text


def test_current_checkout_protected_paths_have_commit_blobs() -> None:
    head = _git("rev-parse", "HEAD")
    assert head.returncode == 0
    checkpoint = head.stdout.decode().strip()

    for path in PROTECTED_PATHS:
        expected = _git("rev-parse", f"{checkpoint}:{path}")
        assert expected.returncode == 0, path

        actual = _git("hash-object", "--", str(ROOT / path))
        assert actual.returncode == 0, path
        assert actual.stdout.decode().strip() == expected.stdout.decode().strip()


def test_fabricated_or_modified_runner_binding_is_detectable() -> None:
    fabricated = _git("cat-file", "-e", ("0" * 40) + "^{commit}")
    assert fabricated.returncode != 0

    expected = _git("rev-parse", "HEAD:scripts/ny_osc_gate6_transient_local.ps1")
    assert expected.returncode == 0
    modified = _git(
        "hash-object",
        "--stdin",
        input_bytes=RUNNER.read_bytes() + b"\n# local drift\n",
    )
    assert modified.returncode == 0
    assert modified.stdout.decode().strip() != expected.stdout.decode().strip()


def test_sixth_runner_requires_machine_checkable_fresh_preflight_before_temp() -> None:
    text = RUNNER.read_text(encoding="utf-8")
    temp_creation = text.index("New-Item -ItemType Directory")

    required = (
        "Assert-FreshPreflightReceipt",
        'status -ne "EXACT_MATCH"',
        "remote_preflight_performed -ne $true",
        "preflight_authorization_ref",
        "performed_at_utc",
        "proposal_checkpoint -ne $ExpectedProposalCheckpoint",
        "runner_checkpoint -ne $RunnerCheckpoint",
        "freshness_window_seconds -ne $ExpectedPreflightFreshnessSeconds",
        "observed_listing.remote_name -ne \"FINDERS.zip\"",
        "observed_listing.size_display -ne \"390.51 MB\"",
        "observed_listing.last_modified_display -ne \"9/16/2026, 1:33:31 PM\"",
        "TotalSeconds",
        "$AgeSeconds -lt 0",
        "$AgeSeconds -gt $ExpectedPreflightFreshnessSeconds",
    )
    for token in required:
        assert token in text
        assert text.index(token) < temp_creation


def test_sixth_runner_still_has_no_network_client() -> None:
    text = RUNNER.read_text(encoding="utf-8").lower()
    for token in (
        "invoke-webrequest",
        "invoke-restmethod",
        "start-bitstransfer",
        "curl.exe",
        "wget.exe",
    ):
        assert token not in text
