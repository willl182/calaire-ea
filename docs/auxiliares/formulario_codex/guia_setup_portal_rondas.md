# Guía de Setup: Portal de Rondas EA

## Objetivo

Documentar la configuración mínima para activar la base técnica del nuevo portal web de rondas y participantes implementado en `apps/portal-rondas-ea/`. Esta guía corresponde a la **Fase 2** del plan `workos-rondas-participantes` y deja listo el arranque local antes de construir el CRUD operativo del coordinador.

## Estructura creada

- `apps/portal-rondas-ea/app/` - rutas iniciales del portal público, `admin` y `participante`
- `apps/portal-rondas-ea/proxy.ts` - protección de rutas con `AuthKit`
- `apps/portal-rondas-ea/prisma/schema.prisma` - modelo de negocio inicial
- `apps/portal-rondas-ea/.env.example` - variables requeridas para WorkOS y PostgreSQL

## Variables requeridas

Copiar `apps/portal-rondas-ea/.env.example` a `.env` dentro del mismo directorio y completar:

- `WORKOS_API_KEY`
- `WORKOS_CLIENT_ID`
- `WORKOS_COOKIE_PASSWORD`
- `NEXT_PUBLIC_WORKOS_REDIRECT_URI`
- `DATABASE_URL`
- `DIRECT_URL`

## Configuración WorkOS

En el panel de WorkOS deben configurarse como mínimo:

- Redirect URI: `http://localhost:3000/callback`
- Sign-in endpoint: `http://localhost:3000/login`
- Sign-out redirect: `http://localhost:3000/`

La implementación sigue el flujo oficial de `AuthKit` para `Next.js App Router`:

- `AuthKitProvider` en `app/layout.tsx`
- `authkitMiddleware` en `proxy.ts`
- `handleAuth()` en `app/callback/route.ts`
- `getSignInUrl()` en `app/login/route.ts`

## Configuración PostgreSQL / Supabase

1. Crear una base PostgreSQL para el portal.
2. Ajustar `DATABASE_URL` y `DIRECT_URL`.
3. Ejecutar migración inicial con Prisma:

```bash
cd apps/portal-rondas-ea
npm install
npx prisma generate
npx prisma migrate dev --name init
```

## Arranque local

```bash
cd apps/portal-rondas-ea
npm install
npm run dev
```

## Alcance entregado en esta fase

- Se creó la estructura base del portal con dos rutas protegidas:
  - `/admin`
  - `/participante`
- Se dejó una vista semilla para:
  - `/admin/rounds`
  - `/participante/rondas`
- Se modelaron entidades núcleo para laboratorios, usuarios, membresías, perfiles, rondas, asignaciones, envíos y auditoría.

## Siguiente fase recomendada

La siguiente implementación debe concentrarse en el **Portal de administración**:

1. CRUD real de `rounds`
2. Configuración de `round_gases`
3. Alta de laboratorios y sincronización con organizaciones WorkOS
4. Asignaciones desde `round_assignments`

## Referencias

- `docs/auxiliares/formulario_codex/diseno_workos_rondas_participantes.md`
- `logs/plans/260421_1204_plan_workos-rondas-participantes.md`
- WorkOS AuthKit for Next.js: https://workos.com/docs/authkit/nextjs
