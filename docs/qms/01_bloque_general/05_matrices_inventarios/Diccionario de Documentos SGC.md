# Diccionario de Documentos SGC - CALAIRE-EA

Actualizado: 2026-06-27  
Fuente vigente: `P-PSEA-02 Matriz documental basica del PEA` y `mapa_navegacion_sgc_pea.html`.

## Convenciones

| Familia | Significado | Uso vigente |
|---|---|---|
| `DG` | Documento general | Marco del PEA y aplicativos que soportan la operacion. |
| `P` | Procedimiento | Reglas, responsabilidades, secuencias y criterios de control. |
| `I` | Instructivo | Ejecucion operativa o uso de aplicativos. |
| `F` | Formato / registro | Plantillas maestras, registros, evidencias y salidas de ronda. |

## Diccionario vigente

| Codigo | Nombre corto | Tipo | Proposito operativo | Relaciones principales |
|---|---|---|---|---|
| `DG-PSEA-01` | Protocolo general de participacion | Documento general | Marco de participacion del ensayo de aptitud. | `P-PSEA-01`, `P-PSEA-02`, `P-PSEA-09` |
| `DG-PSEA-02` | calaire-app | Documento general | Gestion de rondas, participantes, cronogramas, ficha, captura y exportacion. | `P-PSEA-04`, `P-PSEA-08`, `I-PSEA-02`, `I-PSEA-03` |
| `DG-PSEA-03` | pt_app | Documento general | Preprocesamiento, consolidacion, analisis estadistico, H/E e informe final. | `P-PSEA-08`, `I-PSEA-04`, `I-PSEA-05`, `F-PSEA-13` |
| `P-PSEA-01` | Protocolo general EA | Procedimiento marco | Ordena el ensayo de aptitud y referencia el flujo documental. | `DG-PSEA-01`, `P-PSEA-02`, `P-PSEA-04`, `P-PSEA-07`, `P-PSEA-09` |
| `P-PSEA-02` | Matriz documental del PEA | Matriz | Define arquitectura documental, codificacion, estados y ubicacion maestra. | `P-PSEA-03` |
| `P-PSEA-03` | Control de registros y evidencias | Procedimiento | Define estructura de ronda, checklist raiz, registros y evidencias por etapa. | `P-PSEA-08`, `F-PSEA-01` a `F-PSEA-18` segun aplique |
| `P-PSEA-04` | Planificacion de ronda EA | Procedimiento | Planifica rondas con calaire-app, cronograma, ficha basica, planificacion completa, competencia y proveedores cuando aplique. | `DG-PSEA-02`, `I-PSEA-03`, `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-03`, `F-PSEA-04`, `F-PSEA-05`, `F-PSEA-06`, `F-PSEA-16`, `F-PSEA-17` |
| `P-PSEA-05` | Comunicaciones | Procedimiento | Controla comunicaciones formales del PEA. | `F-PSEA-18`, `F-PSEA-13` |
| `P-PSEA-06` | Preparacion y control del item | Procedimiento tecnico | Controla generacion, preparacion y control del item gaseoso. | `F-PSEA-07`, `F-PSEA-11`, `P-PSEA-07`, `P-PSEA-10` a `P-PSEA-13` |
| `P-PSEA-07` | Diseno estadistico | Procedimiento tecnico | Define valor asignado, sigma_pt, incertidumbre, desempeno, H/E y reglas de decision. | `F-PSEA-11`, `F-PSEA-11A` a `F-PSEA-11D`, `F-PSEA-12`, `F-PSEA-13`, `P-PSEA-09` |
| `P-PSEA-08` | Flujo tecnico de datos digitales | Procedimiento | Controla captura, exportacion, preprocesamiento, consolidacion, analisis y archivos tecnicos. | `DG-PSEA-02`, `DG-PSEA-03`, `I-PSEA-04`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-10`, `F-PSEA-12` |
| `P-PSEA-09` | Generacion y emision del informe | Procedimiento | Gobierna la emision del informe final desde pt_app. | `F-PSEA-13`, `P-PSEA-07`, `P-PSEA-10` a `P-PSEA-13` |
| `P-PSEA-10` | Tecnico NO-NO2 | Procedimiento tecnico por analito | Procedimiento activo para oxidos de nitrogeno. | `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09` |
| `P-PSEA-11` | Tecnico CO | Procedimiento tecnico por analito | Procedimiento activo para monoxido de carbono. | `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09` |
| `P-PSEA-12` | Tecnico O3 | Procedimiento tecnico por analito | Procedimiento activo para ozono. | `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09` |
| `P-PSEA-13` | Tecnico SO2 | Procedimiento tecnico por analito | Procedimiento activo para dioxido de azufre. | `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09` |
| `P-PSEA-14` | Colusion y falsificacion | Procedimiento de gestion | Previene, detecta y trata indicios de colusion o falsificacion. | `P-PSEA-15` a `P-PSEA-21`, `P-PSEA-05` |
| `P-PSEA-15` | TNC / NC / CAPA | Procedimiento de gestion | Controla trabajo no conforme, no conformidades y acciones correctivas. | `F-PSEA-14`, `F-PSEA-13` |
| `P-PSEA-16` | Valores sensibles | Procedimiento de gestion | Controla divulgacion y manejo de valores sensibles. | `F-PSEA-13` |
| `P-PSEA-17` | Quejas | Procedimiento de gestion | Recibe, evalua y resuelve quejas del PEA. | `F-PSEA-14`, `F-PSEA-13` |
| `P-PSEA-18` | Apelaciones | Procedimiento de gestion | Recibe, evalua y resuelve apelaciones. | `F-PSEA-15`, `F-PSEA-13` |
| `P-PSEA-19` | Confidencialidad | Procedimiento de gestion | Controla confidencialidad operativa interna. | `F-PSEA-13` |
| `P-PSEA-20` | Competencia | Procedimiento de gestion | Controla competencia y autorizacion operativa. | `F-PSEA-16`, `F-PSEA-13` |
| `P-PSEA-21` | Proveedores criticos | Procedimiento de gestion | Controla evaluacion y seguimiento de proveedores criticos. | `F-PSEA-17`, `F-PSEA-13` |
| `P-PSEA-23` | Mejora continua | Procedimiento de gestion | Codigo reservado/placeholder para mejora continua. | Pendiente de integrar al mapa si se activa. |
| `I-PSEA-02` | Participante calaire-app | Instructivo | Guia al participante en calaire-app y reporte de datos. | `DG-PSEA-02`, `F-PSEA-08` |
| `I-PSEA-03` | Administracion rondas calaire-app | Instructivo | Guia administracion interna de rondas y exportaciones. | `DG-PSEA-02`, `F-PSEA-04`, `F-PSEA-09` |
| `I-PSEA-04` | Preprocesador pt_app | Instructivo | Ejecuta preprocesamiento y registra entradas, salidas, version y responsable. | `DG-PSEA-03`, `F-PSEA-10`, `F-PSEA-11A` a `F-PSEA-11D`, `F-PSEA-12` |
| `I-PSEA-05` | Analisis PT pt_app | Instructivo | Ejecuta modulo de analisis PT y genera salidas e informe. | `DG-PSEA-03`, `F-PSEA-11`, `F-PSEA-12`, `F-PSEA-13` |
| `F-PSEA-01` | Calendario global | Formato maestro | Calendario general exportable desde calaire-app. | `P-PSEA-04`, `F-PSEA-05` |
| `F-PSEA-02` | Cronograma detallado | Formato maestro | Cronograma detallado de actividades de ronda. | `P-PSEA-04`, `F-PSEA-05` |
| `F-PSEA-03` | Registro de participacion y carga de datos del participante | Registro digital | Registro diligenciado en calaire-app por el participante; fuente para equipos y planificacion. | `DG-PSEA-02`, `I-PSEA-02`, `F-PSEA-04`, `F-PSEA-06` |
| `F-PSEA-04` | Equipos e instrumentos | Anexo tecnico | Exportacion de equipos e instrumentos desde F-PSEA-03. | `F-PSEA-03`, `P-PSEA-08`, `I-PSEA-03`, `DG-PSEA-03` |
| `F-PSEA-05` | Ficha basica de ronda EA | Formato maestro | Resumen basico/caratula de ronda. | `P-PSEA-04`, `F-PSEA-06`, `F-PSEA-01`, `F-PSEA-02` |
| `F-PSEA-06` | Planificacion de ronda EA | Formato maestro | Planificacion completa tecnica, logistica, estadistica y documental de ronda. | `P-PSEA-04`, `F-PSEA-03`, `F-PSEA-04`, `F-PSEA-05`, `F-PSEA-07` |
| `F-PSEA-07` | Control del item gaseoso | Formato maestro | Evidencia preparacion y control del item. | `P-PSEA-06` |
| `F-PSEA-08` | Datos reportados | Formato maestro | Datos reportados por participante. | `I-PSEA-02`, `P-PSEA-08`, `F-PSEA-09` |
| `F-PSEA-09` | Exportacion analisis PT | Formato maestro | Exportacion oficial calaire-app hacia pt_app. | `P-PSEA-08`, `DG-PSEA-03` |
| `F-PSEA-10` | Registro preprocesamiento | Formato maestro | Registro de preprocesamiento de datos. | `I-PSEA-04`, `P-PSEA-08` |
| `F-PSEA-11` | Homogeneidad y estabilidad | Formato maestro | Registro principal de H/E del item. | `P-PSEA-06`, `P-PSEA-07`, `I-PSEA-05` |
| `F-PSEA-11A` | Datos homogeneidad | Subformato H/E | Datos preprocesados de homogeneidad. | `I-PSEA-04`, `F-PSEA-11` |
| `F-PSEA-11B` | Datos estabilidad | Subformato H/E | Datos preprocesados de estabilidad. | `I-PSEA-04`, `F-PSEA-11` |
| `F-PSEA-11C` | Resultados homogeneidad | Subformato H/E | Resultados de homogeneidad. | `I-PSEA-04`, `F-PSEA-11` |
| `F-PSEA-11D` | Resultados estabilidad | Subformato H/E | Resultados de estabilidad. | `I-PSEA-04`, `F-PSEA-11` |
| `F-PSEA-12` | Dataset oficial consolidado | Formato/dataset | Dataset oficial para evaluacion de aptitud; evidencia de `04_datos_y_preprocesamiento` en cada ronda. | `P-PSEA-07`, `P-PSEA-08`, `I-PSEA-04`, `I-PSEA-05` |
| `F-PSEA-13` | Informe final de resultados | Formato maestro | Informe oficial de resultados de ronda. | `P-PSEA-09`, `I-PSEA-05`, procedimientos de gestion |
| `F-PSEA-14` | Registro queja o NC | Registro de gestion | Evidencia de queja, trabajo no conforme o NC segun aplique. | `P-PSEA-15`, `P-PSEA-17` |
| `F-PSEA-15` | Registro apelaciones | Registro de gestion | Evidencia de apelaciones. | `P-PSEA-18` |
| `F-PSEA-16` | Competencia y autorizacion | Matriz de gestion | Evidencia de competencia y autorizacion operativa; se conserva en planificacion de ronda cuando aplique. | `P-PSEA-20`, `P-PSEA-03` |
| `F-PSEA-17` | Evaluacion proveedores criticos | Registro de gestion | Evidencia de evaluacion de proveedores; se conserva en planificacion de ronda cuando aplique. | `P-PSEA-21`, `P-PSEA-03` |
| `F-PSEA-18` | Comunicacion participantes | Formato maestro | Comunicaciones formales y evidencia de envio/respuesta. | `P-PSEA-05` |
