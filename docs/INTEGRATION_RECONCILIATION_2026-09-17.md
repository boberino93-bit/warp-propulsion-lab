# Integration reconciliation — 2026-09-17

Scope: repository history and student release, not an independent audit of the physical claims or every Library archive.

## Ancestry and preservation

At inspection, `main` was `ac6e4f0f5692ac6e118edf27ed9da12a4228790f`; `planning/hardware-acquisition-20260917` at `d6408828bafd8dbdb9e37f8ea7bda50174058c90` was 45 commits ahead, zero behind, with merge-base exactly that `main` SHA. Comparison reported additions of distinct research sessions, source files and tests; no deletion of those files. Subsequent README and this integration note are additive changes on the same branch. This ancestry supports a non-forced fast-forward if `main` is still at that exact ancestor; verify again before advancing it. The prior GitHub Actions run for the earlier branch head was successful, but that result does not certify later edits: require CI for final SHA or run exact merged tests and report limits.

## Cumulative log discrepancy, explicitly retained

`docs/RESEARCH_LOG.md` and `docs/ERROR_LOG.md` remain historically append-only and lag behind the versioned sessions. The earlier [historical backfill](RESEARCH_BACKFILL_2026-09-16.md) documents v0.3.2–v0.3.8 without retroactively rewriting old entries. Later sessions are individually preserved under `research/sessions/2026-09-16-1730-UTC.md` through `research/sessions/2026-09-17-0227-UTC.md` and source/tests in their original commits. These sessions include the conventional photon/reaction-thrust baselines, mechanical/noncontact calibration, artifact floor and blinded Monte Carlo campaign. Their individual reported test outcomes are historical; do not misrepresent them as tests run by this integration note. The latest session's NEXT ONE TEST is non-Gaussian and time-correlated artifact stress testing. Full Library archive bytewise reconciliation and independent scientific replication are NOT claimed. Preserve cumulative logs and consult sessions; future log updates must append verified summaries rather than replace them.

## Student release and rights

README, STUDENTS.md, CONTRIBUTING.md, CREDITS.md, LICENSE.md and hardware acquisition plan introduce an educational entry point and owner-approved scoped licenses (MIT original software, CERN-OHL-S-2.0 original hardware source, CC BY 4.0 original documentation). Third-party material retains its original rights; no endorsement or university collaboration is claimed. Hardware remains a CAD $500–$1,000 planning target, not a validated or purchased device.

## External involvement and safety

At reconciliation, PR #19 discussion returned no comments. This is not a repository-wide proof of no outside involvement; future hourly runs must inspect issues, PR reviews, discussions where available, and new external commits before research. Never overwrite external edits or publish unverified third-party materials under the project's licenses.

## Release criteria

Before moving `main`: verify branch ancestry again, inspect exact final CI/test outcome, and preserve existing session and error history. After moving `main`: read back main SHA and student entry files. If any gate fails, leave main unchanged and record the blocker.
