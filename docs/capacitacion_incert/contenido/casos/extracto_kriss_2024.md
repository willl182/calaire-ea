# Caso de taller — Comparación BIPM.QM-K1 con KRISS (2024)

## Propósito del caso

Este extracto presenta datos públicos de la comparación de ozono a nivel ambiente realizada entre KRISS y BIPM en 2024. Su uso en el módulo 7 consiste en reconstruir presupuestos de incertidumbre, interpretar una regresión con incertidumbres y covarianzas, y juzgar si transporte del patrón introdujo cambio metrológicamente significativo.

## 1. Contexto de comparación

BIPM.QM-K1 es una comparación clave continua, organizada como serie de comparaciones bilaterales. Funciona desde enero de 2007 y evalúa grado de equivalencia de fotómetros de ozono mantenidos como patrones nacionales o patrones primarios de redes internacionales. Valor de referencia se determina con NIST Standard Reference Photometer BIPM-SRP27, mantenido por BIPM como referencia común (informe, secciones 3 y 5, p. 2).

Comparación de 2024 enfrentó patrón nacional coreano KRISS-SRP5 con referencia común BIPM-SRP27 mediante patrón de transferencia KRISS-SRP3. Primero, KRISS-SRP5 y KRISS-SRP3 se compararon en KRISS en agosto de 2024; después, KRISS-SRP3 se comparó con BIPM-SRP27 en BIPM, un mes más tarde; finalmente, KRISS-SRP5 y KRISS-SRP3 volvieron a compararse en KRISS en octubre de 2024 para comprobar estabilidad del patrón de transferencia (informe, sección 8, p. 3). Mediciones cubrieron intervalo nominal de fracción de cantidad de ozono de **0 nmol mol⁻¹ a 500 nmol mol⁻¹** (informe, resumen, p. 1; sección 12.4, p. 6).

Cada corrida incluyó diez niveles no nulos más mediciones de cero al inicio y final, en secuencia **0, 220, 80, 420, 120, 320, 30, 370, 170, 500, 270 y 0 nmol mol⁻¹**; cada punto fue promedio de diez mediciones individuales (informe, secciones 8.1.b y 8.2.b, pp. 3–4). Serie se aceptó cuando desviación estándar de diez mediciones de KRISS-SRP5 o BIPM-SRP27 fue menor que **1 nmol mol⁻¹** (informe, secciones 8.1.b y 8.2.b, pp. 3–4).

## 2. Presupuestos de incertidumbre

Tablas siguientes transcriben componentes y valores de Tablas 1 y 2 del informe. Informe comunica fuente, distribución, incertidumbre estándar, incertidumbre estándar combinada por componente, coeficiente de sensibilidad y contribución a `u(x)`, pero **no clasifica explícitamente fuentes como tipo A o tipo B**. Por regla de este caso, columna “Tipo A/B” queda como **no reportado**; estudiantes deberán discutir clasificación posible sin presentarla como dato publicado. Columna “Comportamiento” se basa en expresión publicada de contribución: término sin `x`, constante; término multiplicado por `x`, proporcional.

### 2.1 BIPM-SRP27

| Componente | Fuente | Distribución | Incertidumbre estándar | Combinada `u(y)` | Contribución a `u(x)` / nmol mol⁻¹ | Tipo A/B | Comportamiento |
|---|---|---:|---:|---:|---:|---|---|
| Optical Path `L_opt` | Measurement scale | Rectangular | 0.0006 cm | 0.52 cm | `2.89 × 10⁻³ x` | no reportado | proporcional |
| Optical Path `L_opt` | Repeatability | Normal | 0.01 cm | 0.52 cm | `2.89 × 10⁻³ x` | no reportado | proporcional |
| Optical Path `L_opt` | Correction factor | Rectangular | 0.52 cm | 0.52 cm | `2.89 × 10⁻³ x` | no reportado | proporcional |
| Pressure `P` | Pressure gauge | Rectangular | 0.029 kPa | 0.034 kPa | `3.37 × 10⁻⁴ x` | no reportado | proporcional |
| Pressure `P` | Difference between cells | Rectangular | 0.017 kPa | 0.034 kPa | `3.37 × 10⁻⁴ x` | no reportado | proporcional |
| Temperature `T` | Temperature probe | Rectangular | 0.03 K | 0.07 K | `2.29 × 10⁻⁴ x` | no reportado | proporcional |
| Temperature `T` | Temperature gradient | Rectangular | 0.058 K | 0.07 K | `2.29 × 10⁻⁴ x` | no reportado | proporcional |
| Ratio of intensities `D` | Scaler resolution | Rectangular | `8 × 10⁻⁶` | `1.4 × 10⁻⁵` | 0.28 | no reportado | constante |
| Ratio of intensities `D` | Repeatability | Triangular | `1.1 × 10⁻⁵` | `1.4 × 10⁻⁵` | 0.28 | no reportado | constante |
| Absorption Cross section per molecule `σ` | Hearn value | no reportado | `1.22 × 10⁻¹⁹ cm²` | `1.22 × 10⁻¹⁹ cm²` | `1.06 × 10⁻² x` | no reportado | proporcional |

**Origen:** informe, sección 12.4, Tabla 1, p. 7. Expresión resumida publicada: `u(x) = √[(0.28)² + (2.92 × 10⁻³ x)²]`, con valores de `x` en nmol mol⁻¹ (informe, ecuación 4, p. 7). Apéndice 1 del protocolo publica misma estructura del presupuesto y, para uso convencional común de sección eficaz, muestra contribución de `σ` como “–”; además deriva `u(x) = √[(0.28)² + (2.92 × 10⁻³ x)²]` (protocolo, App. 1, secciones 1–2, pp. 21–23).

### 2.2 KRISS-SRP5

| Componente | Fuente | Distribución | Incertidumbre estándar | Combinada `u(y)` | Contribución a `u(x)` / nmol mol⁻¹ | Tipo A/B | Comportamiento |
|---|---|---:|---:|---:|---:|---|---|
| Optical Path `L_opt` | Measurement scale | Rectangular | 0.003 cm | 0.52 cm | `2.89 × 10⁻³ x` | no reportado | proporcional |
| Optical Path `L_opt` | Variability | Rectangular | 0.03 cm | 0.52 cm | `2.89 × 10⁻³ x` | no reportado | proporcional |
| Optical Path `L_opt` | Divergence | Rectangular | 0.52 cm | 0.52 cm | `2.89 × 10⁻³ x` | no reportado | proporcional |
| Pressure `P` | Pressure gauge | Rectangular | 0.029 kPa | 0.032 kPa | `3.23 × 10⁻⁴ x` | no reportado | proporcional |
| Pressure `P` | Difference between cells | Rectangular | 0.014 kPa | 0.032 kPa | `3.23 × 10⁻⁴ x` | no reportado | proporcional |
| Temperature `T` | Temperature probe | Rectangular | 0.029 K | 0.065 K | `2.15 × 10⁻⁴ x` | no reportado | proporcional |
| Temperature `T` | Temperature bias | Rectangular | 0.058 K | 0.065 K | `2.15 × 10⁻⁴ x` | no reportado | proporcional |
| Ratio of intensities `D` | Scaler resolution | Rectangular | `1.38 × 10⁻⁶` | `1.21 × 10⁻⁵` | 0.24 | no reportado | constante |
| Ratio of intensities `D` | Repeatability | Triangular | `1.20 × 10⁻⁵` | `1.21 × 10⁻⁵` | 0.24 | no reportado | constante |
| Absorption Cross section `σ` | Conventional value | no reportado | `1.22 × 10⁻¹⁹ cm²/molecule` | `1.22 × 10⁻¹⁹ cm²/molecule` | `1.06 × 10⁻² x` | no reportado | proporcional |

**Origen:** informe, sección 12.7, Tabla 2, p. 8. Expresión resumida publicada: `u(x) = √[(0.24)² + (2.92 × 10⁻³ x)²]`, con `x` en nmol mol⁻¹ (informe, ecuación 7, p. 8). Informe indica que mismo término de covarianza usado para BIPM-SRP27 se incluyó para KRISS-SRP5 (sección 12.7, p. 8).

## 3. Regresión y tratamiento de incertidumbre

Relación se ajustó mediante **generalised least-square regression** con software OzonE. Método incluye incertidumbres asociadas a resultados y correlaciones entre mediciones hechas con mismo instrumento a distintas fracciones de ozono; también permite usar patrón de transferencia y manejar correlaciones inevitables por su calibración frente al patrón de referencia (informe, sección 14, pp. 8–9). Informe no usa expresión literal “incertidumbre en ambos ejes”, pero procedimiento incorpora incertidumbres de resultados de referencia y transferencia en ajuste; por tanto, no corresponde describirlo como mínimos cuadrados ordinarios con eje `x` exacto (informe, sección 14, pp. 8–9; sección 15.2, p. 10).

Modelo publicado fue `x_KRISS-SRP5 = a₀ + a₁ x_SRP27` (informe, ecuación 8, p. 9). Resultados:

| Momento | Intercepto `a₀` / nmol mol⁻¹ | `u(a₀)` / nmol mol⁻¹ | Pendiente `a₁` | `u(a₁)` | `cov(a₀,a₁)` |
|---|---:|---:|---:|---:|---:|
| pre BIPM visit | 0.41 | 0.28 | 0.9971 | 0.0046 | `−3.47 × 10⁻⁴` |
| post BIPM visit | −0.03 | 0.28 | 0.9976 | 0.0046 | `−3.52 × 10⁻⁴` |

**Origen:** informe, sección 14.1, ecuaciones 9–10, p. 9. Informe juzga ambos interceptos consistentes con cero mediante `|a₀| < 2u(a₀)` y ambas pendientes consistentes con uno mediante `|1 − a₁| < 2u(a₁)` (sección 14.1, p. 9).

## 4. Estabilidad de transporte

Comparaciones pre y post transporte produjeron pendiente **0.9971** e intercepto **0.41 nmol mol⁻¹** antes de visita, y pendiente **0.9976** e intercepto **−0.03 nmol mol⁻¹** después de visita (informe, sección 14.1, p. 9). Informe resume cambio de pendiente como aumento de **0.05 %**, pequeño frente a incertidumbres, y concluye que patrón de transferencia KRISS-SRP3 puede considerarse estable durante comparación (informe, sección 16, p. 12). No reporta prueba estadística adicional específica para diferencia entre interceptos pre/post; por tanto: **no reportado**.

Conclusión global señala comparación en rango **0 nmol mol⁻¹ a 500 nmol mol⁻¹** y grados de equivalencia con muy buen acuerdo entre ambos patrones (informe, sección 19, pp. 12–13).

## 5. Preguntas dirigidas para taller

1. ¿Qué fuentes del presupuesto podrían evaluarse como tipo A y cuáles como tipo B? Sustentar clasificación con método de evaluación, no solo con forma de distribución.
2. ¿Por qué contribución de `Ratio of intensities D` aparece como término constante, mientras `L_opt`, `P`, `T` y `σ` generan términos proporcionales a `x`?
3. Reconstruir `u(x)` de BIPM-SRP27 para dos niveles elegidos dentro de rango publicado. ¿En qué zona domina término constante de **0.28 nmol mol⁻¹** y en cuál domina término proporcional **`2.92 × 10⁻³ x`** (informe, ecuación 4, p. 7)?
4. Repetir cálculo para KRISS-SRP5 con término constante de **0.24 nmol mol⁻¹**. ¿Qué diferencia práctica produce frente a BIPM-SRP27 (informe, ecuación 7, p. 8)?
5. ¿Qué consecuencias tendría ignorar covarianzas entre mediciones del mismo fotómetro al estimar pendiente e intercepto? Usar modelo de covarianza publicado `u(xᵢ,xⱼ) = xᵢxⱼu_b²`, con `u_b = 2.92 × 10⁻³` (informe, sección 12.5, ecuaciones 5–6, p. 7; protocolo, App. 1, sección 3, pp. 24–25).
6. Aplicar criterios `|a₀| < 2u(a₀)` y `|1 − a₁| < 2u(a₁)` a resultados pre y post. ¿Respaldan conclusión de acuerdo? (informe, sección 14.1, p. 9).
7. ¿Cambio de pendiente de **0.05 %** basta por sí solo para declarar estabilidad? ¿Qué comparación de incertidumbres, covarianzas o diferencia pre/post sería deseable añadir? (informe, sección 16, p. 12).
8. ¿Qué elementos publicados permiten juzgar trazabilidad y comparabilidad, y cuáles quedan no reportados para una evaluación independiente completa?
