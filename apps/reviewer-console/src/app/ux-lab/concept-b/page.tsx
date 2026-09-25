import {
  ConceptSwitcher,
  ProductMark,
  SafetyBand,
  SparkBars,
  Status,
} from "../components";
import styles from "../ux-lab.module.css";
import {
  sourceReadiness,
  syntheticTrend,
} from "@/lib/ux-lab-data";

export default function ConceptBPage() {
  return (
    <main className={styles.labRootLight}>
      <div className={styles.execShell}>
        <header className={styles.execNav}>
          <ProductMark />
          <ConceptSwitcher active="B" light />
        </header>

        <section className={styles.execHero}>
          <div>
            <SafetyBand light />
            <h1>Executive Intelligence</h1>
            <p>
              A business-first view of targetability throughput, decision cost, human effort and
              source expansion readiness. Production metrics stay blank until evidence exists;
              values below are synthetic UX fixtures.
            </p>
          </div>

          <aside className={styles.execHeroAside}>
            <Status tone="info">Stage B · synthetic preview</Status>
            <strong>One question at a time</strong>
            <span>
              Can the core engine turn one authorized registry record into a reliable targetability
              decision at controlled cost?
            </span>
          </aside>
        </section>

        <section className={styles.execKpis}>
          <article className={styles.execKpi}>
            <small>Synthetic opportunities</small>
            <strong>48</strong>
          </article>
          <article className={styles.execKpi}>
            <small>Synthetic reviewable</small>
            <strong>7</strong>
          </article>
          <article className={styles.execKpi}>
            <small>Sample decision cost</small>
            <strong>$4.17</strong>
          </article>
          <article className={styles.execKpi}>
            <small>Production threshold</small>
            <strong>—</strong>
          </article>
        </section>

        <section className={styles.execGrid}>
          <article className={styles.lightCard}>
            <div className={styles.lightCardHeader}>
              <h2>Targetability learning trend</h2>
              <small>Synthetic visual signal · not measured product performance</small>
            </div>
            <SparkBars values={syntheticTrend} />
          </article>

          <article className={styles.lightCard}>
            <div className={styles.lightCardHeader}>
              <h2>What needs attention</h2>
              <small>Human/product gates</small>
            </div>
            <div className={styles.execAttention}>
              <div className={styles.execAttentionItem}>
                <span className={styles.attentionDot} />
                <div>
                  <strong>Controller formation</strong>
                  <p>Real P1 stays blocked until a genuine US controller entity is formed and bound.</p>
                </div>
              </div>
              <div className={styles.execAttentionItem}>
                <span className={styles.attentionDot} />
                <div>
                  <strong>Seven P1 gates</strong>
                  <p>All remain NOT_GRANTED and cannot be inferred from this interface.</p>
                </div>
              </div>
              <div className={styles.execAttentionItem}>
                <span className={styles.attentionDot} />
                <div>
                  <strong>Production KPI thresholds</strong>
                  <p>Intentionally absent until real P1/P2/P3 evidence supports them.</p>
                </div>
              </div>
            </div>
          </article>
        </section>

        <section className={styles.sourceGrid}>
          {sourceReadiness.map((source) => (
            <article className={styles.sourceCard} key={source.name}>
              <strong>{source.name}</strong>
              <span>{source.geography}</span>
              <Status tone={source.state === "VALIDATED ADAPTER" ? "ok" : "neutral"}>
                {source.state}
              </Status>
              <p>{source.detail}</p>
            </article>
          ))}
        </section>

        <footer className={styles.labFooter}>
          Concept B is designed for executive comprehension first. Deep evidence and case-review
          workflows would remain available in dedicated case workspaces rather than crowding the
          management dashboard.
        </footer>
      </div>
    </main>
  );
}
