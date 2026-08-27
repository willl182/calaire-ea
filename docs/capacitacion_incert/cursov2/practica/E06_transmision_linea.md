# E06 — Transmisión de línea O₃

Enlaza con **M4**: es uno de los experimentos concretos del plan de reemplazo (pérdidas de línea mediante prueba de transmisión). Alimenta el término `u_r` (transmisión) de **E15**.

## Objetivo y componente ilustrado

Cuantificar la pérdida o ganancia aparente causada por una línea real, sus uniones y filtro. Ilustra corrección de transporte, incertidumbre de razón y efecto proporcional externo al analizador.

## Instrumentos y montaje

Patrón o UUT estable, calibrador de O₃, válvula selectora inerte o reconexión controlada, línea A corta PFA `≤1 m` sin filtro y línea B real con longitud, codos y filtro usados en estación. Misma entrada/salida y flujo.

## Procedimiento

1. Calentar 2 h; prueba de fugas con aire cero.
2. Purgar ambas líneas 10 min con aire cero.
3. Acondicionar ambas 20 min a 150 nmol/mol.
4. Fijar 150 nmol/mol; flujo igual al uso real, tolerancia ±5 %.
5. Alternar secuencia `A-B-A-B-A-B` para separar deriva.
6. Tras cada cambio, purgar al menos `3V/q` y mínimo 3 min; esperar el criterio de estabilidad.
7. Registrar cinco medias de 1 min por configuración.
8. Repetir a cero para detectar contaminación/desorción.
9. Opcional: repetir a 50 nmol/mol para evaluar si el factor es proporcional.

**Tiempo:** 60–75 min.

## Tabla de registro

| fecha_hora | bloque | configuracion_A_B | longitud_m | diametro_interno_mm | material | filtro_id | nivel_nominal_nmol_mol | replica_1min | lectura_nmol_mol | flujo_L_min | T_C | P_kPa | tiempo_purga_min | tiempo_estabilizacion_min | incidencia |
|---|---:|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|

## Modelo de cálculo

Emparejar cada B con la media de A anterior y posterior interpolada:

\[
A_j^*=(A_{antes}+A_{despues})/2,\qquad T_j=B_j/A_j^*,
\]

\[
\bar T=\frac{1}{p}\sum T_j,\qquad L=1-\bar T,\qquad C_{linea}=1/\bar T,\qquad u(\bar T)=s(T)/\sqrt p.
\]

Con corrección `c_corr=c_obs/T`:

\[
u_r^2(c_{corr})\supset [u(T)/T]^2.
\]

## Ejemplo numérico trabajado

Medias A: `150.2, 150.0, 149.9, 149.7`. Medias B intermedias: `148.8, 148.5, 148.2`.

- B1: `A*=150.1`, `T1=0.99134`.
- B2: `A*=149.95`, `T2=0.99033`.
- B3: `A*=149.80`, `T3=0.98932`.

\[
\bar T=0.99033,\quad L=0.967\%,\quad C_{linea}=1.00977,\qquad s(T)=0.00101,\quad u(\bar T)=0.00058.
\]

Para lectura observada 120.0: `c_corr=120/0.99033=121.17 nmol/mol`; contribución por transmisión `u=121.17(0.00058/0.99033)=0.071 nmol/mol`.

## Criterios de aceptación

- Objetivo operativo: `T≥0.99` y pérdida ≤1.0 %; si el procedimiento local exige otro límite, usarlo predefinido.
- Diferencia entre `T` de 50 y 150 nmol/mol ≤0.5 % relativo.
- Sin aumento de cero >0.5 nmol/mol tras la exposición.
- Si la pérdida es estable pero significativa, corregir y presupuestar; si es variable o dependiente del tiempo, reemplazar línea/filtro.

## Seguridad

Riesgos: exposición al desconectar líneas, contaminación de filtro, bypass bloqueado y memoria de O₃. Antes de reconectar, bajar a aire cero; mantener venteo al destructor (checklist §2).
