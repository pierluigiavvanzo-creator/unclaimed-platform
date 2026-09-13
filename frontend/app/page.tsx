import { getOperationsSummary, type OperationsSummary } from "@/lib/operations-summary";

export const dynamic = "force-dynamic";

function humanize(value: string) {
  return value.replaceAll("_", " ").toLowerCase();
}

function StatusPill({ children, tone = "ok" }: { children: React.ReactNode; tone?: "ok" | "warn" | "blocked" }) {
  return <span className={`status status-${tone}`}>{children}</span>;
}

function MilestoneGrid({ milestones }: { milestones: OperationsSummary["milestones"] }) {
  return (
    <div className="milestone-grid">
      {milestones.map((milestone) => (
        <article className="milestone-card" key={milestone.id}>
          <div className="milestone-id">{milestone.id}</div>
          <h3>{milestone.label}</h3>
          <StatusPill>{humanize(milestone.status)}</StatusPill>
        </article>
      ))}
    </div>
  );
}

function ConsoleUnavailable() {
  return (
    <main className="shell">
      <div className="eyebrow">Unclaimed Insurance Platform</div>
      <section className="hero compact">
        <div>
          <p className="kicker">Reviewer console</p>
          <h1>Governed data unavailable</h1>
          <p className="lede">
            A backend URL is configured, but the read-only reviewer contract could not be verified.
            The console fails closed instead of substituting a preview silently.
          </p>
        </div>
        <StatusPill tone="blocked">fail closed</StatusPill>
      </section>
    </main>
  );
}

export default async function Home() {
  let result: Awaited<ReturnType<typeof getOperationsSummary>>;
  try {
    result = await getOperationsSummary();
  } catch {
    return <ConsoleUnavailable />;
  }

  const { summary, origin } = result;
  const fastApiConnected = origin === "FASTAPI";

  return (
    <main className="shell">
      <header className="topbar">
        <div>
          <div className="eyebrow">Unclaimed Insurance Platform</div>
          <div className="product-name">Operations Console</div>
        </div>
        <div className="topbar-status">
          <StatusPill tone={fastApiConnected ? "ok" : "warn"}>
            {fastApiConnected ? "FastAPI connected" : "embedded synthetic preview"}
          </StatusPill>
          <StatusPill>read only</StatusPill>
        </div>
      </header>

      <section className="hero">
        <div>
          <p className="kicker">M3 · California readiness</p>
          <h1>Evidence first. Acquisition still locked.</h1>
          <p className="lede">
            This reviewer surface exposes verified platform boundaries without real claimant data.
            Every artifact shown below is synthetic and the real-data path remains fail-closed.
          </p>
        </div>
        <div className="hero-metric">
          <span>Approved real sources</span>
          <strong>{summary.source_registry.approved_real_sources}</strong>
          <small>{summary.source_registry.real_source_activation.toLowerCase()}</small>
        </div>
      </section>

      <section className="section">
        <div className="section-heading">
          <div>
            <p className="kicker">Delivery state</p>
            <h2>Milestones</h2>
          </div>
          <span className="contract">contract v{summary.contract_version}</span>
        </div>
        <MilestoneGrid milestones={summary.milestones} />
      </section>

      <section className="dashboard-grid">
        <article className="panel span-2">
          <div className="panel-heading">
            <div>
              <p className="kicker">Synthetic raw boundary</p>
              <h2>Immutable artifact</h2>
            </div>
            <StatusPill>synthetic</StatusPill>
          </div>
          <dl className="details">
            <div><dt>Source</dt><dd>{summary.raw_artifact.source_id}</dd></div>
            <div><dt>Authority</dt><dd>{summary.raw_artifact.authority}</dd></div>
            <div><dt>Bytes</dt><dd>{summary.raw_artifact.byte_count}</dd></div>
            <div><dt>Content type</dt><dd>{summary.raw_artifact.content_type}</dd></div>
            <div className="wide"><dt>SHA-256</dt><dd className="mono">{summary.raw_artifact.content_hash}</dd></div>
            <div className="wide"><dt>Storage reference</dt><dd className="mono">{summary.raw_artifact.storage_reference}</dd></div>
          </dl>
        </article>

        <article className="panel">
          <div className="panel-heading">
            <div>
              <p className="kicker">A11 boundary</p>
              <h2>Privacy gates</h2>
            </div>
            <StatusPill>pass</StatusPill>
          </div>
          <ul className="check-list">
            <li><span>Policy</span><strong>{humanize(summary.governance.privacy_policy)}</strong></li>
            <li><span>Provenance</span><strong>{humanize(summary.governance.provenance)}</strong></li>
            <li><span>Retention</span><strong>{humanize(summary.governance.retention)}</strong></li>
            <li><span>Minimization</span><strong>{humanize(summary.governance.data_minimization)}</strong></li>
            <li><span>Unnecessary PII</span><strong>{humanize(summary.governance.unnecessary_pii)}</strong></li>
          </ul>
        </article>

        <article className="panel">
          <div className="panel-heading">
            <div>
              <p className="kicker">Audit integrity</p>
              <h2>Hash chain</h2>
            </div>
            <StatusPill>verified</StatusPill>
          </div>
          <div className="audit-number">{summary.audit.algorithm}</div>
          <p className="muted">{humanize(summary.audit.chain_verification)}</p>
          <div className="split-row"><span>Append only</span><strong>Yes</strong></div>
          <div className="split-row"><span>Durable persistence</span><StatusPill tone="warn">pending</StatusPill></div>
        </article>

        <article className="panel blocked-panel span-2">
          <div className="panel-heading">
            <div>
              <p className="kicker">Human-gated boundaries</p>
              <h2>Locked capabilities</h2>
            </div>
            <StatusPill tone="blocked">blocked by design</StatusPill>
          </div>
          <div className="blocked-grid">
            {summary.blocked_capabilities.map((capability) => (
              <div className="blocked-item" key={capability}>
                <span className="lock-dot" aria-hidden="true" />
                <span>{humanize(capability)}</span>
              </div>
            ))}
          </div>
        </article>
      </section>

      <footer>
        <span>Snapshot {summary.snapshot_date}</span>
        <span>Mode: {humanize(summary.data_mode)}</span>
        <span>California SCO candidate: {humanize(summary.source_registry.california_sco_candidate)}</span>
      </footer>
    </main>
  );
}
