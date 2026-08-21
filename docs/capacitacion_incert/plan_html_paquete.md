# Plan — HTML del paquete completo del curso

**Objetivo:** un único HTML autocontenido (`contenido/curso_paquete_completo.html`) con todo el material del curso, navegable, imprimible, sin dependencias externas.

## Estructura del documento

1. **Portada e índice** (barra lateral de navegación fija + índice inicial).
2. **Diseño del curso** (`diseno_curso_8h.md`): objetivos, tabla horaria, detalle por módulo.
3. **Handout teórico** (`contenido/handout/handout_teorico_gum_o3.md`).
4. **Guiones de módulo M1–M7** (`contenido/modulos/M*.md`), uno por sección.
5. **Materiales**:
   - Dataset: tabla HTML completa (24 filas) + metadata + código del generador.
   - Plantilla: descripción, tabla de casos (CSV) y código R; nota de que existe xlsx.
   - Demo MCM: código R + gráfico PNG embebido (data URI).
   - Caso KRISS (`contenido/casos/extracto_kriss_2024.md`).
6. **Solucionarios (solo instructor)**: SOL_M2–M5 y SOL_M7 en bloques `<details>` colapsados, con aviso visual (M6 es demostración guiada, sin solucionario propio).
7. **Apéndice de reproducibilidad**: rutas de archivos, semilla, cómo regenerar.

## Requisitos técnicos

- Autocontenido: CSS inline, PNG como data URI, sin CDN. Matemáticas LaTeX → **MathML** (pandoc `--mathml`), sin MathJax.
- Tema claro/oscuro vía `prefers-color-scheme`; imprimible (media print: sin sidebar, `details` abiertos).
- Código con `<pre>` desplazable; tablas anchas en contenedor `overflow-x`.
- Español; misma línea visual que `curso_incertidumbre_o3.html`.

## Método de construcción (reproducible)

Un script `contenido/build_paquete_html.py` (Python + pandoc, sin pip):
1. Lee lista ordenada de fuentes md/csv/R/png.
2. Convierte cada md con `pandoc -f gfm+tex_math_dollars ... --mathml` a fragmento HTML.
3. CSV → tabla HTML; R/py → bloques de código escapados; PNG → base64.
4. Ensambla shell HTML (sidebar generada de los encabezados de sección) + CSS embebido.
5. Escribe `curso_paquete_completo.html` e imprime tamaño y conteo de secciones.

## Ejecución

- **Subagente claude-gpt**: escribe `build_paquete_html.py` + CSS/shell, lo ejecuta hasta producir HTML válido, verifica anclas del índice y ausencia de referencias externas.
- **Hilo principal**: corre el build, inspección rápida (tamaño, secciones, grep de `http` externo, MathML presente).
- **Subagente Opus 5**: revisión final — completitud (todas las fuentes presentes), fidelidad (muestreo de contenido vs md fuente), navegación/anclas, autocontención, impresión, accesibilidad básica.

## Criterios de cierre

- HTML abre sin red; todas las secciones del índice presentes y ancladas.
- Cero `src=/href=` externos (solo anclas internas y data URIs).
- Fórmulas renderizadas (MathML), tablas legibles, solucionarios colapsados con aviso.
- Build reproducible con un solo comando.
