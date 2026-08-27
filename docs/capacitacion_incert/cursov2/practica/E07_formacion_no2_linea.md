# E07 — Formación de NO₂ en línea corta, larga y larga caliente

Enlaza con **M6** como experimento independiente. Mide la cinética real de formación de NO₂ en línea y documenta el defecto D6 (el dataset sintético de M6 Parte B subestima ~100× la cinética); ese ejercicio documental conserva su dataset y su propósito de decisión operativa.

## Objetivo

Medir el artefacto de formación de NO₂ por reacción NO+O₃ durante la residencia externa e interna; comparar tres configuraciones y validar el cálculo cinético.

## Instrumentos

Instrumentos comunes; líneas definidas; control térmico a 35 °C; mezclador capaz de entregar simultáneamente NO=180 y O₃=90 nmol/mol; analizador NOx; analizador O₃ cuando esté disponible.

## Procedimiento

1. **Caracterización geométrica, 10 min.** Medir longitud y DI; calcular volumen. Verificar caudal con patrón.
2. **Blancos, 10 min.** Aire cero y luego NO=180 sin O₃, 5 min cada uno. Confirmar que la diferencia NOx−NO no cambia por línea.
3. **Referencia de mezcla, 10 min.** Preparar NO=180 y O₃=90 nmol/mol en el punto de entrada. Confirmar caudales y ausencia de condensación.
4. **Línea corta A, 20 min.** Instalar 2 m, DI 4 mm, 1.0 L/min, 22 °C. Acondicionar 10 min o hasta estabilidad; registrar cinco medias de 1 min y variables internas.
5. **Purga, 5 min.** Desactivar O₃ y purgar con aire cero.
6. **Línea larga B, 25 min.** Instalar 8 m, DI 6 mm, 1.8 L/min, 28 °C. Acondicionar 15 min; registrar cinco medias.
7. **Purga, 5 min.**
8. **Línea larga caliente C, 30 min.** Misma geometría, 1.55 L/min, 35 °C. Esperar equilibrio térmico 10 min, acondicionar gas 10 min y registrar cinco medias.
9. **Secuencia inversa, 20 min.** Repetir A al final para comprobar deriva. Si A final difiere >1 nmol/mol de A inicial, invalidar la comparación o modelar la deriva.
10. **Análisis, 20 min.** Corregir blancos, calcular residencia total, predicción cinética y diferencia medida.

**Duración:** 155 min.

## Tabla de registro

| configuración | L (m) | DI (mm) | V (mL) | Q (L/min) | t_ext (s) | t_int (s) | T (°C) | P (kPa) | NO entrada | O₃ entrada | NO₂ entrada | NO₂ salida | NO₂ formado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A corta | 2 | 4 | | 1.00 | | 1.5 | 22 | | 180 | 90 | | | |
| B larga | 8 | 6 | | 1.80 | | 1.8 | 28 | | 180 | 90 | | | |
| C larga caliente | 8 | 6 | | 1.55 | | 1.8 | 35 | | 180 | 90 | | | |

## Modelo de cálculo

Volumen cilíndrico: `V=π(d/2)²L`. Residencia externa: `t_ext=V/Q`, `t=t_ext+t_int`. Densidad molecular: `n=P/(k_BT)·10⁻⁶` moléculas/cm³. Concentraciones moleculares iniciales: `A₀=x_NO·n`, `B₀=x_O3·n`. Para `-dA/dt=kAB`, `k=1.8×10⁻¹⁴ cm³ molécula⁻¹ s⁻¹` y `A₀≠B₀`, extensión `z`:

\[
R=\frac{A_0}{B_0}\exp[(A_0-B_0)kt],\qquad z=\frac{RB_0-A_0}{R-1},\qquad
x_{NO_2,form}=10^9\frac{z}{n}\ \mathrm{nmol/mol}.
\]

El modelo debe considerarse predicción de diseño: flujo no ideal, mezcla, perfil térmico, presión y reacción dentro del analizador requieren evaluación experimental (por eso este experimento reemplaza los valores de dataset).

## Ejemplo numérico trabajado

Para A, `L=2 m`, `d=4 mm`: `V=25.13 mL`. Con `Q=1.0 L/min=16.667 mL/s`: `t_ext=1.508 s`, `t=3.008 s`. A 22 °C y 101.325 kPa: `n=2.4865×10¹⁹ cm⁻³`; `A₀=4.4757×10¹²`, `B₀=2.2379×10¹²`. Resultado: `x_NO2,form=18.45 nmol/mol`.

| configuración | V mL | t_ext s | t_int s | t s | T °C | NO₂ formado corregido nmol/mol | consumo de NO inicial % |
|---|---:|---:|---:|---:|---:|---:|---:|
| A corta | 25.13 | 1.51 | 1.50 | 3.01 | 22 | 18.45 | 10.24 |
| B larga | 226.19 | 7.54 | 1.80 | 9.34 | 28 | 42.43 | 23.57 |
| C larga caliente | 226.19 | 8.76 | 1.80 | 10.56 | 35 | 45.13 | 25.07 |

Si NO₂ de entrada es 20 nmol/mol, las salidas cinéticas ideales serían 38.45, 62.43 y 65.13 nmol/mol antes de efectos de convertidor: cambio relativo respecto a NO₂ inicial de 92.2 %, 212.1 % y 225.7 % (no 0.9 %, 2.15 % y 3.1 %, valores del dataset original ahora corregidos — ver defecto D6 en `../datasets/dataset_nox_metadata.md`).

## Criterios de aceptación

- Geometría, caudal, T, P y residencia interna documentados.
- Repetición de A final compatible con A inicial dentro de 1 nmol/mol.
- Para uso rutinario, la formación permitida debe definirse por el objetivo de datos. El criterio didáctico de 2 % no es un límite universal.
- Con las condiciones dadas, la predicción excede ampliamente 2 % respecto al NO₂ inicial; las configuraciones no son aceptables sin corrección/rediseño.
- Preferir reducción de volumen, aumento de caudal compatible, separación de O₃ antes de la línea o modelación validada. La línea caliente no garantiza menor artefacto.
- Si la medición difiere del modelo más que la incertidumbre combinada, investigar mezcla, presión, temperatura real, pérdidas de O₃, residencia interna y respuesta temporal.

## Seguridad

Mezcla NO+O₃ forma NO₂ tóxico. Extracción y destructor de O₃ obligatorios. No calentar la línea sin control de temperatura y material compatible. Desactivar O₃ primero, purgar completamente y después cerrar NO. No desconectar la línea caliente o presurizada.
