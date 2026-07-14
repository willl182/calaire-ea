# CS-12 — Registro de cambios, cancelaciones y reembolsos

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Comercial / financiero
**Requerido antes:** Cuando se activa
**Last revision:** 2026-07-14 (added fee catalog reference, viability impact, refund timing, original quote revision traceability, financial-decision dual authorization)  
**QMS code reference:** ver `00_control/equivalencia_codigos_sgc.md`. `P-PSEA-15` (vigente) = Trabajo no conforme / NC / CAPA. `P-PSEA-16` (vigente) = Divulgación y control de valores sensibles.

## Objetivo

Controlar los cambios comerciales y las decisiones financieras.

## Trigger events

- [ ] El participante cambia los gases seleccionados.
- [ ] El participante agrega/reemplaza un analizador.
- [ ] El participante se retira.
- [ ] CALAIRE-EA postpones or cancels.
- [ ] Minimum enrollment is not achieved.
- [ ] Cambio de fechas o instalaciones.
- [ ] Force majeure affects participation.
- [ ] Refund or credit note is requested.
- [ ] El proveedor identifica un error sustancial en el informe (activa la cadena CS-13 → CS-12).

## Minimum record

| Campo | Valor |
|---|---|
| Record ID | [FILL — unique] |
| Date opened | [FILL] |
| Cliente | [RELLENO] |
| Identificación redonda | [RELLENO] |
| **Original quote reference (family + revision)** | [FILL — e.g., Q-2026-0042 rev 0; required for traceability of superseded terms] |
| **Revised quote reference (if applicable)** | [FILL — e.g., Q-2026-0042 rev 1] |
| Invoice reference | [FILL] |
| Credit note reference (if applicable) | [FILL] |
| **Tarifa aplicable según la lista de tarifas de la Sección 8 CS-01** | [FILL — por ejemplo, "30 % de retención por retiro ≥ 30 días antes del inicio de la ronda"] |
| Compromiso original | [FILL — gases, analizadores, fechas, precio] |
| Cambio solicitado o impuesto | [RELLENO] |
| Applicable contract clause | [FILL — reference CS-08 clause] |
| Impacto técnico/capacidad | [FILL — efecto en la planificación circular; por ejemplo, "libera 1 posición CO"] |
| **Impacto en la viabilidad de la ronda** | [FILL — según CS-04 Tab 7: "la viabilidad cae por debajo del mínimo" o "aún es viable"] |
| Cálculo de tarifas, reembolsos o créditos | [FILL - línea por línea: precio original, tarifa, monto del reembolso, monto del crédito, moneda, tipo de cambio] |
| **Compromiso de tiempo de procesamiento de reembolso** | [FILL - según CS-01 Sección 8: por ejemplo, 30 días hábiles desde la aprobación] |
| **Validez de la nota de crédito** | [FILL — según CS-01 Sección 8: por ejemplo, 12 meses desde la emisión] |
| Decisión | [FILL — aprobado / rechazado / pendiente] |
| Decisión autorizada por (comercial) | [LLENAR NOMBRE, FECHA] |
| Decision authorized by (finance or management) | [FILL NAME, DATE] — **dual authorization required for any financial decision** |
| Fecha de notificación al cliente | [RELLENO] |
| Updated tracker reference | [FILL — CS-10 row updated] |
| Updated quote reference | [FILL — revised quote number if applicable] |
| Updated invoice reference | [FILL — credit note or new invoice] |
| Updated registration reference | [FILL] |
| Closure date | [FILL] |
| Closure authorized by | [FILL NAME, DATE] |

## Controls

- **Las decisiones financieras requieren doble autorización** (comercial + financiera o de gestión). Los cambios de autoridad única no son válidos.
- Capacity changes are reflected immediately in CS-10 (no batched updates).
- Las revisiones de cotizaciones siguen las reglas de control de cotizaciones CS-06. Se debe citar la familia de cotizaciones original + revisión.
- Tiempo de procesamiento de reembolso según CS-01 Sección 8 (normalmente 30 días hábiles desde la aprobación); cualquier retraso más allá del compromiso requiere notificación al cliente con la fecha revisada.
- Las notas de crédito tienen un período de validez según CS-01 Sección 8; Las notas de crédito vencidas no se aceptan sin la reautorización de la gerencia.
- Las quejas técnicas o no conformidades identificadas durante un cambio se encaminan a los controles PEAS existentes (`P-PSEA-15` NC/CAPA, `P-PSEA-16` valores sensibles).
- Si un cambio es provocado por un error sustancial del informe (CS-13), el registro CS-12 debe hacer referencia al identificador del informe CS-13 y a la nota de corrección de cambio CS-13.
- Trazabilidad de la cotización original: cada registro CS-12 debe citar la familia de cotización original + revisión. Esto protege contra disputas sobre qué términos se aplicaban en el momento del compromiso original.

## Fee catalog reference

La lista de tarifas aplicada en este registro se define en CS-01 Sección 8. El resumen de tarifas típicas:

| Scenario | Typical fee / refund |
|---|---|
| Retiro de participantes ≥ N días antes del inicio de la ronda | [FILL — % de retención o tarifa fija] |
| Retiro de participantes < N días antes del inicio de la ronda | [FILL - mayor porcentaje de retención] |
| Participante no presentado | [FILL - sin reembolso] |
| Aplazamiento del proveedor | [FILL: espacio reservado o reembolso completo a elección del cliente] |
| Cancelación de proveedor (inscripción mínima no cumplida) | [FILL — reembolso completo o nota de crédito, elección del cliente] |
| Fuerza mayor | [FILL — reembolso prorrateado o nota de crédito, elección del cliente] |
| Error de informe sustancial (activador CS-13) | [FILL: normalmente reembolso completo de la tarifa de ronda + reemisión gratuita] |

Ver CS-01 Sección 8 para conocer los valores autorizados y las reglas de decisión.

## Approval

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregó referencia del catálogo de tarifas, impacto en la viabilidad, calendario de reembolso, trazabilidad de la cotización original, autorización dual explícita, enlace CS-13. |
