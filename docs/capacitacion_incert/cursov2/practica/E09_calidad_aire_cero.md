# E09 — Calidad de aire cero

Enlaza con **M4** (plan de reemplazo) y **M5**. Alimenta el término `u₀` de **E15** junto con E01.

**Prerrequisito de agenda (A4):** en `P0_agenda_practica.md`, E09 se ejecuta en **P1**, antes de **E01**, porque el residual de aire cero calculado aquí (`u_aire0,A=0.122 nmol/mol` en el ejemplo) es una entrada directa del ejemplo numérico de E01.

## Objetivo y componente ilustrado

Comparar tres fuentes de aire cero y estimar residual, contaminación o efecto de matriz. Ilustra sesgo de cero, selectividad y componente absoluto.

## Instrumentos y montaje

Tres fuentes: A generador usado en calibración, B cilindro o generador independiente, C aire cero alternativo certificado/depurado. Válvula selectora inerte, UUT y, si está disponible, fotómetro patrón. Mismos flujo y línea posterior al selector.

## Procedimiento

1. Calentar 2 h; comprobar fugas.
2. Purgar el colector común 10 min con la fuente A.
3. Ejecutar diseño balanceado `A-B-C-C-B-A`, reduciendo deriva temporal.
4. En cada cambio, purgar 5 min o tres volúmenes; esperar estabilidad 5 min.
5. Registrar diez medias de 1 min por bloque.
6. Después de C, exponer 10 min a 150 nmol/mol y volver a cada fuente para detectar memoria; registrar máximo transitorio y tiempo de recuperación.
7. Si el patrón posee sensibilidad insuficiente cerca de cero, usar diferencias pareadas en el UUT y declarar la limitación.

**Tiempo:** 60–90 min; versión mínima A-B-C con 5 medias: 45 min.

## Tabla de registro

| fecha_hora | bloque | fuente_cero | lote_serie | tratamiento | replica_1min | lectura_UUT_nmol_mol | lectura_patron_nmol_mol | diferencia_vs_A_nmol_mol | flujo_L_min | T_C | P_kPa | tiempo_purga_min | estable | max_transitorio_nmol_mol | tiempo_recuperacion_min | incidencia |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|

## Modelo de cálculo

Para la fuente `j`: `z̄_j`, `s_j`, `d_j=z̄_j-z̄_A`. Con bloques pareados: `u(d_j)=s(d_{j,b})/√B`.

\[
u_{aire0}=\sqrt{u^2(\bar z_j)+u^2_{estabilidad}+u^2_{referencia,cero}}.
\]

No sumar nuevamente ruido del UUT si `u(z̄_j)` ya proviene de la misma serie y el presupuesto usa el resultado de ese promedio.

## Ejemplo numérico trabajado

A: `0.12, 0.18` → media `0.15`. B: `0.48, 0.54` → media `0.51`, diferencias pareadas `0.36, 0.36`. C: `−0.05, 0.01` → media `−0.02`, diferencias `−0.17, −0.17`.

Con `s` dentro de bloque `0.20 nmol/mol`, diez medias por bloque: `u(media)=0.20/√10=0.063`. Estabilidad entre dos bloques A: semidiferencia `0.03`. Referencia cerca de cero `u=0.10`.

\[
u_{aire0,A}=\sqrt{0.063^2+0.03^2+0.10^2}=0.122\ \mathrm{nmol/mol}.
\]

B presenta sesgo frente a A de `+0.36 nmol/mol`; dentro del límite 0.5, pero requiere investigar el depurador. Si el máximo transitorio después de O₃ es `1.4 nmol/mol` y tarda 7 min, el criterio de memoria falla.

## Criterios de aceptación

- `|z̄_j|≤0.5 nmol/mol` respecto a la referencia disponible.
- Diferencia entre fuentes `≤0.5 nmol/mol`.
- `s₁min≤0.5 nmol/mol`.
- Tras O₃, transitorio ≤1.0 nmol/mol y recuperación a ±0.5 nmol/mol en ≤5 min.
- Fuente con olor, humedad, partículas o resultado inestable se rechaza aunque la media cumpla.

## Seguridad

Presión de cilindro si se usa fuente envasada, contaminación cruzada y desorción de O₃. Regulador compatible y asegurado. Ventear O₃ residual a destructor (checklist §2).
