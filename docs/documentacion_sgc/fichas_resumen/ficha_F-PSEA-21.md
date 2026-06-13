# Ficha Resumen: F-PSEA-21

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-21` |
| **Nombre decidido** | Matriz de competencia/autorizacion |
| **Tipo documental** | Matriz |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha preliminar |

---

## Proposito y rol

### Proposito operativo

Matriz que documenta la competencia, formacion, experiencia y autorizacion de los roles tecnicos y operativos del PEA. Asociada a `P-PSEA-27`, su estructura requiere confirmacion y debe alinearse con los requisitos de competencia definidos en ese procedimiento.

### Rol en el flujo

- [x] Matriz
- [x] Evidencia
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [x] Ninguno

No depende de aplicativo; es un documento de gestion.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-27` | Competencia y autorizacion operativa | Referencia |
| Gestion de talento humano | Datos de formacion y experiencia | Insumo |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-27` | Procedimiento que gobierna la matriz | Referencia |
| `P-PSEA-26` | Confidencialidad (quien accede) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-27` | Procedimiento de competencia | Obligatorio |
| `P-PSEA-26` | Confidencialidad operativa | Referencia |
| `P-PSEA-28` | Proveedores criticos (competencia de terceros) | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es el procedimiento de competencia (eso es `P-PSEA-27`); es la matriz documental.
- No cubre talento humano general; solo roles tecnicos y operativos del PEA.
- Su estructura requiere confirmacion; es preliminar.
- No es un registro de formacion institucional.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-27:** `P-PSEA-27` es el procedimiento; `F-PSEA-21` es la matriz.
- **Extenderse a talento humano general:** Debe mantenerse acotado a roles del PEA.
- **Omitir autorizaciones:** Debe incluir quien autoriza la emision de informes.
- **Cerrar estructura prematuramente:** Es preliminar; requiere confirmacion de estructura.

---

## Criterio minimo de elaboracion

La matriz de competencia/autorizacion documenta roles tecnicos/operativos del PEA, vinculada con `P-PSEA-27`, con estructura preliminar por confirmar, sin extenderse a talento humano general.
