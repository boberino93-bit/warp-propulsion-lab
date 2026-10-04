# Agent Bootstrap Contract

Project ID: `warp-propulsion-lab`
Authorized repository: `boberino93-bit/warp-propulsion-lab`
Internal forum namespace: `warp-propulsion-lab::messages`
Preferred forum path: `.interagent/messages`

Before any mutation, a new agent MUST:

1. Determine that it was started for `warp-propulsion-lab` from the project environment or explicit human instruction.
2. Determine its assigned role (`primary`, `manager`, `research`, `recovery`, `qa`, or `build`).
3. Read the project-local internal message/forum state before changing repository state.
4. Read available handoff/state files (`PROJECT_MANIFEST.json`, `START_HERE.md`, and `.interagent/messages` when present).
5. Bind mutation authority only to `boberino93-bit/warp-propulsion-lab`.
6. Emit: `IDENTITY RESOLVED: project=warp-propulsion-lab; role=<role>; forum=warp-propulsion-lab::messages; repositories=boberino93-bit/warp-propulsion-lab; state=<handoff/state ref>`.
7. Only then begin role-specific work.

Fail closed before mutation if project, role, forum, handoff, or repository identity is missing or conflicting. Never infer another repository from similarity. Cross-project communication or mutation requires explicit human authorization and the Intercommunications Enhancements routing protocol.
