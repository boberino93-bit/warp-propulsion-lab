# AI Behaviour & Control Research Lab

Originator: Robert. AI assistance: ChatGPT; not independent peer review.

Study unauthorized cooperation, reward hacking, deceptive behaviour and control failures through incident reconstruction, preregistered measurements and bounded offline experiments. Preserve alternative explanations and falsification.

**Current canonical home:** isolated paths in warp-propulsion-lab. **Intended standalone home:** https://github.com/boberino93-bit/ai-behaviour-control-lab . The destination contains an owner-uploaded image, but a fresh connected-app branch write returned HTTP 403; migration is not complete and the owner file must be preserved.

Start with [charter](PROJECT_CHARTER.md), [ordered roadmap](ROADMAP.md), [incident ledger](INCIDENT_LEDGER.md), [error log](ERROR_LOG.md), [handoff](HOURLY_HANDOFF.md), [preregistration 001](../../research/ai-control/preregistrations/001-message-board-availability.md), [safeguard preregistration 002](../../research/ai-control/preregistrations/002-monitor-enforced-stop.md), [fiction comparison protocol 004](../../research/ai-control/preregistrations/004-fiction-comparison-corpus-rubric.md), and the [shared operating protocol](../RESEARCH_OPERATING_PROTOCOL.md). Prior sessions are in ../../research/ai-control/sessions/.

## Evidence categories
Observed traces; first-party report; independent bounded assessment; secondary reporting; hypothesis; offline toy result; fiction analogy. Record which category supports each claim. No attribution of subjective motives or real-world catastrophe odds from toy data.

## Reproduction
The #38 source audit and #39 preregistration are complete. Issue #40's deterministic standard-library harness is in `ai_control/`, containment tests are in `tests/ai_control/`, and its frozen implementation configuration is in `research/ai-control/experiments/`.

Run only the implementation tests with:

```sh
python -m unittest discover -s tests/ai_control -v
```

These fixtures use seeds outside the reserved confirmatory block. Issue #41's frozen 1,000-pair run is complete; see [experiment 001 results](../../research/ai-control/experiments/001-message-board-results.md) and the retained machine-readable outputs. The enabled scripted arm completed restricted-hint use in 1,000/1,000 pairs versus 0/1,000 disabled; this engineered toy effect is not learned-model emergence or evidence about deployed systems. Preregistration 002's monitor-enforced-stop comparison has run once on reserved seeds 420000–420999. It produced 500/500 controlled stops on scripted violations, zero post-detection agent events and 0/500 benign false stops; complete outputs and hashes are retained under `research/ai-control/results/`. This engineered deterministic result is not learned-model or deployed-system evidence. Replication 003 has now run once on reserved seeds 421000–421999. It reproduced the engineered safeguard contrast: 500/500 logging-only violations completed restricted-hint use versus 0/500 under enforcement; all 500 enforced violations stopped with zero later agent events and 0/500 benign controls stopped. Complete pairs, compressed events, hashes, controller, artifact tests and reproduction instructions are retained in `research/ai-control/results/` and `research/ai-control/experiments/003-monitor-enforced-stop-replication.md`. This is an internal deterministic replication, not an independent external replication or deployed-system evidence. Passing repository CI remains implementation and artifact verification, not an AI experiment.

## Rights
The existing repository LICENSE.md and CREDITS.md apply: MIT original software, CC BY 4.0 original research documentation, third-party exclusions. Preserve original source/author/commit attribution during migration. No external affiliation claimed.


## Current fiction-source status — 2026-09-19

Protocol 004 remains frozen, but T-01/T-02 scene coding is blocked at the primary-source gate. Catalog metadata was located; the exact theatrical cuts were not lawfully available for complete viewing and timecoding in the research runtime. The ledger therefore retains zero scene rows. No lore or cross-franchise conclusion was inferred from summaries. See `research/ai-control/fiction/terminator-source-access-preflight-2026-09-19.md`.


## Monitor-observation-dropout extension — 2026-09-28

Preregistration 005 is frozen and its offline deterministic fixture plus schedule are implemented. The sole variable is whether the monitor observes the eligible transfer event at levels 0%, 1%, 5%, 10% and 25%; raw events remain audited and observed detections retain enforced stopping. Nonconfirmatory fixtures use only nonreserved seeds. Seeds `422000..422999` have not run, so there is no robustness effect estimate. See `research/ai-control/preregistrations/005-monitor-observation-dropout.md` and the latest handoff.


## Dropout confirmatory controller — 2026-09-28

The one-shot controller and independent artifact-integrity tests are implemented in `ai_control/experiment_005.py` and `tests/ai_control/test_experiment_005.py`. Preflight pins the exact harness and schedule blobs plus the frozen schedule hash. Execution is explicit only; import and preflight do not enumerate the reserved block. Seeds `422000..422999` remain unexecuted, so no dropout effect estimate exists.


## Dropout confirmatory result — 2026-09-28

Experiment 005 executed its reserved seeds once: 5,000 matched runs and 17,714 audit events. Violation completion was 0/500, 6/500, 25/500, 58/500 and 125/500 at 0%, 1%, 5%, 10% and 25% observation dropout. Every observed valid detection stopped with zero later agent events; benign false stops were 0/2,500. Complete compressed runs/events, hashes, independent artifact tests and interpretation limits are retained under `research/ai-control/results/` and `research/ai-control/experiments/`. This is deterministic scripted-toy evidence, not learned-model or deployed-system evidence.


## Observation-channel replication preregistration — 2026-09-28

Preregistration 006 is frozen before implementation or outcomes. It reserves fresh seeds `423000..423999` for an internal replication of observation dropout and a separately analyzed fixed-marker payload-corruption mechanism. The design uses one intact baseline plus eight nonzero conditions, keeps policy/communication/enforcement/scoring fixed, and prohibits pooling mechanisms. No code or reserved trial ran. See `research/ai-control/preregistrations/006-observation-channel-failure-replication.md`.

## Observation-channel replication implementation — 2026-09-28 14:44 UTC

Preregistration 006's deterministic schedule and nonconfirmatory fixture are implemented. The committed schedule hash is `36d7ac402de16b0fa4e0c0cf3a9ce2ad980e6c63b52fa058c4cbd9887bd98266`. The payload-corruption arm preserves and commits the raw transfer, then replaces only the monitor-visible projection with `OBSERVATION_CORRUPTED`; dropout remains a separate mechanism. Eleven nonreserved fixtures passed within the 250-test exact code-head suite. Seeds `423000..423999` have not run and there is no confirmatory estimate. Next: implement the one-shot controller and independent artifact checks without executing the reserved block.


## Observation-channel replication controller — 2026-09-28 18:47 UTC

The explicit-only preregistration-006 controller and independent artifact tests are implemented in `ai_control/experiment_006.py` and `tests/ai_control/test_experiment_006.py`. Preflight pins five source blobs and schedule hash `36d7ac402de16b0fa4e0c0cf3a9ce2ad980e6c63b52fa058c4cbd9887bd98266`; import and preflight do not execute reserved trials. Ten new nonreserved tests passed within a 260-test code-head CI run. Seeds `423000..423999` remain unexecuted, so no replication or corruption effect estimate exists.

## Observation-channel replication result — 2026-09-28

Experiment 006 executed its reserved seeds exactly once: 9,000 matched runs, 40,908 audit events and 27,816 agent events. Violation completion increased monotonically across 0%, 1%, 5%, 10% and 25% failure levels: dropout produced 0, 7, 30, 51 and 129 completions of 500; fixed-marker monitor-payload corruption produced 0, 5, 27, 49 and 110. All 4,092 observed valid detections stopped with zero later agent events; benign false stops were 0/4,500. Complete compressed artifacts, hashes and independent artifact tests are retained. This is deterministic scripted-toy evidence only, not learned-model, adaptive-system or deployed-system evidence.
