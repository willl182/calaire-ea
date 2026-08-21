# Contenido del curso — Incertidumbre en analizadores de O₃ y NOx (9 h + M8 opcional)

Curso v2 para operadores de redes de calidad del aire. O₃ permanece como hilo conductor; M6 añade segunda familia instrumental obligatoria: NO, NO₂ y NOx por quimioluminiscencia. Base metrológica: JCGM/GUM, operacionalizada con Eurachem/CITAC QUAM 2012.

Desarrollado según `../plan_desarrollo_contenido.md` y diseño local `diseno_curso_v2.md`. Esta carpeta conserva adaptación para operadores; no reemplaza contenido original de `../contenido/`.

## Orden y tiempos

| Orden | Módulo | Duración | Carácter |
|---:|---|---:|---|
| 1 | M1 — Metrología del ozono y cadena de trazabilidad | 35 min | obligatorio |
| 2 | M2 — Modelo de medición: fotometría UV y Beer–Lambert | 48 min | obligatorio |
| 3 | M3 — Conceptos GUM: evidencia, Tipo A/B, PDFs y combinación | 54 min | obligatorio |
| 4 | M4 — Presupuesto de incertidumbre del analizador O₃ | 82 min | obligatorio |
| 5 | M5 — Patrones de transferencia: calibración multipunto, deriva y verificación | 68 min | obligatorio |
| 6 | M6 — NO/NO₂/NOx por quimioluminiscencia | 90 min | obligatorio |
| 7 | M7 — Taller integrador: presupuesto, validación y reporte | 85 min | obligatorio; cierre evaluado |
| 8 | M8 — Método de Monte Carlo y validación del marco GUM | 30 min | opcional; fuera de 9 h |

Recorrido obligatorio: **462 min (7 h 42 min)**. Jornada nominal: **9 h (540 min)**. Quedan **78 min** para pausas, instalación, cambios de actividad y cierre logístico. M8 añade 30 min fuera de jornada; no condiciona aprobación.

Secuencia QUAM transversal: **especificar, identificar, cuantificar, depurar, combinar, expandir, informar y revisar**. Participantes no necesitan leer QUAM completo: módulos incorporan secciones, listas y ejemplos pertinentes.

## Estructura

| Carpeta | Contenido |
|---|---|
| `handout/` | Handout GUM/O₃ y handout independiente NOx |
| `datasets/` | Verificación multipunto O₃; GPT/convertidor NOx; línea de muestreo NOx; metadata y generadores reproducibles |
| `plantillas/` | Presupuesto O₃ y plantilla NOx con modelo diferencial, eficiencia y covarianza |
| `scripts/` | Demostración opcional M8 de Monte Carlo para Beer–Lambert |
| `casos/` | Extracto BIPM.QM-K1 / KRISS 2024 para M7 |
| `modulos/` | Guiones M1–M7 obligatorios + M8 opcional |
| `modulos/soluciones/` | Solucionarios M1–M7; M8 es demostración sin solucionario separado |

## Fuentes troncales

- JCGM 100:2008, GUM-1:2023, GUM-6, JCGM 101 y JCGM 102.
- Eurachem/CITAC, *Quantifying Uncertainty in Analytical Measurement*, 3.ª ed., 2012. Citas usan páginas editoriales; página física PDF = editorial + 6.
- USEPA Quality Handbook, P1016Y93, EN 14625, NISTIR 6963 y BIPM.QM-K1 para O₃.
- BS EN 14211:2012 para principio, desempeño y ejemplo informativo NO₂; anexos E/F/G son informativos.
- Método EPA NO₂ de febrero de 2002 como guía histórica de GPT y QA/QC, no como requisito vigente universal.
- Doval Miñarro et al. (2011), Gluck et al. (2003) y Pernigotti et al. (2013) para línea, convertidor, interferencias y correlación.

## Control documental NOx

`APOA-370` es analizador de O₃ por absorción UV. No es fuente instrumental para NOx y no contiene convertidor NO₂→NO. El manual local `APNA-370_Operaton_Manual_GZ9100497232L.pdf` (HORIBA Ambient NOx Monitor, 2021) está disponible como fuente instrumental. Verificar si APNA-370 es el equipo realmente instalado queda a cargo del operador antes de atribuir sus especificaciones al sistema local. M6 usa núcleo genérico EN 14211/EPA y datos sintéticos con semilla `20260819`.

## Evaluación y verificaciones

- Ejercicios M1–M6 producen evidencias parciales.
- M7 es cierre evaluado: presupuesto, reporte GUM/QUAM, validación externa, alcance y transferencia breve a NOx.
- Rúbrica revisa mensurando completo, vínculo fuente–efecto, evidencia pertinente, ausencia de doble conteo, covarianza/dependencias y coherencia entre presupuesto y reporte.
- Cifras KRISS contrastadas contra informe público; ejemplo EN 14211 reconstruido a 104 nmol/mol.
- Solucionarios consistentes con datasets y plantillas.
- Scripts R reproducibles; semillas declaradas.
- Build HTML valida archivos, filas y columnas NOx, MathML, anclas, nota APOA-370 y ausencia de recursos externos.
