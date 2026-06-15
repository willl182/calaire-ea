# Ficha Resumen: F-PSEA-15

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-15` |
| **Nombre decidido** | Registro de apelaciones |
| **Tipo documental** | Registro |
| **Estado** | Revisar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha preliminar |

---

## Proposito y rol

### Proposito operativo

Registro de apelaciones recibidas por correo formal institucional. Documenta la recepcion, contenido, evaluacion, respuesta y cierre de cada apelacion. No se gestiona en `calaire-app`; su estructura requiere confirmacion y alineacion con `P-PSEA-18`.

### Rol en el flujo

- [x] Registro oficial
- [x] Evidencia
- [ ] Entrada
- [ ] Salida
- [ ] Criterio tecnico
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

Se gestiona por correo formal institucional; no depende de aplicativo.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-18` | Apelaciones del PEA | Referencia |
| Correo institucional | Canal de recepcion | Origen |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-15` | Si deriva en NC/CAPA | Referencia |
| `P-PSEA-05` | Comunicaciones de respuesta | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-18` | Procedimiento de apelaciones | Obligatorio |
| `P-PSEA-15` | TNC/NC/CAPA si deriva | Obligatorio |
| `P-PSEA-05` | Comunicaciones | Obligatorio |
| `P-PSEA-16` | Control de valores sensibles | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No se gestiona en `calaire-app` (eso es `F-PSEA-14` para quejas).
- No es el procedimiento de apelaciones (eso es `P-PSEA-18`); es el registro.
- Su estructura requiere confirmacion; es preliminar.
- No es un registro de quejas (eso es `F-PSEA-14`); las apelaciones son diferentes.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-18:** `P-PSEA-18` es el procedimiento; `F-PSEA-15` es el registro.
- **Gestionar en calaire-app:** Las apelaciones no se gestionan en `calaire-app`.
- **Omitir conexion con P-PSEA-15:** Debe indicar cuando una apelacion deriva en NC/CAPA.
- **Cerrar estructura prematuramente:** Es preliminar; requiere confirmacion de estructura.

---

## Criterio minimo de elaboracion

El registro de apelaciones documenta recepcion por correo formal, evaluacion y respuesta, vinculado con `P-PSEA-18`, `P-PSEA-15` y `P-PSEA-05`, con estructura preliminar por confirmar, sin gestion en `calaire-app`.
