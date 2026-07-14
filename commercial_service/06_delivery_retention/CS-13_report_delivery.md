# CS-13 — Report Delivery and Participation Message

**Status:** PLANNED  
**Owner:** Round coordinator  
**Required before:** Report issue  
**Last revision:** 2026-07-14 (added standard report-use reminder, CS-12 link for draft corrections, no-reception handling, retention policy)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md`. El informe final está en `F-PSEA-13` (código vigente tras renumeración del 2026-06-14; antes `F-PSEA-04`).

## Purpose

Complete customer delivery consistently. The QMS already controls the technical report through `P-PSEA-09` and `F-PSEA-13`. The commercial layer needs only a controlled delivery message and, if not already covered, a participation statement.

## Delivery message

### Required fields

| Field | Value |
|---|---|
| Participant and round code | [FILL] |
| Attached report identifier/version | [FILL] |
| Confidentiality notice | [FILL — standard text: "This report is confidential and intended solely for the named participant. Distribution to third parties requires written authorization from CALAIRE-EA."] |
| Draft or final status | [FILL] |
| Review/appeal deadline (if draft) | [FILL — typically 14 calendar days from draft issue] |
| Secure access or delivery instructions | [FILL] |
| Report-use reminder | **Standard text — DO NOT modify without CS-01 approval. Ver bloque abajo.** |
| Commercial and technical contacts | [FILL] |

### Standard report-use reminder (use unchanged in both draft and final)

> "The participant may state that it participated in the CALAIRE-EA Round [ID] for the gases [LIST]. It may not state or imply that CALAIRE-EA is accredited, that the round is accredited, or that the participant is technically competent solely by virtue of participation. Detailed performance evaluation is provided in the separate technical report. Distribution of this report or its contents to third parties requires written authorization from CALAIRE-EA."

This text matches the wording approved in CS-01 section 9 ("Report use"). Any modification must be approved in both CS-01 and CS-13 in the same revision to avoid divergence.

### Template — draft report

```text
Subject: CALAIRE-EA — Round [ID] — Participant [CODE] — Draft Report for Review

Dear [CONTACT],

Please find attached the draft report for your review.

Report ID: [ID]
Status: DRAFT

If you have comments or identify errors, please submit them by [DEADLINE] per the appeals procedure (P-PSEA-18).

This draft is confidential and intended solely for the named participant.

REPORT-USE REMINDER (standard):
The participant may state that it participated in the CALAIRE-EA Round [ID] for the gases [LIST]. It may not state or imply that CALAIRE-EA is accredited, that the round is accredited, or that the participant is technically competent solely by virtue of participation. Detailed performance evaluation is provided in the separate technical report. Distribution of this report or its contents to third parties requires written authorization from CALAIRE-EA.

Technical questions: [TECH CONTACT]
Commercial questions: [COMMERCIAL CONTACT]

If your review identifies errors or required corrections that result in a change of scope, dates, or fees, please notify the commercial contact; a CS-12 change record will be opened.
```

### Template — final report

```text
Subject: CALAIRE-EA — Round [ID] — Participant [CODE] — Final Report

Dear [CONTACT],

Please find attached the final report for Round [ID].

Report ID: [ID]
Status: FINAL

REPORT-USE REMINDER (standard):
The participant may state that it participated in the CALAIRE-EA Round [ID] for the gases [LIST]. It may not state or imply that CALAIRE-EA is accredited, that the round is accredited, or that the participant is technically competent solely by virtue of participation. Detailed performance evaluation is provided in the separate technical report. Distribution of this report or its contents to third parties requires written authorization from CALAIRE-EA.

A participation statement is attached separately if required.

Technical questions: [TECH CONTACT]
Commercial questions: [COMMERCIAL CONTACT]
```

## No-reception handling

If the report email bounces or no acknowledgement is received within 5 business days:

1. Round coordinator verifies email address against CS-07 and CS-11 records.
2. Re-send via alternative channel recorded in CS-11 (registered email, portal, or postal mail for international clients).
3. If still no acknowledgement within 5 additional business days, escalate to commercial lead.
4. Document the incident in CS-12 (change/cancellation record) with classification "no-reception".
5. Do not mark the report as "delivered" in CS-10 until a confirmed receipt (read-receipt, signed delivery, or explicit acknowledgement) is on file.

## Retention

Final reports and the corresponding delivery record are retained in the controlled QMS storage for a minimum of 5 years per ISO/IEC 17043 record-retention requirements. Commercial delivery records (date, contact, channel) are retained in CS-10 for the same period.

## Link to CS-12 (change/cancellation)

If the draft review identifies errors that require commercial action (scope change, fee change, additional round days), the commercial contact must:

1. Open a CS-12 record with trigger "scope/date/fee change".
2. Update CS-10 (commercial status) to reflect the in-progress change.
3. Issue a revised quote (CS-06 revision) if fees change.
4. Close the CS-12 record once the technical report is reissued or the change is resolved.

The template note "If your review identifies errors or required corrections that result in a change of scope, dates, or fees, please notify the commercial contact; a CS-12 change record will be opened." appears in the draft template for this reason.

## Participation statement

If not already covered by the QMS report, a separate participation statement may be issued.

### Permitted content

- Organization name
- Round ID and date
- Analyzer identifier
- Selected gases

### Prohibited content

- [ ] Must not claim accreditation before accreditation exists.
- [ ] Must not state or imply technical competence.
- [ ] Must not replace the detailed performance report.
- [ ] Must not publish confidential scores.
- [ ] Must not use a1–a7 or an overall grade.

### Template

```text
CALAIRE-EA — PARTICIPATION STATEMENT

Organization: [NAME]
Round: [ID]
Date: [DATE]
Analyzer: [ID]
Gases: [LIST]

This statement confirms participation in the above round.
It does not constitute accreditation or a statement of technical competence.
Detailed performance evaluation is provided in the separate technical report.
```

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Standardized report-use reminder; added CS-12 link, no-reception handling, retention period. |
