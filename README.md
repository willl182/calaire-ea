# CALAIRE-EA Project Management

Este repositorio contiene el sistema de gestión del conocimiento y seguimiento del proyecto **CALAIRE-EA (Proyecto 61134)**: *Implementación de Ensayos de Aptitud para Gases Contaminantes Criterio*.

El sistema está construido sobre **Logseq**, utilizando una estructura de grafo para conectar tareas, documentos, reuniones y conocimientos técnicos.

El alcance vigente del proyecto llega hasta el **diseño del servicio** de comparaciones interlaboratorios/ensayos de aptitud, incluyendo alistamiento, prueba piloto y análisis de resultados.

## Estructura del Repositorio

*   **`journals/`**: Entradas diarias (bitácora de trabajo) con categorías estándar organizativas.
*   **`pages/`**: Notas permanentes, MOCs (Maps of Content), templates y gestión de conocimiento.
*   **`docs/`**: Documentación externa, referencias estáticas y sistema de clasificación de correos (`tags_project.csv`).
*   **`ref/`**: Referencias sobre el uso del sistema (guía de Logseq, setup y plan de estandarización).
*   **`logs/`**: Sesiones de trabajo del agente AI, hallazgos técnicos y registro de problemas.
*   **`logseq/`**: Configuración del grafo (queries, custom.css, config.edn).

## Estructura Contractual del Proyecto

El proyecto se ejecuta con trazabilidad de tres frentes contractuales:

| Componente | Ubicación | Rol en el proyecto |
|------------|-----------|--------------------|
| **Contrato 1 (2025)** | `docs/contrato_1/` | Base metodológica y documental: estado del arte, protocolos, procedimientos y avance SGC |
| **Contrato APP (2025, paralelo)** | `docs/contrato_app/` | Desarrollo del aplicativo estadístico CALAIRE-APP en R/Shiny |
| **Contrato 2 (2026)** | `docs/contrato_2/` | Alistamiento, ejecución de prueba piloto, revisión de resultados y ajustes de diseño |

Referencia ejecutiva consolidada: `ref/proyecto.md`

## Convenciones

*   **Idioma**:
    *   Contenido: Español.
    *   Propiedades/Tags estructurales: Inglés (e.g., `priority::`, `deadline::`, `type::`).
*   **Flujo de Trabajo**: `TODO` -> `DOING` -> `DONE`.

## Organización de Journals

Los journals diarios siguen una estructura estandarizada con 5 categorías para mantener consistencia:

| Categoría                | Contenido Típico                                           |
|--------------------------|------------------------------------------------------------|
| **Prueba Piloto**        | Rondas EA, confirmaciones laboratorios, logística equipos   |
| **Gestión Administrativa** | Cartas oficiales, comunicaciones, contratación           |
| **Desarrollo Técnico**   | CALAIRE-APP, protocolos, calibración                      |
| **SGC / Calidad**       | Auditorías, ISO 17043/13528, control documental            |
| **Infraestructura**      | Instalaciones, TI, transporte de equipos                     |

**Importante**: Los TODOs, DOING, DONE y #decision deben ubicarse **dentro de la categoría temática** correspondiente, no sueltos al final del journal. Esto mantiene contexto inmediato y evita duplicación.

Uso: ejecutar `/template journal-daily` en el journal del día y eliminar secciones que no apliquen.

## Templates Disponibles

Templates definidos en `pages/templates.md`:

*   **Reunión**: Actas con asistentes, decisiones y acciones.
*   **Protocolo Técnico**: Documentación de gases (CO, NOx, SO2, O3).
*   **Ronda Piloto**: Seguimiento de logística y resultados por laboratorio/semana.
*   **Entregable**: Seguimiento de hitos con plazos y criterios de aceptación.
*   **Journal Diario**: Estructura estandarizada para registros diarios.

## Sistema de Clasificación de Correos

El archivo `docs/tags_project.csv` define etiquetas para clasificar correos de Gmail con mapeo explícito a las categorías del journal.

*   10 grupos de clasificación
*   29 etiquetas totales (incluyendo subtags para granularidad)
*   Columna `Categoria_Journal` para trazabilidad correo ↔ grafo
*   Regla uno a uno: cada etiqueta corresponde a una sola categoría del journal

## MOCs Principales (Puntos de Entrada)

*   `[[CALAIRE-EA]]`: Visión general del proyecto.
*   `[[Prueba Piloto]]`: Coordinación operativa de las rondas EA.
*   `[[CALAIRE-APP]]`: Desarrollo del software estadístico.
*   `[[QMS]]`: Gestión de calidad y normas ISO 17043/13528.
*   `[[Laboratorios]]`: Registro de laboratorios participantes (MOC que lista todos los laboratorios con enlaces a sus páginas individuales).
*   `[[Equipos]]`: Inventario de equipos de medición y calibración.
*   `[[Equipo]]`: Roles y responsabilidades del equipo del proyecto.

## Categorías Temáticas (Journal) como MOCs

Las categorías estándar del journal funcionan como páginas MOC para navegación temática:

*   `[[Gestión Administrativa]]`
*   `[[Desarrollo Técnico]]`
*   `[[Infraestructura]]`
*   `[[Prueba Piloto]]`
*   `[[SGC / Calidad]]` (referenciada en `pages/QMS.md`)

## Páginas de Laboratorios

Cada laboratorio participante tiene su propia página individual con:
*   Información de la institución y ubicación
*   Estatus de participación por ronda (#confirmado, #contactado, #candidato)
*   Inventario de equipos (CO, NOx, SO2, O3)
*   Observaciones y documentación relevante

Laboratorios actuales:
*   `[[SIATA]]` (Sistema de Alerta Temprana)
*   `[[Universidad de Medellín]]`
*   `[[Universidad Pontificia Bolivariana]]`

Para crear una nueva página de laboratorio, ver la estructura en `ref/setup.md` sección 2.5.

## Documentación Técnica

*   **`ref/setup.md`**: Configuración inicial, estandarización de journals, sistema de clasificación de correos y templates.
*   **`AGENTS.md`**: Guía para el agente AI, incluyendo directrices de desarrollo de contenido y sintaxis de Logseq.
*   **`ref/logseq.md`**: Guía completa de Logseq para gestión profesional del conocimiento.

## Logs de Sesiones

El directorio `logs/` mantiene registro de las sesiones del agente AI:

*   **`CURRENT_SESSION.md`**: Estado actual de la sesión (mutable).
*   **`logs/history/*_findings.md`**: Hallazgos técnicos y milestones.
*   **`logs/history/*_problems.md`**: Bloqueos, errores y lecciones aprendidas.

## Setup Inicial

Para configurar este grafo desde cero o entender el sistema de estandarización implementado, seguir las instrucciones en `ref/setup.md`.
