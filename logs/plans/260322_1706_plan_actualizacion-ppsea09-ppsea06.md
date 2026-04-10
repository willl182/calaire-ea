# Plan: Actualización P-PSEA-09 y p-psea-06

**Created**: 2026-03-22 17:06
**Updated**: 2026-03-22 17:16
**Status**: completed
**Slug**: actualizacion-ppsea09-ppsea06

## Objetivo

Actualizar los procedimientos P-PSEA-09 (planificación EA) y p-psea-06 (diseño estadístico) para alinearlos completamente con ISO/IEC 17043:2023 e ISO 13528:2022, integrando las recomendaciones del análisis cruzado de 10 documentos en `docs/ppsea09/` (normas ISO, análisis de IA de claude/gpt/gemini). Las brechas principales son: determinación de σ_pt, selección de estadísticos de desempeño, gestión de riesgos, autorización de personal, y manejo de participantes <12.

## Fases

### Fase 1: Actualización de P-PSEA-09 (Planificación EA)

| # | Sección | Acción | Notas |
|---|---------|--------|-------|
| 1.1 | a) Personal | Agregar autorización explícita ISO 17043 §6.2.6 | 5 funciones que requieren autorización formal: planificar esquemas, evaluar H&E/valores/incertidumbres, evaluar desempeño, emitir opiniones, revisar/autorizar informes |
| 1.2 | d) Participantes | Fortalecer guía numérica | Criterio u(x_pt) ≤ 0.3σ_pt (n≥17 si s*≈σ_pt); contingencia n<12: valor asignado externo, σ_pt prescriptivo, usar z'/ζ/En |
| 1.3 | f) Rango valores | Clarificar | Mantener rangos generales; concentraciones específicas en comunicación detallada |
| 1.4 | g) Fuentes error | Agregar gestión riesgos ISO 17043 §7.2.1.2 | Evaluación de riesgos para cambios significativos en diseño |
| 1.5 | h) Requisitos técnicos | Vincular equipos/certificados | Hojas de vida, certificados vigentes, aplicativo como evidencia H&E |
| 1.6 | o) Análisis estadístico | Agregar lógica de selección | Jerarquía σ_pt (5 métodos ISO 13528 §8), jerarquía valor asignado (5 métodos), árbol decisión estadístico desempeño |
| 1.7 | p) Trazabilidad | Agregar presupuesto incertidumbre | u(x_pt,def) = √[u(x_pt)² + u_hom² + u_stab²] |
| 1.8 | r) Criterios desempeño | Expandir | Tabla interpretación z, z', ζ, En; criterio selección por tipo valor asignado |
| 1.9 | t) Confidencialidad | Vincular política lab | Citar política SGC, retención documental, incluir en comunicación participantes |
| 1.10 | Nueva | Gestión riesgos cambios diseño | Requisito ISO 17043:2023 §7.2.1.2 |
| 1.11 | Todos | Resolver comentarios internos | Integrar `--- comentario ---` como texto normativo o eliminar |

### Fase 2: Actualización de p-psea-06 (Diseño Estadístico)

| # | Sección | Acción | Notas |
|---|---------|--------|-------|
| 2.1 | 2.2.2 | Fortalecer guía n<12 | Valor asignado externo obligatorio; σ_pt prescriptivo; robustas no recomendadas n<20 |
| 2.2 | 2.2.4 | Jerarquía valor asignado | Ranking 5 métodos: formulación > MRC > lab referencia > consenso expertos > consenso participantes |
| 2.3 | 2.2.8 | Expandir σ_pt | 6 métodos ISO 13528 §8 con ranking; prescriptivo tiene prelación |
| 2.4 | 2.2.9 | Completar incertidumbre | Detallar obtención u_hom (=s_s) y u_stab; ejemplo de cálculo integrado |
| 2.5 | 2.2.6 | Manejo fallos Algoritmo A | Fallback: mediana + MADe o Q_n si no converge |
| 2.6 | 2.2.12 | Lógica selección estadístico | Árbol decisión z/z'/ζ/En basado en u(x_pt) ≤ 0.3σ_pt |
| 2.7 | Nueva | Detección multimodalidad | Clusters en resultados, diagnósticos gráficos (kernel density, Youden) |
| 2.8 | Nueva | Participantes excluidos | Resultados tardíos, errores, no-respuesta; tasa exclusión y mínimo viable |

### Fase 3: Verificación cruzada

| # | Archivo | Acción | Notas |
|---|---------|--------|-------|
| 3.1 | P-PSEA-09 | Verificar literales a)-u) vs ISO 17043 §7.2.1.3 | Cobertura completa |
| 3.2 | p-psea-06 | Verificar métodos vs ISO 13528:2022 | Cobertura estadística completa |
| 3.3 | Ambos | Coherencia cruzada | Sin contradicciones entre procedimientos |
| 3.4 | P-PSEA-09 | Comentarios internos resueltos | Todos los `--- comentario ---` procesados |
| 3.5 | Ambos | Referencias cruzadas correctas | P-PSEA-02..08, F-PSEA-01, I-PSEA-01, DG-PSEA-01 |

## Fuentes de referencia

- `docs/ppsea09/iso 13528_2022.md` — Norma estadística base
- `docs/ppsea09/iso 17043_2023.md` — Requisitos generales proveedor EA
- `docs/ppsea09/claude_planstat.md` — Jerarquía σ_pt, estadísticos para n<5
- `docs/ppsea09/gem_planstat.md` — Análisis comprensivo, 6 métodos σ_pt
- `docs/ppsea09/claude_planea.md` — Requisitos específicos calidad del aire
- `docs/ppsea09/gem_planea.md` — Requisitos detallados 17043:2023
- `docs/ppsea09/gpt_planstat.md` — Consideraciones participantes limitados
- `docs/ppsea09/gpt_planea.md` — Guía planificación completa
- `docs/ppsea09/z_planea.md` — Marco de planificación conciso

## Log de Ejecución

- [x] Fase 1 iniciada
- [x] Fase 1 completada
- [x] Fase 2 iniciada
- [x] Fase 2 completada
- [x] Fase 3 iniciada
- [x] Fase 3 completada

## Resultado de implementación

- Se generó `docs/ppsea09/mm25_ppsea09.md` con actualización integral de planificación a)-u) (ISO 17043:2023 §7.2.1.3), gestión de riesgos (§7.2.1.2), autorización de personal (§6.2.6), confidencialidad (§4.2), no subcontratación (§6.4.1) y lógica estadística referenciada a P-PSEA-06.
- Se generó `docs/ppsea09/mm25_ppsea06.md` con jerarquía de valor asignado (5 niveles), jerarquía de σ_pt (6 niveles), reglas explícitas para p < 12, árbol de decisión z/z'/ζ/En, incertidumbre definitiva integrada, homogeneidad/estabilidad con criterios numéricos, fallback del Algoritmo A, detección de multimodalidad y gestión de participantes excluidos.
- Se verificó coherencia cruzada entre ambos artefactos y alineación de referencias a P-PSEA-02..08, F-PSEA-01, I-PSEA-01 y DG-PSEA-01.
