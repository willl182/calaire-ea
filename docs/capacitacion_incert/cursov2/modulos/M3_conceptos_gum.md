# M3 — Conceptos GUM: evidencia, Tipo A/B, PDFs y combinación

## 1 Ficha

- **Duración total:** 54 min: 38 min de exposición guiada, 12 min de ejercicio, 2 min de errores frecuentes y 2 min de cierre.
- **Posición en la jornada:** tercer módulo; antecede M4, donde se construye un presupuesto Tipo B para un analizador de ozono.
- **Prerrequisitos:** M1, especialmente la distinción entre incertidumbre del analizador, del patrón y del valor transferido; M2, especialmente el modelo de medición y la identificación de entradas y salida.
- **Materiales:** proyección o copia de la ficha Sabio Model 2030; tabla del ejercicio; calculadora; pizarra; handout teórico, en especial §§2.1–2.4, 3.1–3.3 y 4.1–4.4. Para autocorrelación, PDFs menos habituales y covarianza, véanse las secciones avanzadas del handout.
- **Fuentes principales:** JCGM 100:2008 / ISO/IEC Guide 98-3:2008, §§2.3, 3.2–3.3, 4.2–4.3 y 5.1–5.2; Eurachem/CITAC QUAM 2012, cap. 7, pp. editoriales 16–25, cap. 8, pp. editoriales 26–29, App. E.1, pp. editoriales 104–105, y App. G, pp. editoriales 126–131; Sabio Environmental, *Model 2030 Portable Ozone Transfer Standard*, ficha técnica de una página, 28 nov. 2023.
- **Idea fuerza:** identificar efecto y evidencia; decidir A/B; asignar PDF; convertir a estándar; declarar qué cubre; depurar duplicados; combinar.

## 2 Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **distinguir** evaluaciones Tipo A y Tipo B según el método empleado, sin confundirlas con efectos aleatorios y sistemáticos;
2. **diferenciar** la desviación estándar de una lectura, \(s\), de la incertidumbre estándar de una media, \(s/\sqrt n\);
3. **convertir** una desviación estándar o RMS, una incertidumbre expandida y límites de especificación mediante PDFs normal, rectangular o triangular cuando la información lo justifique;
4. **expresar** las contribuciones en la unidad del resultado y combinarlas en cuadratura cuando se adopta independencia;
5. **detectar** doble conteo en un presupuesto de incertidumbre de una medición de O₃.

## 3. Guion de exposición con tiempos

El libreto de exposición está organizado en páginas/diapositivas Markdown independientes. Cada página conserva el texto dictable, el minutaje y sus apoyos; este apartado funciona como índice.

1. [M3 — Página 01 — 3.1 Tipo A y Tipo B — 0:00 a 0:09; acumulado 0:09 (9 min)](../paginas/M3_01_3_1_tipo_a_y_tipo_b_0_00_a_0_09_acumulado_0_09_9_min.md)
2. [M3 — Página 02 — 3.2 Tipo A: qué representan \(s\) y \(s/\sqrt n\) — 0:09 a 0:18; acumulado 0:18 (9 min)](../paginas/M3_02_3_2_tipo_a_que_representan_s_y_s_sqrt_n_0_09_a_0_18_acumulado_0_18_9_min.md)
3. [M3 — Página 03 — 3.3 Tipo B y PDFs que reaparecen en el curso — 0:18 a 0:29; acumulado 0:29 (11 min)](../paginas/M3_03_3_3_tipo_b_y_pdfs_que_reaparecen_en_el_curso_0_18_a_0_29_acumulado_0_29_11_min.md)
4. [M3 — Página 04 — 3.4 Contribuciones, combinación cuadrática y doble conteo — 0:29 a 0:38; acumulado 0:38 (9 min)](../paginas/M3_04_3_4_contribuciones_combinacion_cuadratica_y_doble_conteo_0_29_a_0_38_acumulado_0_38_9_min.md)

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

**Enlace con la práctica:** en el Día 2 de laboratorio, `practica/E01_ruido_cero.md` convierte esta distinción en evidencia propia: la serie de 1 s y las medias de 1 min de cero permiten comparar directamente `s` con `s/√n_ef`, calcular la autocorrelación descrita en §3.2 y obtener un `u₀` experimental que M4 y E15 usan como término absoluto.
