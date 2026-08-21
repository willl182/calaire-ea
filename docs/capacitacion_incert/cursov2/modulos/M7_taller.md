# M7 — Taller integrador: presupuesto, validación y reporte

## 1. Ficha

- **Duración:** 85 min.
- **Posición en el curso:** módulo 7 de 7 del recorrido obligatorio; cierre integrador de la jornada de 9 h. M6 NOx se desarrolla antes del taller. M8 Monte Carlo queda como material avanzado opcional fuera de la jornada.
- **Prerrequisitos:** M1–M6; definición de mensurando; evaluaciones Tipo A y Tipo B; conversión a incertidumbres estándar; coeficientes de sensibilidad; ley de propagación GUM; dependencia y covarianza; incertidumbre combinada y expandida; lectura básica de regresión lineal; modelo diferencial NO₂ = NOx − NO visto en M6.
- **Materiales:** `cursov2/casos/extracto_kriss_2024.md`; BIPM.QM-K1 protocol v2.1, App. 1; presupuesto parcialmente resuelto; computador con calculadora u hoja de cálculo; lista combinada GUM §7 + QUAM cap. 9.
- **Modalidad:** trabajo en equipos de dos o tres personas, seguido de revisión cruzada.
- **Entregable:** presupuesto completado, declaración de resultado, propuesta de validación externa, frase de alcance y respuesta breve de transferencia del método a NOx.
- **Nivel de trabajo:** 100 nmol mol⁻¹.
- **Fuentes de los datos:** resultados públicos de BIPM y KRISS. No se emplean datos operativos de organizaciones, redes o esquemas externos.

El mensurando es la fracción de cantidad de sustancia de ozono en aire seco, expresada en mol mol⁻¹ o sus múltiplos. Aunque el valor numérico en nmol mol⁻¹ coincide con ppb, el protocolo indica que ppb y ppbv no son unidades recomendadas (BIPM.QM-K1 protocol v2.1, §4, p. 3). Durante el taller se utiliza **nmol mol⁻¹**.

El Apéndice 1 del protocolo comienza en la página 21 de 25. La tabla del presupuesto ocupa las pp. 21–22, la expresión simplificada se deriva en las pp. 22–23 y los términos de covarianza se desarrollan en las pp. 24–25.

## 2. Objetivos específicos

Al finalizar los 85 minutos, cada participante podrá:

1. **Reconocer** las contribuciones del presupuesto fotométrico de BIPM-SRP27 y relacionarlas con la expresión simplificada de \(u(x)\).
2. **Completar** un presupuesto parcialmente resuelto para la relación KRISS-SRP5/BIPM-SRP27 a 100 nmol mol⁻¹.
3. **Propagar** \(u(x)\), \(u(a_0)\), \(u(a_1)\) y la covarianza entre intercepto y pendiente, conservando el signo del término cruzado.
4. **Calcular** \(u_c(y)\) y \(U=2u_c(y)\), justificando brevemente el uso didáctico de \(k=2\).
5. **Completar** flujo QUAM/GUM: especificar, identificar, cuantificar, depurar, combinar, expandir, informar y revisar.
6. **Interpretar y redactar** resultado auditable conforme a GUM §7 y QUAM cap. 9, con mensurando, modelo, estimación, unidad, cobertura, fuentes, condiciones, alcance y limitaciones.
7. **Proponer** validación externa del presupuesto y transferir en forma breve mismo método al modelo diferencial de NOx.

## 3. Guion de exposición con tiempos

### Bloque 1 — Encuadre del caso y flujo maestro — 0–10 min (acumulado: 10 min)

**Idea fuerza:** la incertidumbre es parte del resultado; no es una cifra añadida al final.

El docente muestra flujo maestro común de QUAM/GUM: **especificar, identificar, cuantificar, depurar, combinar, expandir, informar y revisar**. Caso KRISS es principalmente bottom-up; revisión final debe preguntar cómo contrastar orden de magnitud mediante QC, comparación independiente u otra evidencia experimental. QUAM organiza evaluación práctica en caps. 4–9; taller usa cap. 9, pp. editoriales 30–32, para cierre documental.

El docente presenta el único entregable y explica que la tabla ya contiene datos y operaciones de arranque. El trabajo del equipo consiste en completar celdas, comprobar coherencia y explicar qué domina el resultado, no en transcribir un presupuesto desde cero.

En 2024, KRISS comparó su patrón nacional KRISS-SRP5 con BIPM-SRP27 mediante el patrón de transferencia KRISS-SRP3. Se realizó una comparación KRISS-SRP5/KRISS-SRP3 antes del transporte, una comparación KRISS-SRP3/BIPM-SRP27 en BIPM y otra comparación después del transporte para examinar estabilidad (KRISS report, §8, p. 3, citado en `cursov2/casos/extracto_kriss_2024.md`, §1).

**Párrafo dictable:** “Una evaluación es defendible cuando otra persona puede identificar el mensurando, reconstruir el modelo, seguir cada contribución y comprender el intervalo informado.”

### Bloque 2 — Mensurando y modelo — 10–20 min (acumulado: 20 min)

**Idea fuerza:** antes de combinar incertidumbres, debe definirse qué resultado se estima y mediante qué relación.

Checklist QUAM cap. 5 para este caso: especie; matriz/base seca; unidad; punto físico del sistema; intervalo de trabajo; relación entre `x` e `y`; alcance de comparación; correcciones y dependencias. Cada equipo debe comprobar ocho elementos antes de calcular.

La relación publicada es

\[
y=a_0+a_1x,
\]

con \(a_0=0.41\ \mathrm{nmol\ mol^{-1}}\), \(u(a_0)=0.28\ \mathrm{nmol\ mol^{-1}}\), \(a_1=0.9971\), \(u(a_1)=0.0046\) y \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\) (KRISS report, §14.1, ecuaciones 9–10, p. 9).

**Apoyo en el handout:** ver `handout_teorico_gum_o3.md`, §1.1 — Mensurando y resultado de medición, §1.2 — Modelo de medición y §4.1 — Coeficientes de sensibilidad.

Para el valor \(x\) asignado por BIPM-SRP27, los coeficientes de sensibilidad son \(c_x=a_1\), \(c_{a_0}=1\) y \(c_{a_1}=x\). El docente distingue el presupuesto fotométrico que produce \(u(x)\) de la propagación posterior hacia \(y\).

**Párrafo dictable:** “La incertidumbre del valor de referencia, las incertidumbres de la regresión y su covarianza cumplen funciones distintas; el modelo conserva esa diferencia.”

### Bloque 3 — Presupuesto fotométrico de BIPM-SRP27 — 20–34 min (acumulado: 34 min)

**Idea fuerza:** la fotometría UV combina una contribución absoluta y contribuciones proporcionales a la fracción de ozono.

**Apoyo en el handout:** ver `handout_teorico_gum_o3.md`, §3.2 — Distribución rectangular, §3.3 — Distribución normal y §3.4 — Distribución triangular, para leer la columna de distribuciones publicadas, y §4.4 — Presupuesto y contribuciones, para la estructura de la tabla.

El presupuesto se declara aplicable a BIPM-SRP27 y BIPM-SRP28 entre 0 y 500 nmol mol⁻¹ (BIPM.QM-K1 protocol v2.1, App. 1 §1, p. 21).

| Componente | Fuentes publicadas | Distribuciones publicadas | Incertidumbre estándar combinada | Contribución a \(u(x)\) |
|---|---|---|---:|---:|
| Longitud óptica \(L_{opt}\) | escala, repetibilidad, sesgo | rectangular, normal, rectangular | 0.52 cm | \(2.89\times10^{-3}x\) |
| Presión \(P\) | manómetro, diferencia entre celdas | rectangular, rectangular | 0.034 kPa | \(3.37\times10^{-4}x\) |
| Temperatura \(T\) | sonda, sesgo residual | rectangular, rectangular | 0.07 K | \(2.29\times10^{-4}x\) |
| Cociente de intensidades \(D\) | resolución, repetibilidad | rectangular, triangular | \(1.4\times10^{-5}\) | 0.28 nmol mol⁻¹ |
| Sección eficaz \(\sigma\) | valor convencional CCQM.O3.2019 | no indicada | \(0.35\times10^{-19}\ \mathrm{cm^2\ molecule^{-1}}\) | “–” en esta comparación |

Fuente: BIPM.QM-K1 protocol v2.1, App. 1 §1, pp. 21–22. Al comparar fotómetros UV que usan el mismo valor de sección eficaz, su incertidumbre común puede fijarse en cero; debe incluirse al comparar métodos o valores diferentes, o al evaluar el método completo (protocolo §4.1, p. 3).

La expresión simplificada publicada es

\[
u(x)=\sqrt{(0.28)^2+\left(2.92\times10^{-3}x\right)^2},
\]

con \(x\) en nmol mol⁻¹ (App. 1 §2, ecuación 14, p. 23). A 100 nmol mol⁻¹, el participante debe comprobar que \(u(x)\approx0.405\ \mathrm{nmol\ mol^{-1}}\).

Etiquetas de lectura: `D` aporta término absoluto; `L`, `P` y `T` aportan términos proporcionales; `σ` es común y se cancela solo bajo condiciones declaradas de comparación. Forma se conecta con QUAM App. E.5 y ejemplo A6:

\[
u(x)=\sqrt{u_0^2+(u_r x)^2}.
\]

No reutilizar expresión resumida y filas que ya contiene: produciría doble conteo.

### Bloque 4 — Covarianza y cobertura — 34–48 min (acumulado: 48 min)

**Idea fuerza:** dependencia y cobertura son decisiones visibles del modelo y del informe.

El protocolo señala que las mediciones realizadas con el mismo SRP a distintas fracciones están correlacionadas y desarrolla la covarianza fotométrica en el App. 1 §3, pp. 24–25. En este ejercicio de un solo nivel no se construye una matriz entre niveles; se conserva la covarianza publicada entre \(a_0\) y \(a_1\):

\[
u_c^2(y)=a_1^2u^2(x)+u^2(a_0)+x^2u^2(a_1)+2x\operatorname{cov}(a_0,a_1).
\]

**Apoyo en el handout:** ver `handout_teorico_gum_o3.md`, §4.2 — Ley de propagación de incertidumbre, para el término cruzado de covarianza con su signo, y §4.3 — Doble conteo: GUM §4.3.10.

QUAM cap. 8 recomienda representar entradas que comparten patrón, calibración o datos como dependientes cuando corresponda. Covarianza es término cruzado del modelo, no nueva fila positiva. Si se usa valor absoluto o se agrega como componente independiente, cambia modelo y varianza.

El signo negativo no se elimina ni se reemplaza por valor absoluto. Para el ejercicio obligatorio se fija **\(k=2\)** como aproximación convencional a una cobertura de aproximadamente 95 %, adecuada para practicar construcción e interpretación del presupuesto cuando no se dispone de grados de libertad documentados para todas las entradas. Debe declararse que esta elección no sustituye una evaluación de cobertura más detallada cuando el uso previsto la exija.

**Material avanzado opcional, fuera de la actividad de 24 min:** revisar JCGM 100:2008, Anexo G.4, y `handout_teorico_gum_o3.md`, §4.5, para estudiar Welch–Satterthwaite y la selección de un cuantil t cuando existan grados de libertad sustentados. No se asignan grados de libertad ficticios ni se calcula \(\nu_{eff}\) en el entregable obligatorio.

### Bloque 5 — Trabajo de equipos — 48–72 min (acumulado: 72 min)

Los equipos desarrollan la actividad de la sección 4 durante 24 min. El docente da una señal al minuto 3 para cerrar lectura, al minuto 14 para pasar al informe, al minuto 18 para formular validación externa y alcance, y al minuto 22 para responder la transferencia a NOx e iniciar revisión. Durante el trabajo verifica, en este orden: modelo y unidades; celdas faltantes; signo de covarianza; cálculo de \(u_c\) y \(U\); interpretación y redondeo. No abre actividades adicionales ni solicita reconstruir el ajuste de regresión.

### Bloque 6 — Revisión cruzada y cierre — 72–85 min (acumulado: 85 min)

**Apoyo en el handout:** ver `handout_teorico_gum_o3.md`, §7.1 — Contenido mínimo, §7.2 — Forma de expresar resultado, §7.3 — Redondeo y §7.4 — Lista de comprobación, como pauta de la revisión cruzada del informe GUM §7.

Cada equipo intercambia presupuesto e informe. Lista combinada GUM §7 + QUAM cap. 9 verifica:

1. mensurando inequívoco;
2. resultado y unidad;
3. modelo, fuentes y correcciones;
4. \(u_c\) y \(U\) claramente distinguidas;
5. \(k\) y cobertura aproximada;
6. método y referencias;
7. condiciones y alcance;
8. redondeo coherente;
9. asimetría, si aplica;
10. regla de decisión, si se declara conformidad;
11. dependencias y covarianzas con signo;
12. ausencia de doble conteo.

No usar “95 % de confianza” sin marco. Redondear `U` a una o dos cifras significativas y resultado a misma posición. Separar resultado metrológico de decisión de conformidad.

**Párrafo dictable:** “Informar conforme al GUM significa exponer información suficiente para comprender el resultado y, cuando sea necesario, repetir la evaluación. El presupuesto y el texto deben contar la misma historia metrológica.”

## 4. Ejercicio/actividad

### Enunciado completo

Informe la relación previa al transporte entre KRISS-SRP5 y BIPM-SRP27 para un valor asignado \(x=100\ \mathrm{nmol\ mol^{-1}}\). Complete las celdas marcadas **[completar]**, calcule \(u_c(y)\) y \(U\) con \(k=2\), interprete el presupuesto y redacte una declaración conforme a GUM §7.

Datos:

- \(u(x)=\sqrt{(0.28)^2+(2.92\times10^{-3}x)^2}\ \mathrm{nmol\ mol^{-1}}\).
- \(a_0=0.41\ \mathrm{nmol\ mol^{-1}}\); \(u(a_0)=0.28\ \mathrm{nmol\ mol^{-1}}\).
- \(a_1=0.9971\); \(u(a_1)=0.0046\).
- \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\).
- \(c_x=a_1\), \(c_{a_0}=1\), \(c_{a_1}=x\).
- \(k=2\), cobertura aproximada de 95 % bajo la convención declarada.

Presupuesto parcialmente resuelto:

| Componente | Origen | Estimación | \(u\) estándar | \(c_i\) | Contribución o término en \(u_c^2\) |
|---|---|---:|---:|---:|---:|
| Valor \(x\) | BIPM App. 1, ec. 14 | 100 nmol mol⁻¹ | **[completar]** | 0.9971 | \((0.9971\,u(x))^2\) |
| Intercepto \(a_0\) | KRISS §14.1 | 0.41 nmol mol⁻¹ | 0.28 nmol mol⁻¹ | 1 | 0.078400 |
| Pendiente \(a_1\) | KRISS §14.1 | 0.9971 | 0.0046 | 100 nmol mol⁻¹ | **[completar]** |
| Covarianza \(a_0,a_1\) | KRISS §14.1 | \(-3.47\times10^{-4}\) nmol mol⁻¹ | no aplica | \(2x\) | **[completar con signo]** |
| **Combinación** | modelo | \(y=0.41+0.9971(100)\) | — | — | \(u_c^2=\) **[completar]** |

Complete además:

1. \(y=\) **[completar]** nmol mol⁻¹.
2. \(u_c(y)=\) **[completar]** nmol mol⁻¹.
3. \(U=2u_c(y)=\) **[completar]** nmol mol⁻¹.
4. Identifique la mayor contribución positiva y explique en una frase el efecto de la covarianza negativa.
5. Redacte el resultado con una o dos cifras significativas en \(U\) y la estimación redondeada a la misma posición decimal.
6. Proponga una **validación externa** capaz de comprobar orden de magnitud del presupuesto: comparación posterior al transporte, QC histórico, otra SRP, repetición independiente o evaluación en segundo nivel.
7. Escriba una frase de **alcance** que indique dónde no aplica resultado.
8. **Transferencia a NOx, máximo 50 palabras:** para modelo \(c_{NO_2}=(c_{NO_x}-c_{NO})/\eta_c\), indique mensurando, una dependencia que debe tratarse y un dato externo útil para validar presupuesto.

### Tiempo

**24 min reales:** 3 min para leer y ubicar datos; 10 min para completar y comprobar el presupuesto; 4 min para interpretar y redactar; 3 min para validación externa y alcance; 2 min para transferencia a NOx; 2 min para revisión interna.

### Resultado esperado

**Una línea:** un presupuesto completado y un informe GUM §7 con \(y\), \(u_c(y)\), \(k=2\), \(U\), cobertura aproximada, covarianza, fuentes e interpretación.

Estructura de apoyo:

> La fracción de cantidad de sustancia de ozono en aire seco atribuida a KRISS-SRP5 al compararla, antes del transporte, con BIPM-SRP27 para \(x=100\ \mathrm{nmol\ mol^{-1}}\) fue \(y=[valor]\ \mathrm{nmol\ mol^{-1}}\). La incertidumbre estándar combinada fue \(u_c=[valor]\ \mathrm{nmol\ mol^{-1}}\), incluida la covarianza publicada entre intercepto y pendiente. La incertidumbre expandida fue \(U=[valor]\ \mathrm{nmol\ mol^{-1}}\), obtenida con \(k=2\), para una cobertura aproximada de 95 % bajo la convención declarada. La evaluación aplicó propagación GUM al modelo \(y=a_0+a_1x\) y el presupuesto fotométrico de BIPM-SRP27 del App. 1.

## 5. Errores frecuentes y preguntas típicas

1. **¿Tipo A significa “aleatorio” y Tipo B significa “sistemático”?**  
   No. Tipo A y Tipo B describen el método usado para evaluar la incertidumbre, no la naturaleza aleatoria o sistemática del efecto.

2. **¿Por qué no se toma el valor absoluto de la covarianza negativa?**  
   Porque su signo expresa cómo varían conjuntamente intercepto y pendiente. Cambiarlo altera el modelo y la varianza propagada.

3. **¿Se puede sumar directamente 0.28 y \(2.92\times10^{-3}x\)?**  
   No. Son contribuciones estándar independientes en la expresión publicada y se combinan en cuadratura.

4. **¿Por qué aquí se fija \(k=2\)?**  
   Porque el taller prioriza completar e interpretar un presupuesto con información publicada y no dispone de grados de libertad documentados para todas las entradas. Es una aproximación convencional declarada, no un factor oficial de KRISS o BIPM.

5. **¿Cuándo se usaría Welch–Satterthwaite?**  
   Cuando existan grados de libertad sustentados y el uso requiera estimar \(\nu_{eff}\) para seleccionar el factor de cobertura. Se deja como ampliación avanzada opcional.

Errores que deben corregirse antes de entregar: describir el mensurando solo como “concentración”; mezclar nmol mol⁻¹ con otras unidades sin conversión; redondear componentes antes de combinar; omitir \(u_c\) e informar solo \(U\); declarar “95 % de confianza” sin explicar el marco; contar dos veces una contribución ya incluida; tratar la covarianza como fuente independiente; atribuir \(k=2\) al informe del BIPM o de KRISS.

## 6. Cierre y transición

El taller cierra el curso conectando mensurando, fotometría UV, patrón SRP, modelo, datos, covarianza, cobertura e informe en un producto auditable. Como transición a la práctica laboral, cada participante debe aplicar la misma secuencia a sus sistemas: definir, modelar, documentar, propagar, revisar e informar sin copiar componentes que no correspondan al proceso real.
