# Caso de taller — Comparación BIPM.QM-K1 con KRISS (2024)

## Propósito del caso

Este extracto presenta datos públicos de la comparación de ozono a nivel ambiente realizada entre KRISS y BIPM en 2024. Su uso en el módulo 7 consiste en reconstruir presupuestos de incertidumbre, interpretar una regresión con incertidumbres y covarianzas, y juzgar si el transporte del patrón introdujo un cambio metrológicamente significativo.

## 1. Contexto de comparación

BIPM.QM-K1 es una comparación clave continua, organizada como una serie de comparaciones bilaterales. Funciona desde enero de 2007 y evalúa el grado de equivalencia de fotómetros de ozono mantenidos como patrones nacionales o patrones primarios de redes internacionales. El valor de referencia se determina con el NIST Standard Reference Photometer BIPM-SRP27, mantenido por el BIPM como referencia común (informe, secciones 3 y 5, p. 2).

La comparación de 2024 enfrentó el patrón nacional coreano KRISS-SRP5 con la referencia común BIPM-SRP27 mediante el patrón de transferencia KRISS-SRP3. Primero, KRISS-SRP5 y KRISS-SRP3 se compararon en el KRISS en agosto de 2024; después, KRISS-SRP3 se comparó con BIPM-SRP27 en el BIPM, un mes más tarde; finalmente, KRISS-SRP5 y KRISS-SRP3 volvieron a compararse en el KRISS en octubre de 2024 para comprobar la estabilidad del patrón de transferencia (informe, sección 8, p. 3). Las mediciones cubrieron el intervalo nominal de fracción de cantidad de ozono de **0 nmol mol⁻¹ a 500 nmol mol⁻¹** (informe, resumen, p. 1; sección 12.4, p. 6).

Cada corrida incluyó diez niveles no nulos más mediciones de cero al inicio y al final, en la secuencia **0, 220, 80, 420, 120, 320, 30, 370, 170, 500, 270 y 0 nmol mol⁻¹**; cada punto fue el promedio de diez mediciones individuales (informe, secciones 8.1.b y 8.2.b, pp. 3–4). La serie se aceptó cuando la desviación estándar de diez mediciones de KRISS-SRP5 o BIPM-SRP27 fue menor que **1 nmol mol⁻¹** (informe, secciones 8.1.b y 8.2.b, pp. 3–4).

## 2. Presupuestos de incertidumbre

Las tablas siguientes transcriben componentes y valores de las Tablas 1 y 2 del informe. El informe comunica la fuente, la distribución, la incertidumbre estándar, la incertidumbre estándar combinada por componente, el coeficiente de sensibilidad y la contribución a `u(x)`, pero **no clasifica explícitamente las fuentes como tipo A o tipo B**. Por regla de este caso, la columna “Tipo A/B” queda como **no reportado**; los estudiantes deberán discutir una clasificación posible sin presentarla como dato publicado. La columna “Comportamiento” se basa en la expresión publicada de la contribución: un término sin `x` es constante; un término multiplicado por `x` es proporcional.

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

**Origen:** informe, sección 12.4, Tabla 1, p. 7. Expresión resumida publicada: `u(x) = √[(0.28)² + (2.92 × 10⁻³ x)²]`, con valores de `x` en nmol mol⁻¹ (informe, ecuación 4, p. 7). El Apéndice 1 del protocolo publica la misma estructura del presupuesto y, para el uso convencional común de la sección eficaz, muestra la contribución de `σ` como “–”; además, deriva `u(x) = √[(0.28)² + (2.92 × 10⁻³ x)²]` (protocolo, App. 1, secciones 1–2, pp. 21–23).

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

**Origen:** informe, sección 12.7, Tabla 2, p. 8. Expresión resumida publicada: `u(x) = √[(0.24)² + (2.92 × 10⁻³ x)²]`, con `x` en nmol mol⁻¹ (informe, ecuación 7, p. 8). El informe indica que el mismo término de covarianza usado para BIPM-SRP27 se incluyó para KRISS-SRP5 (sección 12.7, p. 8).

## 3. Regresión y tratamiento de incertidumbre

La relación se ajustó mediante una **regresión generalizada por mínimos cuadrados** con el software OzonE. El método incluye las incertidumbres asociadas a los resultados y las correlaciones entre mediciones hechas con el mismo instrumento a distintas fracciones de ozono; también permite usar un patrón de transferencia y manejar las correlaciones inevitables derivadas de su calibración frente al patrón de referencia (informe, sección 14, pp. 8–9). El informe no usa la expresión literal “incertidumbre en ambos ejes”, pero el procedimiento incorpora las incertidumbres de los resultados de referencia y transferencia en el ajuste; por tanto, no corresponde describirlo como mínimos cuadrados ordinarios con el eje `x` exacto (informe, sección 14, pp. 8–9; sección 15.2, p. 10).

El modelo publicado fue `x_KRISS-SRP5 = a₀ + a₁ x_SRP27` (informe, ecuación 8, p. 9). Resultados:

| Momento | Intercepto `a₀` / nmol mol⁻¹ | `u(a₀)` / nmol mol⁻¹ | Pendiente `a₁` | `u(a₁)` | `cov(a₀,a₁)` |
|---|---:|---:|---:|---:|---:|
| antes de la visita al BIPM | 0.41 | 0.28 | 0.9971 | 0.0046 | `−3.47 × 10⁻⁴` |
| después de la visita al BIPM | −0.03 | 0.28 | 0.9976 | 0.0046 | `−3.52 × 10⁻⁴` |

**Origen:** informe, sección 14.1, ecuaciones 9–10, p. 9. El informe juzga ambos interceptos consistentes con cero mediante `|a₀| < 2u(a₀)` y ambas pendientes consistentes con uno mediante `|1 − a₁| < 2u(a₁)` (sección 14.1, p. 9).

## 4. Estabilidad de transporte

Las comparaciones previas y posteriores al transporte produjeron una pendiente de **0.9971** y un intercepto de **0.41 nmol mol⁻¹** antes de la visita, y una pendiente de **0.9976** y un intercepto de **−0.03 nmol mol⁻¹** después de la visita (informe, sección 14.1, p. 9). El informe resume el cambio de pendiente como un aumento de **0.05 %**, pequeño frente a las incertidumbres, y concluye que el patrón de transferencia KRISS-SRP3 puede considerarse estable durante la comparación (informe, sección 16, p. 12). No se reporta una prueba estadística adicional específica para la diferencia entre los interceptos previos y posteriores; por tanto: **no reportado**.

La conclusión global señala que la comparación cubrió el intervalo de **0 nmol mol⁻¹ a 500 nmol mol⁻¹** y que los grados de equivalencia mostraron muy buen acuerdo entre ambos patrones (informe, sección 19, pp. 12–13).

## 5. Preguntas dirigidas para taller

1. ¿Qué fuentes del presupuesto podrían evaluarse como tipo A y cuáles como tipo B? Sustente la clasificación con el método de evaluación, no solo con la forma de la distribución.
2. ¿Por qué la contribución de `Ratio of intensities D` aparece como término constante, mientras `L_opt`, `P`, `T` y `σ` generan términos proporcionales a `x`?
3. Reconstruya `u(x)` de BIPM-SRP27 para dos niveles elegidos dentro del intervalo publicado. ¿En qué zona domina el término constante de **0.28 nmol mol⁻¹** y en cuál domina el término proporcional **`2.92 × 10⁻³ x`** (informe, ecuación 4, p. 7)?
4. Repita el cálculo para KRISS-SRP5 con el término constante de **0.24 nmol mol⁻¹**. ¿Qué diferencia práctica produce frente a BIPM-SRP27 (informe, ecuación 7, p. 8)?
5. ¿Qué consecuencias tendría ignorar las covarianzas entre mediciones del mismo fotómetro al estimar la pendiente y el intercepto? Use el modelo de covarianza publicado `u(xᵢ,xⱼ) = xᵢxⱼu_b²`, con `u_b = 2.92 × 10⁻³` (informe, sección 12.5, ecuaciones 5–6, p. 7; protocolo, App. 1, sección 3, pp. 24–25).
6. Aplique los criterios `|a₀| < 2u(a₀)` y `|1 − a₁| < 2u(a₁)` a los resultados previos y posteriores. ¿Respaldan la conclusión de acuerdo? (informe, sección 14.1, p. 9).
7. ¿El cambio de pendiente de **0.05 %** basta por sí solo para declarar estabilidad? ¿Qué comparación de incertidumbres, covarianzas o diferencia previa/posterior sería deseable añadir? (informe, sección 16, p. 12).
8. ¿Qué elementos publicados permiten juzgar trazabilidad y comparabilidad, y cuáles quedan no reportados para una evaluación independiente completa?
