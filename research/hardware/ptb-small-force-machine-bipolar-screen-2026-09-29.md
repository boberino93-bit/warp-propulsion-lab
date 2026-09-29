# PTB small-force machine — bipolar target-band screen (2026-09-29)

## Candidate and primary sources

Christian Schlegel, Oliver Slanina, Günther Haucke and Rolf Kumme, “Construction of a standard force machine for the range of 100 μN–200 mN,” *Measurement* 45 (2012), 2388–2392, DOI: https://doi.org/10.1016/j.measurement.2011.11.022. A four-page 2010 conference paper from the same authors is openly available from IMEKO: https://www.imeko.org/publications/tc3-2010/IMEKO-TC3-2010-NP-009.pdf. PTB lists both publications: https://www.ptb.de/cms/en/ptb/fachabteilungen/abt1/fb-12/ag-121/publications.html.

## Frozen-gate result

**Reject at the explicit bipolar-record gate.** The implementation covers the requested magnitude band, but the published record is a one-direction pressing/load experiment rather than a signed bipolar reversal record.

- **Range:** the machine is described for 0.1–200 mN. The target 0.1–1 mN interval is therefore inside its stated range.
- **Momentum boundary/reservoir:** a nanopositioning table presses the force transducer against an electromagnetically compensated balance. Action/reaction closes through the transducer suspension, balance, nanopositioning table and machine frame/base.
- **Force scaling:** the balance controller increases coil current to generate a Lorentz force that restores the lever position; the balance indication is compared with the transducer output. The paper reports 1 μg readability and 3 μg standard deviation for the 20 g balance.
- **Independent measurable prediction:** the transducer output should agree with the balance-equivalent force after calibration against the PTB 200 N force-standard machine and an E2 mass set.
- **Published controls/uncertainty:** ISO 376 loading/unloading and transducer rotation are design capabilities; the photograph notes foil shielding against thermal influence. At about +100 mN, the reported relative deviation starts at 0.05–0.1% and drifts toward about 0.17% after one hour. The table’s small-force uncertainty is estimated rather than demonstrated by a frozen signed trial.
- **First mandatory failure:** the paper describes pressing the transducer and balance together, presents positive load steps and one approximately +100 mN time record, and publishes no explicit randomized bracketed signed `-0.10/0/+0.10 mN` force record. Rotation of a compression transducer is not force-sign reversal.

The audit stops at this first mandatory failure. A covariance-aware `U95 <= 3.0 μN` demonstration, `|error| + U95 <= 5.0 μN`, complete raw bipolar records, null/reversal/thermal/EM/cable/airflow controls, redistributable construction rights and a verified Canadian BOM are **not waived**.

## Evidence status

Public-document screen only. No hardware was selected, purchased, built, calibrated or tested; no thrust was measured; no propulsion claim or discovery follows.
