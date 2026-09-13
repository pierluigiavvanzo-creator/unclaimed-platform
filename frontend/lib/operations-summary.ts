export type MilestoneStatus =
  | "VERIFIED"
  | "COMPLETE"
  | "READINESS_GATES_VERIFIED"
  | "IN_PROGRESS"
  | "BLOCKED";

export interface OperationsSummary {
  contract_version: "1.0.0";
  data_mode: "GOVERNED_SYNTHETIC_PREVIEW";
  read_only: true;
  snapshot_date: string;
  milestones: Array<{
    id: "M0" | "M1" | "M2" | "M3";
    label: string;
    status: MilestoneStatus;
  }>;
  source_registry: {
    approved_real_sources: number;
    real_source_activation: "BLOCKED" | "APPROVED";
    california_sco_candidate: "NOT_APPROVED" | "APPROVED";
  };
  blocked_capabilities: string[];
  raw_artifact: {
    source_id: string;
    source_uri: string;
    authority: string;
    acquisition_method: string;
    content_hash: string;
    byte_count: number;
    content_type: string;
    storage_reference: string;
    synthetic: true;
    immutable: true;
  };
  governance: {
    privacy_policy: "PASS_SYNTHETIC_SCOPE";
    provenance: "PASS";
    approval: "NOT_REQUIRED_SYNTHETIC";
    retention: "PASS";
    data_minimization: "PASS";
    unnecessary_pii: "ABSENT";
  };
  audit: {
    model: "M2_AUDIT_HASH_CHAIN";
    algorithm: "SHA-256";
    chain_verification: "VERIFIED_BY_TEST_SUITE";
    append_only: true;
    durable_persistence: "PENDING";
  };
}

export type SummaryOrigin = "FASTAPI" | "EMBEDDED_SYNTHETIC_PREVIEW";

const contentHash = "5027920b97e7e5827cc45e4fe8484108025e31b792f735809cdb878e2f717bd7";

export const embeddedSummary: OperationsSummary = {
  contract_version: "1.0.0",
  data_mode: "GOVERNED_SYNTHETIC_PREVIEW",
  read_only: true,
  snapshot_date: "2026-09-13",
  milestones: [
    { id: "M0", label: "Repository & Development Harness", status: "VERIFIED" },
    { id: "M1", label: "Machine Contracts", status: "VERIFIED" },
    { id: "M2", label: "State & Governance Core", status: "VERIFIED" },
    { id: "M3", label: "California Data Spike Readiness", status: "READINESS_GATES_VERIFIED" },
  ],
  source_registry: {
    approved_real_sources: 0,
    real_source_activation: "BLOCKED",
    california_sco_candidate: "NOT_APPROVED",
  },
  blocked_capabilities: [
    "REAL_ACQUISITION",
    "BENEFICIARY_MATCHING",
    "OUTREACH",
    "CLAIMANT_VERIFICATION",
    "FEE_AGREEMENT",
    "CLAIM_SUBMISSION",
  ],
  raw_artifact: {
    source_id: "synthetic-reviewer-fixture",
    source_uri: "synthetic://reviewer/m3/raw-artifact",
    authority: "SYNTHETIC_TEST_FIXTURE",
    acquisition_method: "SYNTHETIC_FIXTURE",
    content_hash: contentHash,
    byte_count: 51,
    content_type: "text/csv",
    storage_reference: `raw://synthetic/sha256/${contentHash}`,
    synthetic: true,
    immutable: true,
  },
  governance: {
    privacy_policy: "PASS_SYNTHETIC_SCOPE",
    provenance: "PASS",
    approval: "NOT_REQUIRED_SYNTHETIC",
    retention: "PASS",
    data_minimization: "PASS",
    unnecessary_pii: "ABSENT",
  },
  audit: {
    model: "M2_AUDIT_HASH_CHAIN",
    algorithm: "SHA-256",
    chain_verification: "VERIFIED_BY_TEST_SUITE",
    append_only: true,
    durable_persistence: "PENDING",
  },
};

function isOperationsSummary(value: unknown): value is OperationsSummary {
  if (typeof value !== "object" || value === null) return false;
  const candidate = value as Partial<OperationsSummary>;
  return (
    candidate.contract_version === "1.0.0" &&
    candidate.data_mode === "GOVERNED_SYNTHETIC_PREVIEW" &&
    candidate.read_only === true &&
    Array.isArray(candidate.milestones) &&
    candidate.source_registry?.approved_real_sources !== undefined &&
    Array.isArray(candidate.blocked_capabilities) &&
    candidate.raw_artifact?.synthetic === true &&
    candidate.raw_artifact?.immutable === true
  );
}

export async function getOperationsSummary(): Promise<{
  summary: OperationsSummary;
  origin: SummaryOrigin;
}> {
  const apiBase = process.env.UNCLAIMED_API_BASE_URL?.replace(/\/$/, "");
  if (!apiBase) {
    return { summary: embeddedSummary, origin: "EMBEDDED_SYNTHETIC_PREVIEW" };
  }

  const response = await fetch(`${apiBase}/api/v1/reviewer/operations-summary`, {
    cache: "no-store",
    headers: { Accept: "application/json" },
  });
  if (!response.ok) {
    throw new Error(`Reviewer API unavailable (${response.status})`);
  }

  const payload: unknown = await response.json();
  if (!isOperationsSummary(payload)) {
    throw new Error("Reviewer API returned an invalid contract payload");
  }

  return { summary: payload, origin: "FASTAPI" };
}
