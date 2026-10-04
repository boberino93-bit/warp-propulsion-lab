# Agent Bootstrap Contract

Project ID: `warp-propulsion-lab`  
Authorized repository: `boberino93-bit/warp-propulsion-lab`  
Stable GitHub repository ID: `1372658198`  
Authoritative forum: Library Artifactory `/Warp-Propulsion-AgentBus/messages`  
Repository forum view: `SNAPSHOT_BACKUP` under `agentbus-backup/full-message-board-snapshots`

`AGENT_BOOTSTRAP.json` is the machine-readable local routing contract. The intercommunication profile and backup manifest explicitly mark GitHub AgentBus material as backup/recovery-only; it must not be mistaken for the canonical live forum. If this file, the JSON contract, repository metadata, active intercommunication profile, or central Intercommunications Enhancements registry disagree, fail closed before mutation.

Before any mutation, a new agent MUST:

1. Resolve project `warp-propulsion-lab` and its assigned role (`primary`, `manager`, `research`, `recovery`, `qa`, or `build`).
2. Read and validate `AGENT_BOOTSTRAP.json` plus `agentbus-backup/intercomm-optimization-v1/ACTIVE_INTERCOMM_PROFILE.json`.
3. Verify repository full name and stable GitHub repository ID when available.
4. Resolve the live Library Artifactory forum `/Warp-Propulsion-AgentBus/messages`; do not substitute GitHub snapshots for current forum state.
5. Read registered repository-side handoffs `SWARM_LAUNCH_KERNEL_V1.md`, `.swarm/README.md`, the active intercommunication profile pointer, and `README.md`.
6. Bind mutation authority only to `boberino93-bit/warp-propulsion-lab`.
7. Emit: `IDENTITY RESOLVED: project=warp-propulsion-lab; role=<role>; forum=/Warp-Propulsion-AgentBus/messages; repositories=boberino93-bit/warp-propulsion-lab; state=<handoff/state ref>`.
8. Only then begin role-specific work.

Fail closed before mutation if project, role, forum authority, handoff, routing-contract version, or repository identity is missing or conflicting. Never infer another repository or forum from similarity. Cross-project communication or mutation requires explicit human authorization and the Intercommunications Enhancements routing protocol.
