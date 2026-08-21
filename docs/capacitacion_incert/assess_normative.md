# Evaluación de fuentes para curso de 8 horas

## 1. `Incertidumbre del Ozono.pdf`

**Cubre**

- Caso aplicado a analizadores de O₃ y patrón dinámico de transferencia.
- Modelo con repetibilidad, curva de calibración, certificado del patrón y aire cero.
- Autocorrelación, falta de ajuste, combinación, \(U=ku_c\), resultados por concentración y cálculo en R.
- Uso de incertidumbre en \(z'\), zeta y \(E_n\).

**Partes enseñables**

- §§1–3: mensurando, particularidades del O₃ y diseño experimental.
- §4: repetibilidad Tipo A y corrección por autocorrelación.
- §5: curva multipunto, residuos y falta de ajuste.
- §§6–7: certificado del patrón y aire cero.
- §8: presupuesto, contribuciones relativas e incertidumbre expandida.
- §§9–11: cálculo reproducible, aplicación y limitaciones.

**Papel**

- **Fuente docente principal aplicada.**
- **Fuente principal de ejercicios.**
- No normativa.

**Valoración**

Mejor puente entre GUM y operación real. Contiene datos, fórmulas y decisiones discutibles útiles para taller. Debe presentarse como caso en desarrollo: supone independencia, usa \(k=2\) fijo y deja deriva de ganancia fuera del presupuesto.

---

## 2. `JCGM_GUM-1.pdf` — JCGM GUM-1:2023

**Cubre**

- Introducción vigente a familia GUM.
- Razón para evaluar incertidumbre.
- Mensurando, modelo, Tipo A/Tipo B, propagación y cobertura.
- Mapa de documentos JCGM relacionados.

**Partes enseñables**

- §§2–3: propósito, medición, mensurando e incertidumbre.
- §4: decisiones necesarias para evaluar incertidumbre.
- §§4.8–4.10: Tipo A, Tipo B y propagación.
- §5.1: marco clásico JCGM 100.
- §5.3: función de modelos, enlace con GUM-6.
- §5.4: introducción a Monte Carlo.
- Anexo A: mapa de familia GUM.

**Papel**

- **Referencia internacional introductoria.**
- Fuente para conceptos y terminología.
- No suficiente como guía de cálculo ni como fuente de ejercicios.

**Valoración**

Buena lectura inicial. Breve y clara, pero no desarrolla coeficientes de sensibilidad, covarianzas, grados efectivos ni presupuestos completos.

---

## 3. `JCGM_GUM_6_2020.pdf` — JCGM GUM-6:2020

**Cubre**

- Desarrollo, selección y validación de modelos de medición.
- Modelos teóricos, empíricos, híbridos y multietapa.
- Calibración, regresión, efectos compartidos, deriva y adecuación del modelo.

**Partes enseñables**

- §§5–6: principios y especificación del mensurando.
- §§7.2, 8.1–8.2: modelo híbrido y aptitud para propósito.
- §8.4: cadena multietapa, referencia–patrón–analizador.
- §9: identificación de efectos.
- §§10.2–10.5: correcciones, efectos residuales y fuentes compartidas.
- §10.6: deriva y efectos temporales; crítico para patrones de transferencia.
- §11.4: función de calibración frente a función de medición.
- §§12–13.2: validación y prohibición de extrapolación injustificada.
- Anexo E: análisis causa–efecto.
- Anexo F: comprobación de linealización.
- Anexo C, selectivo: variación aleatoria y reproducibilidad.

**Papel**

- **Referencia técnica para construir y validar modelo.**
- Fuente de actividad causa–efecto.
- Complemento del GUM clásico, no sustituto.

**Valoración**

Muy pertinente para cadena de transferencia y deriva. Evita presupuesto matemáticamente correcto pero físicamente incompleto. Demasiado amplio para cubrir completo en ocho horas.

---

## 4. `ISO_IEC Guide 98-3_2008 ... GUM_1995 ...pdf`

**Cubre**

- Procedimiento clásico completo para expresar incertidumbre.
- Modelo \(Y=f(X_1,\ldots,X_N)\).
- Evaluaciones Tipo A y Tipo B.
- Coeficientes de sensibilidad, covarianzas, combinación, expansión y reporte.

**Partes enseñables**

- §§2.2–2.3: error, incertidumbre y términos esenciales.
- §§3.1–3.4: mensurando, correcciones y consideraciones prácticas.
- §4.1: modelo de medición.
- §§4.2–4.3: evaluaciones Tipo A y Tipo B.
- §§4.3.3–4.3.9: normal, rectangular y triangular.
- §4.3.10: prevención de doble conteo.
- §§5.1–5.2: propagación y correlación.
- §§6.2–6.3: incertidumbre expandida y selección de \(k\).
- §§7–8: reporte y resumen del procedimiento.
- Anexo F: evaluación práctica de componentes.
- Anexo G.3–G.4: distribución t y Welch–Satterthwaite.
- Anexo H.1 o H.3: ejemplo completo por analogía.
- Anexo H.5: opcional para análisis de varianza.

**Papel**

- **Referencia normativa/metrológica troncal.**
- Base del método de cálculo.
- Fuente secundaria de ejercicios por analogía.

**Valoración**

Documento central del curso. Debe gobernar presupuesto y reporte. No identifica por sí mismo fuentes específicas de fotometría UV, generación de O₃, estabilidad o transferencia.

---

## 5. `ISO_IEC Guide 98-3_2008 Suppl.2_2011 ...pdf` — JCGM 102:2011

**Cubre**

- Modelos con varias magnitudes de salida.
- Matrices de covarianza.
- Propagación multivariada y Monte Carlo.
- Regiones conjuntas de cobertura.
- Modelos multietapa.

**Partes enseñables**

- §§3.6–3.12: mensurando vectorial y modelos multivariados/multietapa.
- §§3.18–3.20: covarianza, matriz de covarianza y correlación.
- §5.2: etapas de evaluación.
- §§5.3–5.5: distribuciones de entrada, propagación y resumen.
- §6.2: propagación en modelos explícitos multivariados.
- §§7.1–7.7: flujo Monte Carlo, preferiblemente como demostración.
- §8: validación del marco GUM mediante Monte Carlo.
- §9.2: modelo aditivo.
- §9.5.3: mediciones que comparten parámetros de calibración.
- Anexo B: referencia para sensibilidad y covarianza.
- Anexo D: glosario de símbolos.

**Papel**

- **Referencia avanzada.**
- Fuente para ejercicio opcional sobre concentraciones correlacionadas.
- No necesaria para núcleo operativo de ocho horas.

**Valoración**

Útil cuando varios puntos de O₃ comparten patrón, cero, pendiente o intercepto. Exceso matemático si audiencia solo necesita presupuesto escalar. Limitar a concepto de covarianza y una demostración corta; omitir regiones de cobertura.

---

## 6. `USEPA - Quality Handbook.pdf`

**Cubre**

- Sistema de QA para vigilancia de calidad del aire.
- DQO/MQO, calibración, QC, auditoría, validación y trazabilidad.
- Cadena SRP–estándar de nivel 2–estándar de transferencia–analizador.
- Verificaciones multipunto, cero, span, estabilidad y deriva.

**Partes enseñables**

- §3.1–3.2: DQO, MQO, precisión y sesgo.
- §§10.1–10.3: QC e independencia entre control interno y auditoría.
- §10.4: cero, span, QC de un punto, auditorías y estabilidad.
- §12.1: patrones, trazabilidad y estándares de transferencia.
- §12.1.2: trazabilidad del O₃ a fotómetro UV primario.
- §12.2: procedimiento de calibración.
- §12.3: verificación multipunto, pendiente, intercepto y linealidad.
- §12.4: frecuencia, deriva y riesgo de ajustes excesivos.
- Tabla 12-1: instrumentos y criterios de certificación.
- §12.5: validación de datos frente a fallas.
- Tabla 15-1 y §15.2.1: cadena SRP y auditorías independientes.

**Papel**

- **Fuente operativa y de QA.**
- **Fuente de escenarios y ejercicios procedimentales.**
- Referencia regulatoria estadounidense; no norma metrológica universal ni sustituto del GUM.

**Valoración**

Mejor fuente para explicar operación real de analizadores y estándares de transferencia. Sus tolerancias y criterios de aceptación no deben copiarse directamente como incertidumbres estándar. Contrastar requisitos EPA 2017 con documentos vigentes y requisitos aplicables en Colombia.

---

# Selección final

## Núcleo obligatorio

1. **ISO/IEC Guide 98-3:2008:** método de evaluación y reporte.
2. **JCGM GUM-6:2020:** construcción y validación del modelo.
3. **Incertidumbre del Ozono:** caso práctico integral.
4. **USEPA Quality Handbook:** trazabilidad y operación de analizadores/patrones.

## Uso selectivo

- **JCGM GUM-1:2023:** introducción conceptual y mapa documental.
- **Suplemento 2:** correlaciones entre niveles y Monte Carlo; módulo avanzado breve.

## Distribución posible

- **1 h:** conceptos, mensurando y trazabilidad.
- **1 h:** sistema UV, cadena de transferencia y modelo.
- **1.5 h:** identificación de fuentes; Tipo A y Tipo B.
- **1.5 h:** sensibilidad, combinación y correlación.
- **1 h:** calibración multipunto, estabilidad y deriva.
- **0.5 h:** incertidumbre expandida, cobertura y reporte.
- **1.5 h:** ejercicio integral basado en `Incertidumbre del Ozono.pdf`.

**Diagnóstico:** conjunto suficiente para curso sólido de ocho horas. Principal vacío: documento técnico sectorial específico sobre certificación de estándares de transferencia de O₃ y trazabilidad vigente aplicable en Colombia.
