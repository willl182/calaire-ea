# Contenido del curso — Incertidumbre en analizadores de O₃ y patrones de transferencia (6 h)

Desarrollado según `../plan_desarrollo_contenido.md` y el diseño `../diseno_curso_8h.md` (v2, agnóstico). 2026-08-17.

| Carpeta | Contenido |
|---|---|
| `handout/` | Handout teórico único (fusión de las dos guías, citas JCGM corregidas) |
| `datasets/` | Dataset sintético de verificación multipunto + generador R (semilla 20260817) + metadata con efectos inyectados |
| `plantillas/` | Plantilla de presupuesto en R (casos M4/M7 precargados; self-test EN 14625 u_c=4.3 nmol/mol) + export CSV |
| `scripts/` | Demo MCM adaptativo Beer–Lambert (JCGM 101) con validación GUF↔MCM y gráfico |
| `casos/` | Extracto del caso BIPM.QM-K1 / KRISS 2024 con preguntas de taller |
| `modulos/` | Guiones de instructor M1–M7 (tiempos, guion dictable, referencias con página verificada) |
| `modulos/soluciones/` | Solucionarios de instructor (M2, M3, M4, M5, M7) |

Verificaciones realizadas:
- Cifras del extracto KRISS contrastadas contra el PDF del informe.
- Solucionarios numéricamente consistentes con dataset y plantilla (cálculos de referencia en R).
- Scripts ejecutan con `Rscript` en R base.
- Sin contenido de esquemas PT ni datos operativos propietarios.

Nota didáctica: en la plantilla, varias filas del caso 1 están marcadas `SUPUESTO` a propósito — el guion M4 las usa como ejercicio de auditoría de fuentes.
