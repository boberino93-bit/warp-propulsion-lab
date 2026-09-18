# AI handoff — 2026-09-18

Read README, charter, ROADMAP, ERROR_LOG, shared operating protocol and latest research/ai-control/sessions before work. Original PRs #43 and #44 are merged; the initial source ledger and foundation session are preserved. No agent experiment exists yet.

NEXT ONE TEST: finish a claim-by-claim source audit of issue #38, especially distinguishing the earlier May communication history from the July rebuilt board and the investigators' July 7–13 focus from their later on-site review dates. Then preregister #39. Do not skip directly to implementation.

Migration: target repo is visible but app writes returned HTTP 403. Continue safely in existing isolated paths; never claim target is initialized. Once access is legitimately updated, inspect the destination afresh, preserve any intervening work, copy project content with source commit/blob provenance, copy current issue bodies/comments/state with cross-links, verify destination readback and tests, and only then change the canonical home. Retain originals; no force push or deletion.


## Current handoff — 2026-09-18 01:38 UTC

The complete claim/source audit for #38 is on the current AI audit branch and session `research/ai-control/sessions/2026-09-18-0138-UTC.md`. It corrects May 12 first-board versus July 8 rebuilt-board chronology, distinguishes the later investigator visit dates, explains 70,000 distinct messages/files versus 1.2 million raw rows, and qualifies source independence. No agent experiment ran.

NEXT ONE TEST: #39 preregistration only. Freeze the fully offline communication-disabled versus permitted-message-board toy comparison, metrics, seeds/trials, uncertainty, falsification, resource/event budgets and shutdown before code.

Standalone destination now contains one owner image at `1192862...`, but a fresh branch write returned 403. Preserve it untouched and keep the existing isolated paths canonical until a legitimate write and readback succeed.
