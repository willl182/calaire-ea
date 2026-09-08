# Contenido del curso — Incertidumbre en analizadores de O₃ y NOx (9 h + M8 opcional; práctica de laboratorio aparte)

Curso v2 para operadores de redes de calidad del aire. O₃ permanece como hilo conductor; M6 añade segunda familia instrumental obligatoria: NO, NO₂ y NOx por quimioluminiscencia. Base metrológica: JCGM/GUM, operacionalizada con Eurachem/CITAC QUAM 2012.

Desarrollado según `../plan_desarrollo_contenido.md` y diseño local `diseno_curso_v2.md`. Esta carpeta conserva adaptación para operadores; no reemplaza contenido original de `../contenido/`.

## Correspondencia documental

Cada sesión M1–M8 conserva su libreto principal en `modulos/` y cada unidad temporal de exposición tiene un archivo Markdown individual en `paginas/`. Los módulos funcionan como índice y contexto; las páginas contienen el texto dictable, el minutaje y los apoyos de cada página/diapositiva. No hay fuentes independientes PPT/PPTX/ODP en esta versión: el HTML es un artefacto derivado. El inventario completo, incluidas las excepciones E10/E12/E13 y M8 sin solucionario, está en [`control_documental_md.md`](control_documental_md.md).

## Alcance del curso y del material práctico

- **Curso teórico (obligatorio, 9 h):** M1–M7 en aula, con datasets sintéticos y presupuestos documentales. Cierra con el taller evaluado M7 (caso KRISS/BIPM), que es el entregable del curso. M8 (Monte Carlo) es opcional y queda fuera de las 9 h.
- **Práctica de laboratorio (contenido aparte, no incluido en las 9 h):** protocolos con instrumentos reales de O₃ y NOx, en `practica/`. Es contenido práctico independiente del curso teórico, con su propia programación, sus propios prerrequisitos logísticos y sus propios entregables, entre ellos el presupuesto híbrido del equipo propio (`practica/E15_presupuesto_hibrido.md`). **Los ejercicios teóricos del curso y los experimentos de la práctica son bloques separados: ninguno reemplaza al otro y cada uno conserva su propio entregable.** El bloque P1 se ejecuta con **dos subequipos en paralelo** (vía O₃ y vía NOx) que convergen en E15; sin esa división, P1 dura 9.5–10.5 h en un solo equipo secuencial. Ver el detalle completo de cómputo en `practica/P0_agenda_practica.md`.

**Prerrequisito logístico crítico de la práctica:** `practica/E08_deriva_cero_span.md` es pasivo y debe **iniciarse al menos 7 días antes** de la sesión práctica. Los analizadores, calibrador y patrón deben quedar **encendidos la noche anterior** (o mínimo 2 h antes) para no consumir tiempo de sesión en calentamiento. Ver agenda completa y checklist en `practica/P0_agenda_practica.md` y `practica/checklist_montaje_seguridad.md`.

## Tabla de experimentos de la práctica de laboratorio

| Experimento | Nombre | Módulo(s) enlazado(s) | Bloque |
|---|---|---|---|
| E01 | Ruido y repetibilidad de cero | M3, M4 | P1, vía O₃ (tras E09) |
| E02 | Verificación multipunto O₃, 3 ciclos | M5 | P1, vía O₃ (tras E11) |
| E03 | Covarianza medida NO/NOx | M6, M8 | P2 |
| E04 | GPT y eficiencia del convertidor | M6 | P1, vía NOx (requiere dos sesiones) |
| E05 | Verificación de corrección de firmware | M6 | P1, vía NOx |
| E06 | Transmisión de línea O₃ | M4 | P2 (documental en E15 hasta ejecutarlo) |
| E07 | Formación de NO₂ en línea | M6 | P2 |
| E08 | Deriva de cero y span 24 h/7 d | M4 | precurso ≥7 d antes |
| E09 | Calidad de aire cero | M4, M5 | P1, vía O₃ (prerrequisito de E01) |
| E11 | Tiempo de respuesta t10/t90 | M5 | P1, vía O₃ (antes de E02) |
| E14 | Recorrido documental de cadena metrológica | M1 | P1, vía O₃ |
| E15 | Presupuesto híbrido del equipo propio | M7 | P1, convergencia de ambas vías; entregable evaluado de la práctica |
| E16 | MCM con covarianza medida | M8 | P2 |

E10, E12 y E13 se mencionan en el diagnóstico de la práctica pero no cuentan con protocolo diseñado en esta versión; quedan fuera de P1/P2.

## Orden y tiempos del curso (9 h)

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
| `casos/` | Extracto BIPM.QM-K1 / KRISS 2024 para M7 (validación externa) |
| `modulos/` | Libretos y contexto M1–M7 obligatorios + M8 opcional; cada sección de guion enlaza sus páginas |
| `paginas/` | 39 archivos Markdown, uno por página/diapositiva temporal del libreto M1–M8; fuente canónica de la exposición |
| `modulos/soluciones/` | Solucionarios M1–M7; M8 es demostración sin solucionario separado |
| `practica/` | Contenido práctico de laboratorio, aparte de las 9 h del curso: agenda (`P0_agenda_practica.md`), un protocolo por experimento (`E0x_*.md`), hoja de registro de campo genérica y checklist de montaje y seguridad |
| `control_documental_md.md` | Inventario de sesiones, libretos, páginas, prácticas y excepciones documentales |

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

- Ejercicios M1–M6 producen evidencias parciales dentro del curso.
- **Curso — entregable evaluado: M7** (caso KRISS/BIPM). Es el cierre evaluado del curso de 9 h, se dicte o no la práctica de laboratorio.
- **Práctica de laboratorio — entregable evaluado propio y separado: `practica/E15_presupuesto_hibrido.md`**: presupuesto híbrido construido con evidencia propia (E01/E02/E06/E08/E09), reporte GUM/QUAM, alcance y transferencia breve a NOx. Se evalúa por su cuenta y no sustituye al de M7.
- Rúbrica revisa mensurando completo, vínculo fuente–efecto, evidencia pertinente, ausencia de doble conteo, covarianza/dependencias y coherencia entre presupuesto y reporte.
- Cifras KRISS contrastadas contra informe público; ejemplo EN 14211 reconstruido a 104 nmol/mol.
- Solucionarios consistentes con datasets y plantillas.
- Scripts R reproducibles; semillas declaradas.
- Build HTML valida archivos, filas y columnas NOx, MathML, anclas, nota APOA-370 y ausencia de recursos externos.
