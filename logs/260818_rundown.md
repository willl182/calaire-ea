# Rundown: CALAIRE-EA — Curso incertidumbre v2

**Date**: 2026-08-18

## Current State

- `cursov2/` completo y coherente: M1–M5, M6_taller (cierre obligatorio, 314 min), M7 Monte Carlo opcional. Original `contenido/` intacto.
- Evaluación doble documentada en `evaluacion_propuesta.md`.
- Respuesta comercial lista en `respuesta_solicitud_capacitacion.md` (6 h, virtual 2×3 h, 4 personas); usuario ya la personalizó (saludo a David, sin R, sin pregunta IDEAM).

## Critical Technical Context

- APNA-370 del cliente mide NOₓ — fuera de alcance del curso O₃; alcance adicional a cotizar aparte.
- Vasthi PV-Air 9007: usar su datasheet como caso M4 (sirve de criterio pre-compra).
- Ediciones cursov2 vía `claude-gpt -p` con acceptEdits + allowedTools; bypassPermissions bloqueado.
- Memoria persistente actualizada: `project_cursov2.md`.

## Next Steps

1. Enviar respuesta a David; esperar confirmación de alcance NOₓ y perfil de participantes.
2. Decidir versionado git de `docs/capacitacion_incert/` (todo untracked).

## Branch Status

- Branch: main
- Status: dirty, ahead 1 de origin/main
- Pending changes: `servicio_comercial/*` y otros modificados (sesión previa); `docs/capacitacion_incert/` completo sin rastrear (evaluación, cursov2, respuesta); `logs/` actualizados
