# Plan de Implementación No-Codebase - Revisión Aplicativo Estadístico (Codex53)

**Fecha:** 2026-03-06  
**Estado:** propuesto  
**Documento fuente único:** `docs/ajustes_app/Revisión aplicativo estadístico.pdf`  
**Restricción explícita:** este plan no incluye revisión ni modificación de codebase.

---

## 1. Objetivo

Definir una ruta de implementación técnica, verificable y auditable para resolver los hallazgos del informe de revisión estadística, dejando listos los insumos funcionales y de validación previos a cualquier intervención de software.

## 2. Alcance y exclusiones

### Alcance
- Normalización de reglas estadísticas (homogeneidad, MADe, nIQR, Algoritmo A).
- Estandarización de entradas/salidas para validación externa en Excel.
- Diseño de protocolo de validación cruzada con evidencia trazable.
- Cierre documental de hallazgos con criterios de aceptación.

### Exclusiones
- No se inspecciona arquitectura, scripts, módulos o repositorio del aplicativo.
- No se implementan cambios en UI, backend ni pipelines.
- No se ejecutan pruebas de software; solo validación metodológica/documental.

## 3. Hallazgos consolidados del informe

1. La formulación de homogeneidad (B.10, ISO 13528:2022) requiere control explícito del caso con radicando negativo, definiendo resultado operativo en cero.
2. El cálculo de MADe debe alimentarse con datos de participantes y no con datos de homogeneidad.
3. La regla de selección metodológica requiere umbral formal: con `n >= 12` se debe aplicar Algoritmo A.
4. Existe ambigüedad en la serie utilizada para cálculos (Datos 1 vs Datos 2), lo que afecta reproducibilidad.
5. Se requiere habilitar evidencia de datos para validación del Algoritmo A.
6. El formato de exportación/carga actual dificulta trazabilidad y lectura para verificación externa.

## 4. Plan de implementación por fases

### Fase 1 - Especificación metodológica normativa
**Objetivo:** congelar reglas de cálculo y criterios de uso por método.  
**Actividades:**
- Redactar ficha técnica de B.10 con tratamiento de casos límite.
- Definir fuente de datos válida por estadístico (homogeneidad, estabilidad, participantes).
- Formalizar regla de selección MADe/nIQR/Algoritmo A por tamaño muestral.

**Entregables:**
- `docs/ajustes_app/codex53_especificacion_metodologica.md`
- `docs/ajustes_app/codex53_reglas_decision_estadistica.md`

**Criterio de aceptación:** reglas sin ambigüedad y trazadas a ISO 13528:2022.

### Fase 2 - Estructura de datos y trazabilidad
**Objetivo:** eliminar confusión entre series y orígenes de datos.  
**Actividades:**
- Diseñar diccionario de datos con campos mínimos de auditoría.
- Establecer convención de identificación de serie (`datos_1`, `datos_2`, etc.).
- Crear matriz origen-dato -> cálculo -> salida.

**Entregables:**
- `docs/ajustes_app/codex53_diccionario_datos.md`
- `docs/ajustes_app/codex53_matriz_trazabilidad.md`

**Criterio de aceptación:** cada resultado estadístico se puede reconstruir desde su dataset de origen.

### Fase 3 - Protocolo de validación cruzada (App vs Excel)
**Objetivo:** establecer verificación reproducible sin tocar código.  
**Actividades:**
- Diseñar batería de casos: radicando negativo, `n=11`, `n=12`, datos extremos, series alternas.
- Definir formato de evidencias: entrada, cálculo intermedio, resultado esperado, diferencia.
- Establecer tolerancias y criterio binario de conformidad.

**Entregables:**
- `docs/ajustes_app/codex53_protocolo_validacion_cruzada.md`
- `docs/ajustes_app/codex53_matriz_casos_prueba.md`

**Criterio de aceptación:** cobertura completa de los hallazgos críticos del informe.

### Fase 4 - Estandarización de interfaces de datos
**Objetivo:** mejorar legibilidad y auditabilidad de carga/exportación.  
**Actividades:**
- Proponer plantillas CSV separadas por contexto: homogeneidad, estabilidad, participantes.
- Definir tabla de previsualización para identificación clara de variable, corrida y serie.
- Documentar formato de exportación para revisión de tercero independiente.

**Entregables:**
- `docs/ajustes_app/codex53_plantillas_datos_csv.md`
- `docs/ajustes_app/codex53_especificacion_tablas_revision.md`

**Criterio de aceptación:** un revisor externo puede auditar cálculos sin interpretación adicional.

### Fase 5 - Cierre técnico y habilitación de ejecución futura
**Objetivo:** cerrar formalmente hallazgos y habilitar etapa de implementación en software.  
**Actividades:**
- Consolidar checklist de cierre por hallazgo con evidencia asociada.
- Registrar riesgos residuales y precondiciones para pasar a fase codebase.
- Emitir acta de conformidad metodológica.

**Entregables:**
- `docs/ajustes_app/codex53_checklist_cierre_hallazgos.md`
- `docs/ajustes_app/codex53_acta_conformidad_metodologica.md`

**Criterio de aceptación:** hallazgos clasificados en `cerrado` o `pendiente con acción`, con responsable y fecha.

## 5. Cronograma sugerido (15 días hábiles)

- Días 1-3: Fase 1
- Días 4-6: Fase 2
- Días 7-10: Fase 3
- Días 11-13: Fase 4
- Días 14-15: Fase 5

## 6. Roles mínimos para ejecución

- **Líder metodológico:** aprueba reglas estadísticas y criterios ISO.
- **Analista de datos:** estructura plantillas, trazabilidad y matrices de prueba.
- **Revisor externo:** valida reproducibilidad en Excel y cierre de hallazgos.
- **Coordinación de proyecto:** controla tiempos, evidencias y acta final.

## 7. Condición de salida del plan

Este plan se considera completado cuando exista conformidad metodológica documentada para todos los hallazgos del informe y se emita la autorización formal para iniciar una fase posterior de implementación sobre codebase.
