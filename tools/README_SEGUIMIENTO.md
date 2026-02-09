# Sistema de Seguimiento de Tareas CALAIRE-EA

Este sistema automatiza el seguimiento de tareas del grafo Logseq mediante exportación a CSV, Google Sheets y alertas por email.

---

## Componentes

| Componente | Archivo | Descripción |
|------------|---------|-------------|
| CSV | `tareas_calaire.csv` | Archivo CSV con todas las tareas del grafo |
| Exportador | `tools/export_tareas.py` | Script Python que extrae tareas de Logseq a CSV |
| Alertas | `tools/alertas_tareas.gs` | Google Apps Script para alertas automáticas |

---

## Uso Rápido

### 1. Exportar Tareas a CSV

Ejecuta el script Python para actualizar el CSV con las tareas más recientes:

```bash
python tools/export_tareas.py
```

**Opciones:**
```bash
# Especificar archivo de salida
python tools/export_tareas.py --output mis_tareas.csv

# Especificar directorios personalizados
python tools/export_tareas.py --pages pages/ --journals journals/
```

**Salida:**
- `tareas_calaire.csv` (por defecto)
- Resumen de tareas encontradas por archivo
- Estadísticas: con deadline, TODOs, DOING, DONE

---

### 2. Subir a Google Sheets

1. Abre [Google Sheets](https://sheets.google.com)
2. Crea una hoja nueva: "Tareas CALAIRE-EA"
3. **Opción A - Importar:**
   - Archivo → Importar
   - Sube `tareas_calaire.csv`
4. **Opción B - Copy-Paste:**
   - Copia el contenido del CSV
   - Pega en la hoja

---

### 3. Configurar Alertas Automáticas

#### Instalar el Script

1. En tu hoja de Google Sheets, ve a **Extensiones > Apps Script**
2. Copia el contenido de `tools/alertas_tareas.gs`
3. Pega en el editor de Apps Script
4. **IMPORTANTE:** Cambia `tu-email@ejemplo.com` en la línea 15 por tu email real

#### Activar Trigger

1. En el editor de Apps Script, selecciona la función `configurarTrigger`
2. Haz clic en **Ejecutar**
3. Concede los permisos solicitados (Gmail, Hojas de cálculo)

**Resultado:** El sistema enviará alertas automáticas diariamente a las 8am para tareas con deadline en los próximos 3 días.

---

## Formato del CSV

| Columna | Descripción |
|---------|-------------|
| `id` | Identificador único (ej: APP-01, PI-02) |
| `tarea` | Descripción de la tarea |
| `deadline` | Fecha límite (YYYY-MM-DD) o vacío |
| `prioridad` | `high`, `medium`, `low` o vacío |
| `proyecto` | Proyecto asociado (CALAIRE-APP, CALAIRE-EA) |
| `fuente` | Archivo de origen en Logseq |
| `estado` | `todo`, `doing`, `done` |
| `notas` | Notas adicionales |

---

## Cómo Funciona el Script Python

### Detección de Tareas

El script busca bloques en formato Logseq:

```markdown
- TODO Descripción de la tarea
  project:: [[CALAIRE-APP]]
  priority:: high
  deadline:: 2026-02-15
```

Soporta:
- `TODO`, `DOING`, `DONE` como estado
- Bloques con o sin indentación (tabuladores)
- Propiedades en sub-líneas

### Extracción de Propiedades

| Propiedad | Formato Logseq |
|-----------|----------------|
| deadline | `deadline:: 2026-02-15` |
| priority | `priority:: high` |
| project | `project:: [[CALAIRE-APP]]` |
| status | `status:: pending` |

### Ordenamiento

El CSV se ordena automáticamente:
1. Tareas con deadline primero (cronológicamente)
2. Tareas sin deadline al final (por ID)

---

## Cómo Funcionan las Alertas de Google Sheets

### Lógica de Alertas

El script `alertas_tareas.gs` ejecuta automáticamente:

1. **Diariamente a las 8am:** Lee la hoja de tareas
2. **Calcula días restantes:** `deadline - hoy`
3. **Envía email:** Si `0 < días_restantes ≤ 3`
4. **Actualiza colores:** Formato condicional en la hoja

### Colores de Formato Condicional

| Condición | Color |
|-----------|-------|
| Estado = DONE/done | Verde (`#d4edda`) |
| Deadline < hoy | Rojo (`#f8d7da`) |
| Prioridad = high | Naranja claro (`#fff3cd`) |

### Email de Alerta

El email incluye:
- Lista de tareas próximas (≤3 días)
- Prioridad, proyecto, deadline, días restantes
- Enlace directo a la hoja de Google Sheets

---

## Funciones Adicionales (Apps Script)

### Testear Alertas

Para verificar configuración sin esperar al trigger:

1. En Apps Script, selecciona `testAlertas`
2. Ejecutar
3. Revisa el email recibido

### Ver Estadísticas

Para ver estadísticas de la hoja actual:

1. Selecciona `estadisticas`
2. Ejecutar
3. Revisa el log de ejecución

Salida:
```
📊 Estadísticas de Tareas:
Total: 28
Con deadline: 13
Vencidas: 2
Próximas (≤3 días): 5
Completadas: 5
Alta prioridad: 8
```

---

## Flujo de Trabajo Completo

```
Logseq (Markdown)
    ↓
tools/export_tareas.py
    ↓
tareas_calaire.csv
    ↓
Google Sheets (importación manual o Drive sync)
    ↓
Google Apps Script (alertas automáticas)
    ↓
Email con tareas próximas
```

---

## Mejores Prácticas

### Para Logseq

1. **Usa formato consistente:**
   ```markdown
   - TODO Tarea descriptiva
     project:: [[Nombre del Proyecto]]
     priority:: high
     deadline:: 2026-02-15
   ```

2. **Agrega fechas siempre que sea posible**
3. **Usa prioridades para tareas urgentes**

### Para Google Sheets

1. **Actualiza el CSV semanalmente** o después de cambios importantes
2. **Marca tareas completadas** cambiando `estado` a `done`
3. **Revisa alertas diariamente** y actúa sobre tareas vencidas

### Mantenimiento

- **Limpiar trigger antiguo:** Si necesitas reconfigurar, ejecuta `configurarTrigger` nuevamente
- **Cambiar email:** Edita `CONFIG.EMAIL` en `alertas_tareas.gs`
- **Ajustar días de anticipación:** Cambia `CONFIG.ALERT_DAYS` en `alertas_tareas.gs`

---

## Resolución de Problemas

### Script Python no encuentra tareas

- **Verifica formato:** Los bloques deben usar `- TODO`, `- DOING`, o `- DONE`
- **Verifica indentación:** Use tabuladores, no espacios
- **Revisa rutas:** El script usa directorios relativos al proyecto

### Alertas no llegan

- **Verifica email:** Configura `CONFIG.EMAIL` en el Apps Script
- **Verifica permisos:** Concede permisos a Gmail y Sheets
- **Revisa trigger:** Ejecuta `configurarTrigger()` para reinstalar
- **Testea manualmente:** Ejecuta `testAlertas()` para verificar

### Colores no aplican

- **Ejecuta manualmente:** Ejecuta `formatoCondicional()` en Apps Script
- **Verifica columnas:** Asegúrate de que las columnas coincidan con el CSV

---

## Referencias

- **Plan de implementación:** `logs/plans/260208_1952_plan_seguimiento-tareas-csv.md`
- **Documentación de Logseq:** `ref/logseq.md`
- **AGENTS.md:** Directrices del grafo Logseq CALAIRE-EA

---

## Notas

- El script Python ignora archivos en `.gitignore`
- Solo lee archivos `.md` en `pages/` y `journals/`
- Los IDs se generan automáticamente basándose en el proyecto
- El CSV usa punto y coma (;) como separador en lugar de comas en campos de texto para evitar conflictos
