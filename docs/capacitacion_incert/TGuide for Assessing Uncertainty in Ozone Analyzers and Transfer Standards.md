### Technical Step-by-Step Guide for Assessing Uncertainty in Ozone Analyzers and Transfer Standards

#### 1\. Foundations of Metrological Rigor and Scope

In high-accuracy environmental monitoring, the strategic importance of uncertainty evaluation cannot be overstated. Adherence to the  **ISO/IEC Guide 98-3 (GUM) Supplement 1**  ensures that ozone concentration data is not merely a collection of numbers, but a technically robust and legally defensible record. By utilizing the propagation of distributions, a metrologist quantifies the "degree of belief" in a measurement, providing the rigorous proof required for regulatory compliance and long-term climate modeling.The scope of this guide is the evaluation of measurement uncertainty for a well-defined physical measurand—specifically  **ozone concentration** —modeled through a single-output mathematical relationship. This assessment is governed by the normative references of  **ISO/IEC Guide 98-3:2008 (GUM)**  and its  **Supplement 1** .While the traditional GUM Uncertainty Framework (GUF) relies on the "law of propagation of uncertainty" via Taylor series linearization, the  **Monte Carlo Method (MCM)**  is metrologically superior in scenarios where the measurement model is non-linear, the input PDFs are asymmetric, or the contributory uncertainties are of varying magnitudes. Relying on standard linearization for complex ozone transfer standards carries significant risk; it may yield unrealistic coverage intervals that fail to reflect the true state of knowledge. MCM bypasses these limitations by numerically propagating the full probability distributions of the inputs.

#### 2\. The Formulation Stage: Modeling the Ozone Measurand

The formulation stage serves as the metrological blueprint, dictating the accuracy and integrity of all subsequent numerical calculations. A flawed model at this stage cannot be corrected by even the most sophisticated Monte Carlo simulation.

##### The Four-Step Formulation Process

1. **Define the Output Quantity (**  **$Y**$  **):**  Identify the measurand (e.g., corrected ozone concentration).  
2. **Identify Input Quantities (**  **$X\_1, \\dots, X\_n**$  **):**  List all variables affecting the result. For ozone transfer standards, this includes  **molar volume of air, UV absorption path length, ozone generator stability, cell temperature, and manifold pressure.**  
3. **Develop the Functional Relationship (**  **$Y \= f(X)**$  **):**  Establish the mathematical model relating inputs to the output.  
4. **Assign Probability Density Functions (PDFs):**  Assign a PDF ( $g\_{X\_i}(\\xi\_i)$ ) to each input quantity based on the metrologist’s state of knowledge.

##### Model Requirements

The functional relationship  $f(X)$  must be continuous with respect to the input elements in the neighborhood of their best estimates. In ozone analysis, the model must uniquely define the output; for example, if the chemistry involves quadratic relationships, the specific physical root must be identified.

##### The Principle of Maximum Entropy

In Type B evaluations, the metrologist must apply "expert judgment" through the  **Principle of Maximum Entropy** . This selects a unique PDF that maximizes information entropy under the constraints of available information, thereby avoiding the assumption of knowledge not actually present (Source 6.3.1). This transforms qualitative information into a quantitative  $g\_X(\\xi)$  that represents the most honest state of knowledge.

#### 3\. Comprehensive Assignment of Probability Density Functions (PDFs)

Selecting the correct PDF ( $g$ ) is a strategic encoding of the metrologist's knowledge. These distributions represent the degree of belief regarding the values that can be assigned to the physical inputs.

##### Structured PDF Assignments for Ozone Inputs

* **Rectangular Distributions (**  **$R(a,b)**$  **):**  For inputs where only upper ( $b$ ) and lower ( $a$ ) limits are known, such as manufacturer specs for pressure sensor drift.  
* *Expectation:*   $E(X) \= (a+b)/2$  
* *Variance:*   $V(X) \= (b-a)^2/12$  
* **Gaussian (Normal) Distributions (**  **$N(x, u^2(x))**$  **):**  For inputs where only a best estimate and standard uncertainty are available.  
* *Expectation:*   $E(X) \= x$  
* *Variance:*   $V(X) \= u^2(x)$  
* **t-Distributions (**  **$t\_v(\\bar{x}, s^2/n)**$  **):**  For Type A evaluations from  $n$  independent ozone indications or calibration certificates with finite degrees of freedom  $v$ .  
* *Expectation:*   $E(X) \= \\bar{x}$  (for  $n \> 2$ )  
* *Variance:*   $V(X) \= \\frac{n-1}{n-3} \\cdot \\frac{s^2}{n}$  (for  $n \> 3$ )  
* **Curvilinear Trapezoid (Inexact Limits):**  Assigned when boundaries of an interval (like a digital readout rounding error) are themselves inexact ( $a \\pm d$  and  $b \\pm d$ ).  
* *Expectation:*   $E(X) \= (a+b)/2$  
* *Variance:*   $V(X) \= \\frac{(b-a)^2}{12} \+ \\frac{d^2}{9}$  (Source 6.4.3.3)  
* **Arc Sine (U-shaped) Distributions (**  **$U(a,b)**$  **):**  Critical for inputs that cycle sinusoidally, such as  **sinusoidal temperature cycling in field-deployed ozone shelters.**  
* *Expectation:*   $E(X) \= (a+b)/2$  
* *Variance:*   $V(X) \= \\frac{(b-a)^2}{8}$  (Source 6.4.6.3)Using a U-shaped distribution for cyclical temperature effects provides a more accurate representation than a rectangular assumption, as it correctly identifies higher probability density near the cycle limits.

#### 4\. Propagation of Distributions via Monte Carlo Method (MCM)

MCM provides a numerical implementation of the propagation of distributions that bypasses the need for the complex partial derivatives and sensitivity coefficients required by the GUF.

##### Step-by-Step Implementation Procedure

* **Selection of Trials (**  **$M**$  **):**   $10^6$  trials are recommended for statistical stability of the coverage interval.  
* **Generation of Vectors:**  Sample  $M$  vectors from the assigned input PDFs.  
* **Gaussian:**  Use the  **Box-Muller transform.**  
* **Multivariate Gaussian:**  For correlated inputs, use  **Cholesky decomposition**  ( $U\_x \= R^T R$ ) to transform independent draws into correlated vectors.  
* **Model Evaluation:**  Calculate  $y\_r \= f(x\_r)$  for  $r \= 1, \\dots, M$ .  
* **Sorting:**  Arrange model values into non-decreasing order  $y\_{(1)} \\leq y\_{(2)} \\leq \\dots \\leq y\_{(M)}$  to provide a discrete representation  $G$ .The statistical validity of MCM depends on the pseudo-random number generator. We recommend the  **enhanced Wichmann-Hill generator**  for its  $2^{121}$  period, ensuring no sequence repetition occurs during large-scale ozone uncertainty trials.

#### 5\. Summarization of Results and Adaptive Procedures

Statistical stabilization is required to ensure that reported uncertainty is not an artifact of random sampling noise.

##### Calculating the Estimate and Uncertainty

* **Estimate (**  **$y**$  **):**   $\\bar{y} \= \\frac{1}{M}\\sum\_{r=1}^{M} y\_r$  (Source Formula 16).  
* **Standard Uncertainty (**  **$u(y)**$  **):**   $u^2(y) \= \\frac{1}{M-1}\\sum\_{r=1}^{M} (y\_r \- \\bar{y})^2$  (Source Formula 17).**Metrological Warning:**  To avoid "subtractive cancellation"—where common leading digits are lost in the calculation—Formula 17 is mandatory over the mathematically equivalent mean-square-minus-squared-mean formula (Source 7.6 Note 1).

##### Adaptive Monte Carlo Procedure

To ensure results reach the stipulated numerical tolerance ( $\\delta$ ), follow this stabilization logic:

1. Perform  $M \\geq \\max(J, 10^4)$  trials, where  $J$  is the smallest integer  $\\geq 100/(1-p)$ .  
2. Calculate  $y, u(y), y\_{low}, y\_{high}$  for the sequence  $h$ .  
3. Calculate the standard deviation  $s\_y$  associated with the average of the estimates.  
4. **Stabilization Criteria:**  A numerical result is deemed stabilized only if  **twice the standard deviation (**  **$2s**$  **)**  associated with each parameter ( $y, u(y), y\_{low}, y\_{high}$ ) is less than the numerical tolerance  $\\delta$  (Source 7.9.1, 7.9.4).  
5. If criteria are not met, increase trials and repeat.For asymmetric ozone PDFs, the  **shortest coverage interval**  is calculated by finding  $r^*$  such that  $y\_{(r^*\+q)} \- y\_{(r^\*)}$  is a minimum (where  $q \= pM$ ). This often provides a more physically realistic range than symmetric intervals.

#### 6\. Validation of the GUM Uncertainty Framework (GUF)

Validation confirms whether simpler linear models are sufficient for ongoing monitoring or if high-accuracy standards demand continuous MCM use.

##### The Validation Process

1. Apply GUF to yield a coverage interval  $y \- U\_p, y \+ U\_p$ .  
2. Calculate differences  $d\_{low} \= |y \- U\_p \- y\_{low}|$  and  $d\_{high} \= |y \+ U\_p \- y\_{high}|$ .  
3. If  $d\_{low}$  or  $d\_{high} \> \\delta$ , the GUF is invalid for this application.

##### Theoretical Uncertainty Budget Comparison

Component,GUF Contribution ( $u\_i(y)$ ),MCM-Derived Impact,Ozone Application Example

Model Linearity,First-order Taylor terms,Accounts for all higher-order terms,Non-linear UV absorption at high concentrations

Input PDFs,Assumed Gaussian/t-dist,"Uses assigned  $g$  (Rectangular, U-shaped)",Sinusoidal temp cycling in shelters

Coverage Interval,$k \\cdot u(y)$  (Symmetric),$y\_{low}$  to  $y\_{high}$  (Shortest),Asymmetric drift in generator stability

If the comparison is "unfavorable," the metrologist must abandon GUF. High-accuracy ozone transfer standards often exhibit non-linearities where the linear approximation fails.

#### 7\. Technical Annex: Sampling Algorithms and Notation

Transparency requires standardized notation:  $g$  for the PDF and  $G$  for the distribution function.

##### Principal Symbols

* $u(y)$ : Standard uncertainty.  
* $U\_p$ : Expanded uncertainty for coverage probability  $p$ .  
* $\\delta$ : Numerical tolerance (Source 7.9.2).

##### Sampling Implementation Algorithms

1. **Standard Gaussian**  **$N(0,1)**$  **:**  
2. Generate  $r\_1, r\_2$  from  $R(0,1)$ .  
3. $z\_1 \= \\sqrt{-2 \\ln r\_1} \\cos(2\\pi r\_2)$ .  
4. **t-Distribution with**  **$v**$  **degrees of freedom (Source Table C.5):**  
5. Generate  $r\_1, r\_2$  from  $R(0,1)$ .  
6. If  $r\_1 \< 0.5$ ,  $t \= 1/(4r\_1-1)$  and  $v\_{draw} \= r\_2/t^2$ . Else,  $t \= 4r\_1-3$  and  $v\_{draw} \= r\_2$ .  
7. Accept  $t$  if  $v\_{draw} \< 1 \- |t|/2$  or  $v\_{draw} \< (1 \+ t^2/v)^{-(v+1)/2}$ . Else, repeat.**Numerical Integrity:**  As per  **GUM Clause 7.2.6** , rounding must only occur at the final reporting stage. All intermediate MCM trials must retain full machine precision to prevent the accumulation of numerical errors. The integrity of the uncertainty assignment ultimately depends on the detailed knowledge of the measurement method and the analytical rigor of the metrologist.

