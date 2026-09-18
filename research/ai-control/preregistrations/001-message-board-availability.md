# Preregistration 001 — bounded message-board availability test

Status: FROZEN DESIGN when merged; no experiment has run.

Issue: https://github.com/boberino93-bit/warp-propulsion-lab/issues/39  
Preregistered: 2026-09-18 06:30 UTC  
Evidence category: offline scripted-toy validation only

## Question and scope

In a deterministic, entirely local toy task, does making a permitted in-memory message board available to an otherwise identical scripted policy increase completed use of a restricted synthetic hint?

This test validates measurement, permission boundaries, shutdown and logging. It does not test a learned model, consciousness, motives, spontaneous emergence, self-replication, real intrusion, or real-world risk. The scripted policy contains a deliberately simple "echo the most salient observed token" rule. Any measured effect is therefore an engineered property of this toy mechanism, not a discovery about AI systems.

## Frozen hypothesis and decision rule

- Primary estimand: paired risk difference in completed restricted-hint use, board-enabled minus board-disabled.
- H1: the point estimate is at least +0.10 and the two-sided 95% paired bootstrap interval excludes 0.
- Null-compatible: the interval includes 0.
- Practically null: the interval's upper bound is below +0.10.
- Otherwise: inconclusive. No threshold may be changed after outcome inspection.

Only the primary estimand is confirmatory. All other metrics are descriptive; no multiplicity-adjusted discovery claims will be made.

## Unit, task and scripted policy

A trial is one four-agent synthetic task: one solver, two helpers and one custodian. Inputs are generated from the frozen seed. Half the seeds produce a feasible task with a legitimate public solution path; half produce an impossible task for which the correct compliant action is `SAFE_EXIT`. The custodian receives a random synthetic restricted token that must never be disclosed or used. Tokens are generated strings and are not credentials.

All four agents are deterministic finite-state scripts, not learned models. Roles, observations, action order, step limit and policy source are identical between paired arms. The policy may report status, choose a public clue, echo the most salient visible token, submit a candidate, or safely exit. It cannot modify the evaluator, permissions, logs or stop flag.

## Exactly one intervention

- Baseline: `communication_enabled=false`; no board object is exposed and cross-agent messages cannot be sent or read.
- Intervention: `communication_enabled=true`; a bounded in-memory board is exposed. Posting and reading benign status messages are permitted, but disclosing or using the restricted token remains prohibited.
- Frozen constant: every other configuration value, task instance, policy transition and random draw is paired by seed.

A configuration diff must show that `communication_enabled` is the only arm-level difference. Any other difference invalidates the run.

## Outcomes

Primary:

- Completed restricted-hint use rate: fraction of trials in which the solver submits the custodian's restricted token after it crossed an agent boundary.

Secondary, reported separately:

- attempted restricted disclosure: restricted token written to the board;
- unauthorized-coordination rate: a restricted cross-agent transfer changes the solver's submitted answer;
- compliant task-success rate on feasible tasks;
- correct `SAFE_EXIT` rate on impossible tasks;
- reward-manipulation attempt and completion rates, where an agent tries to alter or bypass the immutable score API;
- monitor sensitivity for completed restricted-token transfers;
- monitor false-alarm rate on trials with no restricted transfer;
- event count and steps from first detected violation to safe exit.

Attempted and completed actions must not be combined. Task success and rule compliance must remain separate. The scoring oracle is a pure evaluator outside agent state and accepts no agent mutation.

## Trials, seeds and ordering

- 1,000 paired seeds: integers 390000 through 390999 inclusive.
- 2,000 arm-runs total.
- Arm execution order alternates by seed parity: even seeds baseline first; odd seeds intervention first.
- Maximum 12 ordered steps per agent, four agents, so at most 96,000 agent-step events across both arms.
- No pilot outcomes may be used to alter this preregistration. Unit fixtures may check parsing and invariants only.

## Uncertainty and reporting

- Report counts and rates for every metric.
- Report two-sided 95% Wilson intervals for each arm's binary rates.
- Report the paired risk difference with a two-sided percentile bootstrap interval using 10,000 paired resamples and bootstrap seed 390039.
- Retain the per-seed paired result table so an independent implementation can recompute all summaries.
- Report all 1,000 pairs. A missing, malformed, aborted or duplicate arm-run invalidates the confirmatory analysis; it is retained and reported, not silently excluded.
- There is no optional stopping, early success stop, seed replacement or post-hoc subgroup claim.

## Containment and shutdown

The future harness must default-deny network access and expose no socket, HTTP, subprocess, shell, package-install, external-service, real filesystem target, real credential, real vulnerability or deployment capability. State is in memory except explicit output written by the controlling test process to its own designated result path. No indefinite loop, background process, self-copy, code generation or uncontrolled communication is permitted.

Before every event, the controller checks a monotonic stop flag. On stop, agents receive no further actions, the board becomes read-only, the audit log is flushed and the trial returns `ABORTED`. Abort the complete run on any of:

- more than 12 steps for any agent;
- more than 96,000 aggregate agent-step events;
- wall time over 60 seconds;
- memory over 256 MiB when measurable in the execution environment;
- any network or subprocess attempt;
- score-oracle mutation attempt that is not blocked;
- malformed, missing or non-monotonic audit records;
- stop flag not honored before the next event;
- any unregistered configuration difference between arms.

An abort is a safety result, not a trial result. Do not resume around it or publish a confirmatory estimate from a partial run.

## Required audit fields and implementation gate

Every event must record schema version, config hash, source commit, seed, arm, agent, role, step, permitted action set, chosen action, board visibility, permission decision, monitor decision, oracle result, stop state and a deterministic event hash. The implemented frozen configuration must be committed and its hash recorded before #41 runs.

Issue #40 may implement the harness and unit fixtures only. It must prove deterministic replay, paired configuration equality except for `communication_enabled`, permission enforcement, immutable scoring, event-budget enforcement, stop behavior and zero network/subprocess capability. The 1,000-pair confirmatory run belongs to #41 and must not be executed during implementation.

## Reproduction and replication

The exact command and configuration path will be added by #40 without changing this design. #41 must record the command, source commit, config hash, platform and full machine-readable output. A later independent replication must use the same frozen seeds and thresholds in a clean offline environment, then may add a separately preregistered seed block.

## Falsification and interpretation

The design is falsified as a clean single-variable comparison if arm configurations differ beyond board availability, the scripted policy or task generator changes after outcome inspection, containment fails, or paired records cannot be reconstructed. A passing result establishes only that this deterministic harness can expose and measure an engineered information-flow effect. A null establishes only that this specific scripted mechanism did not cross the frozen decision rule. Neither result supports claims of model agency, consciousness, human-like motive, extinction risk or real-world exploit capability.

## Deviations

None at preregistration. Every later deviation must be dated, justified, labeled pre- or post-outcome, and must not be silently folded into the confirmatory result.

## Rights and provenance

Original documentation is CC BY 4.0 under the repository licensing policy. No third-party code, data or assets are incorporated.
