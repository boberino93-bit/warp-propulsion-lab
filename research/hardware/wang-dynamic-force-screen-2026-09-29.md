# Wang et al. dynamic-force implementation screen — 2026-09-29

## Bounded question

Does the published Wang et al. torsion-pendulum implementation demonstrate dynamic reference forces in the 0.1–1 mN target band and satisfy the frozen signed ±0.10 mN evidence gate?

Primary source: C. Wang et al., “Dynamic-force extraction for micro-propulsion testing: Theory and experimental validation,” *Review of Scientific Instruments* 89, 115110 (2018), DOI: https://doi.org/10.1063/1.5037365. Bibliographic record: https://pubmed.ncbi.nlm.nih.gov/30501320/.

## Published implementation

- Torsion-pendulum stand; published steady-force range 1–3000 µN.
- An externally supported coil and arm-mounted permanent magnet generate the reference force. The mechanical reaction closes through the fixed base/bench; this is a calibration actuator, not reactionless propulsion.
- The paper reports a calibrated response of 202.15 µN/V, a 0.6 ohm coil in series with 50 ohms, current below 200 mA, and 120–300 µN square, sinusoidal and sawtooth excitation from 0.05–10 Hz.
- The validation example uses 120 µN at 0.1 Hz. Reported reconstruction error is about 10–14 µN below 8 Hz and less than 15 µN in the stated validated band.
- Independently testable prediction: for the documented fixture and preprocessing, reconstructed waveform force should agree with the electromagnetic reference within the reported error below 8 Hz.

The published amplitude interval is 0.12–0.30 mN, so it intersects the required 0.1–1 mN band. No extrapolation is needed for this magnitude screen.

## Frozen-gate result

**REJECT for the present acquisition gate.**

The screen stopped at the next mandatory field after target-force magnitude. The paper does not publish the frozen randomized, bracketed signed sequence at (-0.10, 0, +0.10) mN, nor an exact-applicable raw record proving sign reversal. Its 10–14 µN reconstruction error is not a covariance-aware expanded uncertainty (U95), and it exceeds the current ±0.10 mN calibrator allocation of (U95 <= 3.0) µN even if it were incorrectly treated as one. The required guarded criterion (|error| + U95 <= 5.0) µN is therefore not demonstrated.

Later raw-record provenance, thermal, electromagnetic, cable, airflow, vibration, drift, construction-rights and complete Canadian-BOM gates were stopped, not waived. The reported voltage-to-force relation gives force scaling for this fixture; the paper does not provide a complete actuator power budget suitable for the project’s demonstrator.

## Falsification and status

A qualifying follow-up would need the exact raw signed cycles, independent traceability, covariance-aware uncertainty and frozen controls. Any missing record, (U95 > 3.0) µN, or (|error| + U95 > 5.0) µN at ±0.10 mN rejects it.

This is a negative paper audit. No hardware was selected, purchased, built or tested; no physical thrust was measured and no propulsion claim follows.
