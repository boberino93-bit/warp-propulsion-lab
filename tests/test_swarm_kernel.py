from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest

from swarm_kernel.kernel import (
    KERNEL_VERSION,
    SUPPORTED_PROJECT_KERNEL_VERSIONS,
    ProjectConfig,
    admission_state,
    backpressure_state,
    can_open_start_gate,
    circuit_state,
    convergence_gate,
    lease_transition_allowed,
    new_lease,
    preflight,
    ready_record,
    record_path,
    validate_binding,
)

ROOT = Path(__file__).resolve().parents[1]
CFG = ProjectConfig("example", "owner/example", "main", "Example-AgentBus/")
EXPECTED_PROJECTS = [
    "ai-behaviour-control-lab",
    "benefitflow",
    "duo-open",
    "fold7-power-lab",
    "intercommunicationsenhancements",
    "warp-propulsion-lab",
    "xrp-thesis",
]


class SwarmKernelTest(unittest.TestCase):
    def test_binding_and_path(self):
        with self.assertRaises(PermissionError):
            validate_binding(CFG, "other", "owner/example")
        with self.assertRaises(ValueError):
            record_path("leases", "../run", "task")
        self.assertEqual(
            record_path("leases", "run_1", "task_1"),
            ".swarm/leases/run_1/task_1.json",
        )

    def test_ready_record_binds_execution_instance(self):
        record = ready_record(
            CFG, "run_1", "agent_a", "instance_1", "PRIMARY", "1.0.0", "abc123"
        )
        self.assertEqual(record["agent_instance_id"], "instance_1")
        self.assertEqual(record["schema"], "swarm-kernel/ready/v2")
        self.assertEqual(record["kernel_version"], CFG.kernel_version)

    def test_gate_and_execution_instance_fenced_lease(self):
        self.assertFalse(can_open_start_gate(["a", "b"], ["a"])[0])
        now = datetime(2026, 1, 1, tzinfo=timezone.utc)
        lease = new_lease(CFG, "run_1", "task", "agent_a", "instance_1", 0, now)
        self.assertEqual(lease["version"], 1)
        self.assertEqual(
            lease_transition_allowed(lease, 1, "agent_a", "instance_1", now)[1],
            "RENEW",
        )
        self.assertEqual(
            lease_transition_allowed(lease, 1, "agent_a", "instance_2", now)[1],
            "STALE_INSTANCE",
        )
        self.assertEqual(
            lease_transition_allowed(lease, 1, "agent_b", "instance_b", now)[1],
            "LEASE_HELD",
        )
        self.assertEqual(
            lease_transition_allowed(
                lease,
                1,
                "agent_b",
                "instance_b",
                now + timedelta(seconds=CFG.lease_ttl_seconds + 1),
            )[1],
            "EXPIRED_RECLAIM",
        )

    def test_capacity_backpressure_and_circuit_breaker(self):
        self.assertEqual(circuit_state(CFG, 3), "DEGRADED_READ_ONLY")
        self.assertEqual(backpressure_state(CFG, 15), "HARD_STOP_SECONDARY_WORK")
        self.assertEqual(
            admission_state(CFG, 0, capacity_known=False),
            "CAPACITY_UNKNOWN_READ_ONLY",
        )
        self.assertEqual(
            admission_state(CFG, CFG.max_active_specialists, capacity_known=True),
            "MAX_ACTIVE_SPECIALISTS_REACHED",
        )
        self.assertEqual(admission_state(CFG, 1, capacity_known=True), "ADMIT")

    def test_real_project_contract_matches_current_runtime_contract(self):
        cfg = ProjectConfig.load(ROOT / "swarm_kernel" / "project.json")
        payload = json.loads((ROOT / "swarm_kernel" / "project.json").read_text())
        self.assertEqual(KERNEL_VERSION, "1.2.1")
        self.assertEqual(cfg.kernel_version, "1.2.1")
        self.assertEqual(cfg.project_id, "warp-propulsion-lab")
        self.assertEqual(cfg.repository, "boberino93-bit/warp-propulsion-lab")
        self.assertEqual(cfg.max_active_specialists, 8)
        self.assertTrue(payload["master_handoff_required_before_ready"])
        self.assertEqual(payload["expected_global_round_projects"], EXPECTED_PROJECTS)

    def test_legacy_project_contract_is_explicitly_supported(self):
        payload = {
            "kernel_version": "1.0.0",
            "project_id": "legacy-project",
            "repository": "owner/legacy-project",
            "canonical_branch": "main",
            "coordination_root": "Legacy-AgentBus/",
            "state_root": ".swarm",
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "project.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            cfg = ProjectConfig.load(path)
        self.assertIn(cfg.kernel_version, SUPPORTED_PROJECT_KERNEL_VERSIONS)
        self.assertEqual(cfg.kernel_version, "1.0.0")

    def test_unknown_future_project_contract_fails_closed(self):
        payload = {
            "kernel_version": "9.9.9",
            "project_id": "future-project",
            "repository": "owner/future-project",
            "coordination_root": "Future-AgentBus/",
            "state_root": ".swarm",
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "project.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unsupported swarm-kernel version"):
                ProjectConfig.load(path)

    def test_preflight_requires_handoff_instance_capacity_and_tests(self):
        checks = {
            "identity_binding": True,
            "instance_binding": True,
            "run_epoch": True,
            "role_binding": True,
            "master_handoff_loaded": True,
            "package_parity": True,
            "capacity_admission": True,
            "recovery_state": True,
            "manager_presence": True,
            "foreign_write_policy": True,
            "tests": False,
        }
        result = preflight(CFG, checks)
        self.assertFalse(result["ready"])
        self.assertIn("tests", result["failed"])

    def test_convergence_requires_handoff_checkpoint(self):
        self.assertFalse(
            convergence_gate(
                research_accounted=True,
                manager_dispositions_complete=True,
                primary_decisions_persisted=True,
                package_parity_restored=True,
                unresolved_leases=0,
                recovery_checkpoint_valid=True,
                master_handoff_checkpointed=False,
            )["complete"]
        )


if __name__ == "__main__":
    unittest.main()
