export type UxCase = {
  id: string;
  registry: string;
  registryState: "VALIDATED_ADAPTER" | "FUTURE_NOT_SUPPORTED";
  targetability: "T1" | "T2" | "T3" | "UNRESOLVED";
  serviceNeed: "MATERIAL_EVIDENCE" | "LOW_EVIDENCE" | "UNKNOWN";
  resolvability: "EASY" | "BOUNDED" | "UNKNOWN";
  confidence: "HIGH" | "MEDIUM" | "REVIEW";
  decisionCost: string;
  nextAction: string;
};

export const uxSafetyLabel =
  "SYNTHETIC UX DATA — NO REAL PII — NOT AN AUTHORIZATION SURFACE";

export const uxCases: UxCase[] = [
  {
    id: "SYN-NY-0184",
    registry: "NY OSC",
    registryState: "VALIDATED_ADAPTER",
    targetability: "T1",
    serviceNeed: "MATERIAL_EVIDENCE",
    resolvability: "EASY",
    confidence: "HIGH",
    decisionCost: "$4.17",
    nextAction: "HUMAN REVIEW",
  },
  {
    id: "SYN-NY-0231",
    registry: "NY OSC",
    registryState: "VALIDATED_ADAPTER",
    targetability: "T2",
    serviceNeed: "MATERIAL_EVIDENCE",
    resolvability: "BOUNDED",
    confidence: "MEDIUM",
    decisionCost: "$7.80",
    nextAction: "REVIEW ESTATE PATH",
  },
  {
    id: "SYN-US-FUT-01",
    registry: "Future US registry",
    registryState: "FUTURE_NOT_SUPPORTED",
    targetability: "T3",
    serviceNeed: "MATERIAL_EVIDENCE",
    resolvability: "BOUNDED",
    confidence: "REVIEW",
    decisionCost: "$9.40",
    nextAction: "SOURCE NOT SUPPORTED",
  },
  {
    id: "SYN-CA-FUT-01",
    registry: "Future Canada registry",
    registryState: "FUTURE_NOT_SUPPORTED",
    targetability: "UNRESOLVED",
    serviceNeed: "UNKNOWN",
    resolvability: "UNKNOWN",
    confidence: "REVIEW",
    decisionCost: "—",
    nextAction: "SOURCE NOT SUPPORTED",
  },
];

export const syntheticPipeline = [
  { label: "Discovered", value: 48 },
  { label: "Eligible", value: 22 },
  { label: "Needs L2", value: 12 },
  { label: "Reviewable", value: 7 },
];

export const syntheticTrend = [28, 41, 34, 54, 49, 62, 58, 71, 66, 78, 74, 84];

export const evidenceTimeline = [
  {
    time: "09:12",
    title: "Registry record accepted",
    body: "Synthetic NY OSC record passed the documented structural eligibility boundary.",
    tone: "ok",
  },
  {
    time: "09:18",
    title: "Persistence signal retained",
    body: "Holder Report Year used only as a persistence signal; no value inference.",
    tone: "neutral",
  },
  {
    time: "09:27",
    title: "Targetability evidence assembled",
    body: "Synthetic public-evidence path indicates material service need and bounded resolvability.",
    tone: "ok",
  },
  {
    time: "09:31",
    title: "Human gate required",
    body: "No outreach, representation or claim action is authorized from this workspace.",
    tone: "warn",
  },
];

export const sourceReadiness = [
  {
    name: "NY OSC",
    geography: "New York, US",
    state: "VALIDATED ADAPTER",
    detail: "Stage B experiment anchor",
  },
  {
    name: "Additional US registries",
    geography: "United States",
    state: "FUTURE / NOT SUPPORTED",
    detail: "Prioritize only after Stage B evidence",
  },
  {
    name: "Canadian registries",
    geography: "Canada",
    state: "FUTURE / NOT SUPPORTED",
    detail: "Product target, not current capability",
  },
];
