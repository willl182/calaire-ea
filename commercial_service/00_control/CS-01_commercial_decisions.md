# CS-01 — Commercial Decision Sheet

**Status:** 0.3 — proposal decisions approved; release gates pending  
**Owner:** Service manager  
**Next review:** al completar costos, validación técnica y revisión jurídica  
**Last revision:** 2026-07-14 (institutional decision interview and proposal approval)  
**QMS code reference:** ver `00_control/qms_code_equivalence.md` para mapeo de códigos PSEA / F-PSEA / I-PSEA / DG-PSEA tras la renumeración del 2026-06-14.

## Purpose

Single source of truth for scope, price, conditions and claims. Prevents contradictions among brochure, quote, registration form, terms and customer emails.

## 1. Service identity

| Field | Approved value | Evidence / input source |
|---|---|---|
| Service name | Ensayos de Aptitud para Gases Contaminantes Criterio | decisión institucional del 2026-07-14 |
| Provider legal identity | Universidad Nacional de Colombia, NIT 899.999.063-3, Sede Medellín | confirmación institucional del 2026-07-14; documentos oficiales de contratación UNAL |
| Executing unit | Facultad de Minas, Laboratorio CALAIRE | confirmación institucional del 2026-07-14 |
| Service owner / service manager | Carmen Elena Zapata | Coordinadora EA; confirmación institucional del 2026-07-14 |
| Commercial lead | David Pulgarin | Profesional de Proyectos; confirmación institucional del 2026-07-14 |
| Round coordinator | Carmen Elena Zapata | Coordinadora EA; confirmación institucional del 2026-07-14 |
| Quality / QMS owner | Jeniffer Ochoa | Profesional de Gestión de Calidad; confirmación institucional del 2026-07-14 |
| Complaint contact | David Pulgarin — `calaire_med@unal.edu.co` (recepción y registro); Jeniffer Ochoa (clasificación y supervisión SGC) | decisión institucional del 2026-07-14; `P-PSEA-17` |
| Working language of the service (commercial interface) | Español | decisión institucional del 2026-07-14 |
| Service publication languages (catalogue, EoI, terms) | Español | decisión institucional del 2026-07-14; ver CS-02 sección 12 y CS-08 cláusula 18 |

### Assigned operating team

| Role | Assigned person |
|---|---|
| Coordinadora EA | Carmen Elena Zapata |
| Profesional de Calidad del Aire | Wilson Salas |
| Profesional de Proyectos | David Pulgarin |
| Profesional de Infraestructura | Maira Herrera |
| Ingeniero Operativo | Fabian Moreno |
| Profesional de Gestión de Calidad | Jeniffer Ochoa |

## 2. Selectable scope and packages

| Gas | Reporting units | Individual-gas capacity |
|---|---|---|
| CO | µmol/mol | 4 participant analyzers |
| SO₂ | nmol/mol | 4 participant analyzers |
| NO | nmol/mol | 4 participant analyzers |
| NO₂ | nmol/mol | 4 participant analyzers |
| O₃ | nmol/mol | 4 participant analyzers |

**Package definitions**

- Single-block participation: one of CO, SO₂, O₃ or NO/NO₂.
- Multi-block participation: two or three selected blocks.
- Complete participation: all four blocks (CO, SO₂, O₃ and NO/NO₂).
- Closed institutional package: dedicated round for a single sponsor; full-cost quotation outside the public price list (ver CS-04 Tab 10).

**Standard participation unit:** una organización registrada bajo un código de
participante, con derecho a inscribir hasta un analizador por cada bloque
contratado. La participación completa puede comprender hasta cuatro
analizadores: uno para CO, uno para SO₂, uno para O₃ y uno para el bloque
NO/NO₂. Cada analizador consume un cupo operativo en su bloque, pero el precio
no se calcula por analizador.

**Additional analyzer in the same block:** puede admitirse si queda capacidad
residual después de asignar un cupo primario a cada organización elegible. No
es excluyente, pero requiere revisión de capacidad en CS-09 y no puede desplazar
a otra organización de su primer cupo en ese bloque. Su tratamiento de precio
es provisionalmente sin recargo durante la etapa de propuesta; puede revisarse
cuando CS-04 disponga de costos y evidencia operativa.

## 3. Price anchor and objective

| Item | Approved value | Evidence / input source |
|---|---|---|
| Round benchmark (excl. taxes) | Aproximadamente COP 5.928.000 por organización participante, tanto para uno como para los cuatro bloques de gases; incluye hasta un analizador por bloque y no es un precio aprobado | conversión indicativa del benchmark de EUR 1.600 al 2026-07-14: TRM COP 3.248,87/USD × referencia BCE 1,1404 USD/EUR; cost buildup en CS-04 antes de aprobar |
| Pricing objective | Propuesta para lanzamiento y validación comercial; sin meta de margen ni subsidio comprometido. Antes de emitir una oferta real, el precio no debe quedar por debajo del costo directo de ejecución calculado en CS-04. | decisión institucional del 2026-07-14; referencia blueprint 8.6 |
| Invoicing currency | COP | decisión institucional del 2026-07-14 |
| Exchange-rate method | Para convertir referencias en EUR: tasa cruzada formada con la TRM USD/COP certificada por la Superintendencia Financiera y la referencia EUR/USD del BCE vigentes o más recientes disponibles en la fecha del cálculo. | decisión institucional del 2026-07-14 |
| Currency policy (invoicing ≠ costing) | Cotización y facturación únicamente en COP. El valor queda fijo en COP durante la vigencia de la cotización; referencias en moneda extranjera no constituyen precio ofrecido. | decisión institucional del 2026-07-14 |
| Taxes | Precio expresado antes de impuestos. Los impuestos y retenciones aplicables serán determinados por la Universidad Nacional de Colombia al emitir cada cotización. No se presume una tarifa hasta validación financiera institucional. | decisión institucional del 2026-07-14; validación financiera requerida antes de cotizar |
| Quotation validity | 30 días calendario desde su emisión, sin exceder la fecha límite de inscripción ni quedar vigente dentro de los 15 días anteriores al inicio de la ronda | decisión institucional del 2026-07-14; ver CS-06 sección 1 |
| Acceptance deadline (after which offer is withdrawn) | La primera fecha entre: vencimiento de los 30 días, fecha límite de inscripción, 15 días antes del inicio de la ronda o agotamiento de la capacidad aplicable | decisión institucional del 2026-07-14 |
| Package price rule | Tarifa plana provisional por organización participante: el mismo valor para seleccionar entre uno y cuatro bloques. Los bloques son CO, SO₂, O₃ y NO/NO₂. | decisión institucional del 2026-07-14; modelo de referencia UBA |

**Currency policy** (sub-sección a documentar antes de aprobar):

- Si la moneda de facturación es distinta a la moneda de costo, documentar: tipo de cambio de referencia, frecuencia de actualización, quién autoriza revaluaciones, y si el riesgo cambiario lo asume CALAIRE-EA o el cliente.
- CS-04 Tab 1 (Assumptions) debe referenciar la misma política.

**Architecture**

```text
Participant price = flat round fee per participating organization
                  for one to four selected gas blocks
```

- La tarifa provisional no cambia entre uno y cuatro bloques seleccionados.
- El bloque NO/NO₂ se contrata y opera como una sola unidad con un analizador NOx.
- La tarifa incluye hasta un analizador por bloque contratado.
- Closed institutional rounds require a separate full-cost quotation (CS-04 Tab 10).

## 4. Capacity limits

| Configuration | Current commercial planning limit |
|---|---|
| Gas operated individually | 4 participants / analyzers |
| CO and SO₂ operated simultaneously | 3 participants, up to 2 analyzers each; 6 participant analyzers total |

Capacity is reserved by analyzer and configuration, not only by organization.
Estos valores son límites provisionales de planificación y deben validarse
antes de abrir inscripciones mediante evidencia de conexiones, caudal y margen
de exceso, contrapresión, espacio físico y eléctrico, adquisición de datos y
capacidad de supervisión.

**Capacity verification gate:** before accepting an order, CS-09 check #4 must confirm that the order stays within these limits and that residual capacity after the order is at least 0. Si un pedido consume el último cupo, el siguiente debe ir a wait-list (CS-10) con la regla de prioridad documentada.

## 5. Lifecycle-cost allocation

Approved annual provision to be recovered through round fees:

| Asset | Cost categories included | Allocation method |
|---|---|---|
| O₃ analyzer / reference system | Preventive maintenance, lamps, scrubbers, filters, repairs, spares | Gas-specific |
| SO₂ analyzer | Preventive maintenance, lamps, filters, pumps, repairs, spares | Gas-specific |
| CO analyzer | Preventive maintenance, filters, pumps, repairs, spares | Gas-specific |
| NOx analyzer | Preventive maintenance, converter, ozonator, pumps, filters, repairs, spares | Gas-specific |
| Dynamic calibrator | Calibration, MFC service, seals, valves, maintenance, repair | Common fee or usage hours |
| Zero-air generator | Catalyst / scrubber / filter replacement, compressor / pump service, repair | Common fee or usage hours |

**Round allocation formula**

```text
Annual lifecycle provision
    = planned maintenance + consumables + calibration/service
    + risk-based corrective repair provision

Round allocation
    = annual lifecycle provision × documented round-use factor
```

El **round-use factor** (fracción del año de uso intensivo del equipo atribuible a un round típico) debe documentarse en CS-04 Tab 4 columna "Round-use factor" con su evidencia (historial de uso, campañas anteriores, plan de mantenimiento). Sin este factor la asignación por round no se puede calcular.

Exact parts and intervals must come from installed equipment models, manufacturer schedules, service quotations or maintenance history.

**Evidence owners:** Maira Herrera levanta inventario, modelo, serie y estado;
Fabian Moreno identifica repuestos, consumibles, mantenimiento e intervalos;
David Pulgarin obtiene cotizaciones y costos; Wilson Salas valida la pertinencia
técnica; Carmen Elena Zapata aprueba su incorporación al modelo CS-04.

## 6. Certified-gas cylinder strategy

| Criterion | Multi-component mixture | Individual cylinders | Hybrid |
|---|---|---|---|
| Procurement | Fewer orders / cylinders | Several orders / cylinders | Use existing mixture for launch; compare replacement options before purchase |
| Concentrations | One spec for all dilutions | Optimized per gas | Existing CO/SO₂/NOx specification must be checked against planned levels |
| Stability / compatibility | Must be certifiably stable | Managed separately | Mixture accepted only with valid component-specific stability evidence |
| Traceability | One certificate, component values | Separate certificates | Existing certificate must state values and uncertainties for CO, SO₂ and NOx |
| Package costing | Harder to allocate to single-gas sales | Maps directly to gas package | Flat round fee makes shared allocation acceptable for the proposal |
| Failure / expiry | One issue may affect several gases | Isolated to one gas | Replacement comparison must price the correlated failure/expiry risk |
| Hardware / storage | Fewer regulators / connections | More regulators, storage, handling | Existing configuration favors the mixture if technically suitable |
| Lead time | Custom-mixture availability | Varies by gas | Obtain comparable supplier lead times before replacement approval |
| Estimated cost per round (COP / EUR) | [FILL — from CS-04 Tab 5] | [FILL] | [FILL] |

**Approved strategy:** mezcla multicomponente CO/SO₂/NOx como referencia
provisional para el lanzamiento, usando el cilindro existente solo si su
certificado, vigencia, concentraciones, incertidumbres y estabilidad son
adecuados. O₃ se genera fotométricamente. Antes de reponer inventario, CS-04
debe comparar una nueva mezcla equivalente contra cilindros individuales.  
**Technical approver:** Carmen Elena Zapata, con concepto técnico de Wilson Salas  
**Commercial/finance approver:** pendiente de aprobación institucional sobre la comparación de costos

**Hybrid scope note:** la columna "Hybrid" de esta tabla y de CS-04 Tab 5 es la única que admite combinaciones documentadas (p. ej., mezcla certificada compatible + cilindro individual para un gas que requiere concentración o estabilidad distinta). Sin documentación explícita no se aprueba strategy "hybrid" en CS-01.

## 7. Enrollment and confirmation rules

| Rule | Approved value | Evidence / input source |
|---|---|---|
| Minimum enrollment (participants) | 1 organización confirmada como mínimo operativo provisional | decisión institucional del 2026-07-14; técnicamente compatible con la regla de valor asignado para menos de 12 resultados |
| Minimum enrollment (revenue threshold) | Pendiente de CS-04. Antes de publicar una ronda pagada, la Universidad debe decidir expresamente si ejecuta cuando el ingreso confirmado no cubre el costo directo. | análisis de viabilidad CS-04 |
| Maximum enrollment | Constrained by capacity limits above | sección 4 |
| Confirmation condition | Scope/capacity review AND accepted payment or purchase order | CS-09, CS-10 |
| Payment / PO deadline after registration | 15 días calendario por defecto, sin exceder el cierre de inscripción. Prevalecen las políticas financieras y contractuales vigentes de la Universidad Nacional de Colombia; cualquier plazo distinto debe constar en la cotización. Al vencer sin pago ni orden aceptable, el cupo se libera y la solicitud requiere nueva revisión. | decisión institucional del 2026-07-14; CS-10 columna "Payment deadline" |
| Wait-list priority criteria | Primero, solicitudes completas y elegibles de laboratorios acreditados, en estricto orden de fecha y hora de completitud. Después, las demás organizaciones elegibles, también por orden de completitud. La expresión de interés no reserva prioridad. | decisión institucional del 2026-07-14; CS-10 sección "Wait-list" |
| Partial payment policy | Se rige exclusivamente por las políticas financieras y contractuales vigentes de la Universidad Nacional de Colombia. La cotización debe indicar la modalidad autorizada y CS-09 debe verificar su cumplimiento antes de confirmar el cupo. | decisión institucional del 2026-07-14; CS-06 y CS-09 |

## 8. Cancellation and postponement

| Scenario | Rule | Fee / refund | Reference |
|---|---|---|---|
| Participant withdrawal ≥ 30 días calendario before round start | El participante puede solicitar una única reprogramación, sujeta a capacidad, o cancelar. | Si cancela, devolución de lo pagado menos únicamente costos directos no recuperables, ya incurridos, documentados y permitidos por las políticas de la Universidad. Sin penalidad porcentual genérica. | CS-12 |
| Participant withdrawal < 30 días calendario before round start | El participante puede solicitar una única reprogramación, sujeta a capacidad y al pago de costos incrementales documentados. | No hay devolución automática. Si no se reprograma, solo se reconoce el saldo recuperable que determinen los costos efectivamente comprometidos y las políticas financieras de la Universidad. | CS-12 |
| Participant no-show | La inasistencia sin aviso no genera reprogramación automática. Solo puede evaluarse una excepción por fuerza mayor demostrada y registrada. | Sin devolución, salvo decisión excepcional permitida por las políticas de la Universidad y documentada en CS-12. | CS-12 |
| Participant substitution (analyzer or organization) | Cambio de analizador dentro de la misma organización: permitido hasta 15 días antes del inicio, sujeto a nueva revisión técnica y sin cambiar gases ni capacidad. Cambio de organización: requiere nuevo registro, aceptación de términos y revisión CS-09; el cupo solo se conserva si la nueva organización completa la aceptación dentro del plazo. | Sin tarifa administrativa genérica; se cobran únicamente costos adicionales documentados y permitidos por la Universidad. | CS-08 cláusula 8 |
| Provider postponement (force majeure or logistics) | Notificación con al menos 15 días calendario cuando la causa sea previsible; ante una emergencia, tan pronto como sea razonablemente posible. El participante elige conservar el cupo en la nueva fecha, trasladarlo a otra ronda disponible o cancelar. | Devolución del 100 % si el participante elige cancelar, conforme al trámite financiero de la Universidad; sin penalidad. | CS-12 trigger 4 |
| Provider cancellation (minimum enrollment not met or technical/logistical impossibility) | CALAIRE-EA notifica formalmente y ofrece conservar el cupo para una fecha reprogramada o cancelar la participación, a elección del participante. | Devolución del 100 % de lo pagado si el participante elige cancelar, tramitada conforme a las políticas financieras de la Universidad; sin penalidad. | CS-12 trigger 5 |
| Force majeure affecting participation | Acontecimiento externo, imprevisible e irresistible que impide el cumplimiento, evaluado caso por caso conforme al derecho colombiano. Puede incluir desastre natural, incendio no atribuible, emergencia sanitaria, orden de autoridad, alteración grave del orden público o interrupción crítica externa. No incluye fallas evitables, falta de mantenimiento, falta de fondos ni problemas ordinarios de personal. La parte afectada debe mitigar, documentar y notificar oportunamente. | Reprogramación o reconocimiento del saldo recuperable según el impacto, los costos comprometidos y las políticas de la Universidad; requiere registro y decisión en CS-12. | CS-12 trigger 7; revisión jurídica requerida |
| Refund processing time | El establecido por las políticas y procedimientos vigentes de la Universidad Nacional de Colombia, contado desde que la solicitud queda completa y aprobada. La cotización debe informar el plazo institucional aplicable antes del pago. | política financiera institucional | CS-12 |
| Credit note validity | La emisión, aplicación, vigencia y tratamiento de saldos mediante nota crédito se rigen exclusivamente por las políticas contables y financieras de la Universidad Nacional de Colombia y deben documentarse en cada caso. | política financiera institucional | CS-12 |

**Definición de fuerza mayor:** la cláusula "force majeure" requiere perímetro explícito. Sin lista taxativa o referencia a una ley marco, la cláusula se vuelve litigable. Referenciar aquí el catálogo de eventos cubiertos o la ley aplicable.

## 9. Accreditation and claims

| Rule | Approved wording |
|---|---|
| Accreditation status | The pre-accreditation service may describe its design basis but may not claim that CALAIRE-EA or the round is accredited. |
| Report use | El participante puede declarar que participó en la ronda CALAIRE-EA [ID] para los gases [LISTA]. No puede afirmar ni insinuar que CALAIRE-EA o la ronda están acreditados, ni que el participante es técnicamente competente por el solo hecho de participar. El informe debe utilizarse íntegramente y sin representaciones engañosas de sus resultados o alcance. |

**Texto estándar del report-use reminder** está en CS-13; mantener consistencia. Cualquier variación debe aprobarse en ambos lugares.

## 10. Assigned value and evaluation

| Condition | Rule |
|---|---|
| Fewer than 12 technically valid results | CALAIRE-EA reference value |
| Twelve or more technically valid results | Robust participant consensus |
| Evaluation indicators | z or z′, with ζ and En where uncertainty information is usable |
| Aggregate grading | No a1–a7 grade and no overall pass/fail grade |

## 11. Included and excluded services

**Included:** inscripción y revisión del pedido; un cupo para un analizador en
cada bloque contratado; preparación y coordinación de la ronda; uso de las
instalaciones y del sistema de generación de CALAIRE; ejecución para los gases
contratados; administración y evaluación de datos; informe técnico digital;
constancia de participación; y atención de aclaraciones, quejas y apelaciones
por los canales del QMS.

**Excluded / participant-borne:** transporte del analizador hacia y desde
Medellín; seguro y riesgo del equipo; calibración, mantenimiento o reparación
del analizador del participante; aduanas, visas e impuestos de importación o
exportación; alojamiento, alimentación y demás gastos del personal del
participante.

**Plantilla recomendada para excluidos:**

- Transporte de equipo desde/hacia Medellín (incluye seguro de transporte).
- Riesgo de daño o pérdida del equipo del participante durante el round.
- Visas, permisos de ingreso y estadía del personal del participante.
- Aduanas e impuestos de importación / exportación para clientes internacionales.
- Calibración pre-round del analizador del participante (debe traer calibración vigente).
- Alojamiento y alimentación del personal del participante.

## 12. Approval record

| Version | Date | Approver | Notes |
|---|---|---|---|
| 0.1 DRAFT | [FILL] | [FILL] | Initial draft from MVP blueprint |
| 0.2 DRAFT | 2026-07-14 | [FILL] | Added evidence guidance, working language, exchange rate, fee schedule structure, force majeure scope placeholder. |
| 0.3 PROPOSAL APPROVED | 2026-07-14 | Carmen Elena Zapata | Commercial proposal decisions frozen; finance, legal and technical release gates remain pending. |

## Acceptance test

The owner must be able to answer every field in CS-02 through CS-15 using CS-01 or an existing QMS reference. If a commercial decision is still being invented in an email, CS-01 is incomplete.

## Annex — Evidence guidance per [FILL] marker

Para que un implementador (o un agente AI) que tome esta tarea pueda llenar cada `[FILL]` sin ambigüedad, esta tabla lista qué documento/decision hace falta para cada sección:

| Sección | [FILL] marker | Documento o decisión de origen |
|---|---|---|
| 1 | Service name | propuesta aprobada, naming del SGC |
| 1 | Provider legal identity | registro mercantil, NIT |
| 1 | Roles (service manager, commercial, coordinator, QMS) | organigrama, decreto de creación |
| 1 | Working language of service | decisión de gerencia comercial |
| 1 | Service publication languages | decisión de gerencia comercial |
| 2 | Reporting units por gas | P-PSEA-08 (gestión de datos digitales); informe operativo piloto |
| 3 | Pricing objective (margin / cost recovery / subsidy) | blueprint 8.6 + decisión gerencia |
| 3 | Invoicing currency | política financiera |
| 3 | Exchange-rate method | política financiera |
| 3 | Taxes | asesor tributario |
| 3 | Quotation validity | CS-06 |
| 3 | Acceptance deadline | CS-06 |
| 3 | Flat price and additional analyzer treatment | decisión institucional; validación de costos en CS-04 Tab 6 |
| 6 | Hybrid column | CS-04 Tab 5; aprobación técnica + comercial |
| 6 | Approved strategy + approvers | CS-04 Tab 5; ambos firmantes |
| 7 | Minimum enrollment (number + revenue) | CS-04 Tab 7/8 |
| 7 | Payment / PO deadline | CS-10 |
| 7 | Wait-list priority criteria | CS-10 |
| 7 | Partial payment policy | CS-06, CS-10 |
| 8 | Toda la tabla | CS-12 (cancellation fees) + política financiera |
| 9 | Report use | CS-13 (report-use reminder estándar) |
| 11 | Included / Excluded | CS-06 secciones 6/7, CS-08 cláusula 4 |
