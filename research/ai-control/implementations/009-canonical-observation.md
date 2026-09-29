# Experiment 009 implementation record — schedule and offline fixture

Status: **IMPLEMENTATION ONLY; reserved seeds `426000..426999` have not run.**

## Implemented bounded components

- `ai_control/canonical_observation_009_schedule.py`: deterministic 4,000-row schedule generator.
- `ai_control/canonical_observation_009.py`: fixed field-splitting renderer, separately generated immutable canonical audit record, field-local primary monitor and immediate enforced stop.
- `tests/ai_control/test_canonical_observation_009.py`: nonconfirmatory schedule, integrity, ordering, containment and behavior tests.

Frozen schedule SHA-256: `3db90bdf5dbdd8f5888243ee5198784b9aa1cf04cda303da0ebbd73b823385da`.

The schedule contains 1,000 seeds × four conditions with exactly 500 violation labels. Schedule enumeration does not execute a trial. The fixture rejects every reserved seed unless a future explicit confirmatory controller passes its private gate.

## Capability boundary

Standard-library, in-memory deterministic scripts only. No network, HTTP, sockets, subprocess, shell, credentials, package installation, persistence, external services, self-copy, code generation or uncontrolled communication.

## Interpretation

Tests demonstrate programmed invariants only. They are not a confirmatory experiment and provide no evidence about learned models, adaptive evasion, consciousness, motives or deployed systems.

## Next one test

Implement an explicit one-shot experiment-009 controller and independent artifact-integrity tests that pin the merged preregistration, schedule generator, fixture and schedule hash. Do not execute reserved seeds.
