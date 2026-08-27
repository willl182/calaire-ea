# E01 — Ruido y repetibilidad de cero

Enlaza con **M3** (Tipo A, `s` vs `s/√n`) y **M4** (plan de reemplazo, término absoluto `u₀`). Alimenta `u₀` de **E15**.

## Objetivo y componente ilustrado

Cuantificar ruido de lectura, repetibilidad de cero e incertidumbre del promedio operativo. Ilustra evaluación Tipo A, la diferencia entre `s` y `s/√n`, autocorrelación y el término absoluto `u₀`.

## Instrumentos y montaje

Generador de aire cero, UUT (analizador de O₃), distribuidor PFA/vidrio, línea PFA corta, medidor de flujo y adquisición a 1 s. Aire cero alimenta el UUT con excedente 10–20 %; bypass ventea a destructor catalítico/exterior (ver `checklist_montaje_seguridad.md` §2).

## Procedimiento

1. Calentar UUT y generador 2 h (o desde la noche anterior).
2. Ejecutar prueba de fugas y confirmar bypass.
3. Purgar con aire cero 15 min.
4. Esperar estabilidad común durante 5 min.
5. Registrar 30 min a 1 s, sin cambiar configuración: 1800 observaciones nominales.
6. Continuar 20 min y registrar simultáneamente medias de 1 min, o calcularlas desde datos de 1 s.
7. Repetir la serie completa tres veces en el mismo día, separando series con 5 min de aire cero estable. Para precisión intermedia, repetir en 3 días, dos series por día, si el cronograma del curso lo permite.
8. No ejecutar ajuste de cero entre series. Si un ajuste es obligatorio, cerrar la serie, guardar el estado encontrado y marcar la intervención.

**Tiempo activo:** 55–70 min.

## Tabla de registro

| fecha_hora | dia | operador | serie | segundo_desde_inicio | lectura_cruda_nmol_mol | media_1min_nmol_mol | T_amb_C | P_amb_kPa | flujo_L_min | estado_estable | ajuste_previo | incidencia |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|

## Modelo de cálculo

Para la serie `x_t`, media y desviación estándar:

\[
\bar x=\frac{1}{n}\sum x_t,\qquad s=\sqrt{\frac{\sum(x_t-\bar x)^2}{n-1}}.
\]

Autocorrelación muestral a retardo `k`:

\[
\rho_k=\frac{\sum_{t=1}^{n-k}(x_t-\bar x)(x_{t+k}-\bar x)}{\sum_{t=1}^{n}(x_t-\bar x)^2}.
\]

Sumar hasta el primer retardo donde las autocorrelaciones dejan de ser positivas, o un máximo razonable antes de ruido numérico:

\[
n_{ef}=\frac{n}{1+2\sum_{k=1}^{K}\left(1-\frac{k}{n}\right)\rho_k}.
\]

Aproximación AR(1), útil como comprobación:

\[
n_{ef}\approx n\frac{1-\rho_1}{1+\rho_1}.
\]

Incertidumbre de la media:

\[
u(\bar x)=\frac{s}{\sqrt{n_{ef}}}.
\]

Término absoluto recomendado para una **lectura operativa de 1 min**:

\[
u_0=\sqrt{s_{1min}^2+u^2(\bar z)+u^2_{residual,aire\ cero}},
\]

sin agregar resolución si ya está visible dentro de la dispersión observada.

## Ejemplo numérico trabajado

Serie resumida de 30 medias de 1 min: `n=30`, media `0.18 nmol/mol`, `s=0.31 nmol/mol`. Autocorrelaciones positivas: `ρ1=0.55`, `ρ2=0.30`, `ρ3=0.12`; el siguiente valor es negativo, por tanto `K=3`.

\[
D=1+2[(29/30)0.55+(28/30)0.30+(27/30)0.12]=2.840,
\qquad n_{ef}=30/2.840=10.56.
\]

Si el resultado es la media de 30 min:

\[
u(\bar x)=0.31/\sqrt{10.56}=0.095\ \mathrm{nmol/mol}.
\]

Usar `n=30` sin corregir habría dado `0.057 nmol/mol`, una subestimación de 40 %. Para un resultado operativo de una media de 1 min, el ruido relevante es `s₁min=0.31 nmol/mol`, no 0.095; sin embargo, `u(\bar x)=0.095` sí describe la incertidumbre de la media de 30 min y se conserva como término adicional cuando el presupuesto final combina ambos resultados (media de 1 min y media de sesión). Tomando el residual de aire cero de **E09** (`u_{aire0,A}=0.122 nmol/mol`, ver `E09_calidad_aire_cero.md`):

\[
u_0=\sqrt{s_{1min}^2+u^2(\bar x)+u^2_{residual,aire\ cero}}
=\sqrt{0.31^2+0.095^2+0.122^2}=\sqrt{0.120009}=0.346\approx0.35\ \mathrm{nmol/mol}.
\]

## Criterios de aceptación

- Media de cero, estado encontrado: `|x̄|≤1.0 nmol/mol`; objetivo interno recomendado `≤0.5 nmol/mol`.
- `s₁min≤0.50 nmol/mol`; comparar además con la especificación del fabricante para 60 s.
- Sin tendencia lineal absoluta >0.5 nmol/mol en 30 min.
- Si `n_ef/n<0.25`, revisar el filtro digital y aumentar la duración; no "arreglar" dividiendo por √n nominal.
- **Comparación explícita con el fabricante:** Thermo 49i Table 1-1 declara ruido de cero de `0.25 ppb RMS` a 60 s. El ejemplo numérico de esta sección (`s₁min=0.31 nmol/mol`) **excede** esa especificación (0.31 > 0.25): con este resultado, el equipo evaluado no cumpliría la especificación del fabricante para ruido de cero y debe investigarse (filtro digital, ambiente, línea) antes de aceptar el estado encontrado como normal.

## Seguridad

No se genera O₃ en este experimento, pero el venteo sigue conectado porque el sistema puede conservar O₃ residual. Riesgos: ingreso de aire ambiente por bypass, condensación, ajuste automático durante la serie y falsa independencia por filtro digital. Ver checklist §1 y §2.
