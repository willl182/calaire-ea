# E11 — Tiempo de respuesta y criterio de estabilización

Enlaza con **M5**: fija la espera válida usada en E02.

## Objetivo y componente ilustrado

Medir `t10`, `t90`, tiempo de subida/bajada y validar la regla de espera antes de registrar. Ilustra el efecto dinámico y el sesgo por estabilización insuficiente.

## Instrumentos y montaje

Calibrador capaz de cambio rápido cero/span, distribuidor de bajo volumen, UUT, adquisición a 1 s y patrón opcional en paralelo. Línea representativa de uso.

## Procedimiento

1. Calentar 2 h; fugas y acondicionamiento 20 min a 150 nmol/mol.
2. Mantener cero hasta estabilidad 10 min.
3. Registrar 2 min de línea base a 1 s.
4. Cambiar rápidamente de 0 a 150 nmol/mol sin variar el flujo total; marcar el tiempo de válvula.
5. Registrar hasta estabilidad y mínimo 15 min.
6. Mantener 5 min estable.
7. Cambiar de 150 a 0; registrar mínimo 15 min.
8. Repetir tres ciclos.
9. Calcular `t10`, `t90` por interpolación y el primer instante en que el criterio `<1 nmol/mol en 5 min` permanece cumplido.
10. Comparar con la espera usada en E02.

**Tiempo:** 45–60 min; versión mínima un ciclo: 30 min.

## Tabla de registro

| fecha_hora | ciclo | direccion_subida_bajada | segundo | estado_valvula | lectura_nmol_mol | base_inicial_nmol_mol | meseta_final_nmol_mol | fraccion_respuesta | T_C | P_kPa | flujo_L_min | t10_s | t90_s | estabilidad_5min_cumple | incidencia |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Modelo de cálculo

Para la subida:

\[
f(t)=\frac{y(t)-y_0}{y_\infty-y_0}.
\]

`t10` y `t90` son primeros cruces interpolados de `f=0.10` y `0.90`; tiempo de respuesta `t_r=t_{90}-t_{10}`. Para bajada, usar la fracción restante `(y(t)-y∞)/(y0-y∞)`. Sesgo por registrar en `t`: `b_din(t)=y(t)-y∞`. Si respuesta de primer orden:

\[
y(t)=y_\infty-(y_\infty-y_0)e^{-t/\tau},\qquad t_{90}\approx2.303\tau.
\]

## Ejemplo numérico trabajado

Base `y0=0.2`, meseta `y∞=149.8 nmol/mol`. `y10=15.16`, `y90=134.84`. Cruces interpolados: `t10=22 s`, `t90=178 s`; `tr=t90-t10=156 s`. Para respuesta de primer orden, `t10=-τln(0.9)=0.1054τ` y `t90=-τln(0.1)=2.3026τ`, de modo que `tr=t90-t10=τ(2.3026-0.1054)=τ·ln9=2.1972τ`. Despejando: `τ=tr/ln9=156/2.1972=71.0 s`.

A 180 s la lectura era `135.2`; sesgo frente a la meseta `−14.6 nmol/mol`: registrar a 3 min sería inválido. El criterio de estabilidad se alcanza a 410 s = 6.8 min. Tres tiempos de estabilización: `6.8, 7.2, 6.6 min`; usar espera mínima 8 min antes de evaluar estabilidad, no un promedio fijo de 3 min.

## Criterios de aceptación

- `t90` según especificación del fabricante o procedimiento; si no existe, objetivo didáctico `≤180 s`.
- Diferencia subida/bajada de `t90` ≤20 %.
- Criterio de estabilidad cumplido en ≤10 min.
- Sobreimpulso ≤2 % del nivel.
- E02 debe usar una espera no menor que el máximo observado más verificación de estabilidad.

## Seguridad

Cambio de válvula puede alterar flujo/presión y simular respuesta. O₃ a 150 nmol/mol: venteo continuo a destructor/exterior; purgar con aire cero 10 min al terminar (checklist §2).
