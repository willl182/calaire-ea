# Rundown: CALAIRE-EA Commercial Service

**Date**: 2026-07-14

## Current State

- CS-01 v0.3 proposal decisions are approved; release gates remain pending.
- Four commercial blocks: CO, SO₂, O₃ and NO/NO₂.
- Flat indicative proposal fee: COP 5,928,000 before taxes per organization for
  one to four blocks.
- Commercial artifacts, blueprint and QMS complaint/appeal interfaces were
  aligned with the approved proposal decisions.
- `git diff --check` passes.

## Critical Technical Context

- The fee is not approved for publication and must not fall below direct cost.
- Billing is COP only; University policies control taxes, payment and refunds.
- Capacity limits remain provisional: 4 analyzers per individual block; for
  simultaneous CO/SO₂, 3 organizations and 6 analyzers total.
- Existing gas strategy uses a CO/SO₂/NOx multicomponent cylinder, subject to
  certificate validation; O₃ is generated photometrically.

## Next Steps

1. Complete CS-04 with real cost and lifecycle evidence.
2. Validate physical capacity and the cylinder certificate.
3. Obtain finance/tax and legal approvals.
4. Build CS-10 in protected institutional Excel and run a synthetic simulation.

## Branch Status

- Branch: main
- Status: dirty before commit; no visible ahead/behind difference from origin/main
- Pending changes: commercial artifacts, QMS complaint/appeal procedures,
  blueprint, handoff and session logs
