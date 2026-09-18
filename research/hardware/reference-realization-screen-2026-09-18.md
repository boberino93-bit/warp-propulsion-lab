# Certificate-backed reference realization screen — 2026-09-18

## Decision

**Reject acquisition at this gate.** No product or fixture is selected and no purchase is authorized.

The previous analytical result established only that a mass-derived force reference can fit the frozen uncertainty ceiling. This screen asked whether that reference can be realized now with public, independently checkable evidence and a complete Canadian-dollar fixture cost.

## Frozen gate

A candidate must provide all of the following before selection:

1. an individually calibrated mass near 10.197162 mg, with certificate identifier, accredited scope, calibration date, conventional-mass value and expanded uncertainty;
2. a documented conversion from certificate value to local force including local gravity and air buoyancy;
3. a signed reversal load path that applies both polarities without changing the device under test;
4. measured or independently bounded transfer ratio, alignment, friction, stiction and hysteresis;
5. combined reference-plus-transfer expanded uncertainty `U95 <= 0.005 mN`;
6. a complete, orderable Canadian-supplier BOM with taxes/shipping identified and total project hardware remaining within CAD 500–1,000;
7. construction rights compatible with the repository's hardware policy.

## Screen result

Public searches of three established calibration-weight suppliers did not yield a candidate whose public record simultaneously exposed the individual certificate data, exact delivered Canadian price and signed-force transfer implementation required above. A catalog statement that an accredited certificate is available is not the certificate for the delivered artifact. A nominal 10 mg weight is also not an exact 0.100000 mN reference: at standard gravity it supplies 0.0980665 mN before buoyancy. That value could be useful as a nearby calibration point only after the actual certified mass and site corrections are known.

No public evidence was located for a complete, low-friction bidirectional transfer fixture with measured ratio, friction/stiction and hysteresis uncertainty at the required scale. Consequently, neither a certificate-backed force realization nor the allocated `U95 = 0.005 mN` transfer budget can be verified. Pricing snippets and generic accreditation claims were not treated as an orderable BOM.

## Momentum boundary and falsification

The reference transfers Earth's gravitational reaction through the calibrated mass and fixture into the stand; it is not propellantless thrust. The method is falsified for acquisition if any mandatory certificate field, signed reversal, uncertainty term, construction right or delivered-price line is absent. That falsification condition was met.

## Sources and provenance

- BIPM, *SI Brochure*, 9th edition, definition and realization of SI units: https://www.bipm.org/en/publications/si-brochure
- JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*: https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf
- NIST Handbook 44 (2026), traceable weighing and device requirements: https://www.nist.gov/pml/owm/nist-handbook-44-current-edition
- Supplier domains screened for publicly verifiable 10 mg certificate/product evidence: https://www.troemner.com/ , https://www.mt.com/ , https://www.ricelake.com/

Supplier material is evidence of availability only, not independent validation. No quotation was requested and no private contact data was collected.

## Next one test

Compare two procurement-neutral signed transfer architectures—complete-DUT inversion and a symmetric filament/flexure transfer—using one frozen analytical uncertainty table. Reject either architecture unless friction/stiction, hysteresis, alignment, reversal symmetry and traceability can fit `U95 <= 0.005 mN` without hazardous construction or a purchase.
