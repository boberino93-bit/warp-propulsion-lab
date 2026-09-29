# Preregistered signed-force artifact request protocol — 2026-09-29

Status: **FROZEN WHEN MERGED; no message sent and no person contacted.**

## Purpose and boundary

This protocol defines the minimum documentary request needed to resolve the first missing field found in the public-artifact audit for:

1. Neumann, Simon, and Schmidt, DLR AST, https://doi.org/10.1140/epjti/s40485-021-00074-7.
2. Lam et al., voice-coil calibrator, https://doi.org/10.1016/j.measurement.2018.09.029.

It does not request unpublished scientific conclusions, privileged information, personal data, purchasing advice, endorsement or a new experiment. It does not change either candidate’s current `INCOMPLETE — REQUEST EXACT FIELD: artifact identity` status.

## Preconditions before any future contact

A later contact step may occur only after a separate bounded session:

- verifies a public institutional or publisher-designated professional contact route;
- confirms that contact is within the project’s authorized scope;
- records the exact recipient role without exposing private contact data;
- rechecks the live publication record for a newly public artifact;
- preserves this frozen request without adding broader questions;
- receives no conflicting external contribution or rights correction.

This preregistration itself authorizes no email, message, form submission, upload or account creation.

## Exact request fields

For each publication, ask only whether the authors can identify an existing package corresponding to the published apparatus and calibration. The requested fields are:

1. exact apparatus revision or build identifier used for the reported measurements;
2. drawing and BOM revision identifiers, if such records exist;
3. analysis/acquisition software version, tag or commit identifier, if software was used;
4. raw signed calibration-cycle data-package identifier, if such a package exists;
5. cryptographic digest for that package, preferably SHA-256, or permission for the project to calculate and report one after lawful receipt;
6. public repository/DOI/landing-page URL, if already public;
7. applicable license or a plain statement that redistribution is not authorized;
8. if no package exists or it cannot be shared, permission to record that concise status.

Do not ask the authors to create missing artifacts, perform new analysis, certify procurement fitness, disclose proprietary design details, or send restricted/export-controlled/safety-sensitive material.

## Frozen neutral wording

> We are conducting a documentary reproducibility audit of the calibration evidence reported in [citation/DOI]. The public record did not let us identify the exact apparatus revision or a versioned raw calibration package. Could you please point us to any existing public package or provide only its identifier, revision/version, integrity hash (if available), location and reuse terms? If no such package exists or it cannot be shared, a brief statement to that effect is sufficient. We are not requesting new analysis, unpublished conclusions, proprietary material, personal data or endorsement.

The future message must identify the independent project accurately and must not imply university, DLR, publisher or author affiliation.

## Consent, rights and provenance rules

- Use only a public professional route; do not locate or publish private addresses, phone numbers or personal accounts.
- Treat a response as correspondence, not peer review or endorsement.
- Quote no more than necessary and obtain permission before publishing a nonpublic response verbatim.
- Record a paraphrased status when permission to quote is absent.
- Do not upload, mirror, transform or redistribute any received file until its ownership, license and third-party exclusions are explicit.
- Preserve the sender-supplied filename, revision, timestamp and digest. Calculate a separate SHA-256 without changing the original bytes.
- Quarantine unexpected attachments from experimental code and do not execute macros, binaries, scripts or links requiring credentials.
- Remove personal contact details from public logs.
- Credit authors and upstream institutions exactly as requested; existing third-party rights remain unchanged.
- Silence, refusal, unavailable contact or non-shareable material is a retained null/blocker, not evidence against the publication.

## Contact and stopping limits

If later authorized, send at most one initial request per publication family and one concise follow-up no sooner than 14 calendar days later. Do not contact coauthors serially after a refusal, use social media escalation, or seek unpublished material through third parties.

Stop the request track for a family on any:

- explicit refusal or request for no further contact;
- statement that no qualifying package exists;
- rights/safety restriction preventing lawful inspection;
- ambiguous identity that cannot be resolved without broader disclosure;
- credible correction showing this request targets the wrong apparatus/publication;
- receipt of a complete identifiable package, pending the separate rights/integrity audit.

No response after the one permitted follow-up is recorded as `NO RESPONSE — ARTIFACT IDENTITY UNRESOLVED`.

## Decision outputs

Only these outcomes are allowed:

- `PUBLIC PACKAGE IDENTIFIED — AUDIT NEXT`;
- `NONPUBLIC PACKAGE OFFERED — RIGHTS/INTEGRITY REVIEW REQUIRED`;
- `NO PACKAGE / NOT SHAREABLE — RETAIN INCOMPLETE`;
- `NO RESPONSE — ARTIFACT IDENTITY UNRESOLVED`;
- `WRONG TARGET / CORRECTION — RECONCILE BEFORE CONTACT`.

None is an acquisition pass, calibration validation, physical result or propulsion result.

## NEXT ONE TEST

Audit one public institutional or publisher-designated professional contact route and current rights statement for each publication without sending a message, opening an account or collecting private contact data.
