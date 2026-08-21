# Source-material assessment

## Suggested 8-hour course modules

1. **Ozone metrology and traceability** — 0.75 h  
2. **GUM concepts, measurand, models, PDFs** — 1.25 h  
3. **UV photometry and transfer-standard uncertainty sources** — 1.25 h  
4. **Building uncertainty budgets** — 1.5 h  
5. **Analyzer calibration, repeatability, drift, field effects** — 1.25 h  
6. **Monte Carlo propagation and GUM validation** — 1.0 h  
7. **Worked CalAire/PT case and reporting exercise** — 1.0 h  

---

## `evaluation and uncertainty budget of ozone.md`

### Scope
Broad comparison of three ozone uncertainty contexts:

- Primary Standard Reference Photometer, NIST/BIPM level.
- Analyzer type approval and field operation under EN 14625.
- CalAire proficiency-testing reference value.

### Main topics
- Ozone generation and UV-photometric traceability.
- Beer–Lambert measurement equation.
- SRP uncertainty sources and sensitivity coefficients.
- Laboratory and field uncertainty budgets.
- Repeatability, lack of fit, interferences, environmental effects, drift.
- CalAire four-component model: repeatability, calibration curve, transfer standard, zero air.
- Example expanded uncertainties at several concentrations.

### Math depth
**Medium–high.**

- Full Beer–Lambert model.
- Sensitivity coefficients.
- Root-sum-of-squares budget equations.
- Numerical SRP, laboratory, field, and PT examples.
- Gives final results, but little line-by-line derivation from raw observations.

### Gaps and overlaps
- Best bridge between primary-standard physics, analyzer performance, and CalAire practice.
- CalAire section overlaps strongly with `uncer_o3.html`, but carries far less evidence and detail.
- SRP and EN 14625 content appears nowhere else at comparable depth.
- No detailed Type A calculation, covariance treatment, effective degrees of freedom, Monte Carlo implementation, or reporting workflow.
- References mentioned generically; exact clauses, editions, and source provenance need verification.
- Final spreadsheet offer is irrelevant course material and should be removed.

### Course use
Feeds modules **1, 3, 4, 5, 7**.  
Best core reading for measurement physics and comparison of uncertainty-budget contexts.

---

## `TGuide for Assessing Uncertainty in Ozone Analyzers and Transfer Standards.md`

### Scope
Step-by-step GUM Supplement 1 treatment centered on probability distributions and Monte Carlo propagation for ozone analyzers and transfer standards.

### Main topics
- Measurand formulation and input quantities.
- Measurement-model requirements.
- Maximum-entropy principle.
- Rectangular, Gaussian, Student’s *t*, curvilinear-trapezoid, and arcsine PDFs.
- Monte Carlo sampling.
- Correlated inputs and Cholesky decomposition.
- Estimate, variance, coverage interval, and adaptive stabilization.
- Validation of linearized GUM results against Monte Carlo.
- Sampling algorithms and notation.

### Math depth
**High, mostly theoretical/computational.**

- Equations for PDF moments and output statistics.
- Box–Muller and *t*-distribution sampling algorithms.
- Cholesky treatment of correlation.
- Shortest-interval and adaptive Monte Carlo criteria.
- No complete ozone dataset worked from inputs through final uncertainty budget.
- Few ozone-specific numerical calculations.

### Gaps and overlaps
- Large overlap with `Technical Guide_ Uncertainty Assessment Concepts and Glossary...`.
- More procedural and mathematical than glossary guide.
- Ozone references often function as examples attached to generic GUM material; no explicit analyzer or transfer-standard measurement equation.
- Claims such as MCM being “metrologically superior,” mandatory abandonment of GUF, fixed recommendation of \(10^6\) trials, and preferred Wichmann–Hill generator need qualification.
- *t*-sampling algorithm needs technical validation before teaching.
- Normative citations are incomplete or potentially conflated: JCGM 100/GUM and JCGM 101/GUM Supplement 1 should be identified separately.
- Missing sensitivity analysis, uncertainty-contribution ranking, software exercise, and real worked budget.

### Course use
Feeds modules **2 and 6**; selected content for **4**.  
Best advanced handout for PDF assignment and Monte Carlo lab.

---

## `Technical Guide_ Uncertainty Assessment Concepts and Glossary for Ozone Measurement Systems.md`

### Scope
Conceptual introduction and glossary for distribution-based uncertainty evaluation, followed by compact Monte Carlo and reporting guidance.

### Main topics
- Error-based versus state-of-knowledge interpretation.
- Formulation, propagation, and summarizing stages.
- GUF versus Monte Carlo comparison.
- Probability distribution, PDF, expectation, variance, covariance, and coverage terms.
- Symmetric versus shortest coverage intervals.
- PDF selection for ozone-related inputs.
- Curvilinear-trapezoid variance.
- Basic and adaptive Monte Carlo procedures.
- GUF validation and reporting requirements.

### Math depth
**Medium.**

- Definitions include expectation and variance integrals.
- Curvilinear-trapezoid equation.
- Monte Carlo stabilization example.
- Coverage-interval validation equations.
- No complete uncertainty budget or executable worked example.

### Gaps and overlaps
- Near-subset of `TGuide...`; much content repeated almost verbatim.
- Better suited to prerequisite reading than standalone technical instruction.
- Table formatting is broken around GUF/MCM comparison.
- “Definitions derived verbatim” requires source and copyright/provenance checking.
- Bayesian and maximum-entropy concepts named but not explained enough for application.
- Ozone-specific physical model, calibration data, field effects, drift, sensitivity coefficients, and transfer hierarchy remain thin.
- Examples such as UV-lamp cycling need evidence that effect enters measurand model as described.

### Course use
Feeds modules **1 and 2**, plus reporting portion of **7**.  
Best glossary/pre-course reading; avoid teaching it separately from `TGuide...`.

---

## `uncer_o3.html`

### Scope
Detailed CalAire case study and operational procedure for uncertainty of ozone reference measurements in PT rounds R2A and R3. Connects raw minute data, calibration records, uncertainty components, R scripts, and PT scoring.

### Main topics
- Why ozone differs from cylinder-based gases.
- Four-component measurement model.
- PT experimental design and hourly aggregation.
- QC filters and calibration-validity rules.
- Repeatability with block variance and AR(1) effective sample size.
- Calibration-curve uncertainty using GUM H.3 and lack-of-fit method.
- Concentration-dependent transfer-standard certificate.
- Zero-air residual bias.
- Complete budgets and variance shares by round and concentration.
- R processing chain and central functions.
- Use in \(z\), \(z'\), zeta, and \(E_n\) scores.
- Known limitations and omitted components.

### Math depth
**High and strongly worked.**

- Full component equations.
- AR(1) correction and effective sample size.
- Regression prediction uncertainty.
- Lack-of-fit calculation.
- Concentration-dependent standard uncertainty.
- Complete numerical budgets at 0–180 ppb.
- Variance-contribution analysis.
- R code and source-to-output traceability.

### Gaps and overlaps
- Strongest practical source; overlaps with CalAire section of `evaluation...`.
- Narrow scope: CalAire reference/PT process, not general analyzer certification or SRP calibration.
- No Monte Carlo propagation.
- Independence assumption lacks covariance study.
- Fixed \(k=2\) used despite low degrees of freedom; Welch–Satterthwaite omitted.
- Analyzer drift identified as major missing component.
- Participant uncertainty uses unsupported 15% degradation proxy.
- Use of **EN 14211** for ozone lack of fit needs correction or explicit justification; ozone standard is **EN 14625**, while EN 14211 concerns nitrogen oxides.
- Statement treating uncorrected known zero-air bias as a symmetric rectangular uncertainty requires methodological justification; GUM normally favors correction of known significant bias.
- HTML includes substantial presentation CSS. Extract instructional content into slides/handout rather than use raw source.

### Course use
Feeds modules **4, 5, and 7**; selected context for **1 and 3**.  
Best capstone exercise and instructor demonstration.

---

## Overall synthesis

- **Conceptual base:** `Technical Guide_ Uncertainty Assessment Concepts and Glossary...`
- **Advanced propagation:** `TGuide for Assessing Uncertainty...`
- **Physical and regulatory context:** `evaluation and uncertainty budget of ozone.md`
- **Worked capstone:** `uncer_o3.html`

Main duplication: two technical guides repeat formulation, PDF assignment, Monte Carlo, adaptive tolerance, validation, and reporting. Merge into one theory handout.

Main missing course elements:

- Clear ozone traceability chain: SRP, transfer standard levels, field analyzer.
- One verified measurement equation for each instrument class.
- Guided spreadsheet or R exercise using shared dataset.
- Covariance and sensitivity-coefficient exercise.
- Effective degrees of freedom and coverage-factor selection.
- Decision rules and calibration-certificate interpretation.
- Verified normative references and clause mapping.
- Explicit distinction between analyzer uncertainty, transfer-standard uncertainty, PT reference uncertainty, and assigned-value uncertainty.
