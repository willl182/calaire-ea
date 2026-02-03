# Plan de Implementación - Proyecto CALAIRE-EA (Logseq Setup)

Este documento describe la configuración y estructura del grafo de Logseq para la gestión del proyecto 61134 (CALAIRE-EA).

## Fase 1: Inicialización Git

1.  **Inicializar repositorio**: `git init`
2.  **Configurar `.gitignore`**:
    *   `.DS_Store`
    *   `bak/`
    *   `pages-metadata.edn`
    *   `logseq/graphs-txid.edn`
    *   `logseq/.recycle/`
3.  **Commit inicial**: Guardar estado actual.

## Fase 2: Estructura de Páginas (MOCs)

Crear las siguientes páginas en `/pages/` para centralizar la información:

| Archivo | Propósito | Contenido Clave |
| :--- | :--- | :--- |
| `CALAIRE-EA.md` | **MOC Principal** | Visión general, enlaces a fases, hitos, documentos maestros. |
| `CALAIRE-APP.md` | **Aplicativo** | Gestión del desarrollo del software estadístico, repositorio, bugs, features. |
| `Prueba Piloto.md` | **Ejecución** | Coordinación de las 4 rondas de marzo, logística de equipos, cronograma. |
| `Laboratorios.md` | **Base de Datos** | Registro de laboratorios participantes, contactos, estado de participación. |
| `QMS.md` | **Calidad** | Integración ISO 17043/13528, listado de documentos F-GCM-03, auditorías. |
| `Equipo.md` | **Personas** | Directorio del equipo (Carmen Elena, Jeniffer, David Esteban), roles y responsabilidades. |
| `templates.md` | **Sistema** | Archivo contenedor para todos los templates de Logseq. |

## Fase 3: Templates (Logseq)

Implementar los siguientes templates en `pages/templates.md` usando propiedades en inglés y contenido en español (convención mixta):

### 1. Reunión
```markdown
- #[[Reunión Template]]
  template:: reunion
  - type:: [[Meeting]]
  - attendees:: 
  - project:: [[CALAIRE-EA]]
  - date:: 
  - **Temas Discutidos**
    - 
  - **Decisiones**
    - #decision 
  - **Acciones**
    - TODO 
```

### 2. Protocolo Técnico
```markdown
- #[[Protocolo Template]]
  template:: protocolo
  - type:: [[Protocolo]]
  - gas:: 
  - version:: 1.0
  - status:: #borrador
  - **Objetivo**
    - 
  - **Procedimiento**
    - 
  - **Criterios de Aceptación**
    - 
```

### 3. Ronda Piloto
```markdown
- #[[Ronda Piloto Template]]
  template:: ronda-piloto
  - type:: [[Ronda Piloto]]
  - laboratorio:: 
  - week:: 
  - reception-date:: 
  - return-date:: 
  - **Equipos**
    - 
  - **Resultados**
    - CO:: 
    - NOx:: 
    - SO2:: 
    - O3:: 
  - **Observaciones**
    - 
```

## Fase 4: Configuración de Queries

Agregar las siguientes queries a `logseq/config.edn` (`:default-queries`) para visualización rápida en el Journal:

1.  **Tareas CALAIRE-EA**: Muestra todos los TODO/DOING relacionados con el proyecto.
2.  **Decisiones Recientes**: Rastrea bloques con tag `#decision`.

## Fase 5: Tareas Inmediatas (Backlog Inicial)

Poblar las páginas MOC con las tareas urgentes identificadas:

*   **Prueba Piloto**: Reajuste de cartas, confirmación laboratorios, logística equipos.
*   **Aplicativo**: Informe validación, documentación, testing, migración repo.
*   **QMS**: Protocolos (CO, NOx, SO2, O3), manual transporte, portafolio.
