# Handout — NO, NO₂ y NOₓ por quimioluminiscencia

## Propósito y alcance

Este handout apoya el módulo obligatorio M6 y resume el modelo, las fuentes y los controles necesarios para evaluar incertidumbre en NO, NO₂ y NOₓ por quimioluminiscencia. No sustituye el manual del equipo instalado, la edición normativa aplicable ni el procedimiento de la organización; las cifras del ejemplo EN 14211 y los datasets sintéticos se usan con alcance didáctico.

## 1 Qué mide sistema

Reacción de detección:

\[
\mathrm{NO+O_3\rightarrow NO_2^*+O_2},\qquad
\mathrm{NO_2^*\rightarrow NO_2+h\nu}.
\]

Detector responde a NO. Ruta sin convertidor produce canal NO. Ruta con convertidor produce canal NOₓ: NO original más NO derivado de NO₂ y, según selectividad, otras especies convertibles. NO₂ se calcula por diferencia.

## 2 Modelo mínimo y corregido

\[
c_{NO_2}=c_{NO_x}-c_{NO},
\qquad
c_{NO_2}=\frac{c_{NO_x}-c_{NO}}{\eta_c}.
\]

Usar segunda expresión solo cuando arquitectura y software no hayan aplicado corrección. Confirmar definición de salidas y ruta de calibración.

Coeficientes:

\[
\frac{\partial c_{NO_2}}{\partial c_{NO_x}}=\frac1\eta,
\quad
\frac{\partial c_{NO_2}}{\partial c_{NO}}=-\frac1\eta,
\quad
\frac{\partial c_{NO_2}}{\partial\eta}=-\frac{c_{NO_x}-c_{NO}}{\eta^2}.
\]

Con covarianza:

\[
u^2(c_{NO_2})=\frac{u^2(NO_x)+u^2(NO)-2\operatorname{cov}(NO_x,NO)}{\eta^2}
+\left(\frac{NO_x-NO}{\eta^2}\right)^2u^2(\eta).
\]

Fuentes comunes pueden generar correlación. En diferencia, correlación positiva puede reducir incertidumbre; debe justificarse.

## 3 Convertidor: tres preguntas distintas

- **Eficiencia:** ¿qué fracción de NO₂ se convierte?
- **Selectividad:** ¿qué otras especies generan respuesta?
- **Estabilidad:** ¿cómo cambia con temperatura, contaminación, edad y matriz?

Valor de eficiencia no es su incertidumbre. Diferencia respecto de 100 % tampoco equivale a incertidumbre estándar.

## 4 GPT

Titulación en fase gaseosa genera NO₂ mediante reacción de NO con O₃. Cadena requiere:

- patrón de NO y sus impurezas;
- caudales de NO, dilución y O₃ en base coherente;
- presión y temperatura;
- aire cero y fuente de O₃;
- residencia suficiente para reacción prevista;
- regresión de NO₂ indicado frente a NO₂ generado.

Modelo corto:

\[
NO_{2,ind}=b+\eta NO_{2,GPT}+\varepsilon.
\]

Pendiente representa eficiencia solo bajo supuestos del montaje y rango evaluado.

## 5 Muestreo y reactividad

Antes de cámara pueden ocurrir:

- pérdida de NO₂ en línea/filtro;
- formación de NO₂ por NO+O₃;
- condensación, memoria y respuesta lenta;
- cambio por material, depósitos y caída de presión.

Medir residencia total:

\[
t_{total}=t_{externo}+t_{interno},\qquad
t_{externo}=V/q
\]

con unidades coherentes. Minimizar volumen y longitud, controlar caudal y temperatura, revisar filtro y mantenimiento. EN 14211 reconoce fuentes de muestreo, pero ejemplo informativo no cuantifica todas.

## 6 Presupuesto Anexo F, ejemplo informativo

A 104 nmol/mol, BS EN 14211:2012 Anexo F publica suma de varianzas 30.4 (nmol/mol)² e incertidumbre combinada 5.5 nmol/mol. Con factor 2:

\[
U=11.0\ \mathrm{nmol/mol},\qquad W=10.6\%.
\]

Para interferentes distintos de H₂O, la regla de EN 14211/EN ISO 14956 consiste en sumar por separado respuestas positivas y negativas y conservar el grupo de mayor magnitud; H₂O se trata aparte. En el ejemplo, el valor 0.35 nmol/mol queda dominado por la respuesta a NH₃.

Fuentes dominantes: reproducibilidad de campo, promediación, convertidor y gas de calibración. Datos se parafrasean del ejemplo F.4, p. impresa 88. Anexo es informativo. Comparación con 15 % pertenece a contexto europeo descrito; no es criterio colombiano universal.

## 7 Lista de auditoría

1. Mensurando y base de fracción molar definidos.
2. NO₂ identificado como cálculo, no lectura directa.
3. Corrección del convertidor aplicada una sola vez.
4. Eficiencia, selectividad y estabilidad separadas.
5. GPT trazable: gas, caudales, O₃, condiciones y regresión.
6. Covarianza evaluada con signos del modelo.
7. Residencia externa e interna medida.
8. Interferencias y condensación evaluadas para matriz real.
9. Límites de aceptación separados de incertidumbre estándar.
10. Fuentes incluidas una sola vez.
11. Manual, modelo, rango y versión documental identificados.
12. Criterio regulatorio vigente verificado para contexto local.

## 8 Control documental

HORIBA APOA-370 es analizador de O₃ por absorción UV y no contiene convertidor NO₂→NO. El manual local APNA-370 (HORIBA Ambient NOx Monitor, 2021) está disponible; el operador debe confirmar si corresponde al equipo realmente instalado. No usar especificaciones APOA-370 en presupuesto NOx.

## 9 Referencias

- BS EN 14211:2012, quimioluminiscencia y Anexo F informativo.
- JCGM 100:2008, propagación con covarianzas.
- Doval Miñarro et al. (2011), formación NO₂ en línea.
- Gluck et al. (2003), convertidor y matriz en emisiones; transferencia no automática a aire ambiente.
- Pernigotti et al. (2013), calidad e incertidumbre NO₂.
