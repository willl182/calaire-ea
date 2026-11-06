# CS-15 — Mensaje de renovación / seguimiento y registro de prospectos

<<<<<<< Updated upstream
**Propietario:** Profesional de proyectos
**Última revisión:** 2026-07-14 (se agregaron SLA, vínculo con precios de fidelidad, gestión de falta de respuesta, sincronización con CS-05 y verificación del consentimiento de marketing)
=======
**Estado:** BORRADOR — contenido redactado; aprobación pendiente\
**Propietario:** Líder comercial\
**Requerido:** después de la ronda\
**Última revisión:** 2026-07-14 (se agregaron plazos, regla de precios de fidelización, gestión de falta de respuesta, sincronización con CS-05 y verificación del consentimiento de comunicaciones)
>>>>>>> Stashed changes

## Objetivo

Convertir la participación completada en demanda recurrente.

## Plazos

El seguimiento se envía dentro de un intervalo aprobado posterior a la ronda:

| Hito | Plazo |
|---|---|
<<<<<<< Updated upstream
| Seguimiento enviado tras informe final | [POR DILIGENCIAR — normalmente entre 2 y 4 semanas después de la entrega del informe final según el modelo 18] |
| Seguimiento sin respuesta | [POR DILIGENCIAR — por ejemplo, 30 días después del primer seguimiento, envíe un recordatorio] |
| Cliente potencial marcado como "obsoleto" si no hay respuesta | [POR DILIGENCIAR — por ejemplo, 90 días después del primer seguimiento] |
| Intervalo de reintento para la siguiente ronda | [POR DILIGENCIAR — por ejemplo, 6 meses] |
=======
| Envío del seguimiento | Entre 2 y 4 semanas después de la entrega del informe final |
| Recordatorio si no hay respuesta | 30 días después del primer seguimiento |
| Prospecto marcado como inactivo si no hay respuesta | 90 días después del primer seguimiento |
| Nuevo contacto para la siguiente ronda | 6 meses |
>>>>>>> Stashed changes

Los prospectos inactivos se marcan en CS-10 con el indicador de expresión de interés vencida (igual que CS-05) y se excluyen de las vistas del embudo activo.

## Contenido del mensaje

| Elemento | Requerido | Notas |
|---|---|---|
| Agradecer al participante | Sí | |
| Enlace al formulario de comentarios (CS-14) | Sí | |
| Identificar el siguiente periodo previsto del programa | Sí | Consultar CS-03 |
| Registrar los gases de interés futuro | Sí | Registrar en el embudo de CS-10 |
| Ofrecer la opción de expresión de interés | Sí | Enlace a CS-05 |
| **Mencionar precios de fidelización o descuento por varias rondas** (solo si CS-04/CS-01 aprobaron dicho esquema) | Condicional | Si no existe un esquema aprobado, se omite |
| No divulgar ni hacer divulgación comercial con base en el desempeño confidencial | Sí | Obligatorio |

**Nota sobre precios de fidelización:** si CS-04 no incluye un descuento por varias rondas o un esquema de fidelización, el mensaje no debe inventarlo. Se actualiza CS-04 (con aprobación de la dirección) o se omite el elemento. Inventar un descuento en CS-15 rompe la integridad de las cotizaciones CS-06.

### Plantilla

```text
Asunto: CALAIRE-EA — Gracias y próximo programa — Ronda [ID]

Estimado/a [CONTACTO]:

Gracias por participar en la ronda [ID] de CALAIRE-EA.

Agradecemos sus comentarios para ayudarnos a mejorar el servicio:
[ENLACE al formulario de comentarios CS-14]

Próximo programa
<<<<<<< Updated upstream
- Periodo previsto: [POR DILIGENCIAR]
- Gases ofrecidos: [POR DILIGENCIAR]
=======
- Periodo previsto: [PERIODO según CS-03]
- Bloques ofrecidos: [BLOQUES según CS-03]
>>>>>>> Stashed changes

No se ofrece descuento automático por renovación durante la etapa de propuesta.
Una futura política de fidelización requiere revisión de CS-01 y aprobación de
CS-04 antes de comunicarse.

Si le interesa la próxima ronda, indíquenos qué gases desea incluir:
[ENLACE al formulario de expresión de interés CS-05]

Sus resultados de desempeño seguirán siendo confidenciales y no se utilizarán con fines de mercadeo. Puede revocar en cualquier momento su consentimiento para recibir comunicaciones comerciales respondiendo a este correo electrónico.

Cordialmente,
<<<<<<< Updated upstream
[PROFESIONAL DE PROYECTOS]
=======
David Pulgarín
Líder comercial — CALAIRE-EA
>>>>>>> Stashed changes
```

## Gestión de la falta de respuesta

| Situación | Acción |
|---|---|
| No hay respuesta dentro del plazo de recordatorio | Enviar recordatorio con el mismo contenido + "Si no recibimos noticias suyas antes del [FECHA], marcaremos su interés de renovación como inactivo. Puede reactivarlo en cualquier momento". |
| No hay respuesta después del recordatorio | Marcar el prospecto como inactivo en CS-10 (expresión de interés vencida = Sí) |
| El cliente responde después de quedar inactivo | Reactivar el prospecto y reiniciar el plazo |

## Sincronización con CS-05 (expresión de interés)

Cuando el cliente responde al seguimiento con interés de renovación:

- **No** se crea un nuevo envío CS-05 desde cero; se **actualiza el registro CS-10 existente** con:
    - Nueva entrada en el embudo para la siguiente ronda (estado = Interés para la nueva ronda).
    - Bloques de interés de la respuesta.
    - Periodo preferido.
    - Plazo de compra, si se indicó.
    - Indicador de consentimiento de comunicaciones comerciales (separado del consentimiento del servicio según la Ley 1581/2012).
- El formulario CS-05 sigue siendo el canal formal de expresión de interés para nuevos prospectos; para renovaciones, la actualización CS-10 es suficiente y evita volver a solicitar datos de organización/contacto.

Si el cliente envía explícitamente un nuevo CS-05 (por ejemplo, a través del formulario en lugar de responder al seguimiento), los datos se combinan en el registro CS-10 existente, sin duplicar.

## Registro del prospecto

Se actualiza el seguimiento CS-10 con:

- Nueva entrada en el embudo para la próxima ronda (estado = Interés).
- Bloques de interés de la respuesta.
- Periodo preferido.
- Plazo de compra, si se indicó.
- Indicador de consentimiento de comunicaciones comerciales.
- Fecha de vencimiento del interés (90 días después del seguimiento si no hay respuesta).

## Controles

- No hacer referencia a puntuaciones individuales, puntuaciones z ni desempeño relativo.
- No afirmar que existe acreditación si no existe.
- Consentimiento verificado antes de agregar el contacto a la lista de comunicaciones comerciales (separado del consentimiento del servicio).
- Si el CS-14 se envió de forma anónima, el seguimiento de la renovación no puede hacer referencia a las respuestas anteriores; el mensaje es genérico.
<<<<<<< Updated upstream
- El precio de fidelidad debe provenir del CS-04, no inventado en el CS-15.
=======
- El precio de fidelización debe provenir de CS-04, no inventarse en CS-15.

## Aprobación

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | 2026-07-12 | — | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | — | Se agregaron plazos, regla condicional de precios de fidelización, manejo de falta de respuesta, sincronización con CS-05 y verificación del consentimiento de comunicaciones. |
>>>>>>> Stashed changes
