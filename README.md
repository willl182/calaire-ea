# CALAIRE-EA Project Management

Este repositorio contiene el sistema de gestión del conocimiento y seguimiento del proyecto **CALAIRE-EA (Proyecto 61134)**: *Implementación de Ensayos de Aptitud para Gases Contaminantes Criterio*.

El sistema está construido sobre **Logseq**, utilizando una estructura de grafo para conectar tareas, documentos, reuniones y conocimientos técnicos.

## Estructura del Repositorio

*   **`journals/`**: Entradas diarias (bitácora de trabajo).
*   **`pages/`**: Notas permanentes, MOCs (Maps of Content) y gestión de conocimiento.
*   **`docs/`**: Documentación externa, referencias estáticas y archivos de soporte.
*   **`ref/`**: Referencias sobre el uso del sistema (incluyendo guía de Logseq y setup).
*   **`logseq/`**: Configuración del grafo (queries, custom.css, config.edn).

## Convenciones

*   **Idioma**:
    *   Contenido: Español.
    *   Propiedades/Tags estructurales: Inglés (e.g., `priority::`, `deadline::`, `type::`).
*   **Flujo de Trabajo**: `TODO` -> `DOING` -> `DONE`.

## MOCs Principales (Puntos de Entrada)

*   `[[CALAIRE-EA]]`: Visión general del proyecto.
*   `[[Prueba Piloto]]`: Coordinación operativa.
*   `[[CALAIRE-APP]]`: Desarrollo de software.
*   `[[QMS]]`: Gestión de calidad y normas ISO.

## Setup

Ver `ref/setup.md` para detalles sobre la configuración e implementación de este grafo.
