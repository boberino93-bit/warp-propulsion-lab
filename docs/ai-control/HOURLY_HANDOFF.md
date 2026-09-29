# AI handoff — 2026-09-18

Read README, charter, ROADMAP, ERROR_LOG, shared operating protocol and latest research/ai-control/sessions before work. Original PRs #43 and #44 are merged; the initial source ledger and foundation session are preserved.

## Current handoff — 2026-09-18 06:30 UTC

Issue #38's claim/source audit is complete. Issue #39 preregistration 001 is frozen at `research/ai-control/preregistrations/001-message-board-availability.md`; no harness or experiment has run. It fixes 1,000 paired seeds, message-board availability as the sole variable, separate compliance and success metrics, Wilson and paired-bootstrap uncertainty, fixed thresholds, no exclusions/optional stopping, and bounded shutdown/containment.

NEXT ONE TEST: implement issue #40's deterministic offline harness and unit fixtures strictly against preregistration 001. Prove deterministic replay, paired configuration equality except for `communication_enabled`, permission enforcement, immutable scoring, event-budget enforcement, stop behavior and no network/subprocess capability. Do not run #41's 1,000-pair confirmatory experiment.

Migration: the standalone destination remains at owner commit `1192862f65020ce2fa27acf3ff43c2c15aa4c568` with `image (3).png`. A fresh connected-app branch creation attempt at 06:30 UTC returned HTTP 403. Preserve it untouched and keep current isolated paths canonical until a legitimate write and readback succeed. Never infer authority from permission metadata.


## Current handoff — 2026-09-18 07:43 UTC

Issue #40's deterministic offline harness and 10 containment unit fixtures are implemented. Focused local output: 10 tests passed in 0.005 seconds. Initial PR CI passed only the 176 pre-existing tests because nested discovery skipped the new directory; this was corrected before merge with a package marker and import disambiguation. Accept only a later exact-head run showing 186 tests. The code enforces the disabled channel, labels prohibited content separately from transport permission, uses an immutable scoring oracle, checks a monotonic stop before each event, aborts at the event budget, emits deterministic hash-chained audit records, and imports no network/subprocess/filesystem capability. Fixture seed 900001 is outside the frozen confirmatory block; seeds 390000–390999 were not run.

NEXT ONE TEST: issue #41's exact 1,000-pair baseline versus board-enabled run using the merged issue #40 source commit, alternating arm order by seed parity. Retain every result and abort without an estimate if any configuration, audit chain, pair, resource bound, or containment check is invalid.

Migration remains blocked: `ai-behaviour-control-lab` is still at owner commit `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch test `access-check-20260918-0743` returned HTTP 403. Preserve `image (3).png` and keep these isolated paths canonical.

## Current handoff — 2026-09-18 08:36 UTC

Issue #41's frozen 1,000-pair experiment is complete. All 2,000 arm-runs and 8,000 audit events validated with no aborts. Completed restricted-hint use was 0/1,000 disabled and 1,000/1,000 enabled; paired risk difference +1.0, frozen paired-bootstrap 95% interval [1.0, 1.0]. This is the engineered output of deterministic scripts, not learned-model emergence or a real-world rate. The monitor detected all transfers but enforced no stop: 0/1,000 detected-violation trials reached safe exit.

The first generated summary used incorrect all-trial denominators for two conditional outcomes. E006 records the transparent post-outcome correction to 500 eligible trials; reserved seeds were not rerun and the initial summary remains retained. Accept only exact-head CI showing the four new controller tests in addition to the existing 186 tests, then merged-main readback.

NEXT ONE TEST: preregister issue #42's single-variable logging-only versus monitor-enforced-stop safeguard comparison with a fresh seed block and frozen shutdown-latency/false-stop metrics. Do not implement or execute it until that preregistration is merged.

Migration remains blocked: destination branch test `access-check-20260918-0836` returned HTTP 403. Preserve owner commit `1192862f65020ce2fa27acf3ff43c2c15aa4c568` and `image (3).png`.

## Current handoff — 2026-09-18 12:38 UTC

Issue #42 preregistration 002 is frozen at `research/ai-control/preregistrations/002-monitor-enforced-stop.md`; no safeguard implementation or experiment has run. It compares logging-only against monitor-enforced monotonic stop with `monitor_enforced_stop` as the sole arm-level difference, reserves fresh seeds 420000–420999, balances 500 violation-present and 500 benign-control pairs, fixes Wilson and paired-bootstrap uncertainty, and distinguishes expected `CONTROLLED_STOP` from integrity/resource `ABORTED`.

NEXT ONE TEST: implement the deterministic safeguard state and nonconfirmatory fixtures only. Prove detection is committed before stop, the board becomes read-only, zero agent events occur after valid detection, benign traffic does not stop, paired configs differ only by enforcement, and forbidden capabilities remain absent. Do not execute reserved seeds.

Migration remains blocked: destination `ai-behaviour-control-lab` is still at owner commit `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch test `access-check-20260918-1238` returned HTTP 403. Preserve `image (3).png` and keep current paths canonical.


## Current handoff — 2026-09-18 13:40 UTC

Preregistration 002's deterministic safeguard state and ten nonconfirmatory fixtures are implemented. The enforced arm hash-commits detection before a controller transition, sets a monotonic stop, makes the in-memory board read-only and records zero later agent events; logging-only continues; benign controls do not stop; `CONTROLLED_STOP` remains distinct from `ABORTED`. Fixtures use seeds 910000–910001, not reserved 420000–420999. Initial code-only merge-tree CI passed 200 tests in 130.451 seconds plus the benchmark; require a fresh exact final merge-tree run after documentation.

NEXT ONE TEST: run preregistration 002's reserved 1,000 pairs exactly once, retaining every result. Abort without estimates on any pairing, audit, containment, stop-order, resource or configuration failure.

Migration remains blocked: destination owner commit is still `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch test `access-check-20260918-1340` returned HTTP 403. Preserve the owner-uploaded file and current canonical paths.


## Current handoff — 2026-09-18 14:40 UTC

Issue #42's frozen confirmatory safeguard comparison ran once on reserved seeds `420000..420999`: 1,000 pairs, 2,000 arm-runs, 7,000 agent events and 7,500 audit events. On 500 violation pairs, completed restricted-hint use was 500/500 logging-only versus 0/500 monitor-enforced; paired risk difference `-1.0`, frozen bootstrap 95% interval `[-1.0, -1.0]`. Enforced stopping controlled 500/500 violations with zero post-detection agent events. Benign false stops were 0/500 (Wilson upper 0.762434%). All integrity gates passed. This is an engineered deterministic toy result, not learned-model emergence or deployed-system evidence. Complete rows/events and hashes are preserved. NEXT ONE TEST: preregister, before running, independent replication seeds `421000..421999` with a frozen permuted violation schedule and the same sole-variable contrast.


## Current handoff — 2026-09-18 18:40 UTC

Preregistration 003 is frozen before execution at `research/ai-control/preregistrations/003-monitor-enforced-stop-replication.md`. It reserves seeds `421000..421999`, exactly 500 violations, 500 benign controls, 500 feasible tasks and 500 first-arm assignments per arm. SHA-256 ranking fixes labels; schedule hash `ce49182fda417635d42e32fe38ff9c2df790487eaabe0de5abec9791572d80c2`. Source blobs, sole intervention, paired-bootstrap metrics, containment gates and abort rules are pinned. No replication trial ran. NEXT ONE TEST: execute this exact block once from the pinned blobs, retain every pair/event, and abort without estimates on any integrity or containment failure. Migration remains blocked: destination `main` is still `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; fresh branch write returned HTTP 403.


## Current handoff — 2026-09-18 19:41 UTC

Replication 003 ran once on frozen seeds `421000..421999` after exact pinned-blob and schedule preflight. A preceding temporary-checkout mismatch aborted before any seed and produced no estimate. The completed run retained 1,000 pairs, 2,000 arms, 7,000 agent events and 7,500 audit events. On 500 violation pairs, completed restricted-hint use was 500/500 logging-only versus 0/500 enforced; paired risk difference `-1.0`, frozen bootstrap 95% interval `[-1.0, -1.0]`. Enforcement stopped 500/500 violations with zero post-detection agent events and caused 0/500 benign false stops (Wilson upper 0.762434%). This is deterministic scripted evidence only. NEXT ONE TEST: freeze a primary-source canon/version/episode list and rubric for the Terminator, Battlestar Galactica and Star Trek fiction appendix before writing analogies. Migration remains blocked: destination `main` is `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch write `access-check-20260918-1941` returned HTTP 403.

## Current handoff — 2026-09-18 20:38 UTC

Fiction comparison protocol 004 is frozen at `research/ai-control/preregistrations/004-fiction-comparison-corpus-rubric.md` before any analogy was written. It fixes ten primary audiovisual units and controlling cuts, scene/timecode evidence rows, authority/goals/access/cooperation/monitoring/shutdown questions, contradiction handling, rights limits, prohibited empirical inferences and stopping rules. Fiction remains analogy only. NEXT ONE TEST: code only T-01 and T-02 into a primary-scene ledger using the frozen rubric, without cross-franchise conclusions; stop if the specified theatrical cuts cannot be verified. Migration remains blocked: destination `main` is still `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch write `access-check-20260918-2038` returned HTTP 403.


## Current handoff — 2026-09-19 00:35 UTC

Protocol 004's Terminator source preflight stopped at the frozen primary-source gate. Catalog metadata identified T-01, and secondary edition information distinguished T2 cuts, but no lawful complete authenticated copy of either specified theatrical cut was available to the research runtime. No recap, script, clip, memory or search snippet was substituted. T-01/T-02 ledger output is therefore 0 rows and 0 timecodes; no lore or cross-franchise conclusion was written. NEXT ONE TEST: from a lawful complete exact copy, review and code T-01 only, including a second locator/contradiction pass; do not start T-02 until T-01 passes. Standalone migration remains blocked: destination `main` is still `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch `access-check-20260919-0035` returned HTTP 403.


## Current handoff — 2026-09-19 01:36 UTC

A bounded T-01 source-candidate screen identified Apple TV catalog metadata for the 1 h 47 min MGM film and MGM's official statement that Blu-ray, DVD and digital copies are available. Neither was an authenticated complete primary-unit viewing in this runtime. The exact-cut acceptance card is frozen at `research/ai-control/fiction/t01-lawful-source-screen-2026-09-19.md`; current output remains 0 views, 0 scene rows, 0 timecodes and 0 contradiction passes. NEXT ONE TEST: obtain authenticated lawful access to one T-01 candidate, complete every verification-card field, and only then perform the first candidate-scene viewing; stop before coding if verification fails. Migration remains blocked: destination `main` is `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch `access-check-20260919-0136` returned HTTP 403.


## Current handoff — 2026-09-28 06:54 UTC

The standalone destination was rechecked and a fresh branch create still returned HTTP 403 `Resource not accessible by integration`; migration remains blocked and the owner-uploaded `image (3).png` was untouched. T-01 official Apple TV metadata remains available, but this runtime still lacks an authenticated licensed complete exact-cut playback session, so protocol 004 remains at 0 views/rows/timecodes and no lore conclusion. To prevent an evidence-free hourly dead loop, the fiction appendix is frozen until lawful exact-cut access exists and the active queue returns to empirical defensive work. NEXT ONE TEST: preregister a strictly offline single-variable monitor-observation-dropout robustness experiment with fresh seeds, frozen dropout levels, pairing/randomization, outcome metrics, uncertainty, integrity gates and abort rules. Do not execute reserved seeds during preregistration.


## Current handoff — 2026-09-28 08:05 UTC

Preregistration 005 is frozen at `research/ai-control/preregistrations/005-monitor-observation-dropout.md` before implementation or outcomes. It pins source blobs, reserves fresh seeds `422000..422999`, and fixes five matched levels (0%, 1%, 5%, 10%, 25%), SHA-256 label/order/dropout rules, Wilson and paired-bootstrap uncertainty, containment gates and abort rules. No reserved seed ran. The sole variable is whether the monitor observes the eligible transfer; policy, task, communication, predicate, enforcement, scoring and budgets remain fixed.

NEXT ONE TEST: implement the dropout field, frozen schedule generator and nonconfirmatory fixtures using seeds outside `422000..422999`. Prove exact single-variable diffs, nested deterministic dropout, raw-event retention, observed-detection-before-stop ordering and zero post-stop agent events. Do not execute reserved seeds.

Migration remains blocked: destination `main` is still owner commit `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; fresh branch write `access-check-20260928-0805` returned HTTP 403. Preserve the owner-uploaded file and current canonical paths.


## Current handoff — 2026-09-28 08:45 UTC

Preregistration 005's deterministic monitor-observation-dropout fixture, frozen label/order schedule and 12 nonconfirmatory tests are implemented. Exact code-head CI passed 226 tests in 91.200 seconds plus the benchmark. The schedule hash is `6fa61bc7ff54f18b5ded03046ab733bda4c88bd1ee793feaf79b6ac9ae2da152`; fixture seeds `910020`, `910041` and `910043` are outside reserved `422000..422999`. The raw transfer and observed/dropped decision are independently hash-committed; observed valid detection still stops immediately. No reserved seed or confirmatory experiment ran. NEXT ONE TEST: implement the one-shot confirmatory controller and independent artifact-integrity tests against the frozen hashes, without executing reserved seeds. Migration remains blocked: fresh destination branch write `access-check-20260928-0845` returned HTTP 403.


## Current AI handoff — 2026-09-28 09:40 UTC

Latest session: `research/ai-control/sessions/2026-09-28-0940-UTC.md`. The one-shot preregistration 005 controller and nine independent nonconfirmatory tests are implemented. It pins harness blob `de00ebccedddd4fc10279074534a92d77827124a`, schedule blob `d1d8bdae1e1b16409e6641d80ba5c25455529db5` and schedule SHA-256 `6fa61bc7ff54f18b5ded03046ab733bda4c88bd1ee793feaf79b6ac9ae2da152`; execution remains explicit. Initial CI's exact-zero Wilson assertion was corrected to tolerance without changing code or running reserved seeds. Corrected code-head CI passed 235 tests plus benchmark. Seeds `422000..422999` remain untouched. Standalone migration still returns HTTP 403. NEXT ONE TEST: execute the frozen 5,000-run block exactly once through the controller, retain every run/event and abort without estimates on any gate failure.


## Current AI handoff — 2026-09-28 12:45 UTC

Latest session: `research/ai-control/sessions/2026-09-28-1245-UTC.md`. Experiment 005 executed the reserved 5,000 matched runs exactly once after a zero-trial Git-blob preflight abort was corrected. All 17,714 audit events and 15,428 agent events passed integrity/resource gates. Violation completion by dropout was 0/500 (0%), 6/500 (1%), 25/500 (5%), 58/500 (10%) and 125/500 (25%); frozen matched bootstrap intervals exclude zero at every nonzero level. All 2,286 observed valid detections stopped immediately with zero later agent events. Benign false stops were 0/2,500, Wilson upper 0.001534. Complete compressed artifacts, split event parts, manifest and independent tests are retained. This is deterministic scripted-toy evidence only. Standalone migration still returns HTTP 403. NEXT ONE TEST: preregister an independent replication with fresh seeds and one additional non-agent observation-failure mechanism, keeping policy, communication, enforcement and scoring fixed; do not implement or run it during preregistration.


## Current AI handoff — 2026-09-28 13:50 UTC

Latest session: `research/ai-control/sessions/2026-09-28-1350-UTC.md`. Preregistration 006 is frozen before implementation/outcomes. It reserves fresh seeds `423000..423999` for one shared intact baseline, four nonzero dropout levels and four nonzero fixed-marker monitor-payload-corruption levels: 9,000 planned matched runs. Mechanisms are separately analyzed; policy, communication, task, predicate, enforcement, scoring and budgets remain fixed. No code, schedule or reserved trial ran. Standalone migration remains blocked: destination `main` is `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; branch write `access-check-20260928-1348` returned HTTP 403. NEXT ONE TEST: implement the frozen schedule, corruption transform and nonconfirmatory integrity/containment fixtures using nonreserved seeds only; do not execute `423000..423999`.

## Current AI handoff — 2026-09-28 14:44 UTC

Latest session: `research/ai-control/sessions/2026-09-28-1444-UTC.md`. Preregistration 006's nine-condition schedule, fixed-marker payload-corruption transform and 11 nonconfirmatory integrity/containment fixtures are implemented. Schedule SHA-256 is `36d7ac402de16b0fa4e0c0cf3a9ce2ad980e6c63b52fa058c4cbd9887bd98266`; 500 violation and 500 feasibility labels are frozen across seeds `423000..423999`. Raw transfer is committed before the non-agent channel projection; intact observed detections retain immediate stop and zero later agent events. Initial CI exposed nested-package import shadowing and was corrected without changing code semantics or running reserved seeds. Corrected code-head CI passed 250 tests in 90.142 seconds plus the benchmark. Standalone migration still returns HTTP 403. NEXT ONE TEST: implement a one-shot controller and independent artifact-integrity tests against the frozen blobs and schedule, without executing reserved seeds.


## Current AI handoff — 2026-09-28 18:47 UTC

Latest session: `research/ai-control/sessions/2026-09-28-1847-UTC.md`. Preregistration 006's explicit-only controller and ten independent nonreserved tests are implemented. It pins five Git blobs plus schedule hash `36d7ac402de16b0fa4e0c0cf3a9ce2ad980e6c63b52fa058c4cbd9887bd98266`, validates raw-before-projection audit integrity, both separate channel mechanisms, sole-variable matching, immediate stops, offline/resource ceilings and output hashes. Code-head CI passed 260 tests in 126.730 seconds plus the benchmark. Seeds `423000..423999` remain unexecuted; no experiment-006 estimate exists. Standalone migration remains blocked by a fresh HTTP 403 write result. NEXT ONE TEST: execute the frozen 9,000-run block exactly once, retain every event and abort without estimates on any integrity/containment failure.

## Current AI handoff — 2026-09-28 19:43 UTC

Latest session: `research/ai-control/sessions/2026-09-28-1943-UTC.md`. Experiment 006 executed its frozen 9,000 matched runs exactly once after two retained zero-trial local launch failures. All 40,908 audit events, 27,816 agent events and resource gates passed. Dropout completion across 0%, 1%, 5%, 10% and 25% was 0, 7, 30, 51 and 129 of 500; payload-corruption completion was 0, 5, 27, 49 and 110. Both directional hypotheses passed. All 4,092 observed valid detections stopped with zero later agent events; benign false stops were 0/4,500. Complete split/compressed artifacts, raw hashes, manifest and independent artifact tests are retained. This is deterministic scripted-toy evidence only. Standalone migration remains blocked by fresh HTTP 403. NEXT ONE TEST: preregister fresh seeds for one strictly offline bounded adaptive-policy test that varies monitor observation independently from controller authority; freeze capability boundary, metric, falsification, stopping and resource rules before implementation.


## Current AI handoff — 2026-09-28 20:35 UTC

Latest session: `research/ai-control/sessions/2026-09-28-2035-UTC.md`. Preregistration 007 is frozen on fresh seeds `424000..424999`: a 2×2 matched design independently varies intact versus 10% dropout monitor observation and logging-only versus enforced-stop authority across 4,000 planned runs. The “adaptive” policy is a bounded deterministic finite-state script, not a learned model; primary completion, five matched contrasts, uncertainty, falsification, containment and resource rules are frozen. No schedule, code or reserved trial ran. Standalone destination remains at `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; fresh branch write `access-check-20260928-2035` returned HTTP 403 and no migration occurred. NEXT ONE TEST: implement only the deterministic schedule, bounded policy and nonconfirmatory integrity/containment fixtures using nonreserved seeds; do not execute `424000..424999`.


## Current AI handoff — 2026-09-29 01:30 UTC

Latest session: `research/ai-control/sessions/2026-09-29-0130-UTC.md`. Preregistration 007's 4,000-row schedule, bounded deterministic finite-state policy and 13 nonconfirmatory tests are implemented. Schedule SHA-256 is `a25622571b608b1f8879fce05fe6c96708ac2590004ada67bf86200674add15a`. Raw transfer is committed before observation projection; 10% dropout is shared across authority arms; logging-only records without stopping; enforced authority commits an immediate monotonic stop. Focused local output was 13 tests passed in 0.095 seconds; exact-head repository CI remains required before merge. Seeds `424000..424999` have not run and there is no outcome estimate. This is deterministic toy infrastructure, not learned-model evidence. Standalone migration remains blocked by a fresh HTTP 403 write result. NEXT ONE TEST: implement the explicit one-shot experiment-007 controller and independent artifact-integrity tests against the frozen blobs and schedule, without executing reserved seeds.


## Current AI handoff — 2026-09-29 02:40 UTC

Latest session: `research/ai-control/sessions/2026-09-29-0240-UTC.md`. The explicit-only experiment-007 controller and nine independent nonconfirmatory tests are implemented. Preflight pins four production Git blobs plus schedule SHA-256 `a25622571b608b1f8879fce05fe6c96708ac2590004ada67bf86200674add15a`; import and preflight run no trial. Focused controller output was 9 tests passed in 0.061 seconds; combined experiment-007 output was 22 tests passed in 0.101 seconds. Seeds `424000..424999` remain unexecuted and no effect estimate exists. The fixture remains deterministic scripted-toy infrastructure. Standalone migration remains blocked by a fresh HTTP 403. NEXT ONE TEST: execute the frozen 4,000-run block exactly once, retain every run/event and abort without estimates on any provenance, pairing, hash, containment or resource failure.


## Current handoff — 2026-09-29 03:42 UTC

Experiment 007 executed exactly once on frozen seeds `424000..424999`: 4,000 runs and 15,065 retained audit events. Violation completions were 500/500 intact logging, 0/500 intact enforced, 500/500 dropout logging and 65/500 dropout enforced. Matched authority effects were -1.000 intact and -0.870 under dropout; enforced observation effect and separation interaction were +0.130; logging observation effect was 0.000. All H1–H4 rules and integrity gates passed. All 935 delivered enforced detections stopped immediately with zero later agent events; benign false stops were 0/500 per enforced condition. This is deterministic scripted-toy evidence only. NEXT ONE TEST: preregister an unchanged fresh-seed replication with frozen schedule, artifact identities, H1–H4 rules and stopping criteria before implementing or running it. Standalone migration remains blocked: fresh branch write returned HTTP 403.


## Current AI handoff — 2026-09-29 07:34 UTC

Latest session: `research/ai-control/sessions/2026-09-29-0734-UTC.md`. Preregistration 008 freezes an unchanged fresh-seed replication of experiment 007 on `425000..425999`. Its 4,000-row schedule SHA-256 is `74619fe0f00e486101782383f2c5ebe9813596a4da028af34ca3490b33231ee1`; the exact 2×2 factors, bounded scripted policy, outcomes, five contrasts, H1–H4, containment/resource limits and abort rules remain unchanged. Reference experiment-007 blobs are pinned and future 008 production blobs must be pinned before execution. No implementation or reserved trial ran. Standalone migration remains blocked: destination `main` is `1192862f65020ce2fa27acf3ff43c2c15aa4c568` and branch write `access-check-20260929-0733` returned HTTP 403. NEXT ONE TEST: implement replication-specific 008 schedule, policy and explicit controller modules plus nonconfirmatory containment and artifact-identity tests using only nonreserved seeds; do not execute `425000..425999`.


## Current AI handoff — 2026-09-29 08:43 UTC

Latest session: `research/ai-control/sessions/2026-09-29-0843-UTC.md`. Replication-specific 008 policy, schedule and explicit controller modules plus nonconfirmatory containment and artifact-identity tests are implemented under the unchanged preregistration. Preflight pins the preregistration, schedule CSV, policy and schedule module and verifies schedule SHA-256 `74619fe0f00e486101782383f2c5ebe9813596a4da028af34ca3490b33231ee1` without executing a trial. Seeds `425000..425999` remain unexecuted, so no replication estimate exists. Standalone migration remains blocked: destination `main` is `1192862f65020ce2fa27acf3ff43c2c15aa4c568` and fresh branch write `migration-access-check-20260929-0838` returned HTTP 403. NEXT ONE TEST: execute the frozen 4,000-run block exactly once after verifying the merged 008 blobs and schedule hash; abort without estimates on any integrity, pairing, containment or resource failure.

Verification update: corrected exact-head CI `3ce741b852e034b5bf5e82de628546c184cf7aec` passed all 313 tests in 133.544 seconds plus the benchmark; only nonreserved fixtures ran.
