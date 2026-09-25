import Link from "next/link";

import styles from "./ux-lab.module.css";
import { uxSafetyLabel } from "@/lib/ux-lab-data";

const concepts = [
  { href: "/ux-lab/concept-a", short: "A", label: "Control Room" },
  { href: "/ux-lab/concept-b", short: "B", label: "Executive" },
  { href: "/ux-lab/concept-c", short: "C", label: "Investigation" },
];

export function ProductMark() {
  return (
    <div className={styles.productMark}>
      <span className={styles.productGlyph}>U</span>
      <div>
        <strong>UNCLAIMED</strong>
        <small>North America intelligence platform</small>
      </div>
    </div>
  );
}

export function SafetyBand({ light = false }: { light?: boolean }) {
  return (
    <div className={light ? styles.safetyBandLight : styles.safetyBand}>
      <span className={styles.safetyDot} />
      {uxSafetyLabel}
    </div>
  );
}

export function ConceptSwitcher({
  active,
  light = false,
}: {
  active?: "A" | "B" | "C";
  light?: boolean;
}) {
  return (
    <nav className={light ? styles.switcherLight : styles.switcher} aria-label="UX concepts">
      <Link href="/ux-lab" className={styles.switcherHome}>
        UX Lab
      </Link>
      {concepts.map((concept) => (
        <Link
          key={concept.short}
          href={concept.href}
          className={active === concept.short ? styles.switcherActive : styles.switcherLink}
          aria-current={active === concept.short ? "page" : undefined}
        >
          <span>{concept.short}</span>
          {concept.label}
        </Link>
      ))}
    </nav>
  );
}

export function Status({
  children,
  tone = "neutral",
}: {
  children: React.ReactNode;
  tone?: "ok" | "warn" | "neutral" | "info";
}) {
  const toneClass = {
    ok: styles.statusOk,
    warn: styles.statusWarn,
    neutral: styles.statusNeutral,
    info: styles.statusInfo,
  }[tone];

  return <span className={`${styles.status} ${toneClass}`}>{children}</span>;
}

export function SparkBars({ values }: { values: number[] }) {
  const max = Math.max(...values);
  return (
    <div className={styles.sparkBars} aria-label="Synthetic trend visualization">
      {values.map((value, index) => (
        <span
          key={`${value}-${index}`}
          style={{ height: `${Math.max(18, Math.round((value / max) * 100))}%` }}
        />
      ))}
    </div>
  );
}
