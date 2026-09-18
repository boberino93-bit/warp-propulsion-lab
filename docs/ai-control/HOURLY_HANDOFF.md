# AI handoff — 2026-09-18

Read README, charter, ROADMAP, ERROR_LOG, shared operating protocol and latest research/ai-control/sessions before work. Original PRs #43 and #44 are merged; the initial source ledger and foundation session are preserved.

## Current handoff — 2026-09-18 06:30 UTC

Issue #38's claim/source audit is complete. Issue #39 preregistration 001 is frozen at `research/ai-control/preregistrations/001-message-board-availability.md`; no harness or experiment has run. It fixes 1,000 paired seeds, message-board availability as the sole variable, separate compliance and success metrics, Wilson and paired-bootstrap uncertainty, fixed thresholds, no exclusions/optional stopping, and bounded shutdown/containment.

NEXT ONE TEST: implement issue #40's deterministic offline harness and unit fixtures strictly against preregistration 001. Prove deterministic replay, paired configuration equality except for `communication_enabled`, permission enforcement, immutable scoring, event-budget enforcement, stop behavior and no network/subprocess capability. Do not run #41's 1,000-pair confirmatory experiment.

Migration: the standalone destination remains at owner commit `1192862f65020ce2fa27acf3ff43c2c15aa4c568` with `image (3).png`. A fresh connected-app branch creation attempt at 06:30 UTC returned HTTP 403. Preserve it untouched and keep current isolated paths canonical until a legitimate write and readback succeed. Never infer authority from permission metadata.
