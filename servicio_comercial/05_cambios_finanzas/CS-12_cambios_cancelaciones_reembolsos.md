# CS-12 — Registro de cambios, cancelaciones y reembolsos

**Propietario:** Profesional de proyectos
**Última revisión:** 2026-07-14 (se agregaron la referencia al catálogo de tarifas, el impacto en la viabilidad, el plazo de reembolso, la trazabilidad de la revisión de la cotización original y la doble autorización de decisiones financieras)
**Referencia de códigos del SGC:** ver `00_control/equivalencia_codigos_sgc.md`. `P-PSEA-15` (vigente) = Trabajo no conforme / NC / CAPA. `P-PSEA-16` (vigente) = Divulgación y control de valores sensibles.

## Objetivo

Controlar los cambios comerciales y las decisiones financieras.

## Eventos desencadenantes

- [ ] El participante cambia los gases seleccionados.
- [ ] El participante agrega/reemplaza un analizador.
- [ ] El participante se retira.
- [ ] CALAIRE-EA aplaza o cancela.
- [ ] No se alcanza la inscripción mínima.
- [ ] Cambio de fechas o instalaciones.
- [ ] Una situación de fuerza mayor afecta la participación.
- [ ] Se solicita un reembolso o una nota crédito.
- [ ] El proveedor identifica un error sustancial en el informe (activa la cadena CS-13 → CS-12).

## Registro mínimo

| Campo | Valor |
|---|---|
| ID del registro | [POR DILIGENCIAR — único] |
| Fecha de apertura | [POR DILIGENCIAR] |
| Cliente | [POR DILIGENCIAR] |
| Identificación de la ronda | [POR DILIGENCIAR] |
| **Referencia de la cotización original (familia + revisión)** | [POR DILIGENCIAR — p. ej., Q-2026-0042 rev. 0; necesaria para la trazabilidad de las condiciones reemplazadas] |
| **Referencia de la cotización revisada (si aplica)** | [POR DILIGENCIAR — p. ej., Q-2026-0042 rev. 1] |
| Referencia de factura | [POR DILIGENCIAR] |
| Referencia de nota crédito (si aplica) | [POR DILIGENCIAR] |
| **Tarifa aplicable según la lista de tarifas de la Sección 8 CS-01** | [POR DILIGENCIAR — por ejemplo, "30 % de retención por retiro ≥ 30 días antes del inicio de la ronda"] |
| Compromiso original | [POR DILIGENCIAR — gases, analizadores, fechas, precio] |
| Cambio solicitado o impuesto | [POR DILIGENCIAR] |
| Cláusula contractual aplicable | [POR DILIGENCIAR — referencia a la cláusula de CS-08] |
| Impacto técnico/capacidad | [POR DILIGENCIAR — efecto en la planificación circular; por ejemplo, "libera 1 posición CO"] |
| **Impacto en la viabilidad de la ronda** | [POR DILIGENCIAR — según la pestaña 7 de CS-04: "la viabilidad cae por debajo del mínimo" o "aún es viable"] |
| Cálculo de tarifas, reembolsos o créditos | [POR DILIGENCIAR — línea por línea: precio original, tarifa, monto del reembolso, monto del crédito, moneda, tipo de cambio] |
| **Compromiso de tiempo de procesamiento de reembolso** | [POR DILIGENCIAR — según CS-01 Sección 8: por ejemplo, 30 días hábiles desde la aprobación] |
| **Validez de la nota de crédito** | [POR DILIGENCIAR — según CS-01 Sección 8: por ejemplo, 12 meses desde la emisión] |
| Decisión | [POR DILIGENCIAR — aprobado / rechazado / pendiente] |
| Decisión autorizada por (comercial) | [POR DILIGENCIAR — nombre y fecha] |
| Decisión autorizada por (finanzas o gestión) | [POR DILIGENCIAR — NOMBRE, FECHA] — **se requiere doble autorización para cualquier decisión financiera** |
| Fecha de notificación al cliente | [POR DILIGENCIAR] |
| Referencia actualizada del rastreador | [POR DILIGENCIAR — fila de CS-10 actualizada] |
| Referencia actualizada de cotización | [POR DILIGENCIAR — número de cotización revisada, si aplica] |
| Referencia actualizada de factura | [POR DILIGENCIAR — nota crédito o factura nueva] |
| Referencia actualizada de inscripción | [POR DILIGENCIAR] |
| Fecha de cierre | [POR DILIGENCIAR] |
| Cierre autorizado por | [POR DILIGENCIAR — NOMBRE, FECHA] |

## Controles

- **Las decisiones financieras requieren doble autorización** (comercial + financiera o de gestión). Los cambios de autoridad única no son válidos.
- Los cambios de capacidad se reflejan inmediatamente en CS-10 (sin actualizaciones por lotes).
- Las revisiones de cotizaciones siguen las reglas de control de cotizaciones CS-06. Se debe citar la familia de cotizaciones original + revisión.
- Tiempo de procesamiento de reembolso según CS-01 Sección 8 (normalmente 30 días hábiles desde la aprobación); cualquier retraso más allá del compromiso requiere notificación al cliente con la fecha revisada.
- Las notas de crédito tienen un período de validez según CS-01 Sección 8; Las notas de crédito vencidas no se aceptan sin la reautorización de la gerencia.
- Las quejas técnicas o no conformidades identificadas durante un cambio se encaminan a los controles PEAS existentes (`P-PSEA-15` NC/CAPA, `P-PSEA-16` valores sensibles).
- Si un cambio es provocado por un error sustancial del informe (CS-13), el registro CS-12 debe hacer referencia al identificador del informe CS-13 y a la nota de corrección de cambio CS-13.
- Trazabilidad de la cotización original: cada registro CS-12 debe citar la familia de cotización original + revisión. Esto protege contra disputas sobre qué términos se aplicaban en el momento del compromiso original.

## Referencia al catálogo de tarifas

La lista de tarifas aplicada en este registro se define en CS-01 Sección 8. El resumen de tarifas típicas:

| Escenario | Tarifa / reembolso habitual |
|---|---|
| Retiro de participantes ≥ N días antes del inicio de la ronda | [POR DILIGENCIAR — % de retención o tarifa fija] |
| Retiro de participantes < N días antes del inicio de la ronda | [POR DILIGENCIAR — mayor porcentaje de retención] |
| Participante no presentado | [POR DILIGENCIAR — sin reembolso] |
| Aplazamiento del proveedor | [POR DILIGENCIAR — espacio reservado o reembolso completo a elección del cliente] |
| Cancelación de proveedor (inscripción mínima no cumplida) | [POR DILIGENCIAR — reembolso completo o nota de crédito, elección del cliente] |
| Fuerza mayor | [POR DILIGENCIAR — reembolso prorrateado o nota de crédito, elección del cliente] |
| Error de informe sustancial (activador CS-13) | [POR DILIGENCIAR — normalmente reembolso completo de la tarifa de ronda + reemisión gratuita] |

Ver CS-01 Sección 8 para conocer los valores autorizados y las reglas de decisión.
