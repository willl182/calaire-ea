# Proficiency Testing Service

> **A sellable, repeatable PT service package**, not more technical design.

Based on two systems:

1. **A — Service artifacts:** everything the participant sees, signs, receives, or uses.
2. **B — Commercial model:** how you package, price, sell, invoice, and sustain the rounds.

You already have the pilot, so you can build this from real experience.

---

# A. Service artifacts you need

Think of this like a “PT service kit.” Minimum viable version:

## 1. Public service page / brochure

Purpose: explain what the scheme is, who it is for, what it gives, and why it matters.

Structure:

```text
Service name
PT scheme for [air quality / gases / pollutant / method]

Who should participate
Environmental laboratories, monitoring networks, calibration/testing organizations, etc.

Purpose
External evaluation of measurement performance using PT items and statistical evaluation under ISO/IEC 17043 and ISO 13528 principles.

What participants receive
- Participation confirmation
- Instructions
- PT item / round access
- Result submission form
- Individual performance evaluation
- Final report
- Certificate or participation statement, if applicable

Current status
Pilot completed. Accreditation under ISO/IEC 17043:2023 in process / planned / not yet accredited.

Frequency
Annual / semiannual / per demand

Confidentiality
Participant identities and individual results are coded and confidential.

Contact / registration
[form / email / website]
```

Important: unless you are already accredited, do **not** say “ISO/IEC 17043 accredited.” Say something like:

> “Designed under ISO/IEC 17043:2023 and ISO 13528 principles. Accreditation process under development.”

ONAC describes ISO/IEC 17043 accreditation as evaluation of competence and quality requirements for PT providers, so this distinction matters. ([ONAC][1])

---

## 2. Scheme catalogue

This is your “product menu.”

| Field                | Example                                                                      |
| -------------------- | ---------------------------------------------------------------------------- |
| Scheme code          | PEA-AQ-001                                                                   |
| Scheme name          | Air quality PT scheme                                                        |
| Matrix/item          | Gas mixture / generated atmosphere / digital dataset / instrument comparison |
| Measurands           | CO, NO, NO₂, SO₂, O₃, PM₂.₅, etc.                                            |
| Range                | Low / medium / high concentration                                            |
| Participants         | Laboratories / monitoring stations / networks                                |
| Frequency            | 1 or 2 rounds per year                                                       |
| Assigned value       | CRM, formulation, reference lab, consensus, etc.                             |
| Evaluation           | z-score, z′, zeta, En, % error                                               |
| Report               | Individual + global anonymized report                                        |
| Accreditation status | Pilot / non-accredited / accredited scope                                    |

Your ISO 13528 material already says the design must start from the objective, type of result, assigned value strategy, uncertainty, `sigma_pt`, score, participant number, and treatment of outliers/errors. 

---

## 3. Round announcement

This is what you send before each round.

Template:

```text
Proficiency Testing Round Announcement

Round code:
Round name:
Measurand(s):
Matrix / PT item:
Target range:
Registration deadline:
Expected item distribution date:
Result submission deadline:
Final report date:
Minimum participants:
Evaluation method:
Assigned value approach:
Fee:
Shipping / logistics:
Confidentiality:
Eligibility:
How to register:
Contact:
```

A public round calendar is common among PT providers. For example, Umweltbundesamt publishes a PT scheme document with round conditions, minimum participants, samples, and analysis/reporting structure. ([Umweltbundesamt][2])

---

## 4. Participant agreement / terms

This is a must. It protects you commercially and protects confidentiality.

Minimum clauses:

| Clause                       | Why                                  |
| ---------------------------- | ------------------------------------ |
| Scope of service             | Avoids unrealistic expectations      |
| Accreditation status         | Avoids false claims                  |
| Payment terms                | Defines when they pay                |
| Cancellation policy          | Protects round costs                 |
| Confidentiality              | Required by ISO/IEC 17043            |
| Participant code             | Protects identity                    |
| Deadlines                    | Controls late results                |
| Data use                     | Allows anonymous aggregate reporting |
| Report use                   | Prevents misleading marketing        |
| Appeals and complaints       | Required process                     |
| Force majeure / failed round | Protects you if item/logistics fail  |
| Liability limitation         | Important commercially               |

Your 17043 requirements include confidentiality, participant identity protection, communication, complaints, appeals, report control, and policies for report use. 

---

## 5. Participant guide

This is one of the most important artifacts. It should explain the entire journey.

Suggested sections:

```text
1. Purpose of the PT scheme
2. Who can participate
3. Round timeline
4. Confidentiality and participant coding
5. PT item handling / measurement instructions
6. Required method information
7. Units, decimals, significant figures
8. Result submission process
9. Treatment of late, corrected, or incomplete results
10. Statistical evaluation
11. Interpretation of scores
12. Reports and certificates
13. Complaints and appeals
14. Contact
```

Your own 17043 file says participants need detailed instructions on item handling, measurement, environmental conditions, reporting results/uncertainties, units, significant figures, method information, deadlines, and contacts. 

---

## 6. Result submission form

This should be strict. Most PT problems come from units, decimals, wrong method, wrong item, or late data.

Minimum fields:

| Field                    | Required?                         |
| ------------------------ | --------------------------------- |
| Participant code         | Yes                               |
| Round code               | Yes                               |
| Measurand                | Yes                               |
| Result                   | Yes                               |
| Unit                     | Yes                               |
| Expanded uncertainty     | Optional/required depending score |
| Coverage factor `k`      | If uncertainty required           |
| Method used              | Yes                               |
| Instrument/equipment     | Optional                          |
| Date/time of measurement | Yes                               |
| Environmental conditions | If relevant                       |
| Analyst / reviewer       | Optional/internal                 |
| Comments/deviations      | Yes                               |

For your app: make units dropdowns, not free text.

---

## 7. Final report template

This is the deliverable the customer actually pays for.

Minimum report structure:

```text
1. Cover
2. Identification of provider
3. Round code and report ID
4. Confidentiality statement
5. Objective and scope
6. Participants and coding
7. PT item description
8. Homogeneity/stability evidence or justification
9. Assigned value and uncertainty
10. Statistical design
11. Performance criteria
12. Participant results
13. Scores and interpretation
14. Graphs
15. Technical comments
16. Limitations
17. Conclusions
18. Authorization
19. End of report
20. Annexes
```

ISO/IEC 17043 requires reports to be clear, objective, complete, uniquely identified, authorized, and to include design, PT items, homogeneity/stability, statistical procedures, assigned values, uncertainty, performance criteria, participant results, interpretation, and comments where applicable. 

---

## 8. Certificate / participation statement

Be careful. There are two different things:

| Document                                  | Meaning                               |
| ----------------------------------------- | ------------------------------------- |
| **Certificate of participation**          | They participated                     |
| **Performance report**                    | Shows whether result was satisfactory |
| **Statement of satisfactory performance** | Only if their result meets criteria   |

Do not issue a “certificate of competence” unless your accreditation/legal framework supports it. Safer wording:

```text
This document confirms that [Participant Code / Organization] participated in round [code] of the [scheme name]. Performance evaluation is provided in the corresponding final report [report ID].
```

---

## 9. Complaints and appeals package

Minimum artifacts:

| Artifact                 | Purpose                             |
| ------------------------ | ----------------------------------- |
| Complaint form           | Service dissatisfaction             |
| Appeal form              | Challenge to performance evaluation |
| Internal review log      | Evidence                            |
| Decision letter template | Formal response                     |
| Closure record           | ISO evidence                        |

Your 17043 file distinguishes complaints from appeals and requires records, independent review, progress/result communication, and formal closure when possible. 

---

# B. Commercial model

Now the money part.

You need to decide four things:

1. **What do you sell?**
2. **How do you price it?**
3. **When do participants pay?**
4. **How many participants are needed for break-even?**

---

## 1. Recommended commercial offer

For your first real service after the pilot, I would not sell “custom consulting.” Sell **round participation**.

### Main product

| Product           | Description                            |
| ----------------- | -------------------------------------- |
| Standard PT round | One participant, one round, one report |

### Add-ons

| Add-on                           | Description                          |
| -------------------------------- | ------------------------------------ |
| Additional analyte               | Extra measurand in same round        |
| Additional instrument/site       | Same organization, extra station/lab |
| Late registration                | Higher fee after deadline            |
| Late result processing           | Only if technically acceptable       |
| Extra report copy                | Administrative fee                   |
| Technical interpretation session | Optional paid meeting                |
| Corrective action workshop       | Optional training/consulting         |
| Custom closed round              | Private round for one network/client |

---

## 2. Pricing models you can use

### Model 1 — Per participant per round

Simplest.

```text
Price = fixed fee per participant per round
```

Example:

| Item                       | Price |
| -------------------------- | ----: |
| One participant, one round | COP X |
| Additional measurand       | COP Y |
| Additional site/instrument | COP Z |

Best for: first commercial launch.

---

### Model 2 — Annual subscription

Better once you have recurring demand.

```text
Annual fee = access to 2 or 4 rounds per year
```

Example:

| Plan     | Includes                                             |
| -------- | ---------------------------------------------------- |
| Basic    | 1 round/year                                         |
| Standard | 2 rounds/year                                        |
| Premium  | 2 rounds + interpretation session + priority support |

Best for: monitoring networks, laboratories that need annual PT evidence.

---

### Model 3 — Institutional package

For organizations with multiple stations/labs.

```text
Base institutional fee + price per station/lab
```

Example:

| Component              | Price logic                               |
| ---------------------- | ----------------------------------------- |
| Base round fee         | Covers setup/report                       |
| Per station fee        | Covers additional participant code/result |
| Interpretation meeting | Optional                                  |

Best for: government networks, universities, environmental authorities.

---

### Model 4 — Custom closed round

Private PT/intercomparison for one client.

```text
Price = full project cost + margin
```

This should be much more expensive because you cannot spread costs across participants.

Best for: a monitoring network that wants internal comparison.

---

## 3. Real-world pricing signals

Public PT pricing is not always easy to find, but some examples show the pricing range is not “tiny.” One public ATG 2024 price list shows participation prices around **€470–€495** plus possible participant, packing, cancellation, and shipping-related fees. ([ATG][3]) Klasmeier publicly lists a proficiency test fee of **€1,365**, excluding some additional calibration costs. ([Klasmeier - Präzision in Temperatur][4])

Do **not** copy those prices directly into Colombia. But they prove an important point: PT is usually priced as a **specialized technical assurance service**, not as a cheap lab test.

---

## 4. Basic cost model

Use this formula:

```text
Total round cost =
technical cost
+ logistics cost
+ staff cost
+ software/data cost
+ quality/accreditation cost allocation
+ admin/commercial cost
+ contingency
```

Then:

```text
Minimum price per participant =
Total round cost / expected number of paying participants
```

Then add margin:

```text
Commercial price =
Minimum price per participant × 1.25 to 1.60
```

For early rounds, I would use a margin target of **25–40%**, unless the technical/logistics risk is high.

---

## 5. Your break-even table

Make this for each round.

| Cost item                               | Estimate |
| --------------------------------------- | -------: |
| PT item preparation                     |      COP |
| Reference material / gas / consumables  |      COP |
| Homogeneity/stability checks            |      COP |
| Packaging/shipping/logistics            |      COP |
| Technical staff hours                   |      COP |
| Statistical analysis hours              |      COP |
| Report preparation/review               |      COP |
| Software/app maintenance                |      COP |
| Admin/invoicing/support                 |      COP |
| Quality system/accreditation allocation |      COP |
| Contingency 10–20%                      |      COP |
| **Total round cost**                    |  **COP** |

Then simulate:

| Participants | Required price to break even |
| -----------: | ---------------------------: |
|            5 |                    Total / 5 |
|            8 |                    Total / 8 |
|           10 |                   Total / 10 |
|           15 |                   Total / 15 |
|           20 |                   Total / 20 |

This immediately tells you your **minimum viable participant count**.

---

## 6. Pricing structure I recommend for you

For first real launch after pilot:

### Public non-accredited / pre-accreditation round

| Item                                             | Pricing logic        |
| ------------------------------------------------ | -------------------- |
| Early registration                               | Base price           |
| Regular registration                             | Base price + 10–20%  |
| Additional pollutant/analyte                     | 30–60% of base price |
| Additional station/instrument                    | 40–70% of base price |
| Technical interpretation meeting                 | Fixed add-on         |
| Late correction/reissue due to participant error | Administrative fee   |
| Custom closed round                              | Quoted separately    |

Suggested structure:

```text
Base round participation:
COP [X]

Includes:
- Participant registration
- PT item / round access
- Result submission
- Statistical evaluation
- Individual coded result
- Final report
- Participation statement

Does not include:
- Shipping outside defined area
- Extra instruments/sites
- Corrective-action consulting
- Reissue due to participant error
- Custom analysis not planned in the round
```

---

## 7. Payment policy

Use this:

| Moment                                       | Rule                                                |
| -------------------------------------------- | --------------------------------------------------- |
| Registration                                 | Participant submits form                            |
| Confirmation                                 | You confirm only after payment or purchase order    |
| Before shipment/access                       | Payment must be completed                           |
| Cancellation before round starts             | Partial refund or admin fee                         |
| Cancellation after item preparation/shipment | No refund or limited refund                         |
| Late result                                  | May be included in report only if technically valid |
| Report release                               | Only to paid participants                           |

The ATG price list example explicitly separates participation, shipping/packing, and cancellation-related fees, which is a useful model to copy structurally, not necessarily in amount. ([ATG][3])

---

## 8. Three commercial packages

You can present it like this:

| Package           | For whom                   | Includes                                                     |
| ----------------- | -------------------------- | ------------------------------------------------------------ |
| **Essential**     | Lab only needs PT evidence | Participation + final report                                 |
| **Professional**  | Lab wants interpretation   | Essential + technical interpretation session                 |
| **Institutional** | Network/multiple stations  | Multiple participant codes + consolidated management summary |

Example:

```text
Essential
- One participant code
- One round
- Final report
- Participation statement

Professional
- Everything in Essential
- 60-minute technical interpretation meeting
- Corrective-action orientation note

Institutional
- Multiple participant codes
- Consolidated anonymous summary
- Management presentation
- Optional trend analysis across rounds
```

This is better than only having one price, because some clients only want compliance evidence, while others want help understanding performance.

---

# The exact artifacts I would create first

Do these in this order:

## Week 1 / Sprint 1

1. **PT service one-pager**
2. **Scheme catalogue**
3. **Round announcement**
4. **Pricing sheet**
5. **Registration form**

## Week 2 / Sprint 2

6. **Participant agreement**
7. **Participant guide**
8. **Result submission template**
9. **Complaint/appeal forms**
10. **Dummy final report**

## Week 3 / Sprint 3

11. **Internal round cost calculator**
12. **Break-even model**
13. **Sales email**
14. **FAQ**
15. **Post-round feedback form**

---

# Minimal pricing calculator

Use this structure:

```text
A. Fixed round costs
Technical planning:
PT item preparation:
Homogeneity/stability:
Statistical setup:
Report template/review:
Admin/commercial:
Quality/accreditation allocation:
Software/app allocation:
Contingency:

Total fixed cost:

B. Variable cost per participant
Item/unit cost:
Shipping:
Support/admin:
Data processing:
Certificate/report handling:

Variable cost per participant:

C. Formula
Total cost = fixed cost + variable cost × participants

Price per participant = total cost / participants × margin factor
```

Margin factor examples:

| Strategy               |    Factor |
| ---------------------- | --------: |
| Pilot recovery         | 1.10–1.20 |
| Sustainable service    | 1.30–1.50 |
| High-risk/custom round | 1.60–2.00 |

---

# My recommended starting point

Since you already did a pilot, your next move should be:

> **Launch one paid “pre-accreditation” round with a limited number of participants, using full ISO/IEC 17043-style documentation, but without claiming accreditation.**

Commercially:

```text
Offer:
One PT round + final report + participation statement.

Target:
8–15 participants.

Pricing:
Base price calculated from break-even at 8 participants.
If more than 8 join, margin improves.
If fewer than minimum join, postpone or convert to custom priced round.

Payment:
100% before round start or purchase order before item preparation.

Add-ons:
Interpretation session and extra participant/site.
```

The key rule: **do not price based on what feels “cheap enough.” Price from the round cost and minimum viable participant count.**

Your A and B are basically these two deliverables now:

1. **PT Service Launch Pack** — brochure, guide, registration, agreement, report template.
2. **PT Commercial Workbook** — cost model, break-even, pricing table, packages, cancellation rules.

[1]: https://onac.org.co/en/services/proficiency-testing-providers/?utm_source=chatgpt.com "Proficiency Testing Provider Accreditation"
[2]: https://www.umweltbundesamt.at/fileadmin/site/angebot/analytik/ringversuche/proficiency_testing_scheme.pdf?utm_source=chatgpt.com "Proficiency Testing Scheme 2026"
[3]: https://en.atg.cz/wp-content/uploads/2024/01/Proficiency-Testing-Pricelist-2024.pdf?utm_source=chatgpt.com "PROFICIENCY TESTING PRICELIST 2024"
[4]: https://www.klasmeier.com/en/eignungspruefung-temperatur/?utm_source=chatgpt.com "Proficiency Testing"

