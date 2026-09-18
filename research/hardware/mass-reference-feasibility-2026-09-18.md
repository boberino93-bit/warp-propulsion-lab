# 0.10 mN mass-reference feasibility calculation

Status: **bounded analytical feasibility result only**. No mass, fixture, sensor or supplier was selected; no hardware was purchased, built, calibrated or measured.

## Question and frozen gate

Can a mass-derived independent reference force plausibly satisfy the frozen calibration-demonstrator ceiling at the lowest signed setpoint?

The governing model is

`F_ref = m × g_local × cos(theta) × (1 - rho_air/rho_mass)`

for a directly applied weight in air, before any pulley, lever or other transfer geometry. The frozen acquisition gate requires `U95 <= 0.020 mN` at nominal 0.10 mN, and the same tolerance must also contain observed DUT bias through `|E| + U95 <= 0.020 mN`.

This calculation tests the reference-force contribution only. It does not allocate uncertainty for a not-yet-defined reversal fixture or DUT.

## Nominal reference mass

At conventional standard gravity:

- target force: 0.100000 mN = 1.00000e-4 N;
- `g_n = 9.80665 m/s^2`;
- required nominal mass before buoyancy correction: `m = F/g_n = 1.0197162e-5 kg = 10.197162 mg`.

A common nominal 10 mg mass would produce 0.0980665 mN before buoyancy correction, about 1.9335% below 0.100000 mN. That value could be used only if the protocol records the actual reference value or is prospectively amended; relabelling it as exactly 0.10 mN would be incorrect.

## Feasibility scenario

The following are explicit prospective requirements, not specifications of an identified product:

| Component | Assumption or bound | Standard uncertainty contribution at 0.10 mN |
| --- | --- | ---: |
| Calibrated mass | certificate supplies actual mass and standard uncertainty no worse than 0.10% relative | 0.0001000 mN |
| Local gravity | documented `g_local` with `u(g) <= 50 micrometres/s^2` | 0.000000510 mN |
| Alignment | residual angle magnitude no greater than 1 degree; conservatively charge the full `1-cos(1 degree)` loss | 0.000015230 mN |
| Air buoyancy | `rho_air = 1.20 +/- 0.12 kg/m^3`, `rho_mass = 8000 +/- 200 kg/m^3`; correct the nominal 0.0000150 mN effect | 0.000001546 mN |

The mass term is obtained directly from relative mass uncertainty. The gravity term is `F × u(g)/g`. The alignment term is intentionally conservative: it treats the full worst-case projection loss as an uncertainty contribution rather than assuming a measured angular correction. The buoyancy uncertainty propagates independent air-density and reference-material-density terms.

Assuming independent inputs:

`u_c = sqrt(sum(u_i^2)) = 0.000101166 mN`

Using `k = 2`:

`U95 = 0.000202333 mN`

This consumes about 1.01% of the frozen 0.020 mN expanded-uncertainty ceiling and leaves 0.0197977 mN for observed DUT bias and all other not-yet-budgeted contributions. The ceiling-to-result ratio is about 98.8.

## Sensitivity and falsification

The mass certificate dominates this illustrative budget. Even a 1% relative mass standard uncertainty, with the other assumptions unchanged, would give approximately `U95 = 0.00200 mN`, still below the reference ceiling. That does not relax the traceability requirement or prove the complete apparatus will pass.

This analytical feasibility result fails if any of the following occurs:

- the actual mass lacks an SI-traceable certificate covering its value and uncertainty;
- local gravity is silently replaced by standard gravity;
- the realized mass/geometry cannot produce the preregistered signed nominal point;
- a pulley, lever, fibre, electrostatic actuator or reversal fixture is added without its ratio, hysteresis, friction and alignment uncertainties;
- buoyancy is omitted or double-corrected;
- the complete reference-plus-DUT budget or guard-banded error exceeds 0.020 mN.

## Result and limitation

**Conditional pass for reference-force feasibility:** the four requested contributions can fit comfortably below the frozen ceiling under the stated, independently verifiable bounds.

**Not yet demonstrated:** an independently certifiable 10.197 mg realization, signed physical reversal, a complete transfer fixture, the DUT contribution, repeatability, drift or any physical calibration. The calculation therefore supports continuing acquisition research but does not clear purchasing or hardware selection.

## Sources

- BIPM, [SI Brochure](https://www.bipm.org/en/publications/si-brochure), including the conventional value of standard acceleration due to gravity.
- BIPM/JCGM, [Guide to the Expression of Uncertainty in Measurement](https://www.bipm.org/en/committees/jc/jcgm/publications), for component and combined uncertainty treatment.
- NIST, [SOP 2: Applying Air Buoyancy Corrections](https://www.nist.gov/system/files/documents/2017/05/09/sop2.pdf), for mass-metrology buoyancy correction principles.
- Natural Resources Canada, [Canadian Spatial Reference System tools](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/gpsh.php?locale=en), as a prospective official route for location-dependent gravity information; no site-specific value was claimed here.

Third-party sources remain under their original rights.

## NEXT ONE TEST

Verify one actual, independently traceable way to realize approximately 10.197 mg and reverse its applied force without exceeding an allocated `U95 = 0.005 mN` reference-plus-transfer budget. Require a public certificate/scope, exact load path, ratio/friction/hysteresis terms and a complete CAD-priced fixture BOM. Reject it if any traceability, signed reversal, uncertainty or CAD $1,000 gate fails. Do not buy a sensor.
