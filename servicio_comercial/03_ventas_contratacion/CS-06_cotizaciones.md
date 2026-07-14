# CS-06 — Plantilla de cotización

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Líder comercial
**Requerido antes:** Oferta
**Última revisión:** 2026-07-14 (fecha límite de aceptación versus vencimiento agregada, tabla de cronograma de pagos, impuestos de importación/notas de retención para internacionales, referencia de política cambiaria, regla del método de aceptación)
**QMS code reference:** ver `00_control/equivalencia_codigos_sgc.md`.

## Objetivo

Realizar una oferta comercial controlada.

## Minimum sections

### 1. Quote header

| Campo | Valor |
|---|---|
| Quote number | [FILL — unique, e.g., Q-YYYY-NNNN] |
| Family | [FILL — same family for all revisions; e.g., Q-2026-0042] |
| Revision | [FILL — initial = 0, increment on each revision] |
| Issue date | [FILL] |
| Fecha de caducidad | [FILL: por ejemplo, 30 días desde la emisión, después de los cuales no se puede emitir la oferta, pero sí una nueva] |
| **Fecha límite de aceptación** | [FILL: por ejemplo, 15 días calendario desde la emisión, antes de los cuales el cliente debe firmar para bloquear la oferta; distinto del vencimiento] |
| Acceptance method | Cotización firmada por representante autorizado y devuelta desde correo institucional, u orden de compra formal aceptada por la Universidad |
| Reemplaza cotización anterior | [FILL: número de cotización y revisión que se reemplazan, "ninguna" si es la primera] |

### 2. Información legal y de facturación del cliente

- Legal name
- Tax ID / VAT number
- Billing address
- Billing contact
- **Moneda de facturación**: debe coincidir con la moneda de facturación CS-01, a menos que se apruebe explícitamente lo contrario.

### 3. ID de ronda y fechas

- ID de ronda: [FILL]
- Provisional / confirmed dates: [FILL]
- Location: [FILL]

### 4. Selected gas package

| Gas | Incluido |
|---|---|
| CO | [Sí / No] |
| SO₂ | [Sí / No] |
| NO | [Sí / No] |
| NO₂ | [Sí / No] |
| O₃ | [Sí / No] |

### 5. Analizadores y participantes

- Number of analyzers: [FILL]
- Number of participants covered: [FILL]
- Operating configuration: [Individual gas / Simultaneous CO/SO₂]
- Se acepta analizador adicional con capacidad residual: [SI / NO]; recargo provisional: COP 0

### 6. Entregables incluidos

[FILL - derivado de CS-01 Sección 11.]

### 7. Exclusiones y costes a cargo de los participantes

[FILL — derivado de CS-01 Sección 11. Para clientes internacionales, enumere explícitamente: transporte, seguros, aduanas, visas, impuestos de importación.]

### 8. Precio

| Item | Amount |
|---|---|
| Cuota fija de participación en la ronda | [FILL: solo el valor aprobado en CS-04 Tab 9; nunca copie el punto de referencia interno] |
| Selected-block adjustment | COP 0 |
| Analizador adicional aceptado con capacidad residual | COP 0 durante etapa de propuesta |
| Subtotal (excl. taxes) | [CALC] |
| Impuestos | [FILL – ver notas internacionales si corresponde] |
| **Total** | **[CALC]** |

Moneda: COP. No se podrá emitir ninguna cotización real mientras el campo de tarifa aprobada esté
pending.

**Referencia de política cambiaria** (cuando moneda de facturación ≠ moneda de cálculo de costos): tipo de cambio aplicado, fuente, fecha de actualización, asignación de riesgo cambiario. Extraído de CS-01 / CS-04 Tab 1.

### 9. Calendario de pagos y condiciones de orden de compra aceptables

**Tabla de pagos estándar** (úsela para la variante predeterminada):

| Milestone | % of total | Amount | Due date | Method |
|---|---|---|---|---|
| Order acceptance | [FILL — e.g., 50%] | [CALC] | [FILL] | Wire / PO / card |
| Pre-ronda (5 días hábiles antes del inicio) | [LLENAR - por ejemplo, 50%] | [CALC] | [RELLENO] | Cable / PO |
| **Total** | 100% | [CALC] | | |

**Estructuras de pago alternativas** (seleccione si corresponde, justificación del documento):

- 100% in advance (e.g., for small amounts or first-time clients).
- 100% contra entrega (solo para clientes institucionales con crédito aprobado; requiere preaprobación CS-01).
- PO a 30/60/90 días (solo para clientes institucionales con historial crediticio; necesita aprobación financiera).

**Consecuencias de la mora** (enlace a CS-08 cláusula 6): intereses, suspensión del servicio, desencadenante de cancelación.

### 10. Minimum-enrollment / postponement condition

[LLENAR: por ejemplo, "Esta cotización está condicionada a la inscripción mínima de N participantes antes del [fecha]. Si no se cumple el mínimo, CALAIRE-EA puede posponer o cancelar la ronda con un reembolso completo".]

### 11. Cancellation terms

[FILL: derivado de CS-01 Sección 8, incluido el programa de tarifas según la fecha límite de retiro. Haga referencia a la plantilla de registro CS-12 que se abrirá ante cualquier cambio.]

### 12. Pre-accreditation wording

[FILL — igual que CS-02: "El servicio puede describir su base de diseño pero no puede afirmar que CALAIRE-EA o la ronda estén acreditados".]

### 13. Enlace/referencia a términos y registro

- Términos y condiciones: [ENLACE a CS-08]
- Registration form: [LINK to CS-07]
- Privacy policy / data protection notice: [LINK]

### 14. Método de aceptación y contacto autorizado

- Acceptance: cotización firmada por representante autorizado desde correo institucional u orden de compra formal aceptada por la Universidad. Un correo informal no reserva cupo.
- Authorized CALAIRE-EA contact: [FILL NAME, EMAIL, PHONE]
- **Regla de aceptación:** "Esta cotización se considera aceptada únicamente cuando CALAIRE-EA recibe una aceptación por escrito del contacto autorizado del cliente, firmada o enviada desde un correo electrónico verificado, antes de la fecha límite de aceptación establecida en la sección 1. El silencio no constituye aceptación."

## International variant — additional fields

Sólo para la variante de plantilla "Internacional":

| Campo | Valor |
|---|---|
| Country of origin of client | [FILL] |
| Moneda de facturación | [FILL — debe ser una de las monedas aprobadas por CS-01] |
| Import taxes / VAT treatment | [FILL — e.g., "IVA exento bajo tratado X", "withholding Y%", "client responsible for import duties in country Z"] |
| Divulgación de conversión de moneda | [FILL — "Total expresado en [MONEDA DE FACTURACIÓN] utilizando la tasa de referencia [TASA] de [FECHA]. El cliente asume el riesgo cambiario desde la fecha de aceptación."] |
| Shipping terms (if applicable) | [FILL — INCOTERMS] |
| Nota de transferencia de datos transfronteriza | [FILL — por ejemplo, "Los datos de los participantes se almacenan en Colombia y se procesan según la Ley 1581/2012. Al aceptar, el cliente da su consentimiento a la transferencia transfronteriza de los datos del informe."] |

## Quote control

- Cada revisión conserva la misma familia de cotizaciones con un número de revisión.
- Un cambio en la selección de gas, el recuento del analizador, la identidad del cliente, la ronda o el precio requiere una cotización revisada.
- All revisions are tracked in this file (or a controlled extension per quote family) per `registro_cambios_versiones.md` rules.

## Template variants

| Variant | Trigger | Notas |
|---|---|---|
| Standard | One to four selected blocks | Default flat-fee template |
| Participación completa | Bloques de CO, SO₂, O₃ y NO/NO₂ | Utiliza puntos de referencia planos aprobados |
| Internacional | Cliente fuera de Colombia | Agrega campos de cambio de divisas, impuestos de importación y transferencia de datos transfronterizos |
| Institucional / cerrado | Solicitud de ronda dedicada | Cotización separada del costo total (CS-04 Tab 10) |

## Approval

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregó fecha límite de aceptación, tabla de pagos, campos de datos internacionales/impuestos de importación/cambios transfronterizos, regla de aceptación explícita. |
