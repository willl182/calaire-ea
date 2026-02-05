# Registro de Implementación - Proyecto CALAIRE-EA (Logseq Setup)

Este documento detalla la configuración y estructura del grafo de Logseq implementada para la gestión del proyecto 61134 (CALAIRE-EA).

**Estado:** ✅ Implementado
**Fecha:** 2026-02-03

## 1. Inicialización Git

1.  **Repositorio**: Inicializado en raíz.
2.  **`.gitignore`**: Configurado para excluir archivos de sistema y caché de Logseq.
    *   `.DS_Store`
    *   `bak/`
    *   `pages-metadata.edn`
    *   `logseq/graphs-txid.edn`
    *   `logseq/.recycle/`
3.  **Control de Versiones**: Primer commit realizado con la estructura base.

## 2. Estructura de Páginas (MOCs)

Se han creado las siguientes páginas en `/pages/` para centralizar la información:

| Archivo | Propósito | Contenido Implementado |
| :--- | :--- | :--- |
| `CALAIRE-EA.md` | **MOC Principal** | Visión general, enlaces a fases, hitos, documentos maestros. |
| `CALAIRE-APP.md` | **Aplicativo** | Gestión del desarrollo del software estadístico, repositorio, bugs, features. |
| `Prueba Piloto.md` | **Ejecución** | Coordinación de las 4 rondas de marzo, logística de equipos, cronograma. |
| `Laboratorios.md` | **Base de Datos** | MOC que lista todos los laboratorios participantes con enlaces a páginas individuales. |
| `SIATA.md` | **Laboratorio** | Página individual para Sistema de Alerta Temprana (candidato). |
| `Universidad de Medellín.md` | **Laboratorio** | Página individual para Universidad de Medellín (confirmado Rondas 3-4). |
| `Universidad Pontificia Bolivariana.md` | **Laboratorio** | Página individual para UPB (contactado, carta enviada). |
| `QMS.md` | **Calidad** | Integración ISO 17043/13528, listado de documentos F-GCM-03. |
| `Equipo.md` | **Personas** | Directorio del equipo (Carmen Elena, Jeniffer, David Esteban), roles. |
| `templates.md` | **Sistema** | Archivo contenedor para todos los templates de Logseq. |

### Categorías Temáticas (Journal) como MOCs

Las 5 categorías estándar del journal también funcionan como páginas MOC navegables para organizar el conocimiento por tema. Estas páginas consolidan etiquetas de correo y referencias clave:

- `pages/Gestión Administrativa.md`
- `pages/Desarrollo Técnico.md`
- `pages/Infraestructura.md`
- `pages/Prueba Piloto.md`
- `pages/QMS.md` (alias `[[SGC / Calidad]]` en journals)

Estas categorías están enlazadas desde `pages/CALAIRE-EA.md` en la sección “Categorías Temáticas (Journal)”.

### Sistema de Equipos

Se creó un MOC de inventario para equipos de medición y calibración:

- `pages/Equipos.md`: índice central de analizadores y calibradores usados en las rondas.
- `pages/Calibrador T700.md`: página técnica de referencia como ejemplo de equipo individual.

Para agregar un nuevo equipo:

1. Crear una página individual en `/pages/` siguiendo la plantilla incluida en `pages/Equipos.md`.
2. Añadir el enlace del equipo en la sección correspondiente de `pages/Equipos.md` (Medición o Calibración).
3. Vincularlo con `[[Prueba Piloto]]` y `[[Laboratorios]]` si aplica.

### Estructura de Páginas de Laboratorios

Cada laboratorio participante debe tener su propia página individual en `/pages/` con la siguiente estructura estándar:

```
- tags:: [[Laboratorio]]
- # Nombre del Laboratorio
  type:: [[Laboratorio]]
  status:: #confirmado | #contactado | #candidato | #inactivo
  institution:: Nombre de la institución
  location:: Ciudad
- ## Participación en Rondas EA
    - [[Ronda X]]: #confirmado | #pendiente
- ## Equipos
    - CO: [[Analizador Modelo X]]
    - NOx: [[Analizador Modelo Y]]
    - SO2: [[Analizador Modelo Z]]
    - O3: [[Analizador Modelo W]]
- ## Observaciones
    - 
- ## Documentación
    - 
```

**MOC `[[Laboratorios]]`**: Actúa como índice centralizado que lista todos los laboratorios con enlaces a sus páginas individuales, organizados por estatus:
- **Laboratorios Confirmados**
- **Laboratorios Contactados**
- **Candidatos**

**Estatus de Laboratorio:**

| Status | Significado |
|--------|-------------|
| `#confirmado` | Ha confirmado participación explícita |
| `#contactado` | Se ha enviado carta/invitación oficial |
| `#candidato` | En lista de posibles participantes |
| `#inactivo` | Participó anteriormente pero no en esta ronda |

**Propósito:** Permite trazabilidad detallada por laboratorio, histórico de participación en rondas, y gestión de inventario de equipos.

## 3. Templates

Templates disponibles en `pages/templates.md`:

1.  **Reunión** (`template:: reunion`): Estructura para actas con asistentes, decisiones y acciones.
2.  **Protocolo Técnico** (`template:: protocolo`): Estructura para documentación de gases (CO, NOx, SO2, O3).
3.  **Ronda Piloto** (`template:: ronda-piloto`): Seguimiento de logística y resultados por laboratorio/semana.
4.  **Entregable** (`template:: entregable`): Seguimiento de hitos con plazos y criterios de aceptación.
5.  **Journal Diario** (`template:: journal-daily`): Estructura estándar para registros diarios con categorías organizativas.

## 4. Configuración de Queries

Se ha actualizado `logseq/config.edn` (`:default-queries`) para visualización automática en el Journal:

1.  **📋 CALAIRE-EA Tasks**: Muestra todos los TODO/DOING/NOW/LATER vinculados a la página `[[CALAIRE-EA]]`.
2.  **🎯 Decisiones Recientes**: Rastrea automáticamente cualquier bloque con el tag `#decision`.
3.  **Default**: Se mantienen las secciones "🔨 NOW" y "📅 NEXT".

## 5. Categorías Estándar para Journals

Categorías definidas para el registro diario:

| Categoría                | Contenido Típico                                           |
|--------------------------|------------------------------------------------------------|
| **Prueba Piloto**        | Rondas EA, confirmaciones laboratorios, logística equipos   |
| **Gestión Administrativa** | Cartas oficiales, comunicaciones, contratación           |
| **Desarrollo Técnico**   | CALAIRE-APP, protocolos, calibración                      |
| **SGC / Calidad**       | Auditorías, ISO 17043/13528, control documental            |
| **Infraestructura**      | Instalaciones, TI, transporte de equipos                     |

**Criterio de uso**:
- Solo se crean las secciones que apliquen ese día (no forzar secciones vacías).
- Las secciones extensas van con `collapsed:: true`.

**Convención para notas históricas**:
- Journals con contenido mínimo (2 líneas o menos): marcar como `- #nota-historica`.
- Journals con cronogramas/diagramas desactualizados: encapsular bajo `#version-historica` y colapsar.

## 6. Sistema de Clasificación de Correos

Archivo de referencia: `docs/tags_project.csv`

### Estructura

- **10 grupos de clasificación** (Acción Requerida, Gestión Financiera, Seguimiento y Entregas, Comunicaciones, Referencia, Operación Técnica, Calidad/SGC, Infraestructura, Actividades Transversales)
- **29 etiquetas totales** (incluyendo subtags para granularidad)
- **Columna `Categoria_Journal`**: mapeo explícito entre etiqueta de correo y categoría del journal
- **Regla de uno a uno**: cada etiqueta de correo debe mapearse a una sola categoría de journal para clasificar con precisión

### Mapeo Recomendado

| Categoría Journal | Tags Correo Asociados |
|-------------------|----------------------|
| Prueba Piloto | `[TECH] Ronda*`, `[EVENTO] Taller`, `[Seguimiento] Entregable - Técnico` |
| Gestión Administrativa | `[ACCION] *`, `[Finanzas] *`, `[EVENTO] Socialización`, `[EVENTO] Congreso/Evento`, `[Seguimiento] Entregable - Administrativo`, `[Comunicado] Stakeholders` |
| Desarrollo Técnico | `[TECH] Desarrollo App`, `[TECH] Calibración`, `[EVENTO] Capacitacion` |
| SGC / Calidad | `[SGC] *` |
| Infraestructura | `[INFRA] *` |

### Regla de Clasificación

- Un correo debe tener **una etiqueta primaria** y, por tanto, **una categoría de journal** asociada.
- Evitar asignaciones múltiples a distintas categorías para mantener trazabilidad y consultas consistentes.

### Propósito

Centralizar la clasificación de correos de Gmail con trazabilidad explícita al grafo de Logseq. Cada correo etiquetado tiene una categoría de journal correspondiente, facilitando la conversión de comunicación externa a registro de conocimiento.

## 7. Instrucciones de Uso

### Operaciones Básicas

1.  **Nueva Tarea**: Crear bloque en Journal -> `TODO Tarea... project:: [[CALAIRE-EA]]`.
2.  **Nueva Reunión**: En Journal -> Escribir `[[Reunión: Tema]]`, entrar a la página y aplicar template `reunion`.
3.  **Ver Progreso**: Ir a la página `[[CALAIRE-EA]]` o revisar la sección inferior del Journal diario.

### Uso del Journal Diario

Para mantener consistencia en los registros diarios, usar el template `journal-daily`:

1.  Ejecutar `/template journal-daily` en el journal del día.
2.  Eliminar secciones que no apliquen (no forzar secciones vacías).
3.  Usar `collapsed:: true` para secciones extensas.
4.  Reuniones formales se registran como `#[[Reunión: Tema]]` y se usa el template `reunion`.

### Ubicación de TODOs y Decisiones

- **TODOs** y **#decision** van **dentro de la categoría temática** correspondiente.
- No crear secciones separadas para tareas al final del journal.
- Esto mantiene contexto inmediato y evita duplicación.

| Tipo de bloque | Ubicación |
|----------------|-----------|
| `TODO`, `DOING`, `DONE` | Bajo la categoría temática donde aplica |
| `#decision` | Bajo la categoría donde aplica la decisión |

### Categorías Estándar

| Categoría                | Contenido Típico                                           |
|--------------------------|------------------------------------------------------------|
| **Prueba Piloto**        | Rondas EA, confirmaciones laboratorios, logística equipos   |
| **Gestión Administrativa** | Cartas oficiales, comunicaciones, contratación           |
| **Desarrollo Técnico**   | CALAIRE-APP, protocolos, calibración                      |
| **SGC / Calidad**       | Auditorías, ISO 17043/13528, control documental            |
| **Infraestructura**      | Instalaciones, TI, transporte de equipos                     |

### Convención para Notas Históricas

- Journals con contenido mínimo (2 líneas o menos): marcar como `- #nota-historica`.
- Journals con cronogramas/diagramas desactualizados: encapsular bajo `#version-historica` y colapsar.

### Directrices de Desarrollo de Contenido (para Agente AI)

**Input Processing**: El usuario proporciona notas rápidas en español. El agente debe:

1. **Expandir y desarrollar** el contenido en prosa técnica bien estructurada.
2. **Usar vocabulario apropiado al dominio** (metrología, ensayos de aptitud, estándares ISO).
3. **Agregar contexto y detalle** que clarifique la significancia técnica.
4. **Nunca copiar la entrada del usuario literalmente** - siempre reformular y enriquecer.

**Ejemplos**:

| Entrada Usuario | Salida Agente |
|-----------------|-----------------|
| "UdeM confirmó rondas 3 y 4" | "**Universidad de Medellín:** respuesta positiva recibida. Confirman disponibilidad para participar en [[Ronda 3]] y [[Ronda 4]] del calendario piloto (periodos 18-23 de marzo y 25-30 de marzo 2026 respectivamente)." |
| "verificando espacio al lado del lab" | "**Verificación de espacio físico:** en evaluación activa la disponibilidad del área contigua al laboratorio de gases para almacenamiento temporal de equipos y operaciones auxiliares durante las rondas de ensayo." |

**Tono**:
- Técnico y profesional
- Tercera persona o voz impersonal
- Evitar coloquialismos
- Incluir enlaces relevantes a MOCs (`[[Prueba Piloto]]`, `[[CALAIRE-EA]]`, etc.)
