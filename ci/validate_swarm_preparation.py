"""Fail-closed static validation for Warp Propulsion Lab swarm preparation.

This validator proves repository-side preparation only. It intentionally cannot
prove canonical AgentBus reconciliation, a shared global_run_id, runtime READY
records, or an open start gate.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
V3 = ROOT / "agentbus-backup" / "swarm-deployments" / "warp-bipolar-swarm-20261007-v3-kernel"
EXPECTED_PROJECTS = [
    "ai-behaviour-control-lab",
    "benefitflow",
    "duo-open",
    "fold7-power-lab",
    "intercommunicationsenhancements",
    "warp-propulsion-lab",
    "xrp-thesis",
]
EXPECTED_LANES = {*(f"R{i:02d}" for i in range(1, 11)), "M01", "M02"}


def load(path: Path) -> dict:
    if not path.is_file():
        raise AssertionError(f"required file missing: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    project = load(ROOT / "swarm_kernel" / "project.json")
    handoff = load(ROOT / "MASTER_HANDOFF.json")
    manifest = load(V3 / "MANIFEST.json")
    binding = load(V3 / "GLOBAL_RUN_BINDING.template.json")
    deployment = manifest["deployment"]

    require(project["project_id"] == "warp-propulsion-lab", "wrong project_id")
    require(project["repository"] == "boberino93-bit/warp-propulsion-lab", "wrong repository")
    require(project["kernel_version"] == "1.2.1", "project kernel must be 1.2.1")
    require(project["expected_global_round_projects"] == EXPECTED_PROJECTS, "project set mismatch")
    require(project["master_handoff_required_before_ready"] is True, "master handoff must be required")

    require(handoff["project_id"] == project["project_id"], "handoff project mismatch")
    require(handoff["repository"] == project["repository"], "handoff repository mismatch")
    require(handoff["kernel"]["version"] == project["kernel_version"], "handoff kernel mismatch")
    require(handoff["kernel"]["expected_global_round_projects"] == EXPECTED_PROJECTS, "handoff project set mismatch")
    require(handoff["kernel"]["global_run_id"] is None, "handoff must not invent global_run_id")
    require(handoff["coordination"]["canonical_state_reconciliation_required"] is True, "handoff must preserve canonical reconciliation gate")
    require(handoff["deployment"]["scientific_payloads_mutated"] is False, "scientific payload mutation prohibited")

    require(manifest["authority"] == "NON_AUTHORITATIVE_RECOVERY_ONLY", "GitHub wrapper must remain non-authoritative")
    require(manifest["canonical_promotion_state"] == "PENDING_PROJECT_PRIMARY_AGENTBUS_RECONCILIATION", "V3 must not claim canonical promotion")
    require(deployment["status"] == "PREPARED_NOT_CANONICAL", "V3 status must remain pre-canonical")
    require(deployment["project_id"] == project["project_id"], "V3 project mismatch")
    require(deployment["repository"] == project["repository"], "V3 repository mismatch")
    require(deployment["swarm_kernel"]["version"] == project["kernel_version"], "V3 kernel mismatch")
    require(deployment["swarm_kernel"]["expected_global_round_projects"] == EXPECTED_PROJECTS, "V3 project set mismatch")
    require(deployment["swarm_kernel"]["global_run_id"] is None, "V3 must not invent global_run_id")
    require(deployment["research_scientific_contract"] == "UNCHANGED_FROM_V1", "scientific contract changed")
    require(deployment["scientific_payloads_mutated"] is False, "scientific payload mutation prohibited")
    require(deployment["canonical_reconciliation_required"] is True, "canonical reconciliation gate missing")

    lanes = deployment["lanes"]
    lane_ids = [lane["lane"] for lane in lanes]
    require(len(lane_ids) == len(set(lane_ids)), "duplicate lane IDs")
    require(set(lane_ids) == EXPECTED_LANES, "lane population mismatch")
    for lane in lanes:
        require(
            lane["source_task_path"].startswith(
                "/Warp-Propulsion-AgentBus/tasks/warp-bipolar-swarm-20261004-v1/"
            ),
            f"{lane['lane']} no longer points to frozen V1 scientific payload",
        )

    cap = project["max_active_specialists"]
    formation = deployment["formation"]
    require(formation["max_active_specialists"] == cap == 8, "capacity contract mismatch")
    require(formation["research_agents"] == 10, "research population mismatch")
    require(formation["manager_agents"] == 2, "manager population mismatch")
    require(formation["primary_agents"] == 1, "primary population mismatch")
    require(formation["total"] == 13, "total population mismatch")
    require(len(deployment["capacity_plan"]["wave_a"]) <= cap, "Wave A exceeds capacity")
    require(len(deployment["capacity_plan"]["wave_b"]) <= cap, "Wave B exceeds capacity")

    require(binding["kernel_version"] == project["kernel_version"], "binding kernel mismatch")
    require(binding["expected_global_round_projects"] == EXPECTED_PROJECTS, "binding project set mismatch")
    require(binding["global_run_id"] == "<EXTERNALLY_SUPPLIED_SHARED_VALUE_REQUIRED>", "binding template was prematurely bound")

    required = deployment["swarm_kernel"]["required_files"]
    for rel in required:
        require((ROOT / rel).is_file(), f"kernel required file missing: {rel}")

    runtime_gates = handoff["launch_gates"]
    require(runtime_gates["canonical_agentbus_reconciled"] is False, "repo preparation must not self-certify AgentBus reconciliation")
    require(runtime_gates["shared_global_run_id_received"] is False, "repo preparation must not self-certify a shared run")
    require(runtime_gates["local_start_gate_open"] is False, "repo preparation must not open runtime start gate")

    print("SWARM_PREPARATION_STATIC_PASS")
    print("Runtime gates still required: canonical AgentBus reconciliation, shared global_run_id, READY barrier, local start gate.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"SWARM_PREPARATION_STATIC_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
