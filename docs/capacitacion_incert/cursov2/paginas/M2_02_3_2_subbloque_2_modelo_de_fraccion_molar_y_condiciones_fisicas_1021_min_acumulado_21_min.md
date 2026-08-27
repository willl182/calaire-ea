# M2 — Página 02 — 3.2 Subbloque 2 — Modelo de fracción molar y condiciones físicas (10–21 min; acumulado: 21 min)

- **Sesión:** M2
- **Fuente:** [`modulos/M2_modelo_medicion.md`](../modulos/M2_modelo_medicion.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.2 Subbloque 2 — Modelo de fracción molar y condiciones físicas (10–21 min; acumulado: 21 min)

**Idea fuerza:** temperatura y presión conectan la absorción observada con el número de moléculas y, por tanto, con la fracción molar.

**Guion dictable:** Para trabajar con fracción molar emplearemos como contenido maestro el modelo

\[
x=-\frac{k_B T\ln(D)}{\sigma L P},
\]

donde \(x\) es la fracción molar, \(k_B\) es la constante de Boltzmann, \(T\) es la temperatura termodinámica del gas, \(P\) es la presión absoluta, \(\sigma\) es la sección eficaz de absorción por molécula, \(L\) es la longitud óptica efectiva y \(D=I/I_0\) es la transmitancia.

Leamos el modelo antes de calcular. La temperatura aparece en el numerador: manteniendo fijas las demás magnitudes de entrada, una temperatura mayor produce una fracción molar calculada mayor. Presión, longitud óptica y sección eficaz aparecen en el denominador: si cualquiera aumenta mientras la absorción observada permanece fija, la fracción molar calculada disminuye. La transmitancia está dentro de un logaritmo y, por ello, su comportamiento no es simplemente proporcional.

El modelo obliga a revisar las unidades y la realización de cada magnitud. \(T\) debe ser temperatura termodinámica, no un valor Celsius insertado directamente. \(P\) debe ser presión absoluta, no manométrica. \(L\) debe representar el trayecto óptico efectivo y no solo una dimensión nominal. La definición y las unidades de \(\sigma\) deben ser compatibles con la formulación molecular. Si se usa el coeficiente \(\alpha\) en \(\text{atm}^{-1}\text{cm}^{-1}\), corresponde emplear la forma reglamentaria y las conversiones pertinentes, no sustituirlo automáticamente en la ecuación molecular.

QUAM distingue entre un **modelo físico racional**, que busca representar una relación física independiente del procedimiento, y un **resultado operacional**, cuya definición puede incorporar muestreo, acondicionamiento y promedio. Beer–Lambert es el núcleo físico; un resultado de red puede requerir factores o términos adicionales. Por ejemplo, sin imponerlos al modelo maestro:

\[
x_{resultado}=x_{BL}\,f_{linea}\,f_h+b_0,
\]

donde `f_linea` representa una corrección residual de transmisión, `f_h` una corrección residual de humedad y `b_0` una corrección aditiva de cero. Cada término se conserva solo si corresponde al mensurando y al sistema declarados, con su evidencia e incertidumbre.

La ecuación (4) de la regulación hace visibles correcciones equivalentes mediante los factores \(T/273\) y \(760/P\), junto con una corrección de longitud asociada a pérdidas de ozono. Esa escritura y el modelo basado en \(k_B\) representan la misma necesidad física: relacionar la absorción con las condiciones del gas y con el camino efectivo de las moléculas que llegan a la celda.

**Referencia exacta del bloque:** **40 CFR Part 50, Appendix D, §4.5.3.10**; *Federal Register*, página **70599**, página **5 del PDF**, ecuación (4), incluidos \(T/273\), \(760/P\) y la corrección de \(L\) por pérdidas. Handout teórico, **§1.2**, modelo de medición. JCGM GUM-6:2020, **§§5.5–5.9 y 6.1–6.7, páginas impresas 4–9**, para especificación y construcción del modelo. Eurachem/CITAC QUAM 2012, caps. 4–5, pp. editoriales 10–13 (PDF pp. 16–19), para flujo de evaluación, modelos racionales y mensurandos operacionales; ejemplo A5, pp. editoriales 72–80 (PDF pp. 78–86).
