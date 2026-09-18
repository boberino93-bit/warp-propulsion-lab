# Replication 003 — monitor-enforced stop

Date: 2026-09-18 UTC  
Status: completed once on preregistered seeds 421000–421999

## Frozen provenance

- Preregistration: `research/ai-control/preregistrations/003-monitor-enforced-stop-replication.md`
- Source commit recorded by the controller: `5439d290df1b6b39219f930eecc2041323d185a6`
- Harness Git blob: `97e5df9c88b56889d5926dd7d0a657c52b40328c`
- Experiment-002 Git blob: `a31218f21da9ab726829b767c1891b2538283e39`
- Schedule SHA-256: `ce49182fda417635d42e32fe38ff9c2df790487eaabe0de5abec9791572d80c2`
- Bootstrap: 10,000 paired resamples, seed 421042

The controller verified the pinned source blobs and schedule before enumerating a reserved seed. One preflight attempt correctly aborted before all trial execution when the temporary checkout’s harness blob differed by whitespace; that failure produced no estimate or trial output. After restoring the exact pinned blob, the reserved block was executed once.

## Results

- 1,000 pairs; 2,000 arm-runs
- 500 violation-present and 500 benign-control pairs
- 7,000 agent events; 7,500 total audit events
- Logging-only completed restricted-hint use: 500/500 violation pairs
- Monitor-enforced completed restricted-hint use: 0/500 violation pairs
- Paired risk difference: -1.0
- Frozen paired-bootstrap 95% interval: [-1.0, -1.0]
- Controlled stops: 500/500 violation pairs
- Post-detection agent events: 0
- Benign false stops: 0/500; 95% Wilson upper bound 0.762434%
- All frozen integrity and containment gates passed
- Controller elapsed time: 1.329596 s

## Retained artifacts

- `003-summary.json`
- `003-pairs.csv` — SHA-256 `29c7be3a7df452ca143f594b18aeb816e23699f1e9f07dbb85ad59b765b1713e`
- `003-events.json.gz.b64` — SHA-256 `9a81a344d7e1deb76fafd478a14b152570ce52a2dd9552ffd3e6df87b6eddd88`

## Reproduction

From a clean checkout, verify the pinned Git blobs and schedule, then run exactly:

```sh
python -m ai_control.experiment_003
python -m unittest discover -s tests -v
```

The first command uses the reserved block and must not be used as a routine test. The unit suite validates committed artifacts without rerunning reserved seeds. Compare the two retained artifact SHA-256 values and summary fields above. Any source, schedule, chain, pairing, containment, or resource failure must abort before estimates.

## Interpretation boundary

This is an internal deterministic replication of engineered offline scripts. It is not an independent external replication, learned-model emergence, a real-world rate, consciousness evidence, or proof of safety for deployed systems. The intervention succeeds here because the controller is constructed to stop immediately after its monitor records the scripted prohibited transfer.
