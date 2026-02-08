# Matriz Consolidada de Hallazgos - Fase 1

**Created**: 2026-02-08 16:36
**Fase**: 1 - Consolidación de Análisis Preliminares
**Documento base**: M.LCAFMi-## Comunicacion Detallada EAdocx.md

---

## Resumen

Total hallazgos: **4**  
Hallazgos críticos: **1**  
Hallazgos de alta prioridad: **2**  
Hallazgos de media prioridad: **1**

---

## Matriz de Hallazgos

| # | Brecha | Severidad | Fuente Análisis | Sección/Ancla | Requisito ISO 17043 | Referencia Modelo | Estado Documento |
|---|--------|-----------|----------------|---------------|---------------------|-------------------|------------------|
| 1 | **Seguridad Industrial** - Sin sección de normas de seguridad (EPP, manejo cilindros a presión, rutas evacuación, normas transporte mercancías peligrosas) | Crítica | comparacion_comunicacion_vs_otras.md | "Comparativa Técnica" | 7.3.4.4 (Etiquetado y seguridad transporte), 7.3.4 (Seguridad) | JRC-ERLAP - Sección "Safety" | Omisión |
| 2 | **Definición σpt** - No especifica origen de la desviación estándar para la aptitud (¿fija por criterio regulatorio o derivada de estadística del grupo?) | Alta | compliance_comunicacion.md, comparacion_comunicacion_vs_otras.md | "Hallazgos y Oportunidades de Mejora", "Comparativa Estadística" | 7.4.2 (Criterios de evaluación), ISO 13528:2022 | UBA - Definición σpt basado en rondas previas o reproducibilidad actual | Omisión |
| 3 | **Quejas y Apelaciones** - No menciona procedimiento ni plazos para apelaciones | Alta | compliance_comunicacion.md, comparacion_comunicacion_vs_otras.md | "Hallazgos y Oportunidades de Mejora", "Comparativa de Gestión" | 7.6 (Quejas), 7.7 (Apelaciones), 7.7.2 (Descripción disponible) | UBA - Procedimiento 14 días | Omisión |
| 4 | **Subcontratación** - No declara si alguna fase del proceso es externa (ej. calibración de patrones primarios) | Media | comparacion_comunicacion_vs_otras.md | "Comparativa de Gestión y Comunicación" | 6.4 (Subcontratación), 7.3.1 (Informar a participantes) | UCLSB - Identificación explícita de subcontratista | Omisión |

---

## Hallazgos Detallados

### Hallazgo 1: Seguridad Industrial (Crítica)

**Fuente:** `comparacion_comunicacion_vs_otras.md:17,21`

**Descripción:**
El documento de JRC-ERLAP incluye una sección específica de "Safety" que prohíbe caminar sin escolta y exige EPP. CALAIRE menciona el transporte seguro pero no establece normas de seguridad dentro del laboratorio (ej. manejo de gases a presión, normativa de transporte de cilindros de gas, rutas de evacuación).

**Requisito ISO 17043:**
- Cláusula 7.3.4.4: Etiquetado y seguridad en el transporte
- Cláusula 7.3.4: Seguridad durante la realización del EA

**Impacto:**
Riesgo en esquemas presenciales por falta de protocolos de seguridad industrial para manejo de gases a presión.

**Recomendación:**
Añadir sección "Seguridad" similar a JRC, especificando:
- Normativa de transporte de cilindros
- Normas de seguridad industrial dentro de instalaciones de CALAIRE
- Uso obligatorio de EPP
- Rutas de evacuación

---

### Hallazgo 2: Definición σpt (Alta)

**Fuente:** `compliance_comunicacion.md:52`, `comparacion_comunicacion_vs_otras.md:33`

**Descripción:**
El documento menciona el uso del z-score, cuya fórmula requiere una desviación estándar para la evaluación de la aptitud (σpt). El documento actual NO especifica cómo se determinará este valor.

**Riesgo identificado:**
Si CALAIRE usa la desviación del grupo, penaliza a los participantes cuando el grupo es muy preciso y premia cuando el grupo es malo.

**Requisito ISO 17043:**
- Cláusula 7.4.2: Criterios de evaluación del desempeño
- ISO 13528:2022: Determinación de σpt

**Referencia Modelo (UBA):**
Define σpt basándose en rondas previas (>6 rondas) o la desviación estándar de reproducibilidad de la ronda actual.

**Recomendación:**
Especificar en Sección 7 el origen de σpt:
- ¿Es un valor fijo regulatorio (como JRC)?
- ¿Es estadístico del grupo?
- ¿Es un modelo general como Horwitz?

---

### Hallazgo 3: Quejas y Apelaciones (Alta)

**Fuente:** `compliance_comunicacion.md:54`, `comparacion_comunicacion_vs_otras.md:49`

**Descripción:**
El documento analizado NO menciona el procedimiento de apelación. ISO 17043 exige tener procesos documentados y que la descripción esté disponible para las partes interesadas.

**Requisito ISO 17043:**
- Cláusula 7.6: Quejas
- Cláusula 7.7: Apelaciones
- Cláusula 7.6.2: El proceso de manejo de quejas debe estar disponible
- Cláusula 7.7.2: La descripción del proceso de manejo de apelaciones debe estar disponible

**Referencia Modelo (UBA):**
Define explícitamente un plazo de 14 días para objeciones y describe el proceso.

**Recomendación:**
Incluir apartado sobre "Quejas y Apelaciones" con:
- Procedimiento documentado
- Plazos definidos (ej. 14 días)
- Referencia o enlace al procedimiento completo

---

### Hallazgo 4: Declaración de Subcontratación (Media)

**Fuente:** `comparacion_comunicacion_vs_otras.md:56`

**Descripción:**
El documento no menciona subcontratistas, lo cual es correcto si CALAIRE realiza todo internamente. Sin embargo, debe declarar explícitamente si alguna fase es externa (ej. calibración de patrones primarios).

**Requisito ISO 17043:**
- Cláusula 6.4: Subcontratación
- Cláusula 7.3.1: Los participantes deben ser informados de actividades subcontratadas

**Referencia Modelo (UCLSB):**
Identifica claramente al subcontratista para la preparación de muestras.

**Recomendación:**
Declarar explícitamente en Sección 8:
- ¿Hay actividades subcontratadas?
- Si no, declarar: "Todas las fases del EA son ejecutadas internamente por CALAIRE"
- Si sí, identificar al subcontratista

---

## Cumplimiento Actual vs ISO 17043

| Cláusula ISO 17043 | Estado CALAIRE | Evidencia |
|-------------------|----------------|-----------|
| 7.1.2 Comunicación del esquema | CUMPLE | Objetivos, criterios, cronograma |
| 7.2.3 Determinación del valor asignado | CUMPLE | MRC + fotómetro nivel 2 (método 7.5 ISO 13528) |
| 7.3.5.2 Instrucciones a participantes | CUMPLE | Protocolo detallado Día 1-3 |
| 7.4.2 Criterios de evaluación | CUMPLE PARCIALMENTE | Define ζ-score y En-score, pero omite σpt |
| 7.6 Quejas | NO CUMPLE | Sin procedimiento documentado |
| 7.7 Apelaciones | NO CUMPLE | Sin procedimiento documentado |
| 7.3.4 Seguridad | CUMPLE PARCIALMENTE | Menciona transporte pero omite seguridad in-situ |
| 6.4 Subcontratación | NO CUMPLE | Sin declaración |
| 4.2 Confidencialidad | CUMPLE | Códigos únicos, compromiso no confabulación |

---

## Análisis Comparativo: CALAIRE vs Proveedores de Referencia

| Aspecto | CALAIRE | JRC-ERLAP | UBA | Brno | UCLSB |
|---------|---------|-----------|-----|------|-------|
| Seguridad in-situ | ❌ No | ✅ Exhaustivo | - | - | - |
| Definición σpt | ❌ No | ✅ Fija | ✅ Descripción | ✅ Descripción | ✅ Descripción |
| Quejas/Apelaciones | ❌ No | ✅ Formulario anexo | ✅ 14 días | ❌ No | ❌ No |
| Subcontratación | ❌ No | - | - | - | ✅ Declara |
| Valor asignado | ✅ Referencia | ✅ Referencia | ✅ Consenso | ✅ Consenso | ✅ Consenso |
| Instrucciones técnicas | ✅ Detalladas | ✅ Hora a hora | ✅ Claras | ✅ Normas EN | ✅ Logísticas |

---

## Priorización para Fase 4

**Orden de implementación:**

1. **Seguridad Industrial** (Crítica) - Riesgo operativo y de cumplimiento
2. **Definición σpt** (Alta) - Transparencia estadística, impacto directo en evaluación
3. **Quejas y Apelaciones** (Alta) - Derechos del cliente, requisito ISO 17043
4. **Subcontratación** (Media) - Declaración administrativa

---

## Observaciones Adicionales

### Fortalezas de CALAIRE

1. **Valor asignado metrológicamente superior**: CALAIRE usa un valor de referencia propio (Fotómetro Nivel 2 / MRC), lo cual es superior para grupos pequeños (n<12) en comparación con esquemas por consenso (UBA, Brno).
2. **Manejo de incertidumbre más exigente**: El uso de ζ-score y En-score obliga a los participantes a reportar correctamente sus incertidumbres, mientras que el z'-score de JRC es más permisivo.
3. **Instrucciones técnicas excelentes**: El protocolo in-situ (Día 1-3) es técnicamente sólido y detallado.

### Oportunidad Adicional (No Prioritaria)

- **Gestión de grupos pequeños (n<5)**: Dado que CALAIRE usa valores de referencia, podría explotar esto en la comunicación como ventaja competitiva, diferenciándose de esquemas como Brno que dependen de métodos estadísticos complejos (Horn) para grupos pequeños.

---

## Referencias de Fuentes

- `compliance_comunicacion.md` - Auditoría frente a ISO/IEC 17043:2023
- `comparacion_comunicacion_vs_otras.md` - Comparativa vs JRC-ERLAP, UBA, PTPP, UCLSB
- `comparacion_comunicacion_vs_otras2.md` - Auditoría de ejemplos internacionales (UBA, Brno, UCLSB)

---

## Registro de Revisiones

### Revisión 1 - 2026-02-08 16:38 (Revisor-fase)

**Hallazgos incorporados:**
- ✅ Referencias actualizadas: reemplazadas referencias genéricas "Fuente N" por anclas de sección para trazabilidad
- ✅ Columna "Sección/Ancla" añadida a matriz para ubicación precisa en documentos fuente
- ✅ Cláusulas ISO homogeneizadas a nivel de detalle consistente

**Observaciones pendientes:**
- Referencias a PDFs externos (UBA 2025, JRC-ERLAP) requieren extracción en Fase 3 para completar trazabilidad
- Evidencia de `comparacion_comunicacion_vs_otras2.md` citada en sección "Análisis Comparativo" pero no explícitamente en matriz; esto es correcto dado que ese documento audita ejemplos de referencia, no la comunicación actual de CALAIRE
