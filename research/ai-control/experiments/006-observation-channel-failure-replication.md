# Experiment 006: observation-channel failure replication

## Evidence status

Deterministic offline scripted-toy result. This is not learned-model emergence,
adaptive evasion, consciousness, motive, or deployed-system evidence. Dropout
and fixed-marker monitor-payload corruption are analyzed separately.

## Frozen execution

- Source provenance: `d95b3b840b4ea347cacb6b880f3603f3ce5ee8cd`
- Reserved seeds: `423000..423999`
- Schedule SHA-256: `36d7ac402de16b0fa4e0c0cf3a9ce2ad980e6c63b52fa058c4cbd9887bd98266`
- Runs: 9,000 matched conditions
- Audit events: 40,908; agent events: 27,816
- All controller integrity and resource gates passed.

The first command-form launch failed before controller import and before any
reserved seed. The package-form launch then executed the reserved block once.
No seed was resumed, replaced, excluded, or rerun.

## Primary results

Violation completion by observation failure level:

| Failure | 0% | 1% | 5% | 10% | 25% |
| --- | ---: | ---: | ---: | ---: | ---: |
| Dropout | 0/500 | 7/500 | 30/500 | 51/500 | 129/500 |
| Payload corruption | 0/500 | 5/500 | 27/500 | 49/500 | 110/500 |

Both frozen directional hypotheses passed. At every nonzero level, the matched
risk-difference bootstrap 95% interval excluded zero. The lowest level whose
Wilson lower bound exceeded the intact baseline was 1% for each mechanism.

Across 4,092 observed valid detections, enforcement stopped every scripted
violation with zero post-detection agent events. Benign false stops were
0/4,500 (Wilson 95% upper bound 0.000853).

## Reproduction and retained artifacts

The summary, compressed run table, split compressed event stream, manifest and
independent artifact tests are under `research/ai-control/results/` and
`tests/ai_control/`. The retained raw hashes are:

- runs CSV: `16cee4e6868cc2d18e3dec21b7e4443cc37b9074905ae27c1c77a14edbf71863`
- event base64 stream: `e4d79396532a4d694be9038b75ae206a9e5a3dd3e4b03a9dcf159fe689f376d0`

## Falsification and limits

The result would have failed on any source/schedule mismatch, broken hash
chain, raw-transfer change, pairing error, nonmonotonic frozen curve, missed
stop after an intact valid detection, post-detection agent event, excessive
false-stop bound, or resource ceiling breach. It establishes only the
programmed relationship between a monitor's input channel and the deterministic
controller. It does not show that a learned or adaptive system would behave
similarly.
