# Diagnóstico Final: Arquitectura Documental cursov2

## 1. Problema Raíz
Módulos mezclan capas. Capa 0 (Meta/Instructor) fusionada con Capa 1 (Material Participante). 42% de `modulos/` es instrucción meta. Handout O₃ falla como material porque duplica Capa 1 y mezcla anexos con teoría. Handout NOx funciona bien como ficha. Diapositivas (Capa 2 y 3) no existen. `solo_md/` diverge por copia manual. Vocabulario operativo invertido (M1 usa términos definidos en M3 o handout).

## 2. Modelo de Capas Objetivo (Flujo de Derivación)
* **Capa 0 (Meta Maestro):** Fuente única (`modulos/`). Contiene todo: minutaje, notas, guion, soluciones.
* **Capa 1 (Material Teórico):** Derivada de Capa 0. Prosa limpia para participante. Sin minutaje ni notas de instructor.
* **Capa 2 (Guion Diapositivas):** Derivada de Capa 1. Texto telegráfico.
* **Capa 3 (Diapositivas Visuales):** Capa 2 + diseño visual.
* **Capa R (Referencia/Anexos):** Perpendicular. Glosario, tablas, fórmulas, checklists. (Handouts rediseñados).
* **Protocolos Prácticos:** Autónomos para campo/laboratorio.
* **Solucionarios:** Privados, paso a paso.

## 3. Esquema de Marcado (Fuente Única)
Ideas nuevas nacen en Capa 0. Extraer mecánicamente otras capas usando etiquetas regulares:

```markdown
### 3.N Título — 0:mm a 0:mm; acumulado 0:mm      <- Capa 0
**Idea fuerza:**                                  <- Capa 2
**Guion dictable:**                               <- Capa 0, 1
**Puntos:**                                       <- Capa 2
**Apoyo visual:**                                 <- Capa 3
**Nota de facilitación:**                         <- Capa 0
**Referencias exactas:**                          <- Capa 0, 1 (corta)
**Apoyo en la referencia:**                       <- Capa 0
```

## 4. Plan de Acción (Resolución de Deuda)
1. **Declarar capas:** Actualizar `README.md`. Fijar convención de bloques. Renombrar/declarar handout como Capa R.
2. **Resolver vocabulario (Inversión M1/M3):** Crear bloque M0 (15-20 min) para términos básicos antes de M1. Robusto ante falta de prelectura.
3. **Estandarizar M5, M6, M8:** Escribir `Guion dictable` faltante. 
4. **Etiquetar M1-M4, M7:** Aplicar convención de marcado a discurso existente.
5. **Podar handout O₃:** Eliminar ~520 líneas duplicadas. Dejar solo glosario, tabla PDF, propagación, checklist (Capa R pura).
6. **Automatizar derivación:** Crear `build_capas.py` para generar Capa 1, 2, 3 y `solo_md/` desde Capa 0. Evita drift silencioso.