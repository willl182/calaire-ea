### Technical Guide: Uncertainty Assessment Concepts and Glossary for Ozone Measurement Systems

#### 1\. Introduction to Uncertainty in Ozone Metrology

In the rigorous field of atmospheric metrology, the strategic evaluation of measurement uncertainty is a fundamental prerequisite for the certification of ozone analyzers and transfer standards. The quality of measurement results is not merely a reflection of precision but is a direct consequence of a structured understanding of the measurand—the specific quantity intended to be measured—and a critical analysis of all contribution sources as defined in  **ISO/IEC Guide 98-3** . For ozone sensors utilizing UV photometry, this requires a meticulous decomposition of the Beer-Lambert law parameters, ensuring that the reported mole fraction is scientifically defensible.Metrologists must transition from traditional "error-based" thinking toward a distribution-based "state of knowledge" approach. In this framework, an ozone concentration is not viewed as a single point with a plus-minus error, but as a probability density function (PDF) that quantifies the degree of belief about the values that can be assigned to the measurand. This shift ensures the reliability of data used in regulatory compliance and environmental monitoring. This guide bridges the gap between theoretical metrology and the practical calibration of ozone instrumentation by providing a structured framework for uncertainty assessment.

#### 2\. Core Methodology: The Three Stages of Uncertainty Evaluation

The evaluation of uncertainty is a disciplined, three-stage process:  **Formulation** ,  **Propagation** , and  **Summarizing** . Once the formulation is complete, the resulting PDF for the ozone concentration is mathematically determined, requiring only numerical or analytical implementation to achieve a solution.

##### The Formulation Stage

During formulation, the metrologist establishes the mathematical and probabilistic foundation:

1. **Define the Measurand:**  Explicitly identify the output quantity  $Y$ . In ozone metrology, this is typically the mole fraction or mass concentration of ozone.  
2. **Identify Input Quantities:**  Determine the input quantities  $X \= (X\_{1}, \\dots, X\_{N})^{T}$  upon which  $Y$  depends. For a photometer, these include the absorption cross-section ( $\\sigma$ ), path length ( $L$ ), gas temperature ( $T$ ), and pressure ( $P$ ).  
3. **Develop the Mathematical Model:**  Establish the functional relationship  $Y \= f(X)$ . This model transforms the "indications" (raw sensor signals) into the measurand estimate.  
4. **Assign Probability Density Functions (PDFs):**  Based on available knowledge, assign appropriate PDFs to each input quantity  $X\_{i}$  to represent the state of knowledge regarding their variability.

##### Propagation and Summarizing

The  **Propagation**  stage moves the input PDFs through the model to determine the output PDF  $g\_{Y}(\\eta)$ . The  **Summarizing**  stage then extracts the expectation (the estimate  $y$ ) and the standard deviation (the standard uncertainty  $u(y)$ ) from this resulting PDF.| Feature | GUM Uncertainty Framework (GUF) | Monte Carlo Method (MCM) || \------ | \------ | \------ || **Core Principle** | Law of Propagation of Uncertainty | Propagation of Distributions || **Mathematical Basis** | First-order Taylor series approximation | Random sampling from input PDFs || **Output Characterization** | Assumed Gaussian or shifted  $t$ \-distribution | Numerical representation ( $G$ ) of the distribution || **Ideal Application** | Linear or near-linear ozone models | Non-linear Beer-Lambert models or asymmetric inputs || **Summarizing Extraction** | Analytical derivation of  $y$  and  $u(y)$ | Statistical calculation of  $y$  and  $u(y)$  from  $M$  trials |

#### 3\. Glossary of Principal Terms and Definitions

Precise terminology is required to prevent confusion between statistical concepts and metrological results in transfer standard certifications. The following definitions are derived verbatim from  **ISO/IEC Guide 98-3/Suppl 1:2008** :

* **Probability Distribution:**  A function giving the probability that a random variable takes any given value or belongs to a given set of values.  
* **Probability Density Function (PDF):**  The derivative, when it exists, of the distribution function.  
* **Expectation:**  The property of a random variable, which, for a continuous random variable  $X$  characterized by a PDF  $g\_{X}(\\xi)$ , is given by  $E(X) \= \\int\_{-\\infty}^{\\infty} \\xi g\_{X}(\\xi) d\\xi$ .  
* **Variance:**  The property of a random variable, which, for a continuous random variable  $X$  characterized by a PDF  $g\_{X}(\\xi)$ , is given by  $V(X) \= \\int\_{-\\infty}^{\\infty} (\\xi \- E(X))^{2} g\_{X}(\\xi) d\\xi$ .  
* **Standard Deviation:**  The positive square root  $V(X)^{1/2}$  of the variance.  
* **Covariance (Mutual Uncertainty):**  The property of a pair of random variables that characterizes the dependency between them.  
* **Coverage Interval:**  An interval containing the value of a quantity with a stated probability, based on the information available.  
* **Coverage Probability:**  The probability that the value of a quantity is contained within a specified coverage interval.  
* **Law of Propagation of Uncertainty:**  The method of evaluating standard uncertainty by using a first-order Taylor series approximation to the measurement model.

##### Selection of Coverage Intervals

Metrologists must distinguish between the  **Probabilistically Symmetric Coverage Interval**  and the  **Shortest Coverage Interval** . For ozone sensors that exhibit asymmetric probability distributions—common in non-linear measurement models or when  $u(y)$  is large relative to  $y$ —the shortest interval is the superior choice. The shortest interval always contains the  **mode**  (the most probable value) for unimodal distributions, providing the most compact and realistic range for a stated coverage probability.

#### 4\. Assigning Probability Density Functions (PDFs) to Ozone Sensor Inputs

The assignment of PDFs is based on the  **Principle of Maximum Entropy**  and  **Bayes' Theorem** , ensuring no more information is assumed than is possessed.

##### Common PDF Assignments for Ozone Standards

* **Gaussian (Normal) Distribution:**  Assigned when the only available information is a best estimate and an associated standard uncertainty. This is used for the  **ozone absorption cross-section**  at a specific wavelength.  
* **Rectangular Distribution:**  Assigned when only a lower limit ( $a$ ) and an upper limit ( $b$ ) are known. This is typical for  **manufacturer purity specifications**  for zero-air or known limits of temperature fluctuation.  
* **Arc Sine (U-shaped) Distribution:**  Assigned if a quantity is known to cycle sinusoidally between limits. Metrologists must account for this in the case of  **periodic power fluctuations in the UV lamp**  of an ozone analyzer or diurnal temperature cycling.  
* **Scaled and Shifted t-distribution:**  Assigned when information is derived from a series of independent  **indications**  (Type A evaluation) or calibration certificates specifying effective degrees of freedom.

##### The Curvilinear Trapezoid

Metrologists must account for the impact of rounded interval limits. When the limits of a calibration certificate are subject to rounding, a  **Curvilinear Trapezoid**  (rectangular distribution with inexactly prescribed limits  $d$ ) is assigned. The variance  $V(X)$  of this distribution is calculated as:  $$V(X) \= \\frac{(b-a)^{2}}{12} \+ \\frac{d^{2}}{9}$$  This formula demonstrates that the variance is always greater than that of a standard rectangular distribution, providing a necessary mathematical penalty for the "inexactness" of the reported limits.

#### 5\. The Monte Carlo Method (MCM) for Non-Linear Ozone Models

MCM is the preferred practical alternative when ozone measurement models are non-linear or input distributions are asymmetric, as it reduces the analytical effort required to calculate complex partial derivatives (sensitivity coefficients).

##### MCM Implementation Procedure

1. **Select Trial Number (**  **$M**$  **):**  Choose  $M$  (typically  $10^{5}$  or  $10^{6}$ ) to provide the required numerical tolerance.  
2. **Generate Input Vectors:**  Sample  $M$  vectors from the assigned input PDFs (e.g., sampling  $T, P, \\sigma,$  and  $L$ ).  
3. **Model Evaluation:**  Calculate the model value  $y\_{r} \= f(x\_{r})$  for each vector.  
4. **Sort and Represent:**  Sort the values into strictly increasing order to provide a discrete representation ( $G$ ) of the distribution function.

##### Adaptive Monte Carlo Procedure

To ensure the reported significant digits for ozone concentration are correct, an  **Adaptive Procedure**  is utilized. The procedure continues until the results stabilize within a required  **Numerical Tolerance (**  **$\\delta**$  **)** . A result is stabilized when twice the standard deviation associated with it is less than  $\\delta$ .The value of  $\\delta$  is linked directly to the number of significant digits required. For example, if  $u(y) \= 0.0004$  and one significant digit is meaningful ( $n\_{dig}=1$ ), then  $u(y) \= 4 \\times 10^{-4}$ ,  $c=4$ , and  $l=-4$ . Following  $\\delta \= \\frac{1}{2} 10^{l}$ , the tolerance  $\\delta \= 0.00005$ .

#### 6\. Validation of Results and Reporting Standards

Metrologists are required to validate the GUM uncertainty framework using MCM to ensure that the primary approach (linearization) is demonstrably applicable to the specific ozone analyzer.

##### The Validation Process

Validation is achieved by comparing the coverage intervals:

1. Obtain the GUF interval  $y \- U\_{p}, y \+ U\_{p}$ , where  $U\_{p}$  is the expanded uncertainty.  
2. Obtain the MCM endpoints  $y\_{low}$  and  $y\_{high}$ .  
3. Calculate absolute differences:  $d\_{low} \= |(y \- U\_{p}) \- y\_{low}|$  and  $d\_{high} \= |(y \+ U\_{p}) \- y\_{high}|$ .  
4. If both  $d\_{low} \\leq \\delta$  and  $d\_{high} \\leq \\delta$ , the GUF approach is validated for that specific analyzer.

##### Reporting Requirements

A high-value ozone calibration report must include:

* The  **estimate**  ( $y$ ) of the ozone concentration.  
* The  **standard uncertainty**  ( $u(y)$ ) associated with the estimate.  
* The  **coverage probability**  (typically 95%).  
* The specific  **endpoints**   $y\_{low}, y\_{high}$  of the coverage interval.  
* The  **interval type**  (e.g., Shortest Coverage Interval).Adherence to these standards ensures that ozone transfer standards maintain a transparent and scientifically defensible chain of traceability across monitoring networks.

