# CS-14 — Customer Feedback Form

**Status:** PLANNED  
**Owner:** Service manager  
**Required before:** Round closure  
**Last revision:** 2026-07-14 (added submission date, channel, anonymity option, link to CS-05 for renewal preference, updated QMS codes)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md`. `P-PSEA-17` (vigente) = Quejas del PEA. `P-PSEA-18` (vigente) = Apelaciones del PEA. `F-PSEA-14` (vigente post-renumeración) = Registro de queja / NC / CAPA. `F-PSEA-15` (vigente) = Registro de apelaciones.

## Purpose

Measure service experience and demand.

## Form metadata

| Field | Value |
|---|---|
| Submission channel | [FILL — e.g., URL of the form, email address, app link] |
| Available languages | [FILL — same as CS-02] |
| Anonymity option | Yes — submission can be anonymous (no link to participant code) |
| Submission window | [FILL — open from final report delivery to N days after, then closed] |
| Link to renewal EoI (CS-05) | [FILL — Q11 below feeds CS-05] |

## Important

Technical feedback that indicates a complaint, appeal or nonconformity must be routed into the existing PSEA procedure (`P-PSEA-17`, `P-PSEA-18`, `F-PSEA-14`, `F-PSEA-15`) rather than managed only as a survey comment.

## Minimum questions

| # | Question | Scale / type | Required |
|---|---|---|---|
| 0 | Submission date (auto-captured) | Date | Auto |
| 0a | Submission channel | Portal / email / paper | Auto |
| 1 | Clarity of offer and quotation | 1–5 | Yes |
| 2 | Ease of registration and payment | 1–5 | Yes |
| 3 | Clarity and timeliness of communications | 1–5 | Yes |
| 4 | Facility/logistics experience | 1–5 | Yes |
| 5 | Usefulness and timeliness of report delivery | 1–5 | Yes |
| 6 | Perceived value for price | 1–5 | Yes |
| 7 | Gas/package interest for the next round (cross-link with CS-05 to avoid double-asking) | Multi-select + comments | Yes |
| 8 | Preferred period and procurement lead time | Text | Optional |
| 9 | Likelihood of returning or recommending | 0–10 (NPS) | Yes |
| 10 | Complaint/improvement comments | Free text | Optional |
| 11 | Permission to be contacted for renewal (links to CS-05) | Checkbox | Yes |
| 12 | Anonymity preference | "Submit anonymously" checkbox | Optional |

## Routing rules

- If Q10 mentions a specific complaint, appeal or nonconformity:
  - Route to `P-PSEA-17` (quejas) / `P-PSEA-18` (apelaciones) within 1 business day.
  - Do not close the feedback record until the complaint is logged separately.
  - Record the linkage in `F-PSEA-14` (queja / NC / CAPA) or `F-PSEA-15` (apelaciones).
- If Q10 mentions a commercial issue (billing, terms, cancellation):
  - Route to commercial lead and open CS-12 if financial impact.
- If Q10 is general improvement:
  - Log in improvement register for management review.
- If Q11 = yes, push the gas/package preferences (Q7) and period (Q8) into a new CS-05 expression-of-interest row, linked to the participant's existing CS-10 record.
- If Q12 = "Submit anonymously", the submission is stored without participant code; only aggregate views are possible.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added submission date/channel, anonymity option, CS-05 cross-link, updated QMS codes. |
