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
