The metrological evaluation and uncertainty budget of **ozone (\\(O\_3\\)) analyzers** is distinct from other ambient air gases. Because \\(O\_3\\) is unstable and highly reactive, it cannot be stored in compressed gas cylinders and must be generated dynamically on-site using an ozone generator (calibrator) and certified against ultraviolet (UV) photometry.

Based on the provided standard operating procedures, European Standards (EN 14625), and key metrological protocols (BIPM/NIST), the uncertainty budget for ozone analyzers is established under three distinct operational frameworks:

---

## **1\. Primary Standard Reference Photometer (NIST/BIPM Level 1 SRP)**

The Standard Reference Photometer (SRP) developed by NIST and the US EPA serves as the primary metrological standard for ozone globally. Its operating principle relies on the **Beer-Lambert Law** at the \\(253.7\\text{ nm}\\) mercury emission line to measure transmittances:

\\\[x \= \\frac{-1}{2\\sigma L\_{opt}} \\frac{T}{P} \\frac{R}{N\_A} \\ln(D)\\\]

Where \\(x\\) is the ozone amount fraction, \\(\\sigma\\) is the absorption cross-section, \\(L\_{opt}\\) is the optical path length, \\(T\\) and \\(P\\) are cell temperature and pressure, \\(R\\) and \\(N\_A\\) are physical constants, and \\(D\\) is the ratio of light intensities through the cells.

### Standard Reference Photometer (BIPM-SRP27) Uncertainty Budget:

| Component (\\(y\\)) | Source / Variable | Probability Distribution | Standard Uncertainty \\(u(y)\\) | Sensitivity Coefficient \\(c\_i \= \\frac{\\partial x}{\\partial y}\\) | Uncertainty Contribution to \\(u(x)\\) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Optical Path (\\(L\_{opt}\\))** | Measurement scale, Repeatability, Correction factor | Rectangular | \\(0.52\\text{ cm}\\) | \\(-\\frac{x}{L\_{opt}}\\) | \\(2.89 \\times 10^{-3} \\cdot x\\) |
| **Pressure (\\(P\\))** | Gauge accuracy, cell differences | Rectangular | \\(0.034\\text{ kPa}\\) | \\(-\\frac{x}{P}\\) | \\(3.37 \\times 10^{-4} \\cdot x\\) |
| **Temperature (\\(T\\))** | Temperature probe and gradient | Rectangular | \\(0.07\\text{ K}\\) | \\(\\frac{x}{T}\\) | \\(2.29 \\times 10^{-4} \\cdot x\\) |
| **Intensity Ratio (\\(D\\))** | Scaler resolution (\\(8 \\times 10^{-6}\\)), Repeatability (\\(1.1 \\times 10^{-5}\\)) | Triang. / Rect. | \\(1.4 \\times 10^{-5}\\) | \\(\\frac{x}{D \\ln(D)}\\) | \\(0.28\\text{ nmol/mol}\\) (constant) |
| **Cross-Section (\\(\\sigma\\))** | Conventional CCQM.03.2019 value | Normal | \\(0.35 \\times 10^{-19}\\text{ cm}^2\\) | \\(-\\frac{x}{\\sigma}\\) | \\(1.06 \\times 10^{-2} \\cdot x\\) |

*Note: In direct photometer-to-photometer comparisons using the same cross-section value, the uncertainty of \\(\\sigma\\) is set to zero.*

### BIPM-SRP27 Standard Uncertainty Formula

When the cross-section uncertainty is factored out for direct calibration comparisons, the combined standard uncertainty \\(u(x)\\) simplifies to:

\\\[\\mathbf{u(x) \= \\sqrt{(0.28)^2 \+ (2.92 \\times 10^{-3}x)^2}}\\text{ nmol/mol}\\\]

---

## **2\. Laboratory Type Approval & Field Operation Budgets (BS EN 14625\)**

European Standard **BS EN 14625** specifies the continuous measurement of ambient ozone using UV photometry and details two combined uncertainty budgets evaluated at the hourly alert threshold (\\(l\_h \= 120\\text{ nmol/mol}\\)).

### A. Laboratory Type Approval Budget (Requirement b)

This budget incorporates individual variances determined under controlled laboratory settings:

\\\[\\mathbf{u\_c \= \\sqrt{u\_{r,z}^2 \+ u\_{r,lh}^2 \+ u\_{l,lh}^2 \+ u\_{gp}^2 \+ u\_{gt}^2 \+ u\_{st}^2 \+ u\_V^2 \+ u\_{H\_2O}^2 \+ u\_{int}^2 \+ u\_{av}^2 \+ u\_{\\Delta sc}^2 \+ u\_{cg}^2}}\\\]

* **\\(u\_{r,z}\\) and \\(u\_{r,lh}\\)**: Repeatability at zero and at the alert threshold.  
* **\\(u\_{l,lh}\\)**: Lack of fit of the calibration curve (\\(u\_{l,lh} \= \\frac{r\_{max}}{100} \\frac{l\_h}{\\sqrt{3}}\\)).  
* **\\(u\_{gp}, u\_{gt}, u\_{st}, u\_V\\)**: Influence quantities for sample pressure, sample gas temperature, surrounding temperature, and voltage.  
* **\\(u\_{H\_2O}, u\_{int}\\)**: Positive and negative interferences (water vapor, toluene, xylene).  
* **\\(u\_{av}\\)**: Averaging effect.  
* **\\(u\_{\\Delta sc}\\)**: Difference between sample/calibration ports.  
* **\\(u\_{cg}\\)**: Uncertainty of the calibration gas standard.

#### Example Calculation (EN 14625 Lab Test at \\(120\\text{ nmol/mol}\\)):

* Combined Standard Uncertainty (\\(u\_c\\)): **\\(4.3\\text{ nmol/mol}\\)**  
* Relative Expanded Uncertainty (\\(W\\), with \\(k=2\\)): **\\(7.1%\\)** (conforms to the regulatory limit \\(W \\le 15%\\)).

### B. Field Operation Uncertainty Budget

In actual field installations, the budget is recalculated using site-specific conditions and accounts for **long-term drift** and **calibration zero air purity**:

\\\[\\mathbf{u\_{c,act} \= \\sqrt{u\_{r,z}^2 \+ u\_{r,C}^2 \+ u\_{l,lh}^2 \+ u\_{gp,act}^2 \+ u\_{gt,act}^2 \+ u\_{st,act}^2 \+ u\_{v,act}^2 \+ u\_{H\_2O,act}^2 \+ u\_{int,act}^2 \+ u\_{av}^2 \+ u\_{d,l,z}^2 \+ u\_{d,l,lh}^2 \+ u\_{\\Delta sc}^2 \+ u\_{zg}^2 \+ u\_{cg}^2}}\\\]

* **\\(u\_{r,C}\\)**: The highest value between the standard uncertainty of repeatability at the alert threshold and the field reproducibility (\\(u\_{r,f}\\)).  
* **\\(u\_{d,l,z}\\) and \\(u\_{d,l,lh}\\)**: Long-term drift standard uncertainty at zero and span (modeled as a rectangular distribution over the observed bi-weekly drift: \\(\\frac{D\_{l}}{\\sqrt{3}}\\)).  
* **\\(u\_{zg}\\)**: Standard uncertainty of the zero gas purity (\\(u\_{zg} \= \\frac{1}{\\sqrt{3}}\\) nmol/mol based on a maximum impurity allowance of \\(1\\text{ nmol/mol}\\)).

#### Example Calculation (EN 14625 Field Test at \\(120\\text{ nmol/mol}\\)):

* Combined Standard Uncertainty (\\(u\_{c,act}\\)): **\\(4.7\\text{ nmol/mol}\\)**  
* Relative Expanded Uncertainty (\\(W\\), with \\(k=2\\)): **\\(7.8%\\)**.

---

## **3\. Proficiency Testing (PT) Reference Value Budget (CALAIRE Scheme)**

For proficiency testing gas circuits, CalAire implements a **4-component uncertainty model** based on dynamic generation:

\\\[\\mathbf{u\_c(O\_3) \= \\sqrt{u\_{rep}^2 \+ u\_{curva}^2 \+ u\_{patron}^2 \+ u\_{aire\_cero}^2}}\\\]

This model highlights the unique features of ozone standard dynamics:

1. **No Dilution Flow Term (\\(u\_{flow} \= 0\\))**: The calibrator's output is certified end-to-end; mass flow controller uncertainties are already accounted for inside the calibrator certificate uncertainty (\\(u\_{patron}\\)).  
2. **Concentration-Dependent Standard (\\(u\_{patron}\\))**: Derived from the dynamic calibrator certificate (e.g., \\(U(X) \= 0.0051 \\cdot X \+ 0.67\\text{ ppb}\\), with \\(k=2\\)) rather than a constant cylinder value.  
3. **\\(u\_{rep}\\) (Repeatability)**: Calculated using Type A statistics corrected for auto-correlation (AR(1)).  
4. **\\(u\_{curva}\\) (Analyzer Calibration Curve)**: Represents the uncertainty introduced by the multipoint calibration fit. Because \\(O\_3\\) has significant calibration residuals, this is the most dominant component, accounting for up to **\\(45%\\) of the total variance** at high concentrations.  
5. **\\(u\_{aire\_cero}\\) (Zero Air Purifier)**: Treats any uncorrected zero gas bias (e.g., \\(0.040\\text{ ppb}\\)) as a rectangular distribution (\\(\\frac{|error|}{\\sqrt{3}} \= 0.0231\\text{ ppb}\\)).

### Example Total Budgets in PT Rounds (k \= 2):

* **At \\(180\\text{ ppb}\\) (High Level)**: \\(U \= \\mathbf{2.03\\text{ ppb}}\\) (\\(1.13%\\) relative). The calibrator standard uncertainty (\\(u\_{patron}\\)) is the dominant contributor (\\(61%\\) of variance).  
* **At \\(40\\text{ ppb}\\) (Low Level)**: \\(U \= \\mathbf{1.25\\text{ ppb}}\\) (\\(3.12%\\) relative). At this lower level, the calibration curve uncertainty and calibrator standard uncertainty are almost equal in variance.

---

📊 I can turn this detailed uncertainty framework into a structured spreadsheet template so you can easily calculate and track these specific ozone uncertainty budgets.

