# Session State: CALAIRE-EA Commercial Service

**Last Updated**: 2026-07-14 16:56 -05

## Session Objective

Revisar `DEF_ptservice_prop.md` + `ptservice_art_prop.md` contra la
implementación en `servicio_comercial/`, corregir los defectos hallados y
traducir al español todos los nombres de archivos y carpetas de la capa
comercial.

## Current State

- [x] Revisión completa blueprint vs implementación: los 15 artefactos CS
  existen y cumplen las reglas duras (sin claim de acreditación, sin a1–a7,
  regla <12/≥12, benchmark nunca de cara al cliente, capacidad 4 / 3+6).
- [x] 4 hallazgos corregidos: rutas rotas por traducción automática en
  registro/README; bloque estándar "uso del informe" unificado (texto idéntico
  en CS-01 §9, CS-08 cláusula 16, CS-13 ×2); terminología corregida
  ("cupo" no "taza", "verificación" no "cheque", "Líder comercial" no
  "Plomo comercial"); estados PLANIFICADO → BORRADOR en artefactos con
  contenido redactado (CS-05–09, CS-11–15).
- [x] Renombrado completo a español (sin tildes): raíz `commercial_service/` →
  `servicio_comercial/`, subcarpetas (`01_mercado/`, `02_precios_restringidos/`,
  `03_ventas_contratacion/`, `04_inscripcion_restringida/`,
  `05_cambios_finanzas/`, `06_entrega_retencion/`) y los 24 archivos
  (ej. `CS-01_decisiones_comerciales.md`, `registro_artefactos.md`,
  `CS-10_seguimiento_inscripciones_ingresos.xlsx`). Todo con `git mv`.
- [x] Referencias actualizadas en: artefactos internos, README,
  `ptservice_art_prop.md` (árbol §22), `scripts/build_cs10_tracker.py`,
  `HANDOFF.md`, `finances_handoff.md`. `logs/history/` y `logs/plans/`
  intactos (registro histórico).
- [x] Trazabilidad: filas correctivas en `registro_cambios_versiones.md`;
  entradas 0.3.1 (CS-01) y 0.2.1 (CS-08, CS-09, CS-13) en changelogs en línea.
- [ ] Divergencias DEF vs modelo implementado (4 bloques, tarifa plana por
  organización, analizador adicional sin recargo) — decididas por el usuario;
  DEF queda sin modificar por decisión expresa.
- [ ] Puertas de liberación siguen abiertas: costos reales CS-04, evidencia de
  capacidad, aprobación financiera/legal institucional, despliegue CS-10.

## Critical Technical Context

- Nombres canónicos ahora en español sin tildes; NO reintroducir nombres en
  inglés al citar artefactos. Índice canónico:
  `servicio_comercial/00_control/registro_artefactos.md`.
- Bloque estándar "uso del informe": una sola redacción vigente en CS-01 §9,
  CS-08 cláusula 16 y CS-13 (2 instancias). Cambiarlo exige actualizar los 4
  puntos en la misma revisión.
- `scripts/build_cs10_tracker.py` regenera los xlsx (LibreOffice UNO, puerto
  2002); contraseña placeholder `CAMBIAR-CS10` debe cambiarse antes de uso
  real.
- Nunca publicar COP 5.928.000 hasta que CS-04 pruebe piso de costo directo y
  la Universidad valide impuestos y facturación.
- DEF_ptservice_prop.md NO se toca: divergencias comerciales son decisión del
  usuario, sin control de cambios adicional solicitado.

## Next Steps

1. Commit de renombrado + correcciones (todo staged/tracked vía git mv).
2. Continuar plan de puertas de liberación:
   `logs/plans/260714_1558_plan_commercial-release-gates.md` (costos CS-04,
   evidencia de capacidad, aprobaciones institucionales).
3. Completar aprobadores `[RELLENO]` en filas correctivas de
   `registro_cambios_versiones.md` y changelogs en línea.
