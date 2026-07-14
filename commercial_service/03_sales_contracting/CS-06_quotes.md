# CS-06 — Quotation Template

**Status:** PLANNED  
**Owner:** Commercial lead  
**Required before:** Sale  
**Last revision:** 2026-07-14 (added acceptance deadline vs. expiry, payment schedule table, import tax / withholding notes for international, FX policy reference, acceptance method rule)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md`.

## Purpose

Make a controlled commercial offer.

## Minimum sections

### 1. Quote header

| Field | Value |
|---|---|
| Quote number | [FILL — unique, e.g., Q-YYYY-NNNN] |
| Family | [FILL — same family for all revisions; e.g., Q-2026-0042] |
| Revision | [FILL — initial = 0, increment on each revision] |
| Issue date | [FILL] |
| Expiry date | [FILL — e.g., 30 days from issue, after which the offer cannot be issued but a new one can] |
| **Acceptance deadline** | [FILL — e.g., 15 calendar days from issue, by which the client must sign to lock the offer; distinct from expiry] |
| Acceptance method | Cotización firmada por representante autorizado y devuelta desde correo institucional, u orden de compra formal aceptada por la Universidad |
| Replaces previous quote | [FILL — quote number and revision being replaced, "none" if first] |

### 2. Customer legal and billing information

- Legal name
- Tax ID / VAT number
- Billing address
- Billing contact
- **Currency for billing** — must match CS-01 invoicing currency unless explicitly approved otherwise

### 3. Round ID and dates

- Round ID: [FILL]
- Provisional / confirmed dates: [FILL]
- Location: [FILL]

### 4. Selected gas package

| Gas | Included |
|---|---|
| CO | [Yes / No] |
| SO₂ | [Yes / No] |
| NO | [Yes / No] |
| NO₂ | [Yes / No] |
| O₃ | [Yes / No] |

### 5. Analyzers and participants

- Number of analyzers: [FILL]
- Number of participants covered: [FILL]
- Operating configuration: [Individual gas / Simultaneous CO/SO₂]
- Additional analyzer accepted with residual capacity: [YES / NO]; provisional surcharge: COP 0

### 6. Included deliverables

[FILL — derived from CS-01 Section 11.]

### 7. Exclusions and participant-borne costs

[FILL — derived from CS-01 Section 11. For international clients, list explicitly: transport, insurance, customs, visas, import taxes.]

### 8. Price

| Item | Amount |
|---|---|
| Flat round participation fee | COP 5.928.000 provisional; one to four blocks |
| Selected-block adjustment | COP 0 |
| Additional analyzer accepted with residual capacity | COP 0 during proposal stage |
| Subtotal (excl. taxes) | [CALC] |
| Taxes | [FILL — see international notes if applicable] |
| **Total** | **[CALC]** |

Currency: COP

**FX policy reference** (when invoicing currency ≠ costing currency): type of change applied, source, refresh date, FX risk allocation. Pulled from CS-01 / CS-04 Tab 1.

### 9. Payment schedule and acceptable PO conditions

**Standard payment table** (use for the default variant):

| Milestone | % of total | Amount | Due date | Method |
|---|---|---|---|---|
| Order acceptance | [FILL — e.g., 50%] | [CALC] | [FILL] | Wire / PO / card |
| Pre-round (5 business days before start) | [FILL — e.g., 50%] | [CALC] | [FILL] | Wire / PO |
| **Total** | 100% | [CALC] | | |

**Alternative payment structures** (select if applicable, document rationale):

- 100% in advance (e.g., for small amounts or first-time clients).
- 100% on delivery (only for institutional clients with approved credit; requires CS-01 pre-approval).
- PO at 30/60/90 days (only for institutional clients with credit history; needs finance approval).

**Late payment consequences** (link to CS-08 clause 6): interest, suspension of service, cancellation trigger.

### 10. Minimum-enrollment / postponement condition

[FILL — e.g., "This quotation is conditional on minimum enrollment of N participants by [date]. If minimum is not met, CALAIRE-EA may postpone or cancel the round with full refund."]

### 11. Cancellation terms

[FILL — derived from CS-01 Section 8, including the fee schedule by withdrawal deadline. Reference the CS-12 record template that will be opened on any change.]

### 12. Pre-accreditation wording

[FILL — same as CS-02: "The service may describe its design basis but may not claim that CALAIRE-EA or the round is accredited."]

### 13. Link / reference to terms and registration

- Terms and conditions: [LINK to CS-08]
- Registration form: [LINK to CS-07]
- Privacy policy / data protection notice: [LINK]

### 14. Acceptance method and authorized contact

- Acceptance: cotización firmada por representante autorizado desde correo institucional u orden de compra formal aceptada por la Universidad. Un correo informal no reserva cupo.
- Authorized CALAIRE-EA contact: [FILL NAME, EMAIL, PHONE]
- **Acceptance rule:** "This quotation is considered accepted only when CALAIRE-EA receives a written acceptance from the authorized customer contact, signed or sent from a verified email, by the acceptance deadline stated in section 1. Silence does not constitute acceptance."

## International variant — additional fields

For the "International" template variant only:

| Field | Value |
|---|---|
| Country of origin of client | [FILL] |
| Currency of billing | [FILL — must be one of CS-01 approved currencies] |
| Import taxes / VAT treatment | [FILL — e.g., "IVA exento bajo tratado X", "withholding Y%", "client responsible for import duties in country Z"] |
| Currency conversion disclosure | [FILL — "Total expressed in [BILLING CURRENCY] using reference rate [RATE] of [DATE]. Client assumes FX risk from acceptance date."] |
| Shipping terms (if applicable) | [FILL — INCOTERMS] |
| Cross-border data transfer note | [FILL — e.g., "Participant data is stored in Colombia and processed per Ley 1581/2012. By accepting, client consents to cross-border transfer of report data."] |

## Quote control

- Every revision retains the same quote family with a revision number.
- A change in gas selection, analyzer count, customer identity, round or price requires a revised quote.
- All revisions are tracked in this file (or a controlled extension per quote family) per `release_change_log.md` rules.

## Template variants

| Variant | Trigger | Notes |
|---|---|---|
| Standard | One to four selected blocks | Default flat-fee template |
| Complete participation | CO, SO₂, O₃ and NO/NO₂ blocks | Uses approved flat benchmark |
| International | Customer outside Colombia | Adds FX, import tax and cross-border data transfer fields |
| Institutional / closed | Dedicated round request | Separate full-cost quotation (CS-04 Tab 10) |

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial template |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added acceptance deadline, payment table, international FX/import tax/cross-border data fields, explicit acceptance rule. |
