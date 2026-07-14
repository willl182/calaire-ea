# CS-15 — Renewal / Follow-up Message and Lead Record

**Status:** PLANNED  
**Owner:** Commercial lead  
**Required before:** Post-round  
**Last revision:** 2026-07-14 (added SLA, loyalty pricing link, no-response handling, CS-05 sync, marketing consent check)

## Purpose

Convert completed participation into repeat demand.

## Timing SLA

The follow-up is sent within an approved post-round interval:

| Milestone | SLA |
|---|---|
| Follow-up sent after final report | [FILL — typically 2–4 weeks after final report delivery per blueprint 18] |
| No-response follow-up | [FILL — e.g., 30 days after first follow-up, send a reminder] |
| Lead marked "stale" if no response | [FILL — e.g., 90 days after first follow-up] |
| Re-attempt interval for next round | [FILL — e.g., 6 months] |

Stale leads are flagged in CS-10 with the "Stale-EoI flag" (same as CS-05) and excluded from active pipeline views.

## Message content

| Element | Required | Notes |
|---|---|---|
| Thank the participant | Yes | |
| Link to feedback form (CS-14) | Yes | |
| Identify next expected programme period | Yes | Reference CS-03 |
| Record gases of future interest | Yes | Log in CS-10 pipeline |
| Offer expression-of-interest option | Yes | Link to CS-05 |
| **Mention any loyalty pricing or multi-round discount** (if CS-04 / CS-01 has approved such scheme) | Conditional | If no loyalty scheme exists, omit this row entirely |
| Do not disclose or market based on confidential performance | Yes | Mandatory |

**Loyalty pricing note:** if CS-04 does not currently include a multi-round discount or loyalty scheme, the message must NOT invent one. Either CS-04 must be updated to include the scheme (with management approval), or the message omits the row. Inventing a discount in CS-15 breaks CS-06 quote integrity.

### Template

```text
Subject: CALAIRE-EA — Thank you and next programme — Round [ID]

Dear [CONTACT],

Thank you for participating in CALAIRE-EA Round [ID].

We would appreciate your feedback to help us improve the service:
[LINK to CS-14 feedback form]

Next programme
- Expected period: [FILL]
- Gases offered: [FILL]

No se ofrece descuento automático por renovación durante la etapa de propuesta.
Una futura política de fidelización requiere revisión de CS-01 y aprobación de
CS-04 antes de comunicarse.

If you are interested in the next round, please let us know which gases you would like to include:
[LINK to CS-05 expression-of-interest form]

Your performance results remain confidential and will not be used for marketing purposes. You may revoke your commercial contact consent at any time by replying to this email.

Best regards,
[COMMERCIAL LEAD]
```

## No-response handling

| Scenario | Action |
|---|---|
| No response within SLA reminder window | Send reminder with same content + "If we do not hear from you by [DATE], we will mark your renewal interest as inactive. You can re-activate at any time." |
| No response after reminder | Mark lead as "stale" in CS-10 (Stale-EoI flag = Yes) |
| Customer replies after stale flag | Re-activate lead; reset the stale timer |

## Sync with CS-05 (expression of interest)

When the customer responds to the follow-up with renewal interest:

- Do **not** create a new CS-05 submission from scratch. Instead, **update the existing CS-10 record** with:
  - New pipeline entry for the next round (status = Interest for the new round).
  - Gases of interest from the response.
  - Preferred period.
  - Procurement lead time if stated.
  - Marketing consent flag (separately from service consent per Ley 1581/2012).
- The CS-05 form remains the formal EoI channel for new prospects; for renewals, the CS-10 update is sufficient and avoids re-asking for organization/contact data.

If the customer explicitly submits a new CS-05 (e.g., via the form rather than replying to the follow-up), merge the data into the existing CS-10 record; do not duplicate.

## Lead record

Update CS-10 tracker with:

- New pipeline entry for next round (status = Interest).
- Gases of interest from response.
- Preferred period.
- Procurement lead time if stated.
- Marketing consent flag.
- Stale-EoI date (90 days after follow-up if no response).

## Controls

- No reference to individual scores, z-scores, or relative performance.
- No claim that accreditation exists if it does not.
- Consent checked before adding to marketing list (separately from service consent).
- If CS-14 was submitted anonymously, the renewal follow-up cannot reference the previous responses; the message is generic.
- Loyalty pricing must come from CS-04, not invented in CS-15.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added timing SLA, loyalty pricing conditional rule, no-response handling, CS-05 sync, marketing consent check. |
