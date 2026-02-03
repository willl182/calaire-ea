# Registro de Implementación - Proyecto CALAIRE-EA (Logseq Setup)

Este documento detalla la configuración y estructura del grafo de Logseq implementada para la gestión del proyecto 61134 (CALAIRE-EA).

**Estado:** ✅ Implementado | 🔄 Actualización en curso
**Fecha:** 2026-02-03

## Fase 1: Inicialización Git (✅ Completado)

1.  **Repositorio**: Inicializado en raíz.
2.  **`.gitignore`**: Configurado para excluir archivos de sistema y caché de Logseq.
    *   `.DS_Store`
    *   `bak/`
    *   `pages-metadata.edn`
    *   `logseq/graphs-txid.edn`
    *   `logseq/.recycle/`
3.  **Control de Versiones**: Primer commit realizado con la estructura base.

## Fase 2: Estructura de Páginas (MOCs) (✅ Completado)

Se han creado las siguientes páginas en `/pages/` para centralizar la información:

| Archivo | Propósito | Contenido Implementado |
| :--- | :--- | :--- |
| `CALAIRE-EA.md` | **MOC Principal** | Visión general, enlaces a fases, hitos, documentos maestros. |
| `CALAIRE-APP.md` | **Aplicativo** | Gestión del desarrollo del software estadístico, repositorio, bugs, features. |
| `Prueba Piloto.md` | **Ejecución** | Coordinación de las 4 rondas de marzo, logística de equipos, cronograma. |
| `Laboratorios.md` | **Base de Datos** | Registro de laboratorios participantes. |
| `QMS.md` | **Calidad** | Integración ISO 17043/13528, listado de documentos F-GCM-03. |
| `Equipo.md` | **Personas** | Directorio del equipo (Carmen Elena, Jeniffer, David Esteban), roles. |
| `templates.md` | **Sistema** | Archivo contenedor para todos los templates de Logseq. |

## Fase 3: Templates (Logseq) (✅ Completado)

Templates disponibles en `pages/templates.md`:

1.  **Reunión** (`template:: reunion`): Estructura para actas con asistentes, decisiones y acciones.
2.  **Protocolo Técnico** (`template:: protocolo`): Estructura para documentación de gases (CO, NOx, SO2, O3).
3.  **Ronda Piloto** (`template:: ronda-piloto`): Seguimiento de logística y resultados por laboratorio/semana.
4.  **Entregable** (`template:: entregable`): Seguimiento de hitos con plazos y criterios de aceptación.
5.  **Journal Diario** (`template:: journal-daily`): Estructura estándar para registros diarios con categorías organizativas.

## Fase 4: Configuración de Queries (✅ Completado)

Se ha actualizado `logseq/config.edn` (`:default-queries`) para visualización automática en el Journal:

1.  **📋 CALAIRE-EA Tasks**: Muestra todos los TODO/DOING/NOW/LATER vinculados a la página `[[CALAIRE-EA]]`.
2.  **🎯 Decisiones Recientes**: Rastrea automáticamente cualquier bloque con el tag `#decision`.
3.  **Default**: Se mantienen las secciones "🔨 NOW" y "📅 NEXT".

## Fase 5: Tareas Inmediatas (Backlog Inicial) (✅ Completado)

Se han poblado las páginas MOC con las tareas urgentes identificadas:

*   **Prueba Piloto**: Reajuste de cartas, confirmación laboratorios, logística equipos.
*   **Aplicativo**: Informe validación, documentación, testing, migración repo.
*   **QMS**: Protocolos (CO, NOx, SO2, O3), manual transporte, portafolio.

## Instrucciones de Uso

1.  **Nueva Tarea**: Crear bloque en Journal -> `TODO Tarea... project:: [[CALAIRE-EA]]`.
2.  **Nueva Reunión**: En Journal -> Escribir `[[Reunión: Tema]]`, entrar a la página y aplicar template `reunion`.
3.  **Ver Progreso**: Ir a la página `[[CALAIRE-EA]]` o revisar la sección inferior del Journal diario.

### Uso del Journal Diario

Para mantener consistencia en los registros diarios, usar el template `journal-daily`:

1.  Ejecutar `/template journal-daily` en el journal del día.
2.  Eliminar secciones que no apliquen (no forzar secciones vacías).
3.  Usar `collapsed:: true` para secciones extensas.

#### Categorías Estándar

| Categoría                | Contenido Típico                                           |
|--------------------------|------------------------------------------------------------|
| **Prueba Piloto**        | Rondas EA, confirmaciones laboratorios, logística equipos   |
| **Gestión Administrativa** | Cartas oficiales, comunicaciones, contratación           |
| **Desarrollo Técnico**   | CALAIRE-APP, protocolos, calibración                      |
| **SGC / Calidad**       | Auditorías, ISO 17043/13528, control documental            |
| **Infraestructura**      | Instalaciones, TI, transporte de equipos                     |

#### Convención para Notas Históricas

- Journals con contenido mínimo (2 líneas o menos): marcar como `- #nota-historica`.
- Journals con cronogramas/diagramas desactualizados: encapsular bajo `#version-historica` y colapsar.
