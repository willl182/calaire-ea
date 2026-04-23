# Evolución del Proyecto: calaire-ea

**Fecha de corte**: 2026-04-23  
**Periodo cubierto**: 2026-02-03 → 2026-04-22  
**Repositorio**: `/home/w182/w421/calaire-ea`

---

## Resumen ejecutivo

`calaire-ea` es el repositorio central del proyecto CALAIRE-EA (Ensayo de Aptitud de Calidad del Aire). Funciona como grafo de conocimiento (Logseq), repositorio documental (SGC ISO 17043:2023), y hub de planificación del programa de ensayos de aptitud para contaminantes gaseosos atmosféricos.

---

## Línea de tiempo de hitos

### Fase 1 — Fundación del repositorio (Feb 2026)

| Fecha | Hito | Detalle |
|-------|------|---------|
| 2026-02-03 | Setup inicial | Sistema híbrido Logseq + Git. Arquitectura MOC implementada (CALAIRE-EA → Prueba Piloto, CALAIRE-APP, QMS, Laboratorios, Equipo). |
| 2026-02-03 | Publicación GitHub | Repositorio remoto configurado (`git@github.com:willl182/calaire-ea.git`), rama `main` publicada. |
| 2026-02-03 | Estandarización journals | 5 categorías estándar (Prueba Piloto, Gestión Administrativa, Desarrollo Técnico, SGC/Calidad, Infraestructura). Template `journal-daily` creado. |
| 2026-02-03 | Sistema de clasificación correos | `docs/tags_project.csv` con 10 grupos, 29 etiquetas y columna `Categoria_Journal` para mapeo con el grafo. |
| 2026-02-03 | Memoria 2025 | `pages/memoria_2025.md` — informe anual estructurado con cambios de equipo y planificación piloto. |
| 2026-02-03 | AGENTS.md | Guía de desarrollo de contenido: reformulación técnica (no copiar literal), estándares de calidad documental. |

### Fase 2 — Documentación SGC (Feb–Abr 2026)

| Fecha | Hito | Detalle |
|-------|------|---------|
| 2026-02-08 | Protocolo General EA | `P-PSEA-01` — backbone documental del SGC alineado a ISO 17043:2023. |
| 2026-04-07 | Framework SGC completo | Estructura jerárquica de 4 niveles: Manual, Procedimientos, Instructivos, Formatos. |
| 2026-04-07 | Plan de rondas piloto | Arquitectura de documentación para ronda simple (n=1, SIATA) y ronda compleja (n≥2). |
| 2026-04-08 | Sprint 2 completado | 3 skeletons creados: I-PSEA-09 (Instrucciones a Participantes), I-PSEA-10 (Homogeneidad/Estabilidad), P-PSEA-10 (Manejo de Ítems PT). |
| 2026-04-08 | Segregación operativa/gestión | Documentación separada en categorías Operacional (ejecución técnica) y Management (gobernanza/SGC). |

### Fase 3 — Formato F-PSEA-06 Ronda Simple (Abr 2026)

| Fecha | Hito | Detalle |
|-------|------|---------|
| 2026-04-10 | Fase 1: Criterios de adaptación | Separación de contenido aplicable, adaptable y no trasladable desde planificación general a ronda simple n=1. |
| 2026-04-10 | Fase 2: Formato operativo | F-PSEA-06 dejó de ser placeholder y pasó a formato de control pre-ronda con secciones explícitas. |
| 2026-04-10 | Fase 3: Aterrizaje operativo | Planificación general traducida a controles operativos de ronda simple (eligibilidad, prerrequisitos, roles, custodia, cronograma, trazabilidad). |
| 2026-04-10 | Fase 4: Depuración placeholders | Solo datos no inferibles quedaron como `[POR DEFINIR]` (código de ronda, CRM, firmas, valores aprobados). |
| 2026-04-10 | Decisión σ_pt | Adoptado enfoque post-ronda (fitness-for-purpose), confirmado con protocolo JRC-ERLAP. σ_pt = a · x_pt + b. |

### Fase 4 — Auditorías cruzadas del F-PSEA-06 (Abr 2026)

| Fecha | Hito | Detalle |
|-------|------|---------|
| 2026-04-10 | Auditoría de completitud | 41 verificaciones en 5 dimensiones (A–E). Dictamen: operativamente utilizable pero `no_aprobable` formalmente. |
| 2026-04-10 | Auditoría de placeholders | Evaluación de datos inferibles vs. no inferibles. Inventario completo de 16+ campos `[POR DEFINIR]`. |
| 2026-04-10 | Auditoría de coherencia interdocumental | Dictamen `no_aprobable` con 3 hallazgos críticos consolidados (σ_pt interdocumental, hito T-3, I-PSEA-07 skeleton). |
| 2026-04-10 | Línea base pre-corrección | 0 Blocking, 1 Required (σ_pt), 1 Suggestion (checklist pre-ronda). |
| 2026-04-10 | Backlog de correcciones | C4-01 a C4-04 definidos con fechas objetivo para habilitar aprobación formal. |

### Fase 5 — Acceso operativo e inducción (Abr 2026)

| Fecha | Hito | Detalle |
|-------|------|---------|
| 2026-04-20 | Inducción SST | Respuestas del curso SST persona natural consolidadas. Flujo documentado: UNVirtual → certificado → permiso de ingreso UNAL. |

### Fase 6 — Portal web calaire-app (Abr 2026)

| Fecha | Hito | Detalle |
|-------|------|---------|
| 2026-04-21 | Plan app web rondas | Plan de 7 etapas para portal Next.js 16 + WorkOS + Supabase. |
| 2026-04-21 | Todas las etapas (1–6) completadas | Setup, dashboard coordinador, participantes, formulario reactivo, resultados + CSV, hardening (validaciones, error handling). |
| 2026-04-21 | Integración con pt_app | Plan para exportar CSV compatible con el contrato de `summary_n13.csv`. |
| 2026-04-21 | Rediseño "Institutional Gold" | Paleta dorada `#FDB913` unificando identidad visual entre calaire-app y pt_app. |

---

## Estado del corpus documental

### Documentos creados y en estado operativo

| Código | Título | Estado |
|--------|--------|--------|
| P-PSEA-01 | Protocolo General EA | Operativo |
| P-PSEA-09 | Procedimiento de Planificación Ronda EA | Operativo |
| P-PSEA-10 | Procedimiento de Manejo de Ítems PT | Skeleton completo |
| P-PSEA-20 | Comunicación PT | Skeleton |
| P-PSEA-22 | Reportes PT | Skeleton |
| I-PSEA-07 | Diseño Estadístico | Skeleton con criterios n=1 definidos |
| I-PSEA-09 | Instrucciones a Participantes | Skeleton, 3 brechas identificadas |
| I-PSEA-10 | Homogeneidad y Estabilidad | Skeleton |
| F-PSEA-05 | Confirmación de Participación | Formato |
| F-PSEA-05A | Hoja de Registro del Participante | Formato (versiones XLSX/MD) |
| F-PSEA-06 | Plan de Ronda EA | Draft operativo — ronda simple completado, auditorías ejecutadas |
| F-PSEA-07 a F-PSEA-23 | Formatos operativos | Skeletons creados |

### Documentos de referencia/apoyo

- Comunicaciones a participantes (SIATA v3, Politécnico v1, GICA v3)
- Informes EA previos (3 informes con scores z, zeta, En)
- Cronogramas detallados F-PSEA-01, F-PSEA-02
- Referencia: erlap_pt_scheme.pdf, uba_pt_scheme.pdf

---

## Brechas abiertas

1. **σ_pt interdocumental**: Alineación pendiente entre I-PSEA-07, I-PSEA-09 y F-PSEA-06
2. **Hito T-3 en cronograma**: Falta en F-PSEA-06, requerido por I-PSEA-09
3. **I-PSEA-07 skeleton**: Secciones críticas incompletas para sustento auditable
4. **Aprobación formal F-PSEA-06**: Bloqueada hasta cierre de backlog C4-01 a C4-04
5. **Etapa 7 calaire-app**: Smoke test end-to-end + deploy Vercel pendiente
