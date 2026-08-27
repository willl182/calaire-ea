# E14 — Recorrido documental de cadena metrológica

Enlaza con **M1** (trazabilidad). Abre la jornada de laboratorio (no requiere gases).

## Objetivo y componente ilustrado

Reconstruir la trazabilidad desde el patrón primario/SRP hasta el valor corregido usado por el UUT. Ilustra incertidumbre Tipo B, correcciones, cobertura, vigencia, dependencia y prevención de doble conteo.

## Instrumentos y montaje

No requiere generación de O₃. Usar certificado del patrón de transferencia, certificado superior citado, historial de verificaciones, manual del UUT, procedimiento vigente, identificación de software y la hoja de campo de E02.

## Procedimiento

1. Reunir documentos sin editar: certificado actual, certificado anterior, alcance del laboratorio, procedimiento, registro de recepción, mantenimiento y verificación.
2. Identificar el patrón por fabricante, modelo, serie y firmware.
3. Localizar mensurando, intervalo, matriz/base seca, ecuación de corrección, unidad, incertidumbre, `k`, cobertura, condiciones y fecha de vencimiento.
4. Seguir cada referencia citada hasta el nivel superior disponible. Marcar un eslabón no disponible como vacío, no como "trazable".
5. Verificar que la ecuación implementada en la hoja o software coincide con el certificado, incluido el signo del intercepto.
6. Tomar una indicación real y recalcular el valor corregido manualmente.
7. Construir una matriz "componente–fuente–cobertura–duplicado".
8. Comparar la presión del sensor usada por el software con la presión de celda declarada por certificado/procedimiento. Si no son la misma magnitud, abrir una acción técnica.
9. Revisar la vigencia al momento de la medición, no solo al momento del curso.
10. Cerrar con un estado: completo, condicionado o no demostrable.

**Tiempo:** 30–45 min.

## Tabla de registro

| eslabon | documento | emisor | codigo_version | patron_serie | mensurando | intervalo_nmol_mol | ecuacion_correccion | U_declarada | k | u_estandar | condiciones | fecha_emision | fecha_vigencia | referencia_superior | evidencia_disponible | cubre | no_cubre | posible_duplicado | estado | accion |
|---|---|---|---|---|---|---:|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|---|

## Modelo de cálculo

Para cada certificado: `u=U/k`. Para la ecuación `X=(I-b)/m`, sensibilidades:

\[
\frac{\partial X}{\partial I}=1/m,\quad
\frac{\partial X}{\partial b}=-1/m,\quad
\frac{\partial X}{\partial m}=-(I-b)/m^2=-X/m,
\]

\[
u^2(X)=\left(\frac{u(I)}{m}\right)^2+\left(\frac{u(b)}{m}\right)^2+\left(\frac{X u(m)}{m}\right)^2+\text{covarianzas}.
\]

No combinar la `U` global del certificado con filas internas que ya la componen.

## Ejemplo numérico trabajado

Certificado: `m=1.0030`, `b=−0.40 nmol/mol`, `U(X)=0.50+0.010X`, `k=2`, intervalo 0–200 nmol/mol. Indicación `I=99.90`:

\[
X=(99.90-(-0.40))/1.0030=100.00\ \mathrm{nmol/mol},\qquad
U=0.50+0.010(100)=1.50,\qquad u=0.75\ \mathrm{nmol/mol}.
\]

Si la hoja existente usaba `X=(I+b)/m`, el resultado sería `(99.90−0.40)/1.003=99.20 nmol/mol`: error documental de `−0.80 nmol/mol`. Resultado E14: cadena **condicionada/no conforme documentalmente** hasta corregir la fórmula, preservar los datos y recalcular las verificaciones afectadas. Si el certificado global ya cubre regresión y repetibilidad, no se añaden `u(m)` y `u(b)` otra vez.

## Criterios de aceptación

- Identificación única y coincidencia física de serie.
- Certificado vigente para la fecha de uso.
- Mensurando, unidad, intervalo y condiciones compatibles.
- Ecuación reproducida con error numérico <0.01 nmol/mol en caso de prueba.
- `U`, `k` y cobertura explícitos; referencias superiores localizables.
- Sin doble conteo en el presupuesto.
- Diferencia sensor–celda resuelta o declarada como limitación.

## Seguridad

No hay exposición a O₃ ni a NO. No se abren instrumentos para localizar el sensor de presión. Riesgo principal: aplicar una corrección incorrecta, un certificado vencido o atribuir trazabilidad sin cadena demostrada.
