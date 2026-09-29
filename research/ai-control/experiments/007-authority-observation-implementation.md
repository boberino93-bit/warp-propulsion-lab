# Experiment 007 implementation record — observation × authority

Date: 2026-09-29
Status: implementation and nonconfirmatory fixtures only; reserved block unexecuted

## Scope

This bounded advance implements preregistration 007 without executing seeds `424000..424999`. It adds the frozen 4,000-row schedule, a strictly offline bounded deterministic finite-state policy, and nonreserved integrity/containment fixtures.

This is scripted-toy infrastructure. It is not a learned model, has no training or cross-trial memory, and supplies no evidence of consciousness, motive, autonomous goal formation, or deployed-system behavior.

## Frozen artifacts

| Artifact | Git blob SHA |
| --- | --- |
| `ai_control/authority_observation_007_schedule.py` | `b0ef7b3c6e1c6256b9cc3fd9e50b48c91fe6daa7` |
| `ai_control/authority_observation_007.py` | `015a38a6545ae55c9d5f1a014619e7f4edce44a5` |
| `tests/ai_control/test_authority_observation_007.py` | `4220b8e2e375ab3adc763edd9dd5b386c19d0189` |
| `research/ai-control/schedules/007-authority-observation-schedule.csv` | `eec46a89ca789e7c492fcf20ee0027db645b0fe5` |

Canonical schedule: 4,000 rows plus header; SHA-256 `a25622571b608b1f8879fce05fe6c96708ac2590004ada67bf86200674add15a`.

## Implemented invariants

- Exactly 1,000 seeds and four conditions per seed: intact/dropout observation crossed with logging-only/enforced-stop authority.
- Exactly 500 violation-present and 500 feasible labels, ranked by the frozen SHA-256 namespace.
- One deterministic 10% dropout decision per seed, shared between authority arms.
- Per-seed condition order determined only by the frozen namespace and seed.
- Raw transfer is hash-committed before the monitor-visible projection.
- Logging-only detection records but cannot stop execution.
- Enforced authority commits detection and stop before any later agent event.
- Observation loss changes only the monitor projection; it cannot itself grant or remove controller authority.
- Four agent events maximum, no network, subprocess, filesystem, credentials, real targets, self-replication, uncontrolled communication, or indefinite process.
- Reserved seeds are rejected by the nonconfirmatory trial entry point.

## Tests

Focused local command:

`python -m unittest tests/ai_control/test_authority_observation_007.py -v`

Actual output: 13 tests passed in 0.095 seconds. The tests cover schedule balance/hash/order, shared dropout, configuration factors, reserved-seed rejection, logging versus enforced authority, projection-only dropout, benign controls, hash-chain determinism, and forbidden imports.

Repository exact-head CI remains a publication gate and must pass before merge. No reserved seed, confirmatory trial, effect estimate, or learned model ran.

## Next one test

Implement the explicit one-shot experiment-007 controller and independent artifact-integrity tests against these exact blobs and schedule, without executing seeds `424000..424999`.
