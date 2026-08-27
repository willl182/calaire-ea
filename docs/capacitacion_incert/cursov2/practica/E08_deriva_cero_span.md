# E08 — Deriva de cero y span 24 h/7 d (pasivo, precurso)

Enlaza con **M4**: es el experimento concreto del plan de reemplazo para deriva. **Debe iniciarse ≥7 días antes del Día 2 de laboratorio** (ver `P0_agenda_dia2.md`). Alimenta la deriva de **E15**.

## Objetivo y componente ilustrado

Cuantificar el cambio de cero y sensibilidad a 24 h y 7 d sin ajustes intermedios. Ilustra deriva temporal, precisión intermedia y la diferencia entre límite documental y evidencia propia.

## Diseño y preparación

Iniciar al menos 7 días antes. Usar el mismo patrón, fuente de aire cero, línea, flujo, escala y procedimiento. Programar verificaciones en `t=0`, `24 h` y `7 d`; ideal diario. En cada fecha, realizar cero y span de 150 nmol/mol, dos ciclos, cinco medias de 1 min por punto. Alternar operador A/B si el objetivo incluye operador; conservar operador único si se quiere aislar el equipo.

## Procedimiento

1. Día 0: calentamiento 2 h, fugas, 10 min aire cero, 20 min acondicionamiento O₃.
2. Registrar el estado encontrado del cero y span. No ajustar.
3. Mantener el UUT en operación normal entre fechas. Registrar apagados, mantenimiento, ambiente y cambios de consumibles.
4. A 24 h, repetir la misma secuencia y horario ±1 h.
5. Días 2–6, si es posible, repetir una vez al día.
6. Día 7, repetir dos ciclos completos.
7. Si el instrumento falla el criterio operativo y el procedimiento exige ajuste, guardar los datos previos, marcar la ruptura de serie y continuar como nueva fase.
8. Purgar con aire cero 10 min al terminar cada exposición.

## Tabla de registro

| fecha_hora | tiempo_desde_t0_h | dia | operador | ciclo | punto_cero_span | valor_ref_corregido_nmol_mol | lectura_UUT_nmol_mol | diferencia_nmol_mol | pendiente_span_relativa | T_C | P_kPa | flujo_L_min | horas_operacion | ajuste_desde_t0 | mantenimiento | estable | incidencia |
|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|---|

## Modelo de cálculo

Deriva de cero: `D_0(t)=z(t)-z(0)`.

Deriva de span absoluta y relativa, corrigiendo cero:

\[
S(t)=y_{span}(t)-z(t),\quad D_S(t)=S(t)-S(0),\quad D_{S,r}(t)=\frac{S(t)}{S(0)}-1.
\]

Si la deriva solo se conoce entre observaciones y se corrige en intervalos, modelo rectangular con semiancho igual al máximo cambio no corregido:

\[
u_{deriva}=a/\sqrt3.
\]

Para datos diarios, regresión temporal `d_t=\beta_0+\beta_1t+e_t`. No sumar la deriva como fila aparte si `s_PI` ya cubre el mismo periodo y política de corrección.

## Ejemplo numérico trabajado

Medias de cero: día 0 `0.20`, 24 h `0.75`, 7 d `1.65 nmol/mol`. `D_0(24h)=0.55`, `D_0(7d)=1.45 nmol/mol`.

Span bruto a 150: `150.40`, `150.60`, `150.55`. Corregido por cero: día 0 `150.20`, 24 h `149.85`, 7 d `148.90`.

\[
D_{S,r}(24h)=-0.233\%,\qquad D_{S,r}(7d)=-0.866\%.
\]

Si la corrección de cero es diaria y el máximo cambio entre correcciones es `a=0.55`: `u_deriva,0=0.55/√3=0.318 nmol/mol`. Si el span se verifica semanalmente y no se corrige entre medias, `a_r=0.00866` → `u_deriva,span,r=0.00500`, que a 150 nmol/mol contribuye `0.750 nmol/mol`. No usar a la vez estas filas y `s_PI` semanal si los mismos datos y efectos ya están contenidos.

## Criterios de aceptación

Basados en Thermo 49i como referencia didáctica, salvo especificación propia más aplicable:

- Deriva de cero `<1 nmol/mol/24 h`.
- Deriva de cero `<2 nmol/mol/7 d`.
- Deriva de span: comparar con la especificación real en su periodo; no convertir `<1 %/mes` en límite diario. Objetivo interno propuesto para 7 d: `|D_S,r|≤1 %`.
- Serie sin intervención no documentada.
- Si hay un cambio brusco, investigar antes de modelar como deriva aleatoria.

## Seguridad

Operación desatendida: verificar alarmas, flujo, extracción, destructor y políticas locales. No dejar generación continua de O₃ si el equipo no está aprobado para operación desatendida. Preferir verificaciones programadas con O₃ solo durante cada punto. Purga final con aire cero y venteo seguro (checklist §2).
