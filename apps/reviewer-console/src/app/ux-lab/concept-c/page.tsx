import {
  ConceptSwitcher,
  ProductMark,
  SafetyBand,
  Status,
} from "../components";
import styles from "../ux-lab.module.css";
import { evidenceTimeline, uxCases } from "@/lib/ux-lab-data";

export default function ConceptCPage() {
  const activeCase = uxCases[0];

  return (
    <main className={styles.labRoot}>
      <div className={styles.labWrap}>
        <div className={styles.workspace}>
          <aside className={styles.queuePane}>
            <ProductMark />
            <div className={styles.paneHeading}>
              <strong>Case queue</strong>
              <span>{uxCases.length} synthetic</span>
            </div>
            <div className={styles.queueList}>
              {uxCases.map((item) => (
                <div className={styles.queueItem} key={item.id}>
                  <strong>{item.id}</strong>
                  <span>{item.registry}</span>
                  <span>{item.targetability} · {item.nextAction}</span>
                </div>
              ))}
            </div>
          </aside>

          <section className={styles.workspaceCenter}>
            <header className={styles.workspaceTopbar}>
              <ConceptSwitcher active="C" />
              <SafetyBand />
            </header>

            <div className={styles.workspaceCaseTitle}>
              <span>CASE WORKSPACE · SYNTHETIC</span>
              <h1>{activeCase.id}</h1>
              <p>
                Evidence-first investigation view. No outreach, representation, claim activity or
                real owner PII is enabled.
              </p>
            </div>

            <section className={styles.caseSignals}>
              <article className={styles.signalCard}>
                <small>Targetability</small>
                <strong>{activeCase.targetability}</strong>
              </article>
              <article className={styles.signalCard}>
                <small>Service need</small>
                <strong>{activeCase.serviceNeed.replaceAll("_", " ")}</strong>
              </article>
              <article className={styles.signalCard}>
                <small>Resolvability</small>
                <strong>{activeCase.resolvability}</strong>
              </article>
            </section>

            <article className={`${styles.darkCard} ${styles.timelineCard}`}>
              <div className={styles.darkCardHeader}>
                <h2>Evidence timeline</h2>
                <small>Provenance-aware synthetic sequence</small>
              </div>
              <div className={styles.timeline}>
                {evidenceTimeline.map((event) => (
                  <div className={styles.timelineItem} key={`${event.time}-${event.title}`}>
                    <span className={styles.timelineTime}>{event.time}</span>
                    <span className={styles.timelineRail}>
                      <span className={styles.timelineDot} />
                    </span>
                    <div className={styles.timelineBody}>
                      <strong>{event.title}</strong>
                      <p>{event.body}</p>
                    </div>
                  </div>
                ))}
              </div>
            </article>

            <article className={`${styles.darkCard} ${styles.tableCard}`}>
              <div className={styles.darkCardHeader}>
                <h2>Evidence / contradictions / provenance</h2>
                <small>Expandable production information architecture</small>
              </div>
              <div className={styles.readinessList}>
                <div className={styles.readinessItem}>
                  <strong>Supporting evidence</strong>
                  <Status tone="ok">3 synthetic items</Status>
                  <small>Verified source-page evidence would live here when separately authorized.</small>
                </div>
                <div className={styles.readinessItem}>
                  <strong>Contradictions</strong>
                  <Status tone="neutral">None in fixture</Status>
                  <small>Conflicting identity hypotheses remain visible rather than silently collapsed.</small>
                </div>
                <div className={styles.readinessItem}>
                  <strong>Provenance</strong>
                  <Status tone="info">Traceable</Status>
                  <small>Every material fact should retain source and evidence references.</small>
                </div>
              </div>
            </article>
          </section>

          <aside className={styles.decisionPane}>
            <Status tone="warn">Human gate</Status>
            <h2>Decision panel</h2>
            <p>
              This panel presents evidence and economics. It does not turn a visual click into an
              execution authorization.
            </p>

            <div className={styles.decisionMetric}>
              <small>Service need</small>
              <strong>MATERIAL EVIDENCE</strong>
            </div>
            <div className={styles.decisionMetric}>
              <small>Resolvability</small>
              <strong>BOUNDED / EASY</strong>
            </div>
            <div className={styles.decisionMetric}>
              <small>Confidence</small>
              <strong>{activeCase.confidence}</strong>
            </div>
            <div className={styles.decisionMetric}>
              <small>Decision cost</small>
              <strong>{activeCase.decisionCost} · synthetic</strong>
            </div>
            <div className={styles.decisionMetric}>
              <small>Authorized next action</small>
              <strong>NONE FROM UX LAB</strong>
            </div>

            <div className={styles.reviewButton}>Human review preview</div>
            <div className={styles.reviewNote}>
              Non-interactive by design. Future write actions require authentication, RBAC,
              case-level authorization and deterministic backend gates.
            </div>
          </aside>
        </div>
      </div>
    </main>
  );
}
