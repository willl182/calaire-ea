# M4 — Presupuesto de incertidumbre del analizador O₃

## 1 Ficha

**Duración:** 1 h 22 min (82 min).

**Posición en la jornada:** cuarto módulo, después de M3 — Conceptos GUM: Tipo A/B, PDFs y combinación. Precede a M5 — Patrones de transferencia: calibración multipunto, deriva y verificación.

**Propósito:** construir y auditar un presupuesto documental Tipo B como primera iteración para un analizador de ozono a 120 nmol/mol, a partir de especificaciones de fabricante y otras fuentes documentales, y definir un plan de sustitución por evidencia experimental hasta obtener un presupuesto híbrido.

**Prerrequisitos:**

- distinguir evaluación Tipo A y Tipo B;
- convertir límites e incertidumbres expandidas a incertidumbres estándar;
- reconocer distribuciones normal y rectangular;
- aplicar combinación en cuadratura para componentes independientes;
- interpretar coeficientes de sensibilidad y participación en la varianza.

**Materiales:**

1. `cursov2/plantillas/plantilla_presupuesto.R`, caso 1;
2. Thermo Fisher Scientific, *Model 49i Instruction Manual*, Table 1-1 y cap. 4;
3. HORIBA, *APOA-370 Operation Manual*, §10.2;
4. `cursov2/handout/handout_teorico_gum_o3.md`, §§3.1–3.3 y 4.2–4.4;
5. `evaluation and uncertainty budget of ozone.md`, utilizada únicamente como **fuente secundaria** para la estructura de presupuestos tipo EN 14625;
6. calculadora o entorno R y una hoja para registrar fuente, interpretación, PDF, divisor, alcance de evidencia y contribución;
7. Eurachem/CITAC QUAM 2012, cap. 6, pp. editoriales 14–15; App. C, p. editorial 101; App. D, pp. editoriales 102–103; App. E.5, pp. editoriales 117–120; App. F, pp. editoriales 121–125; App. G, pp. editoriales 126–131.

**Distribución del tiempo:** exposición, 43 min; ejercicio central, 31 min; errores frecuentes y preguntas, 4 min; cierre y transición, 4 min. Total: 82 min.

## 2 Objetivos específicos

Al finalizar el módulo, el participante podrá:

1. **identificar** en una ficha técnica al menos cuatro especificaciones relevantes para un presupuesto de incertidumbre;
2. **convertir** ruido RMS, límites bilaterales e incertidumbre expandida en incertidumbres estándar con una PDF justificada;
3. **calcular** la incertidumbre estándar combinada de un presupuesto Tipo B con componentes independientes;
4. **ordenar** las fuentes según su contribución a la varianza e indicar cuáles requieren evidencia experimental propia;
5. **comparar** especificaciones del Thermo 49i y del APOA-370 sin equiparar magnitudes, periodos o condiciones diferentes;
6. **construir** un diagrama causal depurado y enlazar cada fila con un mecanismo;
7. **marcar** la cobertura de cada dato global y la calidad metrológica de su evidencia;
8. **expresar** incertidumbre como función del nivel y diseñar una versión híbrida futura con QC.

## 3. Guion de exposición con tiempos

El libreto de exposición está organizado en páginas/diapositivas Markdown independientes. Cada página conserva el texto dictable, el minutaje y sus apoyos; este apartado funciona como índice.

1. [M4 — Página 01 — 3.0 Del proceso al presupuesto — 0:00 a 0:06; acumulado 0:06 (6 min)](../paginas/M4_01_3_0_del_proceso_al_presupuesto_0_00_a_0_06_acumulado_0_06_6_min.md)
2. [M4 — Página 02 — 3.1 Del dato documental a la fila del presupuesto — 0:06 a 0:16; acumulado 0:16 (10 min)](../paginas/M4_02_3_1_del_dato_documental_a_la_fila_del_presupuesto_0_06_a_0_16_acumulado_0_16_10_min.md)
3. [M4 — Página 03 — 3.2 Combinación, clasificación y doble conteo — 0:16 a 0:26; acumulado 0:26 (10 min)](../paginas/M4_03_3_2_combinacion_clasificacion_y_doble_conteo_0_16_a_0_26_acumulado_0_26_10_min.md)
4. [M4 — Página 04 — 3.3 Lectura crítica del Thermo 49i — 0:26 a 0:35; acumulado 0:35 (9 min)](../paginas/M4_04_3_3_lectura_critica_del_thermo_49i_0_26_a_0_35_acumulado_0_35_9_min.md)
5. [M4 — Página 05 — 3.4 Comparación con APOA-370 y presupuestos de laboratorio/campo — 0:35 a 0:43; acumulado 0:43 (8 min)](../paginas/M4_05_3_4_comparacion_con_apoa_370_y_presupuestos_de_laboratorio_campo_0_35_a_0_43_acumulado_0_43_8_min.md)

## 4 Ejercicio/actividad

### Presupuesto Tipo B del Thermo 49i y comparación con APOA-370 — 0:43 a 1:14; acumulado 1:14 (31 min)

**Apoyo en el handout:** ver Handout teórico, §3.8 — Ejemplo Tipo B con especificación genérica, como modelo de conversión de una especificación a incertidumbre estándar, y §4.4 — Presupuesto y contribuciones, para la estructura de la tabla y la clasificación.

**Organización:** parejas; una persona opera la plantilla y la otra verifica manual y trazabilidad. Intercambian funciones a mitad del ejercicio.

**Datos del caso 1 a 120 nmol/mol:** ruido RMS 0.25 ppb, normal con divisor 1; deriva de cero en 24 h con límite 1.0 ppb, rectangular; deriva de span precargada como 1 % de 120 ppb, rectangular, pero marcada para auditoría frente al periodo mensual del manual; linealidad 1 % de escala completa de 200 ppb, rectangular; efecto de presión equivalente 0.36 ppb, rectangular y con fuente pendiente; resolución 0.1 ppb tratada como semiancho 0.05 ppb, rectangular y con fuente pendiente; certificado de calibración con \(U=1.8\) ppb y \(k=2\), con fuente pendiente. Use \(c_i=1\), independencia y grados de libertad infinitos para este ejercicio Tipo B.

**Secuencia de trabajo:**

1. **0:43–0:49:** registre cada componente, valor, unidad, PDF, divisor, fuente declarada y alcance/cobertura de evidencia.
2. **0:49–0:57:** convierta las entradas a incertidumbres estándar y ejecute el caso 1 de `plantilla_presupuesto.R`.
3. **0:57–1:03:** compruebe combinación en cuadratura y ordene componentes por contribución, sin confundir clasificación matemática con validez metrológica.
4. **1:03–1:09:** audite las filas contra Thermo Table 1-1: clasifique como verificada, interpretación no respaldada o fuente adicional requerida.
5. **1:09–1:14:** compare semicuantitativamente con APOA-370 a escala completa de 200 ppb. Incluya linealidad, reproducibilidad, deriva diaria de cero y span y detección a dos sigma; no calcule un total del APOA ni sume posibles componentes solapados.

**Productos:**

1. tabla completa del caso 1, total combinado, incertidumbre expandida, clasificación matemática y clasificación de evidencia;
2. diagrama causal de una página, con cada fila enlazada a una rama y cada vacío marcado;
3. auditoría de procedencia y párrafo de comparación prudente con APOA-370;
4. plan de reemplazo de tres filas por evidencia propia, ejecutado en el Día 2 de laboratorio con protocolos concretos: ruido/deriva mediante `practica/E01_ruido_cero.md` y `practica/E08_deriva_cero_span.md` (E08 debe iniciarse ≥7 días antes, ver `practica/P0_agenda_dia2.md`), linealidad/falta de ajuste mediante verificación multipunto y residual en `practica/E02_verificacion_multipunto.md`, y pérdidas de línea mediante `practica/E06_transmision_linea.md`; la presión mediante calibración del sensor y diferencia sensor–celda queda documentada como vacío en `practica/E14_recorrido_documental.md` cuando no exista puerto de acceso aprobado;
5. dos salidas conceptuales, sin recalcular: presupuesto actual bottom-up documental y futuro presupuesto híbrido con \(u_{PI}\), patrón y fuentes externas no cubiertas.

Para el presupuesto híbrido use como regla: si la precisión intermedia ya contiene día, operador, recalibración, ambiente y equipo, no añada esas ramas otra vez. Documente cobertura y conserve solo mecanismos externos o no representados (QUAM cap. 7, pp. editoriales 16–25; ejemplo A4, pp. editoriales 60–71; PDF pp. 22–31 y 66–77).

**Resultado esperado, en una línea:** el caso 1 ejecutado sin modificar debe dar aproximadamente \(u_c=1.75\) ppb, \(U=3.50\) ppb con \(k=2\) exacto (\(gl=\infty\)) y \(W=2.9\%\), acompañado de la advertencia de que la deriva de span está mal periodizada frente al manual y tres entradas requieren una fuente adicional.

## 5 Errores frecuentes y preguntas típicas

### 1:14 a 1:18; acumulado 1:18 (4 min)

**Errores frecuentes:**

- tratar todo límite como incertidumbre estándar sin aplicar divisor;
- leer “1 %” sin indicar si corresponde a lectura o escala completa;
- cambiar “por mes” a “por día” para acomodar la plantilla;
- sumar detección, ruido y reproducibilidad como componentes independientes sin revisar solapamiento;
- atribuir al manual cifras que proceden de un certificado, supuesto o cálculo auxiliar;
- interpretar el primer lugar de la clasificación como prueba de que la fuente está correctamente modelada.

**Preguntas típicas y respuestas cortas:**

1. **¿RMS siempre equivale a incertidumbre estándar?** Solo cuando la definición, el promedio y las condiciones son compatibles con el mensurando.
2. **¿Una especificación “±a” siempre usa rectangular?** No; rectangular es defendible cuando solo se conocen límites y no hay información que favorezca valores internos.
3. **¿Puede usarse la deriva mensual para un resultado diario?** Solo mediante un modelo temporal explícito y evidencia; no cambiando la etiqueta.
4. **¿El componente mayor es siempre el primero que debe reducirse?** No; primero se verifica que sea válido, independiente y pertinente.
5. **¿Por qué no calculamos una incertidumbre total del APOA-370?** Porque la ficha no define por sí sola un presupuesto completo ni resuelve solapamientos y condiciones de uso.

## 6 Dependencia con el nivel y cierre

### 1:18 a 1:22; acumulado 1:22 (4 min)

QUAM App. E.5 y ejemplo A6 expresan una incertidumbre dependiente del nivel como

\[
u(c)=\sqrt{u_0^2+(u_r c)^2},
\]

donde \(u_0\) reúne términos absolutos como cero, ruido, resolución o residual, y \(u_r c\) reúne escala, patrón, pendiente y T/P relativas. Sin recalcular el caso 1, identifique cualitativamente qué término dominaría a 10, 120 y 180 nmol mol⁻¹. Cerca de cero suele dominar el término constante; a niveles altos, el proporcional. Fuente: QUAM App. E.5, pp. editoriales 117–120 (PDF pp. 123–126), y ejemplo A6, pp. editoriales 81–88 (PDF pp. 87–94).

Para el ejercicio de esta sección, `k=2` es un valor exacto convencional (grados de libertad efectivos infinitos, `gl=Inf`), no una aproximación "≈2"; Welch–Satterthwaite queda para material avanzado cuando existan grados de libertad finitos documentados.

**Enlace con la práctica:** el presupuesto híbrido cualitativo descrito aquí se calcula con datos reales en `practica/E15_presupuesto_hibrido.md`, que integra E01/E09 (u₀), E02 (u_r y residual), E06 (transmisión) y E08 (deriva) sin doble conteo. Ese experimento pertenece al Día 2 de laboratorio y es independiente del ejercicio documental de este módulo: ninguno reemplaza al otro.

> **Alerta cerca de cero.** La incertidumbre relativa puede crecer sin límite útil, un intervalo simétrico puede incluir valores físicamente imposibles y detección, cuantificación, estimación y decisión no son equivalentes. El análisis numérico queda para material avanzado. Fuente: QUAM App. F, pp. editoriales 121–125 (PDF pp. 127–131).

### Cierre

Un presupuesto defendible comienza con lectura crítica, definición del efecto y trazabilidad de cada entrada; el cálculo y la clasificación vienen después. El caso mostró qué puede obtenerse de especificaciones y, sobre todo, qué debe reemplazarse con calibraciones y verificaciones propias. En M5 se desarrollará esa evidencia mediante calibración multipunto, análisis de falta de ajuste, deriva y verificación de patrones de transferencia.
