# E15 — Presupuesto híbrido del equipo propio

Enlaza con **M7** por método, no por sustitución: aplica a evidencia propia el mismo procedimiento que el taller documental. Es el **entregable evaluado del Día 2**, independiente del entregable de M7 (caso KRISS/BIPM, `../casos/extracto_kriss_2024.md`), que conserva íntegro su rol de cierre del Día 1. El caso KRISS puede usarse aquí como contraste de orden de magnitud, sin que ninguno de los dos entregables reemplace al otro.

## Objetivo y componente ilustrado

Construir un presupuesto evaluado con evidencia propia y documental:

\[
u(c)=\sqrt{u_0^2+(u_r c)^2}.
\]

Integra E01/E09 como término absoluto, E02 como término relativo y residual, E06 como transporte, E08 como deriva y el certificado como patrón. Entrena la depuración anti-doble-conteo.

**Nota de agenda (A4):** en `P0_agenda_dia2.md`, **E09 se ejecuta en P1 como prerrequisito de E01** (su residual de aire cero alimenta directamente el `u₀` de E01). **E06 queda en P2** (bloque opcional); si el equipo no alcanza a ejecutar P2, el término de transmisión de línea se declara **documental** (supuesto conservador, no medido) y la limitación se anota explícitamente en la declaración final. El ejemplo numérico de esta sección asume que E06 sí se ejecutó (o que se dispone de una medición previa equivalente); si no es el caso, sustituya esa fila por el supuesto documental antes de calcular.

## Instrumentos y montaje

Hojas de E01, E02, E06, E08, E09, E11, certificados, manuales, calculadora/R y matriz de cobertura. Sin O₃ activo salvo verificación opcional.

## Procedimiento

1. Definir el resultado: media de cinco lecturas de 1 min del UUT, aire seco, puerto de muestra, intervalo 0–180 nmol/mol.
2. Dibujar ramas: patrón/generación, aire cero, transporte, respuesta UUT, deriva, T/P, datos.
3. Para cada candidato, registrar mecanismo, evidencia, periodo, condiciones y cobertura.
4. Elegir `u₀`: ruido/repetibilidad de la media operativa, residual de aire cero y deriva aditiva no cubierta.
5. Elegir `u_r`: pendiente/escala, incertidumbre relativa del patrón, transmisión proporcional y deriva de span no cubierta.
6. Separar términos locales no representables por la forma de dos parámetros; si son pequeños y conservadores, asignarlos justificadamente a `u₀` o `u_r`; si no, usar un modelo extendido.
7. Eliminar duplicados. Si `s_PI` ya cubre día, operador, ruido y ambiente, no conservar esas filas por separado.
8. Calcular a 0, 20, 100 y 180 nmol/mol.
9. Calcular la contribución porcentual a la varianza.
10. Validar el orden de magnitud contra residuos de E02, QC histórico o comparación independiente (incluyendo el caso KRISS como contraste externo).
11. Informar `u_c`; si se requiere `U`, declarar `k` y fundamento. Para el curso, `k=2` didáctico.

**Tiempo:** 90 min.

## Tabla de registro

| componente | mecanismo | evidencia | tipo_A_B | valor_original | PDF | divisor | u_estandar | forma_absoluta_relativa | coef_sensibilidad | contribucion_a_u0 | contribucion_a_ur | periodo_cubierto | condiciones_cubiertas | cubierto_por | duplicado_eliminado | fuente | calidad_evidencia | observacion |
|---|---|---|---|---:|---|---:|---:|---|---:|---:|---:|---|---|---|---|---|---|---|

## Modelo de cálculo

\[
u_0=\sqrt{\sum_j u_{0,j}^2},\qquad u_r=\sqrt{\sum_k u_{r,k}^2},\qquad u(c)=\sqrt{u_0^2+(u_rc)^2}.
\]

Si existe covarianza relevante, añadir términos cruzados; la forma simple supone independencia entre el grupo absoluto y el relativo.

## Ejemplo numérico trabajado

Filas depuradas, alineadas con los valores realmente calculados en cada experimento (no con supuestos redondeados independientes):

- Repetibilidad de media operativa y cero (**E01**, que ya incorpora el residual de aire cero de **E09**): `u₀=0.346 nmol/mol` absoluta (ver `E01_ruido_cero.md`, ejemplo recalculado con residual E09=0.122).
- Deriva de cero residual entre correcciones (**E08**, `a=0.55 nmol/mol` — no 0.60): `0.55/√3=0.318 nmol/mol` absoluta.
- Falta de ajuste residual **E02**: `0.25 nmol/mol` absoluta.
- Patrón: `0.60 %` → `u_r=0.0060`.
- Pendiente/precisión intermedia **E02**: `0.45 %` → `0.0045`.
- Transmisión de línea **E06** (valor medido en el ejemplo de `E06_transmision_linea.md`: `u(T̄)/T̄=0.00058/0.99033=0.0586 %`, no `0.30 %`): `u_r=0.00059`.
- Deriva de span residual **E08** (`a_r=0.00866`, no un límite documental de `0.50 %`): `0.00866/√3=0.00500`.

\[
u_0=\sqrt{0.346^2+0.318^2+0.25^2}=\sqrt{0.28334}=0.532\ \mathrm{nmol/mol},
\]

\[
u_r=\sqrt{0.0060^2+0.0045^2+0.00059^2+0.00500^2}=\sqrt{0.0000816}=0.00903.
\]

\[
u(20)=\sqrt{0.532^2+(0.00903\times20)^2}=0.562,\quad
u(100)=\sqrt{0.532^2+0.903^2}=1.048,\quad
u(180)=\sqrt{0.532^2+1.625^2}=1.710\ \mathrm{nmol/mol}.
\]

Con `k=2`: `U(100)=2.10 nmol/mol`, `U(180)=3.42 nmol/mol`. A 100 nmol/mol, fracción de varianza proporcional `=0.903²/1.098=74.2 %`: prioridad, patrón/pendiente.

## Criterios de aceptación

- Cada fila tiene mecanismo, fuente, PDF, unidad y cobertura.
- Ninguna cifra global se combina con componentes que ya contiene.
- La predicción del presupuesto es compatible con verificaciones independientes: al menos 95 % de diferencias históricas dentro de aproximadamente `±2u(c)` cuando las condiciones son comparables, sin usar los mismos datos como única validación.
- El presupuesto se usa solo dentro del intervalo y las condiciones evaluados.
- Cerca de cero se informa incertidumbre absoluta; no un porcentaje infinito.

## Seguridad

Riesgo metrológico: falsa precisión, doble conteo y usar tres ciclos como evidencia anual. Si se hace verificación adicional, aplicar el venteo de O₃ común (checklist §2).

## Declaración final

> Para el mensurando y condiciones definidos, el equipo presenta una incertidumbre estándar modelada como `u(c)=√(u₀²+(uᵣc)²)` nmol/mol, con `u₀=[valor] nmol/mol` y `uᵣ=[valor]`. Resultado válido entre `[mínimo, máximo] nmol/mol`, con promedio de cinco lecturas de 1 min, líneas y aire cero evaluados, y política de corrección indicada. Incertidumbre expandida `U=ku(c)` solo cuando se declare `k`, cobertura y regla de decisión.
