# CS-04 — Price Model and Approved Price List

**Status:** PLANNED — RESTRICTED ACCESS  
**Owner:** Finance / commercial  
**Required before:** Quotation  
**Last revision:** 2026-07-14 (added round-use factor, closed-institutional tab, exchange-rate policy, cash flow, package variants 2/3/4 gases, benchmark derivation)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md`. Los códigos PSEA / F-PSEA referenciados en este modelo apuntan a los significados vigentes post-renumeración 2026-06-14.

## Purpose

Validate the provisional flat round fee, calculate real costs and viability, and
support a future price revision without assuming gas- or analyzer-based billing.

## Pricing architecture

```text
Participant price = flat round fee per participating organization
                  for one to four selected blocks
```

The proposal uses **COP 5.928.000 excluding taxes per participating
organization**, whether it selects one to four blocks: CO, SO₂, O₃ and NO/NO₂.
The amount is an indicative conversion of EUR 1.600, not an approved price and
not a substitute for the cost model. It includes up to one analyzer per block;
one additional analyzer may be accepted without surcharge only when residual
capacity exists.

## Workbook tabs

The actual cost model should be implemented as a spreadsheet with the following tabs. This document defines the required content for each tab.

### Tab 1 — Assumptions

| Assumption | Value | Source / owner |
|---|---|---|
| Reference exchange rate | TRM USD/COP × referencia BCE USD/EUR, solo para convertir benchmarks | CS-01 |
| Exchange-rate refresh frequency | En la fecha de revisión del benchmark | CS-01 |
| FX risk allocation | No aplica a clientes: cotización y facturación únicamente en COP | CS-01 |
| Capacity per gas (individual) | 4 analyzers | CS-01 |
| Capacity simultaneous CO/SO₂ | 3 participants, 6 analyzers | CS-01 |
| Expected enrollment | [FILL] | Market estimate |
| Taxes (IVA, withholding, etc.) | [FILL] | Tax advisor |
| Tax differential for international clients | [FILL — IVA exento, withholding, treaty application] | Tax advisor |
| Target margin / objective | Lanzamiento y validación; sin margen ni subsidio comprometidos; no cotizar bajo costo directo | CS-01 |
| Round-use factor for lifecycle allocation | [FILL — fracción entre 0 y 1] | Technical manager (basado en historial de uso) |
| Payment collection timing (default) | [FILL — e.g., 100% anticipado / 50% orden + 50% pre-round / PO a 30 días] | Política financiera |
| Payment collection timing (institutional) | [FILL] | Política financiera |

### Tab 2 — Common cost

| Cost item | Annual amount | Round allocation | Notes |
|---|---|---|---|
| Coordination | [FILL] | [FILL] | |
| Facility setup | [FILL] | [FILL] | |
| Registration and data administration | [FILL] | [FILL] | |
| Report delivery | [FILL] | [FILL] | |
| Shared equipment (calibrator, zero-air generator) | [FILL] | [FILL] | From Tab 4 |

### Tab 3 — Gas cost

| Block | Cylinder / generation cost | Analyzer-specific lifecycle | Cost allocation | Notes |
|---|---|---|---|---|
| CO | [FILL] | [FILL] | [CALC] | |
| SO₂ | [FILL] | [FILL] | [CALC] | |
| NO/NO₂ | [FILL] | [FILL] | [CALC] | Un solo bloque NOx |
| O₃ | [FILL] | [FILL] | [CALC] | |

### Tab 4 — Equipment lifecycle

Annual provision for all identified CALAIRE equipment:

| Asset | Planned maintenance | Consumables | Calibration / service | Risk-based corrective repair provision | Total annual provision | **Round-use factor** | **Round allocation** |
|---|---|---|---|---|---|---|---|
| O₃ analyzer / reference system | [FILL] | [FILL] | [FILL] | [FILL] | [CALC] | [FILL — 0–1] | [CALC] |
| SO₂ analyzer | [FILL] | [FILL] | [FILL] | [FILL] | [CALC] | [FILL — 0–1] | [CALC] |
| CO analyzer | [FILL] | [FILL] | [FILL] | [FILL] | [CALC] | [FILL — 0–1] | [CALC] |
| NOx analyzer | [FILL] | [FILL] | [FILL] | [FILL] | [CALC] | [FILL — 0–1] | [CALC] |
| Dynamic calibrator | [FILL] | [FILL] | [FILL] | [FILL] | [CALC] | [FILL — 0–1] | [CALC] |
| Zero-air generator | [FILL] | [FILL] | [FILL] | [FILL] | [CALC] | [FILL — 0–1] | [CALC] |

**Round-use factor (RUF):** fracción del año de uso intensivo del equipo atribuible a un round típico. Se estima a partir del historial de campañas (horas de uso / horas totales disponibles) o, en su defecto, a partir del plan de mantenimiento del fabricante. Sin este factor, la asignación por round no se puede calcular.

**Fórmula:**

```text
Annual lifecycle provision
    = planned maintenance + consumables + calibration/service
    + risk-based corrective repair provision

Round allocation
    = annual lifecycle provision × round-use factor (RUF)
```

Exact parts and intervals must come from installed equipment models, manufacturer schedules, service quotations or maintenance history.

### Tab 5 — Cylinder strategy

Compare multi-component mixture, individual cylinders and hybrid options:

| Criterion | Multi-component mixture | Individual cylinders | Hybrid (if applicable) |
|---|---|---|---|
| Procurement | Fewer orders / cylinders | Several orders / cylinders | [FILL] |
| Concentrations | One spec must suit all dilutions | Optimized per gas | [FILL] |
| Stability / compatibility | Must be certifiably stable | Managed separately | [FILL] |
| Traceability | One certificate, component values | Separate certificates | [FILL] |
| Package costing | Harder to allocate to single-gas sales | Maps directly to gas package | [FILL] |
| Failure / expiry | One issue may affect several gases | Isolated to one gas | [FILL] |
| Hardware / storage | Fewer regulators / connections | More regulators, storage, handling | [FILL] |
| Lead time | Custom-mixture availability | Varies by gas | [FILL] |
| Estimated cost per round (COP / EUR) | [FILL] | [FILL] | [FILL] |
| **Recommendation** | [FILL] | [FILL] | [FILL] |

**Approved strategy:** [FILL]  
**Technical approver:** [FILL]  
**Commercial/finance approver:** [FILL]

### Tab 6 — Flat participation fee

| Selected blocks | Included analyzers | Provisional fee excl. taxes | Additional analyzer with residual capacity | Notes |
|---|---:|---:|---:|---|
| Any 1 block | Up to 1 | COP 5.928.000 | COP 0 | Proposal only |
| Any 2 blocks | Up to 2, one per block | COP 5.928.000 | COP 0 | Proposal only |
| Any 3 blocks | Up to 3, one per block | COP 5.928.000 | COP 0 | Proposal only |
| All 4 blocks | Up to 4, one per block | COP 5.928.000 | COP 0 | CO, SO₂, O₃ and NO/NO₂ |

An additional analyzer never displaces another organization's first position
and requires CS-09 capacity review.

### Tab 6.A — Benchmark validation

This tab compares the real direct and full cost per participating organization
against COP 5.928.000. It must show cost separately for each selected-block
scenario even though the proposed customer price is flat.

| Measure | Value (COP) | Source / calculation |
|---|---:|---|
| Direct cost, 1 block | [CALC] | Tabs 2–4 |
| Direct cost, 2 blocks | [CALC] | Tabs 2–4 |
| Direct cost, 3 blocks | [CALC] | Tabs 2–4 |
| Direct cost, 4 blocks | [CALC] | Tabs 2–4 |
| Full allocated cost, 4 blocks | [CALC] | Tabs 2–4 |
| Provisional flat fee | 5.928.000 | CS-01 |
| Contribution / shortfall by scenario | [CALC] | fee − cost |
| **Interpretation / decision** | [FILL] | management approval before quotation |

### Tab 7 — Enrollment

| Scenario | Participants | Analyzers | Revenue | Costs | Contribution | Cash inflow timing | Viable? |
|---|---|---|---|---|---|---|---|
| Low (1 participant, 1 gas) | 1 | 1 | [CALC] | [CALC] | [CALC] | [FILL] | [FILL] |
| Expected | [FILL] | [FILL] | [CALC] | [CALC] | [CALC] | [FILL] | [FILL] |
| Full capacity individual gas | 4 | 4 | [CALC] | [CALC] | [CALC] | [FILL] | [FILL] |
| Full simultaneous CO/SO₂ | 3 | 6 | [CALC] | [CALC] | [CALC] | [FILL] | [FILL] |
| Mixed selection | [FILL] | [FILL] | [CALC] | [CALC] | [CALC] | [FILL] | [FILL] |

**Cash inflow timing:** columna crítica para entender la viabilidad real. Si el ingreso se cobra 100% anticipado y los costos se pagan durante el round, la viabilidad operativa es muy distinta a un escenario de pago a 30 días. CS-06 sección 9 y CS-10 columna "PO/payment/invoice status" usan esta misma escala temporal.

### Tab 8 — Scenarios

| Scenario | Description | Result |
|---|---|---|
| Break-even individual gas | Minimum paid positions to cover cost | [CALC] |
| Break-even simultaneous CO/SO₂ | Minimum paid positions to cover cost | [CALC] |
| Break-even complete package | Minimum paid positions to cover cost | [CALC] |
| Low capacity | 1–2 participants | [CALC] |
| Expected capacity | [FILL] | [CALC] |
| Full capacity | Per CS-01 limits | [CALC] |
| Worst-case cash flow (low enrollment + late payment) | Tensión de caja | [CALC] |

### Tab 9 — Approval

| Field | Value |
|---|---|
| Approved flat participation fee | [FILL] |
| Approved selected-block adjustment | COP 0 unless CS-01 is revised |
| Approved additional-analyzer fee | COP 0 during proposal stage, subject to residual capacity |
| Approved cylinder strategy (from Tab 5) | [FILL] |
| Approved packages (from Tab 6) | [FILL] |
| Approved exchange-rate policy (from Tab 1) | [FILL] |
| Approved cash collection timing (from Tab 1) | [FILL] |
| Approved prices valid from | [FILL] |
| Approved prices valid until | [FILL] |
| Approver (commercial/finance) | [FILL NAME, DATE, SIGNATURE] |
| Approver (technical) | [FILL NAME, DATE, SIGNATURE] |
| Approver (management) | [FILL NAME, DATE, SIGNATURE] |

### Tab 10 — Closed institutional round (full-cost quotation)

Esta pestaña cubre rondas dedicadas a un solo sponsor o un grupo cerrado de participantes que requieren cotización full-cost (blueprint 8.6). Se estructura distinto a la lista pública: no hay paquetes estándar, todo se calcula bottom-up.

| Item | Cálculo |
|---|---|
| Sponsor identification | [FILL] |
| Round scope (gases, configuration, capacity reserved) | [FILL] |
| Common cost (Tab 2 round allocation × 1 round) | [CALC] |
| Gas-specific cost (Tab 3 × number of analyzers reserved) | [CALC] |
| Equipment lifecycle (Tab 4 round allocation × reserved hours) | [CALC] |
| Exclusive use premium (capacity not shared with public round) | [FILL] |
| Custom requirements (extra reports, custom language, dedicated facility days) | [FILL] |
| Travel / on-site support (if sponsor requires CALAIRE staff) | [FILL] |
| Subtotal cost | [CALC] |
| Markup (according to pricing objective) | [FILL] |
| Indicative institutional price (excl. taxes) | [CALC] |
| Payment terms (typically 50% order + 50% pre-round for institutional) | [FILL] |
| Sponsor approval signature | [FILL] |
| Internal approval (commercial/finance + management) | [FILL] |

**Reglas de Tab 10:**

- No usar precios de lista pública; todo es cost-plus.
- El "exclusive use premium" es obligatorio: el sponsor paga por la capacidad que no se ofrece a otros clientes.
- Requiere doble aprobación (commercial/finance + management) por el tamaño relativo.
- El sponsor typically paga ≥ 50% al confirmar la orden; CS-06 variante "Institutional/closed" lo refleja.

## Customer-facing price list

The external list (see `approved_price_lists.md`) shows only approved prices, currency, taxes, inclusions, additional-analyzer fee, validity and quotation requirement. Internal cost and margin details remain restricted.

## Commercial logic checks

- [ ] The flat fee is shown consistently for one to four selected blocks.
- [ ] An additional analyzer is accepted only with residual capacity and does not displace a first position.
- [ ] Closed institutional rounds require a separate full-cost quotation (Tab 10).
- [ ] The proposal objective and direct-cost floor from CS-01 are documented.
- [ ] The COP 5.928.000 benchmark is tested against verified capacity, not an assumed 8–15 participant round.
- [ ] Round-use factor is populated for every asset in Tab 4.
- [ ] Tab 6.A shows direct and full-cost contribution or shortfall for every selected-block scenario.
- [ ] Cash inflow timing in Tab 7 reflects the payment policy from CS-01 / CS-06.

## Approval

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial structure from CS-01 |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added round-use factor, Tab 6.A benchmark derivation, Tab 10 closed-institutional, exchange-rate policy, cash flow column, 2/3/4-gas package rows. |
