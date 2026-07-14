# MVP Blueprint for CALAIRE-EA Gas PT Commercial Service Artifacts

**Source proposal:** `DEF_ptservice_prop.md`  
**QMS source of truth:** `docs/qms/`
**Purpose:** Create the minimum commercial artifact system required to turn the existing CALAIRE-EA technical PT scheme into a clear, contractable and repeatable paid service  
**Out of scope:** Recreating round plans, technical procedures, homogeneity/stability records, statistical workbooks, result datasets or final technical-report controls already covered by the QMS

---

## 1. Objective

This blueprint defines the route for creating the commercial service artifacts around the existing CALAIRE-EA Quality Management System (QMS). It focuses on the gap between having a technically controlled proficiency testing scheme and having a service that a customer can understand, select, purchase, attend and close administratively.

The MVP must allow a prospective participant to move through this chain without undocumented decisions:

```text
Discover service
      ↓
Understand scope and conditions
      ↓
Select one or more of four blocks: CO, SO₂, O₃ and NO/NO₂
      ↓
Receive a controlled quotation
      ↓
Register and accept terms
      ↓
Receive commercial confirmation
      ↓
Receive existing QMS technical instructions
      ↓
Participate in the round
      ↓
Receive report and participation statement
      ↓
Close billing, feedback and renewal
```

The technical workflow begins after commercial confirmation and remains governed by the PSEA documents. The commercial artifacts must reference that system rather than duplicate it.

### 1.1 Source hierarchy

The artifact project uses this precedence:

1. Approved QMS documents and records in `docs/qms/`.
2. `DEF_ptservice_prop.md` for the approved commercial service design.
3. This blueprint for creating the commercial artifact layer.
4. Archived, pilot, analysis and historical files only as non-controlling source material.

No file outside `docs/qms/` may be treated as the current QMS master merely because it has the same PSEA code or a later filesystem timestamp. When a commercial artifact needs technical wording, its owner must cite or link the applicable document in `docs/qms/`; copying technical clauses into a commercial template is discouraged because it creates parallel requirements.

## 2. Commercial rules to freeze before drafting

All commercial artifacts must use the same rules:

| Topic | Controlling commercial rule |
|---|---|
| Selectable scope | A participant may select one or more of four blocks: CO, SO₂, O₃ and NO/NO₂. NO and NO₂ are contracted as one NOx block. |
| Flat proposal benchmark | Approximately COP 5,928,000 excluding taxes per participating organization for one to four blocks; indicative, not approved for release. |
| Package rule | The provisional price is flat for one to four selected blocks. |
| Assigned value | Fewer than 12 technically valid results: CALAIRE-EA reference value. Twelve or more: robust participant consensus. |
| Evaluation | z or z′, with ζ and En where uncertainty information is usable. |
| Aggregate grading | No a1–a7 grade and no overall pass/fail grade. |
| Accreditation wording | The pre-accreditation service may describe its design basis but may not claim that CALAIRE-EA or the round is accredited. |
| Standard participation unit | One registered analyzer/measurement system under one participant code. |
| Additional analyzer | May be accepted without surcharge when residual capacity exists; it may not displace another organization's first position. |
| Individual-gas capacity | Current planning maximum: 4 participants/analyzers for a gas operated individually. |
| Simultaneous CO/SO₂ capacity | Current planning maximum: 3 participants with up to 2 analyzers each; 6 participant analyzers total. |
| Confirmation | Registration is not confirmed until scope/capacity review and accepted payment or purchase order. |
| Technical control | Technical instructions, execution, data handling, evaluation and reports remain governed by the approved PSEA QMS. |

These rules should be held in one short approved commercial decision sheet. Brochures, quotes, forms and emails should source their wording from it.

## 3. Existing QMS coverage: what should not be rebuilt

The source-of-truth directory `docs/qms/` already contains a substantial QMS. The commercial layer must integrate with it.

| Existing area | Controlling evidence in `docs/qms/` | Blueprint decision |
|---|---|---|
| General PT protocol and responsibilities | `P-PSEA-01 Protocolo General EA_v2.docx` | Reuse; do not create a new technical service procedure. |
| Document and record control | `P-PSEA-02`, `P-PSEA-03`, inventories and master matrices | Use existing coding, approval and retention system. |
| Round planning | `P-PSEA-04`, `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-05`, `F-PSEA-06` | Commercial confirmation becomes an input to the existing planning process. |
| Participant communication | `P-PSEA-05 Comunicaciones del PEA.md` and prior communications | Complete/approve the QMS procedure as planned; create commercial message templates under it. |
| Participant registration and equipment data | `F-PSEA-03` participant registration, `F-PSEA-04` technical/equipment annex, `calaire-app`, participant-form prototypes | Reuse technical fields; add only missing commercial/legal fields. |
| Participant instructions | `DG-PSEA-01`, `I-PSEA-01`, `I-PSEA-02`, `comunicacion_2_participantes.md` | Reuse after commercial confirmation; separate public offer from detailed technical guide. |
| Technical execution and item control | `P-PSEA-06`, `P-PSEA-10`–`13`, `F-PSEA-07`, `F-PSEA-11` series | Fully out of scope for this commercial artifact project. |
| Statistical design and data | `P-PSEA-07`, `P-PSEA-08`, `F-PSEA-08`–`12`, `pt_app` documents | Do not recreate; commercial documents state only participant-facing evaluation rules. |
| Final technical report | `P-PSEA-09`, `F-PSEA-13` | Reuse. Only add a commercial delivery message and participation statement if absent. |
| Complaints and appeals | `P-PSEA-17`, `P-PSEA-18`, `F-PSEA-14`, `F-PSEA-15` | Reference in terms and customer communications; do not duplicate procedures. |
| Confidentiality | `P-PSEA-19`, participant coding in QMS | Reuse; commercial registration captures disclosure consent. |
| Competence and providers | `P-PSEA-20`, `P-PSEA-21`, `F-PSEA-16`, `F-PSEA-17` | Out of commercial build scope. |
| Nonconforming work and sensitive values | `P-PSEA-15`, `P-PSEA-16` | Reference only where customer notification is required. |

### 3.1 Important interface observation

`P-PSEA-01` already assigns participant communication, registration and commercial management to the project professional. It also describes announcement, expression of interest, selection, formal invitation and application registration. This provides the QMS backbone for the customer journey.

However, the repository does not show a complete controlled commercial package containing a price architecture, quotation, purchase/contract review, payment confirmation, cancellation/refund terms, sales tracker and standard renewal follow-up. Those are the MVP artifacts to create.

The commercial model must also add lifecycle costs not previously taken into account: spare parts, maintenance and consumables for the CALAIRE O₃, SO₂, CO and NOx analyzers, dynamic calibrator and zero-air generator. The certified-gas supply strategy—multi-component mixture versus individual cylinders or a justified hybrid—also remains a technical-commercial decision affecting cost, package availability and operational risk.

### 3.2 Existing drafts that can be reused

Useful source material includes:

- `docs/comunicacion_2_participantes.md` for clear participant-facing explanations;
- `docs/descripcion_programa_ea.md` for programme description;
- `docs/calendario_ppiloto.md` and existing calendars for scheduling lessons;
- `docs/auxiliares/formulario_codex/` for registration-flow prototypes;
- `F-PSEA-03` and `F-PSEA-04` for participant registration and equipment fields;
- existing proposal/contract files as layout references, not as automatically approved service terms.

These sources are drafting aids only. They do not override the QMS masters in `docs/qms/`.

Pilot wording that says participation is free or that reports cannot support regular participation must not be copied into the paid-service offer.

## 4. Commercial MVP artifact set

The MVP needs 15 commercial artifacts. They can be implemented as controlled templates, spreadsheets and reusable email messages.

| ID | Artifact | Primary function | Owner | Required before |
|---|---|---|---|---|
| CS-01 | Commercial decision sheet | Single source for scope, price, conditions and claims | Service manager | Any drafting |
| CS-02 | Service catalogue / brochure | Explain and position the offer | Commercial lead | Marketing |
| CS-03 | Annual programme and round notice | Publish dates, capacity and selected scope | Round coordinator | Marketing |
| CS-04 | Price model and approved price list | Set package prices and viability threshold | Finance/commercial | Quotation |
| CS-05 | Expression-of-interest form | Validate demand before opening sales | Commercial lead | Launch decision |
| CS-06 | Quotation template | Make a controlled commercial offer | Commercial lead | Sale |
| CS-07 | Registration/order form | Capture buyer, selected scope and administrative data | Round coordinator | Order acceptance |
| CS-08 | Terms and conditions / participant agreement | Establish binding service conditions | Management/legal | Order acceptance |
| CS-09 | Contract/PO review checklist | Confirm that CALAIRE-EA can accept the order | Commercial + scheme | Confirmation |
| CS-10 | Enrollment and revenue tracker | Control capacity, order, payment and viability | Round coordinator | Confirmation/execution |
| CS-11 | Confirmation and onboarding pack | Confirm the purchase and hand off to QMS | Round coordinator | Technical preparation |
| CS-12 | Change, cancellation and refund record | Control commercial changes and financial decisions | Commercial/finance | When triggered |
| CS-13 | Report delivery and participation message | Complete customer delivery consistently | Round coordinator | Report issue |
| CS-14 | Customer feedback form | Measure service experience and demand | Service manager | Round closure |
| CS-15 | Renewal/follow-up message and lead record | Convert completed participation into repeat demand | Commercial lead | Post-round |

## 5. Artifact CS-01 — Commercial decision sheet

### Purpose

Prevent contradictions among the brochure, quote, registration form, terms and customer emails.

### Minimum content

- service name and provider legal identity;
- selectable gases and reporting units;
- package definitions;
- standard participation unit and additional-analyzer rule;
- working flat benchmark of approximately COP 5,928,000 excluding taxes per participating organization;
- current capacity limits for individual-gas and simultaneous CO/SO₂ configurations;
- approved lifecycle-cost allocation for CALAIRE analyzers and shared generation equipment;
- approved multi-component-mixture, individual-cylinder or hybrid gas strategy;
- approved invoicing currency and exchange-rate method;
- taxes and quotation validity;
- minimum and maximum enrollment;
- payment/PO requirement for confirmation;
- cancellation and provider-postponement rules;
- accreditation-status wording;
- participant-facing assigned-value and evaluation wording;
- included and excluded services;
- responsible commercial, technical and complaint contacts.

### Acceptance test

The owner must be able to answer every field in CS-02 through CS-15 using CS-01 or an existing QMS reference. If a commercial decision is still being invented in an email, CS-01 is incomplete.

## 6. Artifact CS-02 — Service catalogue / brochure

### Purpose

Give a prospective customer enough information to decide whether to request a quotation without overwhelming them with technical procedure details.

### Recommended structure

1. What the service is.
2. Who should participate.
3. Why participation is valuable.
4. Selectable gases: CO, SO₂, NO, NO₂ and O₃.
5. One-to-four-block participation under the provisional flat fee.
6. Facility-based participation model.
7. What the standard fee includes.
8. Approximate schedule from registration to final report.
9. Performance evaluation summary.
10. Confidentiality summary.
11. Pre-accreditation status.
12. How to express interest or request a quotation.

### Mandatory wording controls

The brochure must:

- state that one or more of the four blocks may be selected;
- avoid a1–a7 and aggregate pass/fail grading;
- avoid claiming accreditation;
- distinguish the paid service from the free pilot;
- avoid publishing concentration levels unless they are part of the approved public scope;
- identify costs borne separately by the participant, including transport and equipment risk.

### Format

One concise web page plus a two-to-four-page PDF is sufficient for the MVP. Both should use the same approved text.

## 7. Artifact CS-03 — Annual programme and round notice

### Purpose

Convert the generic service into a purchasable scheduled round.

### Minimum fields

- programme year, round ID and status;
- location and dates;
- selectable gases offered in that round;
- participant/analyzer capacity;
- registration opening and deadline;
- minimum-enrollment decision date;
- approximate report date;
- working language;
- package-price link or instruction to request a quote;
- contact and registration link;
- pre-accreditation statement;
- notice that technical details follow after confirmation.

The round notice should not duplicate the detailed PSEA technical instructions.

## 8. Artifact CS-04 — Price model and approved price list

### 8.1 MVP pricing architecture

Use:

```text
Participant price = flat round fee per participating organization
                  for one to four selected blocks
```

The proposal benchmark is approximately **COP 5,928,000 excluding taxes per
participating organization** for one to four blocks. It is an indicative
conversion of the available UBA bundle benchmark and must be tested against
actual direct and full cost before release.

### 8.2 Minimum workbook tabs

| Tab | Required content |
|---|---|
| Assumptions | Exchange rate, capacity, expected enrollment, taxes, target margin |
| Common cost | Coordination, facility setup, registration, data administration and report delivery |
| Gas cost | Incremental cost for CO, SO₂, NO, NO₂ and O₃ |
| Equipment lifecycle | Spares, preventive/corrective maintenance and consumables for critical CALAIRE equipment |
| Cylinder strategy | Cost/risk comparison of multi-component mixture, individual cylinders and hybrid option |
| Packages | Single, multi and complete price calculation |
| Enrollment | Revenue and contribution by participant count |
| Scenarios | Low, expected and full capacity; break-even result |
| Approval | Approved prices, cylinder strategy, date, approvers and validity period |

### 8.3 Equipment lifecycle costs

CS-04 must include an evidence-based annual provision for:

| Asset | Cost categories to include |
|---|---|
| O₃ analyzer/reference system | Preventive maintenance, applicable lamps/scrubbers/filters, repairs and spares |
| SO₂ analyzer | Preventive maintenance, applicable lamps/filters/pumps, repairs and spares |
| CO analyzer | Preventive maintenance, applicable filters/pumps, repairs and spares |
| NOx analyzer | Preventive maintenance, converter/ozonator/pumps/filters as applicable, repairs and spares |
| Dynamic calibrator | Calibration, MFC service, seals, valves, maintenance and repair provision |
| Zero-air generator | Catalyst/scrubber/filter replacement, compressor/pump service and repair provision |

Exact parts and intervals must come from installed equipment models, manufacturer schedules, service quotations or maintenance history—not generic assumptions.

```text
Annual lifecycle provision
    = planned maintenance + consumables + calibration/service
    + risk-based corrective repair provision

Round allocation
    = annual lifecycle provision × documented round-use factor
```

Gas-specific analyzer costs should be assigned to the corresponding gas package. Shared calibrator and zero-air costs should be allocated through the common fee or actual usage hours.

### 8.4 Certified-gas cylinder strategy

CS-04 must document this comparison before price approval:

| Criterion | Multi-component mixture | Individual cylinders |
|---|---|---|
| Procurement | Potentially fewer orders/cylinders | Several orders/cylinders |
| Concentrations | One specification must suit all intended dilutions | Concentration optimized per gas |
| Stability/compatibility | Exact mixture and matrix must be certifiably stable | Component stability managed separately |
| Traceability | One certificate with component-specific values and uncertainties | Separate certificate for each cylinder |
| Package costing | Shared inventory is harder to allocate to single-gas sales | Consumption maps directly to gas package |
| Failure/expiry | One issue may affect several gases | Issue normally isolated to one gas |
| Hardware/storage | Potentially fewer regulators and connections | More regulators, storage and handling |
| Lead time | Custom-mixture availability may dominate | Availability varies by individual gas |

A hybrid strategy is acceptable—for example, a certified compatible mixture plus an individual cylinder for a gas requiring a different concentration or stability condition. The technical manager must approve suitability; commercial/finance must approve cost allocation.

### 8.5 Capacity and revenue model

| Configuration | Current commercial planning limit |
|---|---|
| Gas operated individually | 4 participants/analyzers |
| CO and SO₂ operated simultaneously | 3 participants, up to 2 analyzers each; 6 participant analyzers total |

Capacity is reserved by analyzer and configuration, not only by organization. A participant registering two analyzers consumes two positions. These planning limits should be verified operationally against manifold/reference connections, total flow and excess-flow margin, backpressure, physical/electrical space, acquisition capacity and supervision.

The workbook must calculate at least:

- individual-gas revenue with 1, 2, 3 and 4 paid positions;
- simultaneous CO/SO₂ revenue with 1, 2 and 3 participants and up to 6 analyzers;
- complete four-block revenue constrained by the lowest applicable capacity;
- mixed selections where participants purchase different gases;
- the impact of reserving any position for reference or operational needs.

The COP 5,928,000 benchmark must not be tested using an assumed 8–15 participants when current physical capacity is four. Minimum enrollment and viability must be configuration-specific.

### 8.6 Commercial logic

- The proposal uses the same price for one to four blocks.
- An additional analyzer has no surcharge during the proposal stage but requires residual capacity.
- The cost model must show contribution or shortfall separately for each selected-block scenario.
- Closed institutional rounds require a separate full-cost quotation.
- Management must explicitly record whether the first paid round targets profit, full cost recovery or strategic subsidy.

### 8.7 Price-list output

The customer-facing list should show only approved prices, currency, taxes, inclusions, additional-analyzer fee, validity and quotation requirement. Internal cost and margin details remain restricted.

## 9. Artifact CS-05 — Expression-of-interest form

### Purpose

Verify demand before committing dates and costs.

### Minimum questions

- organization and contact;
- country/city;
- one or more desired blocks among CO, SO₂, O₃ and NO/NO₂;
- number and type of analyzers;
- preferred period;
- procurement method and approximate lead time;
- ability to transport equipment to Medellín;
- interest at the approximate COP 5,928,000 flat benchmark;
- need for quotation in COP, EUR or another currency;
- interest in an institutional/closed round;
- authorization for commercial follow-up.

The form should ask whether separate CO and SO₂ analyzers will be brought and whether simultaneous operation is feasible, because this determines use of the three-participant/six-analyzer configuration.

This is not registration and creates no reserved place. The form must say so explicitly.

## 10. Artifact CS-06 — Quotation template

### Minimum sections

1. Unique quote number, issue date and expiry.
2. Customer legal and billing information.
3. Round ID and provisional/confirmed dates.
4. Selected gas package.
5. Number of analyzers and participants covered.
6. Included deliverables.
7. Exclusions and participant-borne costs.
8. Price, currency, taxes and total.
9. Payment schedule and acceptable PO conditions.
10. Minimum-enrollment/postponement condition.
11. Cancellation terms.
12. Pre-accreditation wording.
13. Link/reference to terms and registration.
14. Acceptance method and authorized CALAIRE-EA contact.

### Quote control

Every revision retains the same quote family with a revision number. A change in gas selection, analyzer count, customer identity, round or price requires a revised quote.

## 11. Artifact CS-07 — Registration/order form

### Reuse rather than duplicate

Use the existing `calaire-app`, `F-PSEA-03` participant-registration fields and `F-PSEA-04` technical/equipment fields. Add a commercial section rather than creating a second technical registration system.

### Commercial/legal fields to add

- customer legal name and tax ID;
- billing address and billing contact;
- quote/PO number;
- selected gas package and analyzer count;
- requested report language;
- acceptance of terms;
- confidentiality/disclosure selection;
- participant marketing consent, separated from service consent;
- authorized contractual and technical contacts;
- special invoicing documents or procurement portal;
- signature/acceptance date.

### Status logic

```text
Interest → Quoted → Registered → Under review →
Accepted pending payment/PO → Confirmed → Wait-listed/Rejected/Withdrawn
```

Only “Confirmed” participants flow into formal round planning.

## 12. Artifact CS-08 — Terms and conditions / participant agreement

### Minimum clauses

- parties and service description;
- selected scope and technical-QMS incorporation by reference;
- provider and participant responsibilities;
- equipment transport, custody, installation and risk;
- participant readiness and consequences of instrument failure;
- price, tax, payment and PO conditions;
- minimum enrollment, postponement and provider cancellation;
- participant withdrawal, substitution and cancellation fees;
- deadlines, result corrections and late submissions;
- confidentiality, coding and disclosure consent;
- anti-collusion and truthful reporting;
- assigned-value rule: `<12` reference, `>=12` robust consensus;
- evaluation indicators and absence of a1–a7 aggregate grading;
- draft review, complaints and appeals;
- report amendments and superseded reports;
- permitted report use and prohibition on misleading claims;
- pre-accreditation status;
- force majeure, applicable law and approved liability language.

Legal counsel or the University's authorized contracting function should approve the binding clauses. The blueprint defines content, not legal wording.

## 13. Artifact CS-09 — Contract/PO review checklist

### Purpose

Stop CALAIRE-EA from accepting an order it cannot deliver or whose purchase-order language conflicts with the PT conditions.

### Checks

- quote is valid and matches registration;
- selected gases are offered in the round;
- analyzer capacity remains available by gas and operating configuration;
- the order stays within four individual-gas positions or the three-participant/six-analyzer simultaneous CO/SO₂ limit, unless a verified revision exists;
- equipment appears compatible based on submitted data;
- price, currency, taxes and payment match;
- PO does not silently override cancellation, confidentiality or report rules;
- customer-specific report or language requirement is feasible;
- conflict-of-interest or impartiality risk is referred to the existing QMS control;
- disclosure consent is recorded;
- required payment/PO evidence is received;
- acceptance, wait-list or rejection decision is authorized.

## 14. Artifact CS-10 — Enrollment and revenue tracker

### Minimum columns

- prospect/customer ID;
- organization and country;
- round ID;
- selected gases;
- analyzer count;
- quote number, value, currency and expiry;
- registration date;
- contract-review status;
- PO/payment/invoice status;
- participant code after confirmation;
- capacity consumed;
- operating configuration: individual gas or simultaneous CO/SO₂;
- commercial status;
- cancellation/refund status;
- owner and next action;
- communication link/location.

### Required views

1. Pipeline: interest through quotation.
2. Enrollment: confirmed capacity by gas/analyzer.
3. Viability: confirmed revenue versus minimum threshold.
4. Receivables: invoiced, paid and overdue.
5. Exceptions: wait-listed, cancelled, refunded or disputed.

The tracker may be a protected spreadsheet for the MVP. Participant technical results must not be stored in it.

The tracker should automatically flag more than four confirmed analyzer positions for an individual gas and more than three participants or six analyzers for simultaneous CO/SO₂.

## 15. Artifact CS-11 — Confirmation and onboarding pack

### Confirmation message

The confirmation must state:

- customer, round and participant code;
- selected gas or gases;
- confirmed analyzer count;
- dates and location;
- payment/PO status;
- primary technical and administrative contacts;
- next deadlines;
- attached or linked QMS participant instructions;
- change/cancellation contact.

### Onboarding pack

Do not create new technical documents. Package the approved existing materials applicable to that participant:

- detailed participation protocol (`DG-PSEA-01` or approved successor);
- `I-PSEA-01` packaging/transport instructions where applicable;
- `I-PSEA-02` `calaire-app` participant instructions;
- technical/equipment questionnaire link;
- current schedule generated through existing PSEA planning;
- facility and safety information;
- official communication channel.

## 16. Artifact CS-12 — Change, cancellation and refund record

### Trigger events

- participant changes selected gases;
- participant adds/replaces an analyzer;
- participant withdraws;
- CALAIRE-EA postpones or cancels;
- minimum enrollment is not achieved;
- dates or facility change;
- force majeure affects participation;
- refund or credit note is requested.

### Minimum record

- customer, round, quote and invoice references;
- original commitment;
- requested or imposed change;
- applicable contract clause;
- technical/capacity impact;
- fee, refund or credit calculation;
- decision and authorization;
- customer notification date;
- updated tracker, quote, invoice and registration references.

## 17. Artifact CS-13 — Report delivery and participation message

The QMS already controls the technical report through `P-PSEA-09` and `F-PSEA-13`. The commercial layer needs only a controlled delivery message and, if not already covered, a participation statement.

### Delivery message fields

- participant and round code;
- attached report identifier/version;
- confidentiality notice;
- draft or final status;
- review/appeal deadline if draft;
- secure access or delivery instructions;
- report-use reminder;
- commercial and technical contacts.

### Participation statement

It may state organization, round, date, analyzer and selected gases. It must not:

- claim accreditation before accreditation exists;
- state or imply technical competence;
- replace the detailed performance report;
- publish confidential scores;
- use a1–a7 or an overall grade.

## 18. Artifacts CS-14 and CS-15 — Feedback and renewal

### CS-14 minimum feedback questions

- clarity of offer and quotation;
- ease of registration and payment;
- clarity and timeliness of communications;
- facility/logistics experience;
- usefulness and timeliness of report delivery;
- perceived value for price;
- gas/package interest for the next round;
- preferred period and procurement lead time;
- likelihood of returning or recommending;
- complaint/improvement comments.

Technical feedback that indicates a complaint, appeal or nonconformity must be routed into the existing PSEA procedure rather than managed only as a survey comment.

### CS-15 renewal follow-up

Within an approved post-round interval, send a controlled message that:

- thanks the participant;
- links to the feedback form;
- identifies the next expected programme period;
- records gases of future interest;
- offers an expression-of-interest option;
- does not disclose or market based on confidential performance.

## 19. Commercial artifact interfaces with the QMS

| Commercial output | Existing QMS recipient/input under `docs/qms/` |
|---|---|
| Confirmed participant and selected gases | `P-PSEA-04` round planning and `F-PSEA-03` participant registration (renumerado: antiguo `F-PSEA-05`) |
| Participant identity and equipment information | `F-PSEA-04` technical/equipment annex (renumerado: antiguo `F-PSEA-05A`), `calaire-app` |
| Confirmed schedule and contacts | `P-PSEA-05` communications |
| Disclosure consent | `P-PSEA-19` confidentiality control |
| Conflict identified during contract review | Existing impartiality/nonconforming-work controls |
| Customer technical instructions | `DG-PSEA-01`, `I-PSEA-01`, `I-PSEA-02` |
| Submitted results and evaluation | `P-PSEA-07`, `P-PSEA-08`, `pt_app` flow |
| Technical report | `P-PSEA-09`, `F-PSEA-13` (renumerado: antiguo `F-PSEA-04`) |
| Complaint or appeal | `P-PSEA-17` complaints, `P-PSEA-18` appeals, `F-PSEA-14` complaint / NC / CAPA register (renumerado: antiguo `F-PSEA-16`), `F-PSEA-15` appeals register (renumerado: antiguo `F-PSEA-17`) |
| Customer feedback requiring action | Relevant PSEA improvement/nonconforming-work route |

The handoff should be a controlled export or approved participant list, not manual retyping across multiple spreadsheets.

### 19.1 Code renumbering note (2026-06-14)

The SGC PEA approved and applied a functional code renumbering on 2026-06-14 (`docs/sgc/matriz_equivalencias_codigos_sgc_pea.md`). Several QMS codes used in this blueprint changed meaning or number. The table above is updated to the vigente codes. The complete equivalence map used by the commercial artifacts lives in `commercial_service/00_control/qms_code_equivalence.md` and must be consulted whenever an artifact references a `P-PSEA-XX`, `F-PSEA-XX`, `I-PSEA-XX` or `DG-PSEA-XX` code.

The most consequential changes for the commercial layer:

- `F-PSEA-05A` (technical/equipment annex) **no longer exists**; the same content is at `F-PSEA-04`.
- `F-PSEA-04` (final report) **no longer points to the report**; the final report is now at `F-PSEA-13`.
- `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19` changed meaning entirely (now = complaints, appeals, confidentiality respectively) and must not be confused with the retired SGC-macro codes of the same number.
- `P-PSEA-15` now = NC/CAPA (was continuous improvement, reserved).

## 20. Build plan

### Phase 1 — Freeze the offer (Week 1)

Create CS-01 and approve:

- legal provider identity;
- service/package names;
- selectable gases;
- price anchor and pricing objective;
- participation unit;
- payment and cancellation principles;
- claim wording;
- commercial roles and approval authority.

**Exit criterion:** No unresolved service-rule contradiction remains.

### Phase 2 — Build price and market-facing materials (Weeks 2–3)

Create CS-02 through CS-05:

- populate cost and enrollment assumptions;
- populate spares, maintenance and consumable provisions for the O₃, SO₂, CO and NOx analyzers, dynamic calibrator and zero-air generator;
- compare multi-component-mixture, individual-cylinder and hybrid certified-gas strategies;
- model the four-position individual-gas and three-participant/six-analyzer simultaneous CO/SO₂ limits;
- validate the flat one-to-four-block proposal price against actual costs;
- draft catalogue and round notice;
- test interest with a short prospect list;
- revise offer based on concrete procurement feedback.

**Exit criterion:** A prospect can understand the offer and CALAIRE-EA can determine whether the round is commercially viable.

### Phase 3 — Build order-to-confirmation flow (Weeks 3–4)

Create CS-06 through CS-11:

- quotation;
- registration additions to existing app/forms;
- terms;
- order review;
- enrollment tracker;
- confirmation/onboarding pack.

Test the flow using:

1. one block and one analyzer;
2. all four blocks with up to four analyzers;
3. two analyzers;
4. international quotation;
5. wait-listed customer;
6. PO with conflicting conditions.

**Exit criterion:** A simulated customer reaches “Confirmed” without an undocumented exception.

### Phase 4 — Build exception and closure flow (Week 5)

Create CS-12 through CS-15 and test:

- participant cancellation;
- provider postponement;
- package change;
- draft report delivery;
- final report delivery;
- feedback and renewal.

**Exit criterion:** Commercial records close cleanly and technical complaints/appeals enter the existing QMS.

### Phase 5 — Release and pilot (Week 6)

- approve controlled versions;
- train the commercial and round-coordination users;
- publish only CS-02, CS-03 and approved price information;
- retain editable masters in controlled storage;
- run the first paid-round commercial workflow;
- review defects after closure and revise once.

## 21. MVP approval gates

| Gate | Required artifacts | Approval question |
|---|---|---|
| Market release | CS-01–CS-05 | Is the offer accurate, priced, understandable and honestly positioned? |
| Quote release | CS-04, CS-06, CS-08 | Can the price and conditions be defended and accepted? |
| Order acceptance | CS-07–CS-10 | Do scope, capacity, terms and payment/PO align? |
| Technical handoff | CS-11 + QMS inputs | Can the existing round-planning process act on the confirmed order? |
| Change/refund | CS-12 | Is the financial and capacity effect documented and authorized? |
| Report delivery | CS-13 + existing QMS report approval | Is the correct controlled report going to the correct recipient? |
| Commercial closure | CS-14–CS-15 | Are feedback, revenue status and future interest recorded? |

## 22. Minimal folder structure

```text
commercial_service/
├── 00_control/
│   ├── CS-01_commercial_decisions
│   ├── artifact_register
│   └── release_change_log
├── 01_market/
│   ├── CS-02_catalogue
│   ├── CS-03_programme_round_notice
│   └── CS-05_expressions_of_interest
├── 02_pricing_restricted/
│   ├── CS-04_cost_price_model
│   └── approved_price_lists
├── 03_sales_contracting/
│   ├── CS-06_quotes
│   ├── CS-07_registrations
│   ├── CS-08_terms
│   └── CS-09_contract_reviews
├── 04_enrollment_restricted/
│   ├── CS-10_tracker
│   └── CS-11_confirmations
├── 05_changes_finance/
│   └── CS-12_change_cancellation_refund
└── 06_delivery_retention/
    ├── CS-13_report_delivery
    ├── CS-14_feedback
    └── CS-15_renewal
```

Technical round records stay in the PSEA/QMS structure under `docs/qms/`. Do not copy them into the commercial folder.

## 23. MVP definition of done

The commercial artifact system is ready when:

1. A prospect can see that one or more of four blocks are selectable.
2. The approximately COP 5,928,000 flat benchmark is reflected in the price model and clearly marked as provisional.
3. The same provisional price applies coherently to one through four blocks.
4. Equipment spares, maintenance and consumables are included for all identified CALAIRE analyzers and shared generation equipment.
5. The multi-component-mixture, individual-cylinder or hybrid gas strategy is approved.
6. Capacity and revenue use the current four-position individual-gas and three-participant/six-analyzer simultaneous CO/SO₂ limits, unless verification approves a revision.
7. The paid service is clearly distinguished from the pilot.
8. No artifact claims accreditation or uses a1–a7 grading.
9. A quotation defines scope, analyzer count, inclusions, exclusions, price and conditions.
10. Registration reuses existing QMS/app technical fields instead of duplicating them.
11. Terms cover payment, cancellation, confidentiality, report use and the assigned-value rule.
12. Contract review prevents acceptance beyond capacity or under conflicting PO terms.
13. Confirmed enrollment flows into the existing QMS round plan.
14. Commercial and participant identity data are access-controlled.
15. Changes, cancellations, refunds and postponements are traceable.
16. Report delivery references the controlled QMS report rather than creating a parallel report.
17. Complaints and appeals route into existing PSEA controls.
18. Feedback and future demand are captured after the round.

## 24. Immediate next actions

1. Approve this commercial-only scope for the artifact project.
2. Assign owners for service, commercial/finance, quality and round coordination.
3. Create CS-01 and freeze the commercial rules.
4. Review and approve the still-pending `P-PSEA-05` communication procedure because it is the main QMS interface.
5. Build CS-04 around the approximately COP 5,928,000 flat benchmark and direct-cost floor.
6. Inventory the CALAIRE O₃, SO₂, CO and NOx analyzers, dynamic calibrator and zero-air generator and obtain lifecycle-cost evidence.
7. Approve the multi-component-mixture, individual-cylinder or hybrid certified-gas strategy.
8. Verify the four-position individual-gas and three-participant/six-analyzer simultaneous CO/SO₂ capacity.
9. Decide the launch price objective: margin, full cost recovery or strategic subsidy.
10. Draft CS-02 and CS-03 using existing programme and participant communications.
11. Extend the existing participant registration flow with the CS-07 commercial fields.
12. Draft CS-06, CS-08 and CS-09 as one contractable sales package.
13. Simulate the full interest-to-confirmation workflow before publishing the paid offer.

This sequence keeps the MVP narrow: use the existing QMS to operate the proficiency test, and build only the commercial shell required to make that technical capability purchasable and repeatable.
