# Plan: Coordinación Laboratorios + CALAIRE-APP + Roles

**Created**: 2026-02-05 13:56
**Updated**: 2026-02-05 14:02
**Status**: in_progress
**Slug**: `coordinacion-labs-app-roles`

---

## Objetivo

Registrar noticias del día (Gelima/UPB confirma Ronda 5, SIATA pendiente confirmación, potencial suplencia técnica, César Yate devolvió primeros resultados de CALAIRE-APP), coordinar confirmaciones de laboratorios, preparar invitación a Politécnico Isaza Cadavid, y documentar roles de suplencia.

---

## Fases

### Fase 1: Registro de Noticias del Día

**Objetivo:** Documentar en journal las novedades recibidas el 5 de febrero 2026.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | `journals/2026_02_05.md` | Crear | Registrar: Gelima (Universidad Pontificia Bolivariana) confirma Ronda 5 (8-13 abril), SIATA pendiente de confirmación por llamada para Rondas 1-2 (semanas 3-4 febrero), potencial suplencia técnica si se concreta nueva contratación, César Yate (consultor ISO 17043) devolvió primeros resultados de CALAIRE-APP |
| 1.2 | `pages/CALAIRE-APP.md` | Modificar | Agregar tarea: "TODO Revisar primeros resultados de César Yate y aplicar ajustes técnicos" con `priority:: high`, `deadline:: 2026-02-10` |

---

### Fase 2: Actualización Confirmaciones Laboratorios

**Objetivo:** Actualizar estado de confirmación de UPB/Gelima y mantener estado de SIATA como pendiente.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | `pages/Universidad Pontificia Bolivariana.md` | Modificar | Actualizar `[[Ronda 5]]: #confirmado`, agregar observación "Confirmación recibida 2026-02-05 para 2da semana de abril (Ronda 5)" |
| 2.2 | `pages/SIATA.md` | Modificar | Mantener `status:: #candidato`, agregar observación "Pendiente confirmación definitiva por llamada - seguimiento activo" |
| 2.3 | `pages/Prueba Piloto.md` | Modificar | Actualizar sección "Confirmaciones de Laboratorios": `[[Universidad Pontificia Bolivariana]] :: Confirmada para Ronda 5`, mantener `[[SIATA]] :: Pendiente confirmación (semanas 3-4 febrero)` |
| 2.4 | `pages/Ronda 5.md` | Modificar | Agregar `[[Universidad Pontificia Bolivariana]]` como laboratorio confirmado |
| 2.5 | `pages/Laboratorios.md` | Modificar | Mover `[[Universidad Pontificia Bolivariana]]` de "Laboratorios Contactados" a "Laboratorios Confirmados" |

---

### Fase 3: Gestión Contacto Politécnico Isaza Cadavid

**Objetivo:** Preparar estructura para invitación a la profesora Myryam del Politécnico Isaza Cadavid.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | `pages/Politécnico Colombiano Jaime Isaza Cadavid.md` | Crear | Página de laboratorio con `status:: #candidato`, contacto pendiente: "Profe Myryam (correo por buscar, teléfono: usuario buscará manualmente)" |
| 3.2 | `pages/Laboratorios.md` | Modificar | Agregar `[[Politécnico Colombiano Jaime Isaza Cadavid]]` en sección "Candidatos" |
| 3.3 | `docs/carta_politecnico_v1.md` | Crear | Borrador basado en estructura de `docs/carta_gica_v3.md`, adaptar destinatario (Profe Myryam) y fechas disponibles del calendario piloto |

**Nota:** Búsqueda de correo de profe Myryam no fue posible vía Google Search en entorno actual. Usuario confirmó que buscará teléfono manualmente.

---

### Fase 4: Documentación Roles y Suplencia

**Objetivo:** Documentar esquema de suplencia técnica contingente.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | `pages/Fabian Moreno.md` | Modificar | Agregar sección "## Rol de Suplencia" explicando: "En caso de concretarse nueva contratación, Fabián asume rol de backup técnico para operaciones de calibración y pruebas." |
| 4.2 | `pages/Equipo.md` | Modificar | Agregar subsección en "Técnico" sobre esquema de suplencia: "[Nuevo contratado - pendiente] como técnico principal, Fabián Moreno como backup técnico" |

---

### Fase 5: Actualización Estado Sesión

**Objetivo:** Sincronizar `CURRENT_SESSION.md` con nuevo estado del proyecto.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 5.1 | `logs/CURRENT_SESSION.md` | Modificar | Actualizar objetivo: "Coordinación de laboratorios participantes en Prueba Piloto y revisión de resultados CALAIRE-APP", listar confirmaciones actualizadas (UPB confirmada Ronda 5, SIATA pendiente), mencionar revisión pendiente de César Yate |

---

### Placeholder: Ajustes CALAIRE-APP (Info Pendiente)

**Objetivo:** Una vez el usuario proporcione la información adicional de César Yate sobre los resultados de CALAIRE-APP, agregar fase específica para documentar discrepancias y planificar los ajustes requeridos.

**Contexto:** César Yate es consultor experto en ISO 17043 (ensayos de aptitud) y está validando los cálculos estadísticos del aplicativo (homogeneidad, estabilidad, MADe) según ISO 13528.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| P.1 | `journals/2026_02_05.md` | Modificar | Registrar detalles técnicos de discrepancias reportadas por César (cálculos aplicativo vs manual) |
| P.2 | `pages/CALAIRE-APP.md` | Modificar | Agregar tareas específicas de corrección según análisis (ej: TODO Corregir algoritmo X, TODO Validar cálculo Y) |

---

## Resumen

| Tipo | Cantidad | Archivos |
|------|----------|----------|
| **Crear** | 3 | `journals/2026_02_05.md`, `pages/Politécnico Colombiano Jaime Isaza Cadavid.md`, `docs/carta_politecnico_v1.md` |
| **Modificar** | 9 | `pages/CALAIRE-APP.md`, `pages/Universidad Pontificia Bolivariana.md`, `pages/SIATA.md`, `pages/Prueba Piloto.md`, `pages/Ronda 5.md`, `pages/Laboratorios.md`, `pages/Fabian Moreno.md`, `pages/Equipo.md`, `logs/CURRENT_SESSION.md` |

---

## Log de Ejecución

- [x] Fase 1: Registro de Noticias del Día iniciada
- [x] Fase 1: Registro de Noticias del Día completada
- [ ] Fase 2: Actualización Confirmaciones Laboratorios iniciada
- [ ] Fase 2: Actualización Confirmaciones Laboratorios completada
- [ ] Fase 3: Gestión Contacto Politécnico Isaza Cadavid iniciada
- [ ] Fase 3: Gestión Contacto Politécnico Isaza Cadavid completada
- [ ] Fase 4: Documentación Roles y Suplencia iniciada
- [ ] Fase 4: Documentación Roles y Suplencia completada
- [ ] Fase 5: Actualización Estado Sesión iniciada
- [ ] Fase 5: Actualización Estado Sesión completada
- [ ] Placeholder: Ajustes CALAIRE-APP (pendiente info usuario sobre César)

---

## Resultados de Revisión (Subagente) - Fase 1

**Hallazgos críticos:** Ninguno.

**Hallazgos importantes** (corregidos):
- Indentación con mezcla de tabs y espacios en propiedades de `journals/2026_02_05.md`: corregido a tabs únicos
- Inconsistencia con convención de idioma para tags/propiedades (`status:: #confirmado` vs inglés): corregido a `status:: confirmed` (sin #)
- Encabezado `# Registro del Día` sin prefijo de bloque: corregido a `- # Registro del Día`
- Nuevo TODO en `pages/CALAIRE-APP.md` sin `project:: [[CALAIRE-EA]]`: corregido

**Hallazgos menores:** Ninguno después de correcciones.

**Riesgos mitigados:**
- Jerarquía de bloques en Logseq ahora consistente con tabs
- Queries globales de `[[CALAIRE-EA]]` ahora incluirán el nuevo TODO
- Convención de idioma para propiedades alineada con estándar del proyecto

**Recomendaciones del revisor aplicadas:**
1. Normalizar indentación con tabs ✅
2. Estandarizar `status::` a valores en inglés (sin #) ✅
3. Añadir `project:: [[CALAIRE-EA]]` al nuevo TODO ✅

**Checklist de verificación del revisor - Fase 1** (4/4 completados):
- [x] `journals/2026_02_05.md` usa tabs sin espacios en propiedades
- [x] `status::` consistente con convención de tags en inglés (sin tag #)
- [x] Nuevo TODO en `pages/CALAIRE-APP.md` aparece en query de tareas de `[[CALAIRE-EA]]`
- [x] Vista en Logseq confirma jerarquía correcta de bloques y propiedades
