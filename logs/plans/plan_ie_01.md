# Plan: Informe Ejecutivo CALAIRE-EA (Ene 28 - Feb 8, 2026)

**Created**: 2026-02-08 08:31
**Updated**: 2026-02-08 08:42
**Status**: completed
**Slug**: `informe-ejecutivo-ene-feb26`

---

## Objetivo

Generar un informe ejecutivo en formato Markdown y Word para los miembros del equipo, cubriendo las últimas 2 semanas del proyecto (Enero 28 - Febrero 8, 2026), con diagramas visuales (Gantt y Timeline de la prueba piloto) y detalle técnico de hallazgos iniciales de CALAIRE-APP.

---

## Características del Informe

| Elemento | Detalle |
|----------|---------|
| **Periodo** | Enero 28 - Febrero 8, 2026 (2 semanas) |
| **Ubicación** | `docs/informes/informe_ejecutivo_260208.md` |
| **Formatos** | Markdown + Word (.docx) |
| **Diagramas** | Gantt y Timeline en PNG (renderizados con mermaid-cli) |
| **Sección CALAIRE-APP** | Nivel: Detalle técnico (cronología completa) |
| **TODOs** | No incluir tabla, solo próximos pasos en narrativa |

---

## Estructura del Informe

```markdown
# Informe Ejecutivo - Proyecto CALAIRE-EA
## Periodo: Enero 28 - Febrero 8, 2026

### 1. Resumen Ejecutivo
   - Estado general del proyecto
   - Hitos clave del periodo

### 2. Cronograma Prueba Piloto (Actualizado)
   - Tabla resumen de rondas (8 rondas, 2 canceladas)
   - Diagrama Gantt (imagen PNG insertada)
   - Diagrama Timeline semanal (imagen PNG insertada)

### 3. Gestión de Participantes
   - Confirmaciones recibidas (UdeM, UPB)
   - Pendientes (SIATA, Politécnico)
   - Decisiones: cancelación febrero, reubicación SIATA

### 4. Hallazgos CALAIRE-APP (Detalle Técnico)
   - Cronología: demostración César Yate (Ene 28) → discrepancias (Feb 4-5) → análisis de causa raíz (Feb 7)
   - Hallazgo: imputación de datos (menor gravedad)
   - Estado de núcleo estadístico (z-score, En, MADe)
   - Tareas pendientes y deadlines

### 5. Recursos Humanos y Contratación
   - Postergación contratación técnico principal
   - Transición de roles (Fabián Moreno)

### 6. Próximos Pasos
   - Confirmación SIATA para Ronda 6
   - Contacto Politécnico JIC
   - Envío informe hallazgos CALAIRE-APP
   - Preparación logística equipos
```

---

## Fases

### Fase 1: Preparación del Entorno

**Objetivo:** Crear estructura de directorios y preparar herramientas de generación de diagramas.

| # | Archivo/Comando | Acción | Descripción |
|---|-----------------|--------|-------------|
| 1.1 | `docs/informes/` | Crear directorio | Nueva carpeta dedicada para informes ejecutivos |
| 1.2 | `npm install -g @mermaid-js/mermaid-cli` | Ejecutar | Instalar mermaid-cli para generar PNGs desde código Mermaid |

**Estado:** pendiente

---

### Fase 2: Generación de Diagramas PNG

**Objetivo:** Renderizar los diagramas Mermaid (Gantt y Timeline) como imágenes PNG para inserción en el informe Word.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | `docs/informes/gantt_piloto.png` | Generar | Renderizar Gantt desde `docs/gantt.md` usando `mmdc -i docs/gantt.md -o docs/informes/gantt_piloto.png` |
| 2.2 | `docs/informes/timeline_piloto.png` | Generar | Renderizar Timeline desde `docs/timeline.md` usando `mmdc -i docs/timeline.md -o docs/informes/timeline_piloto.png` |

**Estado:** pendiente

**Nota:** Timeline Mermaid es extenso; es posible que requiera ajustes de escala para renderizar correctamente como PNG.

---

### Fase 3: Redacción del Informe Markdown

**Objetivo:** Escribir el informe completo en formato Markdown con estructura detallada basada en journals de las últimas 2 semanas.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | `docs/informes/informe_ejecutivo_260208.md` | Crear | Documento con 6 secciones detalladas basado en journals `2026_01_28.md` hasta `2026_02_07.md` |

**Fuentes de Información (Journals):**

| Fecha | Eventos Clave |
|-------|---------------|
| Ene 28 | Demostración CALAIRE-APP a César Yate |
| Ene 29 | Definición perfil contratista 2026 |
| Ene 30 | Documentación T700U, ajuste cartas, reprogramación rondas |
| Feb 2 | Auditoría CALAIRE, actualización cronograma maestro |
| Feb 3 | Confirmación UdeM (Rondas 3-4), actualización cartas, verificación espacio físico |
| Feb 4 | Revisión estadística CALAIRE-APP (discrepancias) |
| Feb 5 | Confirmación UPB (Ronda 5), seguimiento SIATA, resultados CALAIRE-APP |
| Feb 7 | Cancelación rondas febrero, reubicación SIATA, extensión calendario, hallazgo imputación datos |

**Estado:** pendiente

---

### Fase 4: Conversión a Word

**Objetivo:** Convertir el informe Markdown a formato Word para distribución al equipo.

| # | Comando | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | `pandoc -o docs/informes/260208_ie_01.docx docs/informes/260208_ie_01.md` | Ejecutar | Convertir Markdown a Word (.docx) con imágenes PNG correctamente referenciadas |

**Estado:** pendiente

---

### Fase 5: Verificación y Commit

**Objetivo:** Validar la calidad del documento final y registrar cambios en el repositorio.

| # | Acción | Descripción |
|---|--------|-------------|
| 5.1 | Verificar | Revisar que imágenes PNG estén correctamente insertadas y rendericen en Word |
| 5.2 | Commit | `git add docs/informes/ && git commit -m "Add executive report Jan28-Feb8 with Mermaid diagrams"` |
| 5.3 | Push | Sincronizar commits con repositorio remoto |

---

### Fase 6: Revisión del Informe (5 Modelos)

**Objetivo:** Obtener 5 revisiones independientes del informe ejecutivo. Cada modelo evalúa **todas las 6 secciones** desde **todas las 5 perspectivas** (precisión técnica, claridad, completitud, estructura, accionabilidad).

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 6.1 | `docs/informes/estructura_revision.md` | Crear | Estructura estándar para las revisiones (formato de tabla por sección y perspectiva) |
| 6.2 | `docs/informes/260208_ie_01_rev1.md` | Generar | Revisión Modelo 1 (evalúa 5 perspectivas × 6 secciones) |
| 6.3 | `docs/informes/260208_ie_01_rev2.md` | Generar | Revisión Modelo 2 (evalúa 5 perspectivas × 6 secciones) |
| 6.4 | `docs/informes/260208_ie_01_rev3.md` | Generar | Revisión Modelo 3 (evalúa 5 perspectivas × 6 secciones) |
| 6.5 | `docs/informes/260208_ie_01_rev4.md` | Generar | Revisión Modelo 4 (evalúa 5 perspectivas × 6 secciones) |
| 6.6 | `docs/informes/260208_ie_01_rev5.md` | Generar | Revisión Modelo 5 (evalúa 5 perspectivas × 6 secciones) |

**Perspectivas de Revisión:**
- **Precisión Técnica:** Exactitud de datos, fechas, terminología ISO, consistencia interna
- **Claridad y Redacción:** Gramática, claridad, coherencia narrativa, tono profesional
- **Completitud:** Cobertura del periodo, temas críticos, omisiones, contexto
- **Estructura y Formato:** Jerarquía de información, organización, tablas/figuras, navegabilidad
- **Accionabilidad:** Próximos pasos específicos, ownership, priorización, dependencias

**Estados de Evaluación:** OK, Ajuste menor, Ajuste mayor, Crítico

---

### Fase 7: Consolidación e Implementación de Ajustes

**Objetivo:** Integrar hallazgos de las 5 revisiones, priorizar, deduplicar, e implementar correcciones en el informe Markdown.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 7.1 | `docs/informes/260208_ie_01_rev_consolidado.md` | Crear | Matriz consolidada con hallazgos únicos de los 5 modelos, indicando consenso |
| 7.2 | Clasificar | Priorizar | Ordenar por severidad: Crítico > Mayor > Menor > OK |
| 7.3 | Deduplicar | Identificar | Hallazgos repetidos entre modelos (indica consenso fuerte) |
| 7.4 | `docs/informes/260208_ie_01.md` | Modificar | Implementar correcciones aprobadas en el informe fuente |
| 7.5 | Documentar | Registrar | Log de decisiones: qué se implementó, qué se descartó, justificaciones |

**Estructura del Consolidado:**
- Matriz por sección × perspectiva con hallazgos únicos
- Indicador de consenso: [M1] [M2] [M3] [M4] [M5] (qué modelos identificaron el hallazgo)
- Top 10 correcciones prioritarias
- Métricas de calidad por sección y por perspectiva

---

### Fase 8: Regeneración del Informe en Word

**Objetivo:** Generar versión final del documento Word con las correcciones aplicadas.

| # | Comando | Acción | Descripción |
|---|---------|--------|-------------|
| 8.1 | `pandoc -o docs/informes/260208_ie_01.docx docs/informes/260208_ie_01.md` | Ejecutar | Regenerar Word desde Markdown corregido |
| 8.2 | Verificar | Inspeccionar | Confirmar PNGs correctamente insertados en Word |
| 8.3 | Verificar | Inspeccionar | Revisar formato de tablas, encabezados en Word |

---

### Fase 9: Commit Final

**Objetivo:** Registrar versión final revisada en el repositorio.

| # | Acción | Descripción |
|---|--------|-------------|
| 9.1 | Actualizar plan | Marcar todas las fases como completadas en `plan_ie_01.md` |
| 9.2 | Git add | Agregar archivos modificados/nuevos (informe corregido, revisiones, consolidado) |
| 9.3 | Git commit | Commit con mensaje descriptivo de incorporación de revisiones |
| 9.4 | Push | Sincronizar con repositorio remoto (si se solicita) |

## Archivos Generados

| Archivo | Formato | Propósito |
|---------|---------|-----------|
| `logs/plans/plan_ie_01.md` | Markdown | Plan de ejecución |
| `docs/informes/260208_ie_01.md` | Markdown | Fuente editable del informe |
| `docs/informes/260208_ie_01.docx` | Word (.docx) | Documento final para distribución al equipo |
| `docs/informes/gantt_piloto.png` | PNG | Diagrama Gantt visual de la prueba piloto |
| `docs/informes/timeline_piloto.png` | PNG | Timeline semanal visual de la prueba piloto |
| `docs/informes/estructura_revision.md` | Markdown | Plantilla de estructura para revisiones |
| `docs/informes/260208_ie_01_rev1.md` | Markdown | Revisión Modelo 1 (5 perspectivas × 6 secciones) |
| `docs/informes/260208_ie_01_rev2.md` | Markdown | Revisión Modelo 2 (5 perspectivas × 6 secciones) |
| `docs/informes/260208_ie_01_rev3.md` | Markdown | Revisión Modelo 3 (5 perspectivas × 6 secciones) |
| `docs/informes/260208_ie_01_rev4.md` | Markdown | Revisión Modelo 4 (5 perspectivas × 6 secciones) |
| `docs/informes/260208_ie_01_rev5.md` | Markdown | Revisión Modelo 5 (5 perspectivas × 6 secciones) |
| `docs/informes/260208_ie_01_rev_consolidado.md` | Markdown | Matriz consolidada de hallazgos |

---

## Dependencias y Requisitos

| Herramienta | Versión | Estado | Comando de instalación |
|-------------|---------|--------|------------------------|
| **pandoc** | 3.9 | ✓ Disponible | Preinstalado en `/usr/bin/pandoc` |
| **mermaid-cli** | 11.12.0 | ✓ Disponible | Instalado con `npm install -g @mermaid-js/mermaid-cli` |
| **npm** | 25.2.1 | ✓ Disponible | Preinstalado en mise |

---

## Riesgos Identificados

| Riesgo | Severidad | Mitigación |
|--------|-----------|------------|
| mermaid-cli requiere puppeteer/chromium | Medium | Probar instalación con `mmdc --version` antes de generar PNGs |
| Timeline Mermaid muy largo para PNG (105 líneas) | High | Considerar dividir en múltiples imágenes o ajustar altura del PNG |
| Pandoc puede no incluir automáticamente imágenes PNG | Medium | Usar sintaxis `![Descripción](ruta/imagen.png)` estándar en Markdown |

---

## Contexto del Proyecto

| Parámetro | Valor |
|-----------|-------|
| **Proyecto** | CALAIRE-EA (Proyecto 61134: INM + UNAL) |
| **Objetivo** | Implementación de Ensayos de Aptitud (EA) para CO, NOx, SO2, O3 |
| **Fase Actual** | Fase II: Ejecución y Piloto (EN PROGRESO) |
| **Prueba Piloto** | Marzo-Mayo 2026 (reestructurada el 2026-02-07) |

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
- [ ] Fase 6 completada (2/5 revisiones: rev1, rev3 generados)
- [ ] Fase 7 iniciada
- [ ] Fase 7 completada
- [ ] Fase 8 iniciada
- [ ] Fase 8 completada
- [ ] Fase 9 iniciada
- [ ] Fase 9 completada
