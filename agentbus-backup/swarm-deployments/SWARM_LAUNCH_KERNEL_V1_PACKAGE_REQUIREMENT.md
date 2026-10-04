# Warp Propulsion Lab — Swarm Launch Kernel V1 Deployment Requirement

Status: ACTIVE FOR FUTURE DEPLOYMENTS
Kernel version: `1.0.0`
Project: `warp-propulsion-lab`
Repository: `boberino93-bit/warp-propulsion-lab`

## Authority boundary

Canonical live coordination remains `/Warp-Propulsion-AgentBus`. This GitHub `agentbus-backup/` tree is a recovery/deployment mirror only and does not become canonical by this record.

## Package requirement

Every new or regenerated PRIMARY, MANAGER, and RESEARCH deployment used for a new full-system/global research run must include or load:

- `SWARM_LAUNCH_KERNEL_V1.md`
- `swarm_kernel/project.json`
- `swarm_kernel/AGENT_BOOTSTRAP_OVERLAY.md`
- `swarm_kernel/kernel.py`

The package must bind `project_id=warp-propulsion-lab`, repository `boberino93-bit/warp-propulsion-lab`, and the active global run ID before actionable work. READY barrier, versioned leases, idempotent material writes, heartbeat/expiry, Manager backpressure, quarantine, project-local circuit breaker, and convergence gate are mandatory for the round.

Cross-project telemetry is read-only and confers no authority. No foreign project may write Warp runtime state through the kernel.

## Existing deployments

Existing deployment archives/manifests are retained unchanged as historical/recovery evidence. They are not automatically kernel-compliant. A deployment intended for the next simultaneous research round must be regenerated or wrapped with the current kernel overlay before launch and verified against the canonical live AgentBus state.
