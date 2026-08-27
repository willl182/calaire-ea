# M5 — Patrones de transferencia: calibración multipunto, deriva y verificación

## 1. Ficha

- **Duración:** 68 min.
- **Posición en el curso:** módulo 5 del recorrido obligatorio; sigue al presupuesto de incertidumbre del analizador y precede al módulo obligatorio M6 sobre NO/NO₂/NOₓ. El taller integrador corresponde a M7.
- **Prerrequisitos:** M1–M4. La persona participante debe reconocer la cadena de trazabilidad del ozono, interpretar un modelo de medición, distinguir evaluaciones Tipo A y Tipo B, y comprender incertidumbre estándar, sensibilidad y presupuesto de incertidumbre.
- **Materiales:** proyector o pantalla; calculadora, hoja de cálculo o software estadístico; `cursov2/datasets/dataset_verificacion_multipunto.csv`; `cursov2/datasets/dataset_metadata.md`; certificado simulado incluido en el enunciado; hoja o archivo para registrar regresión, diferencias y residuos.
- **Fuentes principales:** USEPA P1016Y93, §§4–5 y App. A; USEPA, *SOP for Calibrators*, §12; CARB, *Performance Audits Using a Portable Ozone Transfer Standard*, v5, App. C, §§C.7–C.9; JCGM GUM-6:2020, §10.6; USEPA, *Quality Assurance Handbook for Air Pollution Measurement Systems*, vol. II, §12.4.
- **Idea fuerza:** verificar no es ajustar hasta obtener coincidencia; es conservar el estado encontrado y obtener evidencia de que la relación metrológica permanece aceptable bajo un criterio declarado.

## 2. Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **Distinguir** calibración, verificación, reverificación y ajuste, explicando qué evidencia se pierde cuando se interviene el instrumento antes de registrar su estado encontrado.
2. **Corregir** la indicación de una referencia mediante la pendiente y el intercepto de su certificado, conservando por separado los datos originales y los valores corregidos.
3. **Calcular e interpretar** diferencias por punto, pendiente, intercepto y residuos para cada ciclo de una comparación multipunto.
4. **Evaluar** la estabilidad entre tres ciclos mediante la dispersión de pendientes e interceptos y reconocer indicios de deriva, curvatura o estabilización insuficiente.
5. **Emitir y documentar** una decisión de conformidad según límites explícitos, identificando el requisito decisivo y una comprobación técnica previa a cualquier ajuste.
6. **Evaluar** qué componentes cubren la regresión, el residual y la repetición entre ciclos.
7. **Separar** datos de validación o verificación usados para conformidad de aquellos usados para cuantificar incertidumbre.
8. **Reconocer** incertidumbre de predicción, dependencia con nivel y ramas no cubiertas por el ajuste.

## 3. Guion de exposición con tiempos

El libreto de exposición está organizado en páginas/diapositivas Markdown independientes. Cada página conserva el texto dictable, el minutaje y sus apoyos; este apartado funciona como índice.

1. [M5 — Página 01 — Bloque 0–8 min — Verificación, calibración y estado encontrado.](../paginas/M5_01_bloque_08_min_verificacion_calibracion_y_estado_encontrado.md)
2. [M5 — Página 02 — Bloque 8–18 min — Diseño de una comparación multipunto.](../paginas/M5_02_bloque_818_min_diseno_de_una_comparacion_multipunto.md)
3. [M5 — Página 03 — Bloque 18–28 min — Corrección por certificado, regresión y residuos.](../paginas/M5_03_bloque_1828_min_correccion_por_certificado_regresion_y_residuos.md)
4. [M5 — Página 04 — Bloque 28–38 min — Estabilidad, deriva y decisión de ajustar.](../paginas/M5_04_bloque_2838_min_estabilidad_deriva_y_decision_de_ajustar.md)
5. [M5 — Página 05 — Bloque 60–68 min — Puesta en común y síntesis posterior al ejercicio.](../paginas/M5_05_bloque_6068_min_puesta_en_comun_y_sintesis_posterior_al_ejercicio.md)

## 4. Ejercicio/actividad

**Duración total: 22 min (acumulado: 38–60 min).**

**Enunciado.** Trabajen en parejas con `cursov2/datasets/dataset_verificacion_multipunto.csv`. El archivo contiene tres ciclos de verificación. Cada ciclo presenta cero previo, seis niveles cercanos a 20, 40, 70, 100, 140 y 180 ppb, y cero posterior. Las columnas relevantes son `ciclo`, `punto`, `nivel_nominal`, `lectura_ref`, `lectura_uut`, `T_celda_K`, `P_celda_kPa` y `flujo_L_min`.

El certificado simulado de la referencia establece:

- pendiente \(m=1.003\);
- intercepto \(b=-0.4\ \text{ppb}\);
- corrección \(X=(\text{lectura\_ref}-b)/m\);
- incertidumbre expandida \(U(X)=0.5\ \text{ppb}+0.01X\), con \(k=2\).

**Trabajo de cálculo, 8 min (38–46 min).** Conserven `lectura_ref` y creen una columna para \(X\). Para cada fila calculen \(d=\text{lectura\_uut}-X\). Para cada ciclo ajusten `lectura_uut = intercepto + pendiente × X` usando ceros y niveles, calculen residuos y registren pendiente, intercepto, residuo de mayor magnitud, cero previo y cero posterior. No calculen diferencia porcentual cuando \(X=0\).

**Trabajo de evaluación, 14 min (46–60 min).** Apliquen el siguiente **criterio de conformidad didáctico, fijado antes del análisis**:

- para cada punto con \(X\le50\ \text{ppb}\): \(|d|\le1.5\ \text{ppb}\);
- para cada punto con \(X>50\ \text{ppb}\): \(|100d/X|\le3.1\%\);
- pendiente de cada ciclo entre 0.97 y 1.03;
- intercepto de cada ciclo entre −3 y +3 ppb;
- desviación estándar de las tres pendientes menor que 0.0075;
- desviación estándar de los tres interceptos menor que 1.00 ppb.

Los límites reproducen con finalidad formativa P1016Y93 §4.4.1 y App. A. La incertidumbre expandida del certificado no se sumará a los límites: el ejercicio usa una regla binaria simple. Para un uso real, el sistema de calidad debe definir la regla de decisión y el tratamiento del riesgo.

Entreguen una tabla de tres filas, una por ciclo, con pendiente, intercepto, máxima diferencia y máxima magnitud de residuo. Añadan una **matriz de cobertura**:

| Dato | Fuente que puede cuantificar | Qué cubre | Qué no cubre |
|---|---|---|---|
| Residuos dentro de ciclo | Regresión | Dispersión/falta de ajuste local | Patrón, largo plazo |
| Variación entre ciclos | Tres ciclos | Estabilidad corta | Deriva entre meses |
| Certificado | Calibración superior | Valor de referencia declarado | Montaje local si no está incluido |
| Ceros pre/post | Verificación | Cambio aditivo corto | Pendiente o interferencias |

Para cada fila confirme o corrija la cobertura propuesta según condiciones reales. No construya un presupuesto completo en este módulo. Añadan una conclusión de máximo 100 palabras: **conforme** o **no conforme**, requisito decisivo, patrón visible en los residuos y una comprobación técnica previa a cualquier ajuste. No se solicita solución numérica desarrollada.

**Resultado esperado:** decisión de conformidad trazable, sustentada en valores de referencia corregidos, requisitos por punto y por ciclo, estabilidad entre ciclos e inspección de residuos.

**Bloque 60–68 min — Puesta en común y síntesis posterior al ejercicio.**

Solicite a dos grupos que comuniquen únicamente cuatro elementos: decisión, requisito decisivo, patrón de residuos y comprobación previa al ajuste. Contraste datos, criterio, interpretación y acción: los datos muestran; el criterio clasifica; la interpretación propone causas; el procedimiento autoriza acciones. Una causa posible no debe escribirse como hecho confirmado.

Cierre el bloque con la secuencia de baja fricción: **corregir la referencia, conservar los originales, evaluar todos los puntos y ciclos, inspeccionar residuos, aplicar el criterio predefinido y documentar antes de intervenir**. P1016Y93 resume el deber documental: “Ensure all documentation is complete and all records are saved to the appropriate data storage system” (§5.1, p. física 40).

## 5. Errores frecuentes y preguntas típicas

1. **¿Puedo usar `lectura_ref` directamente?** No. Debe aplicarse la ecuación del certificado y conservar tanto la indicación original como el valor corregido.
2. **¿Una pendiente aceptable demuestra conformidad?** No. También deben cumplir intercepto, diferencias por punto, estabilidad entre ciclos y cualquier otro requisito declarado.
3. **¿Un coeficiente de determinación cercano a uno elimina la necesidad de revisar residuos?** No. Puede coexistir con sesgo proporcional, desplazamiento o curvatura sistemática.
4. **¿Si un punto falla debo ajustar inmediatamente?** No. Primero se revisan estabilidad, montaje, aire cero, flujo, presión, tubería, certificado, transcripción y estado de ambos instrumentos.
5. **¿La deriva es simplemente la diferencia entre cero previo y cero posterior?** No. Esa diferencia es un diagnóstico de corto plazo; la deriva también puede afectar la pendiente y requiere una historia temporal para caracterizarse.

Errores frecuentes adicionales: usar límites de conformidad como incertidumbre estándar; tratar residual, repetibilidad y precisión intermedia como independientes sin revisar inclusión; reducir un componente común al aumentar puntos; usar regresión fuera del intervalo calibrado; asumir que incertidumbre del patrón está incluida en OLS; sobrescribir datos originales, mezclar niveles de ciclos distintos en una única regresión, calcular porcentajes cerca de cero, eliminar un punto sin causa técnica documentada, redondear antes de decidir y presentar una hipótesis causal como conclusión comprobada.

## 6. Cierre y transición

Una verificación defendible conserva el estado encontrado, aplica las correcciones vigentes, evalúa puntos, regresión, residuos y estabilidad, y documenta la decisión antes de cualquier intervención. El módulo M6 transfiere esta disciplina a NO/NO₂/NOₓ; el taller integrador M7 cierra el recorrido obligatorio con un presupuesto y un informe auditables. Monte Carlo queda como M8 opcional y material avanzado.

**Enlace con la práctica:** en el Día 2 de laboratorio, `practica/E02_verificacion_multipunto.md` ejecuta exactamente este diseño de tres ciclos (ascendente, descendente, pseudoaleatorio) con instrumento real, produce `u_pred`, `s_pooled`/ANOVA y la matriz de cobertura que este módulo describe de forma documental. `practica/E11_tiempo_respuesta.md` valida además la espera mínima usada antes de registrar cada punto.
