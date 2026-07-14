# CS-11 — Confirmation and Onboarding Pack

**Status:** PLANNED  
**Owner:** Round coordinator  
**Required before:** Technical preparation  
**Last revision:** 2026-07-14 (added wait-list and rejection templates, confirmation expiration rule, additional participants field, fix to QMS code references)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md`. Las referencias QMS usan los códigos vigentes post-renumeración 2026-06-14.

## Purpose

Confirm the purchase and hand off to QMS. This artifact also covers the **wait-list** and **rejection** messages sent to customers whose registration cannot be confirmed.

## Confirmation message

### Required fields

| Field | Value |
|---|---|
| Customer legal name | [FILL] |
| Round ID | [FILL] |
| Participant code | [FILL — assigned per QMS] |
| Selected gas or gases | [FILL] |
| Confirmed analyzer count | [FILL] |
| Dates and location | [FILL] |
| Payment / PO status | [FILL] |
| Primary technical contact | Wilson Salas — `calaire_med@unal.edu.co` |
| Primary administrative contact | David Pulgarin — `calaire_med@unal.edu.co` |
| Additional participants from same organization (if any) | [FILL — NAMES, EMAILS] |
| Next deadlines | [FILL — e.g., equipment data submission, readiness checklist] |
| Attached or linked QMS participant instructions | [FILL] |
| Change / cancellation contact | David Pulgarin — `calaire_med@unal.edu.co` |
| **Acknowledgement deadline** | 5 días hábiles desde el envío. Si no hay respuesta, se realiza y registra seguimiento; no se libera un cupo confirmado por pago u orden aceptada sin aplicar el proceso formal de cancelación. |

### Template

```text
Subject: CALAIRE-EA — Round [ID] — Participant [CODE] — Confirmation

Dear [CONTACT],

Your registration for CALAIRE-EA Round [ID] is confirmed.

Participant code: [CODE]
Selected gases: [GASES]
Confirmed analyzers: [COUNT]
Additional participants from your organization: [LIST or "none"]
Dates: [DATES]
Location: [LOCATION]

Payment / PO status: [STATUS]

This confirmation is valid until [DATE]. If we do not receive acknowledgement by that date, the slot will be released and your registration will be moved to the wait-list (priority preserved per CS-01 Section 7).

Next steps and deadlines:
- [FILL]

Attached you will find the participant instructions and schedule.

Technical questions: [TECH CONTACT]
Administrative questions: [ADMIN CONTACT]
Changes / cancellation: [CHANGE CONTACT]

Best regards,
[ROUND COORDINATOR]
```

## Wait-list message

When a customer is wait-listed (CS-09 check 4 or 6 fails because capacity is exhausted), the round coordinator sends this message:

### Template

```text
Subject: CALAIRE-EA — Round [ID] — [ORGANIZATION] — Wait-listed

Dear [CONTACT],

Thank you for your interest in CALAIRE-EA Round [ID].

Unfortunately, the round has reached its capacity for the configuration you selected. Your registration has been placed on the wait-list.

Wait-list priority: [PRIORITY RANK]
Wait-list date: [DATE]
Selected gases: [GASES]
Round dates: [DATES]

We will contact you within 5 business days if a slot becomes available. If a slot does not become available, we will offer one of the following options by the minimum-enrollment decision date [DATE]:
- Transfer your registration to the next scheduled round, OR
- Issue a full refund / credit note (per CS-01 Section 8).

To remain on the wait-list, no action is required from you. To withdraw, please contact [COMMERCIAL CONTACT].

Best regards,
[ROUND COORDINATOR]
```

## Rejection message

When a registration is rejected (CS-09 check fails for a non-capacity reason, e.g., equipment incompatibility, conflicting PO terms, conflict of interest), the round coordinator sends this message:

### Template

```text
Subject: CALAIRE-EA — Round [ID] — [ORGANIZATION] — Registration not accepted

Dear [CONTACT],

Thank you for your interest in CALAIRE-EA Round [ID].

After contract review (CS-09), we are unable to accept your registration for this round. The reason is:

[REASON — e.g., "Equipment calibration certificate expires before round start", "PO clause 7 conflicts with the cancellation terms in CS-08", "Conflict of interest referred to QMS impartiality control"]

If you believe this decision is in error, you may:
- Request a review by the commercial lead within 10 business days, OR
- Resubmit a corrected registration for a later round.

We remain at your service for future rounds.

Best regards,
[ROUND COORDINATOR]
```

## Onboarding pack

Do not create new technical documents. Package the approved existing materials applicable to that participant:

| Document | QMS reference | Purpose |
|---|---|---|
| Detailed participation protocol | DG-PSEA-01 (or approved successor) | Technical execution guide |
| Packaging/transport instructions | I-PSEA-01 | Where applicable |
| calaire-app participant instructions | I-PSEA-02 | Data submission guide |
| Technical/equipment annex | `F-PSEA-04` (post-renumeración 2026-06-14; antiguo `F-PSEA-05A`) | Verify equipment compatibility |
| Participant registration | `F-PSEA-03` (antiguo `F-PSEA-05`) | Identidad y datos administrativos |
| Current schedule | Generated through existing PSEA planning | Round timeline |
| Facility and safety information | [FILL — fixed document, not per round] | Local requirements |
| Official communication channel | [FILL] | Email / portal / group |

## Handoff to QMS

The confirmed participant list is exported to:

- `P-PSEA-04` round planning and `F-PSEA-03` participant registration (antiguo `F-PSEA-05`)
- `F-PSEA-04` technical/equipment annex (antiguo `F-PSEA-05A`) and `calaire-app` for technical data capture
- `P-PSEA-05` communications procedure

**Code mapping note:** ver `00_control/qms_code_equivalence.md`. El QMS renumeró los códigos el 2026-06-14; las referencias de arriba son las vigentes.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
