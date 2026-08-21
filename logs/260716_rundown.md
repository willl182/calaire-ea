# Rundown: CALAIRE-EA Commercial Service

**Date**: 2026-07-16

## Current State

- `main` contiene la localización comercial y la eliminación del paquete de
  patrocinio/referencias a1–a7; está un commit por delante de `origin/main`.
- Hay 26 archivos rastreados modificados, incluidos documentos comerciales, el
  generador CS-10 y dos libros XLSX.
- Hay entregables DOCX, 15 fichas más índice, una presentación comercial, 16
  XLS de datos de temperatura y scripts/temporales sin seguimiento.
- Las puertas económica, técnica, financiera, jurídica y de despliegue siguen
  abiertas.

## Critical Technical Context

- No publicar precio ni fecha antes de cerrar
  `logs/plans/260714_1558_plan_commercial-release-gates.md`.
- Capacidad vigente: 4 analizadores por bloque; CO/SO₂ limitado a 3
  organizaciones y 6 analizadores totales.
- La clave placeholder CS-10 es `CAMBIAR-CS10`; debe rotarse antes del uso real.
- No versionar el lock `.~lock.CS-02_catalogo.docx#` ni `scripts/__pycache__/`.
- Los demás archivos sin seguimiento requieren clasificación explícita; no
  asumir que son descartables.

## Next Steps

1. Revisar el diff de los 26 archivos modificados y validar los generadores.
2. Validar y clasificar fichas, DOCX, presentación, XLS de temperatura y
   material de prueba antes de preparar commits.
3. Ejecutar las fases pendientes del plan de puertas de liberación.

## Branch Status

- Branch: `main` (ahead 1 de `origin/main`)
- Status: dirty, sin conflictos reportados
- Pending changes: 26 archivos rastreados modificados; entregables DOCX/HTML/MD,
  fichas, datos XLS, scripts y temporales sin seguimiento
