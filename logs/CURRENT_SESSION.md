# Session State: CALAIRE-EA Ajuste Comunicación Detallada EA

**Last Updated**: 2026-02-08 17:05

## Session Objective

Planificar y ejecutar el ajuste de la Comunicación Detallada del Ensayo de Aptitud (M.LCAFMi-## Comunicacion Detallada EAdocx.md) para cerrar 4 brechas identificadas frente a ISO/IEC 17043:2023 y mejores prácticas internacionales.

## Current State

- [x] Fase 1 completada: Consolidación de Análisis Preliminares
  - Matriz de 4 brechas priorizadas creada
  - Hallazgo crítico: Seguridad Industrial (sin sección de normas)
  - Hallazgos de alta prioridad: Definición σpt, Quejas y Apelaciones
  - Hallazgo de media prioridad: Declaración Subcontratación

- [x] Fase 2 completada: Mapeo de Comunicación Actual
   - Estructura actual documentada (8 secciones con duplicidad en Sección 8)
   - Ubicación propuesta para cada mejora:
     * Seguridad Industrial: Sección 9 (antes de DECLARACIÓN)
     * Definición σpt: Ampliar Sección 7 (línea 122-124)
     * Quejas y Apelaciones: Sección 10 (después de DECLARACIÓN)
     * Subcontratación: Ampliar Sección 8 (línea 140-141)
   - Estructura final propuesta: 11 secciones

- [x] Fase 3 completada: Extracción de Modelos de Referencia (PDFs)
   - Extraído sección Safety de JRC-ERLAP (11.5)
   - Extraído Quejas/Apelaciones de UBA
   - Extraído Criterio de desempeño σpt de UBA (parcial)
   - Extraído Horn procedure de Brno (PTPP_ZK 2023/1)
   - Extraído Subcontratación de UCLSB
   - Revisado con revisor-fase: hallazgos incorporados
   - Entregable: `logs/plans/260208_1701_fase3_modelos_referencia.md`

- [ ] Fase 4: Redacción de Mejoras

- [ ] Fase 5: Implementación

## Critical Technical Context

- El documento base es de Logseq knowledge graph, NO código. No hay build commands.
- El archivo de comunicación tiene imágenes embebidas en base64 (image1, image2) que deben preservarse.
- Hay duplicidad de numeración en Sección 8 (Confidencialidad y Declaración) que debe corregirse en Fase 5.
- Las referencias a documentos adjuntos (F-PSEA-01, F-PSEA-02, I-PSEA-01) son URLs de Google Docs que deben mantenerse.
- Se usa subagente `revisor-fase` para validar cada fase antes de proceder.

## Files Created

1. `logs/plans/260208_1635_plan_ajuste-comunicacion-detallada-ea.md` - Plan principal con 5 fases
2. `logs/plans/260208_1635_fase1_matriz_hallazgos.md` - Matriz de hallazgos consolidados
3. `logs/plans/260208_1635_fase2_mapa_estructura.md` - Mapa de estructura y ubicación de mejoras
4. `logs/plans/260208_1701_fase3_modelos_referencia.md` - Modelos extraídos de 4 PDFs

## Next Steps

1. Iniciar Fase 4: Redactar mejoras basado en modelos extraídos
2. Revisar σpt pendiente: consultar `docs/iso 13528_2022.md` para definición formal
3. Redactar 4 borradores lineados (Safety, σpt, Quejas/Apelaciones, Subcontratación)
4. Revisar Fase 4 con revisor-fase
5. Actualizar plan con log de ejecución
6. Commit git de cambios de la sesión
