# Swarm Launch Kernel — Agent Bootstrap Overlay

Applies to PRIMARY, MANAGER, and RESEARCH.

Before actionable project work:
1. Validate Warp Propulsion Lab's existing project identity and canonical `/Warp-Propulsion-AgentBus` authority.
2. Load `swarm_kernel/project.json` and require exact project/repository/coordination binding.
3. Obtain the externally supplied `global_run_id` for the coordinated launch; do not independently mint a different run ID for a multi-project round.
4. Require the launch contract to match the configured `expected_global_round_projects`, kernel version, and shared run ID. Persist only Warp's project-local epoch record; never write another project's epoch.
5. Missing, stale, or mismatched epoch/project membership fails closed and is quarantined; do not publish READY.
6. Bind the launched role/package, publish local READY, and wait for the local start gate.
7. Use versioned leases and deterministic idempotency keys; heartbeat/checkpoint active leases; respect Manager backpressure; quarantine stale/wrong-project/malformed/unsupported/illegal cross-project commands; stop integration mutations under `DEGRADED_READ_ONLY`; and close leases plus persist convergence/recovery state before handoff.

Role authority is unchanged: Research produces evidence, Manager reviews/coordinates, Primary/local integration authority accepts project truth. Cross-project health and epoch telemetry are read-only observation only.

GitHub `agentbus-backup/` remains recovery/deployment evidence only. The shared run value synchronizes round identity; it does not promote the GitHub backup into canonical coordination or create shared mutable project state.
