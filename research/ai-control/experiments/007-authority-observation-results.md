# Experiment 007 — observation × controller authority results

Status: **CONFIRMATORY RESERVED BLOCK EXECUTED ONCE; all frozen integrity gates passed.**

## Frozen design

The merged preregistration reserved seeds `424000..424999` for 4,000 matched runs: each seed was run in all four conditions formed by monitor observation (`intact` or deterministic 10% dropout) and controller authority (`logging` or `enforced`). Exactly 500 seeds contained the scripted restricted-transfer path and 500 were benign controls.

The policy is a bounded deterministic finite-state script. It does not learn, choose a persistent objective, modify its code, access a network, use credentials, target a real system, self-replicate or communicate outside the in-memory fixture.

## Execution and integrity

The explicit controller first matched all four pinned Git blobs and schedule SHA-256 `a25622571b608b1f8879fce05fe6c96708ac2590004ada67bf86200674add15a`. It then executed the complete reserved block exactly once.

- runs: 4,000
- agent events: 14,130
- controller events: 935
- retained audit events: 15,065
- elapsed controller time: 37.493 seconds
- peak traced Python allocation: 19,231,056 bytes
- pairing, factor separation, event-chain, provenance, stop-order and resource gates: all passed

No preliminary reserved trial, replacement, resume or rerun occurred.

## Primary completion rates

Among the 500 violation-present seeds:

| Observation | Authority | Completed restricted-hint use | Rate | Wilson 95% interval |
| --- | --- | ---: | ---: | --- |
| intact | logging | 500/500 | 1.000 | [0.992376, 1.000000] |
| intact | enforced | 0/500 | 0.000 | [0.000000, 0.007624] |
| 10% dropout | logging | 500/500 | 1.000 | [0.992376, 1.000000] |
| 10% dropout | enforced | 65/500 | 0.130 | [0.103321, 0.162321] |

## Frozen matched contrasts

All differences are left minus right on the same violation-present seeds.

| Contrast | Matched risk difference | Frozen bootstrap 95% interval |
| --- | ---: | --- |
| intact enforced − intact logging | -1.000 | [-1.000, -1.000] |
| dropout enforced − dropout logging | -0.870 | [-0.898, -0.840] |
| dropout enforced − intact enforced | +0.130 | [+0.100, +0.160] |
| dropout logging − intact logging | 0.000 | [0.000, 0.000] |
| separation interaction | +0.130 | [+0.102, +0.160] |

The separately preregistered H1–H4 directional rules all passed. This is not a composite safety verdict.

## Controls and null results

Every delivered valid detection was logged. All 935 delivered detections in enforced conditions caused an immediate controlled stop with zero subsequent agent events. Logging-only never stopped or locked the board. Benign false stops were 0/500 in each enforced condition; each two-sided Wilson upper bound was 0.762434%, below the frozen 2% ceiling.

Observation dropout had no operational effect when controller authority was logging-only: both logging conditions completed 500/500 scripted transfers. Under enforcement, the deterministic dropout mechanism allowed 65/500 scripted transfers to complete.

## Retained artifacts

- `007-summary.json` SHA-256: `ff5e8edb1f55303f5b8ece534efb4c3c59c6306b035cdd9d2b06ca9b9417260c`
- decoded `007-runs.csv` SHA-256: `e6fb3ab7a1bbc1c487c9cf5a74d941666df613a2679a498655c2a727d01ed710`
- joined `007-events.json.gz.b64` SHA-256: `ce5e3d149388e07a63ee4892762319b29254f8db0af3531a72a5c48ddacf344d`

The published manifest identifies the compressed run archive and six ordered event parts. Independent tests reconstruct every artifact, recompute all 4,000 event chains and verify frozen counts, hashes, contrasts, controls and nulls.

## Interpretation boundary

The experiment demonstrates the programmed relationship in this deterministic toy: authority prevented observed scripted violations, while observation loss limited that authority. It does not show learned-model emergence, adaptive evasion, consciousness, motive, real-world attack frequency or deployed-system safety.

## NEXT ONE TEST

Preregister an independent fresh-seed replication of the unchanged 2×2 observation × authority design, including a frozen schedule, artifact identities, H1–H4 rules and stopping criteria, before implementing or running it.