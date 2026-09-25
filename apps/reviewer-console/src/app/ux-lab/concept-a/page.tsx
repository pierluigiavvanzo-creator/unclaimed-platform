import {
  ConceptSwitcher,
  ProductMark,
  SafetyBand,
  Status,
} from "../components";
import styles from "../ux-lab.module.css";
import {
  sourceReadiness,
  syntheticPipeline,
  uxCases,
} from "@/lib/ux-lab-data";

export default function ConceptAPage() {
  return (
    <main className={styles.labRoot}>
      <div className={styles.labWrap}>
        <div className={styles.controlRoom}>
          <aside className={styles.sideRail}>
            <ProductMark />
            <nav aria-label="Synthetic product navigation">
              <span>Overview</span>
              <span>Opportunities</span>
              <span>Cases</span>
              <span>Sources</span>
              <span>Evidence</span>
              <span>Economics</span>
              <span>Compliance</span>
              <span>Audit</span>
            </nav>
            <div className={styles.railFooter}>
              Stage B<br />
              One bounded NY OSC targetability experiment
            </div>
          </aside>

          <section className={styles.controlMain}>
            <header className={styles.controlTopbar}>
              <ConceptSwitcher active="A" />
              <div className={styles.topbarActions}>
                <div className={styles.searchMock}>Search cases, evidence, sources...</div>
                <div className={styles.avatar}>PO</div>
              </div>
            </header>

            <div className={styles.controlContent}>
              <div className={styles.pageTitleRow}>
                <div>
                  <SafetyBand />
                  <h1>Intelligence Control Room</h1>
                  <p>Operational shell · targetability, evidence, economics and governance.</p>
                </div>
                <Status tone="info">Stage B · synthetic preview</Status>
              </div>

              <section className={styles.kpiGrid}>
                <article className={styles.kpiCard}>
                  <small>Synthetic discovered</small>
                  <strong>48</strong>
                  <span>UX demonstration only</span>
                </article>
                <article className={styles.kpiCard}>
                  <small>Synthetic reviewable</small>
                  <strong>7</strong>
                  <span>No production KPI implied</span>
                </article>
                <article className={styles.kpiCard}>
                  <small>Targetability decision cost</small>
                  <strong>$4.17</strong>
                  <span>Synthetic case sample</span>
                </article>
                <article className={styles.kpiCard}>
                  <small>Human gate</small>
                  <strong>ON</strong>
                  <span>No autonomous outreach</span>
                </article>
              </section>

              <section className={styles.controlGrid}>
                <article className={styles.darkCard}>
                  <div className={styles.darkCardHeader}>
                    <h2>Targetability pipeline</h2>
                    <small>Synthetic demonstration funnel</small>
                  </div>
                  <div className={styles.pipeline}>
                    {syntheticPipeline.map((step, index) => (
                      <div
                        className={styles.pipelineStep}
                        key={step.label}
                        style={
                          {
                            "--pipeline-width": `${100 - index * 17}%`,
                          } as React.CSSProperties
                        }
                      >
                        <span>{step.label}</span>
                        <strong>{step.value}</strong>
                      </div>
                    ))}
                  </div>
                </article>

                <article className={styles.darkCard}>
                  <div className={styles.darkCardHeader}>
                    <h2>Source readiness</h2>
                    <small>North America target</small>
                  </div>
                  <div className={styles.readinessList}>
                    {sourceReadiness.map((source) => (
                      <div className={styles.readinessItem} key={source.name}>
                        <strong>{source.name}</strong>
                        <Status
                          tone={
                            source.state === "VALIDATED ADAPTER" ? "ok" : "neutral"
                          }
                        >
                          {source.state}
                        </Status>
                        <small>{source.detail}</small>
                      </div>
                    ))}
                  </div>
                </article>
              </section>

              <article className={`${styles.darkCard} ${styles.tableCard}`}>
                <div className={styles.darkCardHeader}>
                  <h2>Priority opportunities</h2>
                  <small>All rows are synthetic UX fixtures</small>
                </div>
                <div className={styles.tableWrap}>
                  <table className={styles.caseTable}>
                    <thead>
                      <tr>
                        <th>Case</th>
                        <th>Registry</th>
                        <th>Targetability</th>
                        <th>Service need</th>
                        <th>Resolvability</th>
                        <th>Decision cost</th>
                        <th>Next action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {uxCases.map((item) => (
                        <tr key={item.id}>
                          <td className={styles.mono}>{item.id}</td>
                          <td>{item.registry}</td>
                          <td>
                            <Status
                              tone={
                                item.targetability === "UNRESOLVED" ? "warn" : "ok"
                              }
                            >
                              {item.targetability}
                            </Status>
                          </td>
                          <td>{item.serviceNeed.replaceAll("_", " ")}</td>
                          <td>{item.resolvability}</td>
                          <td>{item.decisionCost}</td>
                          <td>{item.nextAction}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </article>
            </div>
          </section>
        </div>
      </div>
    </main>
  );
}
