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
