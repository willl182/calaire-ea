# M3 — Página 02 — 3.2 Tipo A: qué representan \(s\) y \(s/\sqrt n\) — 0:09 a 0:18; acumulado 0:18 (9 min)

- **Sesión:** M3
- **Fuente:** [`modulos/M3_conceptos_gum.md`](../modulos/M3_conceptos_gum.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

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

«Los analizadores pueden aplicar filtros digitales y las lecturas cercanas pueden estar autocorrelacionadas. En ese caso, registrar cada segundo no garantiza \(n\) datos independientes. Para este módulo basta la alerta: no usar automáticamente \(s/\sqrt n\). El cálculo con tamaño efectivo, bloques o series temporales queda en el handout avanzado (ver Handout teórico, §2.4 — Autocorrelación y tamaño de muestra efectivo).»

**Conexión posterior:** M5 usa la desviación estándar muestral de pendientes e interceptos entre tres ciclos; no calcula automáticamente la incertidumbre de una media. M7 fija didácticamente \(k=2\) sin asignar grados de libertad; Welch–Satterthwaite queda como ampliación avanzada.

**Referencia integrada:** JCGM 100:2008, §§4.2.1–4.2.7. Eurachem/CITAC QUAM 2012, §§7.7–7.9, pp. editoriales 18–22 (PDF pp. 24–28), para precisión, sesgo y uso de datos experimentales. Handout teórico, §2.1 — Media, desviación estándar e incertidumbre de la media, y §2.2 — Grados de libertad; desarrollo de autocorrelación en §2.4.
