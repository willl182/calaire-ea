# CS-12 — Change, Cancellation and Refund Record

**Status:** PLANNED  
**Owner:** Commercial / finance  
**Required before:** When triggered  
**Last revision:** 2026-07-14 (added fee catalog reference, viability impact, refund timing, original quote revision traceability, financial-decision dual authorization)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md`. `P-PSEA-15` (vigente) = Trabajo no conforme / NC / CAPA. `P-PSEA-16` (vigente) = Divulgación y control de valores sensibles.

## Purpose

Control commercial changes and financial decisions.

## Trigger events

- [ ] Participant changes selected gases.
- [ ] Participant adds/replaces an analyzer.
- [ ] Participant withdraws.
- [ ] CALAIRE-EA postpones or cancels.
- [ ] Minimum enrollment is not achieved.
- [ ] Dates or facility change.
- [ ] Force majeure affects participation.
- [ ] Refund or credit note is requested.
- [ ] Provider identifies a substantive error in the report (triggers CS-13 → CS-12 chain).

## Minimum record

| Field | Value |
|---|---|
| Record ID | [FILL — unique] |
| Date opened | [FILL] |
| Customer | [FILL] |
| Round ID | [FILL] |
| **Original quote reference (family + revision)** | [FILL — e.g., Q-2026-0042 rev 0; required for traceability of superseded terms] |
| **Revised quote reference (if applicable)** | [FILL — e.g., Q-2026-0042 rev 1] |
| Invoice reference | [FILL] |
| Credit note reference (if applicable) | [FILL] |
| **Applicable fee per CS-01 Section 8 fee schedule** | [FILL — e.g., "30% retention per withdrawal ≥ 30 days before round start"] |
| Original commitment | [FILL — gases, analyzers, dates, price] |
| Requested or imposed change | [FILL] |
| Applicable contract clause | [FILL — reference CS-08 clause] |
| Technical/capacity impact | [FILL — effect on round planning; e.g., "releases 1 CO position"] |
| **Impact on round viability** | [FILL — per CS-04 Tab 7: "viability drops below minimum" or "still viable"] |
| Fee, refund or credit calculation | [FILL — line-by-line: original price, fee, refund amount, credit amount, currency, FX rate] |
| **Refund processing time commitment** | [FILL — per CS-01 Section 8: e.g., 30 business days from approval] |
| **Credit note validity** | [FILL — per CS-01 Section 8: e.g., 12 months from issue] |
| Decision | [FILL — approved / rejected / pending] |
| Decision authorized by (commercial) | [FILL NAME, DATE] |
| Decision authorized by (finance or management) | [FILL NAME, DATE] — **dual authorization required for any financial decision** |
| Customer notification date | [FILL] |
| Updated tracker reference | [FILL — CS-10 row updated] |
| Updated quote reference | [FILL — revised quote number if applicable] |
| Updated invoice reference | [FILL — credit note or new invoice] |
| Updated registration reference | [FILL] |
| Closure date | [FILL] |
| Closure authorized by | [FILL NAME, DATE] |

## Controls

- **Financial decisions require dual authorization** (commercial + finance or management). Single-authority changes are not valid.
- Capacity changes are reflected immediately in CS-10 (no batched updates).
- Revisions to quotes follow CS-06 quote-control rules. The original quote family + revision must be cited.
- Refund processing time per CS-01 Section 8 (typically 30 business days from approval); any delay beyond commitment requires customer notification with revised date.
- Credit notes have a validity period per CS-01 Section 8; expired credit notes are not honored without management re-authorization.
- Technical complaints or nonconformities identified during a change are routed to existing PSEA controls (`P-PSEA-15` NC/CAPA, `P-PSEA-16` valores sensibles).
- If a change is triggered by a substantive report error (CS-13), the CS-12 record must reference the CS-13 report identifier and the CS-13 change-correction note.
- Original quote traceability: every CS-12 record must cite the original quote family + revision. This protects against disputes about which terms applied at the time of the original commitment.

## Fee catalog reference

The fee schedule applied in this record is defined in CS-01 Section 8. The summary of typical fees:

| Scenario | Typical fee / refund |
|---|---|
| Participant withdrawal ≥ N days before round start | [FILL — % retention or fixed fee] |
| Participant withdrawal < N days before round start | [FILL — higher % retention] |
| Participant no-show | [FILL — no refund] |
| Provider postponement | [FILL — slot preserved or full refund at customer choice] |
| Provider cancellation (min enrollment not met) | [FILL — full refund or credit note, customer choice] |
| Force majeure | [FILL — prorated refund or credit note, customer choice] |
| Substantive report error (CS-13 trigger) | [FILL — typically full refund of round fee + free re-issue] |

Ver CS-01 Section 8 for the authoritative values and decision rules.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added fee catalog reference, viability impact, refund timing, original quote traceability, explicit dual authorization, CS-13 link. |
