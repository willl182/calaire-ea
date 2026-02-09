# Plan: Sistema de Seguimiento de Tareas CALAIRE-EA

**Created**: 2026-02-08 19:52
**Updated**: 2026-02-08 20:02
**Status**: completed
**Slug**: seguimiento-tareas-csv

---

## Objetivo

Implementar un sistema automatizado para extraer, exportar y hacer seguimiento de todas las tareas del grafo Logseq mediante CSV, Google Sheets y alertas automáticas. Esto evitará que las tareas con deadline pasen desapercibidas.

---

## Fases

### Fase 1: Crear Plan Documentado

**Objetivo:** Documentar el sistema de seguimiento en el plan actual

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | `logs/plans/260208_1952_plan_seguimiento-tareas-csv.md` | Crear | Archivo de plan con estructura y fases |

### Fase 2: Extracción Manual → CSV

**Objetivo:** Generar CSV inicial con todas las tareas con deadline del grafo

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | `tareas_calaire.csv` | Crear | CSV con tareas de `pages/CALAIRE-APP.md`, `pages/Prueba Piloto.md`, `pages/CALAIRE-EA.md` y `journals/` |
| 2.2 | `tareas_calaire.csv` | Verificar | Validar que todas las tareas tengan: id, tarea, deadline, prioridad, proyecto, fuente, estado, notas |

**Columnas del CSV:**
```
id,tarea,deadline,prioridad,proyecto,fuente,estado,notas
```

### Fase 3: Script Python de Exportación

**Objetivo:** Crear script reutilizable para extraer tareas del grafo Logseq

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | `tools/export_tareas.py` | Crear | Script que lee `pages/*.md` y `journals/*.md`, extrae TODO/DOING/DONE y propiedades |
| 3.2 | `tools/export_tareas.py` | Implementar | Regex para detectar bloques TODO/DOING/DONE y propiedades (deadline::, priority::, project::) |
| 3.3 | `tools/export_tareas.py` | Implementar | Generación de CSV ordenado por deadline |
| 3.4 | `tools/export_tareas.py` | Documentar | Comentarios de uso: `python tools/export_tareas.py --output tareas_calaire.csv` |

### Fase 4: Google Apps Script de Alertas

**Objetivo:** Crear script para Google Sheets que envíe alertas por email

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | `tools/alertas_tareas.gs` | Crear | Archivo con Google Apps Script |
| 4.2 | `tools/alertas_tareas.gs` | Implementar | Función `enviarAlertas()` que revisa columna Deadline |
| 4.3 | `tools/alertas_tareas.gs` | Implementar | Lógica de alerta: enviar email si faltan ≤3 días |
| 4.4 | `tools/alertas_tareas.gs` | Implementar | Función `formatoCondicional()` para colores: rojo=vencido, amarillo=próximo (≤3 días), verde=completado |
| 4.5 | `tools/alertas_tareas.gs` | Documentar | Instrucciones para instalar trigger diario a las 8am |

---

## Log de Ejecución

- [x] Fase 1 iniciada - Plan creado
- [x] Fase 1 completada
- [x] Fase 2 iniciada - Extracción manual de tareas
- [x] Fase 2 completada - CSV generado (15 tareas iniciales)
- [x] Fase 3 iniciada - Script Python creado
- [x] Fase 3 completada - Script Python funcional (28 tareas extraídas)
- [x] Fase 4 iniciada - Google Apps Script creado
- [x] Fase 4 completada - Sistema de alertas activo (requiere configuración en Google Sheets)

## Hallazgos de la Fase 3

El script Python detectó **28 tareas** en total, distribuidas en:
- 6 archivos de pages/ (CALAIRE-APP, Prueba Piloto, QMS)
- 3 archivos de journals/
- 13 tareas con deadline
- 22 TODOs, 1 DOING, 5 DONEs

El CSV generado por el script reemplaza el CSV manual inicial con una extracción más completa y automatizada.

## Entregables Finales

| Archivo | Descripción |
|---------|-------------|
| `tareas_calaire.csv` | CSV con 28 tareas del grafo |
| `tools/export_tareas.py` | Script Python reutilizable |
| `tools/alertas_tareas.gs` | Google Apps Script para alertas |
| `tools/README_SEGUIMIENTO.md` | Documentación completa del sistema |

## Próximos Pasos (Usuario)

1. **Configurar Google Sheets:**
   - Importar `tareas_calaire.csv` en una hoja nueva
   - Instalar el Apps Script cambiando el email
   - Ejecutar `configurarTrigger()` para activar alertas

2. **Flujo de trabajo recurrente:**
   - Ejecutar `python tools/export_tareas.py` para actualizar el CSV
   - Subir el CSV a Google Sheets (importación o copy-paste)
   - Revisar alertas diarias por email
