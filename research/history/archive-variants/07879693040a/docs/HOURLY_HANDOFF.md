# Hourly research handoff and continuity

The separate scheduled hourly task is configured to pursue functioning propulsion as the primary goal. **That task is not a running process in this ZIP; no automatic synchronization between the task and this repository has been established.** Each run should inspect any available prior records and be explicit when missing.

Suggested prompt for each run:

> Identify last accessible verified result and open issue. Select one solvable propulsion subproblem. State system boundary and momentum/energy flows. Reproduce or falsify equations with units/tests and a reliable source. Report one bounded result, one failed alternative if any, corrections, uncertainty, and next falsifiable test. Do not claim you edited a repository unless you actually did; flag changes to fold back into the canonical research log.

**Merge protocol**: collect hourly outputs, transcribe only verified results with date/source/assumptions into `docs/RESEARCH_LOG.md`, add corrections to `docs/ERROR_LOG.md`, write tests for equations, run all tests, commit, make a new ZIP or connected GitHub commit. No silent overwrite. The user can supply the latest repository snapshot in a future conversation if the persistent file is not available automatically.
