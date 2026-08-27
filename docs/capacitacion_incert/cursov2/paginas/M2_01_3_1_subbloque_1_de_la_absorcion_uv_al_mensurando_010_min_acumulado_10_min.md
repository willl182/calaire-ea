# M2 — Página 01 — 3.1 Subbloque 1 — De la absorción UV al mensurando (0–10 min; acumulado: 10 min)

- **Sesión:** M2
- **Fuente:** [`modulos/M2_modelo_medicion.md`](../modulos/M2_modelo_medicion.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.1 Subbloque 1 — De la absorción UV al mensurando (0–10 min; acumulado: 10 min)

**Idea fuerza:** el fotómetro no observa directamente una fracción molar; observa una disminución de intensidad y la convierte mediante un modelo físico.

**Guion dictable:** Comencemos por separar tres elementos. El mensurando es la fracción molar de ozono que queremos atribuir al gas. Las observaciones primarias son dos intensidades ópticas: \(I_0\), obtenida para una condición de referencia sin absorción de ozono, e \(I\), obtenida cuando el ozono está presente en el trayecto óptico. El puente entre ambas observaciones y el mensurando es la ley de Beer–Lambert.

Antes de modelar, debe especificarse qué resultado se atribuirá. «Concentración de ozono» es insuficiente. Una formulación adecuada para el caso fotométrico es: «fracción molar de O₃ en aire seco dentro de la celda fotométrica, en nmol mol⁻¹, atribuida mediante Beer–Lambert bajo T y P medidas». QUAM establece una declaración inequívoca del mensurando y un modelo coherente con ella (QUAM cap. 5, pp. editoriales 12–13; PDF pp. 18–19).

Para un resultado de estación debe declararse, no presuponerse, si el mensurando incluye línea, filtro, acondicionamiento, intervalo de promedio y representatividad espacial o temporal. Esas fronteras determinan qué fuentes pertenecen al presupuesto fotométrico y cuáles pertenecen al resultado operativo de red.

La transmitancia se define como

\[
D=\frac{I}{I_0}.
\]

La formulación reglamentaria expresa

\[
\text{Transmittance}=\frac{I}{I_0}=e^{-\alpha c l},
\]

y, al despejar la concentración expresada en partes por millón,

\[
c(\text{ppm})=-\frac{10^6}{\alpha l}\ln\left(\frac{I}{I_0}\right).
\]

La lectura física es directa. Sin absorción, \(I\) e \(I_0\) son casi iguales, \(D\) se aproxima a uno y \(\ln D\) se aproxima a cero. Al aumentar la cantidad de ozono en el camino óptico, disminuye \(D\), el logaritmo se hace más negativo y el signo negativo situado delante de la expresión produce una concentración positiva.

**Apoyo en el handout:** ver Handout teórico, §1.1 — Mensurando y resultado de medición, y §1.2 — Modelo de medición, para la separación entre mensurando, observaciones y modelo.

La regla final de la EPA de 2023 adopta para el coeficiente de absorción del ozono el valor \(304.39\ \text{atm}^{-1}\text{cm}^{-1}\), con incertidumbre estándar \(0.94\ \text{atm}^{-1}\text{cm}^{-1}\). La incertidumbre estándar relativa correspondiente es aproximadamente \(0.31\,\%\). Este parámetro fija la escala de la medición: una variación relativa en el coeficiente produce una variación relativa de igual magnitud y signo contrario en el resultado calculado.

**Referencia exacta del bloque:** Eurachem/CITAC QUAM 2012, cap. 5, pp. editoriales 12–13 (PDF pp. 18–19); EPA, final rule 2023; **40 CFR Part 50, Appendix D, §4.1**; *Federal Register*, página **70595**, página **1 del PDF**, ecuaciones \(\text{Transmittance}=I/I_0=e^{-\alpha c l}\) y \(c(\text{ppm})=-10^6(\alpha l)^{-1}\ln(I/I_0)\). NISTIR 6963, **§3, página impresa 7**, para el principio de fotometría UV.
