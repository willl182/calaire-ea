# E03 — Covarianza medida entre canales NO y NOx

Enlaza con **M6/M8**. Alimenta la covarianza medida usada en **E16** y la corrección de u(NO2) en M6 §3.2.

## Objetivo

Estimar covarianza y correlación entre indicaciones simultáneas de NO y NOx bajo concentración estable; cuantificar la incertidumbre de la diferencia `D=X-N` usando independencia, covarianza medida y desviación estándar directa de diferencias.

## Instrumentos y montaje

Instrumentos comunes de la lista general (`checklist_montaje_seguridad.md` §1, §3, §4); cilindro de NO; diluidor; aire cero; adquisición de datos de ambos canales con sello temporal común.

## Procedimiento

1. **Preparación, 10 min.** Completar comprobaciones comunes. Desactivar corrección de eficiencia solo si el manual lo permite y registrar el estado. Seleccionar promedio de 60 s para el resultado principal; conservar datos de 1 s si están disponibles.
2. **Cero, 10 min.** Aire cero durante 5 min de acondicionamiento y registrar 5 pares de 1 min. Confirmar estabilidad.
3. **Generación, 5 min.** Generar NO de `200±10 nmol/mol` sin O₃. Usar caudales verificados. Mantener caudal y presión constantes.
4. **Estabilización, 10 min.** Acondicionar hasta que las medias móviles de NO y NOx cambien <1 nmol/mol en 5 min.
5. **Serie principal, 60 min.** Registrar al menos 60 pares sincronizados `(N_i,X_i)`, uno por minuto. No eliminar puntos por apariencia. Marcar eventos operativos.
6. **Chequeo de estacionariedad, 10 min.** Graficar o revisar primera y segunda mitad; calcular pendientes temporales. Si la deriva excede 1 nmol/mol/h o hay un salto operativo, repetir después de corregir la causa.
7. **Cierre, 5 min.** Volver a aire cero, purgar la línea de NO y cerrar el cilindro siguiendo la secuencia del laboratorio.
8. **Análisis, 20 min.** Calcular medias, desviaciones, covarianza, correlación, diferencias y autocorrelación de primer orden. Si los datos de 1 min tienen autocorrelación, no usar `n` nominal para la incertidumbre de la media.

**Duración estimada:** 130 min incluyendo análisis; adquisición útil: 60 min.

## Tabla de registro

| campo | unidad/forma |
|---|---|
| fecha, operador, analizador, firmware | texto |
| corrección de eficiencia | activada/desactivada/no configurable |
| concentración certificada de NO | µmol/mol |
| caudales NO, dilución y total | mL/min o L/min |
| temperatura, presión | °C, kPa |
| índice y hora | entero, ISO 8601 |
| `N_i`, `X_i` | nmol/mol |
| `D_i=X_i-N_i` | nmol/mol |
| temperatura convertidor, presión y caudal de muestra | unidades del equipo |
| bandera de estabilidad/evento | texto |

## Modelo de cálculo

Para `n` pares:

\[
\bar N=\frac1n\sum N_i,\quad \bar X=\frac1n\sum X_i,\qquad
s_N^2=\frac{\sum(N_i-\bar N)^2}{n-1},\quad s_X^2=\frac{\sum(X_i-\bar X)^2}{n-1},
\]

\[
s_{XN}=\operatorname{cov}(X,N)=\frac{\sum(X_i-\bar X)(N_i-\bar N)}{n-1},\quad r=\frac{s_{XN}}{s_Xs_N}.
\]

Varianza de una diferencia individual:

\[
s_D^2=s_X^2+s_N^2-2s_{XN},
\]

que debe coincidir, salvo redondeo, con la varianza calculada directamente sobre `D_i`. Para la media de diferencias independientes, `u(D̄)=s_D/√n`. Con autocorrelación de primer orden aproximada `r1`:

\[
n_{ef}\approx n\frac{1-r_1}{1+r_1},\qquad u(\bar D)=\frac{s_D}{\sqrt{n_{ef}}}.
\]

## Ejemplo numérico trabajado

Serie de 60 pares: `X̄=200.42`, `N̄=199.98`, `s_X=1.20`, `s_N=1.00`, `r=0.70`.

\[
s_{XN}=0.70(1.20)(1.00)=0.840\ (\mathrm{nmol/mol})^2.
\]

Si se supone independencia: `s_D,ind=√(1.20²+1.00²)=1.562 nmol/mol`. Con covarianza medida:

\[
s_D=\sqrt{1.20^2+1.00^2-2(0.840)}=\sqrt{0.760}=0.872\ \mathrm{nmol/mol}.
\]

El cálculo directo de las 60 diferencias debe dar aproximadamente 0.872 nmol/mol. Si `r1=0.25`: `n_ef=60(0.75/1.25)=36`, `u(D̄)=0.872/√36=0.145 nmol/mol`. Usar 60 sin corregir daría 0.113 nmol/mol y subestimaría la incertidumbre de la media.

## Criterios de aceptación

- Al menos 60 pares válidos y sincronizados.
- Identidad `s_D²≈s_X²+s_N²-2s_XN` dentro de 1 % por cálculo sin redondear.
- Sin salto, alarma ni deriva >1 nmol/mol/h durante la serie.
- La covarianza debe medirse, no imponerse. Un resultado negativo, cero o positivo puede ser válido si está respaldado por datos.
- Si la sincronización entre canales no puede demostrarse, el ensayo no sirve para un presupuesto diferencial dinámico.

## Seguridad

Cilindro de NO siempre sujeto, regulador compatible y prueba de fugas previa. Mantener bypass en extracción. Aunque E03 no genera O₃, confirmar que el generador de O₃ está desactivado. Al terminar, cerrar la válvula del cilindro, consumir presión atrapada conforme al procedimiento y purgar con aire cero.
