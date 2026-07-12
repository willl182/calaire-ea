# Ficha Resumen: P-PSEA-17

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-17` |
| **Nombre decidido** | Quejas del PEA |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna la recepcion, registro, evaluacion, respuesta y seguimiento de quejas de participantes u otras partes interesadas en el PEA. Las quejas se gestionan como casos SGC en `calaire-app` y pueden derivar en trabajo no conforme o acciones correctivas si afectan la conformidad del ensayo.

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

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Las quejas se gestionan como casos SGC en `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| Participantes | Quejas recibidas | Origen |
| `calaire-app` | Interfaz de registro de casos SGC | Origen |
| `P-PSEA-05` | Comunicaciones del PEA | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-15` | TNC/NC/CAPA (si deriva) | Referencia |
| `F-PSEA-14` | Registro/caso de queja | Referencia |
| `P-PSEA-08` | Flujo de datos afectado | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-15` | Si la queja deriva en NC/CAPA | Obligatorio |
| `P-PSEA-05` | Comunicaciones que registran la queja | Obligatorio |
| `F-PSEA-14` | Registro de caso de queja | Obligatorio |
| `P-PSEA-08` | Flujo de datos que puede afectarse | Referencia |
| `DG-PSEA-02` | Aplicativo de gestion de casos | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un procedimiento de apelaciones (eso es `P-PSEA-18`); las quejas son diferentes.
- No es un procedimiento de colusion (eso es `P-PSEA-14`); conecta con el si la queja lo involucra.
- No es un procedimiento de comunicaciones (eso es `P-PSEA-05`); conecta con el.
- No es un procedimiento de TNC/NC/CAPA (eso es `P-PSEA-15`); conecta con el.

#### Riesgos de interpretacion

- **Confundir con apelaciones:** Las quejas (`P-PSEA-17`) se gestionan en `calaire-app`; las apelaciones (`P-PSEA-18`) van por correo formal.
- **Omitir conexion con P-PSEA-15:** Debe indicar claramente cuando una queja deriva en NC/CAPA.
- **Omitir registro en calaire-app:** Las quejas deben quedar como casos SGC en el aplicativo.
- **Tratar como simple reclamo informal:** El procedimiento debe gobernar quejas formales con trazabilidad.

---

## Criterio minimo de elaboracion

El procedimiento define recepcion, registro como caso SGC en `calaire-app`, evaluacion, respuesta, seguimiento y conexion con `P-PSEA-15`, `P-PSEA-05` y `F-PSEA-14`, diferenciando claramente quejas de apelaciones.
