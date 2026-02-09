# Fase 2: Hallazgos Específicos del Informe EA_2025-12-10_13-z-3-3

**Fecha:** 2026-02-08
**Estado:** completado
**Informe analizado:** Informe_EA_2025-12-10_13-z-3-3.md

---

## 1. Sección 1: Información del Proveedor y del Esquema

| Sección/Subsección | Hallazgo | Severidad | Referencia Normativa | Acción Requerida |
|------------------|---------|----------|---------------------|-------------------|
| 1.1. Información del Proveedor | No hay brecha | - | - | - |
| 1.3. Confidencialidad y Uso del Informe | No hay brecha | - | - | - |
| 1.4. Roles de Autorización y Personal Clave | No hay brecha | - | - | - |
| 1.5. Participantes e Instrumentación | No hay brecha | - | - | - |

---

## 2. Sección 2: Descripción del Ensayo y Metodología

| Sección/Subsección | Hallazgo | Severidad | Referencia Normativa | Acción Requerida |
|------------------|---------|----------|---------------------|-------------------|
| 2.1. Ítems de Ensayo y Producción | No hay brecha | - | - | - |
| 2.2. Homogeneidad y Estabilidad | Brecha CRÍTICA: Fallos reportados sin acción mitigatoria | Alta | ISO 13528 Anexo B, ISO 17043 7.3.2.1 | Añadir subsección 2.2.3 explicando: (a) qué acción se tomó cuando fallaron criterios, (b) si se expandió $u(x_{pt})$, (c) cómo afectó esto a la evaluación de participantes |
| 2.3. Determinación del Valor Asignado | Falta documentación de política para grupos pequeños | Media | ISO 13528 5.4 | Añadir nota: "Para n < 10, el Valor Asignado es el Valor de Referencia de CALAIRE (no consenso)" |
| 2.3. Determinación del Valor Asignado | Falta documentación de criterio de decisión para usar z vs z' | Media | ISO 13528 9.2.1, 9.5.1 | Añadir subsección 2.3.2: "Criterio de Selección de Score" |
| 2.3. Determinación del Valor Asignado | Falta explicación de justificación de $\sigma_{pt}$ | Alta | ISO 13528 8.1.2, ISO 17043 7.2.2.3 | Añadir subsección 2.3.3: "Justificación de $\sigma_{pt}$" con política fitness for purpose o derivada del grupo |
| 2.4. Compatibilidad Metrológica | Falta documentación de conclusiones | Media | ISO 13528 7.8 | Añadir: "Si |xdiff| > 2$udiff|, se investiga la causa y se documenta en el informe" |

---

## 3. Sección 3: Criterios de Evaluación

| Sección/Subsección | Hallazgo | Severidad | Referencia Normativa | Acción Requerida |
|------------------|---------|----------|---------------------|-------------------|
| 3.1. Indicadores de Desempeño | Falta definición de z'-score y ζ-score | Media | ISO 13528 9.5.1, 9.6.1 | Añadir definiciones en Tabla 3.1 como notas al pie o subsección separada |
| 3.1. Indicadores de Desempeño | Falta definición de En-score | Baja | ISO 13528 9.7.1 | Añadir definición opcional (evaluación alternativa) |
| 3.2. Tratamiento Estadístico | No hay brecha | - | - | - |

---

## 4. Sección 4: Resultados y Discusión

| Sección/Subsección | Hallazgo | Severidad | Referencia Normativa | Acción Requerida |
|------------------|---------|----------|---------------------|-------------------|
| 4.1. Resumen General del Desempeño | No hay brecha | - | - | - |
| 4.2. Evaluación por Contaminante | No hay brecha | - | - | - |

---

## 5. Sección 5: Conclusiones

| Sección/Subsección | Hallazgo | Severidad | Referencia Normativa | Acción Requerida |
|------------------|---------|----------|---------------------|-------------------|
| 5. Conclusiones | Falta mención de hallazgos de estabilidad | Alta | ISO 17043 7.4.3.2 r | Añadir: "Se identificaron fallos en criterios de estabilidad para múltiples contaminantes. Esto se evaluó según ISO 13528 Anexo B." |
| 5. Conclusiones | Falta mención de compatibilidad metrológica | Media | ISO 13528 7.8 | Añadir: "La compatibilidad metrológica fue evaluada para todos los contaminantes" |
| 5. Conclusiones | Falta referencia a políticas de $\sigma_{pt}$ | Alta | ISO 13528 8.1.2 | Añadir: "El criterio $\sigma_{pt}$ se determinó según [política seleccionada]" |

---

## 6. Anexos

| Anexo | Hallazgo | Severidad | Referencia Normativa | Acción Requerida |
|-------|---------|----------|---------------------|-------------------|
| Anexo A: Valores Asignados | Falta documentación de cadena de trazabilidad | Media | ISO 17043 7.4.3.2 l | Añadir columna "Trazabilidad Metrológica" en Tabla A.1 |
| Anexo B: Homogeneidad y Estabilidad | Fallos en múltiples entradas sin notas explicativas | Alta | ISO 13528 Anexo B, ISO 17043 7.3.2.1 | Añadir notas explicativas para cada "NO CUMPLE" explicando la acción tomada o su impacto |

---

## 7. Hallazgos Estructurales (Nuevas Secciones Requeridas)

| Nueva Sección | Contenido Requerido | Severidad | Referencia Normativa |
|----------------|---------------------|----------|---------------------|
| 2.3.1. Política de Grupos Pequeños | "Para n < 10 participantes, el Valor Asignado será el Valor de Referencia medido por CALAIRE. El criterio $\sigma_{pt}$ se establecerá según directivas regulatorias o experto (fitness for purpose)." | Alta | ISO 13528 5.4 |
| 2.3.2. Criterio de Selección de Score | "Se usa z-score. Si $u(x_{pt})/\sigma_{pt} > 0.5$, se usa z'-score. Si los participantes reportan incertidumbres confiables, se puede usar ζ-score." | Media | ISO 13528 9.2.1, 9.5.1, 9.6.1 |
| 2.3.3. Justificación de $\sigma_{pt}$ | "El criterio $\sigma_{pt}$ se determina basándose en [opción seleccionada]: (a) Directiva regulatoria X% (fitness for purpose), (b) Desviación robusta del grupo ($s^*$) para n ≥ 10." | Alta | ISO 13528 8.1.2, 8.1.3 |
| 3.3. Gestión de Inestabilidad | "Si falla el criterio de estabilidad (ss > 0.3$\sigma_{pt}$ o diferencia > criterio definido), se expande la incertidumbre del valor asignado: $u'(x_{pt}) = \sqrt{u^2(x_{pt}) + s^2_{instab}}$, donde $s^2_{instab}$ es la varianza de inestabilidad." | Alta | ISO 13528 Anexo B |

---

## 8. Hallazgos en Tablas y Gráficos

| Tabla/Gráfico | Hallazgo | Severidad | Acción Requerida |
|----------------|---------|----------|-------------------|
| Tabla 3. Criterios de evaluación | Falta definición de z'-score y ζ-score | Media | Añadir definiciones como notas al pie |
| Tabla A.1. Valores Asignados | Falta columnas de trazabilidad y política $\sigma_{pt}$ | Alta | Añadir columnas: "Fuente de Valor Asignado", "Política $\sigma_{pt}$" |
| Tabla B.1. Homogeneidad | Fallos sin notas explicativas | Alta | Añadir columnas "Acción Tomada" y "Impacto en Evaluación" |
| Tabla B.2. Estabilidad | Fallos sin notas explicativas | Alta | Añadir columnas "Acción Tomada" y "Impacto en Evaluación" |

---

## 9. Hallazgos de Redacción y Claridad

| Elemento | Hallazgo | Severidad | Acción Requerida |
|---------|---------|----------|-------------------|
| Lenguaje técnico | No se usa terminología ISO (ej: "ítems de ensayo" en vez de "proficiency test items") | Baja | Armonizar terminología con ISO 17043/13528 |
| Explicación de métodos | No se explica por qué se usa Algoritmo A | Media | Añadir justificación técnica del algoritmo seleccionado |
| Interpretación de resultados | No se incluye guía de interpretación para participantes | Media | Añadir sección "Guía de Interpretación de Resultados" |

---

## 10. Hallazgos Críticos (Bloqueantes)

| # | Hallazgo | Ubicación | Severidad | Impacto en Informe |
|---|---------|-----------|----------|-------------------|
| 1 | Fallos en estabilidad sin acción mitigatoria documentada | Sección 2.2, Anexo B | Alta | Puede invalidar evaluación según ISO 13528 Anexo B |
| 2 | Falta política de $\sigma_{pt}$ fitness for purpose | Sección 2.3 | Alta | No es consistente con ISO 13528 8.1.2 para evaluación longitudinal |
| 3 | Falta justificación de $\sigma_{pt}$ | Sección 2.3 | Alta | Falta documentación requerida por ISO 17043 7.2.2.3 |
| 4 | Falta documentación de acciones ante fallos de estabilidad | Sección 5, Anexo B | Alta | Falta transparencia y trazabilidad de decisiones |

---

## Resumen de Hallazgos por Severidad

| Severidad | Cantidad | Secciones Afectadas |
|-----------|----------|-------------------|
| Alta | 5 | 2.2, 2.3, 5, Anexo B, A.1 |
| Media | 5 | 2.3, 2.4, 3.1, 5, A.1 |
| Baja | 2 | 3.1, 9 |

**Total:** 12 hallazgos identificados
