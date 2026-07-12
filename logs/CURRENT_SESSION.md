# Session State: CALAIRE-EA Commercial PT Service

**Last Updated**: 2026-07-12 16:34 -05

## Session Objective

Align the definitive service proposal, commercial artifact blueprint and QMS navigation map with `docs/qms/` as the sole active QMS source of truth.

## Current State

- [x] `DEF_ptservice_prop.md` now defines `docs/qms/` as the controlling QMS directory and establishes document precedence.
- [x] `ptservice_art_prop.md` now references only `docs/qms/` for QMS masters and clearly separates commercial artifacts from technical QMS controls.
- [x] `docs/qms/mapa_navegacion_sgc_pea.html` includes a visible source-of-truth banner, canonical folder paths and the active `EA-<codigo-ronda>` record structure.
- [x] Broken dependencies on archived `fichas_resumen` links were removed from the navigation-map detail panel.
- [x] The navigation map was rendered through the collaborative preview: title/header loaded, source banner displayed and 50 nodes rendered without JavaScript errors.
- [x] Former auxiliary/QMS working trees were reorganized under `docs/z_archivos_para_descartar/` by the user.
- [ ] Create the 15 controlled commercial artifacts defined in `ptservice_art_prop.md`.

## Critical Technical Context

- `docs/qms/` is the only active source of truth for QMS procedures, instructions, master forms, matrices and round evidence.
- Files under `docs/z_archivos_para_descartar/`, historical pilot folders, analyses or duplicate paths are non-controlling unless incorporated by an approved document in `docs/qms/`.
- QMS technical and quality requirements override conflicting proposal or commercial-template text.
- The definitive proposal controls commercial intent; the blueprint controls the commercial-artifact build route.
- Commercial artifacts should cite/link QMS masters rather than copy technical requirements.
- Service rules remain: one/several/all five gases; reference value below 12 valid results and robust consensus at 12 or more; no a1-a7 grade; approximately EUR 1,600 five-gas benchmark.

## Next Steps

1. Create CS-01 using only approved QMS references under `docs/qms/`.
2. Build CS-04 with equipment lifecycle, cylinder-strategy and verified-capacity inputs.
3. Create CS-02 through CS-15 in blueprint order.
4. Update QMS masters through formal change control if commercial implementation reveals a conflict.
