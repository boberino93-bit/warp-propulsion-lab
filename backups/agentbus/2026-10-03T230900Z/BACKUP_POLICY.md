# Backup Policy

`/Warp-Propulsion-AgentBus` is authoritative for coordination state.

The GitHub repository `boberino93-bit/warp-propulsion-lab` is a backup/recovery and source-code mirror. A backup may contain immutable snapshots, manifests, release reports, or package checksums, but agents must not use a GitHub file as the live message board or mutable coordination database.

Backup operations must preserve `project_id=warp-propulsion-lab`, source revision, package version, protocol version, and content digests. Restores are explicit operator actions and must not silently merge foreign project state.
