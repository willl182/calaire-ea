# M3 — Conceptos GUM: evidencia, Tipo A/B, PDFs y combinación

## 1 Ficha

- **Duración total:** 54 min: 38 min de exposición guiada, 12 min de ejercicio, 2 min de errores frecuentes y 2 min de cierre.
- **Posición en la jornada:** tercer módulo; antecede M4, donde se construye un presupuesto Tipo B para un analizador de ozono.
- **Prerrequisitos:** M1, especialmente la distinción entre incertidumbre del analizador, del patrón y del valor transferido; M2, especialmente el modelo de medición y la identificación de entradas y salida.
- **Materiales:** proyección o copia de la ficha Sabio Model 2030; tabla del ejercicio; calculadora; pizarra; handout teórico, en especial [§§2.1–2.4](../handout/gum_o3/O3_H02_evaluacion_tipo_a.md#gum-tipo-a), [§§3.1–3.3](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-info-a-distribucion) y [§§4.1–4.4](../handout/gum_o3/O3_H04_propagacion_guf.md#gum-coef-sensibilidad). Para autocorrelación, PDFs menos habituales y covarianza, véanse las secciones avanzadas del handout.
- **Fuentes principales:** JCGM 100:2008 / ISO/IEC Guide 98-3:2008, §§2.3, 3.2–3.3, 4.2–4.3 y 5.1–5.2; Eurachem/CITAC QUAM 2012, cap. 7, pp. editoriales 16–25, cap. 8, pp. editoriales 26–29, App. E.1, pp. editoriales 104–105, y App. G, pp. editoriales 126–131; Sabio Environmental, *Model 2030 Portable Ozone Transfer Standard*, ficha técnica de una página, 28 nov. 2023.
- **Idea fuerza:** identificar efecto y evidencia; decidir A/B; asignar PDF; convertir a estándar; declarar qué cubre; depurar duplicados; combinar.

## 2 Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **distinguir** evaluaciones Tipo A y Tipo B según el método empleado, sin confundirlas con efectos aleatorios y sistemáticos;
2. **diferenciar** la desviación estándar de una lectura, \(s\), de la incertidumbre estándar de una media, \(s/\sqrt n\);
3. **convertir** una desviación estándar o RMS, una incertidumbre expandida y límites de especificación mediante PDFs normal, rectangular o triangular cuando la información lo justifique;
4. **expresar** las contribuciones en la unidad del resultado y combinarlas en cuadratura cuando se adopta independencia;
5. **detectar** doble conteo en un presupuesto de incertidumbre de una medición de O₃.

## 3 Guion de exposición con tiempos

### 3.1 Tipo A y Tipo B — 0:00 a 0:09; acumulado 0:09 (9 min)

**Idea fuerza:** Tipo A y Tipo B describen cómo se evaluó una incertidumbre, no si el efecto es aleatorio o sistemático.

**Guion dictable:**

«En una red de calidad del aire recibimos información de varias formas: una serie de lecturas de O₃, una especificación del fabricante, un certificado de calibración o datos históricos de verificaciones. El GUM llama **Tipo A** a la evaluación basada en análisis estadístico de observaciones y **Tipo B** a la evaluación basada en otra información.»

«Tipo A no significa “aleatorio” y Tipo B no significa “sistemático”. Por ejemplo, la dispersión de verificaciones repetidas puede servir para evaluar mediante un método Tipo A la incertidumbre asociada a un efecto que luego tratamos como corrección. A la inversa, el ruido puede evaluarse mediante un método Tipo B si solo disponemos del RMS declarado por el fabricante.»

«La incertidumbre estándar es una desviación estándar que representa la dispersión de valores razonablemente atribuibles a una magnitud. No reemplaza una corrección conocida. Si existe un sesgo significativo y corregible, se corrige; después se evalúa la incertidumbre que permanece.»

Antes de clasificar, seleccione evidencia pertinente. QUAM cap. 7 propone considerar certificados o patrones estrechamente pertinentes; validación o estudios colaborativos; QC interno y precisión intermedia; comparaciones o ensayos de aptitud; experimentos específicos; especificaciones o literatura; modelos físicos; y juicio técnico documentado. No es una jerarquía absoluta: la evidencia elegida debe coincidir con el mensurando, intervalo, condiciones y procedimiento.

Use esta decisión operativa:

1. ¿La cifra procede del análisis estadístico de observaciones pertinentes? **Tipo A**.
2. ¿Procede de certificado, especificación, resolución, experiencia previa o literatura? **Tipo B**.
3. ¿No está claro el origen? No se asigna el tipo por intuición: se documenta la duda y se busca la fuente.

**Conexión posterior:** M4 usa manuales y un certificado, por lo que su presupuesto es principalmente Tipo B. M5 calcula desviaciones estándar entre ciclos, una evaluación Tipo A. M7 exige reconocer ambos métodos sin inferirlos de la forma de la PDF.

**Referencia integrada:** JCGM 100:2008, §§2.3.1–2.3.3 y 4.2–4.3. Eurachem/CITAC QUAM 2012, cap. 7, pp. editoriales 16–25 (PDF pp. 22–31), especialmente selección de datos disponibles. Handout teórico, [§2 — Evaluación Tipo A (introducción)](../handout/gum_o3/O3_H02_evaluacion_tipo_a.md#gum-tipo-a) y [§3.1 — De información disponible a distribución](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-info-a-distribucion).

### 3.2 Tipo A: qué representan \(s\) y \(s/\sqrt n\) — 0:09 a 0:18; acumulado 0:18 (9 min)

**Idea fuerza:** \(s\) describe la dispersión de las observaciones; \(s/\sqrt n\) describe la incertidumbre de su media bajo condiciones específicas.

**Guion dictable:**

«Supongamos que hacemos \(n\) lecturas de O₃ bajo condiciones estables. La media resume la serie y la desviación estándar experimental \(s\) describe cuánto se dispersan las lecturas individuales alrededor de esa media.»

\[
\bar{x}=\frac{1}{n}\sum_{j=1}^{n}x_j,
\qquad
s(x)=\sqrt{\frac{\sum_{j=1}^{n}(x_j-\bar{x})^2}{n-1}}.
\]

«Si el mensurando es **la media de esas \(n\) observaciones** y las observaciones pueden tratarse como independientes, la incertidumbre estándar de la media es:»

\[
u(\bar{x})=\frac{s(x)}{\sqrt n}.
\]

«No se divide por \(\sqrt n\) por el solo hecho de tener muchos datos. Primero se pregunta: ¿el resultado que se informará es una lectura o el promedio definido por el procedimiento? Segundo: ¿la serie es estable y aporta observaciones aproximadamente independientes?»

Distinga el alcance temporal y organizacional del dato: **repetibilidad de lectura** bajo condiciones cercanas; **precisión intermedia** entre días, ciclos, operadores o condiciones internas; **reproducibilidad** entre laboratorios o equipos; e **incertidumbre de la media** de observaciones independientes. No son cifras intercambiables.

Ejemplo verbal: si cinco verificaciones independientes de cero producen una desviación estándar de 0.40 nmol mol⁻¹, \(s=0.40\) nmol mol⁻¹ describe la dispersión de una verificación. Si el resultado definido es la media de las cinco, entonces \(u(\bar{x})=0.40/\sqrt5=0.18\) nmol mol⁻¹, bajo los supuestos indicados.

«Solo disminuye con \(s/\sqrt n\) el componente asociado a observaciones independientes que se promedian. Un patrón común, deriva, sesgo o corrección compartida no desaparece al aumentar \(n\).»

«Los analizadores pueden aplicar filtros digitales y las lecturas cercanas pueden estar autocorrelacionadas. En ese caso, registrar cada segundo no garantiza \(n\) datos independientes. Para este módulo basta la alerta: no usar automáticamente \(s/\sqrt n\). El cálculo con tamaño efectivo, bloques o series temporales queda en el handout avanzado (ver Handout teórico, [§2.4 — Autocorrelación y tamaño de muestra efectivo](../handout/gum_o3/O3_H02_evaluacion_tipo_a.md#gum-autocorrelacion-neff)).»

**Conexión posterior:** M5 usa la desviación estándar muestral de pendientes e interceptos entre tres ciclos; no calcula automáticamente la incertidumbre de una media. M7 fija didácticamente \(k=2\) sin asignar grados de libertad; Welch–Satterthwaite queda como ampliación avanzada.

**Referencia integrada:** JCGM 100:2008, §§4.2.1–4.2.7. Eurachem/CITAC QUAM 2012, §§7.7–7.9, pp. editoriales 18–22 (PDF pp. 24–28), para precisión, sesgo y uso de datos experimentales. Handout teórico, [§2.1 — Media, desviación estándar e incertidumbre de la media](../handout/gum_o3/O3_H02_evaluacion_tipo_a.md#gum-media-desviacion), y [§2.2 — Grados de libertad](../handout/gum_o3/O3_H02_evaluacion_tipo_a.md#gum-grados-libertad); desarrollo de autocorrelación en [§2.4](../handout/gum_o3/O3_H02_evaluacion_tipo_a.md#gum-autocorrelacion-neff).

### 3.3 Tipo B y PDFs que reaparecen en el curso — 0:18 a 0:29; acumulado 0:29 (11 min)

**Idea fuerza:** el divisor depende del significado de la información, no del nombre del componente.

**Guion dictable:**

«En Tipo B preguntamos qué afirma realmente la fuente. Para cada PDF deben quedar dos campos explícitos: **qué información factual se conoce** y **por qué la forma seleccionada la representa**. No se elige triangular porque produzca menor incertidumbre. QUAM App. E.1 y App. G reúnen conversiones y fuentes comunes como certificados, resolución, T/P y repetibilidad (App. E.1, pp. editoriales 104–105, PDF pp. 110–111; App. G, pp. editoriales 126–131, PDF pp. 132–137). ¿Entrega una desviación estándar, una incertidumbre expandida o solamente límites? La respuesta determina el tratamiento.»

#### Normal: desviación estándar, RMS o incertidumbre expandida documentada

- Si una fuente entrega una desviación estándar compatible con el mensurando, esa cifra ya es una incertidumbre estándar.
- Un ruido RMS puede conservarse como incertidumbre estándar cuando su definición, tiempo de promedio y condiciones son compatibles; no recibe por costumbre un divisor adicional.
- Si un certificado declara incertidumbre expandida \(U\) y factor de cobertura \(k\):

\[
u=\frac{U}{k}.
\]

«No se supone \(k=2\) si el certificado declara otro factor o no informa cómo se obtuvo. La palabra “normal” tampoco convierte por sí sola una fuente en Tipo A: la clasificación depende del método de evaluación.»

#### Rectangular: solo se conocen límites y no se favorecen valores internos

Si el efecto puede estar entre \(-a\) y \(+a\), y la información disponible no favorece ninguna zona del intervalo:

\[
u=\frac{a}{\sqrt3}.
\]

Ejemplos del contexto O₃: deriva declarada como límite, linealidad \(\pm1\%\) de escala completa o error de redondeo dentro de medio incremento digital, siempre que esa interpretación corresponda a la fuente.

«Antes de dividir, convierta el límite a la unidad del resultado. En una escala completa de 200 ppb, \(\pm1\%\) FS significa \(a=2\) ppb. En un punto seleccionado de 120 ppb, \(\pm1\%\) del setpoint significa \(a=1.2\) ppb. No son la misma especificación.»

#### Triangular: los valores cercanos al centro son más plausibles

Si existen límites \(-a\) y \(+a\), pero además hay fundamento para considerar más probables los valores cercanos al centro:

\[
u=\frac{a}{\sqrt6}.
\]

«La triangular no se elige para obtener un valor menor que con la rectangular. Se usa solo cuando la evidencia o el mecanismo justifican ese mayor peso central. Reaparece en M7, donde el presupuesto publicado del fotómetro asigna una PDF triangular a la repetibilidad del cociente de intensidades; allí se respeta la distribución publicada.»

Resumen para la pizarra:

| Información disponible | Tratamiento habitual, si está justificado |
|---|---|
| Desviación estándar o RMS compatible | \(u=s\) o \(u=\mathrm{RMS}\) |
| Incertidumbre expandida con \(k\) | \(u=U/k\) |
| Límites \(\pm a\), valores igualmente plausibles | rectangular: \(u=a/\sqrt3\) |
| Límites \(\pm a\), centro más plausible | triangular: \(u=a/\sqrt6\) |

«Las PDFs arcoseno y trapezoidal no se necesitan para resolver M4, M5 ni el ejercicio principal de M7. Se mencionan para reconocer que existen; sus mecanismos, fórmulas y ejemplos quedan en el handout avanzado (Handout teórico, [§3.6 — Distribución arcoseno o en U](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-pdf-arcoseno), y [§3.7 — Trapecio curvilíneo para límites inexactos](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-pdf-trapecio)).»

**Referencia integrada:** JCGM 100:2008, §§4.3.1–4.3.9. Handout teórico, [§3.1 — De información disponible a distribución](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-info-a-distribucion), [§3.2 — Distribución rectangular](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-pdf-rectangular), [§3.3 — Distribución normal](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-pdf-normal) y [§3.4 — Distribución triangular](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-pdf-triangular); ejemplo desarrollado en [§3.8](../handout/gum_o3/O3_H03_tipo_b_pdfs.md#gum-ejemplo-tipo-b).

### 3.4 Contribuciones, combinación cuadrática y doble conteo — 0:29 a 0:38; acumulado 0:38 (9 min)

**Idea fuerza:** primero se expresan todas las contribuciones en la unidad del resultado; después se combinan una sola vez.

**Guion dictable:**

«Una incertidumbre de entrada no entra al presupuesto solo por estar expresada como desviación estándar. Debemos saber cuánto cambia el resultado cuando cambia esa entrada. Para un modelo \(Y=f(X_1,\ldots,X_N)\), el coeficiente de sensibilidad es:»

\[
c_i=\frac{\partial f}{\partial X_i},
\qquad
u_i(y)=|c_i|u(x_i).
\]

«En muchos presupuestos operativos de O₃, las entradas ya se convierten a ppb o nmol mol⁻¹ equivalentes y entonces \(c_i=1\). En M7, en cambio, la sensibilidad de la pendiente de una recta es el nivel \(x\); por eso su contribución aumenta para el nivel alto.»

Si las contribuciones pueden tratarse como independientes:

\[
u_c(y)=\sqrt{\sum_i [c_i u(x_i)]^2}.
\]

Ejemplo breve para la pizarra: si dos contribuciones independientes son 0.6 y 0.8 nmol mol⁻¹,

\[
u_c=\sqrt{0.6^2+0.8^2}=1.0\ \mathrm{nmol\ mol^{-1}},
\]

no 1.4 nmol mol⁻¹.

«La combinación cuadrática no corrige un modelo incompleto. Una cifra global debe declarar su **cobertura**. Por ejemplo, la precisión intermedia obtenida durante meses puede cubrir ruido, recalibración, operador, parte del ambiente y variación del equipo. Esas ramas no se añaden otra vez sin demostrar qué fracción queda fuera. La incertidumbre del patrón o las pérdidas de línea pueden permanecer externas y sumarse si no están cubiertas.»

«La combinación cuadrática no corrige un modelo incompleto. Antes de calcular, revise el **doble conteo**: cada fila debe representar un efecto identificable y aparecer una sola vez. Si un certificado ya incluye repetibilidad o condiciones ambientales, no se agregan otra vez sin una desagregación coherente. Si la repetibilidad observada ya contiene la resolución, una fila adicional de resolución puede duplicar parte de la variación.»

Use esta lista por fila:

1. ¿Qué mecanismo representa?
2. ¿Qué evidencia lo cuantifica?
3. ¿Qué periodo y condiciones cubre?
4. ¿Cómo se convierte a incertidumbre estándar y a la unidad de salida?
5. ¿Qué ramas ya están cubiertas por esa cifra?
6. ¿Qué dependencia existe con otras entradas?

«La fórmula anterior supone independencia. Las entradas que comparten patrón, calibración o datos pueden requerir covarianza. Como el cálculo explícito de covarianza aparece recién en M7, aquí queda como alerta: no imponer independencia si se conoce una fuente compartida. El desarrollo y los términos cruzados se consultan en el handout avanzado (Handout teórico, [§4.2 — Ley de propagación de incertidumbre](../handout/gum_o3/O3_H04_propagacion_guf.md#gum-ley-propagacion)) y se trabajan en M7.»

**Referencia integrada:** JCGM 100:2008, §§5.1–5.2 y advertencia de doble conteo en §4.3.10. Eurachem/CITAC QUAM 2012, caps. 7–8, pp. editoriales 16–29 (PDF pp. 22–35), y ejemplo A4, pp. editoriales 60–71 (PDF pp. 66–77), para agrupación de precisión, sesgo y fuentes externas. Handout teórico, [§4.1 — Coeficientes de sensibilidad](../handout/gum_o3/O3_H04_propagacion_guf.md#gum-coef-sensibilidad), [§4.2 — Ley de propagación de incertidumbre](../handout/gum_o3/O3_H04_propagacion_guf.md#gum-ley-propagacion) y [§4.3 — Doble conteo: GUM §4.3.10](../handout/gum_o3/O3_H04_propagacion_guf.md#gum-doble-conteo).

## 4 Ejercicio/actividad — 0:38 a 0:50; acumulado 0:50 (12 min)

### Conversión y combinación de especificaciones del Sabio Model 2030

**Organización:** parejas; 9 min de trabajo y 3 min de puesta en común.

**Enunciado listo para entregar:** A partir de la ficha Sabio Model 2030, complete la tabla. Para cada componente, indique el método Tipo A/B, la PDF o interpretación, el límite absoluto cuando corresponda y la incertidumbre estándar en ppb. Luego combine las cuatro contribuciones en cuadratura, suponiendo independencia y \(c_i=1\). Finalmente, escriba una advertencia de una línea sobre posible doble conteo o falta de evidencia y responda la pregunta de cobertura.

**Datos:**

- ruido de cero: **0.6 ppb RMS**;
- deriva límite de cero: **<1.0 ppb/24 h**;
- linealidad: **±1 % de escala completa (FS)**;
- exactitud del generador: **±1 % del punto seleccionado (setpoint)**;
- rango asignado: **0–200 ppb**;
- punto seleccionado: **120 ppb**.

| Componente | Información original | Tipo A/B | PDF o interpretación | Conversión a \(u\) estándar | \(u\) (ppb) | ¿Cubierta por otra cifra? |
|---|---|---|---|---|---:|---|
| Ruido | 0.6 ppb RMS |  |  |  |  |  |
| Deriva de cero | <1.0 ppb/24 h |  |  |  |  |  |
| Linealidad | ±1 % FS; FS = 200 ppb |  |  |  |  |  |
| Generador | ±1 % setpoint; setpoint = 120 ppb |  |  |  |  |  |

\[
u_c=\sqrt{u_{ruido}^2+u_{deriva}^2+u_{linealidad}^2+u_{generador}^2}.
\]

**Pregunta final:** si se dispusiera de una cifra de precisión intermedia de verificaciones que incluyera ruido y deriva, ¿qué filas no podrían mantenerse automáticamente? No recalcule el total para ese escenario; identifique cobertura y evidencia faltante.

**Supuestos didácticos:** trate el RMS como incertidumbre estándar bajo condiciones compatibles; trate los tres límites como rectangulares; use las especificaciones como evaluaciones Tipo B. La independencia se adopta solo para practicar la combinación y debe revisarse en un presupuesto real.

**Resultado esperado:** cuatro conversiones justificadas, un total combinado con unidad y una advertencia como: «Antes de aceptar el total, debe comprobarse si ruido, linealidad o exactitud del generador se solapan y si las condiciones de la ficha corresponden al uso real». No se exige incertidumbre expandida ni covarianza.

## 5 Errores frecuentes y preguntas típicas — 0:50 a 0:52; acumulado 0:52 (2 min)

1. **“Tipo A significa aleatorio y Tipo B sistemático”.** No; clasifican el método de evaluación.
2. **Dividir todo por \(\sqrt3\).** Solo se usa para límites modelados con PDF rectangular; un RMS compatible ya puede ser una incertidumbre estándar.
3. **Dividir por \(\sqrt n\) sin definir el resultado.** Solo corresponde a la media de \(n\) observaciones aproximadamente independientes bajo condiciones estables.
4. **Confundir 1 % FS con 1 % de la lectura.** FS se aplica a la escala completa; el porcentaje del setpoint se aplica al valor seleccionado.
5. **Sumar incertidumbres estándar linealmente.** Las contribuciones independientes se combinan en cuadratura.
6. **Agregar todas las cifras disponibles.** Primero se revisa si dos filas describen el mismo efecto o si una ya está incluida en el certificado.
7. **Tomar una prueba de sesgo no significativa como prueba de sesgo cero.** Ausencia de significancia no demuestra ausencia de sesgo.
8. **Dividir una precisión global en fuentes ficticiamente independientes.** Mantenga agrupación y cobertura observadas.
9. **Elegir la especificación más conservadora sin comprobar pertinencia.** Conservadurismo no corrige incompatibilidad de condiciones.
10. **Incluir una falla o equivocación como incertidumbre.** Investigue y controle operación inválida.

## 6 Cierre y transición — 0:52 a 0:54; acumulado 0:54 (2 min)

Pida al grupo repetir la secuencia en voz alta: **identificar efecto y evidencia; decidir A/B; asignar PDF; convertir a estándar; declarar qué cubre; depurar duplicados; combinar si la independencia es defendible**.

En M4 se aplicará esta secuencia a ruido RMS, límites rectangulares e incertidumbre expandida de un certificado en un presupuesto Tipo B de un analizador de O₃. M5 reutilizará la desviación estándar para comparar ciclos. M7 retomará la triangular publicada, las sensibilidades del modelo y, ya de forma explícita, la covarianza.
<<<<<<< Updated upstream
=======

**Enlace con la práctica:** en la práctica de laboratorio complementaria, `practica/E01_ruido_cero.md` convierte esta distinción en evidencia propia: la serie de 1 s y las medias de 1 min de cero permiten comparar directamente `s` con `s/√n_ef`, calcular la autocorrelación descrita en §3.2 y obtener un `u₀` experimental que M4 y E15 usan como término absoluto.
>>>>>>> Stashed changes
