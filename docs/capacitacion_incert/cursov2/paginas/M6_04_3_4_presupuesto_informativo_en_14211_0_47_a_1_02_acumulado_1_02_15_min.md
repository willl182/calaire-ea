# M6 — Página 04 — 3.4 Presupuesto informativo EN 14211 — 0:47 a 1:02; acumulado 1:02 (15 min)

- **Sesión:** M6
- **Fuente:** [`modulos/M6_no_nox_quimioluminiscencia.md`](../modulos/M6_no_nox_quimioluminiscencia.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.4 Presupuesto informativo EN 14211 — 0:47 a 1:02; acumulado 1:02 (15 min)

Anexo F de BS EN 14211:2012 es informativo. Ejemplo a límite horario de NO₂:

\[
l_h=104\ \mathrm{nmol/mol}.
\]

Verificación directa contra PDF, Anexo F, ejemplo F.4:

- suma de varianzas publicada: 30.4 (nmol/mol)²;
- incertidumbre combinada publicada: 5.5 nmol/mol;
- con factor de cobertura 2, incertidumbre expandida absoluta reconstruida: 11.0 nmol/mol;
- incertidumbre expandida relativa publicada: 10.6 %.

\[
W=100\frac{2(5.5)}{104}=10.6\%\text{, redondeado}.
\]

Para interferentes distintos de H₂O, EN 14211/EN ISO 14956 agrupa por signo: se suman por separado las respuestas positivas y negativas y se toma el grupo de mayor magnitud; H₂O se trata aparte. En el ejemplo, el valor 0.35 nmol/mol queda dominado por NH₃.

Valores estándar principales, parafraseados del ejemplo: repetibilidad cero (dos filas) 0.00 y 0.00; repetibilidad a concentración 0.09; falta de ajuste 0.90; presión de muestra 0.06; temperatura de muestra 0.26; entorno 0.44; tensión 0.02; H₂O 0.249; otros interferentes 0.35; promediación 2.70; reproducibilidad de campo 3.22; deriva cero 0.58; deriva span 1.44; diferencia muestra/calibración 1.04; convertidor 2.08; gas de calibración 2.08; gas cero 0.60 nmol/mol — 18 filas en total, coherentes con `plantillas/plantilla_presupuesto_nox.R`.

> **Nota de reconstrucción (defecto D1):** la suma de estas 18 filas redondeadas da `Σu_i²=31.4306 (nmol/mol)²` y `u_c=5.606 nmol/mol`, que **no** reproduce exactamente la suma publicada `30.4 (nmol/mol)²` ni `u_c=5.5 nmol/mol` del ejemplo EN 14211 (diferencia ≈3.4 % en varianza, por redondeo y reconstrucción). Ambos valores se reportan por separado; no se presenta 5.606 como reproducción exacta del total normativo. Ver comentario en `plantillas/plantilla_presupuesto_nox.R`.

Dominan reproducibilidad, promediación, convertidor y gas de calibración. Reducir contribuciones diminutas no mejora total de forma material. Comparación con 15 % solo corresponde al contexto europeo indicado; no presentarla como criterio colombiano universal.
