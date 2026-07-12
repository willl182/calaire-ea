# Inventario Maestro de Fichas Resumen del SGC PEA

**Estado:** activo  
**Fecha:** 2026-06-13  
**Proposito:** matriz maestra del universo de fichas resumen del PEA. Define codigo, nombre, familia, estado, prioridad, clase de ficha y fase de elaboracion para 55 codigos documentales y 3 subformatos adicionales.

---

## Documentos generales (DG-PSEA)

| Codigo | Nombre | Familia | Estado | Prioridad | Clase de ficha | Fase de elaboracion | Nota de control |
|---|---|---|---|---|---|---|---|
| `DG-PSEA-01` | Protocolo general de participacion EA | DG | Mantener | Cierre | Ficha diferida | Fase 9 | Cierre global; no tocar ahora. |
| `DG-PSEA-02` | Aplicativo `calaire-app` | DG | Actualizar | Alta | Ficha activa | Fase 3 | Consolidar como documento general. |
| `DG-PSEA-03` | Aplicativo `pt_app` | DG | Elaborar | Alta | Ficha activa | Fase 3 | Consolidar como documento general; no es formato. |

---

## Procedimientos (P-PSEA)

| Codigo | Nombre | Familia | Estado | Prioridad | Clase de ficha | Fase de elaboracion | Nota de control |
|---|---|---|---|---|---|---|---|
| `P-PSEA-01` | Protocolo general EA | P | Mantener | Cierre | Ficha diferida | Fase 9 | Cierre global; no tocar ahora. |
| `P-PSEA-10` | Procedimiento tecnico NO/NO2 | P | Actualizar | Media | Ficha activa | Fase 8 | Especifico por analito; citar transversales. |
| `P-PSEA-11` | Procedimiento tecnico CO | P | Actualizar | Media | Ficha activa | Fase 8 | Especifico por analito; citar transversales. |
| `P-PSEA-12` | Procedimiento tecnico O3 | P | Actualizar | Media | Ficha activa | Fase 8 | Corregir referencias antiguas. |
| `P-PSEA-13` | Procedimiento tecnico SO2 | P | Actualizar | Media | Ficha activa | Fase 8 | Especifico por analito; citar transversales. |
| `P-PSEA-07` | Diseno estadistico | P | Mantener / actualizar | Alta | Ficha activa | Fase 5 | Nucleo tecnico central; no es instructivo. |
| `P-PSEA-09` | Generacion/emision del informe de resultados | P | Elaborar / actualizar | Alta | Ficha preliminar | Fase 5 | Absorbe `P-PSEA-22`; no definir contenido `F-PSEA-13`. |
| `P-PSEA-14` | Colusion y falsificacion | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Independiente; conecta con `P-PSEA-15`, `P-PSEA-16`, `P-PSEA-19`. |
| `P-PSEA-04` | Planificacion de ronda EA | P | Actualizar | Alta | Ficha activa | Fase 5 | Transversal; soportado en `calaire-app`. |
| `P-PSEA-06` | Preparacion y control del item de ensayo gaseoso | P | Elaborar / actualizar | Alta | Ficha activa | Fase 5 | No envio fisico; calibrador dinamico + cilindro. |
| `P-PSEA-11` | No aplicable | P | Reservar | No priorizar | Registro de no activo | Fase 9 | Ausencia de envio fisico de items. |
| `P-PSEA-02` | Matriz documental del PEA | P | Elaborar | Alta | Ficha activa | Fase 3 | Basica: `DG`, `P`, `I`, `F`, subformatos. |
| `P-PSEA-03` | Matriz de registros y evidencias del PEA | P | Elaborar | Alta | Ficha activa | Fase 3 | Evidencias por ronda/evento; no archivos tecnicos internos. |
| `P-PSEA-22` | Riesgos generales del PEA | P | Por elaborar | No priorizar | Ficha preliminar | Fase 9 | Idea reservada; no desarrollar ahora. |
| `P-PSEA-23` | Mejora continua del PEA | P | Por elaborar | No priorizar | Ficha preliminar | Fase 9 | Idea reservada; no desarrollar ahora. |
| `P-PSEA-15` | Trabajo no conforme, no conformidades y acciones correctivas | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Conecta con quejas, apelaciones, colusion. |
| `P-PSEA-17` | Auditorias internas/externas | P | Retirar | No priorizar | Registro de no activo | Fase 9 | Fuera del alcance PEA; sistema macro. |
| `P-PSEA-18` | Revision por la direccion | P | Retirar | No priorizar | Registro de no activo | Fase 9 | Fuera del alcance PEA; sistema macro. |
| `P-PSEA-19` | Imparcialidad | P | Retirar | No priorizar | Registro de no activo | Fase 9 | Fuera del alcance PEA; se maneja por fuera. |
| `P-PSEA-05` | Comunicaciones del PEA | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | `calaire-app` + correo segun aplique. |
| `P-PSEA-16` | Divulgacion y control de valores sensibles | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Control de niveles, `x_pt`, `sigma_pt`, resultados. |
| `P-PSEA-22` | Reportes PT | P | Absorber | No priorizar | Registro de no activo | Fase 9 | Absorbido por `P-PSEA-09`. |
| `P-PSEA-08` | Flujo tecnico de datos digitales del PEA | P | Elaborar / actualizar | Alta | Ficha activa | Fase 3 | Mapa clave: aplicativos, archivos tecnicos, formatos, salidas. |
| `P-PSEA-17` | Quejas del PEA | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Casos SGC en `calaire-app`. |
| `P-PSEA-18` | Apelaciones del PEA | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Correo formal institucional; no `calaire-app`. |
| `P-PSEA-19` | Confidencialidad operativa interna del PEA | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Acotada a datos, participantes, resultados. |
| `P-PSEA-20` | Competencia y autorizacion operativa del PEA | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Roles tecnicos/operativos; no talento humano general. |
| `P-PSEA-21` | Proveedores criticos del PEA | P | Mantener / actualizar | Media-alta | Ficha activa | Fase 7 | Respetar limites de tercerizacion ISO/IEC 17043. |

---

## Instructivos (I-PSEA)

| Codigo | Nombre | Familia | Estado | Prioridad | Clase de ficha | Fase de elaboracion | Nota de control |
|---|---|---|---|---|---|---|---|
| `I-PSEA-02` | Uso de `calaire-app` por participante | I | Mantener / actualizar | Media-alta | Ficha activa | Fase 4 | Integrar con `DG-PSEA-02` y `P-PSEA-05`. |
| `I-PSEA-03` | Administracion de rondas en `calaire-app` | I | Mantener / actualizar | Media-alta | Ficha activa | Fase 4 | Cubre administracion interna de rondas. |
| `I-PSEA-04` | Uso del preprocesador de `pt_app` | I | Elaborar | Alta | Ficha activa | Fase 4 | No reemplaza `P-PSEA-07`; explica uso operativo. |
| `I-PSEA-05` | Uso del modulo de analisis PT de `pt_app` | I | Elaborar | Alta | Ficha activa | Fase 4 | No reemplaza `P-PSEA-07`; explica uso operativo. |

---

## Formatos y registros (F-PSEA)

| Codigo | Nombre | Familia | Estado | Prioridad | Clase de ficha | Fase de elaboracion | Nota de control |
|---|---|---|---|---|---|---|---|
| `F-PSEA-01` | Calendario global de ronda | F | Actualizar | Media | Ficha activa | Fase 6 | Exportable desde `calaire-app`. |
| `F-PSEA-02` | Cronograma detallado de ronda | F | Actualizar | Media | Ficha activa | Fase 6 | Diligenciable/exportable desde `calaire-app`. |
| `F-PSEA-03` | No aplicable | F | Retirar | No priorizar | Registro de no activo | Fase 9 | Sustituido por `F-PSEA-05`. |
| `F-PSEA-13` | Informe final de resultados | F | Mantener / actualizar | Media-alta | Ficha preliminar | Fase 6 | Generado desde `pt_app`; no definir contenido ahora. |
| `F-PSEA-03` | Registro de participacion | F | Mantener / actualizar | Media | Ficha activa | Fase 6 | Principal registro de participacion. |
| `F-PSEA-04` | Anexo tecnico de equipos e instrumentos | F | Mantener / actualizar | Media | Ficha activa | Fase 6 | Equivalente a `ronda_1_equipos.csv`; alimenta `pt_app`. |
| `F-PSEA-05` | Plan de ronda EA | F | Mantener / actualizar | Media-alta | Ficha activa | Fase 6 | Integra `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-06` y nota A-U. |
| `F-PSEA-06` | Ficha digital de ronda EA | F | Elaborar / actualizar | Alta | Ficha activa | Fase 4 | Exportable desde `calaire-app`; insumo de `F-PSEA-05`. |
| `F-PSEA-07` | Preparacion y control del item | F | Mantener / actualizar | Media | Ficha activa | Fase 6 | Dossier del item gaseoso. |
| `F-PSEA-08` | Datos reportados por participante | F | Mantener / actualizar | Media | Ficha activa | Fase 6 | Registro en `calaire-app`. |
| `F-PSEA-10` | Registro de preprocesamiento de datos | F | Elaborar | Alta | Ficha activa | Fase 4 | No es aplicativo; referencia `preprocesamiento_log.csv`. |
| `F-PSEA-11` | No aplicable | F | Reservar | No priorizar | Registro de no activo | Fase 9 | Ausencia de envio fisico de items. |
| `F-PSEA-09` | Datos de participantes exportados para analisis PT | F | Mantener / actualizar | Alta | Ficha activa | Fase 6 | Exportacion oficial hacia `pt_app`; no es `ronda_<n>_completa.csv`. |
| `F-PSEA-11` | Homogeneidad y estabilidad del item | F | Mantener / actualizar | Alta | Ficha activa | Fase 6 | Registro principal de H/E. |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | F | Elaborar | Alta | Ficha activa | Fase 4 | Subformato del preprocesador. |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | F | Elaborar | Alta | Ficha activa | Fase 4 | Subformato del preprocesador. |
| `F-PSEA-11C` | Resultados de homogeneidad | F | Elaborar | Alta | Ficha activa | Fase 4 | Salida de analisis desde `pt_app`. |
| `F-PSEA-11D` | Resultados de estabilidad | F | Elaborar | Alta | Ficha activa | Fase 4 | Salida de analisis desde `pt_app`. |
| `F-PSEA-12` | Datos oficiales consolidados para evaluacion de aptitud | F | Elaborar | Alta | Ficha activa | Fase 4 | Dataset oficial `ronda_<n>_completa.csv`. |
| `F-PSEA-14` | Registro/caso de queja o NC | F | Revisar | Media | Ficha preliminar | Fase 7 | Caso SGC en `calaire-app`; confirmar estructura. |
| `F-PSEA-15` | Registro de apelaciones | F | Revisar | Media | Ficha preliminar | Fase 7 | Correo formal institucional; confirmar estructura. |
| `F-PSEA-16` | Matriz de competencia/autorizacion | F | Mantener / actualizar | Media | Ficha preliminar | Fase 7 | Confirmar estructura de matriz. |
| `F-PSEA-17` | Evaluacion de proveedores criticos | F | Mantener / actualizar | Media | Ficha preliminar | Fase 7 | Confirmar estructura de evaluacion. |

---

## Resumen por clase de ficha

| Clase | Cantidad | Codigos |
|---|---|---|
| Ficha activa | 41 | `DG-PSEA-02`, `DG-PSEA-03`, `P-PSEA-10` a `P-PSEA-07`, `P-PSEA-14` a `P-PSEA-06`, `P-PSEA-02`, `P-PSEA-03`, `P-PSEA-15`, `P-PSEA-05`, `P-PSEA-16`, `P-PSEA-08` a `P-PSEA-21`, `I-PSEA-02`, `I-PSEA-03`, `I-PSEA-04`, `I-PSEA-05`, `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-03`, `F-PSEA-04`, `F-PSEA-05`, `F-PSEA-06`, `F-PSEA-07`, `F-PSEA-08`, `F-PSEA-10`, `F-PSEA-09`, `F-PSEA-11`, `F-PSEA-11A`, `F-PSEA-11B`, `F-PSEA-11C`, `F-PSEA-11D`, `F-PSEA-12` |
| Ficha preliminar | 8 | `P-PSEA-09`, `P-PSEA-22`, `P-PSEA-23`, `F-PSEA-13`, `F-PSEA-14`, `F-PSEA-15`, `F-PSEA-16`, `F-PSEA-17` |
| Ficha diferida | 2 | `DG-PSEA-01`, `P-PSEA-01` |
| Registro de no activo | 7 | `P-PSEA-11`, `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19`, `P-PSEA-22`, `F-PSEA-03`, `F-PSEA-11` |

---

## Resumen por fase de elaboracion

| Fase | Paquete de trabajo | Cantidad |
|---|---|---|
| Fase 3 | Fichas base de arquitectura | 5 |
| Fase 4 | Aplicativos, instructivos y formatos criticos | 11 |
| Fase 5 | Procedimientos transversales tecnicos | 5 |
| Fase 6 | Formatos operativos activos | 9 |
| Fase 7 | Gestion operativa PEA | 13 |
| Fase 8 | Procedimientos por analito | 4 |
| Fase 9 | Documentos diferidos y no activos | 11 |

---

## Criterio de aceptacion de Fase 1

- [x] El universo exacto de fichas esta definido (53 codigos documentales).
- [x] Cada codigo tiene asignado: estado, prioridad, clase de ficha y fase de elaboracion.
- [x] No hay ambiguedad entre ficha activa, preliminar, diferida y no activo.
- [x] Los documentos retirados, reservados, absorbidos y fuera de alcance estan identificados.
- [x] La matriz es consistente con `mapa_tentativo_sgc_pea.md`, `mapa_decisiones_documentales_pea.md` y `sesion_grill_sgc_pea_v1.md`.
