# Session State: CALAIRE-EA — Curso incertidumbre v2 + propuesta capacitación

**Last Updated**: 2026-08-18 07:23

## Session Objective

Evaluar complejidad del curso de incertidumbre O₃, crear versión adaptada (cursov2) para operadores de red, y redactar respuesta a solicitud comercial de capacitación (acreditación IDEAM).

## Current State

- [x] Evaluación doble (Opus 5 + claude-gpt): veredicto "demasiado técnico para no expertos"; guardada en `docs/capacitacion_incert/evaluacion_propuesta.md`
- [x] Clon `docs/capacitacion_incert/cursov2/` (target: operadores de red; O₃ mantenido, SIN agnosticismo)
- [x] M7 simplificado (1 nivel 100 nmol/mol, k=2 fijo, W–S opcional, presupuesto medio resuelto)
- [x] M3 reenfocado (solo conceptos usados aguas abajo; autocorrelación/arcoseno/trapezoidal/covarianza remitidos a handout)
- [x] Monte Carlo reordenado: taller ahora `M6_taller.md` (cierra obligatorio, SOL_M6); Monte Carlo ahora `M7_opcional_monte_carlo.md` (último, opcional). Cronograma: 314 min obligatorios en jornada 6 h. HTML y xlsx regenerados.
- [x] Respuesta comercial `docs/capacitacion_incert/respuesta_solicitud_capacitacion.md`: 6 h (no 8), virtual 2×3 h, Vasthi como caso en M4. Usuario la editó a mano (saludo a David, quitó pregunta IDEAM, quitó referencias a R en entregables/plantillas).
- [ ] Enviar respuesta a David / esperar confirmación del cliente (alcance NOₓ, nivel matemático participantes)
- [ ] `docs/capacitacion_incert/` completo sigue SIN rastrear en git

## Critical Technical Context

- M2 y original `contenido/` intactos — NO tocar `contenido/`; cursov2 es la rama de trabajo.
- Cliente: patrones Thermo 49i + Sabio 2030 (ya caso en material) + compra proyectada Vasthi PV-Air 9007; analizadores Horiba APOA-370 (O₃) y APNA-370 (**NOₓ — fuera de alcance**, cotizar aparte).
- Ediciones de cursov2 hechas vía CLI `claude-gpt -p` con `--permission-mode acceptEdits` + `--allowedTools`; bypassPermissions bloqueado.
- Usuario prefiere hoja de cálculo sobre R en material de cara al cliente (edición manual de la respuesta).

## Next Steps

1. Decidir si versionar `docs/capacitacion_incert/` (add + commit) — todo untracked.
2. Al responder cliente: confirmar alcance NOₓ y nivel matemático antes de propuesta final.
