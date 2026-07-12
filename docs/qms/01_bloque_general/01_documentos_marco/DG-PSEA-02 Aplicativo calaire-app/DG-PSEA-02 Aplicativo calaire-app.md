# DG-PSEA-02: Aplicativo calaire-app

## 1. Objetivo

Documentar el alcance, funciones, entradas, salidas, controles y limites del aplicativo `calaire-app` como sistema digital del PEA para la gestion de rondas de ensayo de aptitud, participantes, cronogramas, comunicaciones, captura de datos, registros SGC y exportaciones oficiales hacia el flujo posterior de analisis.

El aplicativo debe permitir demostrar que la informacion operativa de la ronda se mantiene integra, trazable, confidencial y disponible para la revision tecnica y estadistica posterior.

## 2. Alcance

Aplica al uso de `calaire-app` durante las fases de planificacion, ejecucion de ronda, comunicacion operativa, recoleccion de datos, cierre de captura, control documental SGC y exportacion de informacion oficial del ensayo de aptitud para gases contaminantes criterio.

Incluye:

- Gestion de rondas de ensayo de aptitud.
- Registro, confirmacion y administracion de participantes.
- Configuracion de calendarios, cronogramas, analitos, niveles y ventanas de reporte.
- Generacion o consolidacion de la ficha basica de ronda (`F-PSEA-05`) y la planificacion completa (`F-PSEA-06`).
- Captura de datos reportados por los participantes (`F-PSEA-08`).
- Registro de participacion y carga de datos del participante (`F-PSEA-03`), con exportacion de equipos e instrumentos (`F-PSEA-04`).
- Control de usuarios, roles, permisos y acceso a informacion de participantes.
- Trazabilidad de registros, modificaciones, cierres, comunicaciones, notificaciones y exportaciones.
- Exportacion oficial de datos hacia `pt_app` (`F-PSEA-09`).
- Registro operativo de casos SGC de quejas, no conformidades, comunicaciones o incidencias cuando aplique.
- Evidencia de validacion funcional, control de cambios, respaldo, recuperacion y tratamiento de incidentes del aplicativo.

No incluye:

- Definicion de criterios estadisticos, valor asignado, `sigma_pt`, incertidumbre ni reglas de desempeno.
- Preprocesamiento estadistico, evaluacion de homogeneidad/estabilidad ni emision del informe final.
- Aprobacion metodologica del esquema o de la ronda.
- Sustitucion de los procedimientos de comunicacion, planificacion, confidencialidad, trabajo no conforme, quejas o control documental del PEA.

## 3. Ficha del aplicativo

| Campo | Descripcion |
|---|---|
| Aplicativo | `calaire-app` |
| Uso previsto | Planificacion operativa, gestion de participantes, captura controlada de datos, generacion de ficha digital, control documental SGC, exportacion oficial hacia `pt_app` y registro operativo de casos SGC cuando aplique. |
| Rol en el SGC | Aplicativo critico para control de informacion, confidencialidad, trazabilidad, comunicaciones y transferencia de datos oficiales. |
| Requisitos relacionados | ISO/IEC 17043:2023: confidencialidad, comunicacion del esquema, instrucciones, manejo de resultados, registros, datos y sistemas de informacion. ISO 13528:2022: revision inicial de datos, trazabilidad de datos y control de herramientas que soportan el analisis. |
| Instructivos de uso | `I-PSEA-02`, `I-PSEA-03` |
| Procedimientos relacionados | `P-PSEA-03`, `P-PSEA-04`, `P-PSEA-05`, `P-PSEA-08`, `P-PSEA-14`, `P-PSEA-15`, `P-PSEA-17`, `P-PSEA-19` |

## 4. Evidencia visual del aplicativo

Las siguientes capturas se conservan en la subcarpeta `capturas` como evidencia funcional del aplicativo. Las imagenes fueron organizadas para soportar este documento descriptivo.

| Evidencia | Archivo | Control SGC soportado |
|---|---|---|
| Resumen SGC global | `capturas/01-resumen-sgc.png` | Seguimiento del estado general del SGC y visibilidad de registros por ronda. |
| Panel SGC de ronda y publicaciones | `capturas/02-panel-ronda-sgc-publicaciones.png` | Comunicacion controlada del esquema, publicaciones e instrucciones de ronda. |
| Comunicaciones SGC | `capturas/03-comunicaciones-sgc.png` | Registro de comunicaciones operativas y trazabilidad de mensajes. |
| Plantillas SGC | `capturas/04-plantillas-sgc.png` | Control de plantillas y documentos usados para comunicacion o publicacion. |
| Notificaciones y destinatarios | `capturas/05-notificaciones-destinatarios.png` | Evidencia de destinatarios, notificaciones y control de divulgacion. |
| Captura nativa `F-PSEA-08` | `capturas/06-f-psea-08-captura-datos.png` | Captura estructurada de resultados de participantes. |
| Casos SGC unificados | `capturas/07-casos-sgc.png` | Registro operativo de quejas, no conformidades o incidencias. |
| Matriz documental maestra | `capturas/08-matriz-documental-maestra.png` | Control documental del SGC y relacion de documentos aplicables. |
| Cobertura por ronda | `capturas/09-cobertura-por-ronda.png` | Verificacion de cobertura documental y registros por ronda. |
| Matriz documental filtrada | `capturas/10-matriz-documental.png` | Consulta y trazabilidad de documentos SGC aplicables. |

![Resumen SGC](capturas/01-resumen-sgc.png)

![Panel SGC de ronda y publicaciones](capturas/02-panel-ronda-sgc-publicaciones.png)

![Captura nativa F-PSEA-08](capturas/06-f-psea-08-captura-datos.png)

![Casos SGC unificados](capturas/07-casos-sgc.png)

![Matriz documental maestra](capturas/08-matriz-documental-maestra.png)

## 5. Requisitos minimos del aplicativo

| Requisito SGC | Control esperado en `calaire-app` |
|---|---|
| Confidencialidad de participantes | Acceso por rol, proteccion de identidad, visibilidad limitada por participante y restriccion de datos de otros laboratorios. |
| Comunicacion e instrucciones de ronda | Publicacion o registro de calendario, cronograma, ficha digital, instrucciones, notificaciones y cambios controlados. |
| Captura comparable de resultados | Campos estructurados, unidades definidas, validaciones basicas, ventanas de reporte y bloqueo o trazabilidad de cambios posteriores al cierre. |
| Trazabilidad de datos | Registro de ronda, participante, usuario, fecha/hora, identificador de ficha, origen del dato, estado del registro y exportacion asociada. |
| Integridad de datos | Controles para evitar sobrescritura no trazada, duplicados no autorizados, perdida de informacion o modificaciones sin justificacion. |
| Transferencia a `pt_app` | Exportacion oficial identificada como `F-PSEA-09`, con identificador de ronda, fecha/hora, responsable y estado de aprobacion. |
| Tratamiento de desviaciones | Registro de incidentes, correcciones, reaperturas, quejas o no conformidades conforme a los procedimientos SGC aplicables. |
| Control documental | Matriz documental, plantillas, versiones y cobertura por ronda para evidenciar documentos aplicables y registros requeridos. |
| Validacion y cambios | Evidencia de pruebas funcionales, revision de cambios y aprobacion antes de uso oficial o despues de modificaciones relevantes. |

## 6. Matriz de cumplimiento ISO/IEC 17043:2023

| Bloque ISO/IEC 17043 | Como aporta `calaire-app` | Evidencia o registro |
|---|---|---|
| Imparcialidad y confidencialidad | Restringe el acceso por rol y soporta codificacion de participantes para evitar divulgacion no autorizada. | Usuarios, permisos, codigos de participante, registros de acceso cuando aplique. |
| Comunicacion del esquema | Centraliza publicaciones, instrucciones, cronogramas, plantillas y notificaciones. | Panel SGC de ronda, comunicaciones, destinatarios y plantillas. |
| Planificacion de ronda | Permite registrar configuracion de ronda, participantes, fechas, analitos, niveles y responsables. | Ficha basica `F-PSEA-05`, planificacion `F-PSEA-06`, calendario, cronograma y estado de ronda. |
| Instrucciones a participantes | Mantiene instrucciones y documentos de reporte asociados a la ronda. | Publicaciones de ronda, plantillas y comunicaciones controladas. |
| Recepcion y manejo de resultados | Captura resultados de participantes en formularios estructurados y vinculados a ronda. | `F-PSEA-08`, estado de envio, fecha/hora y participante. |
| Registros, datos y sistemas de informacion | Conserva registros que permiten reconstruir la operacion de la ronda y la transferencia de datos. | Bitacora, matriz documental, cobertura por ronda y exportaciones. |
| Quejas, trabajo no conforme y acciones | Permite asociar casos SGC a rondas, participantes o comunicaciones cuando aplique. | Casos SGC, comentarios, estado, responsable y seguimiento. |
| Control de documentos y cambios | Relaciona documentos SGC, plantillas, versiones y cobertura documental por ronda. | Matriz documental maestra y cobertura por ronda. |

## 7. Matriz de cumplimiento ISO 13528:2022

`calaire-app` no ejecuta el calculo estadistico principal. Su aporte a ISO 13528 consiste en entregar datos completos, trazables y revisables para que el analisis posterior sea tecnicamente defendible.

| Bloque ISO 13528 | Como aporta `calaire-app` | Limite del aplicativo |
|---|---|---|
| Diseno estadistico del esquema | Conserva la configuracion operativa de ronda, analitos, niveles y datos esperados. | La justificacion estadistica del diseno se controla en el plan y en `pt_app` o documentos tecnicos. |
| Revision inicial de datos | Facilita revision de completitud, formatos, unidades, duplicados, datos faltantes y consistencia basica antes de exportar. | No decide exclusiones estadisticas ni tratamiento de valores atipicos. |
| Valor asignado e incertidumbre | Conserva los datos reportados y referencias de ronda que alimentan el analisis. | No determina valor asignado, incertidumbre ni `sigma_pt`. |
| Scores e interpretacion | Entrega la base de datos oficial para calculo posterior. | No emite z-score, z-prime, zeta-score ni clasificacion final de desempeno. |
| Validacion de herramientas | Debe contar con pruebas funcionales para captura, permisos, exportaciones y control documental. | La validacion estadistica de formulas y rutinas corresponde al sistema o herramienta de analisis. |
| Trazabilidad de calculo | Asegura origen, estado, usuario, fecha y ronda de cada dato reportado. | La trazabilidad de calculos estadisticos inicia despues de la exportacion oficial. |

## 8. Responsabilidades y uso

| Rol | Responsabilidad |
|---|---|
| Coordinador de ronda | Configurar o aprobar ronda, calendario, cronograma, ficha digital, participantes, comunicaciones y cierre operativo en `calaire-app`. |
| Administrador del aplicativo | Gestionar usuarios, permisos, parametrizacion, versiones del aplicativo, respaldos, trazabilidad tecnica y casos SGC habilitados. |
| Participante | Confirmar participacion, consultar informacion de ronda y registrar datos, equipos e instrumentos dentro de los plazos definidos. |
| Analista PT | Recibir y verificar que la exportacion oficial (`F-PSEA-09`) sea la entrada autorizada para el flujo en `pt_app`. |
| Responsable de calidad | Verificar controles de confidencialidad, registros, documentos, cambios, incidentes y evidencias del aplicativo frente al SGC. |
| Revisor tecnico | Revisar consistencia de datos exportados cuando existan alertas, correcciones, reaperturas o incidencias que puedan afectar la validez de la ronda. |

## 9. Entradas y salidas

### Entradas

| Entrada | Uso |
|---|---|
| Requisitos operativos PEA | Funciones requeridas para gestion de rondas, participantes, comunicaciones y captura. |
| `P-PSEA-04` | Base para configurar la planificacion de ronda. |
| `P-PSEA-05` | Base para controlar comunicaciones operativas. |
| `F-PSEA-05` | Ficha basica de ronda EA, cuando se use como resumen de configuracion. |
| `F-PSEA-06` | Planificacion de ronda EA, cuando se use como base completa de configuracion. |
| Participantes | Datos de contacto, confirmacion, equipos, instrumentos y resultados reportados. |
| Configuracion de ronda | Analitos, niveles, fechas, instrucciones, estado de ronda y responsables. |
| Registros SGC | Quejas, no conformidades, comunicaciones o incidentes asociados a la ronda. |

### Salidas

| Salida | Descripcion |
|---|---|
| `F-PSEA-01` | Calendario global de ronda. |
| `F-PSEA-02` | Cronograma detallado de ronda. |
| `F-PSEA-03` | Registro de participacion y carga de datos del participante. |
| `F-PSEA-04` | Equipos e instrumentos exportados desde F-PSEA-03. |
| `F-PSEA-05` | Ficha basica de ronda EA. |
| `F-PSEA-06` | Planificacion de ronda EA. |
| `F-PSEA-08` | Datos reportados por participante. |
| `F-PSEA-09` | Datos de participantes exportados para analisis PT. |
| `F-PSEA-14` | Caso SGC de queja o no conformidad, si aplica. |
| Bitacora del aplicativo | Evidencia de usuarios, cambios, exportaciones, cierres, reaperturas, incidentes y respaldos cuando aplique. |
| Registro de validacion/cambio | Evidencia de pruebas, version aprobada, cambios liberados y evaluacion de impacto. |

## 10. Campos minimos y trazabilidad

Cada ronda configurada en `calaire-app` debe registrar como minimo:

- Codigo y nombre de la ronda.
- Identificador de configuracion de la ronda.
- Periodo de ejecucion, ventanas de medicion y fechas limite de reporte.
- Analito(s), nivel(es) y magnitudes solicitadas.
- Laboratorios participantes, estado de confirmacion y codigo interno de participante.
- Responsable de la ronda y responsable de la configuracion.
- Identificador de la ficha basica de ronda (`F-PSEA-05`) y de la planificacion completa (`F-PSEA-06`).
- Estado de ronda: borrador, publicada, en captura, cerrada, exportada, anulada o equivalente.
- Historial de cambios relevantes con fecha, usuario, justificacion y aprobacion cuando aplique.

Cada participante debe registrar como minimo:

- Identificacion del laboratorio y codigo de participante usado para proteger su identidad en el flujo de evaluacion.
- Contacto operativo autorizado.
- Registro de participacion (`F-PSEA-03`) y equipos e instrumentos asociados (`F-PSEA-04`).
- Datos reportados por analito y nivel (`F-PSEA-08`).
- Usuario, fecha/hora y estado de envio de los datos.
- Correcciones, reemplazos o reaperturas autorizadas, con justificacion y responsable.

Cada exportacion oficial hacia `pt_app` debe registrar como minimo:

- Identificador de ronda.
- Consecutivo o identificador de exportacion.
- Fecha y hora de generacion.
- Responsable que genera y/o aprueba la exportacion.
- Alcance de datos incluidos.
- Estado de aprobacion para analisis.
- Referencia al archivo conservado como `F-PSEA-09`.
- Observaciones sobre datos faltantes, correcciones, exclusiones o alertas de consistencia.

## 11. Validacion, cambios y mantenimiento

`calaire-app` debe validarse antes de su uso oficial en una ronda y despues de cambios que puedan afectar captura, permisos, exportaciones, reglas de validacion, estructura de datos, reportes, seguridad o disponibilidad.

La evidencia minima de validacion o cambio debe incluir:

- Version del aplicativo, modulo o componente evaluado.
- Alcance de la prueba.
- Casos de prueba y resultado esperado.
- Datos de prueba usados, cuando aplique.
- Resultado obtenido y decision de aceptacion.
- Responsable de ejecucion, revision y aprobacion.
- Evaluacion de impacto sobre rondas abiertas, datos ya capturados o exportaciones emitidas.
- Acciones correctivas o restricciones de uso si se detectan fallas.

Los cambios no deben liberarse para uso oficial si no existe aprobacion del responsable autorizado. Cuando un cambio afecte datos ya reportados, exportaciones oficiales o confidencialidad, debe evaluarse si corresponde registrar trabajo no conforme, no conformidad, accion correctiva o comunicacion controlada.

## 12. Controles operativos

- El acceso al aplicativo debe estar acotado por rol y revisarse ante altas, bajas, cambios de funciones o cierre de ronda.
- Las credenciales de participantes son personales o institucionales controladas y no deben permitir acceso a datos de otros participantes.
- La identidad de participantes debe protegerse en las exportaciones y reportes segun las reglas del PEA.
- Los cambios en calendario, cronograma, ficha digital o instrucciones deben quedar trazables y comunicarse por el canal definido.
- La captura de resultados debe cerrarse segun el cronograma aprobado; cualquier reapertura debe quedar justificada.
- Las exportaciones hacia `pt_app` deben identificarse, conservarse como `F-PSEA-09` y no sobrescribirse sin trazabilidad.
- Los datos exportados deben someterse a una revision de completitud y consistencia antes de su uso analitico.
- Las fallas de disponibilidad, perdida de datos, errores de permisos, exposicion de informacion o exportaciones incorrectas deben registrarse y evaluarse por impacto en la validez de la ronda.
- Deben existir respaldos o mecanismos de recuperacion proporcionales al riesgo de perdida de informacion oficial.
- La documentacion tecnica interna del aplicativo debe mantenerse como soporte controlado, aunque no sustituye este documento general.

## 13. Documentos relacionados

| Codigo | Relacion |
|---|---|
| `I-PSEA-02` | Instructivo de uso de `calaire-app` por participante. |
| `I-PSEA-03` | Instructivo de administracion de rondas en `calaire-app`. |
| `P-PSEA-03` | Control de registros y evidencias del PEA. |
| `P-PSEA-04` | Procedimiento de planificacion de ronda que usa el aplicativo. |
| `P-PSEA-05` | Procedimiento de comunicaciones que usa el aplicativo. |
| `P-PSEA-08` | Flujo tecnico de datos digitales del PEA. |
| `P-PSEA-14` | Control de colusion y falsificacion, cuando los datos del aplicativo generen alertas. |
| `P-PSEA-15` | Trabajo no conforme, no conformidades y acciones correctivas. |
| `P-PSEA-17` | Procedimiento de quejas del PEA gestionadas como casos SGC. |
| `P-PSEA-19` | Confidencialidad operativa interna del PEA. |
| `DG-PSEA-03` | Aplicativo `pt_app` que recibe las exportaciones oficiales. |

## 14. Limites

- No es un formato `F-PSEA`.
- No es un instructivo de uso; la operacion se documenta en `I-PSEA-02` e `I-PSEA-03`.
- No define criterios estadisticos, valor asignado, `sigma_pt`, incertidumbre ni reglas de desempeno.
- No genera el informe final de resultados ni el analisis estadistico.
- No reemplaza procedimientos de planificacion, comunicaciones, confidencialidad, quejas, trabajo no conforme ni control documental.
- No convierte la documentacion tecnica del software en registro oficial de ronda salvo que sea referenciada por `P-PSEA-03` o `P-PSEA-08`.

**Nota:** La documentacion tecnica interna de `calaire-app` se mantiene como soporte del aplicativo y no sustituye este documento codificado.
