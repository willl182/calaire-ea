# CS-09 — Lista de verificación de revisión de contrato/PO

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Comercial + esquema
**Requerido antes:** Confirmación
**Last revision:** 2026-07-14 (added residual capacity check, granular disclosure consent branches, signature requirement per check)  
**QMS code reference:** ver `00_control/equivalencia_codigos_sgc.md`. Las referencias QMS usan los códigos vigentes post-renumeración 2026-06-14.

## Objetivo

Impedir que CALAIRE-EA acepte un pedido que no puede entregar o cuyo lenguaje de orden de compra entra en conflicto con las condiciones del PT.

## Checks

Cada verificación **debe estar firmada** (iniciales) por el revisor; "—" o un espacio en blanco no es aceptable. Una verificación puede ser Pasa, Falla o N/A (con justificación).

| # | Check | Evidence required | Pass / Fail / N/A | Initial |
|---|---|---|---|---|
| 1 | La cotización es válida y coincide con el registro (paquete de gas, recuento del analizador, cliente) | Número de cotización, fecha de emisión, vencimiento, fecha límite de aceptación | | |
| 2 | Quote is not already accepted by another party (no double-booking) | CS-06 revision history / CS-10 quote view | | |
| 3 | Los gases seleccionados se ofrecen en ronda | Aviso de ronda (CS-03) | | |
| 4 | La capacidad del analizador sigue estando disponible por gas y configuración operativa | Vista de capacidad del rastreador CS-10 | | |
| 5 | El pedido se mantiene dentro de los límites de capacidad (4 posiciones de gas individuales o límite de CO/SO₂ simultáneo de 3 participantes/6 analizadores) | Rastreador CS-10 | | |
| 6 | **La capacidad residual después de este pedido es ≥ 0** (este es el límite de aceptación: si se consume el último espacio, márquelo como "último espacio" y requiera autorización comercial principal) | Vista de capacidad del CS-10 | | |
| 7 | El equipo parece compatible según los datos enviados (modelo, fechas de calibración) | `F-PSEA-04` anexo técnico/equipamiento (post-renumeración) y `calaire-app` | | |
| 8 | Coincidencia de precios, moneda, impuestos y cronograma de pagos | Cotización CS-06 vs. registro vs. PO | | |
| 9 | PO no anula silenciosamente las reglas de cancelación, confidencialidad o informes (diferencia cláusula por cláusula frente a CS-08) | Texto del PO revisado con respecto al CS-08 | | |
| 10 | PO no anula silenciosamente la regla de valor asignado, los indicadores de evaluación o la calificación no-a1-a7 (CS-08 cláusulas 12 y 13) | Texto de orden de compra revisado | | |
| 11 | Es posible realizar informes específicos del cliente o requisitos lingüísticos | Confirmación de operaciones | | |
| 12 | El riesgo de conflicto de intereses o de imparcialidad se refiere al control del SGC existente | Registro de imparcialidad/revisión de la gestión | | |
| 13 | **El consentimiento de divulgación se registra Y tiene un alcance correcto** (divulgación regulatoria, divulgación de marketing, divulgación transfronteriza: tres consentimientos separados) | Formulario de inscripción (CS-07) | | |
| 14 | **Data protection consent is recorded** (Ley 1581/2012 text accepted) | Registration form (CS-07) | | |
| 15 | Se recibe el pago requerido / evidencia de orden de compra | Confirmación de finanzas | | |
| 16 | Si estado = En lista de espera, criterios de prioridad de la lista de espera documentados y aplicados (según CS-01 Sección 7) | Vista de lista de espera de CS-10 | | |
| 17 | Se autoriza decisión de aceptación, lista de espera o rechazo (líder comercial para norma; gestión para institucional) | Autoridad de aprobación CS-01 | | |

**Disclosure consent branches** (granularity for check 13):

- **Divulgación reglamentaria:** consentimiento para divulgar resultados a las autoridades reguladoras cuando lo exija la ley (normalmente obligatorio, no opcional).
- **Marketing disclosure:** consent to use anonymized participation data in marketing materials (optional, revocable).
- **Divulgación transfronteriza:** consentimiento para transferir los datos del informe fuera de Colombia para su entrega (requerido para clientes internacionales; explícito según la Ley 1581/2012).

Un solo "Acepto la divulgación" es **insuficiente**: cada sucursal debe verificarse por separado en CS-07 y verificarse en esta lista de verificación.

## Revisar registro

| Campo | Valor |
|---|---|
| Identificación redonda | [RELLENO] |
| Cliente | [RELLENO] |
| Registration date | [FILL] |
| Marca de tiempo de aceptación | [RELLENO — de CS-07] |
| Quote number | [FILL] |
| Quote revision | [FILL] |
| Reviewer | [FILL NAME] |
| Fecha de revisión | [RELLENO] |
| Decision | [Accepted / Wait-listed / Rejected] |
| Decision authorized by | [FILL NAME] |
| Authorization date | [FILL] |
| Notas | [RELLENO] |

## Controls

- Los pedidos rechazados se registran con el motivo (obligatorio; "sin motivo" no es aceptable).
- Los pedidos en lista de espera se rastrean en CS-10 con la fecha de prioridad y los criterios aplicados.
- Los pedidos confirmados activan la confirmación CS-11 y la transferencia QMS.
- Las 17 verificaciones deben estar rubricadas; las iniciales que faltan bloquean la decisión.
- Si falla alguna verificación, el registro es rechazado o devuelto al cliente; el motivo se documenta y se comparte con el cliente.

## Approval

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregó verificación de capacidad residual, ramas de consentimiento de divulgación granular, verificación de protección de datos, requisito de firma por verificación, revisión de texto de orden de compra duplicada (valor asignado + no-a1-a7). |
| 0.2.1 CORRECCIÓN | 2026-07-14 | [RELLENO] | Terminología corregida ("verificación" en lugar de "cheque"); estado actualizado a BORRADOR. |
