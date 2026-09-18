# Surrey/AVS torsional flex-pivot balance evidence-gate audit — 2026-09-18

## Question and frozen acceptance gate

Can the published Surrey Space Centre / Added Value Solutions torsional flex-pivot balance demonstrate the project's unchanged signed force-transfer allocation at the lowest calibration point?

Acceptance remains:

- repeated signed calibration at `-0.10 mN`, zero, and `+0.10 mN`;
- an independently traceable applied-force reference and complete transfer chain;
- numerical contributions for reference calibration, geometry/ratio, contact and alignment, direction-dependent hysteresis, flex-pivot creep/return, thermal drift, cables/lines, electromagnetic coupling, airflow/vacuum and readout/repeatability;
- combined expanded uncertainty `U95 <= 0.005 mN` for reference plus transfer, inside the overall `U95 <= 0.020 mN` lowest-point ceiling;
- no missing term silently assigned zero.

## Primary source

S. Masillo, J. Stubbing, K. Swar, D. Staab, A. Garbayo, and A. Lucca Fabris, “Validation of a torsional balance for thrust measurements of Hall effect and microwave-based space propulsion systems,” *Review of Scientific Instruments* 93, 114501 (2022), DOI: https://doi.org/10.1063/5.0117584 (open access, CC BY 4.0). Institutional copy: https://sussex.figshare.com/articles/journal_contribution/Validation_of_a_torsional_balance_for_thrust_measurements_of_Hall_effect_and_microwave-based_space_propulsion_systems/29489210

Source checked 2026-09-18.

## What the publication demonstrates

The instrument is a titanium rotating beam on a flex pivot with optical-fiber displacement readout. A Novatech F329 load cell on a motorized stage contacts the beam at the same nominal 250 mm arm as the thruster. The final installed system is calibrated under vacuum, so cable and propellant-line stiffness are included in the fitted equivalent stiffness. Liquid-metal DC connections, contactless microwave transmission, a water-cooled pivot hub and vibration-damping feet address known disturbance paths.

The generic low-range example applies ten increasing load values over approximately 0.2–3 mN and repeats the calibration nine times (81 observations). The reported fitted stiffness is approximately 22.2 mN/µm with a 3σ spread of 2.2 mN/µm, and the fit reports `R² = 0.9994`. The XJET installation uses three ten-plateau sequences over 0–about 8 mN; six sequences over two sessions give 1.95% best-fit uncertainty at 3σ. These are useful repeated, in-situ calibration results.

The publication’s propulsion tests are conventional reaction-thrust tests: xenon is expelled by Hall-effect and electron-cyclotron-resonance thrusters, so momentum closes through the exhaust and facility. They are not reactionless-thrust evidence.

## Gate result

**Reject for the present 0.10 mN demonstrator gate.**

1. The lowest explicitly reported calibration range begins near 0.2 mN, not at the required signed 0.10 mN point.
2. The calibration direction is described as the same as the thrust vector. The load cell advances into contact and returns to its original position; the record does not establish independent negative-force plateaus or repeated `-0.10/0/+0.10 mN` signed cycles.
3. The reported 3σ spread or best-fit percentage characterizes calibration-factor repeatability. It is not a complete traceable `U95` budget for the applied load cell plus contact transfer at 0.10 mN.
4. The accessible article does not provide an individual calibration certificate/scope for the F329 reference or numerical terms at 0.10 mN for contact alignment, force-arm ratio, contact friction/stiction, direction-dependent hysteresis, flex-pivot creep/return, thermal drift and other frozen transfer terms.
5. Extrapolating the 1.95% 3σ XJET fit to 0.10 mN would be outside the reported 0–8 mN calibration evidence and would still omit the reference and transfer-chain terms. No such extrapolation is accepted.

The paper therefore advances the design evidence—especially in-situ calibration and repeated-session practice—but cannot numerically demonstrate `U95 <= 0.005 mN` at signed 0.10 mN. No hardware, supplier, affiliation, purchase, build, calibration or thrust measurement is claimed.

## NEXT ONE TEST

Freeze a documentary specification for a noncontact bidirectional 0.10 mN calibrator (voice-coil or electrostatic) that eliminates contact stiction, with independently traceable input-to-force calibration and a complete `U95 <= 0.005 mN` term table. Do not select or buy hardware until one published implementation supplies the required numerical evidence.
