# PDF assessment

Page numbers below = physical PDF pages. Sampling focused on specifications, calibration, verification, and uncertainty content.

## Instrument manuals

### `APOA-370_Operation_Manual_GZ0000051248K.pdf`

- **Covers:** HORIBA APOA-370 UV-absorption ozone analyzer.
- **Uncertainty-relevant sections:**
  - **§10.2 “Specification,” p. 104:** minimum sensitivity 0.5 ppb at 2σ; reproducibility ±1% full scale; linearity ±1% full scale; zero and span drift ±1% FS/day, ±2% FS/week; T90, flow, interferences, environmental limits.
  - **§4 “Calibration,” pp. 23–41:** preparation, automatic calibration, manual calibration.
  - **§4.4.2–4.4.3, pp. 39–40:** zero and span calibration.
- **Course value:** **High.** Good Type B budget exercise using sensitivity, reproducibility, linearity, and drift. Useful comparison against Thermo 49i. Weak on measured noise because averaging period and dedicated noise test absent.

### `EPM-manual-Model 49i.pdf`

- **Covers:** Thermo Model 49i UV photometric ozone analyzer; multipoint calibration against reference photometer.
- **Uncertainty-relevant sections:**
  - **Table 1-1 “Model 49i Specifications,” pp. 25–26:** zero noise 0.25 ppb RMS at 60 s; detection limit 0.5 ppb; zero drift <1 ppb/24 h and <2 ppb/7 d; span drift <1%/month; linearity ±1% FS.
  - **Chapter 4 “Calibration,” pp. 137–150.**
  - **“Ozone Loss Test,” pp. 140–141; “Linearity Check,” pp. 141–143; “Intercomparability Test,” pp. 143–144.**
  - **“Zero Adjust,” p. 145; “Span Adjust,” p. 146; “Calibration Curve,” p. 147.**
  - **“Periodic Zero and Span Checks,” pp. 147–148:** drift calculations and diagnostic limits.
- **Course value:** **Very high.** Best commercial-analyzer source. Supports RMS noise, zero/span drift, multipoint residuals, linear regression, ozone-loss testing, and distinction between uncertainty components and operational pass/fail limits.

### `P1014KAW_copia.pdf`

- **Covers:** EPA SOP for NIST Standard Reference Photometer operation, QC, and ozone-transfer-standard comparisons.
- **Uncertainty-relevant sections:**
  - **§2.2 “Sources of Error in the Photometry Principle,” pp. 13–14:** absorption coefficient, optical path length, transmittance, sensitivity coefficients.
  - **§4.2 “Performing Quality Control Checks,” pp. 29–38:** pressure/temperature zero and span; stability-monitor test; repeated observations.
  - **§5.1–5.2, pp. 41–51:** guest-instrument stability, data-quality factors, pneumatic configuration, excess flow, comparison design.
  - **§6 “SRP Quality Assurance,” pp. 53–55:** stated precision, routine QC, pressure drift, SRP-to-SRP acceptance criteria.
  - **§7.6 “SRP Stability Measurement and Adjustment,” pp. 62–63:** lamp, temperature, power, stabilization, count-ratio variability.
- **Course value:** **Very high.** Strong source for Beer–Lambert sensitivity, repeatability, pressure/temperature effects, regression, and SRP verification. Too detailed for full treatment in eight hours; extract one photometry exercise and one comparison exercise.

---

## International comparison and SRP documents

### `BIPM.QM-K1_2.protocol_copia.pdf`

- **Covers:** BIPM.QM-K1 comparison of national ozone standards against BIPM-SRP27; direct comparison and transfer-standard protocols over 0–500 nmol/mol.
- **Uncertainty-relevant sections:**
  - **Protocol A §5, p. 7; Protocol B §§5.2 and 6.3, pp. 14, 16:** ten readings per level and repeatability limits.
  - **Protocol B §3, p. 12; §7, pp. 16–17:** transfer-standard stability and post-transport comparison.
  - **Protocol A §7, p. 8; Protocol B §§9–10.2, pp. 18–19:** generalized least-squares regression, slope, intercept, predicted values.
  - **Protocol A §6, p. 8; Protocol B §8, p. 17; Appendix 1, pp. 21–25:** GUM budget, distributions, sensitivities, concentration-dependent terms, covariance.
  - Initial/final zero and high-level conditioning appear in procedures, but no independent zero/span adjustment test.
- **Course value:** **Very high.** Best formal source for GUM budgets, constant versus proportional components, covariance, regression with uncertainty in both axes, and transport stability.

### `BIPM.QM-K1_KRISS_2024_copia.pdf`

- **Covers:** Real Protocol B comparison: KRISS-SRP5, transfer KRISS-SRP3, BIPM-SRP27, and SRP28 stability control.
- **Uncertainty-relevant sections:**
  - **§8 “Measurement protocol,” pp. 3–4:** repeated comparison sequences and stability checks.
  - **§§12.4–12.7, pp. 6–8:** BIPM and KRISS uncertainty budgets; covariance; absorption cross-section treatment.
  - **§14, pp. 8–9; §15, pp. 10–11:** generalized least-squares results, slope/intercept, predicted values, degrees of equivalence.
  - **§16 “Stability of the transfer standard,” p. 12:** comparison before/after transport; reported slope change.
- **Course value:** **Very high as worked case.** Provides real data context for budgets, covariance, regression, and drift. Weak for commercial-analyzer noise, response time, and zero/span diagnostics.

### `nistir6963_copia.pdf`

- **Covers:** NIST Standard Reference Photometer design, UV dual-cell measurement, and performance over roughly 0–1000 ppbv.
- **Uncertainty-relevant sections:**
  - **§5 “Electronics Operation,” p. 8; §8, pp. 9–11:** counting, correlated lamp noise, replicated measurements.
  - **§9 “Performance,” pp. 11–12; §10, pp. 12–14:** initial/final zeros, randomized concentration levels, regression, residuals, repeatability, stability.
  - **Tables 2–4, pp. 18–20; Figure 4, p. 25:** zero statistics and linearity results.
  - **§11 “Measurement Uncertainties,” pp. 14–15; Tables 5–6, p. 21:** RSS propagation for cross-section, transmittance, pressure, temperature, and optical length.
- **Course value:** **High.** Best physical explanation of SRP measurement and transmittance/counting uncertainty. Good Beer–Lambert and zero-repeatability exercises. Limited formal span, response-time, and interference treatment.

---

## EPA protocols, rules, and transfer standards

### `Calibrators_SOP_2016_copia.pdf`

- **Covers:** EPA SOP for Teledyne 700EU, T700U, T750, 703E, ozone generators, and mass-flow controllers; Level 2–3 traceability.
- **Uncertainty-relevant sections:**
  - **§12.2, p. 6:** transfer-standard hierarchy and cumulative uncertainty.
  - **§12.3, pp. 7–11:** photometer tracking, multipoint verification, zero/span calibration, recertification.
  - **§12.4, pp. 11–12:** ozone-generator verification and calibration.
  - **§12.5, pp. 12–16:** mass-flow-controller calibration, slope/intercept, standard deviation.
  - **Appendix A, pp. 22–23:** photometer and output-flow calibration.
- **Course value:** **Very high.** Practical source for traceability, zero/span, stabilization, multipoint checks, acceptance decisions, flow calibration, and propagation from MFCs. No complete formal uncertainty budget.

### `OzoneTransferStandard_2030.pdf`

- **Covers:** Sabio Model 2030 portable UV-photometric ozone transfer standard with optional generator.
- **Uncertainty-relevant section:**
  - **“Specifications,” p. 1:** zero noise 0.6 ppb RMS; detection limit 1 ppb; zero drift <1 ppb/24 h and <2 ppb/7 d; span drift <1%/month; precision 1 ppb; linearity ±1% FS; flow 1 L/min; generator accuracy ±1% setpoint.
- **Course value:** **High for short Type B exercise.** Students can convert noise, drift, linearity, and generator accuracy into standard uncertainties. Commercial sheet lacks test methods, confidence levels, covariance, and detailed operating conditions.

### `us epa ozone 2023-22531.pdf`

- **Covers:** 2023 EPA rule updating 40 CFR Part 50 Appendix D; UV photometric calibration and revised ozone absorption cross-section.
- **Uncertainty-relevant sections:**
  - **“Summary” and §I, pp. 1–2:** absorption coefficient 304.39 atm⁻¹ cm⁻¹ with 0.31% uncertainty; QA criteria for slopes, intercepts, zero drift, span drift, and multipoint calibration.
  - **Appendix D §2, p. 4:** measurement principle and traceability.
  - **§4.1 and §4.5, p. 5:** Beer–Lambert equation, temperature, pressure, optical length, ozone loss, repeated determinations, linearity warning.
  - **Figures, pp. 6–8:** analyzer and UV-calibration system layouts.
- **Course value:** **Very high.** Best source for defining measurement equation and sensitivity coefficients. Also useful for separating metrological uncertainty from regulatory QA limits.

### `v5apxc_wa_copia.pdf`

- **Covers:** CARB protocol for multipoint performance audits using Teledyne T703U portable ozone transfer standard and 751H zero-air generator.
- **Uncertainty-relevant sections:**
  - **§C.2, PDF pp. 5–6:** audit configurations and comparison method.
  - **§C.3, p. 6:** SO₂, NO₂, NO, humidity, and VOC interferences.
  - **§C.6.1, p. 8:** quarterly recertification and slope-stability criteria.
  - **§C.7–C.7.2, pp. 8–16:** point selection, pre/post-zero, flow, tubing, warm-up, stabilization, backpressure.
  - **§C.8.3, pp. 17–18:** certified slope/intercept correction and percent difference.
  - **§C.9, pp. 18–19:** acceptance limits and corrective actions.
- **Course value:** **Very high.** Best end-to-end field-audit exercise: correct readings using certificate, calculate errors, evaluate conformance, and discuss tubing, pressure, stabilization, interference, and zero drift. More operational than GUM-focused.

### `P1016Y93.pdf`

- **Covers:** EPA 2023 technical-assistance document for ozone transfer standards: hierarchy, qualification, acceptance, verification, reverification, regression, and uncertainty.
- **Uncertainty-relevant sections:**
  - **§§3.1–3.2, p. 33:** photometer-equipped standards versus generator-only diagnostic devices.
  - **§4.1, pp. 33–35:** repeatability, point-difference, slope/intercept, and between-cycle stability criteria.
  - **§§4.2–4.4, pp. 35–38:** qualification, acceptance, verification, and drift.
  - **§§5.1–5.2, pp. 38–41:** verification and reverification workflows.
  - **§§6.3–6.15, pp. 47–52:** point selection, warm-up, stability, frequency, transport, zero air, excess flow, materials, line conditioning.
  - **Appendix A, pp. 59–63:** regression and stability calculations.
  - **Appendix C, pp. 67–68:** documented calibration and measurement uncertainty.
  - **Appendices D–E, pp. 69–81:** rationale and qualification tests for temperature, elapsed time, relocation, hysteresis, and adjustment.
- **Course value:** **Excellent; strongest course backbone.** Supports classification, verification datasets, regression, drift, flow/zero-air cause analysis, transport effects, and experimental design.

---

## Portable calibrator product sheets

### `Portable Multi Point Calibrator & Zero Air Unit.pdf`

- **Covers:** Vasthi PVair-9007 multipoint calibrator and PVair-9008 zero-air unit; dilution, GPT, optional ozone generator/photo-cell.
- **Uncertainty-relevant sections:**
  - **Product description, p. 1:** dilution/GPT concept, temperature/pressure compensation, zero-air output.
  - **“Technical Specifications,” p. 2:** flow accuracy ±1% FS; repeatability ±0.5% FS; linearity ±0.5% FS; T95 <180 s; zero-air residual contaminants; flow and dew-point limits.
- **Course value:** **Moderate.** Useful critical-reading exercise: convert full-scale flow limits, model dilution-ratio sensitivity, and estimate contamination effects. Missing ozone stability, photometer uncertainty, traceability, drift, test conditions, and raw data. Ozone range conflicts between pp. 1 and 2.

### `vashti Portable Multi Point Calibrator Zero Air Unit.pdf`

- **Covers:** Same PVair-9007/PVair-9008 product; one-page web/product sheet.
- **Uncertainty-relevant section:**
  - **“Technical Details,” p. 1:** same flow accuracy, repeatability, linearity, response, zero-air output, dew point, and residual-gas limits.
- **Course value:** **Low; redundant.** Could support same Type B exercise, but contains less context. Treat both Vasthi PDFs as one commercial source, not independent evidence or proof of transfer-standard qualification.

---

## Recommended 8-hour use

1. **Measurement equation:** EPA 2023 rule + NISTIR 6963.
2. **Commercial analyzer budget:** Thermo 49i; APOA-370 as comparison.
3. **Transfer-standard verification:** P1016Y93.
4. **Formal GUM and regression:** BIPM.QM-K1 protocol.
5. **Real comparison case:** KRISS 2024 report.
6. **Field audit:** CARB Appendix C.
7. **Short specification critique:** Sabio 2030 or one Vasthi sheet.

Best practical dataset structure: zero plus six ozone levels, three cycles, pre/post-zero, reference and analyzer readings, temperature, pressure, flow, and certificate slope/intercept. Students calculate repeatability, regression, residuals, drift, corrected concentration, combined uncertainty, and conformity decision.
