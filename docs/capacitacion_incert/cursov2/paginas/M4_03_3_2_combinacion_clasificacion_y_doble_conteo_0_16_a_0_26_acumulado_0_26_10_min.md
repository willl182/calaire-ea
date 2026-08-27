# M4 — Página 03 — 3.2 Combinación, clasificación y doble conteo — 0:16 a 0:26; acumulado 0:26 (10 min)

- **Sesión:** M4
- **Fuente:** [`modulos/M4_presupuesto_analizador.md`](../modulos/M4_presupuesto_analizador.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.2 Combinación, clasificación y doble conteo — 0:16 a 0:26; acumulado 0:26 (10 min)

**Idea fuerza:** la clasificación orienta prioridades, pero solo después de verificar el modelo y el origen de los datos.

**Guion dictable:**

“En el caso didáctico todas las entradas se expresan directamente en ppb equivalentes. Por eso el coeficiente de sensibilidad es uno. Supondremos independencia para practicar la combinación, aunque en una evaluación real esta hipótesis debe revisarse.”

Escriba:

\[
u_c(y)=\sqrt{\sum_i[c_i u(x_i)]^2},
\qquad
p_i=100\frac{[c_i u(x_i)]^2}{u_c^2(y)}.
\]

“La primera expresión combina las contribuciones estándar independientes. La segunda calcula la participación de cada componente en la varianza. Un porcentaje alto sugiere dónde conviene mejorar la evidencia o el desempeño. Sin embargo, una fuente omitida nunca aparecerá en la clasificación y una fila duplicada parecerá más importante de lo que realmente es.”

“Debemos vigilar especialmente el doble conteo. Si el certificado de calibración ya incorpora repetibilidad, presión o temperatura internas, no se agregan otra vez sin una desagregación coherente. Tampoco se suman como independientes ruido, detección y repetibilidad solo porque las tres cifras aparecen en un manual: pueden describir aspectos solapados.”

“Use dos clasificaciones simultáneas. La primera es participación matemática en la varianza. La segunda es calidad metrológica de evidencia: **verificada, extrapolada, supuesto o faltante**. Un porcentaje pequeño no legitima una fila sin fuente, y un porcentaje grande no confirma que esté bien modelada.”

“Para cada componente anotaremos su linaje: manual, certificado, ensayo propio o supuesto didáctico. La trazabilidad documental no es una columna decorativa; permite descubrir interpretaciones incorrectas antes de aceptar el total.”

**Referencias verificadas:** handout, §4.2, ley de propagación; §4.3, doble conteo; §4.4, presupuesto y contribuciones. JCGM 100:2008, §§5.1–5.2 y advertencia de §4.3.10, según el handout.
