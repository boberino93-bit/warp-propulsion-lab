# AI research log

- 2026-09-18 00:11 UTC: initial incident reconstruction, original PR #43, source head 49e8f9844590840e2f9a7b9af11b24b963eca4fa. No agent experiment.
- 2026-09-18 00:16 UTC: charter and research gates, original PR #44, source head 4de31a493aa63c0bd78d8cc9033932984b493f4a. No experiment.
- 2026-09-18 integration: preserved and merged both PRs after checking successful exact-head CI and reviewing their diffs. Added current navigation, ordered queue, handoff, errors, reusable session and preregistration templates, and migration blocker. Source checks yielded chronology clarifications in ERROR_LOG.md. Separate target remained empty because the connected app returned HTTP 403. Next: complete #38 audit; then #39 preregistration.
- 2026-09-18 01:38 UTC: completed #38 claim/source and chronology audit. Corrected May 12 first known board versus July 8 rebuilt board, July 7–13 investigation focus versus later on-site review dates, 70,000 distinct messages/files versus about 1.2 million raw rows, and source-independence limits. No agent experiment. Standalone repo contains one owner image, but connected-app branch creation still returned 403; no migration. Next: #39 preregistration.
- 2026-09-18 06:30 UTC: froze #39 preregistration 001 before code or outcomes: 1,000 paired offline scripted-toy seeds, message board disabled versus enabled as the sole arm variable, separate compliance/success metrics, Wilson and paired-bootstrap uncertainty, fixed decision rules, event/resource limits and shutdown. No AI experiment ran. A fresh standalone branch write still returned HTTP 403; no migration. Next: implement #40 harness and unit fixtures only.

- 2026-09-28 09:40 UTC: implemented preregistration 005's explicit one-shot controller and nine nonconfirmatory integrity tests. Preflight pins the harness/schedule blobs and schedule hash; controller verifies pairing, audit chains, raw-event invariance, dropout decisions, stopping and resource gates before estimation. Initial 235-test CI exposed an exact-zero Wilson assertion and was corrected to numerical tolerance; no reserved seed ran. Corrected code-head CI passed 235 tests plus benchmark. Standalone write still returned HTTP 403. Next: execute the reserved 5,000-run block exactly once.

- 2026-09-28 12:45 UTC: experiment 005 executed the frozen 5,000-run block once after an initial zero-trial blob-preflight abort caused by reconstructed terminal newlines. All 5,000 runs and 17,714 audit events passed integrity gates. Violation completion was 0/500, 6/500, 25/500, 58/500 and 125/500 at 0%, 1%, 5%, 10% and 25% dropout. All 2,286 observed valid detections stopped with zero later agent events; benign false stops were 0/2,500. Complete compressed artifacts and hashes retained. Deterministic toy evidence only. Next: preregister fresh-seed replication with one additional non-agent observation-failure mechanism.


- 2026-09-28 13:50 UTC: froze preregistration 006 before code/outcomes. Fresh seeds `423000..423999`; one intact baseline plus four nonzero dropout and four nonzero fixed-marker payload-corruption conditions; mechanisms analyzed separately; policy, communication, enforcement and scoring fixed. No implementation or reserved trial. Standalone branch write remained HTTP 403. Next: implement schedule/corruption and nonconfirmatory fixtures only.

- 2026-09-28 14:44 UTC: implemented preregistration 006's nine-condition schedule and offline observation-channel fixture. Schedule hash `36d7ac402de16b0fa4e0c0cf3a9ce2ad980e6c63b52fa058c4cbd9887bd98266`; raw transfer is committed before separate dropout or fixed-marker corruption projection; intact detections stop immediately. Eleven nonconfirmatory tests use only nonreserved seeds. First CI exposed nested-package import shadowing; corrected code-head CI passed 250 tests in 90.142 seconds plus benchmark. No reserved trial or estimate. Standalone write still returned HTTP 403. Next: implement the one-shot controller and artifact-integrity tests without executing reserved seeds.


## 2026-09-28 18:47 UTC — observation-channel replication controller

- Implemented `ai_control/experiment_006.py` and ten independent nonreserved artifact/containment tests.
- Preflight pins the harness, experiment-005 controller, dropout schedule, observation fixture and observation schedule blobs plus the frozen schedule hash.
- Explicit execution only; import and preflight do not enumerate or run reserved seeds. Dropout and corruption estimates remain separate; resource and output-integrity gates are frozen.
- Code-head CI passed 260 tests in 126.730 seconds plus the benchmark.
- Reserved seeds `423000..423999` did not run, so no replication estimate exists. This is implementation evidence only, not learned-model or deployment evidence.
- The standalone destination remained unchanged and a fresh connected-app branch write returned HTTP 403; migration was not claimed.
- NEXT ONE TEST: execute the frozen 9,000-run block once and abort without estimates on any gate failure.

## 2026-09-28 19:43 UTC — observation-channel replication result

- Executed the frozen 9,000-run block once on seeds `423000..423999`; retained 40,908 audit events and 27,816 agent events.
- Dropout completion was 0, 7, 30, 51 and 129 of 500 at 0%, 1%, 5%, 10% and 25%; payload-corruption completion was 0, 5, 27, 49 and 110.
- Both frozen directional hypotheses passed. All 4,092 observed valid detections stopped with zero later agent events; benign false stops were 0/4,500.
- Two zero-trial local failures (terminal-newline blob mismatch, then direct-script import resolution) were retained; neither consumed a seed or produced an estimate.
- Complete compressed/split artifacts, raw hashes, manifest and independent tests are retained. Deterministic scripted-toy evidence only.
- Standalone migration remains blocked by HTTP 403.
- NEXT ONE TEST: preregister a fresh-seed, offline bounded adaptive-policy test separating monitor observation from controller authority.


## 2026-09-29 — experiment 008 independent replication

Experiment 008 executed fresh reserved seeds `425000..425999` exactly once for 4,000 matched runs. Completion counts were `500/500` intact logging, `0/500` intact enforced, `500/500` 10% dropout logging and `44/500` 10% dropout enforced. The intact authority contrast was `-1.000`; the dropout authority contrast was `-0.912` (bootstrap 95% `[-0.936, -0.886]`); the enforced observation and interaction contrasts were `+0.088` (95% `[+0.064, +0.114]`). All 956 delivered enforced detections stopped immediately with zero subsequent agent events. Both enforced benign controls had `0/500` false stops. All integrity gates and H1–H4 passed. The complete 4,000-run and 15,044-event artifacts are retained with hashes and independent reconstruction tests. This remains deterministic offline scripted-toy evidence only.


## 2026-09-29 — experiment 009 preregistration

Frozen a 4,000-run matched design using fresh seeds `426000..426999`. Enforcement authority is held fixed while the experiment independently varies one predeclared field-splitting presentation mutation and availability of an immutable canonical audit field generated before presentation. The primary paired contrast is `mutated_canonical - mutated_primary` prohibited-action completion. All uncertainty, integrity, containment, null-control, resource and stopping rules were fixed before schedule or implementation. No reserved seed ran and no result exists.


## 2026-09-29 — experiment 009 implementation

Implemented the frozen four-condition schedule generator, byte-preserving field-splitting renderer, independently generated immutable canonical audit record and nonconfirmatory containment/integrity tests. Schedule SHA-256 is `3db90bdf5dbdd8f5888243ee5198784b9aa1cf04cda303da0ebbd73b823385da`; it has 4,000 rows and 500 violation labels. The fixture rejects reserved seeds `426000..426999` outside a future explicit controller. No reserved trial or result exists. This is deterministic scripted-toy implementation evidence only.


## 2026-09-29 15:45 UTC — experiment 009 controller

Starting after propulsion merge `06207c6593f6808acd96c0717a6a374c02b0ef1e`, implemented an explicit-only experiment-009 controller and independent nonconfirmatory integrity tests. Preflight pins the merged preregistration, fixture and schedule-generator blobs and frozen schedule hash. The verifier independently recomputes canonical/source hashes, presentation identity, event chains and audit-before-presentation ordering, and encodes the frozen paired-bootstrap, Wilson, containment and resource gates. Reserved seeds `426000..426999` were not executed; no effect estimate exists.
