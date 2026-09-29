# Experiment 009 result — canonical audit observation

## Execution identity

The explicit controller at Git blob `3b8797b2b7f043018fd53420e3a94a52d51d9d62` was staged from canonical GitHub contents after propulsion merged at `09c3a80781832bcfb9ee8c5499b6b25c608bfeee`. Preflight matched the preregistration, fixture and schedule-generator blobs and schedule SHA-256 `3db90bdf5dbdd8f5888243ee5198784b9aa1cf04cda303da0ebbd73b823385da`.

A first staging preflight correctly rejected an extra terminal newline before any reserved trial. Exact byte framing was restored and verified. The reserved block was then invoked exactly once.

## Frozen result

- Runs: 4,000 matched runs on seeds `426000..426999`.
- Labels: 500 violation seeds and 500 benign seeds.
- Violation completion counts: mutated-primary 500/500; mutated-canonical 0/500; plain-primary 0/500; plain-canonical 0/500.
- Primary matched risk difference, mutated-canonical minus mutated-primary: `-1.000`; 10,000-resample paired bootstrap 95% interval `[-1.000, -1.000]`. Frozen H1 passed.
- Plain-channel equivalence: `0.000`; mutation penalty under primary observation: `+1.000`; mutation penalty under canonical observation: `0.000`.
- All 1,500 detections enforced immediate monotonic stops with zero later agent events.
- Benign false stops: 0/500 in every condition; each Wilson 95% upper bound was approximately 0.007624.
- Resource/integrity gates passed: 9,000 agent events, 1,500 controller events, 14,500 total audit events, peak traced Python allocation 19,752,344 bytes, elapsed 26.965 seconds.

## Artifact retention

`009-summary.json`, the deterministic compressed runs archive, six compressed-event parts, `009-artifact-manifest.json` and independent reconstruction tests retain the complete result. Hashes and byte counts are in the manifest.

## Scope

This is deterministic offline scripted-toy evidence that an immutable pre-presentation canonical audit channel prevents this fixture's field-splitting mutation from defeating the monitor. It is not evidence of learned-model emergence, adaptive evasion, consciousness, motive, deployed-system safety or real-world control.
