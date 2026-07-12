# Evolución General del Proyecto CALAIRE-EA

**Fecha de corte**: 2026-04-23  
**Periodo cubierto**: 2026-02-03 → 2026-04-22 (≈11 semanas)  
**Autor**: Generado automáticamente a partir de los logs de sesión de cada repositorio

---

## 1. Visión del ecosistema

El proyecto CALAIRE-EA opera como un ecosistema de tres componentes interconectados:

```
┌──────────────────────────────────────────────────────────┐
│                    CALAIRE-EA (Hub)                       │
│  Logseq + Git — Planificación, SGC, Documentación        │
│  ISO 17043:2023 / ISO 13528:2022                         │
├──────────────────────┬───────────────────────────────────┤
│   pt_app + ptcalc    │         calaire-app               │
│   R/Shiny            │         Next.js 16                │
│   Motor estadístico  │         Portal de rondas          │
│   Validación ISO     │         WorkOS + Supabase         │
│   → shinyapps.io     │         → Vercel                  │
└──────────────────────┴───────────────────────────────────┘
          ↕ CSV (summary_n13.csv contrato) ↕
```

**Identidad visual unificada**: ambas aplicaciones comparten la paleta "Institutional Gold" (`#FDB913`), tipografía DM Sans + JetBrains Mono, y el logo UNAL como elemento de marca.

---

## 2. Cronología consolidada de avances significativos

### Febrero 2026 — Fundamentos

| Semana | Área | Avance |
|--------|------|--------|
| S1 (Feb 3) | calaire-ea | **Fundación del repositorio**: Logseq + Git, arquitectura MOC, publicación GitHub, sistema de journals estandarizado, clasificación de correos. |
| S1 (Feb 5) | pt_app | **Primera auditoría estadística**: verificación de cálculos CO 0-μmol/mol contra Excel de auditoría. Discrepancia de σ_pt identificada (0.00579 vs 0.03982). |

### Marzo 2026 — Correcciones y validación

| Semana | Área | Avance |
|--------|------|--------|
| S5 (Mar 10) | pt_app | **9 correcciones estadísticas (H1–H9)**: fórmula B.10, MADe separado, umbral Algoritmo A (n≥12), trazabilidad por `run`. Ramas paralelas opus/codex. |
| S5 (Mar 11) | pt_app | **Plan de validación cruzada A2**: 15 combinaciones, validación tripartita (APP / R independiente / Python). |
| S8 (Mar 30) | pt_app | **Pipeline de validación tripartita POC**: 5 workbooks Excel, Python sin dependencias, 4446 FAILs iniciales por tolerancia numérica. |
| S8 (Mar 31) | pt_app | **Fases downstream completadas**: Homogeneidad → Estabilidad → Incertidumbres → Puntajes z/z'/ζ/En. Toda la cadena validada. |

### Abril 2026 — SGC, auditorías y aplicación web

| Semana | Área | Avance |
|--------|------|--------|
| S10 (Abr 7) | calaire-ea | **Framework SGC completo**: 4 niveles documentales, segregación operativa/gestión, plan de rondas piloto (simple + compleja). |
| S10 (Abr 8) | calaire-ea | **Sprint 2 SGC completado**: I-PSEA-09, I-PSEA-10, P-PSEA-10 creados. Brechas de I-PSEA-09 identificadas (σ_pt, proceso apelaciones). |
| S10 (Abr 10) | calaire-ea | **F-PSEA-06 ronda simple**: 4 fases de ajuste completadas. Formato operativo con controles pre-ronda, depuración de placeholders, decisión σ_pt post-ronda. |
| S10 (Abr 10) | calaire-ea | **4 auditorías cruzadas de F-PSEA-06**: completitud estructural, placeholders, coherencia interdocumental y línea base pre-corrección. Dictamen: operable pero `no_aprobable` por inconsistencia σ_pt. |
| S11 (Abr 20) | calaire-ea | **Inducción SST**: flujo operativo para acceso a UNAL documentado. |
| S11 (Abr 20) | pt_app | **Cifras significativas ISO**: plan aprobado, convergencia Algoritmo A actualizada, formateo numérico reconfigurado. |
| S12 (Abr 21) | calaire-app | **Portal web creado desde cero**: 6 etapas en un día — setup, dashboard, participantes, formulario, resultados, hardening. |
| S12 (Abr 21) | calaire-app | **Rediseño "Institutional Gold"**: identidad visual unificada con pt_app. |
| S12 (Abr 21) | calaire-app | **Invitación por tokens manuales**: modelo sin correo automático, cupos reclamables. |
| S12 (Abr 21) | calaire-app | **Cierre formal de resultados**: bloqueo post-envío con `submitted_at`. |
| S12 (Abr 22) | pt_app | **Deprecación sample_group**: columna eliminada del contrato, ptcalc v0.1.1, documentación actualizada. |
| S12 (Abr 22) | calaire-app | **Autenticación multi-proveedor**: Email OTP para universidades con Azure AD bloqueado. Panel de laboratorio de referencia. |

---

## 3. Estado actual por componente

### calaire-ea (Hub documental / SGC)

| Dimensión | Estado | Madurez |
|-----------|--------|---------|
| Grafo Logseq | Operativo, journals estandarizados, MOCs definidos | 🟢 Estable |
| SGC ISO 17043 | 23 formatos F-PSEA creados (skeletons), 3 procedimientos, 14 instructivos | 🟡 En desarrollo |
| F-PSEA-06 (Plan de ronda) | Auditado × 4, operable, no aprobado formalmente | 🟡 Requiere correcciones |
| Comunicaciones participantes | 3 cartas institucionales + 3 comunicaciones detalladas | 🟢 Listas |
| Acceso operativo UNAL | Inducción SST documentada, flujo de permisos definido | 🟢 Listo |

### pt_app + ptcalc (Motor estadístico)

| Dimensión | Estado | Madurez |
|-----------|--------|---------|
| Algoritmo A | Corregido (max(0,...)), umbral n≥12, convergencia 1e-04 | 🟢 Estable |
| Cadena downstream | Homogeneidad → Estabilidad → Incertidumbres → Puntajes | 🟢 Completa |
| Validación tripartita | Pipeline implementado (APP/R/Python), workbooks generados | 🟡 FAILs de tolerancia pendientes |
| Cifras significativas | Plan aprobado, fases 1-4 implementadas, fases 5-6 pendientes | 🟡 Incompleto |
| Contrato de datos | `sample_group` deprecado, contrato limpio de 7 columnas | 🟢 Estable |
| Tests | 3 FAILs pre-existentes conocidos (bugs en tests, no en código) | 🟡 Pendiente |
| ptcalc v0.1.1 | Funciones core operativas, sin testthat propio, `devtools::document()` pendiente | 🟡 Requiere pulido |

### calaire-app (Portal web)

| Dimensión | Estado | Madurez |
|-----------|--------|---------|
| Autenticación | WorkOS Email OTP, multi-proveedor resuelto | 🟢 Operativo |
| Dashboard coordinador | Rondas CRUD + transiciones de estado + contaminantes | 🟢 Completo |
| Gestión participantes | Búsqueda, invitación por token, creación de usuarios WorkOS | 🟢 Completo |
| Formulario participante | Auto-save (debounce 1500ms), cierre formal, modo solo lectura | 🟢 Completo |
| Panel referencia | `FormularioReferencia.tsx` con badge violeta, separado del regular | 🟢 Completo |
| Resultados + CSV | Visualización admin + exportación CSV | 🟢 Completo |
| Identidad visual | "Institutional Gold" unificado con pt_app | 🟢 Completo |
| Deploy Vercel | **No ejecutado** | 🔴 Pendiente |
| Migración BD pendiente | `migrate_envios_pt_nuevos_campos.sql` | 🔴 Pendiente |
| Rotación secretos | API keys expuestas en chat anterior | 🔴 Urgente |

---

## 4. Integración entre componentes

### Flujo de datos: calaire-app → pt_app

```
Participante ingresa datos (calaire-app)
  → envios (Supabase)
  → Exportación CSV (admin dashboard)
  → Archivo compatible summary_n13.csv
  → pt_app procesa estadísticas ISO 13528
  → Informe de resultados
```

**Estado**: Plan de integración diseñado (`260421_1946_plan_integracion-pt-app-csv.md`), contrato de salida definido (7 columnas), **implementación pendiente**.

### Flujo documental: calaire-ea ↔ ambas apps

- F-PSEA-06 (Plan de ronda) alimenta la configuración de rondas en calaire-app
- I-PSEA-07 (Diseño Estadístico) define los parámetros de ptcalc
- Los resultados de pt_app alimentarían F-PSEA-14 (Cálculo y Aprobación Estadística)
- Las comunicaciones a participantes (calaire-ea) guían el flujo de invitación de calaire-app

---

## 5. Métricas de progreso

| Métrica | Valor |
|---------|-------|
| Archivos de log history (calaire-ea) | 36 |
| Archivos de log history (pt_app) | 24 |
| Archivos de log history (calaire-app) | 19 |
| Planes formalizados (calaire-ea) | 10 |
| Planes formalizados (pt_app) | 10+ |
| Planes formalizados (calaire-app) | 2 |
| Formatos SGC creados | 23 (F-PSEA-01 a F-PSEA-23) |
| Instructivos creados | 14 (I-PSEA-02 a I-PSEA-15) |
| Procedimientos creados | 4 (P-PSEA-01, 10, 20, 22) |
| Auditorías cruzadas ejecutadas | 4 (sobre F-PSEA-06) |
| Correcciones estadísticas aplicadas | 9 (H1–H9) |
| Pipeline de validación tripartita | 1 (APP/R/Python, 15 combos, 5 workbooks) |

---

## 6. Riesgos y pendientes críticos

### 🔴 Alta prioridad

1. **Rotación de secretos**: `WORKOS_API_KEY` y `SUPABASE_SERVICE_ROLE_KEY` expuestos en chat — requieren rotación inmediata.
2. **Migración SQL pendiente**: `db/migrate_envios_pt_nuevos_campos.sql` no ejecutada en producción.
3. **Deploy Vercel**: calaire-app funcional en local pero sin despliegue en producción.

### 🟡 Media prioridad

4. **Aprobación formal F-PSEA-06**: Backlog C4-01 a C4-04 (alineación σ_pt interdocumental, hito T-3).
5. **Cifras significativas pt_app**: Fases 5-6 (tests + validación cruzada) pendientes.
6. **Exportación CSV calaire-app → pt_app**: Plan diseñado, implementación no iniciada.
7. **ptcalc sin testthat**: Paquete v0.1.1 sin suite de tests propia; depende de tests de integración.
8. **3 FAILs en tests pt_app**: Bugs en tests (no en código), pero dejan el smoke test sucio.

### 🟢 Para planificar

9. **Ronda compleja (n≥2)**: Documentación de Fase 2 existe pero sin implementación operativa.
10. **I-PSEA-07 skeleton**: Secciones críticas por completar con parámetros por analito.
11. **Renombrar `member_special` → `referencia`**: Decisión pendiente (requiere migración SQL).

---

## 7. Documentos de detalle

Los documentos de evolución por componente están en:

| Componente | Archivo |
|------------|---------|
| calaire-ea | [`260423_evolucion_calaire-ea.md`](file:///home/w182/w421/calaire-ea/logs/history/260423_evolucion_calaire-ea.md) |
| pt_app + ptcalc | [`260423_evolucion_pt-app.md`](file:///home/w182/w421/pt_app/logs/history/260423_evolucion_pt-app.md) |
| calaire-app | [`260423_evolucion_calaire-app.md`](file:///home/w182/w421/calaire-app/logs/history/260423_evolucion_calaire-app.md) |

---

*Este documento es un snapshot al 2026-04-23. Debe actualizarse al cierre de cada sprint o hito significativo.*
