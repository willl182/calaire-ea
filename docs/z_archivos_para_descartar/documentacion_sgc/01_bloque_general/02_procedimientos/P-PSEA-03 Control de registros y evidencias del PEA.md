# P-PSEA-03 Control de registros y evidencias del PEA

## Objetivo

Definir como se identifican, clasifican, registran, verifican y cierran los registros y evidencias generadas por rondas, eventos o periodos del Programa de Ensayos de Aptitud para Gases Contaminantes Criterio.

## Alcance

Aplica a registros, formatos diligenciados, evidencias tecnicas, exportaciones digitales, anexos CSV conservados y soportes trazables generados durante la planificacion, ejecucion, analisis, informe y gestion de casos del PEA. No lista el universo documental maestro del sistema; esa funcion corresponde a `P-PSEA-02`.

## Principios de control

1. Cada evidencia debe asociarse con una ronda, evento o periodo de control.
2. Cada registro debe tener codigo o identificador, origen, responsable, fecha de generacion, ubicacion y estado.
3. Los formatos maestros no se tratan como evidencia hasta que son diligenciados, exportados o emitidos para una ronda especifica.
4. Los datos provenientes de `calaire-app` y `pt_app` deben conservar trazabilidad de aplicativo, version o exportacion cuando aplique.
5. Los CSV tecnicos solo se conservan como evidencia cuando soportan una decision, calculo, validacion, trazabilidad de datos o reconstruccion del resultado.
6. La matriz de evidencias se actualiza antes del cierre documental de la ronda y antes de emitir el informe final.

## Responsabilidades

| Rol | Responsabilidad |
|---|---|
| Coordinacion del PEA | Definir la evidencia requerida para cada ronda y aprobar el cierre documental. |
| Responsable tecnico de ronda | Verificar que los registros tecnicos esten completos, fechados y vinculados al flujo operativo. |
| Responsable de datos / aplicativos | Conservar exportaciones, registros de preprocesamiento, datasets oficiales y salidas de `pt_app`. |
| Responsable SGC | Revisar consistencia documental, codificacion, control de cambios, casos de queja, no conformidad o apelacion. |
| Participante | Registrar informacion solicitada en `calaire-app` y remitir aclaraciones cuando se requiera correccion trazable. |

## Flujo de control de registros y evidencias

1. **Apertura de ronda o evento:** se crea identificador de ronda, se define carpeta operativa y se relacionan formatos esperados.
2. **Planificacion:** se registran calendario, cronograma, ficha digital, plan de ronda, participacion y anexos tecnicos.
3. **Ejecucion tecnica:** se conservan registros de preparacion/control del item, datos reportados y soportes de homogeneidad/estabilidad.
4. **Flujo digital:** se controlan exportaciones desde `calaire-app`, registros de preprocesamiento, subformatos H/E y dataset oficial consolidado conforme a `P-PSEA-08`.
5. **Analisis e informe:** se verifica que resultados, graficas, tablas, criterios de desempeno e informe final tengan soporte trazable.
6. **Casos SGC:** se registran quejas, apelaciones, trabajo no conforme, no conformidades, acciones correctivas o indicios de colusion cuando se presenten.
7. **Cierre:** se valida completitud, ubicacion, version, responsable y estado de cada evidencia antes del cierre de ronda.

## Clasificacion de registros y evidencias

| Clase | Descripcion | Ejemplos | Control minimo |
|---|---|---|---|
| Registro oficial | Evidencia formal de una actividad, decision, resultado o comunicacion del PEA. | `F-PSEA-03`, `F-PSEA-05`, `F-PSEA-13`, actas o comunicaciones formales. | Codigo, ronda, fecha, responsable, version/estado y ubicacion. |
| Evidencia tecnica | Soporte que demuestra preparacion, medicion, analisis o verificacion tecnica. | `F-PSEA-07`, `F-PSEA-10`, `F-PSEA-11`, `F-PSEA-12`. | Trazabilidad de equipo/dato, responsable tecnico y relacion con procedimiento. |
| Anexo digital trazable | Archivo digital conservado para reconstruir el flujo de datos o verificar resultados. | CSV exportado, CSV preprocesado, dataset consolidado, salida H/E. | Origen, aplicativo, fecha, version, ruta y relacion con `P-PSEA-08`. |
| Soporte administrativo | Evidencia de gestion de participantes, agenda, comunicaciones o casos SGC. | `F-PSEA-02`, `F-PSEA-14`, `F-PSEA-15`. | Responsable, fecha, asunto, estado y relacion con procedimiento aplicable. |
| Archivo transitorio | Archivo temporal usado para trabajo operativo sin valor de evidencia permanente. | Borradores intermedios, descargas duplicadas, pruebas de carga. | No se conserva como evidencia; se depura o se deja fuera del cierre. |

## Matriz resumen de registros y evidencias

| Codigo / evidencia | Nombre | Origen | Momento de generacion | Responsable primario | Tipo de evidencia | Relacion documental |
|---|---|---|---|---|---|---|
| `F-PSEA-01` | Calendario global de ronda | `calaire-app` / planificacion | Apertura y planificacion | Coordinacion del PEA | Soporte administrativo | `P-PSEA-04`, `F-PSEA-05` |
| `F-PSEA-02` | Cronograma detallado de ronda | `calaire-app` / formato maestro | Planificacion detallada | Coordinacion del PEA | Soporte administrativo / evidencia de planificacion | `P-PSEA-04`, `F-PSEA-05` |
| `F-PSEA-03` | Registro de participacion | `calaire-app` | Inscripcion, confirmacion y cierre de participacion | Coordinacion del PEA | Registro oficial | `P-PSEA-04`, `P-PSEA-05`, `F-PSEA-09` |
| `F-PSEA-04` | Equipos e instrumentos | Participante / `calaire-app` | Inscripcion tecnica y preparacion de analisis | Participante / Responsable tecnico | Evidencia tecnica | `F-PSEA-03`, `F-PSEA-09`, `P-PSEA-08` |
| `F-PSEA-05` | Plan de ronda EA | Coordinacion del PEA | Antes de ejecucion | Coordinacion del PEA | Registro oficial de planificacion | `P-PSEA-04`, `F-PSEA-01`, `F-PSEA-02` |
| `F-PSEA-05A` | Hoja de registro del participante | Participante / anexo operativo | Durante registro o ejecucion | Participante / Coordinacion | Registro auxiliar | `F-PSEA-05`, `F-PSEA-07` |
| `F-PSEA-06` | Ficha digital de ronda EA | `calaire-app` | Apertura y actualizacion de ronda | Coordinacion / Responsable aplicativo | Registro digital estructurado | `P-PSEA-04`, `DG-PSEA-02` |
| `F-PSEA-07` | Preparacion y control del item | Responsable tecnico | Preparacion y control del item gaseoso | Responsable tecnico | Evidencia tecnica | `P-PSEA-06`, `P-PSEA-07` |
| `F-PSEA-08` | Datos reportados por participante | Participante / `calaire-app` | Reporte de resultados por participante | Participante | Registro oficial de datos reportados | `I-PSEA-02`, `P-PSEA-08` |
| `F-PSEA-09` | Datos de participantes exportados para analisis PT | `calaire-app` | Transferencia a `pt_app` | Responsable de datos | Anexo digital trazable | `I-PSEA-03`, `P-PSEA-08` |
| `F-PSEA-10` | Registro de preprocesamiento de datos | `pt_app` | Preprocesamiento | Responsable de datos | Evidencia tecnica | `I-PSEA-04`, `P-PSEA-08` |
| `F-PSEA-11` | Homogeneidad y estabilidad del item | `pt_app` / responsable tecnico | Evaluacion H/E | Responsable tecnico / Responsable de datos | Evidencia tecnica | `P-PSEA-06`, `P-PSEA-07` |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | `pt_app` | Preprocesamiento H/E | Responsable de datos | Anexo digital trazable | `F-PSEA-11`, `P-PSEA-08` |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | `pt_app` | Preprocesamiento H/E | Responsable de datos | Anexo digital trazable | `F-PSEA-11`, `P-PSEA-08` |
| `F-PSEA-11C` | Resultados de homogeneidad | `pt_app` | Evaluacion H/E | Responsable tecnico / datos | Evidencia tecnica | `F-PSEA-11`, `P-PSEA-07` |
| `F-PSEA-11D` | Resultados de estabilidad | `pt_app` | Evaluacion H/E | Responsable tecnico / datos | Evidencia tecnica | `F-PSEA-11`, `P-PSEA-07` |
| `F-PSEA-12` | Datos oficiales consolidados para evaluacion de aptitud | `pt_app` | Cierre de preprocesamiento | Responsable de datos | Dataset oficial / evidencia tecnica | `P-PSEA-07`, `P-PSEA-08`, `F-PSEA-13` |
| `F-PSEA-13` | Informe final de resultados | `pt_app` / Coordinacion | Cierre y emision | Coordinacion / Responsable tecnico | Registro oficial | `P-PSEA-09`, `P-PSEA-07` |
| `F-PSEA-14` | Registro caso de queja o NC segun aplique | Coordinacion / SGC | Cuando se presenta caso | Responsable SGC | Registro de gestion | `P-PSEA-15`, `P-PSEA-17` |
| `F-PSEA-15` | Registro de apelaciones | Coordinacion / SGC | Cuando se presenta apelacion | Responsable SGC | Registro de gestion | `P-PSEA-18` |
| `F-PSEA-16` | Matriz de competencia y autorizacion | Responsable SGC | Antes y durante ejecucion | Responsable SGC | Matriz de soporte | `P-PSEA-20` |
| `F-PSEA-17` | Evaluacion de proveedores criticos | Responsable SGC | Seleccion/evaluacion de proveedor | Responsable SGC | Registro de gestion | `P-PSEA-21` |
| CSV exportado desde `calaire-app` | Exportacion operativa de datos | `calaire-app` | Transferencia a analisis | Responsable de datos | Anexo digital trazable si se conserva | `P-PSEA-08`, `F-PSEA-09` |
| CSV preprocesado o consolidado | Archivo de trabajo reproducible | `pt_app` | Preprocesamiento / consolidacion | Responsable de datos | Evidencia tecnica si soporta resultados | `P-PSEA-08`, `F-PSEA-10`, `F-PSEA-12` |

## Matriz operativa anexa por ronda

Para cada ronda o evento se debe mantener una matriz operativa con los siguientes campos minimos:

| Campo | Descripcion |
|---|---|
| `ronda_evento` | Identificador de ronda, evento o periodo. |
| `codigo_evidencia` | Codigo `F-PSEA`, identificador de CSV o identificador de soporte. |
| `nombre_evidencia` | Nombre operativo del registro o archivo conservado. |
| `origen` | Aplicativo, responsable, participante, procedimiento o fuente. |
| `fecha_generacion` | Fecha de diligenciamiento, exportacion, emision o cierre. |
| `responsable` | Rol o persona responsable del registro. |
| `ubicacion` | Ruta, enlace o repositorio donde queda conservado. |
| `estado` | `pendiente`, `en_revision`, `completo`, `observado`, `cerrado` o `retirado`. |
| `relacion_documental` | Procedimiento, formato o informe que usa la evidencia. |
| `observaciones` | Correcciones, sustituciones, restricciones de confidencialidad o notas de trazabilidad. |

## Verificacion de completitud

Antes de cerrar una ronda se debe confirmar que:

- El cronograma detallado (`F-PSEA-02`) refleja actividades, responsables, fechas y dependencias relevantes.
- El registro de participacion (`F-PSEA-03`) incluye inscripcion, confirmacion, datos de contacto, estado de participacion y resultado final de cada laboratorio.
- Las exportaciones desde `calaire-app` estan vinculadas con los registros de participantes, equipos y datos reportados.
- El registro de preprocesamiento (`F-PSEA-10`) identifica entradas, salidas, fecha, version de herramienta y responsable.
- Los registros H/E (`F-PSEA-11`, `F-PSEA-11A-D`) quedan asociados con el item de ensayo, los datos procesados y los resultados aplicables.
- El dataset oficial (`F-PSEA-12`) coincide con el insumo usado para calculos de desempeno e informe final.
- El informe final (`F-PSEA-13`) cita o conserva las evidencias que soportan los resultados.
- Los casos de queja, apelacion, no conformidad o trabajo no conforme quedan registrados cuando apliquen.

## Control de cambios, correcciones y sustituciones

Cuando una evidencia se corrija o sustituya, la matriz operativa debe conservar:

1. identificador de la evidencia reemplazada;
2. razon de la correccion;
3. fecha y responsable de la sustitucion;
4. ubicacion de la version vigente;
5. decision sobre conservacion o retiro de la version anterior.

Las correcciones de datos reportados por participantes deben conservar trazabilidad de comunicacion y autorizacion, sin modificar silenciosamente el registro original.

## Documentos relacionados

| Codigo | Relacion |
|---|---|
| `P-PSEA-02` | Matriz documental maestra; diferencia documentos controlados de evidencias por ronda. |
| `P-PSEA-04` | Planificacion que genera registros de cronograma, participacion, ficha y plan de ronda. |
| `P-PSEA-06` | Preparacion y control del item que genera evidencias tecnicas. |
| `P-PSEA-07` | Diseno estadistico que usa H/E, dataset oficial y resultados. |
| `P-PSEA-08` | Flujo tecnico de datos digitales y clasificacion de CSV/anexos. |
| `P-PSEA-09` | Generacion y emision del informe final. |
| `DG-PSEA-02` | Aplicativo de origen para participantes, cronograma y datos reportados. |
| `DG-PSEA-03` | Aplicativo de preprocesamiento, analisis e informe. |
| `F-PSEA-02` | Cronograma detallado de ronda. |
| `F-PSEA-03` | Registro de participacion. |

## Limites

- No lista todos los documentos maestros del SGC; esa funcion corresponde a `P-PSEA-02`.
- No define criterios estadisticos ni reglas de decision; esa funcion corresponde a `P-PSEA-07`.
- No describe el flujo tecnico interno de aplicativos; esa funcion corresponde a `P-PSEA-08` y sus instructivos asociados.
- No reemplaza el control documental institucional de version, aprobacion, retencion o disposicion final.
