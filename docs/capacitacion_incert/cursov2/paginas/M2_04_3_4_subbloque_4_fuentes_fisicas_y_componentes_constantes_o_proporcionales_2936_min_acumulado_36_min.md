# M2 — Página 04 — 3.4 Subbloque 4 — Fuentes físicas y componentes constantes o proporcionales (29–36 min; acumulado: 36 min)

- **Sesión:** M2
- **Fuente:** [`modulos/M2_modelo_medicion.md`](../modulos/M2_modelo_medicion.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.4 Subbloque 4 — Fuentes físicas y componentes constantes o proporcionales (29–36 min; acumulado: 36 min)

**Idea fuerza:** el presupuesto debe representar mecanismos físicos; copiar especificaciones sin conectarlas con el modelo no basta.

**Guion dictable:** Para identificar fuentes sin copiar listas, QUAM propone recorrer tanto la ecuación como el proceso y depurar duplicados. Organice el análisis en cuatro grupos: **entradas explícitas** \(T, P, L, \sigma, D\); **operaciones** de generación, transporte, acondicionamiento, lectura y procesamiento; **fuentes externas** como ambiente, interferentes, estabilidad y calibración; y **depuración** de efectos ya cubiertos por otra cifra. Esta estructura procede de QUAM cap. 6, pp. editoriales 14–15 (PDF pp. 20–21), App. C, p. editorial 101 (PDF p. 107), y App. D, pp. editoriales 102–103 (PDF pp. 108–109).

Conectemos cada término con la realización práctica. Primero, las pérdidas de ozono en líneas, conexiones o superficies hacen que la cantidad que llega a la celda sea menor que la presente aguas arriba. La regulación incorpora una corrección asociada a la longitud o al factor de pérdida. Los materiales de las líneas deben seleccionarse y acondicionarse para minimizar reactividad. Una pérdida conocida debe corregirse; la incertidumbre de esa corrección permanece en el presupuesto.

Segundo, los gradientes de temperatura importan porque el valor introducido en la ecuación debe representar el gas en la región pertinente. Un sensor exacto situado en un punto no representativo no elimina la deficiencia del modelo. Deben considerarse calibración, resolución, estabilidad y diferencia entre la temperatura indicada y la temperatura efectiva de la celda.

Tercero, la exactitud de presión influye de manera inversa. Debe verificarse que la presión sea absoluta, que el punto de medición represente la celda y que no se omitan caídas de presión. Calibración, resolución y estabilidad del sensor son fuentes separadas solamente si representan efectos que no están contenidos en una estimación agregada.

Cuarto, la resolución del cociente de intensidades afecta \(D\). Intervienen resolución digital, ruido óptico, estabilidad de la fuente, detección electrónica y cálculo de \(I/I_0\). Debido a la función logarítmica, una resolución fija de señal puede comportarse aproximadamente como una contribución constante en unidades de fracción molar dentro de un intervalo limitado y puede dominar cerca de cero.

**Apoyo en el handout:** ver Handout teórico, §4.4 — Presupuesto y contribuciones, para la organización de estos efectos en un presupuesto, y §3.2 — Distribución rectangular, para el tratamiento de la resolución.

Conviene distinguir componentes proporcionales y constantes. Incertidumbres relativas aproximadamente constantes de \(\sigma\), \(L\), \(T\) y \(P\) producen contribuciones que aumentan con \(x\). Por ejemplo, la incertidumbre relativa de \(0.31\,\%\) del coeficiente de absorción aporta aproximadamente \(0.31\,\%\) del valor medido. En cambio, resolución, ruido de señal, corrección residual de cero o una pérdida expresada como cantidad fija pueden aportar una magnitud casi constante. Esta clasificación depende del modelo y de la evidencia y no debe imponerse por conveniencia.

**Referencia exacta del bloque:** NISTIR 6963, **§§7–8, páginas impresas 9–10**, materiales y líneas; **§11, páginas impresas 14–15**, presupuesto. **40 CFR Part 50, Appendix D, §4.5.3.10** y *Federal Register*, página **70599**, página **5 del PDF**, corrección de longitud por pérdidas. JCGM GUM-6:2020, **§§5.5–5.9, páginas impresas 4–6**, identificación y representación de efectos. Eurachem/CITAC QUAM 2012, cap. 6, pp. editoriales 14–15 (PDF pp. 20–21), App. C, p. editorial 101 (PDF p. 107), y App. D, pp. editoriales 102–103 (PDF pp. 108–109).
