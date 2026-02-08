# Plan: Correcciones Informe Ejecutivo y Calendario

**Created**: 2026-02-08 11:25
**Updated**: 2026-02-08 11:45
**Status**: completed
**Slug**: correcciones-informe-calendario

---

## Objetivo

Corregir inconsistencias técnicas y de contenido en el Informe Ejecutivo del periodo 28 ene - 8 feb 2026, calendario de prueba piloto y documentación relacionada. Las correcciones se basan en aclaraciones proporcionadas por el usuario sobre lo que validó el consultor César Yate y el motivo de cancelación de las rondas de febrero. Además, generar imágenes PNG de los diagramas Mermaid para que carguen correctamente en el informe y la presentación.

---

## Fases

### Fase 1: Correcciones en docs/timeline.md

**Objetivo:** Ajustar el diagrama de timeline para eliminar secciones redundantes y corregir formato de semanas.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | `docs/timeline.md` | Modificar | Líneas 5-6: Eliminar el `.<br>` intermedio en "SEMANAS: Feb 16-21 <br>.<br> Ronda 1 (CANCELLED)" y "SEMANAS: Feb 23-28 <br>.<br> Ronda 2 (CANCELLED)" para que quede en 3 renglones alineado |
| 1.2 | `docs/timeline.md` | Eliminar | Líneas 82-92: Eliminar completamente la sección DOMINGO |
| 1.3 | `docs/timeline.md` | Eliminar | Líneas 93-103: Eliminar completamente la sección LUNES (extra) |

### Fase 2: Correcciones en docs/informes/260208_ie_01.md

**Objetivo:** Actualizar referencias técnicas sobre lo validado por César Yate, motivo de cancelación y eliminar secciones sobre transición de roles.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | `docs/informes/260208_ie_01.md` | Modificar | Línea 30: Cambiar "Demostración CALAIRE-APP a consultor ISO 17043" → "Demostración CALAIRE-APP: homogeneidad, estabilidad, nIQR y MADe a consultor ISO 17043" |
| 2.2 | `docs/informes/260208_ie_01.md` | Modificar | Línea 121: Cambiar "Confirmación de discrepancias en homogeneidad, estabilidad y MADe" → "Confirmación de discrepancias en homogeneidad, estabilidad, nIQR y MADe" |
| 2.3 | `docs/informes/260208_ie_01.md` | Modificar | Línea 130: Cambiar "algoritmos robustos para cálculo de z-score, estadísticos En, y estimadores MADe" → "algoritmos robustos para homogeneidad, estabilidad, nIQR y MADe" |
| 2.4 | `docs/informes/260208_ie_01.md` | Modificar | Línea 136: Cambiar "| Cálculo de z-score | Validado | Conforme a ISO 13528 |" → "| Homogeneidad de muestras | En revisión | Discrepancias atribuibles a imputación |<br>| Estabilidad temporal | En revisión | Discrepancias atribuibles a imputación |<br>| Estimadores robustos (nIQR, MADe) | Validado | Conforme a ISO 13528 |" |
| 2.5 | `docs/informes/260208_ie_01.md` | Modificar | Línea 25: Cambiar "Esta decisión responde a la necesidad de evitar conflictos con el periodo de contingencias ambientales en la región" → "Esta decisión responde a la preparación de las autoridades ambientales para las contingencias de marzo" |
| 2.6 | `docs/informes/260208_ie_01.md` | Modificar | Línea 66: Cambiar "> **Evitar programar rondas en periodos cercanos a contingencias ambientales.** El periodo febrero-marzo constituye una temporada crítica para SIATA y autoridades ambientales como Corantioquia, dedicada a la preparación y respuesta ante contingencias de calidad del aire." → "> **Evitar programar rondas en periodos cercanos a contingencias ambientales.** El periodo febrero-marzo constituye una temporada crítica para SIATA y autoridades ambientales como Corantioquia, dedicada a la preparación de las autoridades para las contingencias de marzo." |
| 2.7 | `docs/informes/260208_ie_01.md` | Eliminar | Líneas 184-194: Eliminar sección "### 5.3 Transición de Roles: Fabián Moreno" completa |
| 2.8 | `docs/informes/260208_ie_01.md` | Modificar | Línea 217: Cambiar "| 4 | **Alistamiento operativo y metrológico:** ... | Fabián Moreno + Wilson Salas |" → "| 4 | **Alistamiento operativo y metrológico:** ... | Wilson Salas |" |
| 2.9 | `docs/informes/260208_ie_01.md` | Modificar | Línea 227: Cambiar "| 9 | **Preparación logística de equipos:** ... | Fabián Moreno |" → "| 9 | **Preparación logística de equipos:** ... | Wilson Salas |" |

### Fase 3: Correcciones en docs/informes/260208_ie_01_slides.md

**Objetivo:** Alinear slides con el informe principal.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | `docs/informes/260208_ie_01_slides.md` | Modificar | Línea 136: Cambiar "- **Núcleo validado:** z-score, En, MADe conformes a ISO 13528" → "- **Núcleo validado:** homogeneidad, estabilidad, nIQR, MADe conformes a ISO 13528" |
| 3.2 | `docs/informes/260208_ie_01_slides.md` | Modificar | Línea 148: Cambiar "| Cálculo z-score | Validado (ISO 13528) |" → "| Homogeneidad | En revisión |<br>| Estabilidad | En revisión |<br>| nIQR, MADe | Validado (ISO 13528) |" |
| 3.3 | `docs/informes/260208_ie_01_slides.md` | Modificar | Líneas 64-66: Actualizar "Fundamento: Reestructuración del Cronograma" para especificar preparación de autoridades para contingencias de marzo |
| 3.4 | `docs/informes/260208_ie_01_slides.md` | Eliminar | Líneas 167-177: Eliminar sección "## Transición de Roles: Fabián Moreno" completa |

### Fase 4: Correcciones en pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md

**Objetivo:** Actualizar página de resumen en Logseq.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | `pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md` | Modificar | Línea 33: Cambiar "Demostración a César Yate (consultor ISO 17043)" → "Demostración a César Yate (consultor ISO 17043): homogeneidad, estabilidad, nIQR, MADe" |
| 4.2 | `pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md` | Modificar | Línea 35: Cambiar "núcleo estadístico (z-score, En, MADe) validado conforme a ISO 13528:2017" → "núcleo estadístico (homogeneidad, estabilidad, nIQR, MADe) validado conforme a ISO 13528:2017" |
| 4.3 | `pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md` | Modificar | Línea 40: Cambiar "Segunda validación con César Yate (Wilson Salas + César Yate, 2026-03-01)" → "Segunda validación con César Yate: homogeneidad, estabilidad, nIQR, MADe (Wilson Salas + César Yate, 2026-03-01)" |
| 4.4 | `pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md` | Modificar | Línea 59: Cambiar "Segunda validación CALAIRE-APP (Wilson Salas + César Yate, 2026-03-25)" → "Segunda validación CALAIRE-APP: homogeneidad, estabilidad, nIQR, MADe (Wilson Salas + César Yate, 2026-03-25)" |
| 4.5 | `pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md` | Eliminar | Línea 45: Eliminar "Transición Fabián Moreno: Técnico operativo durante prueba piloto → Suplencia técnica tras contratación" |
| 4.6 | `pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md` | Modificar | Línea 54: Eliminar referencia a Fabián Moreno en alistamiento operativo |
| 4.7 | `pages/Informe Ejecutivo Ene 28 - Feb 8 2026.md` | Modificar | Línea 60: Eliminar referencia a Fabián Moreno en preparación logística |

### Fase 5: Correcciones en pages/Prueba Piloto.md

**Objetivo:** Actualizar motivo de cancelación de rondas.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 5.1 | `pages/Prueba Piloto.md` | Modificar | Línea 2: Cambiar "Febrero cancelado por contingencias ambientales" → "Febrero cancelado por preparación de autoridades ambientales para contingencias de marzo" |
| 5.2 | `pages/Prueba Piloto.md` | Modificar | Línea 6: Cambiar "2 Rondas (incluyendo 2 canceladas por contingencias ambientales)" → "2 Rondas (incluyendo 2 canceladas por preparación de autoridades para contingencias de marzo)" |
| 5.3 | `pages/Prueba Piloto.md` | Modificar | Línea 29: Cambiar "(Feb 18-23) - Cancelada por contingencias ambientales" → "(Feb 18-23) - Cancelada por preparación de autoridades para contingencias de marzo" |
| 5.4 | `pages/Prueba Piloto.md` | Modificar | Línea 30: Cambiar "(Feb 25-Mar 2) - Cancelada por contingencias ambientales" → "(Feb 25-Mar 2) - Cancelada por preparación de autoridades para contingencias de marzo" |

### Fase 6: Correcciones en journals/2026_02_07.md

**Objetivo:** Actualizar journal del 7 de febrero con correcciones técnicas y eliminar referencias a transición.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 6.1 | `journals/2026_02_07.md` | Modificar | Línea 4: Cambiar "debido a consideraciones operativas y de contingencias ambientales" → "debido a la preparación de las autoridades ambientales para las contingencias de marzo" |
| 6.2 | `journals/2026_02_07.md` | Modificar | Línea 22: Cambiar "núcleo de cálculos estadísticos (z-score, En, algoritmos robustos según ISO 13528:2017)" → "núcleo de cálculos estadísticos (homogeneidad, estabilidad, nIQR, MADe según ISO 13528:2017)" |
| 6.3 | `journals/2026_02_07.md` | Modificar | Línea 27: Cambiar "febrero-marzo constituye un periodo crítico para SIATA y autoridades ambientales como Corantioquia debido a la temporada de contingencias" → "febrero-marzo constituye un periodo crítico para SIATA y autoridades ambientales como Corantioquia debido a la preparación para las contingencias de marzo" |
| 6.4 | `journals/2026_02_07.md` | Modificar | Línea 17: Cambiar "Fabián Moreno mantendrá su rol actual y asumirá función de backup técnico una vez se concrete la nueva contratación" → "Fabián Moreno mantendrá su rol actual" |
| 6.5 | `journals/2026_02_07.md` | Modificar | Línea 39: Eliminar referencia a [[Fabián Moreno]] |

### Fase 7: Correcciones en pages/CALAIRE-APP.md

**Objetivo:** Actualizar referencias técnicas en página del aplicativo.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 7.1 | `pages/CALAIRE-APP.md` | Modificar | Línea 8: Cambiar "núcleo de cálculos estadísticos (z-score, En, algoritmos robustos)" → "núcleo de cálculos estadísticos (homogeneidad, estabilidad, nIQR, algoritmos robustos MADe)" |
| 7.2 | `pages/CALAIRE-APP.md` | Modificar | Línea 29: Cambiar "Cálculo: z-score, En, algoritmos robustos (A)" → "Cálculo: homogeneidad, estabilidad, nIQR, algoritmos robustos (A)" |

### Fase 8: Correcciones en pages/Fabian Moreno.md

**Objetivo:** Eliminar sección sobre rol de suplencia.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 8.1 | `pages/Fabian Moreno.md` | Eliminar | Líneas 9-10: Eliminar sección completa "## Rol de Suplencia" y su contenido |

### Fase 9: Renderizado de Gráficos Mermaid

**Objetivo:** Generar imágenes PNG de los diagramas Mermaid para que carguen correctamente en el informe y la presentación.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 9.1 | `docs/gantt.md` | Renderizar | Generar PNG usando mmdc → `docs/informes/gantt_piloto.png` |
| 9.2 | `docs/timeline.md` | Renderizar | Generar PNG usando mmdc → `docs/informes/timeline_piloto.png` |

---

## Log de Ejecución

- [x] Fase 1 iniciada
- [x] Fase 1 completada
- [x] Fase 2 iniciada
- [x] Fase 2 completada
- [x] Fase 3 iniciada
- [x] Fase 3 completada
- [x] Fase 4 iniciada
- [x] Fase 4 completada
- [x] Fase 5 iniciada
- [x] Fase 5 completada
- [x] Fase 6 iniciada
- [x] Fase 6 completada
- [x] Fase 7 iniciada
- [x] Fase 7 completada
- [x] Fase 8 iniciada
- [x] Fase 8 completada
- [x] Fase 9 iniciada
- [x] Fase 9 completada
