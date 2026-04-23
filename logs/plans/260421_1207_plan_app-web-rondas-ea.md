# Plan: Aplicativo Web Rondas EA (v2)

**Created**: 2026-04-21 12:07
**Updated**: 2026-04-21 15:23
**Status**: completed
**Slug**: app-web-rondas-ea

## Objetivo

Construir una aplicación web real para gestión de rondas de Ensayos de Aptitud (EA), con autenticación WorkOS, base de datos Supabase y formularios reactivos generados por configuración de ronda. Reemplaza el prototipo estático con localStorage (`formulario_codex`) en el largo plazo.

## Stack

| Componente | Tecnología |
|---|---|
| Frontend + API | Next.js 16.2.4 (App Router, TypeScript) |
| Auth | WorkOS AuthKit (magic link, roles admin/participante) |
| Base de datos | Supabase (PostgreSQL + RLS) |
| UI | Tailwind CSS + componentes propios |
| Deploy | Vercel (frontend) + Supabase cloud |

## Modelo de datos

```
rondas
  id, codigo, nombre, estado (borrador|activa|cerrada), created_at

ronda_contaminantes
  id, ronda_id, contaminante (CO|SO2|O3|NO|NO2), niveles (int), replicas (2|3)

ronda_participantes
  id, ronda_id, workos_user_id, invitado_at

envios
  id, ronda_id, workos_user_id, contaminante, nivel (int),
  valores (float[]), promedio (float), incertidumbre (float),
  submitted_at, updated_at
  UNIQUE (ronda_id, workos_user_id, contaminante, nivel)
```

## Reglas de acceso

| Rol | Acceso |
|---|---|
| `admin` | Todas las rondas, todos los envíos, gestión completa |
| `participante` | Solo rondas donde aparece en `ronda_participantes` con estado `activa` |

## Fases

### Etapa 1: Setup base

| # | Tarea |
|---|---|
| 1.1 | Inicializar repo Next.js 16 con App Router + TypeScript |
| 1.2 | Configurar Tailwind + shadcn/ui |
| 1.3 | Integrar WorkOS AuthKit (middleware de sesión, login/logout) |
| 1.4 | Definir roles en WorkOS: `admin`, `participante` |
| 1.5 | Crear schema Supabase con las 4 tablas + RLS |
| 1.6 | Documentar `.env.example` |

**Entregable:** login funcional con roles distinguibles y tablas creadas.

### Etapa 2: Dashboard coordinador

| # | Tarea |
|---|---|
| 2.1 | Página `/dashboard` — lista de rondas con estado |
| 2.2 | Crear ronda: nombre, código único, selección de contaminantes |
| 2.3 | Config por contaminante: niveles (int) + réplicas (2|3) |
| 2.4 | Editar config mientras estado = `borrador` |
| 2.5 | Transiciones de estado: borrador→activa / activa→cerrada |

**Entregable:** coordinador puede crear y publicar rondas completas.

### Etapa 3: Gestión de participantes

| # | Tarea |
|---|---|
| 3.1 | Vista `/dashboard/rondas/[id]/participantes` |
| 3.2 | Buscar usuario por correo (consulta WorkOS) |
| 3.3 | Invitar usuario a la ronda |
| 3.4 | Listar participantes con estado de envío (pendiente/enviado) |
| 3.5 | Eliminar participante (solo si ronda no está cerrada) |

**Entregable:** coordinador gestiona lista de labs por ronda individualmente.

### Etapa 4: Formulario del participante

| # | Tarea |
|---|---|
| 4.1 | Página `/ronda/[codigo]` — acceso restringido por sesión + invitación |
| 4.2 | Generar formulario dinámico desde `ronda_contaminantes` |
| 4.3 | Por nivel: `n` campos de réplica + campo de incertidumbre |
| 4.4 | Cálculo de promedio automático y reactivo (al escribir) |
| 4.5 | Guardado automático (debounce) + botón de envío final |
| 4.6 | Indicador de progreso (contaminantes/niveles completados) |
| 4.7 | Bloqueo del formulario si ronda = `cerrada` |

**Entregable:** participante ingresa y envía datos completos.

### Etapa 5: Vista de resultados

| # | Tarea |
|---|---|
| 5.1 | Vista `/dashboard/rondas/[id]/resultados` |
| 5.2 | Tabla participante × contaminante × nivel |
| 5.3 | Indicadores de completitud por participante |
| 5.4 | Exportar CSV compatible con `ptcalc` / app R ISO 13528 |
| 5.5 | Filtros por contaminante y por participante |

**Entregable:** coordinador descarga datos listos para análisis.

### Etapa 6: Polish y deploy

| # | Tarea |
|---|---|
| 6.1 | Validaciones de formulario (rangos, campos requeridos) |
| 6.2 | Manejo de errores (sesión expirada, acceso denegado, ronda no encontrada) |
| 6.3 | Páginas 404 y acceso denegado con mensajes claros |
| 6.4 | Responsive (funcional en tablet) |
| 6.5 | Deploy Vercel + Supabase cloud |
| 6.6 | Smoke test completo del flujo end-to-end |

**Entregable:** aplicativo en producción con URL compartible.

## Dependencias entre etapas

```
Etapa 1 → Etapa 2 → Etapa 3
                  ↘
                   Etapa 4 → Etapa 5 → Etapa 6
```

## Log de Ejecución

- [x] Etapa 1 iniciada — 2026-04-21
- [x] Etapa 1 completada — 2026-04-21
- [x] Etapa 2 iniciada — 2026-04-21
- [x] Etapa 2 completada — 2026-04-21
- [x] Etapa 3 iniciada — 2026-04-21
- [x] Etapa 3 completada — 2026-04-21
- [x] Etapa 4 iniciada — 2026-04-21
- [x] Etapa 4 completada — 2026-04-21
- [x] Etapa 5 iniciada — 2026-04-21
- [x] Etapa 5 completada — 2026-04-21
- [x] Etapa 6 iniciada — 2026-04-21
- [x] Etapa 6 completada — 2026-04-21
