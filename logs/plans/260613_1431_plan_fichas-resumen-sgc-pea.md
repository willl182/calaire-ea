# Plan: Elaboracion de Fichas Resumen del SGC PEA

**Created**: 2026-06-13 14:31  
**Updated**: 2026-06-13 15:03  
**Status**: completed  
**Slug**: fichas-resumen-sgc-pea

---

## Objetivo

Planificar la elaboracion controlada de fichas resumen para cada documento, procedimiento, instructivo, formato y registro del sistema documental PEA, usando como base `sesion_grill_sgc_pea_v1.md`, `mapa_tentativo_sgc_pea.md` y `mapa_decisiones_documentales_pea.md`.

El resultado esperado no es desarrollar todavia todos los documentos, sino crear una capa de fichas que estabilice el perfil de cada elemento documental: proposito, estado, alcance, relaciones, aplicativo asociado, entradas/salidas, riesgos de interpretacion y criterios minimos para su posterior elaboracion.

---

## Fuentes Base

| Fuente | Uso en el plan |
|---|---|
| `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md` | Decisiones conceptuales, restricciones, flujo oficial de datos y errores a evitar. |
| `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md` | Inventario operativo de documentos, estados, familias, relaciones y orden tentativo de elaboracion. |
| `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md` | Decisiones firmes por codigo documental, documentos retirados/reservados/absorbidos y controles de calidad. |

---

## Alcance

### Incluye

- Fichas para documentos generales `DG-PSEA`.
- Fichas para procedimientos `P-PSEA`.
- Fichas para instructivos `I-PSEA`.
- Fichas para formatos, registros, exportaciones y salidas `F-PSEA`.
- Fichas separadas para subformatos de homogeneidad/estabilidad `F-PSEA-13A` a `F-PSEA-13D`.
- Registro minimo para documentos retirados, reservados, absorbidos o fuera del alcance documental propio del PEA.

### No incluye

- Desarrollo completo de procedimientos, formatos o instructivos.
- Actualizacion de `sgc_res.md`, `README.md` o `P-PSEA-01` en esta fase.
- Definicion detallada del contenido del informe final `F-PSEA-04`.
- Desarrollo de riesgos generales `P-PSEA-14` o mejora continua `P-PSEA-15`.
- Aprobacion, obsolescencia, retencion documental o control documental macro.
- Conversion automatica de archivos tecnicos internos del preprocesador en formatos `F-PSEA`.

---

## Estructura Estandar de Cada Ficha

Cada ficha debe usar una estructura uniforme:

| Campo | Proposito |
|---|---|
| Codigo | Identificador documental (`DG-PSEA`, `P-PSEA`, `I-PSEA`, `F-PSEA`). |
| Nombre decidido | Nombre operativo consolidado en el mapa documental. |
| Tipo documental | Documento general, procedimiento, instructivo, formato, registro, matriz, exportacion o salida. |
| Estado | Mantener, actualizar, elaborar, revisar, reservar, retirar o absorber. |
| Prioridad | Alta, media-alta, media, baja, cierre o no priorizar. |
| Proposito operativo | Que controla, guia, registra, evidencia o produce dentro del PEA. |
| Rol en el flujo | Entrada, salida, registro oficial, evidencia, criterio tecnico, instructivo, matriz o soporte documental. |
| Aplicativo asociado | `calaire-app`, `pt_app`, ambos o ninguno. |
| Entradas principales | Documentos, datos o eventos que alimentan el elemento documental. |
| Salidas principales | Registros, evidencias, decisiones, exportaciones o documentos generados. |
| Documentos relacionados | Procedimientos, formatos, instructivos o aplicativos vinculados. |
| Limites de alcance | Que no debe duplicar, que no gobierna o que queda fuera de esta ficha. |
| Riesgos de interpretacion | Confusiones conocidas que deben evitarse. |
| Criterio minimo de elaboracion | Condicion para considerar lista la ficha. |

---

## Clasificacion de Fichas

| Clase | Criterio | Tratamiento |
|---|---|---|
| Ficha activa | Documento vigente o requerido para el flujo PEA. | Desarrollar ficha completa. |
| Ficha preliminar | Documento requerido, pero con contenido deliberadamente abierto o no priorizado. | Registrar alcance, estado y restricciones; no desarrollar contenido de fondo. |
| Ficha diferida | Documento marco que debe cerrarse al final. | Registrar dependencia de cierre y no usar como fuente normativa final. |
| Registro de no activo | Documento retirado, reservado, absorbido o fuera de alcance. | Registrar decision, razon y documento sustituto cuando aplique. |

---

## Fases

### Fase 1: Consolidar Inventario Maestro de Fichas

**Objetivo:** definir el universo exacto de fichas y clasificar cada codigo documental antes de redactar.

| # | Archivo / grupo | Accion | Descripcion |
|---|---|---|---|
| 1.1 | `DG-PSEA` | Inventariar | Incluir `DG-PSEA-01`, `DG-PSEA-02`, `DG-PSEA-03`; marcar `DG-PSEA-01` como ficha diferida de cierre. |
| 1.2 | `P-PSEA` | Inventariar | Clasificar procedimientos activos, preliminares, diferidos, retirados, reservados o absorbidos. |
| 1.3 | `I-PSEA` | Inventariar | Incluir `I-PSEA-10`, `I-PSEA-16`, `I-PSEA-17`, `I-PSEA-18`. |
| 1.4 | `F-PSEA` | Inventariar | Incluir formatos activos, subformatos H/E y registros de gestion; separar `F-PSEA-03` y `F-PSEA-11` como no activos. |
| 1.5 | Archivos tecnicos internos | Mapear | Listarlos solo como insumos de `P-PSEA-23`, sin convertirlos en fichas `F-PSEA`. |

**Criterio de aceptacion:** existe una matriz de fichas con codigo, nombre, familia, estado, prioridad, clase de ficha y fase de elaboracion.

### Fase 2: Crear Plantilla Base de Ficha Resumen

**Objetivo:** crear una plantilla unica para que todos los subagentes elaboren fichas con el mismo criterio.

| # | Archivo / grupo | Accion | Descripcion |
|---|---|---|---|
| 2.1 | Plantilla de ficha | Crear | Definir campos obligatorios y orden de secciones. |
| 2.2 | Reglas de redaccion | Crear | Incluir voz tecnica, alcance, no duplicacion y trazabilidad documental. |
| 2.3 | Checklist de calidad | Crear | Incluir controles para aplicativos, flujo de datos, H/E, `F-PSEA-12` vs `F-PSEA-14`, y documentos no activos. |

**Criterio de aceptacion:** la plantilla permite elaborar fichas comparables y evita decisiones contradictorias con los mapas base.

### Fase 3: Elaborar Fichas Base de Arquitectura

**Objetivo:** estabilizar primero las fichas que gobiernan el mapa documental y el flujo digital.

| # | Documento | Accion | Descripcion |
|---|---|---|---|
| 3.1 | `P-PSEA-12` | Elaborar ficha | Matriz documental basica del PEA: `DG`, `P`, `I`, `F` y subformatos. |
| 3.2 | `P-PSEA-13` | Elaborar ficha | Matriz de registros/evidencias generadas por ronda o evento. |
| 3.3 | `P-PSEA-23` | Elaborar ficha | Flujo tecnico de datos digitales, aplicativos, archivos tecnicos y salidas oficiales. |
| 3.4 | `DG-PSEA-02` | Elaborar ficha | Aplicativo `calaire-app` como documento general. |
| 3.5 | `DG-PSEA-03` | Elaborar ficha | Aplicativo `pt_app` como documento general. |

**Criterio de aceptacion:** las fichas base explican claramente la diferencia entre matriz documental, matriz de evidencias y flujo tecnico de datos.

### Fase 4: Elaborar Fichas de Aplicativos, Instructivos y Formatos Criticos Nuevos

**Objetivo:** documentar los elementos que habilitan el flujo digital y los formatos nuevos o redefinidos.

| # | Documento / grupo | Accion | Descripcion |
|---|---|---|---|
| 4.1 | `I-PSEA-17`, `I-PSEA-18` | Elaborar fichas | Instructivos de preprocesador y modulo de analisis de `pt_app`; no reemplazan `P-PSEA-06`. |
| 4.2 | `I-PSEA-10`, `I-PSEA-16` | Elaborar fichas | Instructivos de usuario participante y administrador de rondas en `calaire-app`. |
| 4.3 | `F-PSEA-07` | Elaborar ficha | Ficha digital de ronda exportada desde `calaire-app`; insumo de `F-PSEA-06`. |
| 4.4 | `F-PSEA-10` | Elaborar ficha | Registro de preprocesamiento de datos; referencia `preprocesamiento_log.csv`. |
| 4.5 | `F-PSEA-13A-D` | Elaborar fichas | Subformatos de datos/resultados de homogeneidad y estabilidad. |
| 4.6 | `F-PSEA-14` | Elaborar ficha | Dataset oficial consolidado `ronda_<n>_completa.csv`. |

**Criterio de aceptacion:** queda cerrado el perfil documental de los insumos/salidas criticos del flujo `calaire-app` -> `pt_app`.

### Fase 5: Elaborar Fichas de Procedimientos Transversales Tecnicos

**Objetivo:** fichar los procedimientos que deben citar los documentos especificos por gas.

| # | Documento | Accion | Descripcion |
|---|---|---|---|
| 5.1 | `P-PSEA-06` | Elaborar ficha | Procedimiento central de diseno estadistico, valor asignado, `sigma_pt`, incertidumbre, outliers, H/E y desempeno. |
| 5.2 | `P-PSEA-07` | Elaborar ficha preliminar | Generacion/emision del informe; absorbe `P-PSEA-22`; no desarrollar contenido detallado de `F-PSEA-04`. |
| 5.3 | `P-PSEA-09` | Elaborar ficha | Planificacion de ronda con soporte de `calaire-app` y formatos exportables. |
| 5.4 | `P-PSEA-10` | Elaborar ficha | Preparacion y control del item gaseoso; no envio/recepcion fisica de items. |

**Criterio de aceptacion:** los procedimientos transversales quedan listos para ser citados por procedimientos por analito sin duplicacion.

### Fase 6: Elaborar Fichas de Formatos Operativos Activos

**Objetivo:** fichar los registros y formatos activos que soportan planificacion, participantes, datos, H/E e informe.

| # | Documento / grupo | Accion | Descripcion |
|---|---|---|---|
| 6.1 | `F-PSEA-01`, `F-PSEA-02` | Elaborar fichas | Calendario global y cronograma detallado de ronda. |
| 6.2 | `F-PSEA-04` | Elaborar ficha preliminar | Informe final generado desde `pt_app`; sin detallar contenido aun. |
| 6.3 | `F-PSEA-05`, `F-PSEA-05A` | Elaborar fichas | Participacion y anexo tecnico de equipos/instrumentos. |
| 6.4 | `F-PSEA-06`, `F-PSEA-08` | Elaborar fichas | Plan de ronda y dossier de preparacion/control del item. |
| 6.5 | `F-PSEA-09`, `F-PSEA-12` | Elaborar fichas | Datos reportados y exportacion oficial desde `calaire-app`; no confundir `F-PSEA-12` con `F-PSEA-14`. |
| 6.6 | `F-PSEA-13` | Elaborar ficha | Registro principal de homogeneidad y estabilidad. |

**Criterio de aceptacion:** cada formato activo indica origen, responsable funcional, procedimiento relacionado, salida esperada y aplicativo asociado cuando aplique.

### Fase 7: Elaborar Fichas de Gestion Operativa PEA

**Objetivo:** fichar los procedimientos y registros de gestion que soportan control operativo del PEA.

| # | Documento / grupo | Accion | Descripcion |
|---|---|---|---|
| 7.1 | `P-PSEA-08` | Elaborar ficha | Colusion y falsificacion; conecta con `P-PSEA-16`, `P-PSEA-21`, `P-PSEA-26`. |
| 7.2 | `P-PSEA-16` | Elaborar ficha | Trabajo no conforme, no conformidades y acciones correctivas. |
| 7.3 | `P-PSEA-20`, `P-PSEA-21` | Elaborar fichas | Comunicaciones y control de valores sensibles. |
| 7.4 | `P-PSEA-24`, `P-PSEA-25` | Elaborar fichas | Quejas como casos en `calaire-app`; apelaciones por correo formal institucional. |
| 7.5 | `P-PSEA-26`, `P-PSEA-27`, `P-PSEA-28` | Elaborar fichas | Confidencialidad operativa, competencia/autorizacion y proveedores criticos. |
| 7.6 | `F-PSEA-16`, `F-PSEA-17`, `F-PSEA-21`, `F-PSEA-23` | Elaborar fichas preliminares | Registros asociados a quejas/NC, apelaciones, competencia y proveedores; algunos requieren confirmacion de estructura. |

**Criterio de aceptacion:** las fichas distinguen claramente quejas, apelaciones, TNC/NC/CAPA, confidencialidad, competencia y proveedores criticos.

### Fase 8: Elaborar Fichas de Procedimientos por Analito

**Objetivo:** fichar los procedimientos tecnicos por gas despues de estabilizar documentos transversales.

| # | Documento | Accion | Descripcion |
|---|---|---|---|
| 8.1 | `P-PSEA-02` | Elaborar ficha | Procedimiento tecnico NO/NO2; conservar particularidades del gas. |
| 8.2 | `P-PSEA-03` | Elaborar ficha | Procedimiento tecnico CO; conservar particularidades del gas. |
| 8.3 | `P-PSEA-04` | Elaborar ficha | Procedimiento tecnico O3; corregir referencias antiguas. |
| 8.4 | `P-PSEA-05` | Elaborar ficha | Procedimiento tecnico SO2; conservar particularidades del gas. |

**Criterio de aceptacion:** cada ficha indica que el procedimiento por analito debe citar documentos transversales y no duplicar estadistica, H/E, informe ni flujo de datos.

### Fase 9: Registrar Documentos Diferidos y No Activos

**Objetivo:** dejar trazabilidad de documentos que no deben desarrollarse como fichas activas.

| # | Documento / grupo | Accion | Descripcion |
|---|---|---|---|
| 9.1 | `P-PSEA-11`, `F-PSEA-03`, `F-PSEA-11` | Registrar no activo | Reservados/no aplicables por ausencia de envio fisico de items o sustitucion documental. |
| 9.2 | `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19` | Registrar retirados | Fuera del alcance documental propio del PEA; corresponden al SGC macro o gestion externa. |
| 9.3 | `P-PSEA-22` | Registrar absorbido | Absorbido por `P-PSEA-07`. |
| 9.4 | `P-PSEA-14`, `P-PSEA-15` | Registrar preliminar/diferido | Mantener como ideas por elaborar; no desarrollar ahora. |
| 9.5 | `DG-PSEA-01`, `P-PSEA-01` | Registrar cierre | Revisar al final, cuando el sistema de fichas y documentos base este estabilizado. |

**Criterio de aceptacion:** ningun documento retirado, reservado o absorbido queda confundido con una ficha activa.

### Fase 10: Revision de Calidad e Integracion

**Objetivo:** auditar consistencia, relaciones y riesgos de interpretacion antes de usar las fichas para elaborar documentos.

| # | Control | Accion | Descripcion |
|---|---|---|---|
| 10.1 | Tipologia documental | Verificar | Ningun aplicativo queda como formato; ningun archivo tecnico interno queda promovido a `F-PSEA` sin decision explicita. |
| 10.2 | Flujo de datos | Verificar | `F-PSEA-12` y `F-PSEA-14` estan claramente diferenciados; `F-PSEA-10` referencia `preprocesamiento_log.csv`. |
| 10.3 | H/E | Verificar | `F-PSEA-13` y `F-PSEA-13A-D` quedan integrados con `P-PSEA-06`, `P-PSEA-10` y `P-PSEA-23`. |
| 10.4 | Informe | Verificar | `P-PSEA-07` y `F-PSEA-04` se mantienen en nivel preliminar sin definir contenido detallado del informe. |
| 10.5 | Procedimientos por gas | Verificar | `P-PSEA-02` a `P-PSEA-05` no duplican estadistica, H/E, informe ni flujo de datos. |
| 10.6 | Gestion operativa | Verificar | Quejas, apelaciones, TNC/NC/CAPA, confidencialidad, competencia y proveedores quedan separados. |
| 10.7 | Cierre documental | Verificar | `sgc_res.md`, `README.md` y `P-PSEA-01` siguen sin actualizarse hasta el cierre global. |

**Criterio de aceptacion:** el conjunto de fichas puede usarse como base para asignar subagentes de redaccion sin reabrir decisiones ya estabilizadas.

---

## Asignacion Propuesta de Subagentes para Elaboracion de Fichas

| Subagente | Paquete de trabajo | Documentos |
|---|---|---|
| Subagente A - Arquitectura documental | Fichas base y matrices | `P-PSEA-12`, `P-PSEA-13`, `P-PSEA-23`, `DG-PSEA-02`, `DG-PSEA-03`. |
| Subagente B - Flujo digital y formatos criticos | Aplicativos, instructivos y formatos de datos | `I-PSEA-17`, `I-PSEA-18`, `F-PSEA-07`, `F-PSEA-10`, `F-PSEA-13A-D`, `F-PSEA-14`. |
| Subagente C - Procedimientos transversales tecnicos | Nucleo tecnico-operativo | `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09`, `P-PSEA-10`, `F-PSEA-04`. |
| Subagente D - Formatos operativos activos | Planificacion, participantes, item y H/E | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-05`, `F-PSEA-05A`, `F-PSEA-06`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-13`. |
| Subagente E - Gestion operativa PEA | Quejas, apelaciones, TNC/NC/CAPA y controles | `P-PSEA-08`, `P-PSEA-16`, `P-PSEA-20`, `P-PSEA-21`, `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-26`, `P-PSEA-27`, `P-PSEA-28`, `F-PSEA-16`, `F-PSEA-17`, `F-PSEA-21`, `F-PSEA-23`. |
| Subagente F - Procedimientos por analito | Fichas especificas por gas | `P-PSEA-02`, `P-PSEA-03`, `P-PSEA-04`, `P-PSEA-05`. |
| Subagente G - Control de no activos y cierre | Documentos diferidos, retirados, reservados o absorbidos | `DG-PSEA-01`, `P-PSEA-01`, `P-PSEA-11`, `P-PSEA-14`, `P-PSEA-15`, `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19`, `P-PSEA-22`, `F-PSEA-03`, `F-PSEA-11`. |

---

## Reglas Para Subagentes de Redaccion

1. No editar `sgc_res.md`, `README.md` ni `P-PSEA-01`.
2. No desarrollar contenido completo de procedimientos o formatos; producir solo ficha resumen.
3. No inventar estados documentales diferentes a los consolidados en los mapas base.
4. No convertir `calaire-app` ni `pt_app` en formatos.
5. No convertir archivos tecnicos internos del preprocesador en formatos `F-PSEA`.
6. No confundir `F-PSEA-12` con `F-PSEA-14`.
7. No tratar `F-PSEA-10` como aplicativo.
8. No afirmar que H/E no aplica; H/E se documenta en `F-PSEA-13` y subformatos.
9. Mantener `F-PSEA-04` como ficha preliminar si aparece contenido detallado del informe.
10. Marcar documentos retirados, reservados o absorbidos como registro de no activo, no como ficha activa.

---

## Riesgos y Controles

| Riesgo | Impacto | Control |
|---|---|---|
| Mezclar aplicativo con formato | Confusion de arquitectura documental | Verificacion de tipo documental en cada ficha. |
| Promover archivos tecnicos a `F-PSEA` sin decision | Inflacion documental y perdida de trazabilidad | Mapear archivos tecnicos solo en `P-PSEA-23`. |
| Duplicar contenido tecnico transversal en procedimientos por gas | Documentos largos, inconsistentes y dificiles de mantener | Fichar primero `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-23`. |
| Confundir `F-PSEA-12` y `F-PSEA-14` | Error en flujo oficial de datos | Campo obligatorio de entradas/salidas y aplicativo asociado. |
| Cerrar prematuramente `F-PSEA-04` | Definicion incompleta del informe final | Ficha preliminar con restriccion expresa. |
| Desarrollar documentos no priorizados | Desvio del foco actual | Clase de ficha: preliminar, diferida o no activa. |
| Tocar documentos aplazados | Romper la secuencia de estabilizacion | Regla explicita de no editar `sgc_res.md`, `README.md`, `P-PSEA-01`. |

---

## Log de Ejecucion

- [x] Revision inicial delegada a tres subagentes sobre los documentos base.
- [x] Insumos de subagentes incorporados al plan.
- [x] Plan de elaboracion de fichas creado.
- [x] Fase 1 iniciada.
- [x] Fase 1 completada. Inventario maestro creado en `docs/documentacion_sgc/fichas_resumen/00_inventario_maestro_fichas.md`.
- [x] Fase 2 iniciada.
- [x] Fase 2 completada. Plantilla base creada en `docs/documentacion_sgc/fichas_resumen/00_plantilla_ficha_resumen.md`.
- [x] Subagentes A-G asignados y documentos de asignacion creados en `docs/documentacion_sgc/fichas_resumen/asignacion_subagente_*.md`.
- [x] Fase 3 iniciada. Subagente A: 5 fichas base de arquitectura creadas.
- [x] Fase 3 completada. `P-PSEA-12`, `P-PSEA-13`, `P-PSEA-23`, `DG-PSEA-02`, `DG-PSEA-03`.
- [x] Fase 4 iniciada. Subagente B: 8 fichas de flujo digital y formatos criticos creadas.
- [x] Fase 4 completada. `I-PSEA-17`, `I-PSEA-18`, `F-PSEA-07`, `F-PSEA-10`, `F-PSEA-13A-D`, `F-PSEA-14`.
- [x] Fase 5 iniciada. Subagente C: 5 fichas de procedimientos transversales tecnicos creadas.
- [x] Fase 5 completada. `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09`, `P-PSEA-10`, `F-PSEA-04`.
- [x] Fase 6 iniciada. Subagente D: 9 fichas de formatos operativos activos creadas.
- [x] Fase 6 completada. `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-05`, `F-PSEA-05A`, `F-PSEA-06`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-13`.
- [x] Fase 7 iniciada. Subagente E: 13 fichas de gestion operativa PEA creadas.
- [x] Fase 7 completada. `P-PSEA-08`, `P-PSEA-16`, `P-PSEA-20`, `P-PSEA-21`, `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-26`, `P-PSEA-27`, `P-PSEA-28`, `F-PSEA-16`, `F-PSEA-17`, `F-PSEA-21`, `F-PSEA-23`.
- [x] Fase 8 iniciada. Subagente F: 4 fichas de procedimientos por analito creadas.
- [x] Fase 8 completada. `P-PSEA-02`, `P-PSEA-03`, `P-PSEA-04`, `P-PSEA-05`.
- [x] Fase 9 iniciada. Subagente G: 11 fichas de control de no activos y cierre creadas.
- [x] Fase 9 completada. `DG-PSEA-01`, `P-PSEA-01`, `P-PSEA-11`, `P-PSEA-14`, `P-PSEA-15`, `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19`, `P-PSEA-22`, `F-PSEA-03`, `F-PSEA-11`.
- [x] Fase 10 iniciada.
- [x] Fase 10 completada. Se ejecutó la auditoría programática con `audit_fichas.py` y se verificó el cumplimiento de las 10 reglas de calidad. Se corrigieron los subformatos F-PSEA-13 y F-PSEA-13A-D para integrarlos plenamente con P-PSEA-23.

