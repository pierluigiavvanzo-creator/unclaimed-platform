import Link from "next/link";

import { ConceptSwitcher, ProductMark, SafetyBand } from "./components";
import styles from "./ux-lab.module.css";

const concepts = [
  {
    id: "A",
    title: "Intelligence Control Room",
    subtitle: "Operational shell",
    body:
      "Dense, professional operations view for source readiness, targetability, case economics and reviewer workflow.",
    href: "/ux-lab/concept-a",
    footer: "Best default operating shell",
  },
  {
    id: "B",
    title: "Executive Intelligence",
    subtitle: "Business performance",
    body:
      "Light, executive-first view centered on funnel, cost, throughput and source expansion readiness.",
    href: "/ux-lab/concept-b",
    footer: "Best for management and investors",
  },
  {
    id: "C",
    title: "Evidence Investigation",
    subtitle: "Case workspace",
    body:
      "Investigator-first case review with evidence timeline, targetability signals and explicit human decision boundary.",
    href: "/ux-lab/concept-c",
    footer: "Best for deep case review",
  },
];

export default function UxLabPage() {
  return (
    <main className={styles.labRoot}>
      <div className={styles.labWrap}>
        <header className={styles.labHeader}>
          <ProductMark />
          <ConceptSwitcher />
        </header>

        <section className={styles.selectorHero}>
          <div>
            <SafetyBand />
            <h1>Three product directions. One governed platform.</h1>
            <p>
              FRONTEND_PRODUCT_UX_V1_OFFLINE isolates the design decision from real data,
              authorization and production infrastructure. Compare the three concepts before
              adding a permanent component system.
            </p>
          </div>

          <aside className={styles.selectorAside}>
            <strong>Decision rule</strong>
            <p>
              Choose the interaction model that best reduces operator time and improves
              targetability review. Visual preference matters, but workflow clarity matters more.
            </p>
          </aside>
        </section>

        <section className={styles.conceptGrid}>
          {concepts.map((concept, index) => (
            <Link href={concept.href} className={styles.conceptCard} key={concept.id}>
              <div className={styles.conceptPreview}>
                <div className={styles.previewWindow}>
                  <div className={styles.previewTop} />
                  <div className={styles.previewGrid}>
                    <div className={styles.previewRail} />
                    <div
                      className={
                        index === 1 ? styles.previewPanelLight : styles.previewPanel
                      }
                    />
                  </div>
                </div>
              </div>
              <div className={styles.conceptBody}>
                <small>CONCEPT {concept.id} · {concept.subtitle}</small>
                <h2>{concept.title}</h2>
                <p>{concept.body}</p>
              </div>
              <div className={styles.conceptFooter}>
                <span>{concept.footer}</span>
                <span>Open concept →</span>
              </div>
            </Link>
          ))}
        </section>

        <footer className={styles.labFooter}>
          Product target: United States + Canada. Current Stage B remains one bounded NY OSC
          targetability experiment. Future registries shown in these concepts are not represented
          as supported sources.
        </footer>
      </div>
    </main>
  );
}
