# Plan: Informe Operativo de Ejecucion de Pruebas Piloto

**Created**: 2026-05-06 21:43 -0500
**Updated**: 2026-05-06 22:05 -0500
**Status**: in_progress
**Slug**: informe-operativo-pruebas-piloto

---

## Objetivo

Planificar la elaboracion de un informe operativo que documente de forma trazable la ejecucion de la [[Prueba Piloto]] del esquema [[CALAIRE-EA]], desde la invitacion y confirmacion de participantes hasta la planificacion, ejecucion, analisis estadistico, cierre logistico y lecciones operativas de las dos rondas piloto activas.

El informe debe funcionar como evidencia tecnica y administrativa del piloto, articulando la ejecucion real con los controles del [[QMS]], los formatos PSEA aplicables y el flujo de datos hacia [[CALAIRE-APP]].

---

## Alcance del Informe

### Rondas incluidas

| Ronda | Tipo | Fechas operativas | Participantes | Contaminantes |
|---|---|---|---|---|
| [[Ronda 7]] | Ronda simple | 2026-04-22 a 2026-04-24 | [[SIATA]] (P1) | CO, SO2 |
| [[Ronda 8]] | Ronda doble | 2026-04-29 a 2026-05-04 | [[SIATA]] (P1), [[Universidad Pontificia Bolivariana]] (P2) | O3, NO, NO2 |

### Procesos cubiertos

| Proceso | Contenido minimo a documentar | Evidencia fuente |
|---|---|---|
| Invitacion de participantes | Comunicaciones oficiales, condiciones de participacion, confirmaciones, codificacion P1/P2 | P-PSEA-20, F-PSEA-05, F-PSEA-07, correos archivados |
| Planificacion de ronda | Alcance tecnico, recursos, personal, instalaciones, prerequisitos, criterios de aceptacion | F-PSEA-06 por ronda, F-PSEA-08 a F-PSEA-11 |
| Planificacion estadistica | Valor asignado, incertidumbre, sigma_pt, score aplicable, limitaciones por n bajo | I-PSEA-07, I-PSEA-08, I-PSEA-12, F-PSEA-14 |
| Calendario | Secuencia T-14/T-7/T-3/T-1, montaje, medicion, reporte y cierre | F-PSEA-02, calendario_ppiloto.md, paginas Ronda 7 y Ronda 8 |
| Contaminantes | Justificacion del alcance por analito, niveles, CRM, generacion de atmosfera | F-PSEA-06, F-PSEA-08, I-PSEA-02, I-PSEA-15 |
| Desarrollo de la ronda | Check-in, instalacion, estabilizacion, medicion, incidentes, recepcion de resultados | F-PSEA-08, F-PSEA-11, F-PSEA-12, F-PSEA-13 |
| Cierre y aprendizaje | Desviaciones, no conformidades, acciones, decisiones, mejoras para operacion regular | F-PSEA-15, F-PSEA-16, F-PSEA-17, journals, actas |

---

## Estructura Propuesta del Informe

### 1. Resumen ejecutivo

**Objetivo:** presentar el alcance del piloto, las rondas ejecutadas, participantes, contaminantes y principales conclusiones operativas.

| Subseccion | Contenido esperado |
|---|---|
| 1.1 Proposito del piloto | Validacion operativa del esquema CALAIRE-EA para gases contaminantes criterio |
| 1.2 Rondas ejecutadas | Sintesis comparativa de [[Ronda 7]] y [[Ronda 8]] |
| 1.3 Resultado operativo | Estado de invitaciones, ejecucion, recepcion de datos, analisis y cierre |
| 1.4 Limitaciones | Tamano de muestra reducido, caracter formativo del piloto, controles pendientes |

### 2. Antecedentes y marco operativo

**Objetivo:** explicar por que se ejecuto la prueba piloto, cual es su relacion con el esquema [[CALAIRE-EA]] y que documentos del [[QMS]] la gobiernan.

| Subseccion | Contenido esperado |
|---|---|
| 2.1 Contexto del proyecto | Relacion con el Proyecto 61134 y desarrollo del proveedor de EA |
| 2.2 Marco normativo | ISO/IEC 17043:2023 e ISO 13528:2022 como referencias operativas |
| 2.3 Documentos aplicables | P-PSEA-20, F-PSEA-06, I-PSEA-07, I-PSEA-08, I-PSEA-09, F-PSEA-12 a F-PSEA-14 |
| 2.4 Criterio de confidencialidad | Codificacion P1/P2 y tratamiento de resultados individuales |

### 3. Invitacion y gestion de participantes

**Objetivo:** documentar la trazabilidad de la invitacion, confirmacion, elegibilidad y comunicacion con los laboratorios participantes.

| Subseccion | Contenido esperado |
|---|---|
| 3.1 Estrategia de invitacion | Invitacion directa a laboratorios seleccionados para el piloto |
| 3.2 Confirmacion de SIATA | Participacion como P1 en ronda simple y ronda doble |
| 3.3 Confirmacion de UPB | Participacion como P2 en ronda doble |
| 3.4 Registro de participantes | Evidencia F-PSEA-05/F-PSEA-07, contactos, equipos, codigos anonimos |
| 3.5 Comunicaciones pre-ronda | Paquete de instrucciones, recordatorios, cambios, confirmacion logistica |

### 4. Planificacion operativa de las rondas

**Objetivo:** consolidar la preparacion tecnica y logistica de cada ronda antes de la ejecucion.

| Subseccion | [[Ronda 7]] | [[Ronda 8]] |
|---|---|---|
| Tipo de ronda | Simple | Doble / multi-participante |
| Participantes | P1 = [[SIATA]] | P1 = [[SIATA]], P2 = [[Universidad Pontificia Bolivariana]] |
| Contaminantes | CO, SO2 | O3, NO, NO2 |
| Montaje | 2026-04-22 | 2026-04-29 |
| Medicion | 2026-04-23 | 2026-04-30 a 2026-05-02 |
| Cierre logistico | 2026-04-24 | 2026-05-04 |
| Registros clave | F-PSEA-06, F-PSEA-08 a F-PSEA-12 | F-PSEA-06, F-PSEA-08 a F-PSEA-12 |

### 5. Planificacion estadistica

**Objetivo:** documentar el diseno estadistico aplicado antes y despues de cada ronda, con enfasis en las restricciones del piloto por bajo numero de participantes.

| Tema | Criterio del informe |
|---|---|
| Valor asignado | Derivado de referencia trazable, CRM y sistema de dilucion/generacion |
| Incertidumbre del valor asignado | Reportar `u(x_pt)` por contaminante y nivel cuando este disponible |
| `sigma_pt` | Documentar metodo prescrito de aptitud para el proposito y resolver consistencia interdocumental antes de version final |
| Score aplicable | `z'` o `ζ`, segun relacion entre `u(x_pt)`, `sigma_pt` e incertidumbre reportada por participante |
| n bajo | Declarar que el piloto es formativo y que no usa consenso interlaboratorio como base primaria de `x_pt` |
| Herramienta de calculo | Relacionar flujo de datos portal web / CSV / [[CALAIRE-APP]] |

### 6. Calendario y control de hitos

**Objetivo:** reconstruir la linea de tiempo operativa completa desde invitacion hasta cierre.

| Hito | Criterio de documentacion |
|---|---|
| T-14 | Envio de instrucciones pre-ronda y confirmacion de condiciones |
| T-7 | Verificacion de participantes, equipos, accesos y prerequisitos |
| T-3 | Control documental explicito requerido por brecha D3-02 |
| T-1 | Confirmacion logistica, punto de encuentro, recursos y estado de preparacion |
| Dia 0 | Check-in, montaje, acondicionamiento y verificacion funcional |
| Dia de medicion | Ejecucion de mediciones por contaminante y nivel |
| Post-ronda | Recepcion de resultados, revision de datos, calculo estadistico y cierre |

### 7. Desarrollo de la ejecucion

**Objetivo:** narrar tecnicamente lo ocurrido durante cada ronda y registrar desviaciones frente a lo planificado.

| Subseccion | Contenido esperado |
|---|---|
| 7.1 Recepcion e instalacion | Ingreso de equipos, condiciones de montaje, asignacion de puertos |
| 7.2 Preparacion del item PT | CRM, generacion/dilucion, condiciones ambientales, estabilidad inicial |
| 7.3 Ejecucion de mediciones | Secuencia de concentraciones, registro por analito, ventanas de medicion |
| 7.4 Control de calidad operativo | Cero/span, estabilidad, homogeneidad, registros de condiciones |
| 7.5 Reporte del participante | Entrega de resultados, incertidumbre, observaciones y completitud |
| 7.6 Incidentes y desviaciones | Eventos, impacto, decision tecnica y registro asociado |

### 8. Resultados operativos y estadisticos

**Objetivo:** separar resultados de ejecucion de resultados de desempeno, evitando concluir mas de lo que permite el diseno piloto.

| Resultado | Tratamiento |
|---|---|
| Completitud de ejecucion | Rondas ejecutadas vs planificadas, participantes efectivos, registros completos |
| Completitud de datos | Resultados recibidos por participante, contaminante, nivel y replica |
| Validacion de datos | Reglas de integridad, unidades, cifras significativas, plausibilidad |
| Calculo estadistico | Valor asignado, `u(x_pt)`, `sigma_pt`, score y clasificacion |
| Interpretacion | Enfatizar caracter formativo del piloto y limitaciones por n=1 o n=2 |

### 9. Cierre, lecciones aprendidas y mejoras

**Objetivo:** convertir la ejecucion piloto en acciones de mejora para la operacion regular del esquema.

| Subseccion | Contenido esperado |
|---|---|
| 9.1 Lecciones operativas | Logistica de equipos, tiempos de montaje, comunicacion y acceso |
| 9.2 Lecciones metrologicas | Generacion de atmosferas, estabilidad, incertidumbre y trazabilidad |
| 9.3 Lecciones estadisticas | Uso de `z'`/`ζ`, limitaciones por n bajo, validacion de CALAIRE-APP |
| 9.4 Acciones correctivas/preventivas | NC/CAPA si aplica, ajustes documentales y responsabilidades |
| 9.5 Recomendaciones | Condiciones minimas para ronda regular posterior |

### 10. Anexos

**Objetivo:** dejar trazabilidad documental sin sobrecargar el cuerpo principal del informe.

| Anexo | Contenido |
|---|---|
| A | Matriz de trazabilidad documental por ronda |
| B | Calendario operativo y Gantt |
| C | Comunicaciones e invitaciones |
| D | Registros F-PSEA-05 a F-PSEA-14 por ronda |
| E | Salidas estadisticas y archivos CSV |
| F | Registro de incidentes, quejas, apelaciones o desviaciones, si aplica |

---

## Fases de Elaboracion

### Fase 1: Recoleccion y control de evidencias

**Objetivo:** identificar, consolidar y clasificar las fuentes documentales necesarias para redactar el informe.

| # | Archivo / Fuente | Accion | Descripcion |
|---|---|---|---|
| 1.1 | pages/Prueba Piloto.md | Verificar | Confirmar estado actualizado de rondas, participantes y tareas urgentes |
| 1.2 | pages/Ronda 7.md | Verificar | Extraer fechas, participante, analitos y ciclo operativo |
| 1.3 | pages/Ronda 8.md | Verificar | Extraer fechas, participantes, analitos y ciclo operativo |
| 1.4 | docs/prueba_piloto/ronda_simple/ | Consolidar | Revisar formatos F-PSEA-05 a F-PSEA-14 de la ronda simple |
| 1.5 | docs/prueba_piloto/ronda_compleja_fase1/ | Consolidar | Revisar formatos F-PSEA-05 a F-PSEA-14 de la ronda doble |
| 1.6 | journals/ | Extraer | Recuperar decisiones, incidencias y avances documentados durante la ejecucion |

**Estado:** completada parcialmente para borrador operativo. Se verificaron `pages/Prueba Piloto.md`, `pages/Ronda 7.md`, `pages/Ronda 8.md`, F-PSEA-06 de ronda simple y F-PSEA-06 de ronda compleja fase 1. Se identifico diferencia critica entre participantes previstos y efectivos en [[Ronda 8]]: P2/UPB fue diferido y debe conservarse como cambio operativo controlado.

### Fase 2: Definicion del esqueleto del informe

**Objetivo:** crear el documento base con estructura, alcance, tablas maestras y secciones listas para diligenciamiento.

| # | Archivo | Accion | Descripcion |
|---|---|---|---|
| 2.1 | docs/prueba_piloto/informe_operativo_prueba_piloto.md | Crear | Documento maestro del informe operativo |
| 2.2 | docs/prueba_piloto/informe_operativo_prueba_piloto.md | Redactar | Resumen ejecutivo, antecedentes, alcance y matriz de rondas |
| 2.3 | docs/prueba_piloto/informe_operativo_prueba_piloto.md | Estructurar | Agregar secciones 3 a 10 y placeholders controlados para datos faltantes |
| 2.4 | pages/Prueba Piloto.md | Actualizar | Enlazar el informe desde el MOC operativo |

**Estado:** completada. Se creo `docs/prueba_piloto/informe_operativo_prueba_piloto.md` y se enlazo desde `pages/Prueba Piloto.md`.

### Fase 3: Redaccion tecnica por proceso

**Objetivo:** desarrollar las secciones principales del informe con lenguaje tecnico, trazabilidad normativa y referencias internas.

| # | Seccion | Accion | Descripcion |
|---|---|---|---|
| 3.1 | Invitacion y participantes | Redactar | Documentar comunicacion, elegibilidad, confirmaciones y codificacion |
| 3.2 | Planificacion de ronda | Redactar | Consolidar F-PSEA-06, recursos, personal, calendario y condiciones |
| 3.3 | Planificacion estadistica | Redactar | Explicar `x_pt`, `u(x_pt)`, `sigma_pt`, score y limitaciones del piloto |
| 3.4 | Calendario | Redactar | Reconstruir hitos T-14 a cierre, incluyendo control T-3 |
| 3.5 | Contaminantes | Redactar | Describir CO, SO2, O3, NO y NO2 por ronda y soporte metrologico |
| 3.6 | Desarrollo de la ronda | Redactar | Narrar recepcion, montaje, medicion, reporte y desviaciones |

### Fase 4: Resultados, cierre y lecciones aprendidas

**Objetivo:** cerrar el informe con resultados operativos, interpretacion estadistica prudente y acciones de mejora.

| # | Seccion | Accion | Descripcion |
|---|---|---|---|
| 4.1 | Resultados operativos | Redactar | Evaluar completitud de ejecucion, registros y datos recibidos |
| 4.2 | Resultados estadisticos | Redactar | Incorporar tablas de score y salida de [[CALAIRE-APP]] cuando existan |
| 4.3 | Incidentes y desviaciones | Redactar | Relacionar NC/CAPA, quejas, apelaciones o decisiones tecnicas |
| 4.4 | Lecciones aprendidas | Redactar | Formular mejoras para comunicacion, logistica, metrologia y software |
| 4.5 | Recomendaciones | Redactar | Definir condiciones minimas para rondas regulares posteriores |

### Fase 5: Revision, control de calidad y publicacion interna

**Objetivo:** validar que el informe sea consistente, auditable y navegable dentro del grafo Logseq.

| # | Archivo | Accion | Descripcion |
|---|---|---|---|
| 5.1 | docs/prueba_piloto/informe_operativo_prueba_piloto.md | Revisar | Verificar completitud, coherencia tecnica, links y propiedades |
| 5.2 | docs/prueba_piloto/informe_operativo_prueba_piloto.md | Corregir | Cerrar brechas de `sigma_pt`, T-3, fechas y participantes efectivos |
| 5.3 | pages/Prueba Piloto.md | Verificar | Confirmar que el informe queda enlazado desde el MOC |
| 5.4 | logs/CURRENT_SESSION.md | Actualizar | Registrar estado del informe y proximos pasos |
| 5.5 | git | Commit | Confirmar cambios documentales con mensaje significativo |

---

## Controles Criticos

| Control | Riesgo que mitiga | Accion requerida |
|---|---|---|
| Coherencia de `sigma_pt` | Contradiccion entre F-PSEA-06, I-PSEA-07 e I-PSEA-09 | Resolver antes de emitir version final del informe |
| Hito T-3 | Secuencia pre-ronda incompleta | Incluir como control explicito en calendario y checklist |
| Participantes efectivos | Diferencia entre participantes previstos y ejecutados | Documentar claramente por ronda y no mezclar fases |
| Caracter formativo del piloto | Interpretacion excesiva de desempeno con n bajo | Declarar limitaciones estadisticas en resumen y resultados |
| Evidencia de comunicaciones | Observacion por trazabilidad incompleta | Relacionar correos, F-PSEA-05 y F-PSEA-07 |
| Integridad de datos | Resultados no comparables por unidad o formato | Verificar F-PSEA-12/F-PSEA-13 antes de calculo estadistico |

---

## Criterios de Aceptacion

| Criterio | Condicion de aceptacion |
|---|---|
| Alcance completo | El informe cubre invitacion, planificacion, estadistica, calendario, contaminantes, ejecucion, resultados y cierre |
| Trazabilidad por ronda | [[Ronda 7]] y [[Ronda 8]] tienen matrices separadas de participantes, contaminantes, fechas, registros y resultados |
| Trazabilidad documental | Cada afirmacion operativa relevante enlaza o referencia formato, pagina o journal fuente |
| Coherencia estadistica | `x_pt`, `u(x_pt)`, `sigma_pt` y score estan explicados sin contradicciones entre documentos |
| Lenguaje tecnico | Redaccion en espanol profesional, impersonal, compatible con documentacion SGC |
| Integracion Logseq | El informe esta enlazado desde [[Prueba Piloto]] y usa referencias internas consistentes |
| Gestion de brechas | Las brechas `sigma_pt` y T-3 quedan cerradas o marcadas explicitamente como pendientes controlados |

---

## Log de Ejecucion

- [x] Plan creado
- [ ] Fase 1 iniciada
- [ ] Fase 1 completada
- [ ] Fase 2 iniciada
- [ ] Fase 2 completada
- [ ] Fase 3 iniciada
- [ ] Fase 3 completada
- [ ] Fase 4 iniciada
- [ ] Fase 4 completada
- [ ] Fase 5 iniciada
- [ ] Fase 5 completada
