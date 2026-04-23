# Evolución del Proyecto: calaire-app

**Fecha de corte**: 2026-04-23  
**Periodo cubierto**: 2026-04-21 → 2026-04-22  
**Repositorio**: `/home/w182/w421/calaire-app`  
**Stack**: Next.js 16 + WorkOS (autenticación) + Supabase (base de datos)

---

## Resumen ejecutivo

`calaire-app` es el portal web del programa CALAIRE-EA para la gestión de rondas de ensayos de aptitud. Nació el 21 de abril de 2026 como reemplazo del prototipo abandonado en `calaire-ea/apps/portal-rondas-ea`. En 48 horas alcanzó funcionalidad completa: desde la creación de rondas por el coordinador hasta el cierre formal de resultados por participantes, con identidad visual unificada con pt_app.

---

## Línea de tiempo de hitos

### Día 1 — 2026-04-21: Construcción del portal (7 etapas)

| Hora | Etapa | Hito | Detalle |
|------|-------|------|---------|
| ~16:00 | 1 | Setup base | Next.js 16 + WorkOS + Supabase configurados. Esquema SQL con 4 tablas (`rondas`, `ronda_contaminantes`, `ronda_participantes`, `envios`). |
| ~16:49 | — | Sistema de diseño "Institutional Gold" | Paleta dorada `#FDB913` importada de pt_app. Clases CSS puras: `.card`, `.card-accent`, `.header-bar`, `.btn-primary`, `.btn-outline`, `.numeric`. |
| ~16:51 | — | Flujo de invitación por tokens | Modelo de cupos pendientes en `ronda_participantes` con `workos_user_id = pendiente:<token>`. Reclamación automática al autenticarse. |
| ~17:20 | — | Logo UNAL integrado | Componente `LogoUnal.tsx` con `next/image`, aspect ratio preservado, `priority` para LCP. |
| ~17:33 | 4 | Cierre formal de resultados | `enviarInformeFinalAction()` + `getEstadoEnvioParticipante()`. Bloqueo post-envío con `submitted_at` como sello. |
| ~17:49 | — | Rediseño UI formulario participante | Progress bar dorada, KPI cards, inputs con focus ring dorado, botón primario, pantalla de éxito. |
| ~18:18 | — | Integración local funcional | `.env.local` completo, `db/schema.sql` ejecutado, login via route handler, server actions reestructuradas. |
| ~14:44 | 2 | Dashboard coordinador | Creación de rondas (borrador), configuración por contaminante, transiciones `borrador → activa → cerrada`. Server Components + server actions. |
| ~15:02 | 3 | Gestión de participantes | Búsqueda por correo en WorkOS, asignación a ronda, listado con estado de envío, eliminación condicional. |
| ~15:23 | 6 | Hardening | Validación server-side, rechazo de rondas no activas, usuarios no invitados, valores negativos. Páginas 404 y acceso denegado. |
| ~16:33 | — | Gaps funcionales resueltos | Gap 1: Crear usuarios WorkOS desde la app. Gap 2: Vista participante con sus rondas asignadas. |

### Día 2 — 2026-04-22: Flujos avanzados y autenticación multi-proveedor

| Hora | Hito | Detalle |
|------|------|---------|
| ~02:48 | Fase 1b completada | Configuración admin PT final. |
| ~12:04 | Integración PT App CSV | Plan para exportar CSV compatible con `summary_n13.csv` — contrato de salida definido. |
| ~12:17 | Card de enlace PT App | Card visual en dashboard admin apuntando a `https://w421.shinyapps.io/pt_app/`. |
| ~12:18 | Ajuste logo login | Tamaño `height=44` → `height=64`. |
| ~tarde | Autenticación multi-proveedor | Email OTP (Magic Auth) activado. Eliminado chequeo `role-mismatch`. |
| ~tarde | Panel laboratorio de referencia | `FormularioReferencia.tsx` con badge violeta. Bifurcación por `participant_profile === 'member_special'`. |
| ~tarde | Decisión WorkOS sin organización | `auth.role` siempre null. Perfil de referencia → `participant_profile` en Supabase, no WorkOS. |

---

## Arquitectura técnica

### Stack

| Componente | Tecnología |
|------------|------------|
| Frontend/Backend | Next.js 16 (App Router, Server Components, Server Actions) |
| Autenticación | WorkOS (Email OTP / Magic Auth) |
| Base de datos | Supabase (PostgreSQL) |
| Deploy target | Vercel |
| Identidad visual | CSS vars "Institutional Gold" — unificada con pt_app |

### Modelo de datos (Supabase)

```
rondas (id, codigo, nombre, estado, created_at)
  └── ronda_contaminantes (id, ronda_id, contaminante, niveles, replicas)
  └── ronda_participantes (id, ronda_id, workos_user_id, email, participant_profile, token)
       └── envios (id, ronda_id, workos_user_id, contaminante, nivel, replicas_json, submitted_at)
```

### Rutas principales

| Ruta | Rol | Función |
|------|-----|---------|
| `/login` | Público | Inicio de sesión WorkOS |
| `/dashboard` | Admin | Gestión de rondas, card PT App |
| `/dashboard` | Participante | Vista de rondas asignadas |
| `/dashboard/rondas/[id]/participantes` | Admin | Gestión de participantes por ronda |
| `/dashboard/rondas/[id]/resultados` | Admin | Visualización + exportación CSV |
| `/ronda/[codigo]` | Participante | Formulario de entrada de datos |
| `/ronda/[codigo]` (referencia) | Referencia | `FormularioReferencia.tsx` |

---

## Decisiones de diseño clave

1. **Sin correo automático**: Invitación via enlace manual con tokens pre-generados.
2. **Cierre con `submitted_at`**: Sin tabla adicional de submissions. Marca temporal existente sirve para trazabilidad y bloqueo.
3. **Sin migraciones extra**: Modelo de cupos pendientes reutiliza `ronda_participantes` sin tablas nuevas.
4. **CSS vars > Tailwind para colores**: Paleta siempre por CSS variables, utilidades Tailwind solo para layout/spacing.
5. **WorkOS sin organización**: Roles determinados por `participant_profile` en Supabase, no por WorkOS `auth.role`.

---

## Pendientes

| Item | Prioridad | Estado |
|------|-----------|--------|
| Migración `db/migrate_envios_pt_nuevos_campos.sql` | Alta | No ejecutada en Supabase |
| Smoke test flujo referencia (OTP → token → badge violeta) | Alta | Pendiente |
| Decidir renombrar `member_special` → `referencia` en BD | Media | Pendiente |
| Rotación de secretos (WORKOS_API_KEY, SUPABASE_SERVICE_ROLE_KEY) | Alta | Pendiente |
| Deploy Vercel (Etapa 7) | Alta | Pendiente |
| Exportación CSV compatible pt_app (plan aprobado) | Media | Plan diseñado, no implementado |
