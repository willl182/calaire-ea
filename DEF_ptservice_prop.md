# Definitive Proposal: CALAIRE-EA Gaseous Air Pollutants Proficiency Testing Service

**Service:** CALAIRE-EA Proficiency Testing Scheme for Gaseous Air Pollutants  
**Launch product:** CALAIRE-EA Gas PT Round  
**Selectable scored components:** CO, SO₂, NO, NO₂ and O₃  
**Delivery model:** Centralized, controlled-atmosphere intercomparison  
**Normative basis:** ISO/IEC 17043:2023, ISO 13528:2022, and applicable ISO/IEC 17025 controls  
**Status:** Final proposal for implementation and a paid pre-accreditation round

**QMS source of truth:** `docs/qms/`

---

## 1. Executive summary

CALAIRE-EA will establish a centralized proficiency testing (PT) service for organizations that operate ambient-air gaseous pollutant analyzers. Participants will connect their analyzers to a controlled gas-generation and distribution system, measure defined zero and concentration levels, submit results and measurement uncertainties, and receive an independent statistical performance report.

Each round may include one gas, several gases or all five gases: CO, SO₂, NO, NO₂ and O₃. The selected scope will be stated in the round announcement, quotation, registration and approved round plan. Every selected gas must have an approved generation/reference method, levels, uncertainty basis and statistical implementation before execution.

The assigned-value route will depend on the number of technically valid participant results for each component and level. With fewer than 12 valid results, the assigned value will be the CALAIRE-EA reference value. With 12 or more valid results, the assigned value will be the robust participant consensus calculated under the approved statistical plan, with the CALAIRE-EA reference value used as an independent validation check. Performance will be reported by component and level using z or z′, together with ζ and En when participant uncertainty information is technically usable. No aggregate a1–a7 grade or overall pass/fail classification will be issued in the MVP.

The recommended market entry is a paid pre-accreditation round operated with accreditation-level document control. CALAIRE-EA must clearly disclose that the service is not yet accredited. Marketing and payment may begin only after the technical, quality and commercial go/no-go gates in this proposal are satisfied.

## 2. Purpose and intended outcomes

This proposal authorizes the design and controlled launch of a repeatable, commercially viable and accreditation-ready PT service. Its intended outcomes are:

1. A technically valid PT round aligned with ISO/IEC 17043 and ISO 13528 principles.
2. A complete participant journey, from quotation and registration through final reporting.
3. A controlled set of customer-facing, technical, statistical and quality records.
4. A defensible price based on actual cost, capacity and validated demand.
5. Evidence suitable for a future ISO/IEC 17043 accreditation application.

This document defines the service model. It does not replace the applicable standards, approved technical procedures, round plan or statistical plan.

### 2.1 Document precedence and QMS boundary

`docs/qms/` is the sole active source of truth for the CALAIRE-EA QMS. Approved procedures, instructions, master formats, matrices and round records under that directory control technical and quality-system operation. Former QMS copies, auxiliary analyses and archived material outside `docs/qms/` are non-controlling references unless an approved QMS document explicitly incorporates them.

This proposal controls the intended commercial service design. It must be implemented through, and remain consistent with, the approved QMS. If this proposal conflicts with an approved QMS document on technical execution, statistical evaluation, quality control, confidentiality, complaints, appeals or report authorization, the QMS document controls and the proposal must be corrected through change control. Commercial artifacts may reference QMS documents but may not silently restate or modify their controlled requirements.

## 3. Final launch decisions

The following decisions resolve the conflicts and open alternatives in the preceding proposals.

| Topic | Final launch decision |
|---|---|
| Product | Centralized Gas PT Round selectable for one, several or all of CO, SO₂, NO, NO₂ and O₃. |
| O₃ | Available as a selectable scored gas under the same component-readiness requirements as the other gases. |
| Package flexibility | Every round may contain one gas, several gases or all five gases, as defined in its approved scope and round plan. |
| Reporting units | CO in µmol/mol; SO₂, NO, NO₂ and O₃ in nmol/mol. ppm/ppb may appear only as explanatory equivalents. |
| Assigned value with fewer than 12 valid results | CALAIRE-EA reference value, derived from valid reference-analyzer readings. The calibrator setpoint is not the assigned value. |
| Assigned value with 12 or more valid results | Robust participant consensus under the approved ISO 13528 statistical method; the CALAIRE-EA reference value is the independent validation check. |
| NO₂ generation | Gas-phase titration. The fixed-NO or variable-NO design must be selected and approved in the round plan. |
| Closing zero | Include a closing zero whenever drift is evaluated or claimed; otherwise remove drift claims from participant documents. |
| Repeated levels | Not required for the MVP. Repeatability is supported by reference data and homogeneity/stability evidence. Any repeated participant levels must be predefined in the round plan. |
| `sigma_pt` | One approved formula and coefficient set per component, controlled by the statistical procedure and implemented identically in the round plan, software and report. |
| Scoring | z or z′ per level; ζ and En only when uncertainty data are suitable; percentage difference for interpretation. |
| Aggregate grade | No a1–a7 grade and no overall pass/fail classification in the MVP. |
| Accreditation claim | The service may state that it is designed under ISO/IEC 17043:2023 principles and uses ISO 13528 statistical methods. It may not claim accreditation. |

## 4. Service identity, scope and positioning

### 4.1 Public name

**CALAIRE-EA Gaseous Air Pollutants Proficiency Testing Scheme**

Launch offer: **CALAIRE-EA Gas PT Round**, configurable for one, several or all five gases.

### 4.2 Positioning statement

> CALAIRE-EA provides controlled-atmosphere proficiency testing for laboratories, monitoring networks and organizations operating ambient-air gaseous pollutant analyzers. The service supplies independent, uncertainty-aware evidence of measurement performance and comparability.

### 4.3 Declared technical scope

| Code | Component | Proposed declared range | Required unit | Launch status |
|---|---:|---:|---|---|
| CAL-AQ-CO | CO | 0–20 | µmol/mol | Selectable |
| CAL-AQ-SO2 | SO₂ | 0–180 | nmol/mol | Selectable |
| CAL-AQ-NO | NO | 0–500 | nmol/mol | Selectable |
| CAL-AQ-NO2 | NO₂ | 0–250 | nmol/mol | Selectable |
| CAL-AQ-O3 | O₃ | 0–200 | nmol/mol | Selectable |

These are proposed catalogue ranges, not evidence that every value is currently achievable. Before publication, CALAIRE-EA must verify generation and reference capability across every advertised range. Each round plan will define the actual levels used.

### 4.4 Service boundaries

The service evaluates participant measurement performance under the conditions of the round. It does not replace instrument calibration, maintenance, method validation, routine quality control, regulatory instrument approval or participant accreditation.

## 5. Target market and demand validation

Primary customers are:

- public and private ambient-air monitoring networks;
- environmental laboratories and authorities;
- organizations contracted to operate monitoring stations;
- instrument manufacturers, distributors and service providers;
- universities, research institutes and metrology organizations.

The business case must not assume that the market exists merely because the technical need exists. Before accepting payment, CALAIRE-EA will complete a documented demand study containing:

1. A named prospect list for Colombia and the reachable LATAM market.
2. Components and analyzer counts operated by each prospect.
3. Accreditation, contractual or regulatory drivers for participation.
4. Expected purchasing cycle, budget range and procurement constraints.
5. Evidence of willingness to participate, preferably expressions of interest.
6. Competitor and substitute analysis, including overseas schemes and bilateral comparisons.

The minimum viable participant count will be based on confirmed commercial interest and round capacity, not on an unsupported estimate.

## 6. Service model and participant journey

Participants bring or operate analyzers at the designated CALAIRE-EA facility. CALAIRE-EA generates traceable test atmospheres dynamically, distributes them simultaneously through a controlled manifold, monitors reference values and operating conditions, evaluates submitted results and issues coded reports.

| Stage | CALAIRE-EA deliverable | Participant responsibility |
|---|---|---|
| Offer | Programme, scope, price, dates and terms | Select components and confirm eligibility |
| Contract | Quote, contract review and confirmation | Accept terms and provide PO/payment |
| Preparation | Guide, code and technical questionnaire | Declare analyzer, method, calibration and uncertainty information |
| Setup | Connection position, checks and run schedule | Install, warm up and operate the analyzer |
| Execution | Controlled levels, references and event records | Measure according to normal procedure |
| Submission | Controlled result template and deadline | Submit results, units and uncertainty information |
| Evaluation | Dataset freeze, assigned values and scores | Clarify only documented transcription or unit issues |
| Draft report | Coded draft and review deadline | Review and submit a supported appeal if necessary |
| Final report | Authorized final report and participation statement | Use the report under the agreed conditions |
| Follow-up | Optional interpretation session | Investigate performance and corrective action |

Indicative schedule: announce 8–12 weeks before execution; close registration 2–4 weeks before execution; determine execution time from the selected gases and approved sequences; issue the draft report 2–4 weeks after data closure; allow 14 calendar days for appeals; issue the final report after appeals are resolved. A complete five-gas round will normally require approximately one operational week, subject to the NO₂ design and O₃ sequence.

## 7. Technical operating design

### 7.1 Generation and distribution

The PT item is an atmosphere generated dynamically in situ from certified reference material and zero air. It is delivered through an inert distribution manifold with sufficient excess flow to avoid backpressure and participant interference. There is no shipment of a physical PT item.

| Component | Generation/reference approach |
|---|---|
| CO | Dynamic dilution of certified gas with zero air |
| SO₂ | Dynamic dilution of certified gas with zero air |
| NO | Dynamic dilution of certified NO with zero air |
| NO₂ | Gas-phase titration of NO with generated O₃ |
| O₃ | Ozone generator and approved traceable photometric reference route |

The round plan must identify CRM certificates, traceability route, dilution equipment, reference analyzers, calibration status, measurement windows, environmental requirements and level-acceptance criteria.

### 7.2 Concentration sequence and duration

The default component block consists of an initial zero and four non-zero levels: low, medium-low, medium-high and high. The current planning basis is one hour for zero and 1.5 hours for each non-zero level, giving approximately seven hours per component block. These durations include stabilization and reporting; they must not be counted twice.

NO₂ will use one approved gas-phase-titration design:

- **Fixed-NO design:** preferred for launch where cost and stand time are constrained; approximately one seven-hour block.
- **Variable-NO design:** technically richer and more resource-intensive; approximately thirteen hours under the current sequence.

The choice affects gas use, facility time and price and must be frozen before quotation.

### 7.3 Homogeneity and stability

Homogeneity and stability are demonstrated for each round because the PT item is continuously generated and distributed. Tests must cover relevant manifold positions, direct-versus-manifold response where applicable, reference repeatability and stability throughout each level. Residual inhomogeneity is included in the assigned-value uncertainty.

A level that fails approved homogeneity, stability or reference-validity criteria will not be scored. It may be reported only as clearly identified, non-scored technical information.

### 7.4 Safety and technical readiness

Before execution, CALAIRE-EA will approve a gas-handling risk assessment covering cylinders, ventilation, leaks, CO, SO₂, NO/NO₂, generated O₃, emergency response and occupational exposure controls. Equipment readiness, CRM suitability, environmental conditions, participant connections and alarms will be recorded.

## 8. Assigned value, uncertainty and statistical evaluation

### 8.1 Assigned value

The assigned-value route is selected separately for each component and level from the number `p` of technically valid participant results:

```text
if p < 12:  x_pt = CALAIRE-EA reference value
if p >= 12: x_pt = robust participant consensus
```

For `p < 12`, the reference value is derived from valid CALAIRE-EA reference-analyzer readings within the approved measurement window. Its uncertainty budget should include, as applicable, CRM/calibration, dilution, repeatability, lack of fit, drift, environmental influence, homogeneity and stability.

For `p >= 12`, the robust consensus and its uncertainty will be calculated using the method fixed in the approved statistical plan in accordance with ISO 13528. The CALAIRE-EA reference value, generation records, historical results and uncertainty information will be used to validate the consensus before scoring. A materially inconsistent consensus triggers a documented technical review; the level will not be scored until the discrepancy is resolved.

The expanded assigned-value uncertainty will normally use `k = 2`; the corresponding standard uncertainty is used in z′ and ζ calculations. The selected route, valid participant count, calculation, validation and approval decision must be recorded per level.

### 8.2 Proficiency standard deviation

The proposed model is:

```text
sigma_pt = a * x_pt + b
```

The coefficient table proposed in `pt_proposal_o48.md` may be adopted only after reconciliation with the controlled statistical procedure and `pt_app`. One controlled source must govern every calculation.

Particular attention is required for CO: if `x_pt` is expressed in µmol/mol, an intercept expressed in nmol/mol must be converted before calculation. For example, 100 nmol/mol equals 0.1 µmol/mol. Validation tests must detect a factor-of-1,000 unit error.

### 8.3 Scores

The primary fitness-for-purpose score is selected per level:

```text
if u(x_pt) > 0.3 * sigma_pt: use z'
otherwise:                   use z

z  = (x_i - x_pt) / sigma_pt
z' = (x_i - x_pt) / sqrt(sigma_pt^2 + u(x_pt)^2)
```

When participant uncertainty information is technically complete and plausible:

```text
zeta = (x_i - x_pt) / sqrt(u(x_i)^2 + u(x_pt)^2)
En   = (x_i - x_pt) / sqrt(U(x_i)^2 + U(x_pt)^2)
```

| Indicator | Interpretation |
|---|---|
| `|z|` or `|z′| ≤ 2` | Satisfactory |
| `2 < |z|` or `|z′| < 3` | Questionable |
| `|z|` or `|z′| ≥ 3` | Unsatisfactory |
| `|ζ| ≤ 2` | Satisfactory uncertainty compatibility |
| `2 < |ζ| < 3` | Questionable uncertainty compatibility |
| `|ζ| ≥ 3` | Unsatisfactory uncertainty compatibility |
| `|En| < 1` | Satisfactory |
| `|En| ≥ 1` | Unsatisfactory |

ζ criteria must be formally approved in the controlled statistical procedure before use. ζ and En are related presentations of uncertainty compatibility and must not be described as independent confirmations.

Scores are reported per component and level. CALAIRE-EA will not issue an aggregate grade, component pass percentage or overall pass/fail result in the MVP.

### 8.4 Data integrity and software validation

Before scoring, CALAIRE-EA will:

- retain the original participant submission;
- record all accepted corrections and their justification;
- normalize only through documented, validated transformations;
- freeze and uniquely identify the official dataset;
- preserve a raw-to-final traceability map;
- record software/spreadsheet name, version and configuration;
- execute formula test cases for z/z′ selection, ζ, En, rounding and all unit conversions;
- back up the dataset, calculation files and issued reports.

Late, missing, corrected, transposed and technically invalid results will be treated under rules published before the round. Statistical outliers are not deleted merely because they perform poorly.

## 9. Reports, confidentiality and impartiality

### 9.1 Deliverables

The standard package includes a participant guide, equipment questionnaire, result form, coded draft report, final report, participation statement and optional feedback form. The final report will identify the scheme and round, participants by code, components and levels, assigned values and uncertainties, statistical methods, results, interpretations, deviations, authorized signatories and report status.

### 9.2 Confidentiality

Participant identity and results are confidential by default. A controlled code-key register will be stored separately from analysis outputs, with named access authorization and an access log. Disclosure to regulators, clients or the public requires the participant's explicit prior consent unless disclosure is required by law; where legally permitted, the participant will be informed.

Public summaries must be anonymized and checked for indirect identification. The participant agreement will govern use of CALAIRE-EA reports and prohibit misleading extraction, alteration or advertising claims.

### 9.3 Impartiality

CALAIRE-EA will maintain an impartiality risk register covering commercial pressure, prior calibration or consulting relationships, participant relationships, internal performance targets and conflicts involving staff or external experts. Each round requires conflict-of-interest declarations. A person materially involved in a participant's service, calibration or consulting work may not independently authorize that participant's evaluation or decide its appeal.

Appeals must be reviewed by competent personnel not responsible for the original disputed decision. Complaints, appeals, decisions and corrective actions will be logged and retained.

## 10. Accreditation and claim control

Before accreditation, the following wording is controlled:

| Statement | Status |
|---|---|
| “Designed and operated under ISO/IEC 17043:2023 principles” | Allowed if demonstrably true |
| “Statistical evaluation based on ISO 13528 methods” | Allowed if demonstrably true |
| “Accreditation in preparation” | Allowed only while factually true |
| “ISO/IEC 17043 accredited” | Prohibited |
| “Accredited PT provider” | Prohibited |
| “Certificate of competence” | Prohibited |
| “Participation statement” | Allowed |
| “Performance evaluation report” | Allowed |

The same approved wording must be used in the webpage, brochure, quotes, agreements, reports and participation statements.

## 11. Commercial operating model

### 11.1 Revenue model

The launch model is fee-per-round, with component packages and optional add-ons. Annual subscriptions and closed institutional rounds may be introduced after demand and delivery capacity are demonstrated.

The working benchmark is **approximately €1,600 excluding taxes per participant/analyzer for a complete five-gas round**. This is the initial commercial base because it is the only available market price reference. CALAIRE-EA will convert it to the invoicing currency using a stated exchange-rate date and then test it against actual costs, capacity and customer response. The benchmark is a starting price, not a substitute for the cost model.

Recommended offers:

| Offer | Content | Pricing basis |
|---|---|---|
| Complete Gas Round | CO, SO₂, NO, NO₂ and O₃ | Working base: approximately €1,600 excluding taxes per participant/analyzer |
| Multi-gas package | Any selection of two to four gases | Base access fee plus selected-gas fees, capped below the complete-round price |
| Single-gas package | Any one of the five gases | Base access fee plus one gas fee |
| Additional analyzer | Second analyzer under the same participant | Incremental stand, handling and reporting cost |
| Closed network round | Dedicated dates and scope | Full-cost quotation plus contingency and margin |
| Interpretation session | Post-report technical discussion | Fixed professional-services fee |

### 11.2 Cost and price calculation

The initial public-price proposal will use approximately €1,600 excluding taxes for the complete five-gas round. Before release, the cost workbook must confirm whether that benchmark recovers the expected round cost and target margin. If it does not, management must either adjust the price, reduce cost, change the minimum participant count or explicitly approve a subsidized/cost-recovery objective. The required structure is:

```text
Round cost = fixed round cost + (variable cost per analyzer × expected analyzers)

Required revenue = Round cost / (1 - target operating margin)

Base price per analyzer = Required revenue / billable analyzers

Break-even analyzers = ceiling(fixed round cost /
                    (price per analyzer - variable cost per analyzer))
```

Fixed costs include scheme coordination, planning, facility preparation, reference equipment availability, statistical setup, document control, software validation and report preparation. Variable costs include CRM/gas consumption, zero air, consumables, participant setup, data handling, report issuance and transaction costs. Annual accreditation, calibration, maintenance, insurance and commercial costs must be allocated transparently across the expected number of rounds.

The model must also include costs not yet quantified: spare parts, preventive/corrective maintenance and analyzer consumables for the CALAIRE O₃, SO₂, CO and NOx analyzers, the dynamic calibrator and the zero-air generator. These assets are essential production resources; excluding their lifecycle cost would understate the service cost. An annual maintenance/spares provision should be allocated across expected rounds, with gas-specific consumables assigned to the applicable package.

Certified-gas cost must compare a multi-component mixture with individual gas cylinders. The decision must consider certificate uncertainty and traceability, mixture stability and compatibility, concentration suitability, cylinder life, regulator/handling needs, supplier availability, delivery time, consumption by package, and the risk that one depleted or expired mixture affects several gases. A hybrid strategy is permitted where justified. Price approval requires a documented technical-commercial cylinder decision.

The pricing decision must document:

- currency, taxes and payment terms;
- expected and maximum analyzer capacity;
- confirmed participant count and conservative downside case;
- target operating margin and contingency;
- component and add-on cost drivers;
- cancellation, postponement and refund exposure;
- comparison with the approximately €1,600 benchmark and documented justification for any adjustment.

### 11.3 Capacity basis

| Operating configuration | Current planning capacity |
|---|---|
| One gas evaluated individually | Maximum 4 participants/analyzers for that gas |
| CO and SO₂ evaluated simultaneously | Maximum 3 participants, with up to 2 analyzers per participant; 6 participant analyzers in total |

These limits require an operational capacity verification covering manifold outlets, reference connections, total flow, excess-flow margin, backpressure, physical/electrical space, data acquisition and supervision. Commercial capacity is reserved by analyzer and configuration, not only by organization. A participant registering two analyzers consumes two applicable positions.

Capacity directly affects viability. The approximately €1,600 complete-round benchmark must be tested against the verified maximum billable positions rather than an assumed 8–15 participant round. Minimum enrollment, price and package availability must therefore be approved for each announced operating configuration.

### 11.4 Commercial conditions

Registration is confirmed only after contract review and receipt of the required payment or acceptable purchase order. The public offer will state minimum and maximum capacity, the date on which commercial viability is assessed, and CALAIRE-EA's right to postpone or cancel if the minimum is not met.

A proposed participant cancellation schedule is: no charge before the registration deadline; 50% after the deadline but before technical preparation is committed; 100% after preparation or execution begins. The final schedule requires legal and financial approval and must address substitutions, force majeure, CALAIRE-EA cancellation, refunds and credit notes.

## 12. Required MVP artifacts

Every artifact must have an identifier, owner, approver, version, effective date, storage location, retention period and applicable gate.

### 12.1 Customer and commercial

- service webpage/brochure and annual programme;
- round announcement and scope sheet;
- pricing workbook, approved price list and add-on table;
- quote and closed-round quotation templates;
- registration form and tracker;
- contract/PO review checklist and participant agreement;
- confirmation, invoice request and refund/credit decision records;
- participant guide, result template and feedback form.

### 12.2 Governance, people and external providers

- artifact master list, document release record and change log;
- round file index and record-retention matrix;
- impartiality register and per-round declarations;
- confidentiality agreements, code-key register and access log;
- competence criteria, training and authorization records;
- critical supplier approval and monitoring records;
- CRM/cylinder certificate review records.

### 12.3 Technical and safety

- approved round, generation and live run plans;
- equipment and participant-setup readiness checklists;
- gas safety/risk assessment and emergency controls;
- reference-instrument, generation and environmental logs;
- homogeneity/stability records and acceptance summary;
- level-acceptance and nonconforming-work decisions;
- event, deviation and corrective-action records.

### 12.4 Statistical and data integrity

- approved statistical plan and controlled formula source;
- original submissions and correction log;
- official dataset freeze and raw-to-final traceability map;
- assigned-value and uncertainty records;
- software version/configuration and validation test cases;
- calculation review, graph review and backup/export records;
- low-participant and exclusion decision records.

### 12.5 Reporting and post-round

- draft and final report templates;
- technical/statistical report review checklist;
- draft issue and final distribution logs;
- appeal and complaint forms, logs and decision letters;
- report amendment/reissue record;
- participation statement and public-summary template;
- management review and improvement record.

## 13. Approval gates

| Gate | Minimum evidence | Decision authority |
|---|---|---|
| Before marketing | Approved scope, claim wording, feasible ranges, offer, provisional dates and demand study | Scheme manager + quality + commercial |
| Before accepting payment | Approved price, viability scenario, agreement, registration workflow, minimum-participant and cancellation terms | Management + finance/commercial |
| Before execution | Approved round/statistical plans, competent staff, safe and ready equipment, suitable CRMs, participant questionnaires and reference route | Technical manager + scheme coordinator |
| Before scoring | Accepted levels, frozen dataset, approved assigned values, completed reference validation and validated software | Technical manager + statistician |
| Before draft report | Independent calculation and confidentiality review | Report reviewer |
| Before final report | Review window closed, appeals resolved, amendments controlled and final authorization signed | Authorized report signatory |
| Before accreditation application | Internal audit, management review, completed round file, corrective actions and confirmed accreditation route | Top management + quality manager |

Failure of a gate stops the affected activity. Management may not override a technical validity, impartiality, confidentiality or safety failure for commercial reasons.

## 14. Implementation roadmap

### Phase 1 — Freeze the service design

- approve this proposal and the final decision register;
- verify the advertised ranges and readiness evidence for every selectable gas, including O₃;
- reconcile `sigma_pt`, units and formulas across procedures and `pt_app`;
- decide the NO₂ design and closing-zero policy;
- confirm the accreditation route and claim wording.

### Phase 2 — Build and validate the MVP system

- produce the artifact master list and required templates;
- close traceability and uncertainty budgets;
- validate homogeneity/stability methods and statistical software;
- establish competence, supplier, safety, confidentiality and impartiality controls;
- conduct an internal dry run and retain the complete evidence file.

### Phase 3 — Validate the market and price

- complete demand, competitor and regulatory-driver research;
- gather expressions of interest;
- populate the cost workbook and downside scenarios;
- approve price, capacity, margin, cancellation and payment rules;
- release the public offer only after the marketing and payment gates pass.

### Phase 4 — Paid pre-accreditation round

- register and contract participants;
- execute the approved round;
- freeze and evaluate data;
- issue draft and final reports;
- resolve complaints and appeals;
- perform participant feedback and post-round management review.

### Phase 5 — Accreditation readiness

- audit the complete round file against ISO/IEC 17043:2023;
- close nonconformities and improvement actions;
- confirm scope and submit the application when management determines the evidence is sufficient.

## 15. Principal risks and controls

| Risk | Primary control |
|---|---|
| Insufficient demand | Named market study, expressions of interest, minimum-participant gate and postponement clause |
| Price does not recover cost | Evidence-based cost workbook, downside scenario and approved margin |
| Misleading accreditation claim | Controlled wording and quality review of every public artifact |
| Inconsistent statistical results | Single controlled formula source, software validation and independent review |
| CO factor-of-1,000 error | Fixed units and explicit conversion test case |
| Invalid assigned value | Reference route, uncertainty budget, stability evidence and plausibility review |
| Any selected gas lacks technical readiness | Component-specific approval gate before execution |
| Gas distribution bias or instability | Manifold qualification and per-round homogeneity/stability acceptance |
| Conflict of interest | Risk register, declarations and independent authorization/appeal review |
| Confidentiality breach | Coded datasets, separate code key, limited access and release checklist |
| Unsafe gas operation | Approved safety assessment, ventilation, monitoring and emergency response |
| Participant uncertainty is inflated or unusable | Questionnaire review; withhold ζ/En where requirements are not met |

## 16. Governance

| Role | Accountability |
|---|---|
| Top management | Resources, risk acceptance, commercial approval and accreditation decision |
| Scheme manager | Overall scheme design, impartiality and performance |
| Round coordinator | Participant communication, round plan and complete round file |
| Technical manager | Generation, traceability, reference validity, safety and level acceptance |
| Statistician | Statistical plan, software validation, evaluation and technical interpretation |
| Quality manager | Document control, audits, claims, complaints, CAPA and accreditation readiness |
| Commercial/finance lead | Demand evidence, quotation, price, contract review, billing and viability |
| Independent reviewer/signatory | Calculation, confidentiality and report authorization |

One person may hold more than one role only where competence is documented and independence is preserved for reviews, appeals and authorizations.

## 17. Final recommendation

CALAIRE-EA should proceed with the configurable Gas PT Round as a paid pre-accreditation service, subject to the approval gates in this proposal. Each round may include one gas, several gases or all five gases—CO, SO₂, NO, NO₂ and O₃—according to the participant selection and approved round plan.

The immediate priority is operational closure, not additional conceptual expansion: reconcile the statistical source of truth, complete the missing quality and data-integrity artifacts, validate demand, calculate a real price from actual costs, and execute a controlled dry run. Once these conditions are met, the first paid round can provide both customer value and credible evidence for ISO/IEC 17043 accreditation.

---

## Appendix A. Detailed public service offer

### A.1 Service description

The CALAIRE-EA Gas PT Round is a controlled-atmosphere intercomparison for ambient-air monitoring analyzers. Participants select CO, SO₂, NO, NO₂, O₃ or any combination of these gases. CALAIRE-EA generates the selected atmospheres, establishes or validates assigned values, evaluates participant results and supplies a confidential performance report.

The definitive scope of a particular round is the combination of:

- the published round announcement;
- the participant's accepted quotation and registration;
- the approved round plan;
- the approved statistical plan;
- any formally communicated amendment issued before execution.

### A.2 Standard inclusions

The participation fee includes:

1. One registered analyzer or measurement system.
2. The selected gas component or package.
3. Participant instructions and pre-round technical review.
4. Access to the controlled gas sequence.
5. Receipt and validation of one official result set.
6. Assigned-value and performance evaluation.
7. One coded draft report.
8. One final report and participation statement.
9. The standard appeal process.

Unless expressly included in the quotation, the fee does not include transport, accommodation, analyzer calibration or repair, replacement parts, customs, insurance of participant equipment, repeated testing caused by participant failure, or consulting to implement corrective action.

### A.3 Participant eligibility

A participant must:

- operate an analyzer suitable for at least one offered gas;
- identify the analyzer, measurement principle and range;
- declare calibration and traceability status;
- provide the requested uncertainty information where ζ or En is expected;
- comply with facility, connection and safety instructions;
- nominate authorized technical and administrative contacts;
- accept confidentiality, payment, cancellation and report-use terms.

CALAIRE-EA may reject or condition participation when an analyzer presents a safety, flow, pressure, contamination, connection or data-integrity risk.

### A.4 Configurable packages

| Package | Selectable scope | Standard output |
|---|---|---|
| Single gas | CO, SO₂, NO, NO₂ or O₃ | Scores and report for one gas |
| Multi-gas | Any two to four gases | Scores and report for selected gases |
| Complete | CO, SO₂, NO, NO₂ and O₃ | Scores and report for all gases |
| Institutional | Agreed gas selection for a closed organization/network | Dedicated coded report and optional management summary |

## Appendix B. Registration and contract-review fields

### B.1 Organization information

- legal and commercial name;
- tax identification and billing address;
- country and city;
- technical, contractual and billing contacts;
- purchase-order and invoicing requirements;
- requested report language;
- consent or refusal for named disclosure.

### B.2 PT selection

- round identifier and dates;
- selected gas or gas package;
- number of analyzers;
- optional interpretation session;
- special facility or scheduling needs;
- acceptance of the minimum-participant clause.

### B.3 Technical information per analyzer

- manufacturer, model, serial number and internal asset identifier;
- gas and measurement principle;
- measuring and configured range;
- firmware/software version;
- data-averaging interval and acquisition system;
- inlet material, connection and required flow;
- last calibration/verification date and provider;
- reference material or standard used;
- traceability statement and certificate identifier;
- result correction, conversion or compensation functions;
- standard uncertainty, expanded uncertainty, coverage factor and confidence level;
- responsible operator and relevant competence information;
- known limitations or operating conditions.

### B.4 Contract review

Before acceptance, CALAIRE-EA will confirm:

- the selected scope is offered and technically feasible;
- facility capacity and connection compatibility;
- schedule and reporting deadline;
- price, taxes, currency and payment terms;
- participant-specific requirements and deviations;
- confidentiality and disclosure status;
- absence or mitigation of impartiality conflicts;
- capability to meet report-language or administrative requirements;
- consistency between the quotation, purchase order and PT conditions.

## Appendix C. Round plan minimum content

Every round plan will contain at least:

1. Scheme and round identifiers, objectives and scope.
2. Selected gases and actual nominal levels.
3. Dates, facility, participant capacity and connection layout.
4. Staff, responsibilities, competence and authorizations.
5. CRM, zero-air, calibrator, mass-flow and reference-analyzer identification.
6. Traceability and calibration status.
7. Gas-generation equations and operating setpoints.
8. Sequence, stabilization, measurement windows and contingency time.
9. Selected NO₂ GPT alternative.
10. Initial and closing-zero policy.
11. Homogeneity and stability design and criteria.
12. Environmental and safety controls.
13. Level-acceptance and rejection criteria.
14. Data-capture, backup and event-recording arrangements.
15. Nonconforming-work and emergency decisions.
16. Approved deviations from standing procedures.
17. Links to the controlled statistical plan and participant instructions.
18. Technical, quality and scheme approvals.

## Appendix D. Statistical plan minimum content

The statistical plan must be approved before result evaluation and define:

- measurands, levels, units and rounding rules;
- expected and minimum participant numbers;
- definition of a technically valid result;
- assigned-value branch for `p < 12` and `p >= 12`;
- robust consensus algorithm and stopping criteria;
- assigned-value uncertainty for both branches;
- CALAIRE-EA reference-value calculation and validation role;
- `sigma_pt` formula and gas-specific coefficients;
- explicit unit conversion before every formula;
- z versus z′ decision rule;
- ζ and En eligibility and uncertainty normalization;
- performance limits and reporting language;
- treatment of zeros or values near zero;
- handling of censored, non-numeric or below-range data;
- treatment of transcription errors, late corrections and missing results;
- outlier policy and prohibition on performance-based deletion;
- low-participant disclosure in the report;
- graphical presentations and identity protection;
- software/version used and validation evidence;
- independent calculation review and authorization.

## Appendix E. Assigned-value decision workflow

For every gas and level:

1. Close submissions and determine technically valid results.
2. Record the valid participant count `p`.
3. If `p < 12`, calculate the CALAIRE-EA reference value and its uncertainty.
4. If `p >= 12`, calculate the approved robust participant consensus and its uncertainty.
5. Compare the selected assigned value with the CALAIRE-EA reference result, generation records, uncertainty and historical behavior.
6. Investigate any significant discrepancy or technical anomaly.
7. Accept the assigned value, exclude the level, repeat the analysis or report it as non-scored information.
8. Record the selected route and approval decision.
9. Select z or z′ using `u(x_pt) > 0.3 sigma_pt`.
10. Calculate and review applicable performance indicators.

Participant count is assessed by component and level, not merely by total registrations. Consequently, one round may legitimately use a reference assigned value for one level and robust consensus for another if valid-result counts cross the threshold.

## Appendix F. Result-submission rules

Participants will submit:

- round and participant codes;
- analyzer identifier;
- gas and level identifier;
- result in the mandatory reporting unit;
- standard uncertainty, where available;
- expanded uncertainty, coverage factor and confidence level, where available;
- number of observations and averaging period if requested;
- method, correction and dilution information requested by the round;
- comments on alarms, interruptions or deviations;
- authorized submitter and submission date.

The official result is the value received by the deadline. A correction after submission is accepted only under the published correction policy and must preserve the original value, corrected value, requestor, reason, evidence, decision and timestamp. CALAIRE-EA will not invite corrections merely because a result performs poorly.

## Appendix G. Final report structure

The final report should contain:

1. Title, unique report number, round identifier and issue status.
2. Provider identity, address and responsible personnel.
3. Accreditation-status statement and claim-control wording.
4. Objectives, scope, selected gases and dates.
5. Participant codes and confidentiality statement.
6. Generation, distribution and reference methods.
7. Actual levels, units and measurement windows.
8. Homogeneity, stability and environmental summary.
9. Assigned-value route for each level, including valid participant count.
10. Assigned values and associated uncertainties.
11. Statistical methods, `sigma_pt`, score equations and criteria.
12. Participant results and scores per component and level.
13. Graphs that preserve participant anonymity.
14. Comments on excluded or non-scored levels.
15. Deviations and their effect on validity.
16. Technical interpretation without aggregate a1–a7 grading.
17. Instructions for complaints, appeals and report use.
18. Authorized approval and issue date.

Where `p < 12`, the report will identify the reference-value route. Where `p >= 12`, it will identify the robust-consensus method and explain the independent reference validation. The report will not disguise a route change between levels.

## Appendix H. Price implementation

### H.1 Working commercial anchor

The initial benchmark for a complete five-gas round is **approximately €1,600 excluding taxes per participant/analyzer**. This anchor is retained until CALAIRE-EA has enough actual cost and sales evidence to replace or revise it.

### H.2 Package-price method

The complete-round price is not divided equally by five because coordination, registration, setup, connection, statistical control and reporting create a common base cost. CALAIRE-EA should use:

```text
Package price = common participation fee
              + sum(selected gas fees)
              + selected add-ons
```

The sum for all five gases should equal approximately €1,600 before taxes at launch. A multi-gas package should be cheaper than purchasing its gases separately, and no four-gas package should equal or exceed the complete five-gas price unless it has materially higher technical cost.

### H.3 Required pricing worksheet fields

- staff hours by role and loaded hourly cost;
- facility preparation and operating hours;
- CRM and zero-air use by gas and level;
- calibration, maintenance and equipment depreciation allocation;
- homogeneity/stability and reference measurement cost;
- consumables, safety and waste cost;
- software, data processing and reporting cost;
- sales, billing and collection cost;
- annual accreditation and quality-system allocation;
- contingency and target margin;
- participant/analyzer capacity;
- break-even participant count;
- exchange rate, source and effective date;
- applicable taxes and withholding assumptions;
- sensitivity cases for low, expected and full enrollment.

### H.4 Price approval

Management will approve the price in the invoicing currency. The approval record will state whether the service objective is commercial margin, full cost recovery, partial cost recovery or a strategically subsidized launch. Cross-border quotations must address currency risk, bank charges, taxes, customs and payment timing.

## Appendix I. Complaints, appeals and amendments

A complaint concerns service delivery; an appeal challenges a technical or statistical decision affecting a participant result. Both must be acknowledged, investigated, decided and communicated under controlled procedures.

An appeal must identify the disputed gas, level, result or decision; state the requested resolution; and provide supporting evidence. Appeals received during the published 14-calendar-day draft-review window will be resolved before final issue where practicable.

The reviewer must be competent and independent of the original disputed decision. The outcome may confirm, amend or withdraw the result. If an error affects other participants, CALAIRE-EA will assess the full dataset and issue controlled amendments to every affected report. Reissued reports must identify what changed, why, who authorized it and which prior version is superseded.

## Appendix J. Record structure and retention

Each round will have a uniquely identified evidence folder containing:

```text
01_governance_and_approvals
02_offer_contracts_and_registrations
03_participant_codes_and_confidentiality
04_round_and_statistical_plans
05_equipment_crm_and_traceability
06_safety_setup_and_execution
07_raw_reference_and_participant_data
08_homogeneity_stability_and_level_acceptance
09_dataset_freeze_and_calculations
10_draft_reports_and_appeals
11_final_reports_and_distribution
12_feedback_capa_and_management_review
```

The code key will be access-controlled separately. Retention periods must satisfy legal, contractual, accreditation and reconstruction needs. Destruction at the end of retention requires authorization and a destruction record.

## Appendix K. Definitive launch checklist

The service is ready for a paid round only when all applicable items below are confirmed:

### K.1 Service and commercial readiness

- [ ] Round permits selection of one, several or all five gases.
- [ ] Scope, dates, ranges and capacity are published consistently.
- [ ] Complete-round working price is based on approximately €1,600 excluding taxes.
- [ ] Single- and multi-gas pricing is approved.
- [ ] Minimum-enrollment and cancellation rules are approved.
- [ ] Quote, agreement, registration and billing workflow are released.

### K.2 Technical readiness

- [ ] Every selected gas has approved levels and generation/reference method.
- [ ] Reference equipment and CRMs are valid and traceable.
- [ ] NO₂ GPT alternative is selected.
- [ ] O₃ technical arrangements are approved when O₃ is selected.
- [ ] Manifold, flow, homogeneity and stability controls are ready.
- [ ] Safety controls and emergency arrangements are approved.

### K.3 Statistical and data readiness

- [ ] The `<12 reference / >=12 consensus` rule is implemented and tested.
- [ ] `sigma_pt` is single-sourced and controlled.
- [ ] CO unit-conversion tests pass.
- [ ] z/z′, ζ and En formulas pass validation cases.
- [ ] No a1–a7 or aggregate pass/fail grading remains in templates.
- [ ] Dataset freeze, correction and backup controls are operational.

### K.4 Quality readiness

- [ ] Staff competence and authorization are documented.
- [ ] Impartiality and confidentiality controls are active.
- [ ] Critical suppliers are approved.
- [ ] Report, appeal and amendment controls are released.
- [ ] Internal dry run and audit actions are closed.
- [ ] Pre-accreditation wording is correct in all public documents.

## Appendix L. Controlled decisions that remain round-specific

The service design is definitive, but the following are intentionally decided for each round:

- selected gas or gases;
- actual levels within the verified ranges;
- participant and analyzer capacity;
- assigned-value route per gas/level based on valid result count;
- fixed-NO or variable-NO GPT design;
- execution sequence and duration;
- need for repeated levels;
- final-zero inclusion based on drift claims;
- invoicing currency and exchange-rate date;
- approved price and minimum enrollment;
- staff assignments and independent reviewers;
- documented deviations and contingencies.

These round-specific decisions do not weaken standardization. They allow the scheme to remain commercially configurable while preserving the same competence, validity, impartiality, confidentiality and reporting controls for every offered gas.
