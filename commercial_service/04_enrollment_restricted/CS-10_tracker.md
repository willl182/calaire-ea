# CS-10 — Enrollment and Revenue Tracker

**Status:** PLANNED — RESTRICTED ACCESS  
**Owner:** Round coordinator  
**Required before:** Confirmation / execution  
**Last revision:** 2026-07-14 (added wait-list criteria, payment deadline column, partial payment substatus, communication system rule, currency/exposure tracking)

## Purpose

Control capacity, order, payment and viability.

## Format

Archivo Excel institucional protegido para el MVP, almacenado en una ubicación
UNAL con control de acceso y copias de respaldo. Participant technical results
must not be stored in it. La migración futura a `calaire-app` solo procede
después de validar el flujo.

**Communication system rule:** the "Communication link/location" column below
must point to `calaire_med@unal.edu.co` or a controlled institutional project
folder. Personal inboxes and ad-hoc folders are not approved.

## Minimum columns

| Column | Description |
|---|---|
| Prospect/customer ID | Unique identifier |
| Organization | Legal name |
| Country | |
| Preferred language | Español |
| Round ID | |
| Selected blocks | CO, SO₂, O₃, NO/NO₂ |
| Analyzer count | |
| Quote number | Links to CS-06 |
| Quote revision | Initial = 0, increments on each revision |
| Quote value | Original value, before revisions |
| Current committed value | After any revision or change |
| Quote currency | COP |
| Quote expiry | |
| **Quote acceptance deadline** | Primera fecha entre vencimiento de 30 días, cierre de inscripción, 15 días antes de la ronda o agotamiento de capacidad |
| **Payment / PO deadline** | 15 días calendario por defecto o plazo obligatorio de la Universidad, sin exceder el cierre de inscripción |
| Registration date | |
| Acceptance timestamp | [FILL — from CS-07] |
| Acceptance channel | Correo institucional con cotización firmada / orden de compra formal aceptada |
| Contract-review status | Pending / Passed / Failed |
| Contract-review date | |
| Contract reviewer | |
| PO/payment/invoice status | Pending / Partial (X%) / Received / Invoiced / Paid / Overdue |
| **Partial payment tracking** | If PO/payment status = Partial, record: amount received, amount outstanding, % paid, due date of next installment |
| Invoice number | When issued |
| Participant code after confirmation | Assigned per QMS |
| Capacity consumed (by block) | Número de analizadores aceptados en CO, SO₂, O₃ y NO/NO₂; derivado de CS-09 |
| Operating configuration | Individual gas / Simultaneous CO/SO₂ |
| **Last available slot flag** | Yes/No — auto-set to Yes when accepting the last slot (requires commercial lead authorization per CS-09 check 6) |
| Commercial status | Interest / Quoted / Registered / Under review / Quote-revision in progress / Accepted pending payment/PO / Confirmed / Wait-listed / Rejected / Withdrawn |
| **Wait-list priority** | Grupo 1: laboratorio acreditado; grupo 2: demás elegibles. Dentro de cada grupo, fecha/hora de solicitud completa y elegible |
| **Wait-list date** | Date customer was added to wait-list |
| Cancellation/refund status | |
| Cancellation date | |
| Refund/credit note reference | If applicable |
| FX exposure | No aplica: cotización y facturación únicamente en COP |
| Owner | Commercial or round coordinator assigned |
| Next action | |
| Communication link/location | Must be one of the approved systems (ver header) |
| Stale-EoI flag | [FILL — auto-set to Yes if EoI older than CS-05 response-expiry threshold] |

## Wait-list priority rules (default, override per CS-01)

When multiple customers compete for the same slot, priority is:

1. Solicitudes completas y elegibles de laboratorios acreditados, en orden de
   fecha y hora de completitud.
2. Demás organizaciones elegibles, también en orden de fecha y hora de
   completitud.
3. La expresión de interés no reserva prioridad.

Tie-breaker documented in the "Notes" column. The criteria must be applied consistently; deviations require commercial lead sign-off and a CS-12 record.

## Partial payment policy

If CS-01 permits partial payments (e.g., 50% on order, 50% pre-round per CS-06 Section 9):

- Status "Partial (X%)" is used until full payment received.
- The customer cannot transition to "Confirmed" until full payment is recorded.
- If the second installment is overdue, escalate per CS-12 (cancellation trigger) after the grace period defined in CS-01.

## Required views

### 1. Pipeline

Filter: status = Interest through Quoted.

Purpose: Forecast demand and manage prospect follow-up. Exclude rows with Stale-EoI flag = Yes.

### 2. Enrollment

Filter: status = Confirmed.

Group by: gas and operating configuration.

Purpose: Track confirmed capacity vs. limits. Show "Last available slot flag" prominently.

### 3. Viability

Filter: status = Confirmed.

Sum: current committed value (in COP-equivalent using the CS-04 Tab 1 FX policy).

Compare to: minimum enrollment threshold from CS-01.

Purpose: Determine if the round is commercially viable. Show by minimum-enrollment decision date.

### 4. Receivables

Filter: PO/payment/invoice status = Invoiced or Paid or Overdue or Partial.

Purpose: Track cash flow and overdue accounts. Highlight accounts overdue per CS-01 grace period.

### 5. Exceptions

Filter: status = Wait-listed / Cancelled / Refunded / Disputed / Rejected.

Purpose: Manage exceptions and capacity reallocation. Show wait-list priority and date.

## Capacity flags

The tracker should automatically flag:

- More than 4 confirmed analyzer positions for an individual gas.
- More than 3 participants or 6 analyzers for simultaneous CO/SO₂.
- A new "Confirmed" status that would leave residual capacity = 0 (triggers "last slot" warning).
- Stale EoI responses (older than CS-05 response-expiry threshold).

## Controls

- Access-controlled: commercial, finance and round coordinator only.
- No technical results or performance scores.
- Handoff to QMS round planning is a controlled export or approved participant list, not manual retyping.
- "Communication link/location" must use only approved systems; ad-hoc personal inboxes are not acceptable.
- All changes to Confirmed status must be traceable to a CS-12 record (for withdrawals) or CS-09 record (for initial confirmation).

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added wait-list criteria, payment deadline, partial payment tracking, last-slot flag, FX exposure column, approved communication systems rule, stale-EoI flag. |
