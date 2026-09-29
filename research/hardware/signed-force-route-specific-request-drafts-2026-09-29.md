# Route-specific signed-force artifact request drafts and pre-send table — 2026-09-29

Status: **FROZEN DRAFTS ONLY — NOT SENT; no contact details included.**

## Boundary

These drafts instantiate the merged request protocol for the two exact publications already audited. They request only existing artifact-identity fields. They do not ask for new analysis, unpublished conclusions, proprietary or safety-sensitive material, purchasing advice, endorsement, or personal data. They do not authorize an email, form submission, account, attachment retrieval, hardware selection, purchase, calibration, or experiment.

Each candidate remains `INCOMPLETE — REQUEST EXACT FIELD: artifact identity`. A later sending decision requires a new bounded session and every pre-send gate below to pass.

## Draft A — DLR AST record

**Permitted route role:** publisher-designated corresponding-author route or the official DLR institutional publication route. No address is retained here.

**Subject draft:** Documentary reproducibility request for DOI 10.1140/epjti/s40485-021-00074-7

**Body draft:**

> We are conducting an independent documentary reproducibility audit of the calibration evidence reported in Neumann, Simon and Schmidt (2021), DOI 10.1140/epjti/s40485-021-00074-7. The public record did not let us identify the exact apparatus revision or a versioned raw signed-calibration package.
>
> If an existing package corresponds to the reported apparatus and measurements, could you please point us to its public landing page or provide only:
>
> 1. the exact apparatus/build revision;
> 2. drawing and BOM revision identifiers, if they exist;
> 3. acquisition/analysis software version, tag or commit, if software was used;
> 4. the raw signed calibration-cycle package identifier, if it exists;
> 5. its SHA-256 digest, if available, or permission for us to calculate and report one after lawful receipt;
> 6. the public repository, DOI or landing-page URL, if public;
> 7. the applicable licence/reuse terms, or a statement that redistribution is not authorized; and
> 8. if no qualifying package exists or it cannot be shared, permission to record that concise status.
>
> We are not requesting new analysis, unpublished conclusions, proprietary or restricted material, personal data, procurement advice or endorsement. The article's CC BY 4.0 licence is not assumed to cover any unpublished apparatus, software, raw data or correspondence. Unexpected attachments will remain quarantined and will not be executed or redistributed pending a separate rights and integrity review.
>
> A brief reply or pointer is sufficient. This independent project is not affiliated with DLR, the publisher, a university or the authors.

## Draft B — Lam voice-coil record

**Permitted route role:** institution-designated corresponding-author route through the official Heriot-Watt Research Portal/institutional channel. No address is retained here.

**Subject draft:** Documentary reproducibility request for DOI 10.1016/j.measurement.2018.09.029

**Body draft:**

> We are conducting an independent documentary reproducibility audit of the calibration evidence reported in Lam et al. (2019), DOI 10.1016/j.measurement.2018.09.029. The public record did not let us identify the exact apparatus revision or a versioned raw signed-calibration package.
>
> If an existing package corresponds to the reported apparatus and measurements, could you please point us to its public landing page or provide only:
>
> 1. the exact coil, magnet, fixture and current-source/build revisions;
> 2. drawing and BOM revision identifiers, if they exist;
> 3. acquisition/analysis software version, tag or commit, if software was used;
> 4. the raw signed calibration-cycle package identifier, if it exists;
> 5. its SHA-256 digest, if available, or permission for us to calculate and report one after lawful receipt;
> 6. the public repository, DOI or landing-page URL, if public;
> 7. the applicable licence/reuse terms, or a statement that redistribution is not authorized; and
> 8. if no qualifying package exists or it cannot be shared, permission to record that concise status.
>
> We are not requesting new analysis, unpublished conclusions, proprietary or restricted material, personal data, procurement advice or endorsement. No public artefact-package licence was identified, so no inspection, quotation or redistribution of nonpublic material will be assumed permitted without explicit written permission. Unexpected attachments will remain quarantined and will not be executed or redistributed pending a separate rights and integrity review.
>
> A brief reply or pointer is sufficient. This independent project is not affiliated with Heriot-Watt University, the publisher, a university or the authors.

## Field-for-field conformance

| Frozen protocol field | DLR draft | Lam draft | Gate |
| --- | --- | --- | --- |
| Exact apparatus/build revision | requested | requested, with coil/magnet/fixture/source specificity | pass |
| Drawing/BOM revisions | requested if existing | requested if existing | pass |
| Software version/tag/commit | requested if used | requested if used | pass |
| Raw signed-cycle package identity | requested if existing | requested if existing | pass |
| Digest or permission to calculate | requested | requested | pass |
| Public repository/DOI/landing page | requested | requested | pass |
| Licence or non-redistribution statement | requested; article/artifact boundary explicit | requested; written-permission boundary explicit | pass |
| Concise no-package/not-shareable status | requested | requested | pass |
| No new work/proprietary data/personal data/endorsement | explicit | explicit | pass |
| Accurate independent-project identity | explicit | explicit | pass |

## Pre-send decision table

Every row must be `PASS` in a future bounded session before one initial request may be sent. This document does not perform or authorize that session.

| Gate | Required evidence immediately before sending | Current result |
| --- | --- | --- |
| Live target identity | DOI, title and apparatus still match the frozen request | NOT RECHECKED — SEND BLOCKED |
| Newly public package | fresh official-record check finds no complete qualifying package | NOT RECHECKED — SEND BLOCKED |
| Route role | official route remains publisher/institution-designated; no private detail retained | VERIFIED 2026-09-29, MUST RECHECK |
| Rights statement | current article/portal and artifact-rights boundaries recorded | VERIFIED 2026-09-29, MUST RECHECK |
| External correction | no credible correction, ownership dispute, safety issue or wrong-target notice | NOT RECHECKED — SEND BLOCKED |
| Scope fidelity | final text requests only the eight frozen identity/rights fields | PASS FOR DRAFT |
| Privacy | no private address, phone number, personal account or unnecessary personal data in draft/log | PASS FOR DRAFT |
| Affiliation | no university, institutional, author or publisher affiliation implied | PASS FOR DRAFT |
| Attachments and links | quarantine/no-execution/no-credential rule retained | PASS FOR DRAFT |
| Contact count | no earlier initial request or refusal for the publication family | NOT ESTABLISHED — SEND BLOCKED |
| Authorization | a separate bounded session explicitly authorizes exactly one initial request | ABSENT — SEND BLOCKED |

Decision rule: if any row is not `PASS`, send nothing. Refusal, wrong target, safety/rights restriction or prior no-contact request stops the family. Silence permits at most one follow-up no sooner than 14 calendar days after a lawfully sent initial request.

## Allowed later outcomes

Only the merged protocol outcomes may be recorded: `PUBLIC PACKAGE IDENTIFIED — AUDIT NEXT`, `NONPUBLIC PACKAGE OFFERED — RIGHTS/INTEGRITY REVIEW REQUIRED`, `NO PACKAGE / NOT SHAREABLE — RETAIN INCOMPLETE`, `NO RESPONSE — ARTIFACT IDENTITY UNRESOLVED`, or `WRONG TARGET / CORRECTION — RECONCILE BEFORE CONTACT`.

## Evidence status

This bounded advance freezes draft wording and a decision gate. It does not establish that either artifact exists, that contact is authorized, that a response will occur, or that either force-reference candidate meets the signed calibration, uncertainty, controls, construction-rights, BOM or acquisition gates.

No message was sent. No contact detail, account, attachment or nonpublic artifact was collected. No hardware was selected, purchased, built, calibrated or measured. No thrust or propulsion result exists.

## NEXT ONE TEST

Run a dry, no-send completeness and redaction audit on both drafts against the frozen eight-field protocol and the pre-send table; retain any mismatch and send nothing.