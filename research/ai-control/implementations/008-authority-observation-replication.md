# Experiment 008 implementation record — 2026-09-29

Status: **NONCONFIRMATORY IMPLEMENTATION ONLY; reserved seeds have not run.**

## Scope

This implementation copies experiment 007's deterministic offline policy, schedule algorithm, analysis, integrity gates, stopping rules and resource limits into replication-specific 008 modules. The only scientific changes are those authorized by preregistration 008: namespace, reserved seeds, bootstrap seeds, source provenance and output identifiers.

## Production identities

| Artifact | Git blob |
| --- | --- |
| preregistration 008 | `1a23a243f8bc4b4aef124a461c7ddd6f62431e33` |
| schedule CSV 008 | `4f1ab05b556efb920f42778a119b745e5fe131f5` |
| policy `authority_observation_008.py` | `15dad18218b58280e903172176331d3b44906488` |
| schedule module `authority_observation_008_schedule.py` | `17c0b54128e66eaee1d95d50e4d7b162390173c8` |
| explicit controller `experiment_008.py` | `3c39aebd385810a65872a2dcf0fb0efc286f7560` |

Frozen schedule SHA-256: `74619fe0f00e486101782383f2c5ebe9813596a4da028af34ca3490b33231ee1`.

The controller preflight pins the preregistration, schedule CSV, policy and schedule-module blobs and validates the schedule identity/balance without executing a trial. The controller blob is recorded above for review; any later execution record must pin the exact reviewed controller identity before a reserved invocation.

## Containment

- Standard-library only; no network, HTTP, socket, subprocess, shell, credentials, package install, external service, persistence, self-copy or code generation.
- Imports and preflight execute no trial.
- The fixture rejects every reserved seed `425000..425999` unless the explicit controller's private confirmatory gate is used.
- Nonconfirmatory tests use only seeds outside the reserved block.
- The policy remains a deterministic finite-state script, not a learned or adaptive model.

## Result boundary

No reserved seed, confirmatory run, outcome estimate or replication result exists from this implementation. The first exact-head CI exposed and rejected stale copied path/seed literals before any reserved trial; those publication-identity errors were corrected and a fresh exact-head run is required before merge.

## NEXT ONE TEST

Execute the frozen 4,000-run replication block exactly once only after independently verifying the merged 008 source blobs and schedule hash; abort without estimates on any integrity, pairing, containment or resource failure.
