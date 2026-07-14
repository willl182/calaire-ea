# CS-11 — Paquete de confirmación e incorporación

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Coordinador de ronda
**Requerido antes:** Preparación técnica
**Última revisión:** 2026-07-14 (se agregaron plantillas de lista de espera y rechazo, regla de vencimiento de confirmación, campo de participantes adicionales, corrección de referencias de código QMS)
**Referencia de códigos del SGC:** ver `00_control/equivalencia_codigos_sgc.md`. Las referencias al SGC usan los códigos vigentes tras la renumeración del 2026-06-14.

## Objetivo

Confirmar la compra y transferirla al SGC. Este artefacto también cubre los mensajes de **lista de espera** y de **rechazo** enviados a clientes cuya inscripción no se puede confirmar.

## Mensaje de confirmación

### Campos obligatorios

| Campo | Valor |
|---|---|
| Nombre legal del cliente | [RELLENO] |
| Identificación redonda | [RELLENO] |
| Código de participante | [RELLENO — asignado por el SGC] |
| Gas o gases seleccionados | [RELLENO] |
| Cantidad de analizadores confirmados | [RELLENO] |
| Fechas y ubicación | [RELLENO] |
| Estado de pago/orden de compra | [RELLENO] |
| Contacto técnico principal | Wilson Salas — `calaire_med@unal.edu.co` |
| Contacto administrativo principal | David Pulgarín — `calaire_med@unal.edu.co` |
| Participantes adicionales de la misma organización (si los hay) | [RELLENO - NOMBRES, CORREOS ELECTRÓNICOS] |
| Próximos plazos | [RELLENO — p. ej., envío de datos del equipo, lista de verificación de preparación] |
| Instrucciones para participantes del SGC adjuntas o vinculadas | [RELLENO] |
| Contacto de cambio/cancelación | David Pulgarín — `calaire_med@unal.edu.co` |
| **Plazo para confirmar la recepción** | 5 días hábiles desde el envío. Si no hay respuesta, se realiza y registra seguimiento; no se libera un cupo confirmado por pago u orden aceptada sin aplicar el proceso formal de cancelación. |

### Plantilla

```text
Asunto: CALAIRE-EA — Ronda [ID] — Participante [CÓDIGO] — Confirmación

Estimado/a [CONTACTO]:

Su inscripción en la ronda [ID] de CALAIRE-EA está confirmada.

Código de participante: [CÓDIGO]
Gases seleccionados: [GASES]
Analizadores confirmados: [CANTIDAD]
Participantes adicionales de su organización: [LISTA o «ninguno»]
Fechas: [FECHAS]
Ubicación: [UBICACIÓN]

Estado del pago / orden de compra: [ESTADO]

Esta confirmación es válida hasta el [FECHA]. Si para entonces no recibimos acuse de recibo, se liberará el cupo y su inscripción pasará a la lista de espera (se conservará la prioridad según la sección 7 de CS-01).

Próximos pasos y plazos:
- [RELLENO]

Adjuntamos las instrucciones para participantes y el cronograma.

Consultas técnicas: [CONTACTO TÉCNICO]
Consultas administrativas: [CONTACTO ADMINISTRATIVO]
Cambios / cancelación: [CONTACTO PARA CAMBIOS]

Cordialmente,
[COORDINADOR DE RONDA]
```

## Mensaje de lista de espera

Cuando un cliente está en lista de espera (la verificación 4 o 6 del CS-09 falla porque la capacidad está agotada), el coordinador de la ronda envía este mensaje:

### Plantilla

```text
Asunto: CALAIRE-EA — Ronda [ID] — [ORGANIZACIÓN] — En lista de espera

Estimado/a [CONTACTO]:

Gracias por su interés en la ronda [ID] de CALAIRE-EA.

Lamentablemente, la ronda alcanzó la capacidad disponible para la configuración seleccionada. Su inscripción quedó en lista de espera.

Prioridad en la lista de espera: [POSICIÓN]
Fecha de ingreso a la lista de espera: [FECHA]
Gases seleccionados: [GASES]
Fechas de la ronda: [FECHAS]

Nos comunicaremos con usted en un plazo de 5 días hábiles si se libera un cupo. Si no se libera ninguno, a más tardar en la fecha de decisión de inscripción mínima [FECHA] le ofreceremos una de estas opciones:
- Trasladar su inscripción a la siguiente ronda programada; O
- Emitir un reembolso total / nota crédito (según la sección 8 de CS-01).

No necesita realizar ninguna acción para permanecer en la lista de espera. Si desea retirarse, comuníquese con [CONTACTO COMERCIAL].

Cordialmente,
[COORDINADOR DE RONDA]
```

## Mensaje de rechazo

Cuando se rechaza un registro (la verificación CS-09 falla por un motivo no relacionado con la capacidad, por ejemplo, incompatibilidad de equipo, términos de orden de compra contradictorios, conflicto de intereses), el coordinador de la ronda envía este mensaje:

### Plantilla

```text
Asunto: CALAIRE-EA — Ronda [ID] — [ORGANIZACIÓN] — Inscripción no aceptada

Estimado/a [CONTACTO]:

Gracias por su interés en la ronda [ID] de CALAIRE-EA.

Tras la revisión del contrato (CS-09), no podemos aceptar su inscripción para esta ronda. El motivo es:

[MOTIVO — p. ej., «El certificado de calibración del equipo vence antes del inicio de la ronda», «La cláusula 7 de la orden de compra contradice los términos de cancelación de CS-08», «Conflicto de interés remitido al control de imparcialidad del SGC»]

Si considera que esta decisión es errónea, puede:
- Solicitar una revisión por parte del líder comercial en un plazo de 10 días hábiles; O
- Presentar una inscripción corregida para una ronda posterior.

Quedamos a su disposición para futuras rondas.

Cordialmente,
[COORDINADOR DE RONDA]
```

## Paquete de incorporación

No cree nuevos documentos técnicos. Empaquetar los materiales existentes aprobados aplicables a ese participante:

| Documento | Referencia del SGC | Propósito |
|---|---|---|
| Protocolo detallado de participación | DG-PSEA-01 (o sucesor aprobado) | Guía técnica de ejecución |
| Instrucciones de embalaje/transporte | I-PSEA-01 | Cuando corresponda |
| instrucciones para participantes de la aplicación calaire | I-PSEA-02 | Guía de envío de datos |
| Anexo técnico/equipamiento | `F-PSEA-04` (post-renumeración 2026-06-14; antiguo `F-PSEA-05A`) | Verificar la compatibilidad del equipo |
| Registro de participantes | `F-PSEA-03` (antiguo `F-PSEA-05`) | Identidad y datos administrativos |
| Horario actual | Generado a través de la planificación PEAS existente | Línea de tiempo redonda |
| Información sobre instalaciones y seguridad | [RELLENO — documento fijo, no por ronda] | Requisitos locales |
| Canal oficial de comunicación | [RELLENO] | Correo electrónico / portal / grupo |

## Traspaso al SGC

La lista de participantes confirmados se exporta a:

- Planificación de la ronda `P-PSEA-04` y registro de participantes `F-PSEA-03` (antiguo `F-PSEA-05`)
- Anexo técnico/equipamiento `F-PSEA-04` (antiguo `F-PSEA-05A`) y `calaire-app` para captura de datos técnicos
- Procedimiento de comunicaciones `P-PSEA-05`

**Nota sobre equivalencia de códigos:** ver `00_control/equivalencia_codigos_sgc.md`. El SGC renumeró los códigos el 2026-06-14; las referencias anteriores son las vigentes.

## Aprobación

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
