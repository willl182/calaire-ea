# Matriz de Equivalencias de Codigos SGC PEA

**Fecha:** 2026-06-14  
**Estado:** aprobada y aplicada para renumeracion operativa  
**Proposito:** controlar la renumeracion funcional del sistema documental SGC PEA antes de modificar archivos, mapa, fichas, referencias internas o derivados.

---

## Regla de Migracion

- No renombrar archivos hasta aprobar esta matriz.
- Mantener `DG-PSEA`, `P-PSEA`, `I-PSEA` y `F-PSEA` como familias documentales separadas.
- Mantener `DG-PSEA`, `P-PSEA`, `I-PSEA` y `F-PSEA` como familias documentales separadas aunque se reordenen numericamente.
- Los `F-PSEA` no son obligatoriamente Excel. Si el formato corresponde a formulario narrativo, acta, informe, plantilla diligenciable o registro tipo Word, se elaborara como `.md` fuente y `.docx` derivado usando una base Word (`DG-PSEA- Documento General.docx` o plantilla Word aplicable). Si corresponde a matriz o tabla estructurada, se elaborara como `.md`, `.csv` y `.xlsx`.
- Ordenar numericamente cada familia segun flujo documental real: gobierno documental, planificacion, operacion, datos, informe, gestion de casos y soportes.
- Conservar codigos retirados, reservados o absorbidos en la matriz para evitar reutilizacion accidental sin decision explicita.
- Actualizar despues de aprobar: nombres de archivo, titulos internos, mapa de navegacion, fichas resumen, checklist, referencias cruzadas y derivados `.docx`, `.csv` o `.xlsx` segun tipo de formato.

---

## Documentos Generales DG-PSEA

| Codigo actual | Codigo propuesto | Nombre propuesto | Accion | Observaciones |
|---|---|---|---|---|
| DG-PSEA-01 | DG-PSEA-01 | Protocolo general de participacion EA | Mantener | Documento marco; revisar al cierre. |
| DG-PSEA-02 | DG-PSEA-02 | Documento general `calaire-app` | Mantener | Debe elaborarse/actualizarse en repositorio de `calaire-app`. |
| DG-PSEA-03 | DG-PSEA-03 | Documento general `pt_app` | Mantener | Debe elaborarse/actualizarse en repositorio de `pt_app`. |

---

## Procedimientos P-PSEA

| Codigo actual | Codigo propuesto | Nombre propuesto | Accion | Observaciones |
|---|---|---|---|---|
| P-PSEA-01 | P-PSEA-01 | Protocolo general EA | Mantener | Marco general del programa EA. |
| P-PSEA-12 | P-PSEA-02 | Control documental del PEA | Renumerar | Primer procedimiento de gobierno documental. |
| P-PSEA-13 | P-PSEA-03 | Control de registros y evidencias del PEA | Renumerar | Segundo procedimiento de gobierno documental. |
| P-PSEA-09 | P-PSEA-04 | Planificacion de ronda EA | Renumerar | Inicio del flujo operativo de ronda. |
| P-PSEA-20 | P-PSEA-05 | Comunicaciones del PEA | Renumerar | Gobierno de comunicaciones con participantes y partes interesadas. |
| P-PSEA-10 | P-PSEA-06 | Preparacion y control del item de ensayo gaseoso | Renumerar | Procedimiento operativo central del item. |
| P-PSEA-06 | P-PSEA-07 | Diseno estadistico y evaluacion de desempeno | Renumerar | Procedimiento tecnico estadistico transversal. |
| P-PSEA-23 | P-PSEA-08 | Gestion de datos digitales del PEA | Renumerar | Documento marco del flujo de datos; detalles de apps se elaboran en repositorios aplicativos. |
| P-PSEA-07 | P-PSEA-09 | Generacion y emision del informe de resultados | Renumerar | Absorbe rol del antiguo P-PSEA-22. |
| P-PSEA-02 | P-PSEA-10 | Procedimiento tecnico NO/NO2 | Renumerar | Procedimiento especifico por analito. |
| P-PSEA-03 | P-PSEA-11 | Procedimiento tecnico CO | Renumerar | Procedimiento especifico por analito. |
| P-PSEA-04 | P-PSEA-12 | Procedimiento tecnico O3 | Renumerar | Procedimiento especifico por analito. |
| P-PSEA-05 | P-PSEA-13 | Procedimiento tecnico SO2 | Renumerar | Procedimiento especifico por analito. |
| P-PSEA-08 | P-PSEA-14 | Colusion y falsificacion | Renumerar | Procedimiento de gobernanza operativa. |
| P-PSEA-16 | P-PSEA-15 | Trabajo no conforme, no conformidades y acciones correctivas | Renumerar | Debe conectar con quejas, apelaciones y casos SGC. |
| P-PSEA-21 | P-PSEA-16 | Divulgacion y control de valores sensibles | Renumerar | Control de `x_pt`, `sigma_pt`, valores asignados y resultados. |
| P-PSEA-24 | P-PSEA-17 | Quejas del PEA | Renumerar | Gestion de quejas del PEA. |
| P-PSEA-25 | P-PSEA-18 | Apelaciones del PEA | Renumerar | Gestion de apelaciones por canal formal. |
| P-PSEA-26 | P-PSEA-19 | Confidencialidad operativa interna | Renumerar | Confidencialidad de participantes, codigos, datos y resultados. |
| P-PSEA-27 | P-PSEA-20 | Competencia y autorizacion del personal | Renumerar | Roles tecnicos y autorizaciones operativas del PEA. |
| P-PSEA-28 | P-PSEA-21 | Proveedores criticos del PEA | Renumerar | Proveedores/servicios criticos dentro de limites ISO/IEC 17043. |
| P-PSEA-14 | P-PSEA-22 | Riesgos generales del PEA | Reservar / renumerar | No elaborar en esta fase. |
| P-PSEA-15 | P-PSEA-23 | Mejora continua del PEA | Reservar / renumerar | No elaborar en esta fase. |
| P-PSEA-11 | Sin codigo activo | No aplicable por ahora | Retirar / reservar | Antiguo enfoque de envio fisico de items no aplica. |
| P-PSEA-17 | Sin codigo activo | Auditorias internas/externas | Retirar | Pertenece al SGC macro institucional. |
| P-PSEA-18 | Sin codigo activo | Revision por la direccion | Retirar | Pertenece al SGC macro institucional. |
| P-PSEA-19 | Sin codigo activo | Imparcialidad institucional | Retirar | Se gestiona fuera del sistema documental propio del PEA. |
| P-PSEA-22 | Sin codigo activo | Reportes PT | Absorber | Contenido absorbido por generacion/emision del informe de resultados. |

---

## Instructivos I-PSEA

| Codigo actual | Codigo propuesto | Nombre propuesto | Accion | Observaciones |
|---|---|---|---|---|
| I-PSEA-01 | I-PSEA-01 | Embalaje y transporte de equipos de participantes | Mantener | Vigente para equipos e instrumentos de participantes; no corresponde al envio fisico de items de ensayo. |
| I-PSEA-10 | I-PSEA-02 | Uso de `calaire-app` por participante | Renumerar | Elaborar/actualizar en repositorio `calaire-app`. |
| I-PSEA-16 | I-PSEA-03 | Administracion de rondas en `calaire-app` | Renumerar | Elaborar/actualizar en repositorio `calaire-app`. |
| I-PSEA-17 | I-PSEA-04 | Uso del preprocesador de datos de `pt_app` | Renumerar | Elaborar/actualizar en repositorio `pt_app`. |
| I-PSEA-18 | I-PSEA-05 | Uso del modulo de analisis PT de `pt_app` | Renumerar | Elaborar/actualizar en repositorio `pt_app`. |

---

## Formatos y Registros F-PSEA

| Codigo actual | Codigo propuesto | Nombre propuesto | Formato salida | Accion | Observaciones |
|---|---|---|---|---|---|
| F-PSEA-01 | F-PSEA-01 | Calendario global de ronda | `md+csv+xlsx` | Mantener | Exportable desde `calaire-app`. |
| F-PSEA-02 | F-PSEA-02 | Cronograma detallado de ronda | `md+csv+xlsx` | Mantener | Exportable/diligenciable desde planificacion. |
| F-PSEA-05 | F-PSEA-03 | Registro de participacion | `md+csv+xlsx` | Renumerar | Debe volver al mapa; actualmente ausente en mapa visual. |
| F-PSEA-05A | F-PSEA-04 | Anexo tecnico de equipos e instrumentos | `md+csv+xlsx` | Renumerar | Equivalente a datos de equipos/instrumentos del participante. |
| F-PSEA-06 | F-PSEA-05 | Plan de ronda EA | `md+docx` | Renumerar | Integra calendario, cronograma, ficha y nota/matriz A-U. |
| F-PSEA-07 | F-PSEA-06 | Ficha digital de ronda EA | `md+csv+xlsx` | Renumerar | Exportable desde `calaire-app`. |
| F-PSEA-08 | F-PSEA-07 | Registro de preparacion y control del item | `md+docx/csv+xlsx` | Renumerar | Puede requerir narrativa tecnica y tablas de control. |
| F-PSEA-09 | F-PSEA-08 | Datos reportados por participante | `md+csv+xlsx` | Renumerar | Registro capturado en `calaire-app`. |
| F-PSEA-12 | F-PSEA-09 | Datos de participantes exportados para analisis PT | `md+csv+xlsx` | Renumerar | Exportacion oficial de `calaire-app` hacia `pt_app`. |
| F-PSEA-10 | F-PSEA-10 | Registro de preprocesamiento de datos | `md+csv+xlsx` | Mantener | Salida/evidencia del preprocesador `pt_app`. |
| F-PSEA-13 | F-PSEA-11 | Paquete de homogeneidad y estabilidad del item | `md+docx/csv+xlsx` | Renumerar | Paquete unico H/E con componente narrativo y salidas tabulares. |
| F-PSEA-13A | F-PSEA-11A | Datos preprocesados de homogeneidad | `md+csv+xlsx` | Renumerar | Subsalida del paquete F-PSEA-11. |
| F-PSEA-13B | F-PSEA-11B | Datos preprocesados de estabilidad | `md+csv+xlsx` | Renumerar | Subsalida del paquete F-PSEA-11. |
| F-PSEA-13C | F-PSEA-11C | Resultados de homogeneidad | `md+csv+xlsx` | Renumerar | Subsalida del paquete F-PSEA-11. |
| F-PSEA-13D | F-PSEA-11D | Resultados de estabilidad | `md+csv+xlsx` | Renumerar | Subsalida del paquete F-PSEA-11. |
| F-PSEA-14 | F-PSEA-12 | Datos oficiales consolidados para evaluacion de aptitud | `md+csv+xlsx` | Renumerar | Dataset oficial `ronda_<n>_completa.csv`. |
| F-PSEA-04 | F-PSEA-13 | Informe final de resultados | `md+docx` | Renumerar | Generado desde `pt_app`; asociado al procedimiento de informe. |
| F-PSEA-16 | F-PSEA-14 | Registro de queja / NC / CAPA | `md+docx/csv+xlsx` | Renumerar | Debe volver al mapa y anclarse a quejas y NC/CAPA. |
| F-PSEA-17 | F-PSEA-15 | Registro de apelaciones | `md+docx/csv+xlsx` | Renumerar | Debe volver al mapa y anclarse a apelaciones. |
| F-PSEA-21 | F-PSEA-16 | Matriz de competencia y autorizacion | `md+csv+xlsx` | Renumerar | Debe volver al mapa y anclarse a competencia/autorizacion. |
| F-PSEA-23 | F-PSEA-17 | Evaluacion de proveedores criticos | `md+docx/csv+xlsx` | Renumerar | Debe volver al mapa y anclarse a proveedores criticos. |
| F-PSEA-03 | Sin codigo activo | No aplicable / sustituido | N/A | Retirar / reservar | Sustituido por plan de ronda. |
| F-PSEA-11 | Sin codigo activo | No aplicable por ahora | N/A | Reservar | Antiguo envio/recepcion no aplica. |

---

## Regla para Formatos Mixtos

Los formatos con salida `md+docx/csv+xlsx` tendran `.docx` como artefacto principal y `.csv/.xlsx` como auxiliar de consolidacion, seguimiento o exportacion.

| Codigo propuesto | Documento | Artefacto principal | Artefacto auxiliar |
|---|---|---|---|
| F-PSEA-07 | Registro de preparacion y control del item | `.docx` | `.csv/.xlsx` |
| F-PSEA-11 | Paquete de homogeneidad y estabilidad del item | `.docx` | `.csv/.xlsx` |
| F-PSEA-14 | Registro de queja / NC / CAPA | `.docx` | `.csv/.xlsx` |
| F-PSEA-15 | Registro de apelaciones | `.docx` | `.csv/.xlsx` |
| F-PSEA-17 | Evaluacion de proveedores criticos | `.docx` | `.csv/.xlsx` |

---

## Control Posterior a la Renumeracion

- `I-PSEA-01` se mantiene vigente para embalaje y transporte de equipos e instrumentos de participantes; no debe confundirse con el antiguo enfoque de envio fisico de items de ensayo.
- Los codigos retirados quedan sin codigo activo y se conservan como historicos en la matriz documental y en `docs/documentacion_sgc/fichas_resumen/retirados/`.
- `checklist_sgc_pdts.md`, mapa visual, fichas resumen, indice HTML y referencias internas fueron actualizados con los codigos propuestos.
