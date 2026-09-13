import { readFile } from "node:fs/promises";

const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
const data = await readFile(new URL("../lib/operations-summary.ts", import.meta.url), "utf8");

const requiredPageCopy = [
  "Operations Console",
  "Evidence first. Acquisition still locked.",
  "Privacy gates",
  "Hash chain",
  "Locked capabilities",
  "read only",
];

const requiredStates = [
  "GOVERNED_SYNTHETIC_PREVIEW",
  "REAL_ACQUISITION",
  "BENEFICIARY_MATCHING",
  "approved_real_sources: 0",
  "NOT_APPROVED",
];

for (const value of requiredPageCopy) {
  if (!page.includes(value)) throw new Error(`Missing reviewer-console copy: ${value}`);
}
for (const value of requiredStates) {
  if (!data.includes(value)) throw new Error(`Missing fail-closed preview state: ${value}`);
}

console.log("Reviewer console static assertions passed.");
