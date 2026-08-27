# E02 — Verificación multipunto O₃, tres ciclos

Enlaza con **M5** (calibración multipunto, deriva y verificación). Alimenta `u_r`, residual local y precisión intermedia de **E15**.

**Prerrequisito de agenda:** en `P0_agenda_dia2.md`, **E11 (versión mínima, 30 min) se ejecuta antes de E02**, dentro de P1, para fijar con evidencia propia la espera mínima de estabilización usada en el paso 7 de este protocolo. No se usa la constante de tiempo del manual como sustituto.

## Objetivo y componente ilustrado

Verificar la relación entre patrón y UUT, cuantificar pendiente, intercepto, falta de ajuste, incertidumbre de predicción y estabilidad entre ciclos.

## Instrumentos y montaje

Patrón certificado y UUT en paralelo desde el mismo distribuidor; calibrador con O₃; aire cero; líneas PFA de longitud semejante; flujo excedente 10–20 %; venteo seguro a destructor/exterior.

## Procedimiento

1. Calentar 2 h. Verificar vigencia y ecuación del certificado del patrón.
2. Probar fugas con aire cero. Registrar presiones de distribuidor, sensor y celda si existe medición aprobada.
3. Purgar 10 min con aire cero.
4. Acondicionar 20 min a 180 nmol/mol.
5. Volver a cero y esperar estabilidad.
6. Ejecutar tres ciclos independientes, cada uno con cero previo, seis niveles y cero posterior:
   - Ciclo 1 ascendente: `0, 20, 40, 70, 100, 140, 180, 0`.
   - Ciclo 2 descendente: `0, 180, 140, 100, 70, 40, 20, 0`.
   - Ciclo 3 pseudoaleatorio fijo: `0, 70, 180, 20, 140, 40, 100, 0`.
7. En cada cambio, purgar al menos tres constantes de tiempo del sistema, nunca menos de 3 min. Luego aplicar el criterio de estabilidad común.
8. Después de la estabilidad, registrar cinco medias consecutivas de 1 min de patrón y UUT. El resultado del punto es la media de los cinco valores; conservar los cinco.
9. Entre ciclos, mantener aire cero 10 min y confirmar cero estable. No ajustar el UUT.
10. Si un punto falla la estabilidad después de 15 min, registrarlo como no estable y revisar el montaje antes de repetir. No eliminarlo silenciosamente.

**Tiempo:** 55–70 min por ciclo; total 3–3.5 h.

## Tabla de registro

| fecha_hora | ciclo | orden | punto | nivel_nominal_nmol_mol | replica_1min | indicacion_ref_cruda_nmol_mol | valor_ref_corregido_X_nmol_mol | lectura_UUT_nmol_mol | diferencia_d_nmol_mol | T_celda_K | P_sensor_kPa | P_celda_kPa | flujo_ref_L_min | flujo_UUT_L_min | tiempo_estabilizacion_min | estable | incidencia |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Modelo de cálculo

Corrección de certificado:

\[
X_i=(I_{ref,i}-b_{ref})/m_{ref}.
\]

Por ciclo, ajuste OLS:

\[
y_i=b_0+m_0X_i+e_i,\qquad e_i=y_i-(b_0+m_0X_i),\qquad
s_{y/x}=\sqrt{\frac{\sum e_i^2}{N-2}}.
\]

Incertidumbre estándar de predicción de una **media de `r` lecturas** en el nivel `x₀`:

\[
u_{pred}(x_0)=s_{y/x}\sqrt{\frac{1}{r}+\frac{1}{N}+\frac{(x_0-\bar X)^2}{\sum(X_i-\bar X)^2}}.
\]

Sumando la incertidumbre del patrón si no está incluida en el residual:

\[
u_{ver}(x_0)=\sqrt{u_{pred}^2(x_0)+m_0^2u_X^2(x_0)}.
\]

Precisión intermedia con `D` días y `r` réplicas por día:

\[
s_{pooled}=\sqrt{\frac{\sum_{d=1}^{D}(r_d-1)s_d^2}{\sum_{d=1}^{D}(r_d-1)}},
\qquad
s_{dia}=\sqrt{\max\left(0,\frac{MS_{dia}-MS_{dentro}}{r}\right)},
\qquad
s_{PI}=\sqrt{MS_{dentro}+s_{dia}^2}.
\]

## Ejemplo numérico trabajado

Certificado: `m_ref=1.003`, `b_ref=-0.4 nmol/mol`. Ciclo 1, indicaciones de referencia crudas `[-0.40, 19.66, 39.72, 69.81, 99.90, 140.02, 180.14]` → `X≈[0,20,40,70,100,140,180]`. Medias UUT: `[0.30,20.50,40.60,70.75,100.85,141.05,181.45]`.

Ajuste OLS real de estos siete puntos: `y=0.3350+1.00574·X`, con residuos `[-0.035, 0.050, 0.036, 0.013, -0.059, -0.088, 0.082]` nmol/mol (en el orden `X=0,20,40,70,100,140,180`) y `s_y/x=0.0681 nmol/mol`. `Σ(X-X̄)²=25685.7` con `X̄=78.57`.

Para una lectura individual (`r=1`) en `x₀=180`, `N=7`:

\[
u_{pred}=0.0681\sqrt{1+\frac17+\frac{(180-78.57)^2}{25685.7}}
=0.0681\sqrt{1+0.1429+0.4005}=0.0681\times1.2423=0.086\ \mathrm{nmol/mol}.
\]

Con `U_X=0.5+0.01X=2.3 nmol/mol`, `k=2` → `u_X=1.15 nmol/mol`:

\[
u_{ver}=\sqrt{0.086^2+(1.006\times1.15)^2}=1.16\ \mathrm{nmol/mol}.
\]

Tres pendientes (ciclo 1 recalculado, ciclos 2 y 3 sin cambio): `1.0057, 1.0110, 1.0200`; media `1.0122`, `s_m=0.00723` (cumple `<0.0075`, al límite). Interceptos: `0.3350, 0.55, 1.10`; media `0.6617`, `s_b=0.395 nmol/mol` (cumple `<1.00`).

Precisión intermedia a 100 nmol/mol, tres días, tres réplicas, con `MS_dentro=(0.04+0.09+0.0625)/3=0.0642` (equivalente a `SS_dentro/(N-D)=[2(0.04+0.09+0.0625)]/6=0.385/6=0.0642`) y `MS_dia=r·s²_{medias\ diarias}=3(0.303)=0.909`: `s_dia=√[(0.909-0.0642)/3]=√0.2816=0.531`, `s_PI=√(0.0642+0.531²)=√0.34616=0.588 nmol/mol`.

### Ciclo 4 — ejemplo ilustrativo no conforme

Para practicar la rama de rechazo (defecto D8: el dataset sintético de M5 es todo-conforme; esta variante corrige esa ausencia), considere un cuarto ciclo hipotético con pendiente `m₄=1.035` (fuera del rango `0.97–1.03`) e intercepto `b₄=0.40 nmol/mol` (dentro de rango), obtenido, por ejemplo, tras una deriva de span no detectada entre ciclos.

**Árbol de decisión estado-encontrado → investigar → ajustar:**

1. **Estado encontrado:** no se ajusta el UUT al detectar `m₄=1.035>1.03`. Se documenta el ciclo completo, incluida la falla, antes de cualquier intervención.
2. **Investigar (obligatorio antes de ajustar):**
   - ¿La pendiente de los ciclos 1–3 ya mostraba tendencia hacia 1.035, o el salto es abrupto? Un salto abrupto sugiere evento puntual (fuga, cambio de certificado, error de montaje); una tendencia gradual sugiere deriva real de span.
   - ¿El aire cero y los ceros pre/post del ciclo 4 son coherentes con los ciclos anteriores? Si el cero también se desvía, revisar contaminación o fuga antes de atribuir el efecto solo a la pendiente.
   - ¿El certificado del patrón sigue vigente y su ecuación fue aplicada correctamente en este ciclo?
   - ¿Las condiciones (T, P, flujo, tiempo de estabilización) del ciclo 4 son comparables a los ciclos 1–3?
3. **Decisión:**
   - Si la investigación no identifica causa asignable y la pendiente se mantiene fuera de rango en una repetición, el ciclo 4 se reporta como **no conforme**; se documenta el estado encontrado y se activa el procedimiento de ajuste/recalibración autorizado, no un ajuste ad hoc durante la práctica.
   - Si se identifica una causa técnica puntual (por ejemplo, fuga corregible), se corrige la causa, se repite el ciclo con el mismo protocolo y se reevalúa; el ciclo original con la falla queda conservado en el registro, no se sobrescribe.
   - Un ajuste solo se ejecuta tras documentar el estado encontrado completo y conforme al procedimiento autorizado del sistema de calidad; nunca como reacción inmediata dentro del mismo bloque de trabajo.

## Criterios de aceptación

- Para `X≤50`: `|d|≤1.5 nmol/mol`.
- Para `X>50`: `|100d/X|≤3.1 %`.
- Pendiente por ciclo: `0.97–1.03`. Intercepto: `−3 a +3 nmol/mol`.
- `s` de pendientes `<0.0075`; `s` de interceptos `<1.00 nmol/mol`.
- Residuos sin curvatura ni tendencia temporal. Un punto no estable invalida la decisión hasta investigar.
- La aceptación no incorpora automáticamente la incertidumbre del patrón; la regla de decisión real debe estar definida por el sistema de calidad.

## Seguridad

O₃ alto: venteo obligatorio a destructor/exterior (checklist §2). Riesgos: sobrepresión/depresión por bypass, adsorción en líneas, diferencias de tiempo entre ramas, cambio de escala automática y ajuste inadvertido.
