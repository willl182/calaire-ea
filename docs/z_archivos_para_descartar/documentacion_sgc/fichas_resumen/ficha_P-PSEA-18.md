# Ficha Resumen: P-PSEA-18

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-18` |
| **Nombre decidido** | Apelaciones del PEA |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna la recepcion, registro, evaluacion, respuesta y seguimiento de apelaciones de participantes en el PEA. Las apelaciones se reciben por correo formal institucional al correo del grupo y no se gestionan como casos en `calaire-app`. Conecta con comunicaciones, TNC/NC/CAPA y control de valores sensibles.

### Rol en el flujo

- [x] Criterio tecnico
- [x] Procedimiento
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [x] Ninguno

Las apelaciones se reciben por correo formal institucional; no se gestionan en `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| Participantes | Apelaciones recibidas por correo | Origen |
| Correo institucional | Canal oficial de recepcion | Origen |
| `P-PSEA-05` | Comunicaciones del PEA | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-15` | TNC/NC/CAPA (si deriva) | Referencia |
| `F-PSEA-15` | Registro de apelaciones | Referencia |
| `P-PSEA-16` | Control de valores sensibles | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-15` | Si la apelacion deriva en NC/CAPA | Obligatorio |
| `P-PSEA-05` | Comunicaciones que registran la apelacion | Obligatorio |
| `F-PSEA-15` | Registro de apelaciones | Obligatorio |
| `P-PSEA-16` | Control de valores sensibles en apelaciones | Obligatorio |
| `P-PSEA-17` | Quejas (diferenciadas de apelaciones) | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No se gestiona en `calaire-app` (eso es `P-PSEA-17`); va por correo formal.
- No es un procedimiento de quejas (eso es `P-PSEA-17`); las apelaciones son diferentes.
- No es un procedimiento de colusion (eso es `P-PSEA-14`); conecta con el si la apelacion lo involucra.
- No es un procedimiento de TNC/NC/CAPA (eso es `P-PSEA-15`); conecta con el.

#### Riesgos de interpretacion

- **Confundir con quejas:** Las apelaciones (`P-PSEA-18`) van por correo formal; las quejas (`P-PSEA-17`) se gestionan en `calaire-app`.
- **Gestionar en calaire-app:** Las apelaciones no deben gestionarse como casos en `calaire-app` por ahora.
- **Omitir conexion con P-PSEA-15:** Debe indicar claramente cuando una apelacion deriva en NC/CAPA.
- **Omitir registro documental:** Las apelaciones deben quedar registradas en `F-PSEA-15`.

---

## Criterio minimo de elaboracion

El procedimiento define recepcion por correo formal institucional, registro en `F-PSEA-15`, evaluacion, respuesta, seguimiento y conexion con `P-PSEA-15`, `P-PSEA-05` y `P-PSEA-16`, diferenciando claramente apelaciones de quejas y sin gestionar en `calaire-app`.
