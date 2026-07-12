# Diseño Técnico: WorkOS para Participantes y Gestión de Rondas

## Objetivo

Definir una arquitectura objetivo para evolucionar el prototipo de captura de resultados de participantes hacia una plataforma multiusuario con autenticación, perfiles por laboratorio, asignación controlada de rondas y persistencia compartida. El diseño busca soportar la operación de [[Prueba Piloto]] y sentar una base reutilizable para el componente de interacción externa asociado a [[CALAIRE-APP]].

## Decisión de Arquitectura

- `WorkOS` se adopta como capa de identidad y control de acceso, no como repositorio de la lógica operativa del EA.
- La lógica de negocio de participantes, rondas, asignaciones y reportes se implementa en una base de datos propia.
- La interfaz se separa en dos portales reales:
	- portal de administración para el organizador
	- portal de participantes para laboratorios y usuarios asignados
- La persistencia transitoria basada en `localStorage` se reemplaza por almacenamiento centralizado con trazabilidad de cambios y control por estado.

## Stack Recomendado

| Capa | Tecnología | Propósito |
|---|---|---|
| Frontend y backend web | Next.js | Aplicación unificada con rutas para `admin` y `participante` |
| Identidad | WorkOS | Login, invitaciones, organizaciones, sesiones y roles base |
| Base de datos | PostgreSQL | Persistencia principal de negocio |
| Acceso a datos | Prisma | Modelado, migraciones y consultas |
| Despliegue | Vercel | Publicación continua y operación inicial simple |
| Correo transaccional | Resend o Postmark | Invitaciones, alertas y confirmaciones de envío |

## Principios de Diseño

1. La pertenencia organizacional debe corresponder al laboratorio participante.
2. Los permisos deben depender de rol y de asignación explícita de ronda.
3. Cada envío debe quedar asociado a una versión de ronda para preservar trazabilidad.
4. El sistema debe permitir borradores, validación previa y envío final.
5. La configuración de cada ronda debe controlar contaminantes, niveles, ventanas de apertura y reglas de captura.

## Modelo Conceptual

### WorkOS

- `Organization`
	- representa un laboratorio participante o una organización interna administradora
- `User`
	- representa la persona autenticada
- `Role`
	- `platform_admin`
	- `lab_admin`
	- `participant`
	- `reviewer`

### Base de Datos de Negocio

#### `laboratories`

Registro maestro de laboratorios participantes, con código interno, nombre, ciudad, estado de participación y metadatos operativos.

#### `users`

Registro local sincronizado con el identificador de WorkOS. Permite conservar datos extendidos del usuario, trazabilidad interna y vínculo con perfiles operativos.

#### `memberships`

Tabla de pertenencia entre usuarios y laboratorios, con rol operativo, estado y fechas de activación.

#### `participant_profiles`

Perfil operativo del participante. Debe incluir como mínimo:

- usuario asociado
- laboratorio asociado
- cargo o función
- contaminantes habilitados
- estado de habilitación
- observaciones operativas

#### `rounds`

Entidad maestra de ronda. Debe incluir:

- código de ronda
- nombre visible
- descripción técnica
- estado (`draft`, `scheduled`, `open`, `closed`, `archived`)
- fecha de apertura
- fecha de cierre
- unidad sugerida
- número de niveles
- habilitación de segundo promedio
- reglas de validación

#### `round_gases`

Lista de contaminantes habilitados por ronda:

- CO
- SO2
- O3
- NO
- NO2

#### `round_assignments`

Asignación de ronda a laboratorio, usuario o perfil. Debe definir:

- alcance de la asignación
- estado (`assigned`, `accepted`, `in_progress`, `submitted`, `locked`)
- fecha de asignación
- fecha límite efectiva

#### `submissions`

Cabecera del reporte enviado por el participante:

- ronda
- laboratorio
- usuario remitente
- estado (`draft`, `submitted`, `under_review`, `accepted`, `returned`)
- fecha de último guardado
- fecha de envío final
- versión de configuración usada

#### `submission_rows`

Detalle tabular por contaminante y nivel:

- contaminante
- nivel
- promedio 1
- incertidumbre 1
- promedio 2 opcional
- incertidumbre 2 opcional
- observaciones

#### `audit_events`

Bitácora de acciones sensibles:

- creación o edición de ronda
- asignación de participante
- reapertura de ronda
- envío final
- devolución para ajuste

## Relación entre WorkOS y la Base de Negocio

La regla arquitectónica central es la siguiente:

- WorkOS responde `quién es el usuario` y `a qué organización pertenece`.
- La base de datos responde `qué puede ver`, `qué ronda debe diligenciar` y `qué datos ya reportó`.

Esto evita forzar en WorkOS una lógica de negocio que cambiará con frecuencia en la operación del servicio de EA.

## Flujos Principales

### 1. Alta e invitación de laboratorio

1. El administrador crea el laboratorio en la base local.
2. El sistema crea o vincula la organización equivalente en WorkOS.
3. Se invita al `lab_admin`.
4. El `lab_admin` puede aceptar la invitación y gestionar participantes de su organización si esa capacidad se habilita en la fase operativa.

### 2. Configuración de ronda

1. El `platform_admin` crea la ronda.
2. Define contaminantes, niveles, ventanas de captura y reglas opcionales.
3. El sistema guarda la configuración versionada.
4. La ronda permanece en `draft` hasta aprobación operativa.

### 3. Asignación de ronda a perfiles

1. El `platform_admin` selecciona laboratorios o participantes.
2. Crea registros en `round_assignments`.
3. El sistema notifica la apertura o preasignación.
4. El participante sólo visualiza rondas con asignación activa.

### 4. Diligenciamiento por participante

1. El usuario inicia sesión mediante WorkOS.
2. La aplicación carga su organización, rol y asignaciones activas.
3. El portal renderiza la tabla según la configuración vigente de la ronda.
4. El usuario puede guardar borrador antes del envío final.
5. Al enviar, el estado cambia a `submitted` y se bloquea la edición salvo reapertura explícita.

### 5. Revisión organizador

1. El organizador consulta panel de seguimiento por ronda.
2. Visualiza avance por laboratorio y participante.
3. Puede marcar reportes para revisión o devolución.
4. Todas las acciones quedan registradas en `audit_events`.

## Pantallas Requeridas

### Portal `admin`

- panel general de rondas
- creación y edición de rondas
- asignación de laboratorios y participantes
- tablero de seguimiento de estados
- detalle de envíos y exportación consolidada
- auditoría básica de eventos

### Portal `participante`

- tablero de rondas asignadas
- ficha de la ronda con fechas y reglas
- formulario tabular reactivo
- guardado de borrador
- confirmación de envío final
- historial de envíos propios

## Permisos Mínimos

| Rol | Capacidades |
|---|---|
| `platform_admin` | Crear rondas, editar configuración, asignar participantes, revisar envíos, exportar datos |
| `lab_admin` | Ver usuarios de su laboratorio, consultar rondas asignadas al laboratorio, monitorear envíos propios |
| `participant` | Ver y diligenciar exclusivamente sus rondas asignadas |
| `reviewer` | Consultar resultados y estados sin alterar configuración base |

## Estados Operativos

### Ronda

- `draft`
- `scheduled`
- `open`
- `closed`
- `archived`

### Asignación

- `assigned`
- `accepted`
- `in_progress`
- `submitted`
- `locked`

### Envío

- `draft`
- `submitted`
- `under_review`
- `accepted`
- `returned`

## Migración desde el Prototipo Actual

### Activos reutilizables

- estructura conceptual de ronda
- renderizado tabular por contaminante
- configuración de niveles
- manejo opcional de segundo promedio
- exportación tabular como base para consolidación

### Cambios requeridos

- separar interfaz `admin` y `participante`
- reemplazar `localStorage` por PostgreSQL
- incorporar autenticación y sesiones con WorkOS
- añadir control de permisos por rol y organización
- agregar bitácora de eventos y versionado de ronda

## Roadmap Técnico Recomendado

### Fase 1. Fundaciones

- inicializar proyecto web
- configurar WorkOS
- definir esquema de datos
- levantar entorno con autenticación funcional

### Fase 2. Administración de rondas

- construir CRUD de rondas
- habilitar asignaciones por laboratorio y perfil
- exponer tablero de seguimiento

### Fase 3. Portal de participante

- implementar consulta de rondas asignadas
- portar el formulario tabular reactivo
- habilitar borradores y envío final

### Fase 4. Operación y control

- exportaciones consolidadas
- auditoría
- notificaciones
- endurecimiento de validaciones y UX

## Riesgos de Implementación

- confundir la pertenencia organizacional con la asignación operativa de rondas
- modelar permisos sólo por rol y no por asignación explícita
- permitir edición de rondas abiertas sin versionado
- no capturar auditoría de reaperturas y devoluciones
- migrar demasiado pronto a un backend complejo sin validar primero el flujo real de participantes

## Recomendación Final

La arquitectura debe iniciar con una sola aplicación en `Next.js`, `WorkOS` como proveedor de identidad y `PostgreSQL` como núcleo de negocio. Es la combinación de menor fricción para pasar del prototipo actual a una operación controlada, sin comprometer la trazabilidad requerida por el contexto de [[Prueba Piloto]] y la futura consolidación del flujo externo asociado a [[CALAIRE-APP]].
