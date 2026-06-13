# Ficha Resumen: F-PSEA-16

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-16` |
| **Nombre decidido** | Registro/caso de queja o NC segun aplique |
| **Tipo documental** | Registro |
| **Estado** | Revisar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha preliminar |

---

## Proposito y rol

### Proposito operativo

Registro o caso de queja o no conformidad gestionado en `calaire-app` como caso SGC. Documenta la recepcion, evaluacion, respuesta y cierre de quejas que pueden derivar en trabajo no conforme. Su estructura requiere confirmacion y alineacion con `P-PSEA-16` y `P-PSEA-24`.

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

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Se gestiona como caso SGC en `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-24` | Quejas del PEA | Referencia |
| `P-PSEA-16` | TNC/NC/CAPA (si deriva) | Referencia |
| `calaire-app` | Interfaz de casos SGC | Origen |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-16` | Seguimiento de NC/CAPA | Referencia |
| `P-PSEA-20` | Comunicaciones de respuesta | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-24` | Procedimiento de quejas | Obligatorio |
| `P-PSEA-16` | Procedimiento de TNC/NC/CAPA | Obligatorio |
| `P-PSEA-20` | Comunicaciones | Obligatorio |
| `DG-PSEA-02` | Aplicativo de gestion de casos | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el procedimiento de quejas (eso es `P-PSEA-24`); es el registro que resulta.
- No es el procedimiento de TNC/NC/CAPA (eso es `P-PSEA-16`); es el caso documentado.
- No es un registro de apelaciones (eso es `F-PSEA-17`); las apelaciones van por correo.
- Su estructura requiere confirmacion; es preliminar.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-24:** `P-PSEA-24` es el procedimiento; `F-PSEA-16` es el registro/caso.
- **Gestionar apelaciones aqui:** Las apelaciones (`P-PSEA-25`) no se gestionan en `calaire-app`; van por correo.
- **Omitir conexion con P-PSEA-16:** El caso debe vincularse con el procedimiento de TNC/NC/CAPA.
- **Cerrar estructura prematuramente:** Es preliminar; requiere confirmacion de estructura.

---

## Criterio minimo de elaboracion

El registro de caso de queja/NC se gestiona en `calaire-app`, con estructura preliminar por confirmar, vinculado con `P-PSEA-24`, `P-PSEA-16` y `P-PSEA-20`, sin gestionar apelaciones ni cerrar estructura antes de validacion.
