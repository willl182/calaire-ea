# Fase 1: Matriz de Requisitos Normativos para Informes EA

**Fecha:** 2026-02-08
**Estado:** completado
**Base normativa:** ISO/IEC 17043:2023, ISO 13528:2022

---

## 1. Requisitos para Valor Asignado ($x_{pt}$)

| Cláusula Normativa | Requisito | Estado Actual Informe EA-2025 | Brecha | Referencia |
|-------------------|-----------|-----------------------------------|--------|------------|
| ISO 13528 §5.4 (n pequeño) | Para n < 12, usar valor de referencia metrológicamente válido, independiente de participantes | Uso consenso (Algoritmo A) con n=13 | Riesgo: consenso no es robusto para n pequeño, pero n=13 es aceptable | ISO 13528:5.4.1, 5.4.2 |
| ISO 13528 §7.8 (Compatibilidad) | Comparar valor de referencia ($x_{ref}$) con valor de consenso ($x_{pt}$), calcular $u_{diff} = \sqrt{u^2(x_{ref}) + u^2(x_{pt})}$ | Se calcula compatibilidad metrológica, pero no se documenta acción si |$x_{diff}$| > 2$u_{diff}$| | Informe muestra compatibilidad pero no especifica criterio de acción | ISO 13528:7.8.1-7.8.3 |
| ISO 17043 7.2.3.2 | Cuando se usa valor de consenso, proveer estimación de incertidumbre del valor asignado | Informe incluye $u(x_{pt})$ en Tabla A.1 | No hay brecha | ISO 17043 7.2.3.2 |

---

## 2. Requisitos para Criterio de Desempeño ($\sigma_{pt}$)

| Cláusula Normativa | Requisito | Estado Actual Informe EA-2025 | Brecha | Referencia |
|-------------------|-----------|-----------------------------------|--------|------------|
| ISO 13528 §8.1.2 (Fitness for Purpose) | Si existe requisito regulatorio, usarlo como $\sigma_{pt}$ (dividir por 3 para z-score) | $\sigma_{pt} = s^*$ (desviación robusta de participantes) | Brecha crítica: criterio derivado del grupo, no es estable ni consistente en rondas sucesivas | ISO 13528:8.1.2 |
| ISO 13528 §8.1.3 (Consensus-based) | Si se usa consenso, preferir estimador robusto de desviación estándar (s*, nIQR) | Se usa $s^*$ de Algoritmo A | No hay brecha en método, pero el enfoque es problemático para grupos pequeños | ISO 13528:8.1.3 |
| ISO 17043 7.2.2.3 b) | Proveedor debe establecer criterio de evaluación adecuado para el propósito del esquema | Informe no documenta política de selección de $\sigma_{pt}$ | Falta documentación de justificación de $\sigma_{pt}$ | ISO 17043 7.2.2.3 |

---

## 3. Requisitos para Estabilidad y Homogeneidad

| Cláusula Normativa | Requisito | Estado Actual Informe EA-2025 | Brecha | Referencia |
|-------------------|-----------|-----------------------------------|--------|------------|
| ISO 17043 7.3.2.1 | Establecer criterios de homogeneidad y estabilidad basados en riesgos | Se evalúa pero hay fallos reportados (NO CUMPLE CRITERIO) | Brecha crítica: fallos en estabilidad no tienen acción mitigatoria documentada | ISO 17043 7.3.2.1 |
| ISO 13528 Anexo B | ss ≤ 0.3$\sigma_{pt}$ (homogeneidad) | Criterio usado: ss > 0.3$\sigma_{pt}$ indica NO CUMPLE | Fallos en múltiples contaminantes (CO, NO, NO2, O3) | Fallos múltiples indican problema sistemático | ISO 13528 Anexo B |
| ISO 13528 Anexo B | Diferencia de estabilidad ≤ criterio definido | Fallos en estabilidad reportados | Brecha crítica: no se evidencia expansión de incertidumbre del $x_{pt}$ cuando falla estabilidad | ISO 13528 Anexo B |

---

## 4. Requisitos para Criterios de Evaluación (Scores)

| Cláusula Normativa | Requisito | Estado Actual Informe EA-2025 | Brecha | Referencia |
|-------------------|-----------|-----------------------------------|--------|------------|
| ISO 13528 §9.4.1 (z-score) | $z = (x_i - x_{pt})/\sigma_{pt}$; \|z\| ≤ 2: satisfactorio, 2<\|z\|<3: cuestionable, \|z\|≥3: insatisfactorio | Implementado correctamente en Tabla 5 | No hay brecha | ISO 13528:9.4.1 |
| ISO 13528 §9.5.1 (z'-score) | $z' = (x_i - x_{pt})/\sqrt{\sigma_{pt}^2 + u^2(x_{pt})}$ cuando incertidumbre del $x_{pt}$ es alta | No implementado en informe actual | Falta criterio de decisión para usar z vs z' | ISO 13528:9.5.1 |
| ISO 13528 §9.6.1 (ζ-score) | $\zeta = (x_i - x_{pt})/\sqrt{u^2(x_i) + u^2(x_{pt})}$ cuando se evalúa contra incertidumbre reportada | No implementado en informe actual | Opción útil para evaluación alternativa, especial en grupos pequeños | ISO 13528:9.6.1 |
| ISO 13528 §9.7.1 (En-score) | $E_n = (x_i - x_{pt})/\sqrt{U^2(x_i) + U^2(x_{pt})}$ con incertidumbres expandidas | No implementado en informe actual | Opción útil para evaluación compatible | ISO 13528:9.7.1 |

---

## 5. Requisitos para Estructura y Contenido del Informe

| Cláusula Normativa | Requisito | Estado Actual Informe EA-2025 | Brecha | Referencia |
|-------------------|-----------|-----------------------------------|--------|------------|
| ISO 17043 7.4.3.2 a) | Nombre, contacto del proveedor | Implementado (Sección 1.4) | No hay brecha | ISO 17043 7.4.3.2 a) |
| ISO 17043 7.4.3.2 i) | Resultados de participantes, incertidumbres reportadas | Tabla de compatibilidad metrológica presente, pero no se evidencia uso en scores | Falta documentación de cómo se usaron las incertidumbres reportadas | ISO 17043 7.4.3.2 i) |
| ISO 17043 7.4.3.2 j) | Procedimientos para análisis estadístico | Sección 3.2 describe tratamiento estadístico | No hay brecha | ISO 17043 7.4.3.2 j) |
| ISO 17043 7.4.3.2 k) | Datos estadísticos, valores asignados, rango aceptable, gráficos | Tabla A.1 (valores asignados), gráficos de mapa de calor presentes | No hay brecha | ISO 17043 7.4.3.2 k) |
| ISO 17043 7.4.3.2 l) | Trazabilidad metrológica, incertidumbre del valor asignado | Tabla de compatibilidad metrológica incluye diferencias | No se documenta explícitamente la cadena de trazabilidad | ISO 17043 7.4.3.2 l) |
| ISO 17043 7.4.3.2 m) | Procedimientos para establecer valor asignado y su incertidumbre | Sección 2.3 describe consenso y Algoritmo A | No hay brecha | ISO 17043 7.4.3.2 m) |
| ISO 17043 7.4.3.2 n) | Valores asignados, incertidumbres, resumen por método si aplica | Tabla A.1 incluye valores para todos los contaminantes | No hay brecha | ISO 17043 7.4.3.2 n) |
| ISO 17043 7.4.3.2 o) | Procedimientos para establecer $\sigma_{pt}$ | Sección 2.3 describe $s^*$ de Algoritmo A | Falta documentación de política de $\sigma_{pt}$ | ISO 17043 7.4.3.2 o) |
| ISO 17043 7.4.3.2 p) | Comentarios sobre desempeño de participantes | Sección 5 tiene acciones sugeridas | No hay brecha | ISO 17043 7.4.3.2 p) |
| ISO 17043 7.4.3.2 r) | Asesoría sobre interpretación del análisis estadístico | No se incluye explicación detallada de interpretación | Falta guía de interpretación para participantes | ISO 17043 7.4.3.2 r) |

---

## 6. Requisitos Adicionales (Benchmarking JRC/UBA)

| Práctica JRC/UBA | Requisito Implícito | Estado Actual Informe EA-2025 | Brecha | Referencia |
|------------------|-------------------|-----------------------------------|--------|------------|
| JRC (Barbiere) | Usar valor de referencia independiente cuando sea posible | Informe usa consenso | Falta política para valores de referencia en grupos pequeños | Barbiere 2022 |
| JRC (Barbiere) | Evaluar compatibilidad metrológica (7.8) y documentar conclusiones | Se calcula pero no se documentan conclusiones ni acciones | Falta documentación de conclusiones de compatibilidad | Barbiere 2022 |
| UBA | Evaluar z'-score y En-score además de z-score | Solo se implementa z-score | Falta evaluación alternativa con incertidumbres | UBA 2024 |
| UBA | Usar $\sigma_{pt}$ fijo basado en directivas regulatorias (fitness for purpose) | $\sigma_{pt} = s^*$ (del grupo) | Brecha crítica: no es consistente entre rondas | UBA 2024 |

---

## Resumen de Brechas Críticas

| Prioridad | Brecha | Impacto en Conformidad Normativa |
|----------|--------|-----------------------------------|
| Alta | Fallos en estabilidad sin acción mitigatoria | ISO 13528 Anexo B, ISO 17043 7.3.2.1 |
| Alta | $\sigma_{pt}$ derivado del grupo (no fitness for purpose) | ISO 13528 8.1.2, ISO 17043 7.2.2.3 |
| Media | Falta criterio de decisión para usar z vs z' | ISO 13528 9.5.1 |
| Media | No se documentan conclusiones de compatibilidad metrológica | ISO 13528 7.8 |
| Media | Falta guía de interpretación estadística para participantes | ISO 17043 7.4.3.2 r) |
| Baja | No se implementa ζ-score ni En-score | ISO 13528 9.6.1, 9.7.1 (opcional) |
