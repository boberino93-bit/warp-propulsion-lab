# Planck-Balance 1 signed-force reference screen (2026-09-29)

## Scope and frozen gate

This paper-only screen evaluates exactly one additional reversible reference-force implementation against the current ±0.10 mN demonstrator gate. It makes no purchase, build, calibration, thrust measurement, affiliation, or propulsion claim.

Target force: `0.100000 mN = 100.000 µN`. At standard gravity this is `10.197162130 mg`.

Candidate: **Planck-Balance 1 (PB1)**, a tabletop Kibble balance reported by PTB and TU Ilmenau.

Primary source:
- S. Vasilyan et al., “Planck-Balance 1 (PB1) – a table-top Kibble balance for masses from 1 mg to 1 kg – current status,” *Acta IMEKO* 9(5), 2020. DOI: https://doi.org/10.21014/acta_imeko.v9i5.937
- Publisher PDF: https://acta.imeko.org/index.php/acta-imeko/article/download/IMEKO-ACTA-09%20%282020%29-05-32/pdf

The article is marked CC BY 4.0 by the publisher. That license covers the article; it is not evidence that the apparatus design, firmware, drawings, or third-party components are released under construction/reuse terms.

## Physical boundary and prediction

PB1 is a reaction-force metrology system. Its voice coil exchanges momentum with a laboratory-supported magnetic circuit, load cell, frame, and ultimately Earth. It is not a propulsion candidate.

In force mode, the voice-coil force balances a mass load. In velocity mode, the apparatus determines the force factor. The independently observable prediction relevant here is that reversing coil-current sign reverses electromagnetic force while the instrument records current and position. The paper describes equal-magnitude opposite-sign currents in mass-on/mass-off states to cancel current-dependent effects.

## Frozen gate result

| Gate | Evidence | Decision |
|---|---|---|
| Correct live target and boundary | The paper states a nominal 1 mg–1 kg range and a force/velocity-mode Kibble balance; 0.10 mN corresponds to 10.197162130 mg. | Pass for range and boundary only |
| Demonstrated signed ±0.10 mN cycles | Published trials are mass-on/mass-off ABBA sequences. The paper says equal-magnitude opposite currents require tare weights and become difficult below 1 g. It does not report randomized `-0.10/0/+0.10 mN` applied-force cycles. | **Fail — stop** |
| Full uncertainty at ±0.10 mN | Not evaluated after the first mandatory failure. Context only: the paper says the installed load cell limits small-mass work, reports increasing deviation as mass decreases, and treats several effects as work in progress. | Not reached |
| Public raw calibration package | Not evaluated after stop. No raw signed-cycle package was identified in the publisher record inspected. | Not reached |
| Explicit construction/reuse rights | Not evaluated after stop. Article CC BY 4.0 is not apparatus-source licensing. | Not reached |
| Complete Canadian BOM within CAD 500–1,000 | Not evaluated after stop. | Not reached |

The paper reports useful component-level evidence—including a 10 g force-mode standard deviation near 0.2 mg (about 1.96 µN), 2.4 ppm relative repeatability across 19 force-factor determinations, and unresolved small-mass, magnetic-temperature, positioning, nonlinearity, frequency-response, and Abbe-error limitations. Those values cannot be substituted for an expanded uncertainty at signed ±0.10 mN.

## Controls and falsification

A future candidate must publish or make independently reproducible:

- randomized signed `-0.10/0/+0.10 mN` cycles;
- a complete uncertainty budget at that force, including reversal asymmetry, hysteresis, creep, drift, thermal, electromagnetic, cable, airflow, vibration, alignment, and readout terms;
- raw records sufficient to recompute calibration and null/reversal statistics;
- explicit reusable construction/source rights; and
- a complete orderable Canadian BOM within CAD 500–1,000.

Any missing mandatory item rejects acquisition. PB1 is therefore **not selected** for this demonstrator.

## Reproducible arithmetic check

```text
equivalent_mass_mg=10.197162130
target_check= True
```

## Evidence status

This is a bounded literature screen and retained negative result. No hardware was selected, purchased, built, calibrated, or tested; no thrust was measured.

## Next one test

Screen the published NIST KIBB-g2.0 implementation for documented signed low-force cycles, complete uncertainty at approximately ±0.10 mN, public raw records, and explicit reusable construction/source rights; stop at the first mandatory failure and make no purchase.
