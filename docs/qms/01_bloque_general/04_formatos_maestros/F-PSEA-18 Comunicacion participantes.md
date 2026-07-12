# F-PSEA-18: Comunicacion a participantes

**Codigo:** F-PSEA-18  
**Tipo documental:** Formato / Registro  
**Nombre:** Comunicacion a participantes  
**Version:** 1.0  
**Fecha:** 2026-06-27  
**Estado:** Preliminar — Revisar  
**Clase:** Plantilla maestra de comunicacion operativa

---

## 1. Objetivo

Estandarizar y registrar las comunicaciones formales enviadas a participantes del PEA durante la planificacion, preparacion, ejecucion y cierre de una ronda de ensayo de aptitud, asegurando claridad, trazabilidad documental, control de destinatarios y conservacion de la evidencia.

## 2. Alcance

Este formato aplica a comunicaciones dirigidas a participantes cuando se requiera informar, solicitar o confirmar aspectos operativos de una ronda, incluyendo:

- Invitacion, confirmacion o actualizacion de participacion.
- Fechas de instalacion, medicion, desmontaje o devolucion de equipos.
- Solicitud de diligenciamiento de formularios o envio de informacion.
- Envio de calendario, cronograma, instrucciones tecnicas o documentos controlados.
- Cambios relevantes de programacion, lugar, condiciones logisticas o documentos aplicables.
- Recordatorios de acciones pendientes antes, durante o despues de la ronda.

No incluye:

- Informes finales de resultados (eso se documenta en `F-PSEA-13`).
- Reporte de datos de medicion por participante (eso se gestiona en `F-PSEA-08`).
- Quejas, no conformidades o apelaciones formales (eso se gestiona en `F-PSEA-14` y `F-PSEA-15`).
- Comunicaciones internas sin destinatario participante.

## 3. Responsable funcional

| Rol | Responsabilidad |
|---|---|
| Coordinador de ronda | Definir el objetivo de la comunicacion, validar fechas, destinatarios y documentos adjuntos. |
| Lider tecnico | Revisar el contenido tecnico asociado a analitos, medicion, equipos, cronograma y condiciones de ronda. |
| Responsable de calidad | Verificar que la comunicacion sea trazable, no divulgue informacion sensible no autorizada y remita a documentos vigentes. |
| Responsable de emision | Enviar la comunicacion por canal autorizado y conservar la evidencia de envio, adjuntos y respuestas. |
| Participante | Revisar la comunicacion, ejecutar las acciones solicitadas y responder dentro del plazo indicado, cuando aplique. |

## 4. Momento de uso

- Antes de la ronda, para confirmar fechas, participantes, documentos y requerimientos logisticos.
- Durante la ronda, para comunicar instrucciones operativas, cambios aprobados o aclaraciones generales.
- Despues de la ronda, para solicitar informacion pendiente, confirmar recepcion de datos o comunicar hitos de cierre.
- Cada vez que una comunicacion a participantes afecte el cronograma, la preparacion de equipos, la disponibilidad del item, la entrega de datos o la trazabilidad del esquema.

## 5. Campos minimos del registro

| Campo | Descripcion |
|---|---|
| ID_comunicacion | Codigo unico de la comunicacion, por ejemplo `COM-AAAA-RONDA-NNN`. |
| Codigo_ronda | Identificacion de la ronda o prueba piloto a la que aplica. |
| Consecutivo_comunicacion | Numero de comunicacion dentro de la ronda, por ejemplo primera, segunda, tercera. |
| Fecha_emision | Fecha de envio de la comunicacion. |
| Hora_emision | Hora de envio, cuando sea relevante. |
| Emisor | Nombre, cargo y correo de quien envia. |
| Destinatario_principal | Nombre, entidad y correo del participante titular. |
| Destinatarios_copia | Personas en copia, si aplica. |
| Codigo_participante | Codigo anonimo u operativo del participante, por ejemplo `P1`, `P2`. |
| Canal | Correo institucional, `calaire-app`, reunion documentada u otro canal autorizado por `P-PSEA-05`. |
| Asunto | Asunto exacto usado en el mensaje. |
| Proposito | Motivo principal de la comunicacion. |
| Resumen_contenido | Sintesis de la informacion enviada o solicitada. |
| Accion_requerida | Actividad que debe realizar el participante, si aplica. |
| Fecha_limite_respuesta | Plazo para respuesta o entrega de informacion. |
| Documentos_adjuntos | Codigos y nombres de documentos enviados. |
| Evidencia_envio | Ruta, enlace, copia de correo, captura o registro que demuestra la emision. |
| Evidencia_respuesta | Acuse, correo de respuesta, archivo diligenciado o registro asociado. |
| Responsable_seguimiento | Persona encargada de verificar cumplimiento de la accion solicitada. |
| Estado | Borrador / Emitida / Respondida / Cerrada / Escalada. |
| Observaciones | Notas de seguimiento, aclaraciones o desviaciones. |

## 6. Estructura general de la comunicacion

La comunicacion debe redactarse de forma clara y directa. Como minimo debe contener:

1. Encabezado con remitente, destinatario y asunto.
2. Saludo personalizado o institucional.
3. Proposito de la comunicacion.
4. Informacion principal organizada por temas.
5. Acciones requeridas al participante, con fecha limite.
6. Tabla de fechas o hitos, cuando aplique.
7. Tabla de documentos adjuntos, cuando aplique.
8. Datos de contacto para dudas.
9. Firma institucional del PEA.

## 7. Plantilla base de mensaje

```text
De: [Nombre emisor] - [correo institucional]
Para: [Nombre participante] - [correo participante]
CC: [copias, si aplica]
Asunto: [Tema principal] - EA CALAIRE-EA [ronda / periodo]

Estimado/a [nombre]:

Espero se encuentre bien. Le escribimos para [proposito de la comunicacion].

1. [Tema principal]

[Texto breve con la informacion relevante.]

| Ronda | Analitos | Instalacion | Medicion | Devolucion / cierre |
|---|---|---|---|---|
| [Nombre ronda] | [Analitos] | [Fecha] | [Fecha(s)] | [Fecha] |

[Nota aclaratoria si existe un festivo, cambio logistico o condicion especial.]

2. Accion requerida

Por favor [accion solicitada] antes del [fecha limite], incluyendo:

- [Dato/documento requerido 1]
- [Dato/documento requerido 2]
- [Dato/documento requerido 3]

3. Documentos adjuntos

| Codigo | Documento | Accion esperada |
|---|---|---|
| [F-PSEA-XX] | [Nombre documento] | [Diligenciar / revisar / conservar] |

Cualquier duda, puede contactarnos por los canales oficiales:

[Nombre contacto 1] - [cargo]
[telefono] - [correo]

[Nombre contacto 2] - [cargo]
[telefono] - [correo]

Proyecto CALAIRE-EA - Laboratorio CALAIRE
Facultad de Minas, Universidad Nacional de Colombia, Sede Medellin
```

## 8. Ejemplo de uso: actualizacion de fechas y formulario de registro

```text
De: Wilson Rafael Salas Chavez - calaire_med@unal.edu.co
Para: [Nombre participante] - [correo participante]
Asunto: Actualizacion de fechas y formulario de registro - EA CALAIRE-EA Prueba Piloto 2026

Estimado/a [nombre]:

Espero se encuentre bien. Le escribimos con dos novedades importantes antes del inicio de la prueba piloto:

1. Fechas actualizadas

A continuacion se presentan las fechas confirmadas para su participacion:

| Ronda | Analitos | Instalacion | Medicion | Devolucion |
|---|---|---|---|---|
| [Ronda Simple - P1, si aplica] | [CO, SO2] | [fecha] | [fecha] | [fecha] |
| [Ronda Compleja - P1 + P2, si aplica] | [O3, NO, NO2 / CO, SO2] | [fecha] | [fecha(s)] | [fecha] |

[Nota sobre festivos o condiciones especiales, si aplica.]

El calendario y el cronograma detallado de actividades se adjuntan a este correo.

2. Formulario de registro

Para gestionar el permiso de ingreso al campus (Bloque 19A, Universidad Nacional de Colombia, Sede Medellin) necesitamos sus datos con anticipacion. Sin este tramite no podra ingresar con sus equipos el dia de la ronda.

Por favor diligenciar o actualizar en `calaire-app` el F-PSEA-03 - Registro de participacion antes del [fecha limite], incluyendo:

- Datos personales y de acompanantes requeridos para el permiso de ingreso.
- Analizadores y equipos que traera, incluyendo marca, modelo y serial.
- Medio de transporte y hora estimada de llegada.

Documentos adjuntos:

| Codigo | Documento |
|---|---|
| F-PSEA-03 | Registro de participacion y carga de datos del participante |
| F-PSEA-01 | Calendario actualizado de la prueba piloto |
| F-PSEA-02 | Cronograma detallado de actividades |

Cualquier duda, no dude en contactarnos.

[Firma institucional]
```

## 9. Controles de calidad

- La comunicacion debe emitirse por un canal autorizado en `P-PSEA-05`.
- El asunto, destinatarios, fecha, adjuntos y contenido enviado deben conservarse como evidencia.
- Las fechas, analitos, documentos y codigos de participante deben coincidir con el plan de ronda vigente (`F-PSEA-05`) y el calendario/cronograma aplicable (`F-PSEA-01`, `F-PSEA-02`).
- Si se solicita diligenciar un formato, la comunicacion debe indicar fecha limite, responsable de recepcion y documento esperado.
- No se deben divulgar resultados individuales, valores asignados, codigos de otros participantes ni informacion sensible no autorizada.
- Si la comunicacion genera una queja, no conformidad o apelacion, debe escalarse al registro correspondiente.
- Las copias diligenciadas o evidencias de respuesta deben archivarse junto con la ronda correspondiente.

## 10. Relaciones documentales

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-05` | Procedimiento de comunicaciones del PEA. | Obligatorio |
| `F-PSEA-05` | Ficha basica de ronda EA que resume identificacion, alcance, fechas y registros asociados. | Referencia |
| `F-PSEA-03` | Registro de participacion que puede solicitarse mediante esta comunicacion. | Obligatorio cuando aplique |
| `F-PSEA-06` | Planificacion completa de ronda que define condiciones operativas. | Obligatorio |
| `F-PSEA-01` | Calendario de la ronda o prueba piloto. | Referencia |
| `F-PSEA-02` | Cronograma detallado de actividades. | Referencia |
| `F-PSEA-08` | Datos reportados por participante, cuando la comunicacion solicite o aclare reporte de datos. | Referencia |
| `F-PSEA-13` | Informe final de resultados, cuando la comunicacion se relacione con emision o cierre. | Referencia |
| `F-PSEA-14` | Registro de queja o no conformidad, si la comunicacion deriva en caso formal. | Condicional |
| `F-PSEA-15` | Registro de apelaciones, si la comunicacion deriva en apelacion formal. | Condicional |
| `P-PSEA-16` | Divulgacion y control de valores sensibles. | Obligatorio |
| `P-PSEA-19` | Confidencialidad operativa interna del PEA. | Obligatorio |

## 11. Limites

- Este formato no reemplaza el procedimiento `P-PSEA-05`; solo normaliza y registra comunicaciones a participantes.
- No sustituye los formatos tecnicos que se adjuntan o solicitan en la comunicacion.
- No debe usarse para emitir resultados oficiales en lugar de `F-PSEA-13`.
- No reemplaza los registros de quejas, no conformidades o apelaciones cuando la comunicacion derive en esos procesos.
- La plantilla debe personalizarse segun participante, ronda, analitos, fechas y documentos vigentes.
