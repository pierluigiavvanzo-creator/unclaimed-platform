# Apply NY OSC Offline Repair

Base checkpoint:

`61a533e035dfba45d0c1359b8eee0fdbba41d7d8`

This patch is offline-only. It does not authorize another NY OSC download.

## PowerShell

Run from the repository root:

```powershell
git status --short
git branch --show-current
git rev-parse HEAD
```

The expected HEAD is the base checkpoint above. If the working tree has unrelated changes,
stop before applying the patch.

Create an isolated branch:

```powershell
git switch -c mvp1-ny-osc-quote-aware-offline-repair
```

After downloading the `.patch` file to the repository root:

```powershell
git apply --check .\UNCLAIMED_NY_OSC_OFFLINE_REPAIR_FROM_61a533e.patch
git apply .\UNCLAIMED_NY_OSC_OFFLINE_REPAIR_FROM_61a533e.patch
```

Verify:

```powershell
.\.venv\Scripts\Activate.ps1
python -m ruff check .
python -m mypy
python -m pytest -q
git diff --check
git status --short
git diff --stat
```

Do not run `scripts\ny_osc_gate2_retry_transient_local.ps1`. Both second-attempt approvals
are consumed and the repaired script must stop before any download prompt.

Do not commit or push until the test output and diff have been reviewed.
