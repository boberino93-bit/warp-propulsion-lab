# Open-source thrust-stand acquisition gate — 2026-09-18

## Decision

The MIT-licensed [Pablo18011 RC Motor Thrust Stand](https://github.com/Pablo18011/RC-MOTOR-THRUST-STAND) was screened at upstream commit `e5593bd01c35a8805df4f7739a2e728ce212812c`. It does not clear this project's acquisition gate. No design was selected and no hardware was purchased.

The project is a useful open educational reaction-thrust stand for hobby propellers. It is not published evidence of calibrated steady-force performance at 0.1–1 mN, and its parts list is not a complete procurement BOM.

## Provenance and rights

- Upstream author: Pablo18011 / @pablofpv.
- Latest inspected upstream commit: `e5593bd01c35a8805df4f7739a2e728ce212812c`, dated 2023-11-16.
- Upstream repository license: MIT, copyright 2023 Pablo18011.
- The upstream license and credit must be preserved. Nothing here relicenses upstream work under this project's hardware license.
- The repository contains Arduino code, component descriptions, photographs and supporting material. The inspected `Schematic/` path contains only a one-byte placeholder; no dimensioned CAD/construction package was found.

## Momentum and power boundary

The candidate measures ordinary propeller reaction thrust in air. Momentum is transferred to accelerated air and ultimately the room/Earth; the battery or power source supplies electrical power through the ESC and motor. This is a valid established reaction-thrust reference class, not reactionless propulsion.

The upstream package states a 5 kg load cell, Arduino Nano, HX711 amplifier, PWM ESC, motor and propeller. It does not publish a traceable force-versus-power model or measured thrust/power scaling with uncertainty.

## Calibration-range gate

The required project band is 0.1–1 mN.

Using standard gravity, the equivalent calibration masses are:

- 0.1 mN / 9.80665 m/s² = 0.010197 g;
- 1.0 mN / 9.80665 m/s² = 0.101972 g.

Against a 5 kg full-scale load cell, those forces are approximately 2.04 parts per million to 20.4 parts per million of full scale.

The upstream instructions say to calibrate with a known weight and display thrust in grams, but publish no calibration points, residuals, effective resolution, noise spectrum, drift, hysteresis, repeatability, linearity, uncertainty budget or raw calibration data in this band. Nominal ADC bit depth cannot substitute for demonstrated system resolution.

**Result:** FAIL. Published calibration does not cover 0.1–1 mN.

## Controls gate

The upstream package does not document the controls required for this project:

- signed force reversal;
- sham motor/thermal cycles;
- independent mechanical calibration;
- thermal logging;
- electromagnetic pickup tests;
- cable-force tests;
- airflow enclosure and ambient monitoring;
- repeated null distributions and drift characterization.

Its README explicitly warns that a fast propeller may start without warning and can cause injury. No build or operational instruction is adopted here.

**Result:** FAIL for the intended microforce instrument.

## BOM and cost gate

The upstream component list identifies broad categories, including four breadboards, an Arduino Nano-compatible board, 5 kg load cell with HX711, LCD, ESC, sensor modules, wiring, aluminium bar, carbon arm, fasteners, motor and connectors.

It does not provide manufacturer and orderable part numbers for most items, Canadian suppliers, current stock, unit prices, quantities for all mechanical/safety items, a vice or rigid base, power source, propeller, calibration masses/actuator, enclosure, environmental sensors, tax, shipping or substitutions. A complete live-priced Canadian BOM cannot be produced from this source without silently choosing a materially new design.

Because the calibration gate already fails and the source BOM is under-specified, pricing arbitrary substitutions would not establish reproducibility.

**Result:** UNRESOLVED/FAIL. CAD 500–1,000 compliance is not verified.

## Falsification and evidence status

This rejection would be reversed only by source-linked evidence showing a complete, legally redistributable construction package, traceable calibration across 0.1–1 mN with uncertainty and raw results, required controls, and a complete live-priced Canadian BOM within budget.

This screen reports no build, measured thrust, calibration, independent replication, institutional affiliation or propulsion discovery. The historical 35 µN threshold remains synthetic only.

## NEXT ONE TEST

Define and preregister a procurement-neutral 0.1–1 mN calibration demonstrator requirements matrix, including an independent gravitational or other traceable force source, signed reversal, enclosure/environmental controls, and maximum allowable uncertainty. Do not select or purchase a sensor until one published component datasheet plus system-level evidence can satisfy the matrix.
