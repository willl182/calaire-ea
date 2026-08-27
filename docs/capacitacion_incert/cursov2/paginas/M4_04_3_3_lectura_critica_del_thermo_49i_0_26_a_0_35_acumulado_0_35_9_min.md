# M4 — Página 04 — 3.3 Lectura crítica del Thermo 49i — 0:26 a 0:35; acumulado 0:35 (9 min)

- **Sesión:** M4
- **Fuente:** [`modulos/M4_presupuesto_analizador.md`](../modulos/M4_presupuesto_analizador.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.3 Lectura crítica del Thermo 49i — 0:26 a 0:35; acumulado 0:35 (9 min)

**Idea fuerza:** deben conservarse literalmente la base temporal, la escala y las condiciones de cada especificación.

**Guion dictable:**

“La Table 1-1 del Model 49i informa ruido de cero de 0.25 ppb RMS con promedio de 60 s; límite inferior detectable de 0.5 ppb; deriva de cero menor que 1 ppb en 24 horas y menor que 2 ppb en 7 días; deriva de span menor que 1 % por mes, incluyendo deriva de transductores; y linealidad de más o menos 1 % de escala completa. Las especificaciones de desempeño se basan en operación entre 20 °C y 30 °C.”

“Si seleccionamos una escala completa de 200 ppb, la linealidad de 1 % equivale a un límite de 2 ppb. Si solo conocemos ese límite y admitimos valores igualmente posibles dentro de él, usamos rectangular. La deriva de cero de 24 horas puede tratarse de manera análoga. El ruido RMS se conserva como incertidumbre estándar solo para el promedio de 60 segundos declarado.”

“Ahora auditemos la plantilla. El caso 1 rotula una deriva de span de 1 % en 24 horas. La Table 1-1 no respalda ese periodo: dice menos de 1 % por mes. Además, la tabla no aclara en esa fila si el porcentaje se aplica a lectura o a escala completa. Ejecutaremos la plantilla sin modificarla porque el objetivo incluye auditar un caso precargado, pero esa fila debe quedar marcada como supuesto no verificado.”

“La cifra de presión equivalente de 0.36 ppb, la resolución de 0.1 ppb y el certificado con 1.8 ppb y factor dos tampoco aparecen en Table 1-1. Pueden ser entradas válidas si existe otra fuente, pero no deben atribuirse a esa tabla.”

“El capítulo 4 aporta el contexto para reemplazar especificaciones por evidencia. Solicita la misma fuente de aire cero para el fotómetro y el ozonizador, describe una calibración multipunto, propone span cercano al 80 % del límite superior, recomienda al menos otros cinco niveles y establece verificaciones periódicas de cero y span. Por ello, falta de ajuste y deriva deben terminar respaldadas por datos del sistema real.”

**Referencias exactas verificadas:** Thermo Fisher Scientific, *Model 49i Instruction Manual*, Table 1-1, página impresa 1-3, página 25 del PDF. Cap. 4: equipo y aire cero, pp. impresas 4-1–4-2, PDF 137–138; linealidad, pp. 4-5–4-6, PDF 141–142; calibración multipunto, pp. 4-8–4-11, PDF 144–147; verificaciones periódicas, pp. 4-11–4-12, PDF 147–148.
