# M7 — Taller integrador: presupuesto y reporte de incertidumbre

## 1. Ficha

- **Duración:** 70 min.
- **Posición en el curso:** módulo 7 de 7; cierre integrador de la jornada de 6 h.
- **Prerrequisitos:** definición de mensurando; evaluaciones Tipo A y Tipo B; conversión de límites e incertidumbres expandidas a incertidumbres estándar; coeficientes de sensibilidad; ley de propagación GUM; covarianza; incertidumbre combinada y expandida; lectura básica de una regresión lineal.
- **Materiales:** `contenido/casos/extracto_kriss_2024.md`; BIPM.QM-K1 protocol v2.1, App. 1; `contenido/datasets/dataset_verificacion_multipunto.csv` y `contenido/datasets/dataset_metadata.md` como continuidad del M5; `contenido/plantillas/plantilla_presupuesto.R`, caso 2 precargado, como estructura inicial que deberá adaptarse a los niveles y datos BIPM/KRISS; computador con R o calculadora/hoja de cálculo; lista de comprobación de GUM §7.
- **Modalidad:** trabajo en equipos de dos o tres personas, seguido de revisión cruzada.
- **Entregable:** una hoja de presupuesto completa y dos declaraciones de resultado conforme a GUM §7, una para nivel bajo y otra para nivel alto.
- **Niveles de trabajo:** 30 nmol mol⁻¹ y 500 nmol mol⁻¹.
- **Fuentes de los datos:** exclusivamente resultados públicos de BIPM y KRISS. No se emplean datos operativos de organizaciones, redes o esquemas externos.

El mensurando del protocolo es la fracción de cantidad de ozono en aire seco, expresada en mol mol⁻¹ o sus múltiplos. Aunque el valor numérico en nmol mol⁻¹ coincide con ppb, el protocolo indica que ppb y ppbv no son unidades recomendadas (BIPM.QM-K1 protocol v2.1, §4, p. 3). Durante el taller se utilizará **nmol mol⁻¹**.

La revisión directa del PDF confirma que el Apéndice 1 comienza en la **página 21 de 25**. La tabla del presupuesto ocupa las **pp. 21–22**, la expresión simplificada se deriva en las **pp. 22–23** y los términos de covarianza se desarrollan en las **pp. 24–25**.

## 2. Objetivos específicos

Al finalizar los 70 minutos, cada participante podrá:

1. **Reconstruir** el presupuesto de incertidumbre de BIPM-SRP27 a partir de los componentes publicados en el App. 1 y comprobar su equivalencia con la expresión simplificada de \(u(x)\).
2. **Calcular** la estimación, la incertidumbre estándar combinada y la incertidumbre expandida de la relación KRISS-SRP5/BIPM-SRP27 en 30 nmol mol⁻¹ y 500 nmol mol⁻¹.
3. **Incorporar** correctamente una covarianza entre intercepto y pendiente, conservando su signo y distinguiéndola de las contribuciones individuales.
4. **Aplicar** una versión simplificada de Welch–Satterthwaite para obtener grados efectivos de libertad y seleccionar un factor de cobertura bilateral aproximado de 95 %.
5. **Redactar** dos resultados auditables conforme a GUM §7, identificando mensurando, modelo, estimación, unidad, incertidumbres, factor de cobertura, probabilidad de cobertura, fuentes y limitaciones.

## 3. Guion de exposición con tiempos

### Bloque 1 — Encuadre del caso — 0–8 min (acumulado: 8 min)

**Idea fuerza:** la incertidumbre es parte del resultado; no es una cifra añadida al final del cálculo.

El docente presenta el entregable y recuerda que cada fila de la hoja debe representar una fuente o un componente identificable. La hoja debe permitir volver desde el resultado final hasta el dato y la referencia de origen. Si aparece una covarianza, debe mostrarse como término cruzado; no debe ocultarse como si fuera otra incertidumbre estándar independiente.

En 2024, KRISS comparó su patrón nacional KRISS-SRP5 con BIPM-SRP27 mediante el patrón de transferencia KRISS-SRP3. Se realizó una comparación KRISS-SRP5/KRISS-SRP3 antes del transporte, una comparación KRISS-SRP3/BIPM-SRP27 en BIPM y una comparación KRISS-SRP5/KRISS-SRP3 después del transporte para examinar estabilidad (KRISS report, §8, p. 3, citado en `extracto_kriss_2024.md`, §1).

**Párrafo dictable:** “Una evaluación es defendible cuando otra persona puede identificar el mensurando, reconstruir el modelo, seguir cada contribución y comprender por qué el intervalo informado corresponde a la información disponible.”

### Bloque 2 — Mensurando y modelo — 8–16 min (acumulado: 16 min)

**Idea fuerza:** antes de sumar incertidumbres hay que definir qué resultado se estima y qué relación matemática lo representa.

La relación publicada es

\[
x_{\mathrm{KRISS\text{-}SRP5}}=a_0+a_1x_{\mathrm{SRP27}}.
\]

Para la comparación previa a la visita se publicaron \(a_0=0.41\ \mathrm{nmol\ mol^{-1}}\), \(u(a_0)=0.28\ \mathrm{nmol\ mol^{-1}}\), \(a_1=0.9971\), \(u(a_1)=0.0046\) y \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\) (KRISS report, §14.1, ecuaciones 9–10, p. 9).

Para un valor \(x\) asignado por BIPM-SRP27, se adopta \(y=a_0+a_1x\). Sus coeficientes de sensibilidad son \(c_x=a_1\), \(c_{a_0}=1\) y \(c_{a_1}=x\). El docente distingue dos capas: el presupuesto instrumental que produce \(u(x)\) y la propagación posterior de \(x\), \(a_0\) y \(a_1\) hacia \(y\).

**Párrafo dictable:** “La incertidumbre del valor de referencia, la incertidumbre de los parámetros de regresión y la covarianza entre esos parámetros cumplen funciones diferentes. El modelo conserva esa diferencia.”

### Bloque 3 — Presupuesto de BIPM-SRP27 — 16–28 min (acumulado: 28 min)

**Idea fuerza:** el término constante domina cerca de cero; las contribuciones proporcionales crecen con la fracción de ozono.

El presupuesto se declara aplicable a BIPM-SRP27 y BIPM-SRP28 en el intervalo de 0 a 500 nmol mol⁻¹ (BIPM.QM-K1 protocol v2.1, App. 1 §1, p. 21). El docente presenta los componentes agrupados:

| Componente | Fuentes publicadas | Distribuciones publicadas | Incertidumbre estándar combinada | Contribución a \(u(x)\) |
|---|---|---|---:|---:|
| Longitud óptica \(L_{opt}\) | escala, repetibilidad, sesgo | rectangular, normal, rectangular | 0.52 cm | \(2.89\times10^{-3}x\) |
| Presión \(P\) | manómetro, diferencia entre celdas | rectangular, rectangular | 0.034 kPa | \(3.37\times10^{-4}x\) |
| Temperatura \(T\) | sonda, sesgo residual | rectangular, rectangular | 0.07 K | \(2.29\times10^{-4}x\) |
| Cociente de intensidades \(D\) | resolución, repetibilidad | rectangular, triangular | \(1.4\times10^{-5}\) | 0.28 nmol mol⁻¹ |
| Sección eficaz \(\sigma\) | valor convencional CCQM.O3.2019 | no indicada | \(0.35\times10^{-19}\ \mathrm{cm^2\ molecule^{-1}}\) | “–” en esta comparación |

**Cita exacta:** BIPM.QM-K1 protocol v2.1, App. 1 §1, tabla, pp. 21–22. El protocolo explica que, al comparar dos fotómetros UV que usan el mismo valor de sección eficaz, su incertidumbre puede fijarse en cero; debe incluirse al comparar métodos o valores diferentes, o al evaluar el presupuesto completo del método (BIPM.QM-K1 protocol v2.1, §4.1, p. 3).

La expresión simplificada publicada es

\[
u(x)=\sqrt{(0.28)^2+\left(2.92\times10^{-3}x\right)^2},
\]

con \(x\) en nmol mol⁻¹ (BIPM.QM-K1 protocol v2.1, App. 1 §2, ecuación 14, p. 23).

### Bloque 4 — Covarianza y cobertura — 28–40 min (acumulado: 40 min)

**Idea fuerza:** una fuente compartida crea dependencia, y pocos grados de libertad pueden elevar el factor de cobertura por encima de 2.

El protocolo señala que las mediciones realizadas con el mismo SRP a distintas fracciones están correlacionadas y que esta dependencia debe incorporarse en la regresión generalizada (BIPM.QM-K1 protocol v2.1, App. 1 §3, p. 24). Para temperatura, presión y longitud óptica comunes publica

\[
u(x_i,x_j)=x_i x_j u_b^2,\qquad u_b=2.92\times10^{-3},
\]

(BIPM.QM-K1 protocol v2.1, App. 1 §3, ecuaciones 20–21, p. 25).

En el ejercicio no se reconstruye la matriz completa. Se conserva la covarianza publicada entre \(a_0\) y \(a_1\):

\[
u_c^2(y)=a_1^2u^2(x)+u^2(a_0)+x^2u^2(a_1)+2x\operatorname{cov}(a_0,a_1).
\]

El signo no se elimina ni se reemplaza por valor absoluto. Para practicar Welch–Satterthwaite sin atribuir datos inexistentes al informe, se establece un **escenario didáctico explícito**: \(\nu_{a_1}=2\), como si \(u(a_1)\) procediera de tres determinaciones independientes, y \(\nu=\infty\) para las demás contribuciones. Esta asignación no es un dato publicado por KRISS o BIPM.

Se aplica

\[
\nu_{eff}=\frac{u_c^4(y)}{\sum_i u_i^4(y)/\nu_i},
\]

se trunca \(\nu_{eff}\) hacia abajo y se consulta el cuantil t bilateral aproximado de 95 %. Los componentes con \(\nu=\infty\) aportan cero al denominador. La fórmula corresponde a JCGM 100:2008, Anexo G.4; véase también `handout_teorico_gum_o3.md`, §4.5.

### Bloque 5 — Trabajo de equipos — 40–59 min (acumulado: 59 min)

Los equipos desarrollan la actividad de la sección 4. Abren `contenido/plantillas/plantilla_presupuesto.R` y usan el caso 2 precargado solo como ejemplo de columnas, divisores y cálculo de Welch–Satterthwaite; deben sustituir sus valores sintéticos por los datos BIPM/KRISS y crear evaluaciones separadas para 30 y 500 nmol mol⁻¹. `contenido/datasets/dataset_verificacion_multipunto.csv` queda disponible para rastrear la continuidad con M5: muestra cómo pendiente, intercepto y residuos alimentan un presupuesto, pero sus datos sintéticos no se mezclan con las cifras públicas del caso. El docente comprueba primero el modelo y las unidades; después revisa covarianza, grados efectivos y redondeo. No entrega una solución paso a paso.

### Bloque 6 — Revisión cruzada y puesta en común — 59–70 min (acumulado: 70 min)

Cada equipo intercambia su hoja y sus dos reportes. La revisión verifica: mensurando completo, modelo visible, citas, separación entre datos publicados y supuesto didáctico, covarianza con signo, \(u_c\), \(U\), \(k\), probabilidad de cobertura, \(\nu_{eff}\), redondeo final y ausencia de doble conteo.

**Párrafo dictable:** “Reportar conforme al GUM significa exponer información suficiente para comprender el resultado y, cuando sea necesario, repetir la evaluación. El presupuesto y el texto deben contar la misma historia metrológica.”

## 4. Ejercicio/actividad

### Enunciado completo

Informe la relación previa al transporte entre KRISS-SRP5 y BIPM-SRP27 en **30 nmol mol⁻¹** y **500 nmol mol⁻¹**. Prepare una hoja de presupuesto auditable para cada nivel y redacte dos declaraciones conformes a GUM §7. Use `contenido/plantillas/plantilla_presupuesto.R`, caso 2, como punto de partida estructural: conserve su lógica de combinación, pero reemplace sus valores sintéticos y no los atribuya al caso publicado. Use el modelo \(y=a_0+a_1x\); obtenga \(u(x)\) con la expresión del App. 1; propague \(u(x)\), \(u(a_0)\), \(u(a_1)\) y \(\operatorname{cov}(a_0,a_1)\); aplique el escenario simplificado de Welch–Satterthwaite definido en la sección 3. Consulte `contenido/datasets/dataset_metadata.md` para identificar qué elementos de una verificación multipunto originan pendiente, intercepto, residuos y deriva, pero no combine ese dataset sintético con los valores BIPM/KRISS. No presente los grados de libertad didácticos como dato oficial del informe.

La hoja debe contener: componente, origen, estimación, unidad, distribución o método, divisor cuando corresponda, incertidumbre estándar, grados de libertad, coeficiente de sensibilidad, contribución, participación en la varianza, término de covarianza y cita. Los cálculos intermedios conservan precisión suficiente; el redondeo se hace al final. La incertidumbre se informa con una o dos cifras significativas y la estimación se redondea a la misma posición decimal.

### Datos

- \(x=30\) y \(500\ \mathrm{nmol\ mol^{-1}}\).
- \(u(x)=\sqrt{(0.28)^2+(2.92\times10^{-3}x)^2}\ \mathrm{nmol\ mol^{-1}}\).
- \(a_0=0.41\ \mathrm{nmol\ mol^{-1}}\); \(u(a_0)=0.28\ \mathrm{nmol\ mol^{-1}}\).
- \(a_1=0.9971\); \(u(a_1)=0.0046\).
- \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\).
- \(c_x=a_1\), \(c_{a_0}=1\), \(c_{a_1}=x\).
- Escenario didáctico: \(\nu_{a_1}=2\); demás contribuciones, \(\nu=\infty\).
- Probabilidad de cobertura objetivo: aproximadamente 95 %.
- Fuente de regresión: KRISS report, §14.1, ecuaciones 9–10, p. 9.
- Fuente de \(u(x)\): BIPM.QM-K1 protocol v2.1, App. 1 §2, ecuación 14, p. 23.

### Tiempo

**19 min:** 12 min para cálculos y hoja, 5 min para redactar los dos reportes y 2 min para revisión interna.

### Resultado esperado

**Una línea:** dos presupuestos completos y dos reportes GUM §7 que incluyan \(y\), \(u_c(y)\), \(\nu_{eff}\), \(k\), \(U\), cobertura, covarianza, fuentes y limitación didáctica, sin solución algebraica detallada.

Como apoyo de redacción, puede usarse esta estructura:

> La fracción de cantidad de ozono en aire seco atribuida a KRISS-SRP5 al comparar con BIPM-SRP27 en el nivel de [nivel] nmol mol⁻¹ fue \(y=[valor]\ \mathrm{nmol\ mol^{-1}}\). La incertidumbre estándar combinada fue \(u_c=[valor]\ \mathrm{nmol\ mol^{-1}}\). La incertidumbre expandida fue \(U=[valor]\ \mathrm{nmol\ mol^{-1}}\), con \(k=[valor]\), \(\nu_{eff}=[valor]\) y probabilidad de cobertura aproximada de 95 %. La evaluación aplicó propagación GUM al modelo \(y=a_0+a_1x\), incluyó la covarianza publicada entre intercepto y pendiente y utilizó el presupuesto de BIPM-SRP27 del App. 1. Los grados asignados a \(u(a_1)\) pertenecen a un escenario didáctico simplificado y no a un valor publicado por KRISS.

## 5. Errores frecuentes y preguntas típicas

1. **¿Tipo A significa “aleatorio” y Tipo B significa “sistemático”?**  
   No. Tipo A y Tipo B describen el método usado para evaluar la incertidumbre, no la naturaleza aleatoria o sistemática del efecto.

2. **¿Por qué no se toma el valor absoluto de la covarianza negativa?**  
   Porque su signo expresa cómo varían conjuntamente intercepto y pendiente. Cambiarlo altera el modelo y la varianza propagada.

3. **¿Se puede sumar directamente 0.28 y \(2.92\times10^{-3}x\)?**  
   No. Son contribuciones estándar independientes en la expresión publicada y se combinan en cuadratura.

4. **¿Por qué \(k\) no se fija siempre en 2?**  
   Porque el factor depende de la probabilidad de cobertura, la forma de la distribución y los grados efectivos de libertad. Con pocos grados, el cuantil t puede superar 2.

5. **¿Los grados \(\nu_{a_1}=2\) forman parte del resultado oficial KRISS?**  
   No. Son una hipótesis pedagógica declarada para practicar Welch–Satterthwaite; el dato no fue publicado en el extracto usado.

Errores que deben corregirse antes de entregar: describir el mensurando solo como “concentración”; mezclar nmol mol⁻¹ con otras unidades sin conversión; redondear componentes antes de combinar; omitir la incertidumbre estándar combinada y reportar solo \(U\); declarar “95 % de confianza” sin explicar el marco; contar dos veces una contribución ya incluida; asignar porcentajes de varianza a un término cruzado como si perteneciera por completo a una sola fila.

## 6. Cierre y transición

El taller cierra el curso conectando mensurando, modelo, datos, covarianza, cobertura y reporte en un único producto auditable. Como transición a la práctica laboral, cada participante debe aplicar la misma secuencia a sus propios sistemas: definir, modelar, documentar, propagar, revisar y reportar sin copiar componentes que no correspondan al proceso real.
