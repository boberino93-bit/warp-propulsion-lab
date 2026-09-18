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


## Current propulsion handoff — 2026-09-18 07:31 UTC

Latest session: `research/sessions/2026-09-18-0731-UTC.md` (v0.3.39). A primary-source screen compared the Georgia Tech torsional impulse stand (AIAA 2018-2117) and AST/DLR low-drift balance (IEPC-2015-257). Neither clears acquisition: steady 0.1–1 mN calibration, independent calibration, redistributable construction source/rights, and a complete live-priced CAD 500–1,000 BOM were not all demonstrated. No design was selected and no purchase was made. NEXT ONE TEST: resolve those rights/BOM/calibration gates for one openly reproducible published candidate; reject it above CAD 1,000 or without published 0.1–1 mN calibration. Do not purchase hardware.


## Current propulsion handoff — 2026-09-18 08:29 UTC

Latest session: `research/sessions/2026-09-18-0829-UTC.md` (v0.3.40). The MIT-licensed Pablo18011 RC Motor Thrust Stand was rejected for acquisition. Its 5 kg load-cell package has no published 0.1–1 mN calibration, uncertainty, raw calibration results or required artifact controls; its parts list is not an orderable Canadian BOM and its schematic path contains no construction drawing. No substitutions or prices were invented, no design was selected and no purchase was made. NEXT ONE TEST: preregister a procurement-neutral 0.1–1 mN calibration-demonstrator requirements matrix with traceable independent force, signed reversal, environmental controls and maximum uncertainty before selecting a sensor.

## Current propulsion handoff — 2026-09-18 09:30 UTC

Latest session: `research/sessions/2026-09-18-0930-UTC.md` (v0.3.41). The procurement-neutral 0.1–1 mN calibration-demonstrator matrix is frozen: independent SI-traceable reference; signed setpoints; ten randomized cycles; bracketed zeros; JCGM-style uncertainty; null/reversal/thermal/EM/cable/airflow/vibration controls; and guard-banded acceptance. At 0.10 mN, `U95` must not exceed 0.020 mN and `|E| + U95` must also remain within 0.020 mN. No sensor, stand or supplier was selected, no purchase was authorized, and no physical calibration ran. NEXT ONE TEST: calculate whether a procurement-neutral mass-derived reference at 0.10 mN can satisfy the frozen ceiling after mass, local-gravity, alignment and buoyancy uncertainty. Do not select or buy a sensor.


## Current propulsion handoff — 2026-09-18 13:30 UTC

Latest session: `research/sessions/2026-09-18-1330-UTC.md` (v0.3.42). A mass-derived 0.100000 mN reference requires 10.197162 mg at standard gravity before buoyancy correction. Under explicit prospective bounds (0.10% mass standard uncertainty, local-gravity `u <= 50 micrometres/s^2`, conservative 1 degree alignment charge, and bounded air/material density), the four-term reference budget gives `u_c = 0.000101166 mN` and `U95(k=2) = 0.000202333 mN`, about 1.01% of the frozen 0.020 mN ceiling. This is conditional analytical feasibility only: no certified mass, reversal fixture, DUT, build or calibration was demonstrated. NEXT ONE TEST: verify one real traceable realization near 10.197 mg plus a signed reversal transfer method under an allocated `U95 = 0.005 mN` reference-plus-transfer budget, with certificate/scope, load path, friction/hysteresis uncertainty and complete CAD-priced fixture BOM. Reject missing gates; make no purchase.


## Current propulsion handoff — 2026-09-18 14:32 UTC

Latest session: `research/sessions/2026-09-18-1432-UTC.md` (v0.3.43). The certificate-backed reference realization gate failed: no publicly inspectable candidate combined an individual calibrated-value/uncertainty certificate, exact delivered Canadian price and a signed reversal transfer with bounded ratio, friction/stiction and hysteresis. A nominal 10 mg artifact supplies 0.0980665 mN at standard gravity before buoyancy, not 0.100000 mN. No product, fixture or sensor was selected or purchased. NEXT ONE TEST: compare complete-DUT inversion and symmetric filament/flexure transfer in a frozen uncertainty table; reject unless the complete signed path fits `U95 <= 0.005 mN`.


## Current propulsion handoff — 2026-09-18 18:35 UTC

Latest session: `research/sessions/2026-09-18-1835-UTC.md` (v0.3.44). Complete-DUT inversion and symmetric filament/flexure transfer were compared under one frozen allocation: `u_c = 0.002385421 mN`, `U95 = 0.004770843 mN`, margin `0.000229157 mN`. Both fail the evidence gate: inversion lacks measured reseating/cable/gravity-vector/thermal bounds; filament/flexure lacks measured ratio/friction/stiction/creep/hysteresis bounds. No design or purchase. NEXT ONE TEST: audit one published symmetric flexure/filament low-force transfer with repeated signed calibration data against the table; reject missing terms or `U95 > 0.005 mN`.


## Current propulsion handoff — 2026-09-18 19:31 UTC

Latest session: `research/sessions/2026-09-18-1931-UTC.md` (v0.3.45). Frieler and Groll’s 2018 torsional spring-leaf balance was audited against the frozen signed-transfer table. Its automated weight calibration and repeated-run capability are relevant, but the accessible record does not provide signed ±0.10 mN cycles or quantitative transfer-ratio, friction/stiction, hysteresis, creep and thermal terms. Reported 15 µN estimated resolution is not expanded uncertainty and alone equals 75% of the 20 µN lowest-point ceiling. Candidate rejected; no design or purchase. NEXT ONE TEST: audit the 2022 Surrey/AVS torsional flex-pivot balance’s bidirectional calibration/repeatability data against the same table; reject missing numerical terms or `U95 > 0.005 mN`.

## Current propulsion handoff — 2026-09-18 20:30 UTC

Latest session: `research/sessions/2026-09-18-2030-UTC.md` (v0.3.46). The Surrey/AVS flex-pivot balance provides useful repeated in-situ calibration evidence, including nine 0.2–3 mN repetitions and a separate six-sequence/two-session XJET fit, but it fails the frozen lowest-point gate. The publication does not demonstrate signed `-0.10/0/+0.10 mN` cycles or a complete traceable reference/contact-transfer budget with `U95 <= 0.005 mN` at 0.10 mN. No design or purchase. NEXT ONE TEST: freeze a documentary specification for a noncontact bidirectional 0.10 mN calibrator with independently traceable input-to-force calibration and a complete uncertainty table before selecting hardware.
