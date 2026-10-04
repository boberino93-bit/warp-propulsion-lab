# Swarm Launch Kernel — Agent Bootstrap Overlay

Applies to PRIMARY, MANAGER, and RESEARCH. Validate existing project identity first; load `swarm_kernel/project.json` and require exact binding; bind exactly one `global_run_id`; publish local READY; wait for the local start gate; use versioned leases and deterministic idempotency keys; heartbeat/checkpoint active leases; respect Manager backpressure; quarantine stale/wrong-project/malformed/unsupported/illegal cross-project commands; stop integration mutations under `DEGRADED_READ_ONLY`; and close leases plus persist convergence/recovery state before handoff.

Role authority is unchanged: Research produces evidence, Manager reviews/coordinates, Primary/local integration authority accepts project truth. Cross-project health is read-only observation only.
