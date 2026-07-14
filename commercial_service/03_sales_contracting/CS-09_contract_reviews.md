# CS-09 — Contract / PO Review Checklist

**Status:** PLANNED  
**Owner:** Commercial + scheme  
**Required before:** Confirmation  
**Last revision:** 2026-07-14 (added residual capacity check, granular disclosure consent branches, signature requirement per check)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md`. Las referencias QMS usan los códigos vigentes post-renumeración 2026-06-14.

## Purpose

Stop CALAIRE-EA from accepting an order it cannot deliver or whose purchase-order language conflicts with the PT conditions.

## Checks

Each check **must be signed** (initial) by the reviewer; "—" or blank is not acceptable. A check can be Pass, Fail, or N/A (with justification).

| # | Check | Evidence required | Pass / Fail / N/A | Initial |
|---|---|---|---|---|
| 1 | Quote is valid and matches registration (gas package, analyzer count, customer) | Quote number, issue date, expiry, acceptance deadline | | |
| 2 | Quote is not already accepted by another party (no double-booking) | CS-06 revision history / CS-10 quote view | | |
| 3 | Selected gases are offered in the round | Round notice (CS-03) | | |
| 4 | Analyzer capacity remains available by gas and operating configuration | CS-10 tracker capacity view | | |
| 5 | Order stays within capacity limits (4 individual-gas positions or 3-participant/6-analyzer simultaneous CO/SO₂ limit) | CS-10 tracker | | |
| 6 | **Residual capacity after this order is ≥ 0** (this is the acceptance boundary: if consuming the last slot, mark as "last slot" and require commercial lead authorization) | CS-10 capacity view | | |
| 7 | Equipment appears compatible based on submitted data (model, calibration dates) | `F-PSEA-04` technical/equipment annex (post-renumeración) and `calaire-app` | | |
| 8 | Price, currency, taxes and payment schedule match | CS-06 quote vs. registration vs. PO | | |
| 9 | PO does not silently override cancellation, confidentiality or report rules (clause-by-clause diff vs. CS-08) | PO text reviewed against CS-08 | | |
| 10 | PO does not silently override the assigned-value rule, evaluation indicators, or no-a1-a7 grading (CS-08 clauses 12 and 13) | PO text reviewed | | |
| 11 | Customer-specific report or language requirement is feasible | Operations confirmation | | |
| 12 | Conflict-of-interest or impartiality risk is referred to the existing QMS control | Impartiality register / management review | | |
| 13 | **Disclosure consent is recorded AND scoped correctly** (regulatory disclosure, marketing disclosure, cross-border disclosure — three separate consents) | Registration form (CS-07) | | |
| 14 | **Data protection consent is recorded** (Ley 1581/2012 text accepted) | Registration form (CS-07) | | |
| 15 | Required payment / PO evidence is received | Finance confirmation | | |
| 16 | If status = Wait-listed, wait-list priority criteria documented and applied (per CS-01 Section 7) | CS-10 wait-list view | | |
| 17 | Acceptance, wait-list or rejection decision is authorized (commercial lead for standard; management for institutional) | CS-01 approval authority | | |

**Disclosure consent branches** (granularity for check 13):

- **Regulatory disclosure:** consent to disclose results to regulatory authorities when required by law (typically mandatory, not optional).
- **Marketing disclosure:** consent to use anonymized participation data in marketing materials (optional, revocable).
- **Cross-border disclosure:** consent to transfer report data outside Colombia for delivery (required for international clients; explicit per Ley 1581/2012).

A single "I agree to disclosure" is **insufficient** — each branch must be checked separately in CS-07 and verified in this checklist.

## Review record

| Field | Value |
|---|---|
| Round ID | [FILL] |
| Customer | [FILL] |
| Registration date | [FILL] |
| Acceptance timestamp | [FILL — from CS-07] |
| Quote number | [FILL] |
| Quote revision | [FILL] |
| Reviewer | [FILL NAME] |
| Review date | [FILL] |
| Decision | [Accepted / Wait-listed / Rejected] |
| Decision authorized by | [FILL NAME] |
| Authorization date | [FILL] |
| Notes | [FILL] |

## Controls

- Rejected orders are recorded with reason (mandatory; "no reason" is not acceptable).
- Wait-listed orders are tracked in CS-10 with priority date and criteria applied.
- Confirmed orders trigger CS-11 confirmation and QMS handoff.
- All 17 checks must be initialed; missing initials blocks the decision.
- If any check fails, the registration is rejected or sent back to the customer; the reason is documented and shared with the customer.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added residual capacity check, granular disclosure consent branches, data protection check, signature requirement per check, doubled PO text review (assigned value + no-a1-a7). |
