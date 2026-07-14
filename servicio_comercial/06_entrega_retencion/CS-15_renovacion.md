# CS-15 — Mensaje de renovación/seguimiento y registro de clientes potenciales

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Líder comercial
**Requerido antes:** Después de la ronda
**Última revisión:** 2026-07-14 (se agregaron SLA, vínculo con precios de fidelidad, gestión de falta de respuesta, sincronización con CS-05 y verificación del consentimiento de marketing)

## Objetivo

Convertir la participación completada en demanda recurrente.

## SLA de plazos

El seguimiento se envía dentro de un intervalo aprobado posterior a la ronda:

| Hito | SLA |
|---|---|
| Seguimiento enviado tras informe final | [RELLENO: normalmente entre 2 y 4 semanas después de la entrega del informe final según el modelo 18] |
| Seguimiento sin respuesta | [LLENAR: por ejemplo, 30 días después del primer seguimiento, envíe un recordatorio] |
| Cliente potencial marcado como "obsoleto" si no hay respuesta | [RELLENO - por ejemplo, 90 días después del primer seguimiento] |
| Intervalo de reintento para la siguiente ronda | [RELLENO - por ejemplo, 6 meses] |

Los clientes potenciales obsoletos se marcan en CS-10 con el "indicador Stale-EoI" (igual que CS-05) y se excluyen de las vistas de canalización activa.

## Contenido del mensaje

| Elemento | Requerido | Notas |
|---|---|---|
| Agradecer al participante | Sí | |
| Enlace al formulario de comentarios (CS-14) | Sí | |
| Identificar el siguiente periodo previsto del programa | Sí | Consultar CS-03 |
| Registrar los gases de interés futuro | Sí | Registrar en el canal de oportunidades de CS-10 |
| Ofrecer la opción de expresión de interés | Sí | Enlace a CS-05 |
| **Mencione cualquier precio de fidelidad o descuento por rondas múltiples** (si CS-04/CS-01 ha aprobado dicho esquema) | Condicional | Si no existe ningún plan de fidelización, omita esta fila por completo |
| No divulgar ni hacer mercadeo con base en el desempeño confidencial | Sí | Obligatorio |

**Nota sobre precios de lealtad:** si CS-04 no incluye actualmente un descuento de ronda múltiple o un esquema de lealtad, el mensaje NO debe inventar uno. Se debe actualizar CS-04 para incluir el esquema (con la aprobación de la administración) o el mensaje omite la fila. Inventar un descuento en CS-15 rompe la integridad de la cotización de CS-06.

### Plantilla

```text
Asunto: CALAIRE-EA — Gracias y próximo programa — Ronda [ID]

Estimado/a [CONTACTO]:

Gracias por participar en la ronda [ID] de CALAIRE-EA.

Agradecemos sus comentarios para ayudarnos a mejorar el servicio:
[ENLACE al formulario de comentarios CS-14]

Próximo programa
- Periodo previsto: [RELLENO]
- Gases ofrecidos: [RELLENO]

No se ofrece descuento automático por renovación durante la etapa de propuesta.
Una futura política de fidelización requiere revisión de CS-01 y aprobación de
CS-04 antes de comunicarse.

Si le interesa la próxima ronda, indíquenos qué gases desea incluir:
[ENLACE al formulario de expresión de interés CS-05]

Sus resultados de desempeño seguirán siendo confidenciales y no se utilizarán con fines de mercadeo. Puede revocar en cualquier momento su consentimiento para recibir comunicaciones comerciales respondiendo a este correo electrónico.

Cordialmente,
[LÍDER COMERCIAL]
```

## Gestión de la falta de respuesta

| Situación | Acción |
|---|---|
| No hay respuesta dentro de la ventana de recordatorio de SLA | Enviar recordatorio con el mismo contenido + "Si no recibimos noticias suyas antes del [FECHA], marcaremos su interés de renovación como inactivo. Puede reactivarlo en cualquier momento". |
| No hay respuesta después del recordatorio | Marcar cliente potencial como "obsoleto" en CS-10 (indicador obsoleto-EoI = Sí) |
| El cliente responde después de un indicador obsoleto | Reactivar el cliente potencial; reiniciar el plazo para marcarlo como obsoleto |

## Sincronizar con CS-05 (expresión de interés)

Cuando el cliente responde al seguimiento con interés de renovación:

- **No** cree un nuevo envío CS-05 desde cero. En su lugar, **actualice el registro CS-10 existente** con:
- Nueva entrada en pipeline para la siguiente ronda (estado = Interés para la nueva ronda).
- Gases de interés de la respuesta.
  - Periodo preferido.
  - Plazo de adquisición, si se indicó.
- Indicador de consentimiento de marketing (por separado del consentimiento de servicio según la Ley 1581/2012).
- El formulario CS-05 sigue siendo el canal formal de EoI para nuevos prospectos; para renovaciones, la actualización CS-10 es suficiente y evita volver a solicitar datos de organización/contacto.

Si el cliente envía explícitamente un nuevo CS-05 (por ejemplo, a través del formulario en lugar de responder al seguimiento), combine los datos en el registro CS-10 existente; no duplicar.

## Registro del cliente potencial

Actualice el rastreador CS-10 con:

- Nueva entrada en el canal de oportunidades para la próxima ronda (estado = Interés).
- Gases de interés de respuesta.
- Periodo preferido.
- Plazo de adquisición, si se indicó.
- Indicador de consentimiento de marketing.
- Fecha de EoI obsoleta (90 días después del seguimiento si no hay respuesta).

## Controles

- No hacer referencia a puntuaciones individuales, puntuaciones z ni desempeño relativo.
- No afirmar que existe acreditación si no existe.
- Consentimiento verificado antes de agregarlo a la lista de marketing (por separado del consentimiento del servicio).
- Si el CS-14 se envió de forma anónima, el seguimiento de la renovación no puede hacer referencia a las respuestas anteriores; el mensaje es genérico.
- El precio de fidelidad debe provenir del CS-04, no inventado en el CS-15.

## Aprobación

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregó SLA de sincronización, regla condicional de precios de lealtad, manejo de falta de respuesta, sincronización CS-05, verificación de consentimiento de marketing. |
