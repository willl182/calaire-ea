# Plan: Implementación WorkOS para Rondas y Participantes

**Created**: 2026-04-21 12:04 -0500
**Updated**: 2026-04-21 12:45 -0500
**Status**: in_progress
**Slug**: workos-rondas-participantes

---

## Objetivo

Diseñar e implementar la evolución del prototipo de captura de participantes hacia una plataforma multiusuario con autenticación en WorkOS, perfiles por laboratorio, asignación controlada de rondas y persistencia centralizada.

---

## Fases

### Fase 1: Definición arquitectónica y modelo de dominio

**Objetivo:** formalizar la arquitectura objetivo, los roles, las entidades de negocio y los flujos operativos antes de iniciar implementación.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | docs/auxiliares/formulario_codex/diseno_workos_rondas_participantes.md | Crear | Documentar stack, modelo de datos, permisos y flujos principales |
| 1.2 | logs/CURRENT_SESSION.md | Modificar | Actualizar memoria operativa con la decisión arquitectónica |
| 1.3 | pages/CALAIRE-APP.md | Modificar | Enlazar el diseño técnico como siguiente frente del portal externo |
| 1.4 | pages/Prueba Piloto.md | Modificar | Enlazar el diseño como soporte para operación de rondas |

### Fase 2: Base técnica de autenticación y persistencia

**Objetivo:** crear el proyecto base, conectar WorkOS y definir la persistencia principal.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | apps/portal-rondas-ea/app/ | Crear | Inicializar aplicación base en Next.js con estructura `admin` y `participante` |
| 2.2 | apps/portal-rondas-ea/prisma/schema.prisma | Crear | Modelar tablas principales de usuarios, laboratorios, rondas, asignaciones y envíos |
| 2.3 | apps/portal-rondas-ea/.env.example | Crear | Declarar variables requeridas para WorkOS, base de datos y correo |
| 2.4 | docs/auxiliares/formulario_codex/guia_setup_portal_rondas.md | Crear | Registrar instrucciones mínimas de despliegue y configuración |

### Fase 3: Portal de administración

**Objetivo:** habilitar la gestión operativa de rondas y asignaciones.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | rutas `admin/rounds` | Crear | CRUD de rondas con estados, fechas y reglas de captura |
| 3.2 | rutas `admin/assignments` | Crear | Asignación de rondas a laboratorios y perfiles |
| 3.3 | rutas `admin/submissions` | Crear | Seguimiento de avance y consulta de envíos |
| 3.4 | componentes compartidos | Crear | Tablas, filtros y validaciones reutilizables |

### Fase 4: Portal de participante

**Objetivo:** permitir diligenciamiento seguro de rondas asignadas con experiencia tabular.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | rutas `participante/rounds` | Crear | Listado de rondas activas asignadas al usuario |
| 4.2 | rutas `participante/submissions/[id]` | Crear | Formulario tabular reactivo basado en configuración de la ronda |
| 4.3 | capa de persistencia | Modificar | Guardado de borradores y envío final |
| 4.4 | validaciones de negocio | Crear | Reglas de consistencia por contaminante, nivel y ventanas activas |

### Fase 5: Operación, trazabilidad y cierre inicial

**Objetivo:** cerrar el MVP operativo con visibilidad, auditoría y salida consolidada de datos.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 5.1 | módulo de auditoría | Crear | Registrar eventos sensibles y cambios de estado |
| 5.2 | exportación consolidada | Crear | Generar consolidado por ronda para revisión técnica |
| 5.3 | notificaciones | Crear | Enviar invitaciones, alertas de apertura y confirmaciones |
| 5.4 | documentación operativa | Crear | Dejar instructivo breve para organizador y participante |

---

## Criterios de Decisión

- WorkOS se usa exclusivamente para identidad y pertenencia organizacional.
- La asignación de rondas se controla en la base de datos del sistema.
- Ninguna ronda debe publicarse sin versionado básico de configuración.
- El envío final debe quedar bloqueado salvo reapertura explícita por el organizador.

---

## Dependencias y Supuestos

- Se aprueba el uso de `Next.js + WorkOS + PostgreSQL + Prisma`.
- La publicación inicial puede ejecutarse con `Vercel` y una base PostgreSQL administrada.
- El prototipo actual servirá como referencia funcional del formulario tabular.
- La estructura final podrá coexistir con el conocimiento operativo documentado en Logseq.

---

## Log de Ejecución

- [x] Fase 1 iniciada
- [x] Fase 1 completada
- [x] Fase 2 iniciada
- [ ] Fase 2 completada
- [ ] Fase 3 iniciada
- [ ] Fase 3 completada
- [ ] Fase 4 iniciada
- [ ] Fase 4 completada
- [ ] Fase 5 iniciada
- [ ] Fase 5 completada
