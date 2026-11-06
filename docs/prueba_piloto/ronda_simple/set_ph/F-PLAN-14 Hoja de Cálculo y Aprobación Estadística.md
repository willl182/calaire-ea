# F-PLAN-14 — Hoja de Cálculo y Aprobación Estadística

| Campo | Valor |
|-------|-------|
| **Código** | F-PLAN-14 |
| **Nivel** | 4 |
| **Estado** | Borrador |
| **Prioridad** | 🔴 Crítica |
| **Responsable** | Laboratorio de Calidad de Agua — Universidad Nacional |
| **Fecha de Elaboración** | 2026-07-10 |
| **Revisión** | 0 |

---

## I. Objetivo

Documentar el procedimiento estadístico completo para la evaluación de los resultados de los participantes en la ronda de ensayos de aptitud, incluyendo el cálculo del valor asignado, la estimación de la incertidumbre de la evaluación, el cálculo de los Z-scores y la clasificación del desempeño de cada participante. Este documento constituye la evidencia objetiva del cumplimiento de los requisitos de evaluación establecidos en la **ISO 13528:2022**, Secciones 9.2, 9.3 y Anexo A, y la **ISO/IEC 17025:2017**, Cláusula 7.8.

---

## II. Alcance

El presente documento aplica al procesamiento estadístico de los resultados validados provenientes de la revisión de datos (F-PLAN-13) para la Ronda RPT-AGUA-2026-01, abarcando todos los parámetros evaluados y todos los participantes con datos aceptados.

---

## III. Referencias Normativas

| Norma | Sección | Aplicación |
|-------|---------|------------|
| ISO 13528:2022 | Secciones 9.2, 9.3 y Anexo A | Métodos estadísticos para evaluación de resultados |
| ISO/IEC 17025:2017 | Cláusula 7.8 — Informes de resultados | Contenido del informe de evaluación |
| ISO 3534-1:2023 | — | Terminología estadística |
| ISO 17043:2023 | Sección 7 — Evaluación | Requisitos para la evaluación del desempeño |

---

## IV. Información General

| Campo | Valor |
|-------|-------|
| **Código de la ronda** | RPT-AGUA-2026-01 |
| **Fecha del análisis estadístico** | ____/____/________ |
| **Responsable del análisis** | _________________________________________________ |
| **Software utilizado** | _________________________________________________ |
| **Versión del software** | _________________________________________________ |
| **Total de participantes con datos aceptados** | __________ |

---

## V. Método de Asignación del Valor de Referencia

### A. Procedimiento de Asignación

| Paso | Actividad | Descripción |
|------|-----------|-------------|
| 1 | Compilación de datos | Recopilar todos los resultados aceptados tras la revisión de datos |
| 2 | Verificación de normalidad | Aplicar prueba de Shapiro-Wilk o Kolmogorov-Smirnov (α = 0.05) |
| 3 | Cálculo del valor asignado | Media aritmética de los resultados participantes (si normal) o mediana (si no normal) |
| 4 | Estimación de σₚ | Desviación estándar de los resultados participantes |
| 5 | Estimación de σᵣ | Incertidumbre del valor asignado (error estándar de la media) |
| 6 | Cálculo de σₚₜ | σₚₜ = √(σₚ² + σᵣ²) |
| 7 | Verificación de σₚ | Comparar σₚ con el σₚ esperado del método |

---

## VI. Resultados Estadísticos por Parámetro

### A. pH

#### 1. Datos Compilados

| Código Lab | Resultado | Observaciones |
|------------|-----------|---------------|
| PH-001 | _________ | |
| PH-002 | _________ | |
| PH-003 | _________ | |
| PH-004 | _________ | |
| PH-005 | _________ | |
| PH-006 | _________ | |
| PH-007 | _________ | |
| PH-008 | _________ | |
| PH-009 | _________ | |
| PH-010 | _________ | |

#### 2. Estadísticos Descriptivos

| Estadístico | Valor |
|-------------|-------|
| N (número de participantes) | __________ |
| Media (x̄) | __________ |
| Mediana | __________ |
| Desviación estándar (s) | __________ |
| Coeficiente de variación (CV) | __________ % |
| Valor mínimo | __________ |
| Valor máximo | __________ |
| Rango | __________ |

#### 3. Prueba de Normalidad

| Prueba | Estadístico | Valor p | ¿Normal? (α = 0.05) |
|--------|-------------|---------|----------------------|
| Shapiro-Wilk | _________________ | _________________ | ☐ Sí ☐ No |
| Kolmogorov-Smirnov | _________________ | _________________ | ☐ Sí ☐ No |

#### 4. Valor Asignado e Incertidumbre

| Parámetro | Valor |
|-----------|-------|
| **Valor asignado (x₀)** | __________ pH |
| **σₚ (desviación estándar participante)** | __________ pH |
| **σᵣ (incertidumbre del valor asignado)** | __________ pH |
| **σₚₜ (desviación estándar total)** | __________ pH |
| **σₚ esperado del método** | __________ pH |
| **¿σₚ dentro del rango esperado?** | ☐ Sí ☐ No |

#### 5. Cálculo de Z-scores

| Código Lab | Resultado (xᵢ) | xᵢ − x₀ | Z-score = (xᵢ − x₀) / σₚₜ | |Z| | Clasificación |
|------------|-----------------|----------|---------------------------|-----|----------------|
| PH-001 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-002 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-003 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-004 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-005 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-006 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-007 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-008 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-009 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-010 | _________ | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |

---

### B. Conductividad (μS/cm)

#### 1. Estadísticos Descriptivos

| Estadístico | Valor |
|-------------|-------|
| N | __________ |
| Media (x̄) | __________ |
| Mediana | __________ |
| Desviación estándar (s) | __________ |
| CV | __________ % |
| Valor mínimo | __________ |
| Valor máximo | __________ |

#### 2. Valor Asignado e Incertidumbre

| Parámetro | Valor |
|-----------|-------|
| **Valor asignado (x₀)** | __________ μS/cm |
| **σₚ** | __________ μS/cm |
| **σᵣ** | __________ μS/cm |
| **σₚₜ** | __________ μS/cm |

#### 3. Z-scores

| Código Lab | Resultado | Z-score | |Z| | Clasificación |
|------------|-----------|---------|-----|----------------|
| PH-001 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-002 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-003 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-004 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-005 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-006 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-007 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-008 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-009 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-010 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |

---

### C. Alcalinidad (mg/L CaCO₃)

#### 1. Estadísticos Descriptivos

| Estadístico | Valor |
|-------------|-------|
| N | __________ |
| Media (x̄) | __________ |
| Mediana | __________ |
| Desviación estándar (s) | __________ |
| CV | __________ % |
| Valor mínimo | __________ |
| Valor máximo | __________ |

#### 2. Valor Asignado e Incertidumbre

| Parámetro | Valor |
|-----------|-------|
| **Valor asignado (x₀)** | __________ mg/L CaCO₃ |
| **σₚ** | __________ mg/L CaCO₃ |
| **σᵣ** | __________ mg/L CaCO₃ |
| **σₚₜ** | __________ mg/L CaCO₃ |

#### 3. Z-scores

| Código Lab | Resultado | Z-score | |Z| | Clasificación |
|------------|-----------|---------|-----|----------------|
| PH-001 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-002 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-003 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-004 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-005 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |

---

### D. Dureza (mg/L CaCO₃)

#### 1. Estadísticos Descriptivos

| Estadístico | Valor |
|-------------|-------|
| N | __________ |
| Media (x̄) | __________ |
| Mediana | __________ |
| Desviación estándar (s) | __________ |
| CV | __________ % |
| Valor mínimo | __________ |
| Valor máximo | __________ |

#### 2. Valor Asignado e Incertidumbre

| Parámetro | Valor |
|-----------|-------|
| **Valor asignado (x₀)** | __________ mg/L CaCO₃ |
| **σₚ** | __________ mg/L CaCO₃ |
| **σᵣ** | __________ mg/L CaCO₃ |
| **σₚₜ** | __________ mg/L CaCO₃ |

#### 3. Z-scores

| Código Lab | Resultado | Z-score | |Z| | Clasificación |
|------------|-----------|---------|-----|----------------|
| PH-001 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-002 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-003 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-004 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-005 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |

---

### E. Cloruros (mg/L)

#### 1. Estadísticos Descriptivos

| Estadístico | Valor |
|-------------|-------|
| N | __________ |
| Media (x̄) | __________ |
| Mediana | __________ |
| Desviación estándar (s) | __________ |
| CV | __________ % |
| Valor mínimo | __________ |
| Valor máximo | __________ |

#### 2. Valor Asignado e Incertidumbre

| Parámetro | Valor |
|-----------|-------|
| **Valor asignado (x₀)** | __________ mg/L |
| **σₚ** | __________ mg/L |
| **σᵣ** | __________ mg/L |
| **σₚₜ** | __________ mg/L |

#### 3. Z-scores

| Código Lab | Resultado | Z-score | |Z| | Clasificación |
|------------|-----------|---------|-----|----------------|
| PH-001 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-002 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-003 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-004 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-005 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |

---

### F. Sulfatos (mg/L)

#### 1. Estadísticos Descriptivos

| Estadístico | Valor |
|-------------|-------|
| N | __________ |
| Media (x̄) | __________ |
| Mediana | __________ |
| Desviación estándar (s) | __________ |
| CV | __________ % |
| Valor mínimo | __________ |
| Valor máximo | __________ |

#### 2. Valor Asignado e Incertidumbre

| Parámetro | Valor |
|-----------|-------|
| **Valor asignado (x₀)** | __________ mg/L |
| **σₚ** | __________ mg/L |
| **σᵣ** | __________ mg/L |
| **σₚₜ** | __________ mg/L |

#### 3. Z-scores

| Código Lab | Resultado | Z-score | |Z| | Clasificación |
|------------|-----------|---------|-----|----------------|
| PH-001 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-002 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-003 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-004 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-005 | _________ | _________ | _________ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |

---

## VII. Criterios de Desempeño

| Categoría | Rango de Z-score | Color | Interpretación |
|-----------|------------------|-------|----------------|
| **Satisfactorio** | \|Z\| ≤ 2.0 | 🟢 Verde | Resultado dentro del rango aceptable |
| **Cuestionable** | 2.0 < \|Z\| < 3.0 | 🟡 Amarillo | Requiere investigación; posible mejora necesaria |
| **Insatisfactorio** | \|Z\| ≥ 3.0 | 🔴 Rojo | Acción correctiva obligatoria |

---

## VIII. Resumen Consolidado de Desempeño

### A. Por Participante

| Código Lab | pH | Conductividad | Alcalinidad | Dureza | Cloruros | Sulfatos | Calificación Global |
|------------|-----|---------------|-------------|--------|----------|----------|---------------------|
| PH-001 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-002 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-003 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-004 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-005 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-006 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-007 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-008 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-009 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |
| PH-010 | _____ | _____ | _____ | _____ | _____ | _____ | ☐ Satisfactorio ☐ Cuestionable ☐ Insatisfactorio |

### B. Por Parámetro — Distribución de Desempeño

| Parámetro | Satisfactorios (|Z| ≤ 2) | Cuestionables (2 < \|Z\| < 3) | Insatisfactorios (|Z| ≥ 3) | Total |
|-----------|--------------------------|-------------------------------|-----------------------------|-------|
| pH | __________ | __________ | __________ | __________ |
| Conductividad | __________ | __________ | __________ | __________ |
| Alcalinidad | __________ | __________ | __________ | __________ |
| Dureza | __________ | __________ | __________ | __________ |
| Cloruros | __________ | __________ | __________ | __________ |
| Sulfatos | __________ | __________ | __________ | __________ |

### C. Estadísticas Globales de la Ronda

| Métrica | Valor |
|---------|-------|
| **Total de evaluaciones (participantes × parámetros)** | __________ |
| **Satisfactorios** | __________ (__________ %) |
| **Cuestionables** | __________ (__________ %) |
| **Insatisfactorios** | __________ (__________ %) |
| **Promedio de \|Z\|** | __________ |
| **Mediana de \|Z\|** | __________ |

---

## IX. Análisis de Resultados Insatisfactorios

| Código Lab | Parámetro | Z-score | Resultado | Valor Asignado | Desviación (%) | Posible Causa | Acción Correctiva Recomendada |
|------------|-----------|---------|-----------|----------------|----------------|---------------|--------------------------------|
| _________________ | _________________ | _________ | _________ | _________ | _________ % | _________________ | _________________ |
| _________________ | _________________ | _________ | _________ | _________ | _________ % | _________________ | _________________ |
| _________________ | _________________ | _________ | _________ | _________ | _________ % | _________________ | _________________ |

---

## X. Aprobación Estadística

### A. Revisión Metodológica

| Verificación | ¿Cumple? | Observaciones |
|--------------|----------|---------------|
| Método de asignación del valor conforme a ISO 13528 | ☐ Sí ☐ No | |
| σₚ consistente con el σₚ esperado del método | ☐ Sí ☐ No | |
| Cálculo de Z-scores correcto | ☐ Sí ☐ No | |
| Clasificación de desempeño conforme a criterios establecidos | ☐ Sí ☐ No | |
| Resumen consolidado completo | ☐ Sí ☐ No | |

### B. Firma de Aprobación

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Estadístico responsable | _________________ | _________________ | ____/____/________ |
| Revisor independiente | _________________ | _________________ | ____/____/________ |
| Coordinador del Programa de PT | _________________ | _________________ | ____/____/________ |
| Director del Laboratorio | _________________ | _________________ | ____/____/________ |

---

## XI. Historial de Revisiones

| Revisión | Fecha | Cambios | Autor |
|----------|-------|---------|-------|
| 0 | 2026-07-10 | Creación inicial del documento | _________________ |

---

## XII. Checklist de Verificación

- [ ] Datos compilados de la revisión de datos (F-PLAN-13)
- [ ] Prueba de normalidad aplicada
- [ ] Valor asignado calculado correctamente
- [ ] σₚ, σᵣ y σₚₜ estimados
- [ ] Z-scores calculados para cada participante y parámetro
- [ ] Clasificación de desempeño asignada
- [ ] Resumen consolidado completado
- [ ] Análisis de resultados insatisfactorios realizado
- [ ] Aprobación metodológica verificada
- [ ] Firmas de aprobación obtenidas

---

*Documento generado conforme a ISO 13528:2022, Secciones 9.2, 9.3 y Anexo A — Laboratorio de Calidad de Agua, Universidad Nacional.*
