# Asignacion de Subagente G: Control de No Activos y Cierre

**Subagente:** G  
**Paquete de trabajo:** Documentos diferidos, retirados, reservados o absorbidos  
**Documentos asignados:** `DG-PSEA-01`, `P-PSEA-01`, `P-PSEA-11`, `P-PSEA-22`, `P-PSEA-23`, `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19`, `P-PSEA-22`, `F-PSEA-03`, `F-PSEA-11`  
**Fase del plan:** Fase 9

---

## Objetivo

Dejar trazabilidad de documentos que no deben desarrollarse como fichas activas. Ningun documento retirado, reservado o absorbido debe quedar confundido con una ficha activa.

---

## Documentos a registrar

### Fichas diferidas (cierre global)

#### `DG-PSEA-01` — Protocolo general de participacion EA
- **Tipo:** Documento general
- **Clase:** Ficha diferida
- **Prioridad:** Cierre
- **Proposito:** Documento general que establece el marco de participacion. Se revisa al final cuando el sistema de fichas este estabilizado.
- **Razon de diferimiento:** Debe citar flujo de datos e instructivos que aun no estan cerrados.
- **Documento sustituto temporal:** Ninguno; se mantiene vigente.

#### `P-PSEA-01` — Protocolo general EA
- **Tipo:** Procedimiento
- **Clase:** Ficha diferida
- **Prioridad:** Cierre
- **Proposito:** Procedimiento/protocolo marco del ensayo de aptitud.
- **Razon de diferimiento:** Debe citar flujo digital, aplicativos e instructivos cuando el mapa este estabilizado.
- **Documento sustituto temporal:** Ninguno; se mantiene vigente.

### Registros de no activo — Reservados

#### `P-PSEA-11` — No aplicable
- **Tipo:** Procedimiento
- **Clase:** Registro de no activo
- **Prioridad:** No priorizar
- **Decision:** Reservar
- **Razon:** No aplica por ahora porque no hay envio fisico de items de ensayo.
- **Documento sustituto:** Ninguno.

#### `F-PSEA-03` — No aplicable
- **Tipo:** Formato
- **Clase:** Registro de no activo
- **Prioridad:** No priorizar
- **Decision:** Retirar / reservar
- **Razon:** Sustituido por `F-PSEA-05` (plan de ronda).
- **Documento sustituto:** `F-PSEA-05`.

#### `F-PSEA-11` — No aplicable
- **Tipo:** Formato
- **Clase:** Registro de no activo
- **Prioridad:** No priorizar
- **Decision:** Reservar
- **Razon:** No aplica por ausencia de envio fisico de items.
- **Documento sustituto:** Ninguno.

### Registros de no activo — Retirados

#### `P-PSEA-17` — Auditorias internas/externas
- **Tipo:** Procedimiento
- **Clase:** Registro de no activo
- **Prioridad:** No priorizar
- **Decision:** Retirar
- **Razon:** Fuera del alcance documental propio del PEA; pertenece al sistema macro.
- **Documento sustituto:** Sistema de gestion macro.

#### `P-PSEA-18` — Revision por la direccion
- **Tipo:** Procedimiento
- **Clase:** Registro de no activo
- **Prioridad:** No priorizar
- **Decision:** Retirar
- **Razon:** Fuera del alcance documental propio del PEA; pertenece al sistema macro.
- **Documento sustituto:** Sistema de gestion macro.

#### `P-PSEA-19` — Imparcialidad
- **Tipo:** Procedimiento
- **Clase:** Registro de no activo
- **Prioridad:** No priorizar
- **Decision:** Retirar
- **Razon:** Fuera del alcance documental propio del PEA; se maneja por fuera.
- **Documento sustituto:** Ninguno.

### Registros de no activo — Absorbidos

#### `P-PSEA-22` — Reportes PT
- **Tipo:** Procedimiento
- **Clase:** Registro de no activo
- **Prioridad:** No priorizar
- **Decision:** Absorber
- **Razon:** No se mantiene como procedimiento independiente; su contenido queda dentro de `P-PSEA-09`.
- **Documento sustituto:** `P-PSEA-09`.

### Fichas preliminares — Ideas reservadas

#### `P-PSEA-22` — Riesgos generales del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha preliminar
- **Prioridad:** No priorizar
- **Proposito:** Idea reservada para riesgos generales del PEA.
- **Restriccion:** No desarrollar contenido ahora.

#### `P-PSEA-23` — Mejora continua del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha preliminar
- **Prioridad:** No priorizar
- **Proposito:** Idea reservada para mejora continua del PEA.
- **Restriccion:** No desarrollar contenido ahora.

---

## Reglas especificas para este paquete

1. **No activos no son fichas incompletas:** Un registro de no activo es una decision firme, no una ficha a terminar luego.
2. **Diferidos no son cancelados:** `DG-PSEA-01` y `P-PSEA-01` se revisan al cierre; se mantienen vigentes pero no se tocan ahora.
3. **Absorbidos indican sustituto:** `P-PSEA-22` senala explicitamente que su rol queda en `P-PSEA-09`.
4. **Preliminares son ideas:** `P-PSEA-22` y `P-PSEA-23` registran alcance y restriccion, no contenido de fondo.

---

## Entregables

- `ficha_DG-PSEA-01.md` (diferida)
- `ficha_P-PSEA-01.md` (diferida)
- `ficha_P-PSEA-11.md` (no activo)
- `ficha_P-PSEA-22.md` (preliminar)
- `ficha_P-PSEA-23.md` (preliminar)
- `ficha_P-PSEA-17.md` (no activo)
- `ficha_P-PSEA-18.md` (no activo)
- `ficha_P-PSEA-19.md` (no activo)
- `ficha_P-PSEA-22.md` (no activo)
- `ficha_F-PSEA-03.md` (no activo)
- `ficha_F-PSEA-11.md` (no activo)

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md`
- `00_inventario_maestro_fichas.md`
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
