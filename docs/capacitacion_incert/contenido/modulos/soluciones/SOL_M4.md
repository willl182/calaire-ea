# Solución M4 — Presupuesto Tipo B del analizador a 120 nmol/mol

## 1. Enunciado resumido

Construya el presupuesto Tipo B del analizador 49i para una indicación de 120 nmol/mol, usando numéricamente 120 ppb, escala completa de 200 ppb, coeficientes de sensibilidad unitarios e independencia entre componentes. Calcule el total, ordene las contribuciones, audite las filas marcadas como **SUPUESTO** y realice la comparación solicitada con el APOA-370 sin formar un total para este último.

## 2. Solución paso a paso

### 1. Modelo y conversiones

Para cada componente expresado directamente en ppb equivalentes:

\[
u_i(y)=|c_i|u(x_i), \qquad c_i=1.
\]

Las conversiones aplicables son:

- cifra RMS tratada como incertidumbre estándar: \(u=x\);
- límite bilateral \(\pm a\), con PDF rectangular: \(u=a/\sqrt{3}\);
- incertidumbre expandida de certificado: \(u=U/k\).

La combinación de componentes independientes y la participación en la varianza son:

\[
u_c(y)=\sqrt{\sum_i u_i^2(y)},
\qquad
p_i=100\frac{u_i^2(y)}{u_c^2(y)}.
\]

### 2. Conversión de cada entrada

1. **Ruido RMS**

   \[
   u_1=0.25\ \text{ppb}.
   \]

2. **Deriva de cero en 24 h**, límite de 1.0 ppb, rectangular

   \[
   u_2=\frac{1.0}{\sqrt3}=0.5774\ \text{ppb}.
   \]

3. **Deriva de span en 24 h**, entrada precargada como 1 % de la lectura de 120 ppb, rectangular

   \[
   a_3=0.01(120\ \text{ppb})=1.2\ \text{ppb},
   \]

   \[
   u_3=\frac{1.2}{\sqrt3}=0.6928\ \text{ppb}.
   \]

4. **Linealidad**, 1 % de la escala completa de 200 ppb, rectangular

   \[
   a_4=0.01(200\ \text{ppb})=2.0\ \text{ppb},
   \]

   \[
   u_4=\frac{2.0}{\sqrt3}=1.1547\ \text{ppb}.
   \]

5. **Efecto de presión**, límite equivalente de 0.36 ppb, rectangular

   \[
   u_5=\frac{0.36}{\sqrt3}=0.2078\ \text{ppb}.
   \]

6. **Resolución**, incremento de 0.1 ppb tratado como intervalo de redondeo, con semiancho de 0.05 ppb y PDF rectangular

   \[
   a_6=\frac{0.1}{2}=0.05\ \text{ppb},
   \]

   \[
   u_6=\frac{0.05}{\sqrt3}=0.0289\ \text{ppb}.
   \]

7. **Certificado de calibración**, \(U=1.8\) ppb y \(k=2\)

   \[
   u_7=\frac{U}{k}=\frac{1.8}{2}=0.9000\ \text{ppb}.
   \]

### 3. Presupuesto, contribuciones y ranking

| Ranking | Componente | Dato de entrada | PDF y divisor | \(u_i(y)\) (ppb) | \(u_i^2\) (ppb²) | Varianza (%) |
|---:|---|---:|---|---:|---:|---:|
| 1 | Linealidad | 2.0 ppb | rectangular, \(\sqrt3\) | 1.1547 | 1.3333 | **43.5** |
| 2 | Certificado de calibración | \(U=1.8\) ppb, \(k=2\) | normal, 2 | 0.9000 | 0.8100 | **26.4** |
| 3 | Deriva de span 24 h | 1.2 ppb | rectangular, \(\sqrt3\) | 0.6928 | 0.4800 | **15.7** |
| 4 | Deriva de cero 24 h | 1.0 ppb | rectangular, \(\sqrt3\) | 0.5774 | 0.3333 | 10.9 |
| 5 | Ruido RMS | 0.25 ppb | normal, 1 | 0.2500 | 0.0625 | 2.0 |
| 6 | Efecto de presión | 0.36 ppb | rectangular, \(\sqrt3\) | 0.2078 | 0.0432 | 1.4 |
| 7 | Resolución | semiancho 0.05 ppb | rectangular, \(\sqrt3\) | 0.0289 | 0.0008 | 0.03 |
|  | **Suma** |  |  |  | **3.0632** | **100.0** |

El ranking es matemático: ordena las contribuciones incluidas, pero no demuestra que una entrada sea válida, pertinente o independiente.

### 4. Incertidumbre estándar combinada, expandida y relativa

Sustituyendo en la combinación cuadrática:

\[
\begin{aligned}
u_c
&=\sqrt{0.25^2+
\left(\frac{1.0}{\sqrt3}\right)^2+
\left(\frac{1.2}{\sqrt3}\right)^2+
\left(\frac{2.0}{\sqrt3}\right)^2+
\left(\frac{0.36}{\sqrt3}\right)^2+
\left(\frac{0.05}{\sqrt3}\right)^2+
\left(\frac{1.8}{2}\right)^2}\\
&=\sqrt{3.0632\ \text{ppb}^2}\\
&=1.7502\ \text{ppb}\approx1.75\ \text{ppb}.
\end{aligned}
\]

Con grados de libertad infinitos, el factor de cobertura al nivel previsto es aproximadamente \(k=2\):

\[
U=ku_c=2(1.7502\ \text{ppb})=3.5004\ \text{ppb}\approx3.5\ \text{ppb}.
\]

La incertidumbre expandida relativa respecto de 120 ppb es:

\[
W=100\frac{U}{y}
=100\frac{3.5004\ \text{ppb}}{120\ \text{ppb}}
=2.917\%\approx2.9\%.
\]

### 5. Auditoría de las filas **SUPUESTO**

| Fila | Auditoría | Decisión para el ejercicio | Acción necesaria para un presupuesto defendible |
|---|---|---|---|
| Deriva de span 24 h | **Interpretación no respaldada.** La entrada usa 1 % de 120 ppb en 24 h, pero la especificación real del 49i es menor que 1 % **por mes**, incluyendo la deriva de transductores. También debe declararse con claridad si el porcentaje se aplica a la lectura o a la escala completa. | Se conserva sin modificar para reproducir el caso 1 y se marca como supuesto didáctico. | Sustituirla por el periodo correcto mediante un modelo temporal justificado o, preferiblemente, por datos de verificaciones de span del sistema real. No convertir “por mes” en “por 24 h” solo cambiando la etiqueta. |
| Efecto de presión | **Fuente adicional requerida.** El equivalente de 0.36 ppb no procede de la Table 1-1 citada. Falta documentar el cambio de presión considerado y el coeficiente que lo convierte a ppb. | Se mantiene como límite rectangular de 0.36 ppb únicamente para ejecutar el caso. | Aportar manual, estudio o ensayo que documente el intervalo de presión, la función de influencia, las condiciones y la posible inclusión del efecto en la calibración. |
| Resolución | **Fuente adicional requerida.** La cifra de 0.1 ppb no procede de la Table 1-1 citada. Además, debe confirmarse que representa el incremento digital; solo entonces es coherente usar un error de redondeo entre \(-0.05\) y \(+0.05\) ppb. | Se usa semiancho de 0.05 ppb y PDF rectangular. | Verificar la resolución en la documentación aplicable y evitar confundir resolución, ruido, sensibilidad mínima y límite de detección. Revisar solapamiento con otros componentes. |
| Certificado de calibración | **Fuente adicional requerida.** \(U=1.8\) ppb con \(k=2\) es una entrada supuesta y no una especificación de la Table 1-1. | Se convierte correctamente a \(u=0.9\) ppb. | Consultar el certificado real: mensurando, nivel, vigencia, trazabilidad, factor de cobertura y alcance. Confirmar si ya incorpora repetibilidad, presión, temperatura u otros efectos para impedir doble conteo. |

La deriva de cero, la linealidad y el ruido sí encuentran correspondencia en la Table 1-1, siempre que se conserven sus condiciones: deriva de cero en 24 h; linealidad de ±1 % de escala completa; y ruido de 0.25 ppb RMS para promedio de 60 s y condiciones compatibles.

### 6. Comparación prudente con el APOA-370

A una escala completa de 200 ppb, la linealidad del 49i y la del APOA-370 se expresan como ±1 % de escala completa; en ambos casos el límite numérico es:

\[
0.01(200\ \text{ppb})=2\ \text{ppb}.
\]

El APOA-370 también declara reproducibilidad de ±1 % de escala completa, equivalente a un límite de ±2 ppb en esa escala. Esta magnitud no debe sumarse automáticamente con linealidad o sensibilidad mínima porque podría existir solapamiento entre los efectos descritos.

Para deriva diaria, el APOA-370 declara ±1 % de escala completa por día tanto para cero como para span, es decir, ±2 ppb/día a 200 ppb de escala completa. Por su parte, el 49i declara deriva de cero menor que 1 ppb en 24 h y deriva de span menor que 1 % por mes. Por ello, la fila didáctica “deriva de span 24 h” no es homóloga a la especificación real del 49i ni debe presentarse como comparación diaria válida.

La sensibilidad mínima del APOA-370 es 0.5 ppb expresada como \(2\sigma\) para intervalos de 0.2 ppm o menores. Bajo una interpretación normal:

\[
1\sigma=\frac{0.5\ \text{ppb}}{2}=0.25\ \text{ppb}.
\]

Ese valor coincide numéricamente con el ruido de 0.25 ppb RMS del 49i, pero las denominaciones y condiciones no son idénticas: el 49i vincula su ruido a un promedio de 60 s. La coincidencia numérica no autoriza a declarar equivalencia metrológica. No se calcula un total del APOA-370 porque la ficha no resuelve pertinencia, independencia, correlaciones ni posibles solapamientos.

## 3. Resultado final destacado

> **Caso 1 a 120 nmol/mol:** \(u_c=1.75\ \text{ppb}\); \(U(k=2)=3.5\ \text{ppb}\); \(W=2.9\%\). El ranking comienza con **linealidad, 43.5 % de la varianza**; **certificado, 26.4 %**; y **deriva de span, 15.7 %**. La deriva de span de 24 h es un supuesto incompatible con el periodo real de **1 % por mes**; presión, resolución y certificado requieren fuente adicional.

## 4. Criterios de valoración

### Respuesta completa

- muestra las fórmulas de conversión, combinación, expansión y porcentaje relativo;
- sustituye los siete componentes con valores y unidades correctos;
- obtiene \(u_c\approx1.75\) ppb, \(U(k=2)\approx3.5\) ppb y \(W\approx2.9\%\);
- presenta el ranking completo e identifica 43.5 %, 26.4 % y 15.7 % para los tres componentes dominantes;
- audita explícitamente las cuatro filas **SUPUESTO**, incluida la diferencia entre 24 h y 1 % por mes;
- compara linealidad, reproducibilidad, derivas diarias y sensibilidad mínima del APOA-370 sin calcular un total ni equiparar condiciones distintas.

### Respuesta parcial

- aplica correctamente la combinación, pero omite sustituciones, unidades, ranking completo o alguna fila de auditoría;
- obtiene valores cercanos por redondeo, pero no justifica la PDF o el divisor de una o más entradas;
- compara ambos analizadores, pero no conserva claramente escala, periodo, condición o significado de \(2\sigma\);
- reconoce que existen supuestos, pero no indica qué evidencia hace falta para reemplazarlos.

### Respuesta incorrecta

- suma linealmente las incertidumbres estándar o trata todos los límites como incertidumbres estándar;
- usa 1 % de 120 ppb para la linealidad que está especificada respecto de la escala completa de 200 ppb;
- presenta la deriva de span del 49i como 1 % por 24 h sin advertir que la especificación real es por mes;
- atribuye presión, resolución o certificado a la Table 1-1;
- suma las especificaciones del APOA-370 para producir un total o declara equivalencia solo por coincidencia numérica;
- omite unidades o confunde incertidumbre estándar \(u_c\) con incertidumbre expandida \(U\).

## 5. Errores esperables del participante y notas para el instructor

- La plantilla del caso 1 se resuelve **sin corregir sus entradas** para que el cálculo reproducible y la auditoría documental sean actividades separadas.
- Antes de aceptar el ranking, pedir al participante que identifique procedencia, periodo, escala, PDF y posible doble conteo de cada fila.
- Destacar que “mayor contribución” no significa “entrada mejor sustentada”: la deriva de span ocupa el tercer lugar y, al mismo tiempo, es la fila con el problema documental más evidente.
- Aceptar pequeñas diferencias por redondeo, siempre que la suma de varianzas sea aproximadamente 3.0632 ppb² y los resultados redondeados coincidan.
- Para la comparación, exigir lenguaje prudente: una cifra de \(2\sigma\), una cifra RMS, reproducibilidad, linealidad y detección no son intercambiables sin revisar definiciones y condiciones.
