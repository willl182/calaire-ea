# Instrucciones para Actualización de Plantilla Rmd de Informes EA

**Fecha:** 2026-02-08
**Versión:** 1.0
**Propósito:** Este documento proporciona instrucciones detalladas para actualizar la plantilla Rmd que genera los informes de ensayo de aptitud (EA) de CALAIRE, basándose en los hallazgos identificados frente a ISO/IEC 17043:2023, ISO 13528:2022 y las mejores prácticas de JRC (Barbiere) y UBA.

---

## Tabla de Contenidos

1. [Cambio Resumen](#1-cambio-resumen)
2. [Secciones Nuevas a Crear](#2-secciones-nuevas-a-crear)
3. [Modificaciones en Secciones Existenes](#3-modificaciones-en-secciones-existenes)
4. [Actualizaciones en Tablas](#4-actualizaciones-en-tablas)
5. [Ejemplos de Código Rmd](#5-ejemplos-de-código-rmd)
6. [Checklist de Verificación](#6-checklist-de-verificación)

---

## 1. Cambio Resumen

| Categoría | Cambio Requerido | Severidad | Impacto en Conformidad |
|----------|----------------|----------|------------------------|
| Valor Asignado | Añadir política para grupos pequeños (n < 10): usar valor de referencia de CALAIRE, no consenso | Alta | ISO 13528 5.4 |
| $\sigma_{pt}$ | Documentar justificación: fitness for purpose o derivado del grupo | Alta | ISO 13528 8.1.2, ISO 17043 7.2.2.3 |
| Estabilidad/Homogeneidad | Documentar acciones mitigatorias cuando fallan criterios | Alta | ISO 13528 Anexo B, ISO 17043 7.3.2.1 |
| Compatibilidad Metrológica | Añadir conclusiones y acciones cuando |xdiff| > 2$udiff| | Media | ISO 13528 7.8 |
| Scores | Añadir definiciones de z'-score y ζ-score (opcional) | Media | ISO 13528 9.5.1, 9.6.1 |
| Trazabilidad | Documentar cadena de trazabilidad del valor asignado | Media | ISO 17043 7.4.3.2 l |
| Guía de interpretación | Añadir sección de guía para participantes | Media | ISO 17043 7.4.3.2 r |

---

## 2. Secciones Nuevas a Crear

### 2.1. Nueva Sección: 2.3.1. Política de Grupos Pequeños

**Ubicación:** Después de Sección 2.3 "Determinación del Valor Asignado"

**Contenido:**

```markdown
## 2.3.1. Política de Grupos Pequeños

Conforme a los requisitos de ISO 13528:2022 (cláusula 5.4), para rondas con menos de 10 participantes, el **Valor Asignado ($x_{pt}$)** será determinado mediante el **Valor de Referencia** medido por CALAIRE, utilizando sus instrumentos de referencia trazables a patrones nacionales.

Para n ≥ 10 participantes, el **Valor Asignado ($x_{pt}$)** puede determinarse mediante consenso de los participantes utilizando estimadores robustos (ej: Algoritmo A, MADe, nIQR), siempre que la compatibilidad metrológica con el valor de referencia de CALAIRE sea satisfactoria (ver Sección 2.4).

**Justificación:** La estadística robusta pierde confiabilidad con n pequeño debido a la alta incertidumbre del valor estimado. Si un participante tiene sesgo fuerte, este puede arrastrar el valor de consenso, afectando la evaluación de todos los demás participantes.

**Referencia:** ISO 13528:2022, Cláusula 5.4.1-5.4.2
```

---

### 2.2. Nueva Sección: 2.3.2. Criterio de Selección de Score

**Ubicación:** Después de Sección 2.3.1 "Política de Grupos Pequeños"

**Contenido:**

```markdown
## 2.3.2. Criterio de Selección de Score

Para la evaluación del desempeño de los participantes se utiliza el siguiente orden de prioridad:

1. **z-score** (evaluación estándar)
   - Ecuación: $z = \frac{x_i - x_{pt}}{\sigma_{pt}}$
   - Uso: Evaluación principal para todos los casos
   - Criterio: \|z\| ≤ 2.0 (satisfactorio), 2.0 < \|z\| < 3.0 (cuestionable), \|z\| ≥ 3.0 (insatisfactorio)

2. **z'-score** (evaluación ajustada por incertidumbre del valor asignado)
   - Ecuación: $z' = \frac{x_i - x_{pt}}{\sqrt{\sigma_{pt}^2 + u^2(x_{pt})}}$
   - Uso: Cuando $\frac{u(x_{pt})}{\sigma_{pt}} > 0.5$ (incertidumbre del valor asignado es significativa)
   - Criterio: Mismos límites que z-score

3. **ζ-score** (zeta-score, evaluación por incertidumbre reportada)
   - Ecuación: $\zeta = \frac{x_i - x_{pt}}{\sqrt{u^2(x_i) + u^2(x_{pt})}}$
   - Uso: Opcional, cuando los participantes reportan incertidumbres confiables y el proveedor desea evaluar compatibilidad metrológica
   - Criterio: Mismos límites que z-score

**Criterio de Decisión:**
- Si el valor asignado es de referencia (CALAIRE): usar z-score (incertidumbre despreciable)
- Si el valor asignado es de consenso: usar z'-score si $\frac{u(x_{pt})}{\sigma_{pt}} > 0.5$
- Para evaluación alternativa: usar ζ-score si los participantes reportan incertidumbres

**Referencia:** ISO 13528:2022, Cláusulas 9.2.1, 9.5.1, 9.6.1
```

---

### 2.3. Nueva Sección: 2.3.3. Justificación de $\sigma_{pt}$

**Ubicación:** Después de Sección 2.3.2 "Criterio de Selección de Score"

**Contenido:**

```markdown
## 2.3.3. Justificación de $\sigma_{pt}$

El criterio de desempeño $\sigma_{pt}$ (desviación estándar para la evaluación de aptitud) se determina según la siguiente política:

**Opción A: Fitness for Purpose (Requerido por Directivas Regulatorias)**
- Fuente: Directivas regulatorias o metas de calidad para medición de gases contaminantes
- Ejemplo: CO 10-20% de concentración, NO2 15% de concentración, SO2 15% de concentración
- Ventajas:
  - Evaluación consistente entre rondas sucesivas
  - Comparabilidad internacional con JRC y UBA
  - Independiente de la variabilidad del grupo
- Aplicación: Principal, cuando exista directiva regulatoria aplicable

**Opción B: Derivado del Grupo (Estadística Robusta)**
- Fuente: Desviación robusta del grupo ($s^*$ de Algoritmo A, nIQR de Rango Intercuartílico)
- Ecuación: $\sigma_{pt} = s^*$ o $\sigma_{pt} = 0.7413 \times \text{IQR}$
- Ventajas:
  - Refleja la variabilidad real de los participantes
  - Adaptable cuando no exista directiva regulatoria
- Limitaciones:
  - No es estable entre rondas (variabilidad del grupo cambia)
  - Puede ser irrealmente pequeño si los participantes miden igual pero mal
- Aplicación: Alternativo, solo para n ≥ 20 (variabilidad confiable)

**Opción Seleccionada para esta Ronda:** [ESPECIFICAR OPCIÓN A o B]

**Justificación Técnica:** [EXPLICAR POR QUÉ SE SELECCIONÓ ESTA OPCIÓN]

**Referencia:** ISO 13528:2022, Cláusulas 8.1.2, 8.1.3; ISO/IEC 17043:2023, Cláusula 7.4.2.2
```

---

### 2.4. Nueva Sección: 3.3. Gestión de Inestabilidad

**Ubicación:** Después de Sección 3.2 "Tratamiento Estadístico de Datos"

**Contenido:**

```markdown
## 3.3. Gestión de Inestabilidad

Conforme a ISO 13528:2022 (Anexo B), si los ítems de ensayo no cumplen los criterios de estabilidad o homogeneidad, el proveedor debe tomar las siguientes acciones:

### Criterios de Evaluación
- **Homogeneidad:** $s_s \leq 0.3\sigma_{pt}$ (desviación estándar entre ítems de ensayo)
- **Estabilidad:** $|\bar{x}_{\text{final}} - \bar{x}_{\text{inicio}}| \leq c_{\text{estab}}$ (criterio definido según ISO 13528 Anexo B)

### Acciones Requeridas
1. **Expansión de Incertidumbre del Valor Asignado:**
   - Si falla estabilidad, calcular: $s^2_{\text{instab}} = \text{Var}(\bar{x}_{\text{final}} - \bar{x}_{\text{inicio}})$
   - Actualizar incertidumbre: $u'(x_{pt}) = \sqrt{u^2(x_{pt}) + s^2_{\text{instab}}}$
   - Aplicar $u'(x_{pt})$ en cáclculo de z'-score y ζ-score

2. **Documentación en Informe:**
   - Identificar en Anexo B qué contaminantes/niveles fallaron
   - Explicar la acción tomada (expansión de incertidumbre o uso de valor de referencia)
   - Evaluar impacto en resultados de participantes

3. **Evaluación de Continuidad:**
   - Si fallas en estabilidad son sistemáticos (>50% de contaminantes), evaluar continuar con la ronda
   - Si fallas son aislados, proceder con evaluación usando incertidumbre expandida

**Impacto en Participantes:** La expansión de incertidumbre hace más conservador el criterio de evaluación, reduciendo la probabilidad de falsos positivos pero aumentando la probabilidad de falsos negativos.

**Referencia:** ISO 13528:2022, Anexo B.3; ISO/IEC 17043:2023, Cláusula 7.3.2.1
```

---

### 2.5. Nueva Sección: 6. Guía de Interpretación de Resultados

**Ubicación:** Antes de Sección 7 "Conclusiones"

**Contenido:**

```markdown
# 6. Guía de Interpretación de Resultados

Esta guía proporciona orientación a los participantes para interpretar sus resultados de ensayo de aptitud.

## 6.1. Interpretación de Scores

| Score | Rango | Interpretación | Acción Sugerida |
|-------|-------|---------------|------------------|
| \|z\|, \|z'\|, \|ζ\| | 0.0 - 2.0 | Resultado satisfactorio dentro de expectativas | Ninguna acción requerida |
| \|z\|, \|z'\|, \|ζ\| | 2.0 - 3.0 | Resultado cuestionable, posible desviación | Investigar: calibración, procedimiento, equipo, error de cálculo |
| \|z\|, \|z'\|, \|ζ\| | ≥ 3.0 | Resultado insatisfactorio, desviación significativa | Investigación exhaustiva, acción correctiva documentada, reportar a proveedor |

## 6.2. Interpretación de Compatibilidad Metrológica

| Condición | Interpretación | Acción Sugerida |
|-----------|---------------|------------------|
| |xdiff| ≤ 2$udiff$ | Compatible metrológicamente | Ninguna acción requerida |
| 2$udiff$ < |xdiff| ≤ 3$udiff$ | Compatibilidad cuestionable | Investigar sesgo en procedimiento de calibración |
| |xdiff| > 3$udiff$ | No compatible metrológicamente | Investigar procedimiento, reportar acción correctiva a proveedor |

## 6.3. Interpretación de Homogeneidad/Estabilidad

| Condición | Interpretación | Impacto en Participantes |
|-----------|---------------|-------------------------|
| CUMPLE criterio | Ítems de ensayo válidos | Evaluación normal |
| NO CUMPLE (homogeneidad) | Ítems no homogéneos | Puede afectar comparabilidad entre participantes |
| NO CUMPLE (estabilidad) | Ítems no estables | Incertidumbre del valor asignado expandida en evaluación |

## 6.4. Recomendaciones Generales

1. **Revisión de Procedimientos:** Si se observan cuestionables o insatisfactorios en múltiples rondas, revisar procedimientos de calibración y calidad
2. **Validación de Incertidumbres:** Verificar que las incertidumbres reportadas incluyan todos los componentes relevantes
3. **Comparación Histórica:** Comparar resultados con rondas anteriores para identificar tendencias de mejora o deterioro
4. **Capacitación:** Consultar guía de CALAIRE sobre métodos de calibración y manejo de equipos de medición

**Referencia:** ISO 13528:2022, Cláusulas 9.4-9.7; ISO/IEC 17043:2023, Cláusula 7.4.3.2 r
```

---

## 3. Modificaciones en Secciones Existenes

### 3.1. Modificación: Sección 2.2 - Homogeneidad y Estabilidad

**Cambio Requerido:** Añadir documentación de acciones mitigatorias

**Antes:**

```markdown
**Estabilidad:** Se monitoreó la estabilidad de la concentración generada durante cada corrida mediante los instrumentos de referencia de CALAIRE, según ISO 13528:2022, Anexo B. Los datos de estabilidad se presentan en el Anexo B.
```

**Después:**

```markdown
**Estabilidad:** Se monitoreó la estabilidad de la concentración generada durante cada corrida mediante los instrumentos de referencia de CALAIRE, según ISO 13528:2022, Anexo B. Los datos de estabilidad se presentan en el Anexo B.

**Gestión de Inestabilidad:** Para más detalles sobre la gestión de fallos en estabilidad y su impacto en la evaluación, ver Sección 3.3.
```

---

### 3.2. Modificación: Sección 2.3 - Determinación del Valor Asignado

**Cambio Requerido:** Reestructurar para incluir nuevas subsecciones

**Antes:**

```markdown
## 2.3. Determinación del Valor Asignado ($x_{pt}$) y su desviación ($\sigma_{pt}$)

El valor asignado se determinó por consenso de los participantes, utilizando un estimador robusto (Algoritmo A).

La desviación estándar para la evaluación de la aptitud ($\sigma_{pt}$) se estableció para cada contaminante basándose en ISO 13528:2022.

**Método Específico:** *Por consenso:* $\sigma_{pt} = s^{*}$, donde $s^{*}$ es la desviación estándar robusta calculada mediante el Algoritmo A.

Los valores de $x_{pt}$ y $\sigma_{pt}$ calculados para cada nivel se presentan en el Anexo A.
```

**Después:**

```markdown
## 2.3. Determinación del Valor Asignado ($x_{pt}$) y su desviación ($\sigma_{pt}$)

Para esta ronda, el valor asignado y la desviación estándar se determinan según lo siguiente:

**Método de Valor Asignado:** [ESPECIFICAR: Valor de Referencia de CALAIRE / Consenso de Participantes]

**Método de $\sigma_{pt}$:** [ESPECIFICAR: Fitness for Purpose / Derivado del Grupo]

Los valores de $x_{pt}$ y $\sigma_{pt}$ calculados para cada nivel se presentan en el Anexo A.

Para detalles sobre políticas de grupos pequeños, criterios de selección de score y justificación de $\sigma_{pt}$, ver Secciones 2.3.1, 2.3.2 y 2.3.3.
```

---

### 3.3. Modificación: Sección 2.4 - Compatibilidad Metrológica

**Cambio Requerido:** Añadir documentación de conclusiones y acciones

**Antes:**

```markdown
Se evaluó la compatibilidad metrológica calculando las diferencias entre el valor de referencia ($x_{pt,ref}$) y el valor de consenso ($x_{pt,3}$) para cada contaminante y nivel.

[Tabla de compatibilidad]
```

**Después:**

```markdown
Se evaluó la compatibilidad metrológica calculando las diferencias entre el valor de referencia ($x_{pt,ref}$) y el valor de consenso ($x_{pt,3}$) para cada contaminante y nivel.

**Interpretación:**
- Compatible: |xdiff| ≤ 2$udiff|
- Cuestionable: 2$udiff$ < |xdiff| ≤ 3$udiff|
- No compatible: |xdiff| > 3$udiff|

**Acciones Tomadas:** [ESPECIFICAR SI SE TOMARON ACCIONES ANTE INCOMPATIBILIDAD]

[Tabla de compatibilidad con columnas adicionales: "Estado", "Acción"]

**Referencia:** ISO 13528:2022, Cláusula 7.8.1-7.8.3
```

---

### 3.4. Modificación: Sección 3.1 - Indicadores de Desempeño

**Cambio Requerido:** Añadir definiciones de z'-score y ζ-score

**Antes:**

```markdown
Se calcularon los siguientes indicadores de desempeño para cada resultado reportado $x_{i}$ por cada participante:

[Tabla 3 con solo z-score]

: Tabla. Criterios de evaluación del desempeño
```

**Después:**

```markdown
Se calcularon los siguientes indicadores de desempeño para cada resultado reportado $x_{i}$ por cada participante:

-----------------------------------------------------------------------------------------------
Indicador    Ecuación                                   Evaluación
------------ ------------------------------------------ -------------------------------------------
z-score      $z = \frac{x_{i} - x_{pt}}{\sigma_{pt}}$       \|z\| ≤ 2.0: Satisfactorio
                                                       2.0 < \|z\| < 3.0: Cuestionable
                                                       \|z\| ≥ 3.0: Insatisfactorio

z'-score     $z' = \frac{x_{i} - x_{pt}}{\sqrt{\sigma_{pt}^2 + u^2(x_{pt})}}$  Mismos criterios que z-score
             (usado si $u(x_{pt})/\sigma_{pt} > 0.5$)

ζ-score     $\zeta = \frac{x_{i} - x_{pt}}{\sqrt{u^2(x_{i}) + u^2(x_{pt})}}$ Mismos criterios que z-score
            (opcional, para evaluación por incertidumbre)
-----------------------------------------------------------------------------------------------

: Tabla. Criterios de evaluación del desempeño

**Nota:** Para detalles sobre el criterio de selección de score, ver Sección 2.3.2.
```

---

## 3. Hallazgos de Revisión (Fase 1-3)

### 3.1. Hallazgos Fase 1 - Matriz de Requisitos Normativos

| Severidad | Hallazgo | Acción Requerida | Estado |
|-----------|---------|-------------------|--------|
| Alta | Citación incorrecta de ISO 13528 §9.2.1 (debe ser §9.4.1) | Corregir en la tabla | Pendiente |
| Alta | Severidad no normalizada en columna "Brecha" | Unificar a Alta/Media/Baja | Pendiente |
| Alta | Error de formato en compatibilidad (símbolo "|" no escapado) | Escapar símbolo | Pendiente |
| Media | Error tipográfico "compatibla" | Corregir a "compatible" | Pendiente |

### 3.2. Hallazgos Fase 2 - Hallazgos Específicos del Informe

| Severidad | Hallazgo | Acción Requerida | Estado |
|-----------|---------|-------------------|--------|
| Alta | Inconsistencia en severidades (mezcla Alta/Media/Baja con Bloqueantes) | Unificar esquema | Pendiente |
| Alta | Resumen de severidades incorrecto (conteos no coinciden) | Recalcular y actualizar | Pendiente |
| Alta | Acciones requeridas con placeholders no accionables | Reemplazar por acciones concretas | Pendiente |
| Media | Referencias normativas inconsistentes (falta año) | Verificar y corregir | Pendiente |
| Media | Duplicación de hallazgos en "Hallazgos Críticos (Bloqueantes)" | Aclarar si es resumen | Pendiente |
| Baja | Notación matemática incorrecta (delimitadores incompletos) | Corregir sintaxis LaTeX | Pendiente |

### 3.3. Hallazgos Fase 3 - Instrucciones para Rmd

| Severidad | Hallazgo | Acción Requerida | Estado |
|-----------|---------|-------------------|--------|
| Bloqueante | Bloques de código Rmd anidados (triples backticks) | Usar fences de 4 backticks o escapar | Pendiente |
| Bloqueante | Cierres de fences duplicados | Eliminar fences sobrantes | Pendiente |
| Alta | Notación matemática inconsistente (compatibilidad metrológica) | Normalizar con LaTeX y definir variables | Pendiente |
| Alta | Criterio de estabilidad no alineado (texto vs código) | Alinear `c_estab` con texto y código | Pendiente |
| Alta | Ejemplos Rmd con funciones/objetos no definidos | Añadir dependencias y preparación de entorno | Pendiente |
| Media | Encabezados de tablas truncados o desalineados | Reparar estructuras | Pendiente |
| Baja | Errores ortográficos ("Existenes", "cálculo") | Corregir | Pendiente |

---

## 4. Acciones de Corrección Pendientes

### 4.1. Acciones Fase 1

1. [ ] Corregir citación ISO 13528 §9.2.1 → §9.4.1
2. [ ] Unificar severidades a Alta/Media/Baja
3. [ ] Escapar símbolo "|" en compatibilidad
4. [ ] Corregir "compatibla" → "compatible"

### 4.2. Acciones Fase 2

1. [ ] Unificar esquema de severidad
2. [ ] Recalcular resumen de severidades
3. [ ] Reemplazar placeholders por acciones concretas
4. [ ] Verificar y corregir referencias normativas
5. [ ] Aclarar duplicación en "Hallazgos Críticos"
6. [ ] Corregir notación matemática

### 4.3. Acciones Fase 3

1. [ ] Corregir bloques de código Rmd
2. [ ] Eliminar fences duplicados
3. [ ] Normalizar notación matemática
4. [ ] Alinear criterio de estabilidad
5. [ ] Añadir dependencias para ejemplos Rmd
6. [ ] Reparar encabezados de tablas
7. [ ] Corregir errores ortográficos

---

## 5. Plan de Implementación

### 5.1. Priorización

| Prioridad | Fase | Acción | Severidad |
|----------|-------|--------|----------|
| 1 | Fase 3 | Corregir bloques de código Rmd | Bloqueante |
| 2 | Fase 3 | Normalizar notación matemática | Alta |
| 3 | Fase 1 | Corregir citación ISO | Alta |
| 4 | Fase 2 | Unificar severidades | Alta |
| 5 | Fase 2 | Reemplazar placeholders | Alta |
| 6 | Fase 3 | Alinear criterio de estabilidad | Alta |
| 7 | Fase 3 | Añadir dependencias | Alta |

### 5.2. Cronograma

- Semana 1: Corregir Fase 1 (citación, severidades, formato)
- Semana 2: Corregir Fase 2 (severidades, placeholders, referencias)
- Semana 3: Corregir Fase 3 (bloques Rmd, notación matemática, dependencias)
- Semana 4: Verificación final y actualización de checklist

---

## 6. Checklist de Verificación (Actualizado)

Antes de finalizar la actualización de la plantilla Rmd, verificar lo siguiente:

- [ ] Sección 2.3.1 "Política de Grupos Pequeños" creada
- [ ] Sección 2.3.2 "Criterio de Selección de Score" creada
- [ ] Sección 2.3.3 "Justificación de $\sigma_{pt}$" creada
- [ ] Sección 3.3 "Gestión de Inestabilidad" creada
- [ ] Sección 6 "Guía de Interpretación de Resultados" creada
- [ ] Tabla A.1 actualizada con columnas "Fuente de Valor Asignado" y "Política σpt"
- [ ] Tabla B.1 actualizada con columnas "Acción Tomada" e "Impacto en Evaluación"
- [ ] Tabla B.2 actualizada con columnas "Acción Tomada" e "Impacto en Evaluación"
- [ ] Tabla de compatibilidad metrológica actualizada con columnas "Estado" y "Acción"
- [ ] Sección 2.3 actualizada para referenciar nuevas subsecciones
- [ ] Sección 2.4 actualizada con interpretación y acciones de compatibilidad
- [ ] Sección 3.1 actualizada con definiciones de z'-score y ζ-score
- [ ] Sección 5 actualizada con mención de estabilidad y compatibilidad
- [ ] Código Rmd para selección automática de método de valor asignado
- [ ] Código Rmd para selección automática de método de $\sigma_{pt}$
- [ ] Código Rmd para expansión de incertidumbre en caso de inestabilidad
- [ ] Referencias normativas agregadas en todas las secciones nuevas
- [ ] Bloques de código Rmd renderizan correctamente
- [ ] Notación matemática consistente en todo el documento
- [ ] Ejemplos de código son ejecutables con dependencias especificadas```

---

### 3.5. Modificación: Sección 5 - Conclusiones

**Cambio Requerido:** Añadir mención de hallazgos de estabilidad y compatibilidad metrológica

**Antes:**

```markdown
# 5. Conclusiones

**Conformidad General:** El desempeño general de los laboratorios participantes en esta ronda fue positivo.

**Áreas de Preocupación:** Se observaron desempeños cuestionables o insatisfactorios en algunos participantes.

**Acciones Sugeridas para Participantes:** Se recomienda...
```

**Después:**

```markdown
# 5. Conclusiones

**Conformidad General:** El desempeño general de los laboratorios participantes en esta ronda fue positivo.

**Áreas de Preocupación:** Se observaron desempeños cuestionables o insatisfactorios en algunos participantes.

**Evaluación de Estabilidad/Homogeneidad:** [ESPECIFICAR SI HUBO FALLOS Y CÓMO SE GESTIONARON]

**Evaluación de Compatibilidad Metrológica:** [ESPECIFICAR ESTADO DE COMPATIBILIDAD Y ACCIONES TOMADAS]

**Acciones Sugeridas para Participantes:** Se recomienda a los laboratorios con resultados **Cuestionables** ($2.0 < |z| < 3.0$) investigar las posibles causas de la desviación. Se requiere a los laboratorios con resultados **Insatisfactorios** ($|z| \geq 3.0$) realizar una investigación exhaustiva de las causas raíz (e.g., calibración, procedimiento, equipo) e implementar acciones correctivas documentadas.

Para más detalles sobre la interpretación de resultados, ver Sección 6. Guía de Interpretación.
```

---

## 4. Actualizaciones en Tablas

### 4.1. Tabla A.1: Valores Asignados y Parámetros Estadísticos

**Cambio:** Añadir columnas de trazabilidad y política $\sigma_{pt}$

**Nueva Estructura:**

```
Contaminante   Nivel     Fuente de Valor   Política σpt    Valor   Incertidumbre   Desviación
                         Asignado                               Asignado     u(x_pt)        (sigma_pt)
```

**Ejemplo de Rmd:**

```rmd
| Contaminante | Nivel | Fuente de Valor Asignado | Política σpt | Valor Asignado (x_pt) | Incertidumbre u(x_pt) | Desviación (sigma_pt) |
|-------------|-------|------------------------|------------|----------------------|---------------------|-------------------|
| CO          | 0-ppm | Valor de Referencia CALAIRE | Fitness for Purpose | -0.0183 | 0.0022 | 0.0060 |
| CO          | 2-ppm | Valor de Referencia CALAIRE | Fitness for Purpose | 2.0137 | 0.0002 | 0.0006 |
```

---

### 4.2. Tabla B.1: Resumen de Evaluación de Homogeneidad

**Cambio:** Añadir columnas de acción tomada e impacto

**Nueva Estructura:**

```
Contaminante   Nivel     Items   Réplicas   sigma_pt   u(x_pt)   ss        sw  Criterio c  Cumple   Acción Tomada            Impacto en Evaluación
```

**Ejemplo de Rmd:**

```rmd
| Contaminante | Nivel | Items | Réplicas | sigma_pt | u(x_pt) | ss | sw | Criterio c | Cumple | Acción Tomada | Impacto en Evaluación |
|-------------|-------|-------|----------|----------|---------|----|----|-----------|--------|--------------|---------------------|
| CO | 0-ppm | 10 | 3 | 0.0412 | 0.0163 | 2.9570 | 4.4192 | 0.0124 | No | Incertidumbre expandida en u(x_pt) | Más conservador, reduce falsos positivos |
```

---

### 4.3. Tabla B.2: Resumen de Evaluación de Estabilidad

**Cambio:** Añadir columnas de acción tomada e impacto

**Nueva Estructura:**

```
Contaminante   Nivel     Items   Réplicas   sigma_pt   u(x_pt)   Diferencia Criterio c  Cumple   Acción Tomada            Impacto en Evaluación
```

**Ejemplo de Rmd:**

```rmd
| Contaminante | Nivel | Items | Réplicas | sigma_pt | u(x_pt) | Diferencia | Criterio c | Cumple | Acción Tomada | Impacto en Evaluación |
|-------------|-------|-------|----------|----------|---------|-----------|-----------|--------|--------------|---------------------|
| CO | 0-ppm | 2 | 3 | 0.0395 | 0.0349 | 1.3313 | 0.0124 | No | Incertidumbre expandida en u(x_pt) | Más conservador, reduce falsos positivos |
```

---

### 4.4. Tabla de Compatibilidad Metrológica (Sección 2.4)

**Cambio:** Añadir columnas de estado y acción

**Nueva Estructura:**

```
Contaminante   Nivel      Valor Ref    Valor Consenso  Dif (Ref -  Estado   Acción
                       (Alg A)                   3)
```

**Ejemplo de Rmd:**

```rmd
| Contaminante | Nivel | Valor Ref (Alg A) | Valor Consenso 3 | Dif (Ref - 3) | Estado | Acción |
|-------------|-------|------------------|---------------------|---------------|--------|--------|
| CO | 0-ppm | -0.0301 | -0.0183 | 0.0117 | Compatible | Ninguna |
| NO | 0-ppb | 0.5240 | 0.5719 | 0.0480 | Cuestionable | Investigar sesgo en calibración |
```

---

## 5. Ejemplos de Código Rmd

### 5.1. Sección 2.3.1: Política de Grupos Pequeños

```rmd
## 2.3.1. Política de Grupos Pequeños

```{r}
n_participantes <- nrow(resultados_participantes)
if (n_participantes < 10) {
  metodo_valor_asignado <- "Valor de Referencia CALAIRE"
  x_pt <- valor_referencia_CALAIRE
} else {
  metodo_valor_asignado <- "Consenso de Participantes (Algoritmo A)"
  x_pt <- robust_mean(resultados_participantes, method = "Algorithm A")
}
```

Conforme a los requisitos de ISO 13528:2022 (cláusula 5.4), para rondas con menos de 10 participantes, el **Valor Asignado ($x_{pt}$)** será determinado mediante el **Valor de Referencia** medido por CALAIRE.

Para n ≥ 10 participantes, el **Valor Asignado ($x_{pt}$)** puede determinarse mediante consenso de los participantes utilizando estimadores robustos, siempre que la compatibilidad metrológica sea satisfactoria (ver Sección 2.4).

**Referencia:** ISO 13528:2022, Cláusula 5.4.1-5.4.2
```
```

---

### 5.2. Sección 2.3.3: Justificación de $\sigma_{pt}$

```rmd
## 2.3.3. Justificación de $\sigma_{pt}$

```{r}
# Opción A: Fitness for Purpose
sigma_pt_fitness <- function(concentracion, contaminante) {
  if (contaminante == "CO") {
    return(concentracion * 0.10)  # 10%
  } else if (contaminante == "NO2") {
    return(concentracion * 0.15)  # 15%
  } else {
    return(concentracion * 0.15)  # 15% (default)
  }
}

# Opción B: Derivado del Grupo
sigma_pt_grupo <- function(resultados) {
  s_star <- robust_sd(resultados, method = "Algorithm A")
  return(s_star)
}

# Selección
if (existe_directiva_regulatoria) {
  sigma_pt <- sigma_pt_fitness(concentracion, contaminante)
  metodo_sigma_pt <- "Fitness for Purpose"
} else {
  sigma_pt <- sigma_pt_grupo(resultados)
  metodo_sigma_pt <- "Derivado del Grupo"
}
```

**Opción Seleccionada para esta Ronda:** `r metodo_sigma_pt`

**Justificación Técnica:** `r justificacion_sigma_pt`

**Referencia:** ISO 13528:2022, Cláusulas 8.1.2, 8.1.3
```
```

---

### 5.3. Sección 3.3: Gestión de Inestabilidad

```rmd
## 3.3. Gestión de Inestabilidad

```{r}
# Criterio de estabilidad (ISO 13528 Anexo B)
criterio_estab <- 0.3 * sigma_pt
dif_estab <- abs(x_final - x_inicio)

# Verificar cumplimiento
cumple_estab <- dif_estab <= criterio_estab

# Si no cumple, expandir incertidumbre
if (!cumple_estab) {
  s_instab_sq <- var(c(estabilidad_inicial, estabilidad_final))
  u_xpt_expandida <- sqrt(u_xpt^2 + s_instab_sq)
  nota_estab <- "Incertidumbre expandida para z'-score y ζ-score"
} else {
  u_xpt_expandida <- u_xpt
  nota_estab <- "Sin acción requerida"
}
```

### Acciones Requeridas
1. **Expansión de Incertidumbre del Valor Asignado:**
   - Si falla estabilidad, calcular: $s^2_{\text{instab}} = \text{Var}(\bar{x}_{\text{final}} - \bar{x}_{\text{inicio}})$
   - Actualizar incertidumbre: $u'(x_{pt}) = \sqrt{u^2(x_{pt}) + s^2_{\text{instab}}}$
   - Aplicar $u'(x_{pt})$ en cáclculo de z'-score y ζ-score

**Referencia:** ISO 13528:2022, Anexo B.3
```
```

---

### 5.4. Tabla A.1 con Nuevas Columnas

```rmd
```{r}
# Crear tabla A.1 con trazabilidad y política sigma_pt
tabla_A1 <- data.frame(
  Contaminante = contaminantes,
  Nivel = niveles,
  Fuente_Valor = ifelse(metodo_valor_asignado == "Valor de Referencia CALAIRE",
                        "Valor de Referencia CALAIRE",
                        "Consenso (Algoritmo A)"),
  Politica_sigma_pt = metodo_sigma_pt,
  Valor_Asignado = x_pt,
  Incertidumbre = u_xpt,
  Desviacion = sigma_pt
)

knitr::kable(tabla_A1,
  caption = "Tabla A.1. Resumen de Valores Asignados y Parámetros Estadísticos",
  booktabs = TRUE,
  align = "lcccccc")
```
```
```

---

## 6. Checklist de Verificación

Antes de finalizar la actualización de la plantilla Rmd, verificar lo siguiente:

- [ ] Sección 2.3.1 "Política de Grupos Pequeños" creada
- [ ] Sección 2.3.2 "Criterio de Selección de Score" creada
- [ ] Sección 2.3.3 "Justificación de $\sigma_{pt}$" creada
- [ ] Sección 3.3 "Gestión de Inestabilidad" creada
- [ ] Sección 6 "Guía de Interpretación de Resultados" creada
- [ ] Tabla A.1 actualizada con columnas "Fuente de Valor Asignado" y "Política σpt"
- [ ] Tabla B.1 actualizada con columnas "Acción Tomada" e "Impacto en Evaluación"
- [ ] Tabla B.2 actualizada con columnas "Acción Tomada" e "Impacto en Evaluación"
- [ ] Tabla de compatibilidad metrológica actualizada con columnas "Estado" y "Acción"
- [ ] Sección 2.3 actualizada para referenciar nuevas subsecciones
- [ ] Sección 2.4 actualizada con interpretación y acciones de compatibilidad
- [ ] Sección 3.1 actualizada con definiciones de z'-score y ζ-score
- [ ] Sección 5 actualizada con mención de estabilidad y compatibilidad
- [ ] Código Rmd para selección automática de método de valor asignado
- [ ] Código Rmd para selección automática de método de $\sigma_{pt}$
- [ ] Código Rmd para expansión de incertidumbre en caso de inestabilidad
- [ ] Referencias normativas agregadas en todas las secciones nuevas

---

## 7. Referencias Normativas

- ISO/IEC 17043:2023 - Conformity assessment — General requirements for proficiency testing
- ISO 13528:2022 - Statistical methods for use in proficiency testing by interlaboratory comparison
- Barbiere M., et al. (2022). Proficiency testing scheme for SO2, CO, O3, NO and NO2 in filtered ambient air. JRC Technical Report EUR 31348 EN.
- Umweltbundesamt (2024). Proficiency Testing for Gaseous Air Pollutants 2024.

---

## Apéndice: Mapeo de Secciones Normativas a CALAIRE

| Normativa | Cláusula | Sección CALAIRE | Estado |
|-----------|---------|-------------------|--------|
| ISO 13528 5.4 | Grupos pequeños | 2.3.1 | Nueva |
| ISO 13528 8.1.2 | Fitness for purpose | 2.3.3 | Nueva |
| ISO 13528 9.5.1 | z'-score | 2.3.2, 3.1 | Nueva |
| ISO 13528 9.6.1 | ζ-score | 2.3.2, 3.1 | Nueva |
| ISO 13528 Anexo B | Inestabilidad | 3.3 | Nueva |
| ISO 13528 7.8 | Compatibilidad metrológica | 2.4 | Modificada |
| ISO 17043 7.4.3.2 l | Trazabilidad | A.1 | Modificada |
| ISO 17043 7.4.3.2 r | Guía de interpretación | 6 | Nueva |
