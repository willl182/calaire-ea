# M7 — Taller integrador: presupuesto, validación y reporte

## 1. Ficha

- **Duración:** 85 min.
- **Posición en el curso:** módulo 7 de 7 del recorrido obligatorio; cierre integrador de la jornada de 9 h. M6 NOx se desarrolla antes del taller. M8 Monte Carlo queda como material avanzado opcional fuera de la jornada.
- **Prerrequisitos:** M1–M6; definición de mensurando; evaluaciones Tipo A y Tipo B; conversión a incertidumbres estándar; coeficientes de sensibilidad; ley de propagación GUM; dependencia y covarianza; incertidumbre combinada y expandida; lectura básica de regresión lineal; modelo diferencial NO₂ = NOx − NO visto en M6.
- **Materiales:** `cursov2/casos/extracto_kriss_2024.md`; BIPM.QM-K1 protocol v2.1, App. 1; presupuesto parcialmente resuelto; computador con calculadora u hoja de cálculo; lista combinada GUM §7 + QUAM cap. 9.
- **Modalidad:** trabajo en equipos de dos o tres personas, seguido de revisión cruzada.
- **Entregable:** presupuesto completado, declaración de resultado, propuesta de validación externa, frase de alcance y respuesta breve de transferencia del método a NOx.
- **Relación con la práctica de laboratorio:** este taller y su entregable son **independientes** de la práctica instrumental, que es contenido aparte y no cuenta dentro de las 9 h del curso. El ejercicio con el caso KRISS/BIPM descrito aquí conserva íntegro su rol de cierre evaluado del curso. `practica/E15_presupuesto_hibrido.md` es un **entregable separado y adicional** de la práctica, que aplica el mismo método a evidencia propia; ninguno reemplaza al otro y cada uno se evalúa por su cuenta.
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

El libreto de exposición está organizado en páginas/diapositivas Markdown independientes. Cada página conserva el texto dictable, el minutaje y sus apoyos; este apartado funciona como índice.

1. [M7 — Página 01 — Bloque 1 — Encuadre del caso y flujo maestro — 0–10 min (acumulado: 10 min)](../paginas/M7_01_bloque_1_encuadre_del_caso_y_flujo_maestro_010_min_acumulado_10_min.md)
2. [M7 — Página 02 — Bloque 2 — Mensurando y modelo — 10–20 min (acumulado: 20 min)](../paginas/M7_02_bloque_2_mensurando_y_modelo_1020_min_acumulado_20_min.md)
3. [M7 — Página 03 — Bloque 3 — Presupuesto fotométrico de BIPM-SRP27 — 20–34 min (acumulado: 34 min)](../paginas/M7_03_bloque_3_presupuesto_fotometrico_de_bipm_srp27_2034_min_acumulado_34_min.md)
4. [M7 — Página 04 — Bloque 4 — Covarianza y cobertura — 34–48 min (acumulado: 48 min)](../paginas/M7_04_bloque_4_covarianza_y_cobertura_3448_min_acumulado_48_min.md)
5. [M7 — Página 05 — Bloque 5 — Trabajo de equipos — 48–72 min (acumulado: 72 min)](../paginas/M7_05_bloque_5_trabajo_de_equipos_4872_min_acumulado_72_min.md)
6. [M7 — Página 06 — Bloque 6 — Revisión cruzada y cierre — 72–85 min (acumulado: 85 min)](../paginas/M7_06_bloque_6_revision_cruzada_y_cierre_7285_min_acumulado_85_min.md)

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
