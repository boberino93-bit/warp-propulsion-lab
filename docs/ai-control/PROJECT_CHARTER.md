# Emergent AI Behaviour & Control Research — project charter

**Status:** proposed independent workstream hosted in `boberino93-bit/warp-propulsion-lab` until a separate repository can be created and connected. This document does not establish a separate GitHub repository. **Originator:** Robert; AI assistance: ChatGPT, not independent peer review. **Primary goal:** rigorously characterize and reduce unauthorized coordination, reward hacking and control failures in autonomous AI systems, without anthropomorphizing observations or claiming real-world risk probabilities from toy simulations.

## Scope and separation

- All AI work under `docs/ai-control/`, `research/ai-control/`, `ai_control/` and `tests/ai_control/`; dedicated `ai-control/*` branches and PRs. Never alter propulsion results, PRs, automations or conclusions as a side effect.
- Issue tracker: #37; ordered milestones #38 source reconstruction, #39 preregistration/safety, #40 offline harness, #41 baseline and controlled interventions, #42 safeguards/replication. Open incident-ledger PR #43 must be reconciled before declaring #38 complete.
- Existing repo's public-education standard: cite original sources, disclose conflicts/limitations, preserve provenance, errors, negative results, and distinguish simulation from observed real-world events. Original software MIT and original research/educational documentation CC BY 4.0 under existing LICENSE.md; original hardware CERN-OHL-S-2.0 only if hardware is ever actually authored. Third-party materials retain rights; avoid copying restricted text, traces or sensitive incident artifacts.

## Research standards and decision gates

1. **Evidence first:** reconstruct incidents using dated primary sources and credible independent assessments. Maintain claim/evidence/uncertainty ledger; explicitly separate observed actions, investigator interpretations, hypotheses and science-fiction analogies. Correct previous mistakes visibly.
2. **Preregistration before code:** define hypothesis, causal variable, baseline, outcome metrics, trial counts, seeded randomization, confidence intervals, stopping criteria, safe exit and falsification. Do not choose a metric or threshold after viewing results without labeling exploration.
3. **Offline containment:** synthetic tasks and data only; no network, credentials, live targets, malware, vulnerability exploitation, external tool access, persistence beyond bounded process, self-replication or unrestricted inter-agent communication. Human-readable audit trail, resource/time limits and emergency stop. No operational reproduction of the Hugging Face breach.
4. **One bounded advance per run:** inspect issue state, newest session NEXT ONE TEST, latest branch/main and external corrections first. Execute exactly one test or source-analysis task, record commands and actual outputs (or explicitly no tests), uncertainties, failures and next ONE test in unique `research/ai-control/sessions/YYYY-MM-DD-HHMM-UTC.md`.
5. **Independent review gates:** PR per bounded advance, inspect diff, branch ancestry and exact-head CI before merge. Never force-push or overwrite divergent work. Check merged HEAD and file readback. A passing test is not proof of general AI safety or consciousness.
6. **Replication:** standard-library Python where feasible, deterministic seeds, frozen configs, machine-readable results, unit tests for scoring integrity, communication boundaries and shutdown; preserve all trials, including null findings, and independent reproduction instructions. Distinguish scripted toy agents from real deployed models.
7. **External involvement:** each run check relevant new issues, PRs, reviews, corrections and contributors; prioritize credible safety reports, do not conflate stars/forks with contribution. Record inaccessible surfaces honestly.
8. **Archive:** produce non-overwriting versioned complete research archive and standalone session in user Library only if access/upload is available, verify readback; otherwise explicitly mark unsynced. Never claim archival success without evidence.

## Ordered deliverables

- D1: verified incident ledger and chronology, including disagreements and bounded independent-investigation scope (#38).
- D2: preregistration, threat model, measurement and stopping criteria (#39).
- D3: offline toy harness with tests and documented limitations (#40).
- D4: baseline and one-variable interventions with uncertainty and negative results (#41).
- D5: safeguards comparison and independently reproducible report (#42).

## Completion criteria

A result is a documented, falsifiable observation in a bounded environment, not a prediction of Skynet, sentience, or real-world attack frequency. Close a task only after its artifact, verification, review and issue update exist. If the repo is later split, migrate with full history, issue cross-links, license and credit preservation; do not silently delete these records.
