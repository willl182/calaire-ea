# Plan: Ajuste de F-PSEA-06 Ronda Simple

**Created**: 2026-04-10 10:26 -0500
**Updated**: 2026-04-10 11:09 -0500
**Status**: completed
**Slug**: ajuste-fpsea06-ronda-simple

---

## Objetivo

Ajustar `docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md` para convertir el placeholder actual en un plan operativo de ronda simple listo para diligenciamiento y aprobación, integrando la estructura ya definida para la ronda CO/SO₂ con SIATA y la información normativa-operativa contenida en `docs/prueba_piloto/Planificación antes del inicio del ensayo de aptitud.docx.md`.

---

## Fases

### Fase 1: Consolidación de insumos y criterios del formato

**Objetivo:** identificar qué información del documento de planificación general aplica de forma directa a la ronda simple y qué elementos deben excluirse o adaptarse por corresponder a escenarios multi-analito o multi-participante.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Verificar | Levantar la estructura actual del placeholder, campos abiertos y vacíos críticos |
| 1.2 | docs/prueba_piloto/Planificación antes del inicio del ensayo de aptitud.docx.md | Analizar | Mapear los puntos a)–u) de planificación previa contra secciones potenciales del plan de ronda |
| 1.3 | logs/CURRENT_SESSION.md | Verificar | Confirmar restricciones ya definidas para la ronda simple: analitos, participante, semana, duración, método de valor asignado y enfoque estadístico |
| 1.4 | docs/prueba_piloto/I-PSEA-07 Diseño Estadístico.md | Verificar | Confirmar que para n=1 se documente uso de valor de referencia trazable y σ_pt prescrito |
| 1.5 | docs/prueba_piloto/I-PSEA-09 Instrucciones a Participantes.md | Verificar | Alinear información de cronograma, comunicaciones previas y requisitos del participante |
| 1.6 | docs/prueba_piloto/P-PSEA-10 Procedimiento de Manejo de Items PT.md | Verificar | Extraer requisitos operativos sobre CRM, manifold, almacenamiento, check-in y condiciones del ítem PT in situ |

**Resultado Fase 1 ejecutada (2026-04-10):**

| Fuente | Hallazgo consolidado | Implicación para F-PSEA-06 |
|---|---|---|
| `F-PSEA-06` actual | El archivo de ronda simple sigue como placeholder descriptivo; no tiene estructura de aprobación, recursos, cronograma ni matriz de responsabilidades | En Fase 2 debe migrar de ficha-resumen a formato operativo diligenciable |
| `Planificación antes del inicio...docx.md` | Los puntos a)–u) sí aportan contenido para personal, criterios de participación, riesgos, cronograma, reporte y control estadístico, pero están redactados a nivel de programa | En Fase 3 se debe especializar cada punto a la ronda simple y evitar copiar el documento fuente como bloque narrativo |
| `logs/CURRENT_SESSION.md` | La ronda simple está confirmada como CO y SO₂ con SIATA, semana 20–25 abr 2026, duración 1 jornada, con valor asignado trazable y σ_pt prescrito | Estos parámetros se toman como restricciones base del formato; no deben reabrirse en el ajuste |
| `I-PSEA-07` | Para n=1 no aplica consenso; debe documentarse referencia trazable para `x_pt`, `σ_pt` prescrito y score `z'` o `ζ` | F-PSEA-06 no debe heredar el texto del documento fuente sobre consenso o mediana para participantes múltiples |
| `I-PSEA-09` | El paquete pre-ronda exige T-14, F-PSEA-05A, cronograma previo, requisitos del participante y datos de contacto del coordinador | F-PSEA-06 debe incluir una vista de cronograma y prerrequisitos alineada con la comunicación pre-ronda |
| `P-PSEA-10` | El ítem PT es una atmósfera generada in situ; los cilindros de participantes no son el ítem PT. Se requiere control de MRC, manifold, check-in y condiciones seguras | F-PSEA-06 debe separar claramente recursos de CALAIRE, materiales del participante y condiciones de operación del manifold |

**Criterios definidos para el ajuste:**

- Se incorporan al plan de ronda los puntos del documento fuente vinculados con personal, servicios externos, requisitos del participante, cronograma, riesgos técnicos, trazabilidad, reporte y confidencialidad.
- Se adaptan los contenidos que en el documento fuente están redactados para el programa EA completo, aterrizándolos a una sola ronda, un solo participante y dos analitos.
- Se excluyen del F-PSEA-06 de ronda simple los enfoques de consenso entre participantes, la lógica de simultaneidad multi-laboratorio y cualquier formulación que presuponga operación con hasta ocho instrumentos.
- Se mantiene como dato pendiente únicamente lo que no puede inferirse con la evidencia disponible: código formal de ronda, responsables nominales, certificados/lotes CRM, setpoints aprobados, `σ_pt` final por analito y firmas.

**Mapa inicial de aplicabilidad del documento fuente `a)`–`u)`:**

| Estado | Ítems | Criterio |
|---|---|---|
| Aplicación directa | a, c, e, g, h, i, j, l, m, n, s, t, u | Se pueden convertir en secciones o tablas operativas del plan de ronda |
| Aplicación adaptada | b, d, f, k, o, p, q, r | Requieren especialización a SIATA, CO/SO₂, n=1 y enfoque de referencia trazable |
| Exclusión parcial | d, o | Se elimina del ajuste la parte asociada a capacidad máxima simultánea y a valor asignado por consenso |

### Fase 2: Diseño de la estructura objetivo del plan de ronda

**Objetivo:** definir la arquitectura del documento para que F-PSEA-06 opere como formato de ejecución y control, no solo como nota descriptiva.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Reemplazar la sección descriptiva actual por secciones operativas del plan: identificación, alcance, participantes, recursos, cronograma, criterios, aprobaciones |
| 2.2 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Incorporar tabla maestra de la ronda simple con participante P1 = SIATA, analitos CO y SO₂, semana 20–25 abr 2026 y duración de 1 jornada |
| 2.3 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Definir subsección de recursos críticos: CRM, sistema de dilución, aire cero, generador, manifold, UPS, control ambiental y personal autorizado |
| 2.4 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Definir subsección de control estadístico: origen de x_pt, criterio para σ_pt, score aplicable y referencias cruzadas a instructivos técnicos |

**Resultado Fase 2 ejecutada (2026-04-10):**

| Componente | Implementación realizada | Efecto sobre el formato |
|---|---|---|
| Identificación documental | Se añadieron secciones de control, alcance técnico y aprobaciones | El formato ya opera como registro aprobable y no como nota descriptiva |
| Tabla maestra de ronda | Se consolidó participante, analitos, ventana operativa y duración | La ronda simple quedó fijada en una sola vista operativa |
| Recursos críticos | Se separaron recursos CALAIRE, personal autorizado y criterios del ítem PT | Se evita confundir CRM/manifold con materiales del participante |
| Control estadístico | Se incorporó matriz pre-ronda para `x_pt`, `u(x_pt)`, `σ_pt` y score | El formato quedó alineado con `I-PSEA-07` para n=1 sin lógica de consenso |

### Fase 3: Aterrizaje del contenido del documento de planificación previa

**Objetivo:** traducir la planificación general a contenido específico de la ronda simple, indicando explícitamente qué puntos aplican, cuáles se adaptan y cuáles no corresponden a esta ronda.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Integrar el punto a) en matriz de roles y responsabilidades del personal involucrado |
| 3.2 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Integrar los puntos b), h) y u) en apartados de proveedores/servicios externos, control de ítems PT y respuesta ante incidentes |
| 3.3 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Integrar los puntos c), d), e), j), k) y l) en requisitos del participante, actividades, información a suministrar y cronograma operativo |
| 3.4 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Integrar los puntos f), g), m), o), p), q) y r) en rangos esperados, riesgos técnicos, homogeneidad/estabilidad, análisis estadístico, trazabilidad y evaluación del desempeño |
| 3.5 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Integrar los puntos i), n), s) y t) en controles de integridad de resultados, formatos de reporte, devoluciones al participante y confidencialidad/publicidad |
| 3.6 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Marcar explícitamente exclusiones o adaptaciones necesarias para esta ronda simple: capacidad máxima de 8 equipos no aplica, elementos multi-participante no aplican, consenso entre participantes no aplica para n=1 |

**Resultado Fase 3 ejecutada (2026-04-10):**

| Componente | Implementación realizada | Efecto sobre el formato |
|---|---|---|
| Roles y responsabilidades | Se añadió matriz RACI para coordinación EA, soporte técnico, soporte estadístico, logística y participante | El plan ahora distribuye aprobaciones, ejecución y soporte por actividad crítica |
| Participación y prerrequisitos | Se integraron criterios de elegibilidad, información previa requerida y condiciones de ingreso del participante | El formato dejó explícitos los requisitos previos y la información mínima de control |
| Recursos, ítem PT e incidentes | Se incorporaron proveedores/servicios, controles de producción-custodia del ítem PT y tabla de respuesta ante incidentes | La ronda quedó alineada con manejo seguro del manifold, CRM y contingencias |
| Cronograma y reporte | Se añadieron actividades esperadas del participante, paquete de información pre-ronda y ventana de reporte | El documento pasó de cronograma básico a secuencia operativa con entregables |
| Riesgos, trazabilidad y exclusiones | Se incorporaron rangos de trabajo, matriz de riesgos técnicos, trazabilidad metrológica, integridad de resultados y exclusiones explícitas para n=1 | Se evita trasladar al formato lógica multi-participante o de consenso no aplicable |

### Fase 4: Cierre documental y validación interna

**Objetivo:** dejar el formato consistente con la documentación ya creada del piloto y señalar con precisión los campos que aún requieren dato real del laboratorio.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Verificar | Revisar coherencia con I-PSEA-07, I-PSEA-09, P-PSEA-10 y la estructura confirmada de la ronda simple |
| 4.2 | docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md | Modificar | Mantener placeholders solo para datos no inferibles: códigos internos, setpoints aprobados, certificados CRM, responsables nominales, firmas y σ_pt final por analito |
| 4.3 | logs/CURRENT_SESSION.md | Modificar | Actualizar el estado de sesión si se ejecuta el ajuste del formato en esta misma línea de trabajo |
| 4.4 | logs/history/ | Crear | Registrar hallazgo al cerrar el ajuste, documentando decisiones de adaptación desde la planificación general al formato de ronda simple |

**Resultado Fase 4 ejecutada (2026-04-10):**

| Verificación / ajuste | Implementación realizada | Resultado |
|---|---|---|
| Coherencia documental | Se verificó alineación de cronograma T-14, custodia del ítem PT in situ y criterio n=1 contra `I-PSEA-07`, `I-PSEA-09` y `P-PSEA-10` | El formato quedó consistente con la línea documental del piloto y con la distinción ítem PT vs materiales del participante |
| Depuración de placeholders | Se mantuvieron como pendientes únicamente campos no inferibles (código de ronda, setpoints, CRM/lotes, `x_pt`, `u(x_pt)`, `σ_pt`, responsables, firmas) | Se eliminó el placeholder de sede y se fijó el criterio de reporte con base en la comunicación oficial |
| Cronograma de reporte | Se definió ventana de reporte de resultados de 15 días posteriores al fin de mediciones (límite 2026-05-08) | Se deja el formato listo para diligenciamiento y aprobación pre-ronda |

---

## Supuestos de trabajo

- La ronda simple continúa definida como una jornada de CO y SO₂ con un único participante: SIATA.
- Para esta ronda no aplica valor asignado por consenso entre participantes; el plan debe reflejar valor de referencia trazable a CRM y σ_pt prescrito.
- El documento `Planificación antes del inicio del ensayo de aptitud.docx.md` se toma como insumo de contenido, no como plantilla literal; por tanto, su texto debe reformularse y especializarse.
- Los puntos del documento fuente que describen operación general del esquema se incorporan solo en la medida en que afecten la ejecución de la ronda simple.

---

## Riesgos y focos de revisión

- Riesgo de arrastrar al formato de ronda simple criterios pensados para esquemas con múltiples participantes o evaluación por consenso.
- Riesgo de inconsistencia entre F-PSEA-06 y los instructivos ya desarrollados en Sprint 2, especialmente sobre comunicaciones, manejo de ítems PT y modelo estadístico para n bajo.
- Riesgo de dejar el formato demasiado narrativo y poco usable como registro operativo aprobable.
- Riesgo de no distinguir entre condiciones generales del programa EA y datos específicos exigibles para esta ronda piloto.

---

## Log de Ejecución

- [x] Fase 1 iniciada
- [x] Fase 1 completada
- [x] Fase 2 iniciada
- [x] Fase 2 completada
- [x] Fase 3 iniciada
- [x] Fase 3 completada
- [x] Fase 4 iniciada
- [x] Fase 4 completada
