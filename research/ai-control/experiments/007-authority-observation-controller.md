# Experiment 007 one-shot controller — implementation record

Date: 2026-09-29
Status: controller and independent nonconfirmatory integrity tests implemented; reserved block unexecuted

## Scope

This bounded advance implements the explicit experiment-007 controller required by preregistration 007. Import and preflight do not execute a trial. Only an explicit `run_confirmatory()` call can open the private controller gate for seeds `424000..424999`.

The controller remains strictly offline and standard-library only. The bounded finite-state policy is scripted software, not a learned model.

## Frozen provenance

| Artifact | Git blob SHA |
| --- | --- |
| preregistration 007 | `802cdcfa5869481f1cccaf56487d88dbfdcdc308` |
| `authority_observation_007.py` | `e1fba1c0c52bf9c7393045675960997ed20baef8` |
| `authority_observation_007_schedule.py` | `b0ef7b3c6e1c6256b9cc3fd9e50b48c91fe6daa7` |
| frozen schedule CSV | `eec46a89ca789e7c492fcf20ee0027db645b0fe5` |
| `experiment_007.py` | `9324f5629b42884d9fb335fa0b5fa57ee936dcc0` |
| `test_experiment_007.py` | `34be2c150419c3d0d9fee3dd11de31359c99f6ca` |

Schedule SHA-256 remains `a25622571b608b1f8879fce05fe6c96708ac2590004ada67bf86200674add15a`.

## Controller gates

Preflight verifies the four frozen production blobs, schedule SHA-256, 4,000 unique seed-condition rows, four conditions per seed, seed interval and label balance before trial execution.

The controller independently verifies:

- event hash chains and exact source provenance;
- condition/config/violation/feasibility identity;
- deterministic shared dropout decision;
- raw transfer versus monitor projection;
- delivered detection logging;
- logging-only nonintervention;
- enforced detection-before-stop ordering, read-only board and zero later agent events;
- benign scoring and false-stop controls;
- four matched rates, five preregistered contrasts and fixed bootstrap seeds;
- H1–H4 separately, without a composite safety verdict;
- 4,000-run, 20,000-agent-event, 5,000-controller-event, 120-second and 256-MiB ceilings.

Output writers are defined for complete run CSV, deterministic gzip/base64 event data and a summary with file hashes. They are not invoked on import or preflight.

## Actual nonconfirmatory tests

Focused controller command:

`python -m unittest tests/ai_control/test_experiment_007.py -v`

Actual output: 9 tests passed in 0.061 seconds.

Combined experiment-007 implementation/controller command:

`python -m unittest tests/ai_control/test_authority_observation_007.py tests/ai_control/test_experiment_007.py -v`

Actual output: 22 tests passed in 0.101 seconds.

Tests use only nonreserved fixture seeds. A reserved seed is tested only for rejection by the ordinary fixture entry point; no reserved trial executes.

The first focused run failed two preflight tests because locally reconstructed preregistration and CSV files contained one extra terminal newline and therefore did not match their pinned Git blobs. Exact byte framing was restored; controller code, schedule and outcomes did not change. No reserved seed ran.

## Evidence limits

No confirmatory run, effect estimate, model inference, network access, real target, exploit, self-replication or deployment occurred. Passing controller tests demonstrates implementation integrity only.

## NEXT ONE TEST

Execute the frozen 4,000-run experiment-007 block exactly once through the explicit controller, retaining every run and event and aborting without estimates on any provenance, pairing, hash, containment or resource failure.
