# Hardware acquisition plan — experimental propulsion track

Status: planning only; no hardware purchased, built, calibrated or tested. Robert plans an initial personal prototype documented for university-student reproduction. No university affiliation is claimed.

## Decision and constraints

- Adapt and reproduce an existing published, independently documented thrust-stand design rather than inventing a new instrument from scratch. Survey university/NASA/JPL publications and open hardware projects; verify original design files, measured noise/drift, calibration, rights and replicability. An upstream design keeps its own license and is **not** automatically relicensed under this project's CERN-OHL-S-2.0 license. See [LICENSE.md](../LICENSE.md).
- Initial budget: CAD $500–$1,000 including parts, consumables, shipping/taxes where possible. Existing equipment: 3D printer, soldering station, multimeter. Personal prototype first; document for subsequent student reproduction.
- First target: physically calibrate approximately 0.1–1 mN, magnitude and sign, with documented uncertainty. Earlier 35 µN detection threshold is synthetic, not measured performance or procurement guarantee.
- No purchasing before comparing published designs and reviewing a complete costed BOM and realistic sensitivity/error budget.

## Acquisition gates

1. Find at least two credible published designs; record primary references, upstream license and permitted modifications, CAD/electronics/software availability, actual measured performance, constraints and total build cost.
2. Produce a BOM with manufacturer/part number, quantity, CAD unit and extended cost, supplier, stock, tax/shipping, substitutions and existing-tool offsets. Verify live prices before purchase.
3. Specify rigid base/enclosure, suitable sensor or torsion balance, independently characterized mechanical calibration, environmental monitoring, logging and reversible fixture. Verify geometry, load path, sign and resolution.
4. Complete safety review: no improvised pressure vessels, high voltage, high-power lasers or vacuum equipment. Use low-risk established reaction-thrust examples only after calibration and suitable supervision.
5. Freeze acceptance criteria before tests: 0.1–1 mN reference forces, correct sign, repeatability, combined-uncertainty agreement, sham/reversal/null controls. Measure power and expelled mass/velocity as applicable and close full-system momentum boundary.
6. Release original project-owned CAD, BOM, build guide, schematics, calibration, uncertainty, raw data, analysis and student exercises with the category-specific licenses in LICENSE.md. Preserve third-party terms, credits and negative results; no claimed endorsement.

## Primary-source screen result — 2026-09-18

The [first two-candidate screen](../research/hardware/thrust-stand-primary-source-screen-2026-09-18.md) found that neither the Georgia Tech pulsed torsional stand nor the AST/DLR low-drift balance currently clears every acquisition gate. The missing items include a completed independent calibration in the target band, complete redistributable construction source with explicit rights, and a live-priced full BOM. No design was selected and no purchase was authorized.

## Open-source candidate result — 2026-09-18 08:29 UTC

The [MIT-licensed hobby stand screen](../research/hardware/open-source-stand-gate-2026-09-18.md) found usable code and a component outline, but no demonstrated 0.1–1 mN calibration, uncertainty, complete construction drawings, artifact-control package or procurement-grade Canadian BOM. It was rejected without inventing substitutions or prices.

## Immediate next hardware task

Preregister a procurement-neutral 0.1–1 mN calibration-demonstrator requirements matrix. Specify a traceable independent force source, signed reversal, enclosure and environmental controls, and maximum allowable uncertainty before selecting or pricing a sensor. No purchase authorization is implied.

## Frozen calibration-demonstrator gate — 2026-09-18

Before any sensor or stand selection, apply `research/hardware/calibration-demonstrator-requirements-2026-09-18.md`. It requires an independent traceable reference, signed 0.1–1 mN calibration, ten randomized cycles, complete uncertainty, guarded error, and null/reversal/thermal/EM/cable/airflow/vibration controls. At 0.10 mN, expanded uncertainty may not exceed 0.020 mN and observed bias consumes that same tolerance. The matrix does not authorize a purchase; the next step is a reference-force feasibility calculation only.


## Mass-reference feasibility result — 2026-09-18 13:30 UTC

The [bounded feasibility calculation](../research/hardware/mass-reference-feasibility-2026-09-18.md) found that mass, local-gravity, 1 degree alignment and buoyancy terms can conditionally fit below the 0.020 mN ceiling: the stated prospective scenario gives `U95 = 0.000202333 mN` at 0.10 mN. This does not identify a certified 10.197 mg realization, solve signed reversal, include a transfer fixture or DUT, or authorize selection/purchase. The next acquisition gate is one real certificate-backed mass realization and reversible load path under an allocated `U95 = 0.005 mN` reference-plus-transfer budget, with complete Canadian fixture BOM.


## Signed-force evidence-request gate — 2026-09-28

Before any author/supplier contact or pricing, apply `research/hardware/signed-force-evidence-request-matrix-2026-09-28.md`. It freezes raw randomized signed-cycle, blinding, reversal, provenance, covariance and family-specific transfer/current fields under the existing ±0.10 mN limits. Missing evidence is not a design invitation and cannot be replaced by catalog values. No contact or purchase is authorized.


## Public artifact audit result — 2026-09-28

The [bounded public artifact audit](../research/hardware/signed-force-public-artifact-audit-2026-09-28.md) stopped both the DLR AST and Lam voice-coil candidates at the first mandatory evidence-request field after source identity: no versioned exact-apparatus/raw-package identity and integrity hash was publicly verifiable through the inspected official locations. DLR explicitly reports data/materials availability as not applicable; the accessible Lam publisher record exposed no qualifying package. Later acquisition fields remain unscored. This is not evidence that unpublished artifacts do not exist and does not authorize contact or purchase. Next: preregister a privacy-preserving request limited to the exact missing fields; send nothing during preregistration.


## Signed-force author-request protocol — 2026-09-29

The [frozen request protocol](../research/hardware/signed-force-author-request-preregistration-2026-09-29.md) limits any later author contact to existing artifact-identity fields for the DLR AST and Lam voice-coil publications. It does not authorize a message, account, attachment use, hardware choice or purchase. Consent, reuse rights, credit, redaction, attachment quarantine and stopping rules must be satisfied before any received material enters the public evidence track. Both candidates remain incomplete.


## 2026-09-29 — author-route rights gate

The documentary artifact-request track now has one verified public professional route role per target publication. The DLR article is CC BY 4.0 with third-party exclusions, but unpublished artifacts remain outside that automatic grant. The Lam record exposes no public package licence, so explicit written permission is mandatory before inspection or redistribution of any nonpublic material. No contact, account, purchase or hardware action occurred. The acquisition gate remains closed.


## 2026-09-29 — route-specific request drafts (not sent)

The [two route-specific drafts and pre-send table](../research/hardware/signed-force-route-specific-request-drafts-2026-09-29.md) implement the frozen eight-field request for the DLR and Lam publication records. Unrechecked live-record, public-package, external-correction, prior-contact and explicit-authorization gates default to `SEND BLOCKED`. No outreach, account, contact detail, attachment, hardware choice, purchase or measurement occurred; the acquisition gate remains closed.


## 2026-09-29 — signed-force request dry audit

A field-for-field dry audit found both frozen publication-family drafts complete and redacted against the eight-field request protocol. This does not authorize contact or advance either candidate toward acquisition. Live target, newly public package, current route/current rights, complete prior-contact history and explicit authorization remain unresolved, so the request track stays `SEND BLOCKED`. No hardware was selected, purchased, built, calibrated or measured.


## 2026-09-29 — signed-force live pre-send recheck

The [one-pass live recheck](../research/hardware/signed-force-live-gate-recheck-2026-09-29.md) retained `SEND BLOCKED` for both publication families. DLR still exposes no qualifying package and reports data/materials as not applicable. The Lam publisher record still identifies the exact article, but no qualifying package was exposed and the previously used institutional endpoint was inaccessible. Complete off-repository prior-contact history remains unestablished. No contact, hardware choice, purchase, build, calibration or measurement occurred.
