# Solución M3 — Ejercicio Sabio 2030

## 1. Enunciado resumido

Convierta en incertidumbres estándar las especificaciones de ruido, deriva de cero, linealidad y generador del Sabio Model 2030. Para cada componente, indique Tipo A/B, PDF, tratamiento, unidad, supuesto justificativo y posible cobertura por otra cifra. Combine las cuatro componentes para caso base. Después evalúe, sin recalcular, qué filas no pueden mantenerse automáticamente si precisión intermedia incluye ruido y deriva.

## 2. Solución paso a paso

### 1. Ruido de cero

**Información original:**

\[
0.6\ \text{ppb RMS}
\]

1. Como **supuesto didáctico explícito**, el valor RMS se interpreta como incertidumbre estándar del ruido de una indicación individual, únicamente si definición, promedio y condiciones son compatibles.
2. El ejercicio adopta una **PDF normal centrada en cero como supuesto didáctico**; el dato RMS por sí solo no demuestra normalidad ni media cero. En un caso real debe verificarse definición y evidencia antes de asignar la forma.
3. Como el dato ya representa una desviación estándar, no se aplica divisor adicional:

\[
u_{\mathrm{ruido}}=0.6\ \text{ppb}.
\]

No se divide por \(\sqrt{3}\), porque no se proporcionó un intervalo de límites equiprobables. Tampoco se divide por \(\sqrt{n}\), porque el ejercicio caracteriza una indicación individual y no la media de \(n\) observaciones independientes.

### 2. Deriva de cero

**Información original:**

\[
|\delta_{\mathrm{deriva}}|<1.0\ \text{ppb en 24 h}.
\]

1. El límite se representa mediante el intervalo simétrico:

\[
-1.0\ \text{ppb}\leq \delta_{\mathrm{deriva}}\leq +1.0\ \text{ppb}.
\]

2. Se propone una **PDF rectangular**. Esta elección se justifica por máxima entropía: si solo se conocen límites finitos y no existe información que favorezca algún valor dentro del intervalo, la distribución uniforme es la PDF de máxima entropía sobre ese soporte.
3. El semiancho es:

\[
a_{\mathrm{deriva}}=1.0\ \text{ppb}.
\]

4. La incertidumbre estándar de una PDF rectangular es:

\[
u_{\mathrm{deriva}}=\frac{a_{\mathrm{deriva}}}{\sqrt{3}}
=\frac{1.0\ \text{ppb}}{\sqrt{3}}
=0.57735\ \text{ppb}
\approx 0.577\ \text{ppb}.
\]

El intervalo temporal de 24 h forma parte de la condición de validez de esta componente; el valor calculado corresponde al límite especificado para ese periodo.

### 3. Linealidad

**Información original:**

\[
\pm1\ \%\ \mathrm{FS},
\qquad
\mathrm{FS}=200\ \text{ppb}.
\]

1. La especificación está referida a la escala completa, no al punto seleccionado.
2. Se convierte el porcentaje a fracción adimensional:

\[
1\ \%=\frac{1}{100}=0.01.
\]

3. El semiancho absoluto del intervalo de linealidad es:

\[
a_{\mathrm{lin}}=0.01\times 200\ \text{ppb}=2.0\ \text{ppb}.
\]

Por tanto:

\[
-2.0\ \text{ppb}\leq \delta_{\mathrm{lin}}\leq +2.0\ \text{ppb}.
\]

4. Se propone una **PDF rectangular**. Por máxima entropía, la distribución uniforme es la elección que añade menos información no disponible cuando solo se conocen los límites y ningún valor interno es más plausible que otro.
5. La incertidumbre estándar es:

\[
u_{\mathrm{lin}}=\frac{a_{\mathrm{lin}}}{\sqrt{3}}
=\frac{2.0\ \text{ppb}}{\sqrt{3}}
=1.15470\ \text{ppb}
\approx 1.155\ \text{ppb}.
\]

### 4. Exactitud del generador

**Información original:**

\[
\pm1\ \%\ \text{del setpoint},
\qquad
C_{\mathrm{set}}=120\ \text{ppb}.
\]

1. La especificación se aplica al punto seleccionado de \(120\ \text{ppb}\), no a la escala completa.
2. Se convierte el porcentaje a fracción adimensional:

\[
1\ \%=0.01.
\]

3. El semiancho absoluto es:

\[
a_{\mathrm{gen}}=0.01\times120\ \text{ppb}=1.20\ \text{ppb}.
\]

Por tanto:

\[
-1.20\ \text{ppb}\leq \delta_{\mathrm{gen}}\leq +1.20\ \text{ppb}.
\]

4. Se propone una **PDF rectangular**. Esta es la PDF de máxima entropía cuando la información disponible se limita a un intervalo finito y no permite asignar mayor plausibilidad a posiciones particulares dentro de él.
5. La incertidumbre estándar es:

\[
u_{\mathrm{gen}}=\frac{a_{\mathrm{gen}}}{\sqrt{3}}
=\frac{1.20\ \text{ppb}}{\sqrt{3}}
=0.69282\ \text{ppb}
\approx 0.693\ \text{ppb}.
\]

### 5. Combinación del caso base

Bajo supuesto didáctico de independencia y \(c_i=1\):

\[
\begin{aligned}
u_c&=\sqrt{0.600^2+0.57735^2+1.15470^2+0.69282^2}\\
&=\sqrt{2.50667}\ \text{ppb}\\
&=1.583\ \text{ppb}.
\end{aligned}
\]

Este total corresponde solo a cuatro filas documentales del caso base. No demuestra por sí solo ausencia de solapamiento.

### 6. Cobertura por precisión intermedia hipotética

| Fila | ¿Puede quedar cubierta? | Decisión |
|---|---|---|
| Ruido | Sí, si precisión intermedia incluye dispersión de lecturas bajo mismo promedio y condiciones | No mantener automáticamente; documentar cobertura |
| Deriva de cero | Sí, si verificaciones abarcan periodo y cambios de cero pertinentes | No mantener automáticamente; documentar cobertura temporal |
| Linealidad | No necesariamente | Mantener solo si precisión intermedia no incorpora falta de ajuste en intervalo completo |
| Generador | No necesariamente; depende de si patrón/generación formó parte del QC | Revisar certificado, montaje y diseño del QC |

No se recalcula total híbrido porque no se entrega valor numérico de precisión intermedia ni cobertura completa. Regla correcta: sustituir filas cubiertas y sumar solo fuentes externas o no representadas.

## 3. Resultado final destacado

| Componente | Información original | Tipo A/B | PDF propuesta y justificación por información disponible | Conversión a incertidumbre estándar | Incertidumbre estándar | ¿Cubierta por otra cifra? |
|---|---|---|---|---|---:|---|
| Ruido de cero | \(0.6\ \text{ppb RMS}\) | Tipo B | Normal adoptada como supuesto didáctico; RMS compatible | RMS se trata como incertidumbre estándar; divisor \(1\) | \(0.600\ \text{ppb}\) | Sí, si cifra global incluye mismo ruido y promedio |
| Deriva de cero | \(<1.0\ \text{ppb}/24\ \text{h}\) | Tipo B | Rectangular: solo se conocen límites y no se favorecen valores internos | \(1.0\ \text{ppb}/\sqrt{3}\) | \(0.577\ \text{ppb}\) | Sí, si cifra global cubre deriva y periodo |
| Linealidad | \(\pm1\ \%\ \mathrm{FS}\), \(\mathrm{FS}=200\ \text{ppb}\) | Tipo B | Rectangular: solo se conoce intervalo finito | \((0.01\times200\ \text{ppb})/\sqrt{3}\) | \(1.155\ \text{ppb}\) | No automáticamente |
| Generador | \(\pm1\ \%\) del setpoint, setpoint \(=120\ \text{ppb}\) | Tipo B | Rectangular: solo se conoce intervalo finito | \((0.01\times120\ \text{ppb})/\sqrt{3}\) | \(0.693\ \text{ppb}\) | Depende de diseño de QC |

> **Resultado final destacado:** \(u_{\mathrm{ruido}}=0.600\ \text{ppb}\), \(u_{\mathrm{deriva}}=0.577\ \text{ppb}\), \(u_{\mathrm{linealidad}}=1.155\ \text{ppb}\) y \(u_{\mathrm{generador}}=0.693\ \text{ppb}\). Las cuatro componentes quedan expresadas como incertidumbres estándar y producen \(u_c\approx1.583\ \text{ppb}\) para caso base. Ante precisión intermedia que incluya ruido y deriva, esas filas no se mantienen automáticamente; no se calcula nuevo total sin dato y cobertura.

## 4. Criterios de valoración

### Completa

- Identifica el ruido RMS como incertidumbre estándar de \(0.6\ \text{ppb}\), sin dividirlo por \(\sqrt{3}\) ni por \(\sqrt{n}\).
- Clasifica las cuatro evaluaciones como Tipo B; adopta normal para ruido solo como supuesto didáctico compatible y rectangular para los tres límites por la información disponible.
- Usa exactamente \(\mathrm{FS}=200\ \text{ppb}\) para la linealidad y el setpoint de \(120\ \text{ppb}\) para el generador.
- Presenta explícitamente los semianchos, divisores, operaciones, resultados y unidades.
- Obtiene, con redondeo coherente, \(0.600\), \(0.577\), \(1.155\) y \(0.693\ \text{ppb}\), y \(u_c\approx1.583\ \text{ppb}\) para caso base.
- Identifica ruido y deriva como filas potencialmente cubiertas por precisión intermedia y evita recalcular escenario sin datos.

### Parcial

- El procedimiento conceptual es correcto, pero existe un error aritmético menor, una unidad omitida o una justificación incompleta de máxima entropía.
- Confunde de forma aislada escala completa y setpoint, pero muestra correctamente cómo convertir un límite porcentual rectangular a incertidumbre estándar.
- Presenta resultados correctos sin hacer explícito uno de los pasos intermedios requeridos.

### Incorrecta

- Divide el valor RMS por \(\sqrt{3}\) o por \(\sqrt{n}\) sin fundamento.
- Usa un valor de escala completa distinto de \(200\ \text{ppb}\), aplica la linealidad al setpoint o aplica la especificación del generador a la escala completa.
- Trata los límites como incertidumbres estándar sin convertirlos, asigna PDFs sin justificación compatible con la información disponible o mezcla unidades.
- Omite combinación del caso base o recalcula escenario hipotético sin valor ni cobertura de precisión intermedia.

## 5. Errores esperables del participante y notas para el instructor

- Recalcar que RMS se acepta aquí como desviación estándar del ruido de una indicación individual bajo las condiciones de la ficha; no es un límite rectangular.
- Hacer que las personas participantes distingan verbalmente \(1\ \%\) de escala completa, que produce \(2.0\ \text{ppb}\), de \(1\ \%\) del setpoint, que produce \(1.20\ \text{ppb}\).
- Señalar que máxima entropía no significa elegir siempre una PDF rectangular: con media y varianza conocidas y soporte no acotado, conduce a la normal; con solo límites finitos y ausencia de preferencias internas, conduce a la uniforme.
- Mantener trazabilidad de las cuatro componentes; combinar solo caso base. Escenario con precisión intermedia se resuelve por lógica de cobertura, no inventando total.
- Aceptar pequeñas diferencias por redondeo si los valores sin redondear y las unidades son correctos.
