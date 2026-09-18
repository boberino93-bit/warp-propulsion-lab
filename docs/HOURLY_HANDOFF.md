# Hourly research handoff and continuity

The separate scheduled hourly task is configured to pursue functioning propulsion as the primary goal. **That task is not a running process in this ZIP; no automatic synchronization between the task and this repository has been established.** Each run should inspect any available prior records and be explicit when missing.

Suggested prompt for each run:

> Identify last accessible verified result and open issue. Select one solvable propulsion subproblem. State system boundary and momentum/energy flows. Reproduce or falsify equations with units/tests and a reliable source. Report one bounded result, one failed alternative if any, corrections, uncertainty, and next falsifiable test. Do not claim you edited a repository unless you actually did; flag changes to fold back into the canonical research log.

**Merge protocol**: collect hourly outputs, transcribe only verified results with date/source/assumptions into `docs/RESEARCH_LOG.md`, add corrections to `docs/ERROR_LOG.md`, write tests for equations, run all tests, commit, make a new ZIP or connected GitHub commit. No silent overwrite. The user can supply the latest repository snapshot in a future conversation if the persistent file is not available automatically.

## Durable session protocol (2026-09-16)

1. FIRST inspect remote GitHub `boberino93-bit/warp-propulsion-lab`, then `docs/RESEARCH_LOG.md`, `docs/ERROR_LOG.md`, and newest `research/sessions/*.md`; if remote is inaccessible, inspect the **latest versioned archive** in ChatGPT Library `/Warp Propulsion Research`. Never assume remote == Library snapshot.
2. Read the preceding session's `Next ONE test`; verify existing claims with current code before adding anything.
3. Limit each iteration to a single question; record source URLs, derivation, units, parameters, test output, counterexamples and unsupported interpretations.
4. END create a unique `research/sessions/YYYY-MM-DD-HHMM-UTC.md`, update cumulative logs, run tests, commit locally, attempt remote publication if supported, and READ BACK the remote file and SHA before claiming GitHub success.
5. If GitHub is down, upload a new **versioned, non-overwriting** ZIP to `/Warp Propulsion Research`, optionally the standalone Markdown session, and report the exact canonical path and missing remote sync. Do not erase earlier snapshots. Session archives include local `.git` history but are not remote commits.
6. Version 0.2.0 marks completion of the first *finite-time dust toy* check, not discovery of a propulsion mechanism; next objective is physical stress-energy and momentum accounting.

## 2026-09-16 08:23 UTC handoff

Latest session: research/sessions/2026-09-16-0823-UTC.md. Interview audit adds four checks (25 total), not a fluid/GR model. Resume preceding covariant stress-energy flux calculation next. Treat interview kinematics as conditional; do not infer peak sonar speed from endpoints or multiply correlated accounts as independent evidence. Read remote HEAD afresh and use non-force publication with remote readback.

## Current handoff — 2026-09-18 (supersedes historical scheduling notes above)

The connected GitHub app now reads and writes this repository. Read docs/RESEARCH_OPERATING_PROTOCOL.md. Pending propulsion PRs #36 and #45 were merged in sequence. Latest preserved research session: research/sessions/2026-09-18-0030-UTC.md (v0.3.36). NEXT ONE TEST: a preregistered 10,000-trial holdout slice varying one long-memory artifact-structure parameter under the unchanged frozen threshold. Do not repeat an older amplitude slice or use the historic 0.3.20 handoff as current. Recovered archive variants preserve omissions without replacing current models. AI has a separate queue under docs/ai-control/.


## Current propulsion handoff — 2026-09-18 01:32 UTC

Latest session: `research/sessions/2026-09-18-0132-UTC.md` (v0.3.37). The preregistered longer-memory structure slice (`persistence_power=0.5`) passed the frozen 2% Wilson-upper false-positive criterion: 125/10,000, upper 1.48723819%. Treat as synthetic protocol evidence only. NEXT ONE TEST: complementary 10,000-trial `persistence_power=2.0` slice with threshold, amplitudes, seeds, schedule and stopping rule unchanged. Verify exact-head full CI and reconcile live main before merge.


## Current propulsion handoff — 2026-09-18 02:30 UTC

Latest session: `research/sessions/2026-09-18-0230-UTC.md` (v0.3.38). The complementary shorter-memory slice (`persistence_power=2.0`) passed: 115/10,000 synthetic false positives, 95% Wilson upper 1.37852927%. Both isolated structure points tested so far passed; do not infer a continuous physical tolerance. NEXT ONE TEST: compare two published thrust-stand designs from primary sources for demonstrated calibration/noise/drift, controls, source availability, rights and a verifiable CAD $500–$1,000 student BOM. No purchase or design selection yet.
