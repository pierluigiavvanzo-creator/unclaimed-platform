import Link from "next/link";

import { getOperationsSnapshot } from "@/lib/operations";

function StatusPill({ value }: { value: string }) {
  const blocked = value.includes("BLOCKED") || value === "PENDING" || value === "NOT_CONNECTED";
  return <span className={blocked ? "pill pill-warn" : "pill pill-ok"}>{value.replaceAll("_", " ")}</span>;
}

export default async function Home() {
  const { data, source } = await getOperationsSnapshot();

  return (
    <main className="shell">
      <header className="hero">
        <div>
          <p className="eyebrow">UNCLAIMED INSURANCE PLATFORM</p>
          <h1>M3 Operations Console</h1>
          <p className="lede">A read-only view of provenance, governance and deployment readiness.</p>
          <Link href="/ux-lab" className="ux-lab-entry">Explore FRONTEND_PRODUCT_UX_V1_OFFLINE →</Link>
        </div>
        <div className="mode-card">
          <span>Data mode</span>
          <strong>{data.mode.replaceAll("_", " ")}</strong>
          <small>Source: {source === "backend" ? "FastAPI contract" : "typed synthetic fallback"}</small>
        </div>
      </header>

      <section className="alert">
        <strong>Safety boundary active.</strong>
        <span>No real acquisition, no beneficiary matching, no real PII.</span>
      </section>

      <section className="grid milestones">
        {data.milestones.map((milestone) => (
          <article className="card" key={milestone.id}>
            <div className="card-top"><span>{milestone.id}</span><StatusPill value={milestone.status} /></div>
            <h2>{milestone.label}</h2>
          </article>
        ))}
      </section>

      <section className="grid two-col">
        <article className="card feature-card">
          <p className="eyebrow">SOURCE REGISTRY</p>
          <div className="metric">{data.source_registry.approved_real_sources}</div>
          <p>Approved real sources</p>
          <dl>
            <div><dt>Real acquisition</dt><dd><StatusPill value={data.source_registry.real_acquisition} /></dd></div>
            <div><dt>Beneficiary matching</dt><dd><StatusPill value={data.source_registry.beneficiary_matching} /></dd></div>
          </dl>
        </article>

        <article className="card feature-card">
          <p className="eyebrow">GOVERNANCE</p>
          <dl>
            <div><dt>Privacy gate</dt><dd><StatusPill value={data.governance.privacy_gate} /></dd></div>
            <div><dt>Source approval</dt><dd><StatusPill value={data.governance.source_approval_gate} /></dd></div>
            <div><dt>Retention</dt><dd><StatusPill value={data.governance.retention_policy} /></dd></div>
            <div><dt>PII mode</dt><dd><StatusPill value={data.governance.pii_mode} /></dd></div>
          </dl>
        </article>
      </section>

      <section className="grid two-col">
        <article className="card feature-card">
          <p className="eyebrow">SYNTHETIC RAW ARTIFACT</p>
          <h2>{data.raw_artifact.artifact_id}</h2>
          <dl className="mono-list">
            <div><dt>SHA-256</dt><dd>{data.raw_artifact.sha256}</dd></div>
            <div><dt>Provenance SHA-256</dt><dd>{data.raw_artifact.provenance_sha256}</dd></div>
            <div><dt>Bytes</dt><dd>{data.raw_artifact.byte_count}</dd></div>
            <div><dt>Source</dt><dd>{data.raw_artifact.source_uri}</dd></div>
          </dl>
        </article>

        <article className="card feature-card">
          <p className="eyebrow">AUDIT & PLATFORM</p>
          <dl>
            <div><dt>Audit chain</dt><dd><StatusPill value={data.audit.chain} /></dd></div>
            <div><dt>Durable audit backend</dt><dd><StatusPill value={data.audit.durable_backend} /></dd></div>
            <div><dt>Supabase</dt><dd><StatusPill value={data.platform.supabase} /></dd></div>
          </dl>
        </article>
      </section>

      <footer>
        Contract v{data.contract_version} · Synthetic reviewer surface · Backend governance remains authoritative
      </footer>
    </main>
  );
}
