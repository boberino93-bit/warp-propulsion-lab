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


## Current propulsion handoff — 2026-09-19 00:30 UTC

Latest session: `research/sessions/2026-09-19-0030-UTC.md` (v0.3.47). A documentary specification is frozen for an externally supported noncontact bidirectional calibrator. At ±0.10 mN it allocates (u_c <= 1.5) µN, (U95 <= 3.0) µN and requires `|E| + U95 <= 5.0` µN, with signed and physical reversal plus null, thermal, EM/electrostatic, cable, airflow, vibration, position, creep and drift controls. Voice-coil and opposed-electrode electrostatic principles remain unselected candidates. No hardware, purchase, build or calibration. NEXT ONE TEST: audit one published noncontact voice-coil implementation against the frozen specification, including traceability, signed ±0.10 mN data, covariance-aware uncertainty, controls, rights and a delivered Canadian BOM; reject missing gates and make no purchase.


## Current propulsion handoff — 2026-09-19 01:30 UTC

Latest session: `research/sessions/2026-09-19-0130-UTC.md` (v0.3.48). Schwertheim et al.'s AVM12-6.4 voice-coil calibration is a relevant externally supported architecture with interlaboratory validation over 0.5–100 mN, but it fails the frozen ±0.10 mN gate. The publication does not demonstrate signed ±0.10 mN cycles, (U95 <= 3.0) µN and `|E| + U95 <= 5.0` µN at both signs, the complete covariance-aware control table, redistributable construction rights or a delivered Canadian BOM. No extrapolation, design selection or purchase. NEXT ONE TEST: preregister a paper-only scaling calculation for the AVM12-6.4 architecture at ±0.10 mN using manufacturer force-constant/current data and source-meter uncertainty; stop on missing datasheets or covariance terms and make no purchase.


## Current handoff — 2026-09-19 02:30 UTC

The paper-only signed ±0.10 mN voice-coil scaling protocol is frozen before extraction at `research/hardware/voice-coil-scaling-preregistration-2026-09-19.md`. It pins the AVM12-6.4 and B2902A document hierarchy, equations, covariance-aware uncertainty table, (u_c ≤ 1.5 µN), (U95 ≤ 3.0 µN), guard-band and falsification rules. No calculation ran and no hardware was selected or purchased. NEXT ONE TEST: execute the exact document extraction/calculation once; retain an incomplete table and no estimate if any required specification or covariance bound is missing.


## Current propulsion handoff — 2026-09-28 06:48 UTC

Latest session: `research/sessions/2026-09-28-0648-UTC.md`. The frozen AVM12-6.4/B2902A extraction gate was executed once. Akribis' current exact-model page authenticates 0.54 N/Arms ±10% force constant and 1.10 ohm ±10% resistance, and Keysight's official B2900A-series data sheet provides B2902A source-current accuracy by range. The calculation nevertheless STOPPED before any estimate because the required revision-pinned AVM12-6.4 record and numerical position/current/temperature dependence, hysteresis/remanence, drift and covariance bounds were not available. Unknown terms were not set to zero. No hardware or propulsion result. NEXT ONE TEST: recover the exact revision used by Schwertheim et al. with those missing bounds; if still unavailable, retire this candidate under the frozen gate and audit the opposed-electrode electrostatic candidate.


## Current propulsion handoff — 2026-09-28 07:30 UTC

Latest session: `research/sessions/2026-09-28-0730-UTC.md`. The final bounded AVM12-6.4 document recovery found a 2009 drawing and a post-paper 2021 revision-0 customer drawing, but neither authenticates the experimental revision or supplies the missing position/current/temperature, hysteresis/remanence, drift and covariance bounds. The paper-calculation candidate is retired under the unchanged frozen gate; no estimate or hardware action. NEXT ONE TEST: preregister a paper-only opposed-electrode electrostatic noncontact-calibrator audit at signed ±0.10 mN, freezing the external momentum boundary, force equation, uncertainty/control terms, rights and Canadian-BOM gates before evaluating a design.


## Current propulsion handoff — 2026-09-28 08:35 UTC

Latest session: `research/sessions/2026-09-28-0835-UTC.md`. The paper-only opposed-electrode electrostatic calibrator audit is frozen before candidate evaluation. It fixes the external reaction boundary, `F = 1/2 (V - V_CPD)^2 dC/dx`, electrode-selected sign, covariance-aware uncertainty/control table, signed and physical reversals, traceability, construction-rights, safety and delivered Canadian-BOM gates under the unchanged ±0.10 mN limits. No candidate result, calculation, hardware or measurement. NEXT ONE TEST: apply the table once to the NIST EFB primary record and exact accessible construction evidence; stop on the first mandatory missing gate, without inventing a mirror electrode or making a purchase.


## Current propulsion handoff — 2026-09-28 09:30 UTC

Latest session: `research/sessions/2026-09-28-0930-UTC.md`. The frozen table was applied once to the NIST EFB primary and official follow-on records. NIST documents a concentric-cylinder actuator and micronewton force realization from voltage and capacitance gradient, but the audit STOPPED at the first mandatory missing gate: the exact record does not document two independently characterized opposed electrodes for signed ±0.10 mN selection. No mirror electrode, estimate, right or BOM item was invented; no hardware action or propulsion result. NEXT ONE TEST: preregister a paper-only 0.10 mN photon-pressure calibration audit with momentum closure, absorber/externally supported reflector scaling, traceable power, loss/thermal/alignment controls, uncertainty, safety, rights and CAD $500–$1,000 BOM gates. Do not select or purchase a laser.


## Current propulsion handoff — 2026-09-28 12:35 UTC

Latest session: `research/sessions/2026-09-28-1235-UTC.md`. The paper-only signed ±0.10 mN photon-pressure audit is frozen. It fixes external momentum closure, `F=P/c` absorption and ideal externally supported `F=2P/c` reflection, ideal lower-bound powers of 29,979.2458 W and 14,989.6229 W, traceable optical momentum, signed/physical reversals, null/loss/thermal/EM/alignment/airflow controls, covariance-aware uncertainty, rights, CAD $500–$1,000 BOM and qualified laser-safety gates. A self-contained source/mirror system has zero net external force. No candidate, laser, purchase, operation or measurement. NEXT ONE TEST: apply the table once to NIST HALO/EFB photon-momentum evidence; stop at the first missing mandatory gate and do not extrapolate 0.1–5 kW data to 15–30 kW.


## Current propulsion handoff — 2026-09-28 13:40 UTC

Latest session: `research/sessions/2026-09-28-1340-UTC.md`. The frozen photon-pressure table was applied once to NIST's HALO/EFB record. The audit stopped at the first mandatory failure: the fixed multi-reflection implementation does not demonstrate two independently characterized opposed directions or a complete physical reversal at signed ±0.10 mN. Laser on/off is a null, not negative force. No rights/BOM/safety pass was inferred after the stop; no hardware, extrapolation, purchase, build or force measurement occurred. NEXT ONE TEST: preregister a paper-only low-risk mechanical or electromagnetic reference-force screen with inherent sign reversal at ±0.10 mN under the unchanged uncertainty, rights, Canadian BOM and personal-prototype safety gates.


## Current propulsion handoff — 2026-09-28 14:28 UTC

Latest session: `research/sessions/2026-09-28-1428-UTC.md`. Froze a paper-only comparison protocol for differential deadweight/symmetric transfer and independently calibrated current-reversed voice-coil reference forces at signed ±0.10 mN. It retains the existing uncertainty, guard-band, reversal, null/thermal/EM/cable/airflow/vibration, rights, complete Canadian BOM and personal-safety gates. No candidate, component, price, purchase, build or measurement. NEXT ONE TEST: apply the table once to one published implementation from each family; stop each at its first mandatory failure and make no purchase.


## Current propulsion handoff — 2026-09-28 18:34 UTC

Latest session: `research/sessions/2026-09-28-1834-UTC.md`. The frozen table was applied to the DLR AST weight-on-string calibration and Lam et al. voice-coil calibrator. DLR failed at the first signed-reversal gate because the published system is a one-direction pull and provides no symmetric opposed `-0.10/0/+0.10 mN` cycles. The Lam primary publisher record reports `30–23,000 µN` magnitudes and `7.80–18.48%` steady-force uncertainty errors but does not document complete current reversal or negative cycles at `±0.10 mN`; that mandatory field is UNKNOWN and therefore failed. Later gates were not scored. No selection, purchase, build, calibration or thrust measurement. NEXT ONE TEST: preregister a documentary evidence-request matrix freezing the minimum raw signed cycles, sign convention and uncertainty fields needed for each family before any author/supplier contact or purchase.


## Current propulsion handoff — 2026-09-28 19:34 UTC

Latest session: `research/sessions/2026-09-28-1934-UTC.md`. Froze a minimum evidence-request matrix for signed differential mechanical transfer and installed-geometry current-reversed voice-coil calibration. It defines exact provenance, cycle-row, sign, blinding, reversal, raw-hash, covariance and family-specific fields under the unchanged ±0.10 mN acceptance limits. No author/supplier contact, component, price, purchase, build, calibration or measurement occurred. NEXT ONE TEST: audit the two publications’ public supplementary/raw-data locations against the matrix and stop each family at its first missing mandatory field; do not contact or purchase.


## Current propulsion handoff — 2026-09-28 20:27 UTC

Latest session: `research/sessions/2026-09-28-2027-UTC.md`. Applied the frozen evidence-request matrix to public supplementary/raw-data locations for the DLR AST and Lam voice-coil publications. Both stopped at the first mandatory missing field: no versioned exact-apparatus/raw-package identity and hash was publicly verifiable. DLR’s official article says data/materials availability is not applicable; the Lam publisher endpoint exposed no such package and direct access returned HTTP 403. Later fields were not scored. No contact, purchase, build, calibration, force measurement or propulsion result. NEXT ONE TEST: preregister a bounded privacy-preserving author data-request protocol asking only for the missing artifact-identity fields; freeze consent/credit/licensing handling and send nothing.


## Current propulsion handoff — 2026-09-29 01:26 UTC

Latest session: `research/sessions/2026-09-29-0126-UTC.md`. Froze a privacy-preserving request protocol for the exact artifact-identity fields missing from the DLR AST and Lam voice-coil public records. It limits any later request to existing apparatus/drawing/BOM/software revisions, raw-package identifier/hash, location and reuse terms; freezes consent, credit, rights, attachment quarantine, redaction, contact-count and stopping rules. No message was sent, no person contacted and no candidate status changed. No hardware or measurement. NEXT ONE TEST: audit one public institutional or publisher-designated professional contact route and current rights statement for each publication without sending, opening an account or collecting private contact data.


## Current propulsion handoff — 2026-09-29 02:34 UTC

Latest session: `research/sessions/2026-09-29-0234-UTC.md`. The public route/rights audit verified a publisher-designated corresponding-author role and institutional route for both the DLR AST and Lam voice-coil publications. The DLR article is CC BY 4.0 with third-party exclusions and states data/materials are not applicable; that article licence does not cover unpublished apparatus/software/raw packages. The Lam publisher/institutional records expose no public artifact-package licence; any nonpublic package requires explicit written permission. No message was sent, no account opened and no contact detail retained. Candidate evidence remains incomplete. NEXT ONE TEST: freeze two route-specific, field-for-field request drafts and a pre-send decision table; send nothing and expose no contact details.


## Current propulsion handoff — 2026-09-29 03:33 UTC

Latest session: `research/sessions/2026-09-29-0333-UTC.md`. Two route-specific, field-for-field artifact-identity request drafts and a pre-send decision table are frozen. The DLR draft preserves the article-versus-unpublished-artifact CC BY 4.0 boundary; the Lam draft requires explicit written permission for nonpublic material. Unrechecked live-target, newly-public-package, external-correction, prior-contact and authorization gates remain `SEND BLOCKED`. No message or contact occurred and no contact details were retained. NEXT ONE TEST: run a dry, no-send completeness and redaction audit against the frozen eight-field protocol and pre-send table; retain any mismatch and send nothing.


## Current propulsion handoff — 2026-09-29 07:25 UTC

Latest session: `research/sessions/2026-09-29-0725-UTC.md`. The dry no-send audit found both route-specific request drafts complete for all eight frozen fields and free of private contact data, unnecessary personal identifiers, affiliation claims and executable/credential-bearing attachment instructions. No textual mismatch required correction. Sending remains blocked because live target, newly public package, current route/current rights, complete prior-contact history and explicit authorization are not all established. No contact or hardware action occurred. NEXT ONE TEST: in one no-send session, recheck only those unresolved live gates for both publication families; if any remains unresolved, retain `SEND BLOCKED` and stop.


## Current propulsion handoff — 2026-09-29 08:37 UTC

Latest session: `research/sessions/2026-09-29-0837-UTC.md`. A one-pass live recheck retained `SEND BLOCKED` for both DLR and Lam publication families. DLR's article still reports data/materials availability as not applicable; Lam's exact article remains identifiable, but no qualifying package was exposed and the previously used institutional endpoint was inaccessible. Complete off-repository prior-contact history is not establishable. No contact, hardware action or experiment occurred. NEXT ONE TEST: screen one different openly documented, inherently reversible ±0.10 mN reference-force implementation for a public raw calibration package, explicit construction/reuse rights and a complete uncertainty record; stop at the first mandatory failure and make no purchase.


## 2026-09-29 09:30 UTC handoff

- Screened Planck-Balance 1 against the frozen ±0.10 mN reversible reference-force gate.
- Retained negative result: the paper documents mass-on/mass-off ABBA operation and opposite coil currents, but not randomized signed `-0.10/0/+0.10 mN` applied-force cycles; it states equal-and-opposite-current tare operation becomes difficult below 1 g.
- Later acquisition gates were stopped, not waived. Article CC BY 4.0 was not treated as hardware/source licensing. No purchase, build, calibration, or thrust measurement.
- Artifact: `research/hardware/pb1-signed-force-screen-2026-09-29.md`.
- Session: `research/sessions/2026-09-29-0930-UTC.md`.
- **NEXT ONE TEST:** screen NIST KIBB-g2.0 for documented signed low-force cycles, complete uncertainty near ±0.10 mN, public raw records, and explicit reusable construction/source rights; stop at the first mandatory failure and make no purchase.
