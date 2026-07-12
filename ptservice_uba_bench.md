---

# 1. What their service actually is

Their public positioning is clear:

> They offer accredited proficiency testing for gaseous air pollutants for operators of national/international air-quality monitoring networks, manufacturers of measurement equipment, civil engineers, and laboratories measuring air quality.

That gives you a useful target-market statement. They are not only selling to “labs”; they explicitly include:

| Target client                                       | Why relevant for us                   |
| --------------------------------------------------- | ------------------------------------- |
| Air quality monitoring networks                     | Very important for Colombia / LATAM   |
| Measurement equipment manufacturers                 | Possible future client segment        |
| Environmental laboratories                          | Direct PT participants                |
| Civil engineers / air-quality measurement providers | Potential private-sector participants |

They state that their facility is used to assess performance of air-quality measurements through proficiency testing. ([Umweltbundesamt][1])

For your proposal, you can position CALAIRE-EA similarly:

> “A proficiency testing scheme for operators of ambient air quality monitoring instruments and laboratories performing measurements of gaseous air pollutants, designed to support external quality assurance, technical competence, and comparability of measurements.”

This connects very well with your ISO/IEC 17043 requirement that the scheme must clearly define scope, participants, clients, PT items, assigned values, and performance evaluation. 

---

# 2. Their technical-service model

This is the most important benchmark.

Their PT is not based on shipping a small sample to each lab. It is a **field/intercomparison facility model**:

> Participants bring or operate their ambient air monitoring instruments at an inter-laboratory facility over several days, while the provider generates controlled concentrations of gases.

They describe the exercise as lasting usually **three to four days**, during which participants measure **NO, NO₂, CO, SO₂ and O₃**. Then the provider performs statistical analysis comparing participant results with reference values. ([Umweltbundesamt][1])

The next exercise page says they organize a **one-week proficiency test** for operators of ambient air quality measuring devices. ([Umweltbundesamt][2])

## Practical implication for your service

You have two possible models:

| Model                       | Description                                                | Commercial impact                                                  |
| --------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ |
| **Centralized facility PT** | Participants bring analyzers to your facility              | Easier to control gases, higher logistical burden for participants |
| **Mobile / on-site PT**     | You bring gas generation/reference system to networks/labs | Higher cost, but attractive for national networks                  |
| **Hybrid**                  | Centralized annual round + special on-site closed rounds   | Best commercial structure                                          |

For CALAIRE-EA, I would define the core service as:

> **Centralized or controlled-atmosphere intercomparison for gaseous air pollutants, with optional closed/on-site rounds for monitoring networks.**

---

# 3. Scope and measurement ranges

They publish their gas scope and ranges:

| Gas |           Published range |
| --- | ------------------------: |
| O₃  | up to 200 nmol/mol or ppb |
| SO₂ | up to 180 nmol/mol or ppb |
| CO  |  up to 20 µmol/mol or ppm |
| NO  | up to 500 nmol/mol or ppb |
| NO₂ | up to 250 nmol/mol or ppb |

([Umweltbundesamt][2])

## Practical implication for your scheme catalogue

Your catalogue should include the same type of information, not just “we offer CO/SO₂/NOx.”

Example:

| Scheme code | Component |                       Range | Unit           | Method expectation                        | Evaluation |
| ----------- | --------- | --------------------------: | -------------- | ----------------------------------------- | ---------- |
| CAL-AQ-CO   | CO        |                        0–20 | µmol/mol / ppm | Reference/equivalent ambient-air analyzer | z′ / En    |
| CAL-AQ-SO2  | SO₂       |                       0–180 | nmol/mol / ppb | EN 14212 or equivalent                    | z′ / En    |
| CAL-AQ-NOX  | NO/NO₂    | NO up to 500; NO₂ up to 250 | nmol/mol / ppb | EN 14211 or equivalent                    | z′ / En    |
| CAL-AQ-O3   | O₃        |                       0–200 | nmol/mol / ppb | EN 14625 or equivalent                    | z′ / En    |

Even if you use Colombian/US/EPA methods instead of EN methods, the artifact should still show: **component, range, unit, accepted method family, score, and report output**.

---

# 4. Requirements for participants

They explicitly require or recommend that monitoring instruments comply with reference methods:

| Component | Standard named by Umweltbundesamt |
| --------- | --------------------------------- |
| O₃        | EN 14625                          |
| SO₂       | EN 14212                          |
| CO        | EN 14626                          |
| NO/NO₂    | EN 14211                          |

They also say other measurement methods may be possible by contacting them, and that participants are responsible for calibration of their instruments and recording their data. ([Umweltbundesamt][2])

## Practical implication for your participant guide

Your guide needs a section like:

```text
Eligible instruments and methods

Participants should use instruments and methods normally used for ambient air quality monitoring. The preferred methods are [Colombian / EPA / EN / equivalent methods]. Other methods may be accepted after technical review.

Participants are responsible for:
- instrument installation and operation;
- calibration status;
- internal QA/QC;
- data recording;
- reporting results within the established deadline.
```

This is important because it avoids you being responsible for the participant’s calibration. Your ISO/IEC 17025 support file also reinforces that equipment calibration, traceability, and competence must be controlled where they affect validity. 

---

# 5. Evaluation model: z′ and En

This is extremely useful.

They state that compliance is evaluated using:

| Criterion                     | Purpose                                                  |
| ----------------------------- | -------------------------------------------------------- |
| **z′-score**                  | Common/general performance criterion                     |
| **En number**                 | Individual criterion considering measurement uncertainty |
| Repeatability/reproducibility | Additional technical performance information             |
| Measurement uncertainty       | Included in the assessment framework                     |

They cite the standards/protocols of the European Reference Laboratory for Air Pollution, and the next exercise page says results are evaluated according to the **AQUILA N37 protocol** for intercomparison exercises. ([Umweltbundesamt][1]) ([Umweltbundesamt][2])

They also define a pass rule:

> The PT is passed if **80% of all possible results of a component** are assessed with z′-score categories **a1 to a3**. ([Umweltbundesamt][2])

## Practical implication for your proposal

This gives you a strong model:

```text
Primary performance evaluation:
- z′-score for comparison against reference values, incorporating the uncertainty of the assigned/reference value when relevant.

Complementary evaluation:
- En number when participant uncertainty is reported and technically usable.
- Repeatability/reproducibility indicators when the design includes repeated concentration levels or repeated measurements.
```

Your ISO 13528 file already supports using z-score, z′, zeta, En, difference, percentage deviation, and uncertainty-aware criteria depending on the objective and uncertainty structure. 

For CALAIRE-EA, I would **not** start with too many scores. I would propose:

| Score                        | Use                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------- |
| **z′-score**                 | Main score for participant performance                                       |
| **En**                       | Optional/secondary, only when participant reports valid expanded uncertainty |
| **% difference**             | Easy interpretation for participants                                         |
| **Repeatability indicators** | If multiple repeated levels are included                                     |

---

# 6. Accreditation positioning

They publicly state two accreditation claims:

1. Their gaseous air pollutant PT is accredited under **EN ISO/IEC 17043:2023** on the next exercise page. ([Umweltbundesamt][2])
2. Their general gas PT page still mentions accreditation since 2017 under **EN ISO/IEC 17043:2010**. ([Umweltbundesamt][1])

This shows something useful: mature providers display accreditation prominently but also keep older page text, so you must be careful with version consistency.

## Practical implication for your public page

For CALAIRE-EA, until accreditation is granted, use:

> “Designed and operated under ISO/IEC 17043:2023 principles and ISO 13528 statistical methods. Accreditation under ISO/IEC 17043 is in preparation / in process. The scheme is not yet accredited.”

Do **not** put “accredited” anywhere until the scope certificate exists.

---

# 7. Their price model for gaseous air pollutants

This is the key commercial information.

For their 2025 gaseous air pollutant PT, they publish:

> Participation for O₃, SO₂, CO and NO/NO₂: **€1,655 excl. VAT**, including evaluation of results and provision of the report. ([Umweltbundesamt][2])

This is very useful because it is the same technical family as your intended service.

## What this means for you

Their model is:

```text
One package price = participation in the full gas PT bundle
Includes: evaluation + report
Excludes: VAT
```

They do **not** publicly show separate prices per gas. They package the gas round as a bundle:

| Package                  | Includes               |
| ------------------------ | ---------------------- |
| Gaseous air pollutant PT | O₃ + SO₂ + CO + NO/NO₂ |
| Price                    | €1,655 excl. VAT       |
| Included                 | Evaluation + report    |

For CALAIRE-EA, I would copy the **structure**, not the exact price.

Recommended pricing structure:

| Package                                     | Includes                         | Pricing logic             |
| ------------------------------------------- | -------------------------------- | ------------------------- |
| **Full Gas PT Round**                       | CO, SO₂, NO/NO₂, O₃ if available | Main package              |
| **Core Gas PT Round**                       | CO, SO₂, NO/NO₂                  | If O₃ is not ready        |
| **Single Component Add-on / Limited Round** | One gas only                     | Higher price per gas      |
| **Institutional Round**                     | Multiple instruments/sites       | Base fee + per instrument |
| **Closed Network Round**                    | Private exercise for one client  | Quoted separately         |

Given their €1,655 benchmark, a Colombian/LATAM pre-accreditation price could be built from your cost model, but strategically you now know this is **not a €100–€300 service**. It is a specialized QA/compliance service.

---

# 8. Their cancellation policy

They publish a clear cancellation rule:

| Timing                        |           Charge |
| ----------------------------- | ---------------: |
| Up to 7 days before start     |             Free |
| Up to 3 days before start     | 25% handling fee |
| Less than 3 days before start |      Full amount |

([Umweltbundesamt][2])

## Practical implication

Copy this structure almost directly. For CALAIRE-EA:

```text
Cancellation policy

- Free cancellation up to 7 calendar days before the start of the round.
- Cancellation between 7 and 3 calendar days before the start: 25% administrative/handling fee.
- Cancellation less than 3 calendar days before the start or no-show: 100% of the participation fee.
- For closed or custom rounds, cancellation conditions are defined in the quotation.
```

This is especially important for gas PT because your cost is committed before the participant arrives.

---

# 9. Their complaint / objection process

They have two complaint/appeal mechanisms.

For the general PT programme, participants can report complaints or objections by email within **14 days** after receiving confirmation of participation and after receiving the report. Complaints are handled under complaints management, reviewed by experts not involved in the matter, with no disadvantage to the complainant, and justified complaints may lead to editorial/technical changes and a new report edition. ([Umweltbundesamt][3])

For the gas PT page, objections to the assessment in the **draft report** must be submitted by email within **14 days** after the draft report. ([Umweltbundesamt][2])

## Practical implication

Your service artifacts need two windows:

| Stage                           | Artifact                                           | Deadline                  |
| ------------------------------- | -------------------------------------------------- | ------------------------- |
| After confirmation/instructions | Complaint or objection to participation conditions | 14 days                   |
| After draft report              | Appeal/objection to assessment                     | 14 days                   |
| After final report              | Complaint about report/service                     | 14 days or defined period |

Recommended text:

```text
Participants may submit complaints or objections by email within 14 calendar days after receiving the participation confirmation, draft report, or final report, as applicable. Appeals against performance assessment must refer to the specific result, criterion, calculation, or technical reason for objection. Appeals are reviewed by competent personnel not involved in the original decision.
```

This maps directly to your ISO/IEC 17043 requirement for complaints and appeals. 

---

# 10. Their reporting model

They publish historical reports online for 2010–2025 and state:

> All reports are in German with English summary. ([Umweltbundesamt][1])

For the gas PT exercise, they also state that results are published in a **non-anonymous form**, with reports downloadable from the website. ([Umweltbundesamt][2])

Important: this differs from their general PT scheme, where reports are described as aggregated and anonymized with randomly assigned lab codes. ([Umweltbundesamt][4])

## Practical implication

You need to decide your confidentiality model clearly.

For CALAIRE-EA in Colombia/LATAM, I recommend **anonymous coded results by default**, because that is safer commercially and easier for first participants to accept.

Possible policy:

| Result type                                | Default                                      |
| ------------------------------------------ | -------------------------------------------- |
| Individual participant report              | Identified only to that participant          |
| General final report                       | Coded/anonymized                             |
| Public report                              | Aggregated/anonymized only                   |
| Disclosure to regulator/accreditation body | Only if required and contractually disclosed |
| Non-anonymous publication                  | Only with explicit prior consent             |

Your 17043 document already requires participant identity confidentiality and rules for coding, access, publication, aggregated data, and prevention of indirect identification. 

---

# 11. Their registration/order artifact

Their order form is very useful as a minimum registration model. It asks for the number of desired PTs, the selected PT code, institution, department, VAT number, name, address, country, email, phone, contact person, invoice email, invoice address, notes, and privacy statement acceptance. ([Umweltbundesamt][5])

## Practical implication

Your registration form should include:

```text
Participant / institution data
- Organization
- Department
- Tax ID / NIT
- Contact person
- Technical contact
- Billing contact
- Address
- City / country
- Email
- Phone

PT selection
- Round code
- Components: CO / SO2 / NO / NO2 / O3
- Number of instruments/sites
- Method or instrument type
- Need invoice / purchase order?
- Notes

Legal
- Acceptance of terms and conditions
- Privacy/confidentiality acknowledgement
- Permission or refusal for non-anonymous publication
```

This is one of your urgent D artifacts.

---

# 12. Their general commercial terms

Their analytical services terms say orders must be written, preferably by email, and must include number of samples, parameters, customer-specific requirements, customer name/address, delivery/invoice address, VAT number if applicable, and email. Oral orders are not accepted. ([Umweltbundesamt][6])

They also reserve the right to reject orders if capacity is exceeded or if capacity is under-used, explicitly mentioning the **break-even point**. ([Umweltbundesamt][6])

## Practical implication

This is very important for your F model.

You need a clause like:

```text
The provider reserves the right to postpone, cancel, or modify a PT round if the minimum number of participants is not reached, if technical conditions cannot be guaranteed, or if the validity of the round may be compromised.
```

And in the quotation:

```text
Minimum number of participants required for the round: [N].
If the minimum number is not reached by the registration deadline, the provider may:
- postpone the round;
- cancel the round without penalty;
- offer the participant a custom-priced closed round.
```

This protects you commercially and technically.

---

# 13. Their general annual programme model

Their annual programme is a strong artifact to copy structurally. It includes:

| Element                 | Found in their programme                             |
| ----------------------- | ---------------------------------------------------- |
| Annual programme title  | “Proficiency Testing Scheme 2026”                    |
| Edition/date            | Edition 1: 10.11.2025                                |
| Why PT matters          | Technical competence / external QC                   |
| Standards               | EN ISO/IEC 17043, ISO 5725-2, ISO 13528              |
| Minimum participants    | Minimum 15 participants                              |
| Sample/result workflow  | Samples sent, results entered online                 |
| Deadline                | Usually 4–5 weeks after dispatch                     |
| Assigned value approach | Consensus / expert labs depending case               |
| Confidentiality rules   | Random lab code, consent for disclosure              |
| Complaints/objections   | 14-day procedure                                     |
| Accreditation statement | Accredited PT provider                               |
| How to participate      | Registration/billing instructions                    |
| Programme table         | PT code, matrix, analytes, dispatch, deadline, price |
| Shipping costs          | Separated from participation fee                     |

([Umweltbundesamt][4])

This maps almost perfectly to the service launch pack we already discussed. 

---

# 14. Shipping / logistics price model

For their environmental PT programme, they separate participation price from shipping. Their 2026 shipment costs are:

| Destination              | Shipping/packing cost |
| ------------------------ | --------------------: |
| Austria                  |                   €35 |
| Germany                  |                   €82 |
| EU countries             |                  €174 |
| Other European countries |                  €186 |

([Umweltbundesamt][3])

For the gas PT, since participants likely bring instruments to the facility, shipping is less central, but the general model is still useful.

## Practical implication for CALAIRE-EA

Use separate logistics lines:

| Fee type                    | Recommendation             |
| --------------------------- | -------------------------- |
| Participation fee           | Main PT service            |
| Instrument transport        | Participant responsibility |
| On-site/mobile round travel | Quoted separately          |
| Consumables/accessories     | Included or quoted         |
| Additional instrument       | Add-on fee                 |
| Closed round logistics      | Full pass-through + margin |

---

# 15. What to copy into your proposal

## D — Service artifacts to build from this benchmark

| Artifact                   | What Umweltbundesamt shows                                     | What CALAIRE-EA should create |
| -------------------------- | -------------------------------------------------------------- | ----------------------------- |
| Public PT page             | Purpose, target users, accreditation, gases, facility, contact | Webpage/brochure              |
| Next exercise page         | Date, requirements, ranges, evaluation, cost, cancellation     | Round announcement            |
| Annual programme           | Calendar, codes, prices, rules, complaint policy               | Annual PT programme PDF       |
| Order form                 | PT selection + participant/billing data                        | Registration form             |
| Complaint/objection policy | 14-day email process, independent review                       | Complaint/appeal procedure    |
| Reports archive            | Historic reports, public visibility                            | Dummy report + future archive |
| Accreditation links        | Confirmation/scope                                             | Accreditation status page     |
| Terms and conditions       | Written orders, pricing, capacity/break-even                   | Participant agreement         |

---

# 16. F — Commercial model to build from this benchmark

For your service, I would propose this structure:

## Core product

```text
CALAIRE-EA Gas PT Round
Components: CO, SO2, NO/NO2 [and O3 if ready]
Format: controlled atmosphere intercomparison / centralized or mobile
Includes:
- registration
- participant instructions
- controlled gas exposure / measurement window
- result submission
- statistical evaluation
- individual performance result
- final report
- participation statement
```

## Price architecture

| Item                        | Logic                                          |
| --------------------------- | ---------------------------------------------- |
| Full gas round              | Main package price                             |
| Additional instrument/site  | Add-on                                         |
| Institutional package       | Multiple instruments/sites                     |
| Interpretation meeting      | Add-on                                         |
| Closed round                | Custom quote                                   |
| Late cancellation           | Fee                                            |
| Non-accredited launch price | Introductory but not cheap                     |
| Accredited future price     | Higher price after ISO/IEC 17043 accreditation |

## Policy structure

| Policy                | Recommended                                            |
| --------------------- | ------------------------------------------------------ |
| Minimum participants  | Define N; maybe 8–15                                   |
| Registration deadline | 2–4 weeks before round                                 |
| Payment               | Before participation or against approved PO            |
| Cancellation          | Free until 7 days; 25% until 3 days; 100% under 3 days |
| Results deadline      | Fixed, no late data unless approved                    |
| Appeals               | 14 days after draft report                             |
| Confidentiality       | Anonymous by default                                   |
| Public report         | Aggregated/coded only unless consent                   |
| Capacity / break-even | Provider may postpone/cancel if minimum not reached    |

---

# 17. Most useful direct benchmark: price

The clearest number you now have is:

> **€1,655 excl. VAT** for participation in the gas PT for **O₃, SO₂, CO and NO/NO₂**, including evaluation and report. ([Umweltbundesamt][2])

I would not convert and copy it directly, but it is a powerful reference. It tells you your final accredited service can be positioned as a **premium technical competence service**, not a simple lab test.

For a Colombian pre-accreditation round, you could define:

```text
Price = full round cost / minimum participants × margin factor
```

Then compare it against the €1,655 benchmark as an international ceiling/reference.

---

# 18. My updated recommendation

Based on Umweltbundesamt, your next deliverable should be:

## “CALAIRE-EA Proficiency Testing Programme 2027”

A PDF or webpage with:

1. Purpose of the PT programme
2. Accreditation status
3. Target participants
4. Components and ranges
5. Measurement method requirements
6. Round date/location
7. Participation fee
8. What is included
9. Registration deadline
10. Minimum participants
11. Cancellation conditions
12. Evaluation criteria: z′ and optional En
13. Reporting and confidentiality policy
14. Complaints/appeals process
15. Contact and registration form

That single document will solve most of your D and F gap.

[1]: https://www.umweltbundesamt.at/en/pollutants/proftests-airpollutants "Accredited proficiency testing for Gaseous Air Pollutants"
[2]: https://www.umweltbundesamt.at/en/pollutants/proftests-airpollutants/rv-airpoll "Next intercomparison exercise"
[3]: https://www.umweltbundesamt.at/en/en-prof-tests-matrices "Proficiency testing scheme"
[4]: https://www.umweltbundesamt.at/fileadmin/site/angebot/analytik/ringversuche/proficiency_testing_scheme.pdf "Proficiency Testing Scheme"
[5]: https://www.umweltbundesamt.at/en/services/laboratory-services/interlaboratory-comparison/en-prof-tests-matrices/order-form-for-proficiency-testing-scheme "Order Form for Proficiency testing scheme"
[6]: https://www.umweltbundesamt.at/fileadmin/site/angebot/analytik/general_terms_and_conditions_for_analytical_services.pdf "General Terms and Conditions for Analytical Services"

