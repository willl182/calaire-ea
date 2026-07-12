# Mapa Tentativo del SGC PEA

**Estado:** documento de trabajo  
**Fecha:** 2026-06-13  
**Proposito:** consolidar una vista rapida del sistema documental tentativo del PEA, indicando el rol de cada documento y sus formatos/registros relacionados.

## Criterio de alcance

Este mapa describe el sistema documental propio del PEA. No incluye procesos del SGC macro que se gestionan por fuera, como auditorias internas/externas, revision por la direccion, imparcialidad institucional, control documental macro, talento humano general o compras generales.

## Documentos generales

| Codigo | Documento | Descripcion rapida | Formatos / registros relacionados |
|---|---|---|---|
| `DG-PSEA-01` | Protocolo general de participacion EA | Documento general que establece el marco de participacion, condiciones generales del ensayo de aptitud y reglas del programa. | Cita formatos operativos de ronda; se revisa al final. |
| `DG-PSEA-02` | Aplicativo `calaire-app` | Documento general del aplicativo usado para gestion de rondas, participantes, cronogramas, ficha de ronda, captura/exportacion de datos y casos de quejas. | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-05`, `F-PSEA-05A`, `F-PSEA-06`, `F-PSEA-07`, `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-16`. |
| `DG-PSEA-03` | Aplicativo `pt_app` | Documento general del aplicativo usado para preprocesamiento, consolidacion, analisis estadistico, H/E e informe final. | `F-PSEA-04`, `F-PSEA-10`, `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`. |

## Procedimientos del PEA

| Codigo | Documento | Estado tentativo | Descripcion rapida | Formatos / registros relacionados |
|---|---|---:|---|---|
| `P-PSEA-01` | Protocolo general EA | Mantener | Procedimiento/protocolo marco del ensayo de aptitud. Debe citar el flujo digital, aplicativos e instructivos cuando el mapa este estabilizado. | Todos los formatos principales de ronda; especialmente `F-PSEA-06`, `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-14`, `F-PSEA-04`. |
| `P-PSEA-02` | Procedimiento tecnico NO/NO2 | Actualizar | Procedimiento especifico por analito. Debe conservar solo condiciones tecnicas propias de NO/NO2 y citar documentos transversales. | `F-PSEA-08`, `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`. |
| `P-PSEA-03` | Procedimiento tecnico CO | Actualizar | Procedimiento especifico por analito. Debe conservar solo condiciones tecnicas propias de CO y citar documentos transversales. | `F-PSEA-08`, `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`. |
| `P-PSEA-04` | Procedimiento tecnico O3 | Actualizar | Procedimiento especifico por analito. Debe corregir referencias antiguas y evitar duplicar estadistica, H/E e informe. | `F-PSEA-08`, `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`. |
| `P-PSEA-05` | Procedimiento tecnico SO2 | Actualizar | Procedimiento especifico por analito. Debe conservar solo condiciones tecnicas propias de SO2 y citar documentos transversales. | `F-PSEA-08`, `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`. |
| `P-PSEA-06` | Diseno estadistico | Mantener / actualizar | Procedimiento tecnico central para valor asignado, `sigma_pt`, incertidumbre, outliers, desempeno, reglas de decision e integracion de H/E. No es instructivo de `pt_app`. | `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`. |
| `P-PSEA-07` | Generacion/emision del informe de resultados | Elaborar / actualizar | Procedimiento que gobierna la generacion y emision del informe final desde `pt_app`. Absorbe el rol de `P-PSEA-22`. | `F-PSEA-04`, `F-PSEA-14`, resultados H/E cuando apliquen. |
| `P-PSEA-08` | Colusion y falsificacion | Mantener / actualizar | Procedimiento independiente para prevenir, detectar y tratar indicios de colusion o falsificacion. | `F-PSEA-06`, `F-PSEA-09`, `F-PSEA-12`, registros de caso si escala. |
| `P-PSEA-09` | Planificacion de ronda EA | Actualizar | Procedimiento transversal para planificar la ronda usando `calaire-app` y formatos exportables. | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-06`, `F-PSEA-07`, `F-PSEA-08`. |
| `P-PSEA-10` | Preparacion y control del item de ensayo gaseoso | Elaborar / actualizar | Procedimiento para generar concentraciones con calibrador dinamico y cilindro, tomando niveles definidos en la ronda. No trata envio fisico de items. | `F-PSEA-07`, `F-PSEA-08`, `F-PSEA-13`, `F-PSEA-13A-D`. |
| `P-PSEA-11` | Reservado / no aplicable | Reservar | No aplica por ahora porque no hay envio fisico de items de ensayo. | Ninguno. |
| `P-PSEA-12` | Matriz documental del PEA | Elaborar | Matriz basica de todo lo numerado del PEA: `DG`, `P`, `I`, `F` y subformatos, con estado y relacion documental. | Lista todos los documentos y formatos; no genera registros operativos de ronda. |
| `P-PSEA-13` | Matriz de registros y evidencias del PEA | Elaborar | Matriz de evidencias generadas por ronda, evento, periodo o cuando aplique. | Todos los registros `F-PSEA` vigentes y evidencias operativas asociadas. |
| `P-PSEA-14` | Riesgos generales del PEA | Por elaborar / no intervenir | Idea reservada para riesgos generales del PEA. No desarrollar por ahora. | Por definir. |
| `P-PSEA-15` | Mejora continua del PEA | Por elaborar / no intervenir | Idea reservada para mejora continua del PEA. No desarrollar por ahora. | Por definir. |
| `P-PSEA-16` | Trabajo no conforme, no conformidades y acciones correctivas | Mantener / actualizar | Procedimiento para TNC/NC/CAPA del PEA. Puede recibir casos desde colusion, quejas, apelaciones, datos o informe. | `F-PSEA-16` o caso/registro equivalente; evidencias asociadas segun el caso. |
| `P-PSEA-17` | Auditorias internas/externas | Retirar | Fuera del alcance documental propio del PEA. Se gestiona por el SGC macro. | Ninguno en PEA. |
| `P-PSEA-18` | Revision por la direccion | Retirar | Fuera del alcance documental propio del PEA. Se gestiona por el SGC macro. | Ninguno en PEA. |
| `P-PSEA-19` | Imparcialidad | Retirar | Fuera del alcance documental propio del PEA. Se maneja por fuera. | Ninguno en PEA. |
| `P-PSEA-20` | Comunicaciones del PEA | Mantener / actualizar | Procedimiento de comunicaciones por `calaire-app` y correo, segun el tipo de comunicacion. | Evidencias de comunicacion, `F-PSEA-09`, `F-PSEA-16`, `F-PSEA-17`, envio/emision de `F-PSEA-04`. |
| `P-PSEA-21` | Divulgacion y control de valores sensibles | Mantener / actualizar | Procedimiento para controlar divulgacion de niveles, `x_pt`, `sigma_pt`, valores de referencia, resultados agregados y demas informacion sensible. | `F-PSEA-06`, `F-PSEA-04`, salidas de `pt_app`, registros de comunicacion. |
| `P-PSEA-22` | Reportes PT | Absorber / reservar | No se mantiene como procedimiento independiente. Su contenido queda dentro de `P-PSEA-07`. | `F-PSEA-04`. |
| `P-PSEA-23` | Flujo tecnico de datos digitales del PEA | Elaborar / actualizar | Mapa/procedimiento de datos: captura, exportacion, preprocesamiento, consolidacion, analisis e informe. Incluye archivos tecnicos sin codigo `F-PSEA`. | `F-PSEA-09`, `F-PSEA-10`, `F-PSEA-12`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`. |
| `P-PSEA-24` | Quejas del PEA | Mantener / actualizar | Procedimiento de quejas gestionadas como casos SGC en `calaire-app`. | `F-PSEA-16` o caso SGC equivalente; comunicaciones relacionadas. |
| `P-PSEA-25` | Apelaciones del PEA | Mantener / actualizar | Procedimiento de apelaciones manejadas aparte por correo formal al correo institucional del grupo. | `F-PSEA-17` o registro equivalente; comunicaciones formales. |
| `P-PSEA-26` | Confidencialidad operativa interna del PEA | Mantener / actualizar | Procedimiento acotado a confidencialidad de datos, participantes, codigos, archivos exportados y resultados. No es politica institucional general. | `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-14`, `F-PSEA-04`, registros de acceso/comunicacion si aplican. |
| `P-PSEA-27` | Competencia y autorizacion operativa del PEA | Mantener / actualizar | Procedimiento acotado a roles tecnicos y operativos del PEA. No cubre talento humano general. | `F-PSEA-21` o matriz equivalente de competencia/autorizacion. |
| `P-PSEA-28` | Proveedores criticos del PEA | Mantener / actualizar | Procedimiento acotado a proveedores o servicios criticos del PEA, respetando limites de tercerizacion de ISO/IEC 17043. No cubre compras generales. | `F-PSEA-23` o evaluacion equivalente de proveedores criticos. |

## Formatos y registros F-PSEA

| Codigo | Formato / registro | Estado tentativo | Descripcion rapida | Procedimientos relacionados |
|---|---|---:|---|---|
| `F-PSEA-01` | Calendario global de ronda | Actualizar | Calendario general desde inicio de ronda hasta entrega de informe final; exportable desde `calaire-app` y util para Gantt/Mermaid. | `P-PSEA-09`, `F-PSEA-06`. |
| `F-PSEA-02` | Cronograma detallado de ronda | Actualizar | Cronograma diligenciable/exportable de actividades detalladas de ronda. | `P-PSEA-09`, `F-PSEA-06`. |
| `F-PSEA-03` | Reservado / sustituido | Retirar / reservar | Sustituido por el plan de ronda `F-PSEA-06`. | Ninguno. |
| `F-PSEA-04` | Informe final de resultados | Mantener / actualizar | Informe final generado desde `pt_app`. | `P-PSEA-07`, `P-PSEA-06`, `P-PSEA-20`, `P-PSEA-21`. |
| `F-PSEA-05` | Registro de participacion | Mantener / actualizar | Registro de participacion del laboratorio/participante. | `P-PSEA-09`, `P-PSEA-20`. |
| `F-PSEA-05A` | Anexo tecnico de equipos e instrumentos | Mantener / actualizar | Datos de equipos e instrumentos del participante; equivalente a `ronda_1_equipos.csv`. | `P-PSEA-23`, `P-PSEA-06`. |
| `F-PSEA-06` | Plan de ronda EA | Mantener / actualizar | Plan tecnico-operativo de la ronda. Indica, entre otros, que H/E se documenta en `F-PSEA-13`. | `P-PSEA-09`, `P-PSEA-08`, `P-PSEA-10`, `P-PSEA-21`. |
| `F-PSEA-07` | Ficha digital de ronda EA | Elaborar / actualizar | Exportacion desde `calaire-app` con informacion estructurada de la ronda, incluyendo matriz/nota A-U. | `P-PSEA-09`, `F-PSEA-06`, `P-PSEA-10`. |
| `F-PSEA-08` | Preparacion y control del item | Mantener / actualizar | Dossier/registro de preparacion y control del item gaseoso. | `P-PSEA-10`, `P-PSEA-02` a `P-PSEA-05`, `P-PSEA-09`. |
| `F-PSEA-09` | Datos reportados por participante | Mantener / actualizar | Registro diligenciado por el participante en `calaire-app`. | `P-PSEA-20`, `P-PSEA-23`, `P-PSEA-26`. |
| `F-PSEA-10` | Registro de preprocesamiento de datos | Elaborar | Registro de ejecucion del preprocesador: entradas, salidas, fecha, version, responsable/ruta y observaciones. | `P-PSEA-23`, `I-PSEA-17`. |
| `F-PSEA-11` | Reservado / no aplicable | Reservar | No aplica por ausencia de envio fisico de items. | Ninguno. |
| `F-PSEA-12` | Datos de participantes exportados para analisis PT | Mantener / actualizar | Exportacion oficial desde `calaire-app` hacia `pt_app`. No es `ronda_<n>_completa.csv`. | `P-PSEA-23`, `P-PSEA-26`. |
| `F-PSEA-13` | Homogeneidad y estabilidad del item | Mantener / actualizar | Registro principal de H/E del item de ensayo. | `P-PSEA-06`, `P-PSEA-10`, `P-PSEA-23`. |
| `F-PSEA-13A` | Datos preprocesados de homogeneidad | Elaborar | Subformato producido por `pt_app` para datos preprocesados de homogeneidad. | `P-PSEA-06`, `P-PSEA-23`, `I-PSEA-17`. |
| `F-PSEA-13B` | Datos preprocesados de estabilidad | Elaborar | Subformato producido por `pt_app` para datos preprocesados de estabilidad. | `P-PSEA-06`, `P-PSEA-23`, `I-PSEA-17`. |
| `F-PSEA-13C` | Resultados de homogeneidad | Elaborar | Resultado de homogeneidad exportado desde `pt_app`. | `P-PSEA-06`, `P-PSEA-23`, `I-PSEA-18`. |
| `F-PSEA-13D` | Resultados de estabilidad | Elaborar | Resultado de estabilidad exportado desde `pt_app`. | `P-PSEA-06`, `P-PSEA-23`, `I-PSEA-18`. |
| `F-PSEA-14` | Datos oficiales consolidados para evaluacion de aptitud | Elaborar | Dataset oficial `ronda_<n>_completa.csv`, generado por el preprocesador y usado para evaluacion de aptitud. | `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-23`, `I-PSEA-17`, `I-PSEA-18`. |
| `F-PSEA-16` | Registro/caso de queja o NC | Revisar | Registro o caso SGC relacionado con quejas y/o NC, segun se defina la implementacion. | `P-PSEA-16`, `P-PSEA-24`. |
| `F-PSEA-17` | Registro de apelaciones | Revisar | Registro de apelacion recibida por correo formal institucional. | `P-PSEA-25`, `P-PSEA-20`. |
| `F-PSEA-21` | Matriz de competencia/autorizacion | Mantener / actualizar | Evidencia de competencia/autorizacion de roles tecnicos y operativos del PEA. | `P-PSEA-27`. |
| `F-PSEA-23` | Evaluacion de proveedores criticos | Mantener / actualizar | Evaluacion o registro de proveedores/servicios criticos del PEA. | `P-PSEA-28`. |

## Instructivos

| Codigo | Instructivo | Estado tentativo | Descripcion rapida | Formatos / registros relacionados |
|---|---|---:|---|---|
| `I-PSEA-10` | Uso de `calaire-app` por participante | Mantener / actualizar | Instrucciones para que el participante use `calaire-app` y registre datos. | `F-PSEA-09`, comunicaciones de ronda. |
| `I-PSEA-16` | Administracion de rondas en `calaire-app` | Mantener / actualizar | Instrucciones para el administrador de rondas en `calaire-app`. | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-05`, `F-PSEA-05A`, `F-PSEA-07`, `F-PSEA-12`. |
| `I-PSEA-17` | Uso del preprocesador de `pt_app` | Elaborar | Instrucciones operativas para ejecutar preprocesamiento y registrar salidas. | `F-PSEA-10`, `F-PSEA-13A`, `F-PSEA-13B`, `F-PSEA-14`. |
| `I-PSEA-18` | Uso del modulo de analisis PT de `pt_app` | Elaborar | Instrucciones operativas para ejecutar analisis PT y generar salidas/informe. | `F-PSEA-13C`, `F-PSEA-13D`, `F-PSEA-14`, `F-PSEA-04`. |

## Elementos fuera del alcance documental propio del PEA

| Elemento | Decision |
|---|---|
| Auditorias internas/externas | Fuera del PEA; sistema macro. |
| Revision por la direccion | Fuera del PEA; sistema macro. |
| Imparcialidad | Fuera del PEA; se maneja por fuera. |
| Control documental macro | Fuera de `P-PSEA-12`; lo maneja el sistema macro. |
| Talento humano general | Fuera de `P-PSEA-27`; solo queda competencia/autorizacion operativa PEA. |
| Compras generales | Fuera de `P-PSEA-28`; solo proveedores criticos PEA. |
| Politica institucional de confidencialidad | Fuera de `P-PSEA-26`; solo confidencialidad operativa PEA. |

## Orden tentativo de elaboracion

1. `P-PSEA-12` Matriz documental del PEA.
2. `P-PSEA-13` Matriz de registros/evidencias.
3. `P-PSEA-23` Flujo tecnico de datos digitales.
4. `DG-PSEA-03`, `I-PSEA-17`, `I-PSEA-18` para `pt_app`.
5. Formatos nuevos/redefinidos: `F-PSEA-07`, `F-PSEA-10`, `F-PSEA-13A-D`, `F-PSEA-14`.
6. Procedimientos transversales: `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09`, `P-PSEA-10`, `P-PSEA-20`, `P-PSEA-21`, `P-PSEA-24` a `P-PSEA-28`.
7. Procedimientos por analito: `P-PSEA-02` a `P-PSEA-05`.
8. Cierre: `sgc_res.md`, `README.md`, `P-PSEA-01`.
