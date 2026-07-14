# CS-07 — Registration / Order Form

**Status:** PLANNED  
**Owner:** Round coordinator  
**Required before:** Order acceptance  
**Last revision:** 2026-07-14 (added timestamp/IP/channel, wait-list priority, revised-quote status, clarified QMS code reference for technical data)

## Purpose

Capture buyer, selected scope and administrative data. Reuses existing QMS/app technical fields rather than duplicating them.

## Reuse rather than duplicate

Use the existing `calaire-app` and the QMS technical fields for equipment and registration data. The current QMS field references (post-renumeración 2026-06-14) are:

- Equipment and instrument data: `F-PSEA-04` (antiguo `F-PSEA-05A`)
- Participant registration: `F-PSEA-03` (antiguo `F-PSEA-05`)

Ver `00_control/qms_code_equivalence.md` para el mapeo completo.

Add a commercial section rather than creating a second technical registration system.

## Commercial / legal fields to add

| Field | Required | Notes |
|---|---|---|
| Customer legal name | Yes | Must match tax records |
| Tax ID | Yes | |
| Billing address | Yes | |
| Billing contact | Yes | |
| Quote / PO number | Yes | Links to CS-06 (must be valid, not expired, and not already accepted by another party) |
| Selected gas package | Yes | CO, SO₂, NO, NO₂, O₃ |
| Analyzer count | Yes | |
| Requested report language | Yes | Derived from CS-05 question 15 |
| Acceptance of terms | Yes | Checkbox / signature |
| Confidentiality / disclosure selection | Yes | Per `P-PSEA-19` (vigente post-renumeración) |
| Participant marketing consent | Yes | Separated from service consent; Ley 1581/2012 compliance text required |
| Authorized contractual contact | Yes | |
| Authorized technical contact | Yes | |
| Special invoicing documents / procurement portal | No | If applicable |
| **Acceptance timestamp** | Yes | ISO 8601 with timezone; auto-captured by portal or noted by commercial lead if paper |
| **Acceptance channel** | Yes | Portal / email / signed PDF / paper; helps dispute resolution |
| **Acceptance IP / origin (if portal)** | Yes (if portal) | For audit; not required for paper or email |
| **Wait-list priority** | Optional (auto-filled) | Filled by CS-10 if status = Wait-listed; based on CS-01 priority criteria |
| Signature / acceptance date | Yes | Customer-side date (may differ from acceptance timestamp if postal) |

## Status logic

```text
Interest → Quoted → Registered → Under review →
Accepted pending payment/PO → Confirmed → Wait-listed / Rejected / Withdrawn
            │
            └──→ Quote-revision in progress (transient)
                  → back to Quoted with revised quote number
```

**Branch:** when a customer accepts a quote that requires revision (e.g., the round capacity changed, the customer wants to add a gas, the price must be re-quoted), the registration transitions to "Quote-revision in progress" before returning to "Quoted" with a new quote number. The original quote family is recorded as "superseded" and a CS-12 record is opened.

Only **"Confirmed"** participants flow into formal round planning.

## Registration checklist

- [ ] Technical fields completed (via `calaire-app` and QMS fields referenced above).
- [ ] Commercial fields completed.
- [ ] Terms accepted.
- [ ] Disclosure consent recorded.
- [ ] Marketing consent recorded separately with explicit Ley 1581 text.
- [ ] Quote number valid and matches selection (and not already accepted by another party).
- [ ] Acceptance timestamp / channel recorded.
- [ ] Contract review (CS-09) initiated.
- [ ] If status = Wait-listed, wait-list priority recorded (CS-10) and customer notified.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added acceptance timestamp/IP/channel, wait-list priority, quote-revision branch, updated QMS code references. |
