# CS-11 — Paquete de confirmación e incorporación

<<<<<<< Updated upstream
**Propietario:** Líder técnico
**Última revisión:** 2026-07-14 (se agregaron plantillas de lista de espera y rechazo, regla de vencimiento de confirmación, campo de participantes adicionales, corrección de referencias de código SGC)
=======
**Estado:** BORRADOR — contenido redactado; aprobación pendiente\
**Propietario:** Coordinador de ronda\
**Requerido antes de:** preparación técnica\
**Última revisión:** 2026-07-14 (se agregaron plantillas de lista de espera y rechazo, regla de vencimiento de confirmación, campo de participantes adicionales, corrección de referencias de códigos SGC)\
>>>>>>> Stashed changes
**Referencia de códigos del SGC:** ver `00_control/equivalencia_codigos_sgc.md`. Las referencias al SGC usan los códigos vigentes tras la renumeración del 2026-06-14.

## Objetivo

Confirmar la compra y traspasarla al SGC. Este artefacto también cubre los mensajes de **lista de espera** y de **rechazo** enviados a clientes cuya inscripción no se puede confirmar.

## Mensaje de confirmación

### Campos obligatorios

| Campo | Valor |
|---|---|
<<<<<<< Updated upstream
| Nombre legal del cliente | [POR DILIGENCIAR] |
| Identificación de la ronda | [POR DILIGENCIAR] |
| Código de participante | [POR DILIGENCIAR — asignado por el SGC] |
| Gas o gases seleccionados | [POR DILIGENCIAR] |
| Cantidad de analizadores confirmados | [POR DILIGENCIAR] |
| Fechas y ubicación | [POR DILIGENCIAR] |
| Estado de pago/orden de compra | [POR DILIGENCIAR] |
| Contacto técnico principal | Líder técnico — `calaire_med@unal.edu.co` |
| Contacto administrativo principal | Profesional de proyectos — `calaire_med@unal.edu.co` |
| Participantes adicionales de la misma organización (si los hay) | [POR DILIGENCIAR — NOMBRES, CORREOS ELECTRÓNICOS] |
| Próximos plazos | [POR DILIGENCIAR — p. ej., envío de datos del equipo, lista de verificación de preparación] |
| Instrucciones para participantes del SGC adjuntas o vinculadas | [POR DILIGENCIAR] |
| Contacto de cambio/cancelación | Profesional de proyectos — `calaire_med@unal.edu.co` |
=======
| Razón social del cliente | Según CS-07 |
| Identificación de la ronda | Según CS-03 |
| Código de participante | Asignado por el SGC |
| Bloques seleccionados | Según la cotización aceptada |
| Cantidad de analizadores confirmados | Según CS-09 |
| Fechas y ubicación | Según CS-03 |
| Estado de pago / orden de compra | Según CS-10 |
| Contacto técnico principal | Wilson Salas — `calaire_med@unal.edu.co` |
| Contacto administrativo principal | David Pulgarín — `calaire_med@unal.edu.co` |
| Participantes adicionales de la misma organización | Nombres y correos, si los hay |
| Próximos plazos | Envío de datos del equipo (`F-PSEA-04`) y lista de verificación de preparación, según el cronograma de la ronda |
| Instrucciones del SGC para participantes | Paquete de incorporación (sección siguiente) |
| Contacto de cambio/cancelación | David Pulgarín — `calaire_med@unal.edu.co` |
>>>>>>> Stashed changes
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

Le agradecemos confirmar la recepción de este mensaje dentro de los 5 días
hábiles siguientes.

Próximos pasos y plazos:
<<<<<<< Updated upstream
- [POR DILIGENCIAR]
=======
- Enviar los datos técnicos del equipo (F-PSEA-04) antes del [FECHA].
- Completar la lista de verificación de preparación antes del [FECHA].
>>>>>>> Stashed changes

Adjuntamos las instrucciones para participantes y el cronograma.

Consultas técnicas: Wilson Salas — calaire_med@unal.edu.co
Consultas administrativas: David Pulgarín — calaire_med@unal.edu.co
Cambios / cancelación: David Pulgarín — calaire_med@unal.edu.co

Cordialmente,
<<<<<<< Updated upstream
[DIRECTORA DEL GRUPO]
=======
Carmen Elena Zapata
Coordinadora de ronda — CALAIRE-EA
>>>>>>> Stashed changes
```

## Mensaje de lista de espera

Cuando un cliente está en lista de espera (la verificación 4 o 6 del CS-09 falla porque la capacidad está agotada), la Directora del grupo envía este mensaje:

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
- Trasladar su inscripción a la siguiente ronda programada; o
- Emitir un reembolso total / nota crédito (según la sección 8 de CS-01).

No necesita realizar ninguna acción para permanecer en la lista de espera. Si desea retirarse, escriba a calaire_med@unal.edu.co.

Cordialmente,
<<<<<<< Updated upstream
[DIRECTORA DEL GRUPO]
=======
Carmen Elena Zapata
Coordinadora de ronda — CALAIRE-EA
>>>>>>> Stashed changes
```

## Mensaje de rechazo

Cuando se rechaza un registro (la verificación CS-09 falla por un motivo no relacionado con la capacidad, por ejemplo, incompatibilidad de equipo, términos de orden de compra contradictorios, conflicto de intereses), la Directora del grupo envía este mensaje:

### Plantilla

```text
Asunto: CALAIRE-EA — Ronda [ID] — [ORGANIZACIÓN] — Inscripción no aceptada

Estimado/a [CONTACTO]:

Gracias por su interés en la ronda [ID] de CALAIRE-EA.

Tras la revisión del contrato (CS-09), no podemos aceptar su inscripción para esta ronda. El motivo es:

[MOTIVO — p. ej., «El certificado de calibración del equipo vence antes del inicio de la ronda», «La cláusula 7 de la orden de compra contradice los términos de cancelación de CS-08», «Conflicto de interés remitido al control de imparcialidad del SGC»]

Si considera que esta decisión es errónea, puede:
<<<<<<< Updated upstream
- Solicitar una revisión por parte del profesional de proyectos en un plazo de 10 días hábiles; O
=======
- Solicitar una revisión por parte del líder comercial en un plazo de 10 días hábiles; o
>>>>>>> Stashed changes
- Presentar una inscripción corregida para una ronda posterior.

Quedamos a su disposición para futuras rondas.

Cordialmente,
<<<<<<< Updated upstream
[DIRECTORA DEL GRUPO]
=======
Carmen Elena Zapata
Coordinadora de ronda — CALAIRE-EA
>>>>>>> Stashed changes
```

## Paquete de incorporación

No se crean documentos técnicos nuevos. Se empaquetan los materiales aprobados existentes aplicables a ese participante:

| Documento | Referencia del SGC | Propósito |
|---|---|---|
| Protocolo detallado de participación | DG-PSEA-01 (o sucesor aprobado) | Guía técnica de ejecución |
| Instrucciones de embalaje / transporte | I-PSEA-01 | Cuando corresponda |
| Instrucciones para participantes de `calaire-app` | I-PSEA-02 | Guía de envío de datos |
| Anexo técnico de equipos | `F-PSEA-04` (tras la renumeración del 2026-06-14; antiguo `F-PSEA-05A`) | Verificar la compatibilidad del equipo |
| Registro de participantes | `F-PSEA-03` (antiguo `F-PSEA-05`) | Identidad y datos administrativos |
<<<<<<< Updated upstream
| Horario actual | Generado a través de la planificación PEAS existente | Cronograma de la ronda |
| Información sobre instalaciones y seguridad | [POR DILIGENCIAR — documento fijo, no por ronda] | Requisitos locales |
| Canal oficial de comunicación | [POR DILIGENCIAR] | Correo electrónico / portal / grupo |
=======
| Cronograma vigente | Generado en la planificación existente del PEA (`F-PSEA-02`) | Línea de tiempo de la ronda |
| Información sobre instalaciones y seguridad | Documento fijo del laboratorio (no cambia por ronda) | Requisitos locales |
| Canal oficial de comunicación | `calaire_med@unal.edu.co` (`P-PSEA-05`) | Comunicaciones de la ronda |
>>>>>>> Stashed changes

## Traspaso al SGC

La lista de participantes confirmados se exporta a:

- Planificación de la ronda `P-PSEA-04` y registro de participantes `F-PSEA-03` (antiguo `F-PSEA-05`)
- Anexo técnico de equipos `F-PSEA-04` (antiguo `F-PSEA-05A`) y `calaire-app` para captura de datos técnicos
- Procedimiento de comunicaciones `P-PSEA-05`

**Nota sobre equivalencia de códigos:** ver `00_control/equivalencia_codigos_sgc.md`. El SGC renumeró los códigos el 2026-06-14; las referencias anteriores son las vigentes.
<<<<<<< Updated upstream
=======

## Aprobación

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | 2026-07-12 | — | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | — | Plantillas de lista de espera y rechazo, regla de acuse de recibo, participantes adicionales y códigos SGC corregidos |
>>>>>>> Stashed changes
