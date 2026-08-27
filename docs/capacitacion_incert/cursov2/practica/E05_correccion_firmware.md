# E05 — Verificación de corrección de eficiencia en firmware

Enlaza con **M6** §3.2 (advertencia de doble corrección) y con **E04**.

## Objetivo

Determinar si el firmware aplica corrección automática por `η`, verificar el valor configurado y evitar doble corrección en el cálculo externo.

## Instrumentos

Mismos de E04; acceso autorizado a configuración o menú de diagnóstico; copia del manual y registro de configuración.

## Procedimiento

1. **Revisión documental, 5 min.** Identificar la definición del canal NO₂ mostrado, el parámetro de eficiencia y la posibilidad de activar/desactivar la corrección.
2. **Registrar estado encontrado, 5 min.** Fotografiar o transcribir firmware, valor `η_f`, modo y unidades. No cambiar la configuración sin autorización.
3. **Cero y NO base, 5 min.** Confirmar cero y NO base estables.
4. **Nivel GPT, 10 min.** Aplicar `G=100 nmol/mol`. Estabilizar 5 min y registrar cinco medias de 1 min de NO, NOx y NO₂ mostrado.
5. **Prueba de identidad, 5 min.** Calcular `D=X-N`, `D/η_f` y comparar ambos con el NO₂ mostrado.
6. **Cambio controlado, 10 min.** Solo si está autorizado, guardar la configuración y cambiar temporalmente `η_f` de 0.970 a 0.950, sin cambiar el gas. Esperar 3 min y registrar cinco medias. Restaurar el valor original inmediatamente.
7. **Confirmación, 5 min.** Repetir la lectura con el valor restaurado y verificar el retorno.
8. **Documentación, 5 min.** Declarar el modelo correcto para exportación cruda y para pantalla.

**Duración:** 50 min.

## Tabla de registro

| estado | η_f | NO | NOx | D | D/η_f | NO₂ mostrado | diferencia vs modelo | observación |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| encontrado | | | | | | | | |
| cambio autorizado | | | | | | | | |
| restaurado | | | | | | | | |

Todas las concentraciones en nmol/mol.

## Modelo de cálculo

Hipótesis H0, firmware sin corrección: `M≈D=X-N`. Hipótesis H1, firmware corrige eficiencia: `M≈D/η_f`. Cambio esperado al modificar η, manteniendo D constante:

\[
\Delta M=D\left(\frac1{\eta_2}-\frac1{\eta_1}\right).
\]

## Ejemplo numérico trabajado

Con gas estable se observa `X=448.0`, `N=351.0` → `D=97.0 nmol/mol`. Con `η_f=0.970`: `D/η_f=100.0 nmol/mol`. La pantalla muestra 100.1 nmol/mol: coincide con la corrección.

Si se cambia temporalmente a 0.950: `M2=97.0/0.950=102.105 nmol/mol`, `ΔM=2.105 nmol/mol`. La pantalla muestra 102.0 nmol/mol mientras NO y NOx crudos permanecen dentro de 0.3 nmol/mol: el resultado confirma corrección automática. Aplicar de nuevo `D/η` al NO₂ mostrado produciría `100.1/0.970=103.2 nmol/mol`: doble corrección incorrecta.

## Criterios de aceptación

- Estado del firmware y valor de `η_f` quedan trazables.
- El modelo seleccionado reproduce la pantalla dentro de un máximo de 0.5 nmol/mol o la resolución del equipo.
- El cambio observado por la modificación autorizada coincide con `ΔM` dentro de la incertidumbre y estabilidad del gas.
- Configuración original restaurada y verificada.
- Si los campos NO y NOx exportados ya están procesados, documentar la arquitectura; no asumir que son crudos.

## Seguridad

Aplican los controles de cilindro NO y venteo de O₃ de E04. Cambio de firmware solo con autorización, copia del estado inicial y responsable presente. No dejar el instrumento operativo con un valor de prueba.
