# Rundown: CALAIRE-EA Commercial Service

**Date**: 2026-07-14

## Current State

- Capa comercial completa y en español: raíz renombrada
  `commercial_service/` → `servicio_comercial/`, subcarpetas y 24 archivos
  traducidos (sin tildes), todo vía `git mv`.
- 4 defectos de revisión corregidos: rutas rotas en registro/README, bloque
  estándar "uso del informe" unificado (CS-01 §9 = CS-08 cl.16 = CS-13 ×2),
  terminología ("cupo", "verificación", "Líder comercial"), estados
  PLANIFICADO → BORRADOR en CS-05–09 y CS-11–15.
- CS-10 v0.3 implementado (xlsx protegido + simulación sintética + generador
  `scripts/build_cs10_tracker.py`).
- CS-01 v0.3 aprobado (Carmen Elena Zapata); puertas financiera/legal/técnica
  abiertas.
- DEF_ptservice_prop.md sin modificar por decisión del usuario: divergencias
  (4 bloques, tarifa plana COP 5.928.000 por organización, analizador
  adicional sin recargo) son decisiones institucionales del 2026-07-14.

## Critical Technical Context

- Índice canónico: `servicio_comercial/00_control/registro_artefactos.md`
  (ubicaciones verificadas contra archivos reales).
- Bloque estándar "uso del informe": cambiarlo exige actualizar CS-01, CS-08 y
  CS-13 (2 instancias) en la misma revisión.
- Nunca publicar COP 5.928.000 hasta que CS-04 pruebe piso de costo directo y
  la Universidad valide impuestos/facturación.
- Contraseña placeholder del tracker: `CAMBIAR-CS10` (cambiar antes de uso
  real). Generador requiere LibreOffice UNO en puerto 2002.
- `logs/history/` y `logs/plans/` conservan rutas viejas a propósito
  (registro histórico).

## Next Steps

1. Commit del renombrado + correcciones (working tree completo).
2. Ejecutar plan de puertas de liberación:
   `logs/plans/260714_1558_plan_commercial-release-gates.md` (costos CS-04,
   evidencia de capacidad 4 / 3+6, aprobaciones institucionales).
3. Completar aprobadores `[RELLENO]` en `registro_cambios_versiones.md` y
   changelogs en línea de CS-01/CS-08/CS-09/CS-13.

## Branch Status

- Branch: main (ahead 1 de origin/main)
- Status: dirty
- Pending changes: renombrado completo `servicio_comercial/` (24 RM staged),
  M en HANDOFF.md, finances_handoff.md, ptservice_art_prop.md, logs/;
  untracked: `servicio_comercial/04_inscripcion_restringida/*.xlsx`,
  `scripts/`, `finances_handoff.md`, `logs/history/260714_*`.
