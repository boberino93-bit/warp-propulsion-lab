# AI Behaviour & Control Research Lab

Originator: Robert. AI assistance: ChatGPT; not independent peer review.

Study unauthorized cooperation, reward hacking, deceptive behaviour and control failures through incident reconstruction, preregistered measurements and bounded offline experiments. Preserve alternative explanations and falsification.

**Current canonical home:** isolated paths in warp-propulsion-lab. **Intended standalone home:** https://github.com/boberino93-bit/ai-behaviour-control-lab . The destination contains an owner-uploaded image, but a fresh connected-app branch write returned HTTP 403; migration is not complete and the owner file must be preserved.

Start with [charter](PROJECT_CHARTER.md), [ordered roadmap](ROADMAP.md), [incident ledger](INCIDENT_LEDGER.md), [error log](ERROR_LOG.md), [handoff](HOURLY_HANDOFF.md), the [frozen message-board preregistration](../../research/ai-control/preregistrations/001-message-board-availability.md), and the [shared operating protocol](../RESEARCH_OPERATING_PROTOCOL.md). Prior sessions are in ../../research/ai-control/sessions/.

## Evidence categories
Observed traces; first-party report; independent bounded assessment; secondary reporting; hypothesis; offline toy result; fiction analogy. Record which category supports each claim. No attribution of subjective motives or real-world catastrophe odds from toy data.

## Reproduction
The #38 source audit and #39 preregistration are complete. Issue #40's deterministic standard-library harness is in `ai_control/`, containment tests are in `tests/ai_control/`, and its frozen implementation configuration is in `research/ai-control/experiments/`.

Run only the implementation tests with:

```sh
python -m unittest discover -s tests/ai_control -v
```

These fixtures use seed 900001, outside the reserved confirmatory block. No 1,000-pair AI experiment has run; seeds 390000–390999 remain reserved for issue #41 after the harness source commit is merged. Passing repository CI is implementation verification, not an AI experiment or evidence about learned models.

## Rights
The existing repository LICENSE.md and CREDITS.md apply: MIT original software, CC BY 4.0 original research documentation, third-party exclusions. Preserve original source/author/commit attribution during migration. No external affiliation claimed.
