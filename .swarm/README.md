# `.swarm/` Project-Local Runtime Namespace

Reserved for Swarm Launch Kernel records. Use sharded immutable/per-task records rather than one shared mutable state file. Records are bound to this project and a `global_run_id`. Other projects may only read published health telemetry where permitted. GitHub claims use create-if-absent; updates use current blob SHA plus expected lease version; stale writers reread/reconcile/back off and never force-push.
