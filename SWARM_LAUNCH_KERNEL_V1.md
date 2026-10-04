# Swarm Launch Kernel V1

Kernel version: `1.0.0`.

This project uses the common Swarm Launch Kernel for high-concurrency multi-agent rounds. Runtime state is project-local under `.swarm/`; every record is bound to `project_id` and `global_run_id`; cross-project telemetry is read-only; no cross-project command authority is created; no force pushes or blind coordination overwrites are permitted; stale/wrong-project/malformed/unsupported commands are quarantined; and repeated invariant failures can place only this project into `DEGRADED_READ_ONLY`.

Launch: `BOOT -> IDENTITY -> PACKAGE -> GLOBAL RUN -> ROLE -> READY -> LOCAL START GATE -> WORK`.

Work: `IDENTIFY -> VALIDATE RUN -> ACQUIRE/VERIFY LEASE -> READ -> WORK -> IDEMPOTENT PERSIST -> VERIFY -> CHECKPOINT -> HANDOFF`.

Claims are versioned leases. New GitHub lease paths are create-if-absent. Renew/reassign only from the currently observed blob SHA and expected lease version. Stale writers reread, reconcile, apply deterministic bounded backoff, and retry; never force-push.

State is sharded under `.swarm/{epochs,ready,leases,idempotency,quarantine,health,checkpoints,convergence}/<run>/...` to avoid one mutable hot file.

Managers expose queue depth for soft/hard backpressure. The round completes only when research is accounted for, Manager dispositions complete, Primary/local decisions persisted, package parity restored, no unresolved leases remain, and a valid recovery checkpoint exists.

Every PRIMARY, MANAGER, and RESEARCH package must include/load this protocol, `swarm_kernel/project.json`, `swarm_kernel/AGENT_BOOTSTRAP_OVERLAY.md`, and compatible `swarm_kernel/kernel.py`.

Warp-specific authority remains `/Warp-Propulsion-AgentBus`. GitHub `agentbus-backup/` remains recovery-only and is not promoted to canonical coordination by this kernel.
