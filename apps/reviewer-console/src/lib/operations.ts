export type OperationsSnapshot = {
  contract_version: "1.0.0";
  mode: "SYNTHETIC_READ_ONLY";
  milestones: Array<{ id: string; label: string; status: string }>;
  source_registry: {
    approved_real_sources: 0;
    real_acquisition: "BLOCKED";
    beneficiary_matching: "BLOCKED";
  };
  raw_artifact: {
    artifact_id: string;
    sha256: string;
    byte_count: number;
    content_type: string;
    source_id: string;
    source_uri: string;
    authority: string;
    acquisition_method: string;
    retrieved_at: string;
    provenance_sha256: string;
    synthetic: true;
    immutable: true;
  };
  governance: {
    privacy_gate: "PASS_SYNTHETIC_ONLY";
    source_approval_gate: "BLOCKED_NO_REAL_SOURCE";
    retention_policy: "REQUIRED";
    pii_mode: "NO_REAL_PII";
  };
  audit: {
    chain: "HEALTHY_SYNTHETIC";
    algorithm: "SHA-256";
    durable_backend: "PENDING";
  };
  platform: {
    vercel: "NOT_CONNECTED";
    supabase: "NOT_CONNECTED";
  };
};

export const syntheticFallback: OperationsSnapshot = {
  contract_version: "1.0.0",
  mode: "SYNTHETIC_READ_ONLY",
  milestones: [
    { id: "M0", label: "Repository & Development Harness", status: "VERIFIED" },
    { id: "M1", label: "Machine Contracts", status: "VERIFIED" },
    { id: "M2", label: "State & Governance Core", status: "VERIFIED" },
    {
      id: "M3",
      label: "California Data Spike Readiness",
      status: "GOVERNANCE_READY_REAL_ACQUISITION_BLOCKED",
    },
  ],
  source_registry: {
    approved_real_sources: 0,
    real_acquisition: "BLOCKED",
    beneficiary_matching: "BLOCKED",
  },
  raw_artifact: {
    artifact_id: "synthetic:m3-operations-console-demo",
    sha256: "d8f9fb455e7c7cc962a71f11201ef8b5d8922262b3010bd7a84afc711c8b279f",
    byte_count: 49,
    content_type: "text/plain",
    source_id: "synthetic-m3-demo",
    source_uri: "synthetic://m3/operations-console",
    authority: "UNCLAIMED_PLATFORM_TEST_FIXTURE",
    acquisition_method: "SYNTHETIC_FIXTURE",
    retrieved_at: "2026-09-13T00:00:00Z",
    provenance_sha256: "f4e9c9868f9fb7f10d19c00135019afd9262df5ac209e070a13b51b8af5319ee",
    synthetic: true,
    immutable: true,
  },
  governance: {
    privacy_gate: "PASS_SYNTHETIC_ONLY",
    source_approval_gate: "BLOCKED_NO_REAL_SOURCE",
    retention_policy: "REQUIRED",
    pii_mode: "NO_REAL_PII",
  },
  audit: { chain: "HEALTHY_SYNTHETIC", algorithm: "SHA-256", durable_backend: "PENDING" },
  platform: { vercel: "NOT_CONNECTED", supabase: "NOT_CONNECTED" },
};

function isSnapshot(value: unknown): value is OperationsSnapshot {
  if (typeof value !== "object" || value === null) return false;
  const candidate = value as Partial<OperationsSnapshot>;
  return candidate.contract_version === "1.0.0" && candidate.mode === "SYNTHETIC_READ_ONLY";
}

export async function getOperationsSnapshot(): Promise<{
  data: OperationsSnapshot;
  source: "backend" | "synthetic-fallback";
}> {
  const baseUrl = process.env.REVIEWER_API_BASE_URL;
  if (!baseUrl) return { data: syntheticFallback, source: "synthetic-fallback" };

  try {
    const response = await fetch(`${baseUrl.replace(/\/$/, "")}/api/reviewer/m3/operations`, {
      cache: "no-store",
    });
    if (!response.ok) return { data: syntheticFallback, source: "synthetic-fallback" };
    const payload: unknown = await response.json();
    return isSnapshot(payload)
      ? { data: payload, source: "backend" }
      : { data: syntheticFallback, source: "synthetic-fallback" };
  } catch {
    return { data: syntheticFallback, source: "synthetic-fallback" };
  }
}
