# CS-05 — Expression-of-Interest Form

**Status:** PLANNED  
**Owner:** Commercial lead  
**Required before:** Marketing release  
**Last revision:** 2026-07-14 (added calibration certificate question, response expiry, preferred language, data protection consent text)

## Purpose

Verify demand before committing dates and costs.

## Important note

This is not registration and creates no reserved place. The form must say so explicitly.

## Form metadata

| Field | Value |
|---|---|
| Available languages | [FILL — same as CS-02 publication languages] |
| Response expiry | [FILL — e.g., 60 days from submission; stale responses purged from CS-10] |
| Storage | [FILL — e.g., commercial CRM, secure form backend] |
| Owner of last review | [FILL NAME] |

## Minimum questions

| # | Question | Response type | Purpose |
|---|---|---|---|
| 1 | Organization name | Text | Identify prospect |
| 2 | Contact name and email | Text | Commercial follow-up |
| 3 | Country / city | Text | Logistics and time zone |
| 4 | Desired gas(es) | Multi-select: CO, SO₂, NO, NO₂, O₃ | Scope validation |
| 5 | Number and type of analyzers (manufacturer, model, year) | Text | Capacity and compatibility planning |
| 6 | Date of last analyzer calibration | Date | Compatibility filter — stale calibrations may need recalibration before round |
| 7 | Calibration certificate valid until | Date | Compatibility filter — must be valid at round start |
| 8 | Will separate CO and SO₂ analyzers be brought? | Yes / No / Unknown | Determines simultaneous-config feasibility |
| 9 | Is simultaneous CO/SO₂ operation feasible for you? | Yes / No / Unknown | Determines use of 3-participant / 6-analyzer config |
| 10 | Preferred period | Date range / quarter | Calendar planning |
| 11 | Procurement method and approximate lead time | Text | Sales cycle estimate |
| 12 | Ability to transport equipment to Medellín | Yes / No / With assistance | Risk flag |
| 13 | Interest at the provisional flat round benchmark (COP 5.928.000 excl. taxes for one to four blocks) | Yes / No / Negotiate | Price sensitivity |
| 14 | Need for quotation in COP, EUR or another currency | Single select | Currency planning |
| 15 | Preferred language for commercial communications | Single select (Spanish / English / other) | Multilingual support |
| 16 | Interest in an institutional / closed round | Yes / No | Separate quoting trigger |
| 17 | Authorization for commercial follow-up (with explicit consent text) | Checkbox (required) | Data protection compliance — ver texto abajo |

## Consent text (question 17, must be visible and not pre-checked)

> "I authorize CALAIRE-EA to contact me regarding this expression of interest and to store the information submitted for the purpose of preparing a quotation. I understand that I may revoke this consent at any time by contacting the commercial lead, and that my data will be handled per the CALAIRE-EA privacy policy and Colombian data protection law (Ley 1581 de 2012, Decreto 1377 de 2013)."

The full privacy policy URL or PDF reference should be linked next to the checkbox.

## Controls

- Form explicitly states: "Submitting this expression of interest does not reserve a place in the round."
- Data handling references existing confidentiality controls (`P-PSEA-19`, código vigente tras renumeración 2026-06-14; ver `00_control/qms_code_equivalence.md`).
- Responses feed into CS-10 tracker as pipeline stage "Interest".
- Responses older than the response-expiry threshold are marked "stale" in CS-10 and excluded from active pipeline views.
- Question 6 and 7 (calibration dates) feed the CS-09 equipment compatibility check.
- Question 15 (preferred language) feeds the CS-06 and CS-08 language selection.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added calibration dates, response expiry, language preference, Ley 1581 consent text. |
