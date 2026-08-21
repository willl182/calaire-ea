# Rundown: CALAIRE-EA — Presentación Intercambio Técnico INM

**Date**: 2026-08-11

## Current State

- Presentación IT INM (12 ago 2026 9:00) lista: `docs/informes/presentacion_it_inm.md` + `.pptx` compilado.
- Plan de la presentación en `docs/informes/plan_presentacion_it_inm.md`.
- Correcciones aplicadas: pt_app = estadístico / calaire-app = gestión (calaire-app2); apps entregados pendientes de prueba en última ronda; informe de rondas R1 y R2 = `informe_operativo_prueba_piloto_v3-1.md`, emitido.

## Critical Technical Context

- Recompilar: `cd docs/informes && pandoc presentacion_it_inm.md -o presentacion_it_inm.pptx --slide-level=2`.
- T700U dañado: en garantía, proveedor en pruebas, prórroga gestionada — dificultad principal en slides.
- Memoria persistente nueva: `project_aplicativos.md` (mapeo apps).

## Next Steps

1. Ensayar presentación contra agenda INM; confirmar fecha finalización y Ronda C.
2. Opcional: plantilla institucional con `--reference-doc`.

## Branch Status

- Branch: main
- Status: dirty, ahead 1 de origin/main
- Pending changes: servicio_comercial/* (sesión anterior), logs/, docs/informes/presentacion_it_inm.{md,pptx}, plan_presentacion_it_inm.md, nuevos docs/ sin trackear
