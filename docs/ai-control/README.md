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
