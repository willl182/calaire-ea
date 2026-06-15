# Ficha Resumen: F-PSEA-17

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-17` |
| **Nombre decidido** | Evaluacion de proveedores criticos |
| **Tipo documental** | Registro |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha preliminar |

---

## Proposito y rol

### Proposito operativo

Registro de evaluacion de proveedores y servicios criticos para el PEA. Documenta criterios de evaluacion, resultados, seguimiento y decisiones de aprobacion o rechazo de proveedores. Asociado a `P-PSEA-21`, su estructura requiere confirmacion.

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

No depende de aplicativo; es un documento de gestion.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-21` | Proveedores criticos del PEA | Referencia |
| `P-PSEA-20` | Competencia de terceros | Referencia |
| Proveedores | Datos de desempeno y evaluacion | Insumo |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-21` | Procedimiento que gobierna el registro | Referencia |
| `P-PSEA-06` | Preparacion del item (usa proveedores aprobados) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-21` | Procedimiento de proveedores criticos | Obligatorio |
| `P-PSEA-20` | Competencia de terceros | Obligatorio |
| `P-PSEA-06` | Preparacion del item | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es el procedimiento de proveedores (eso es `P-PSEA-21`); es el registro de evaluacion.
- No cubre compras generales; solo proveedores criticos del PEA.
- Su estructura requiere confirmacion; es preliminar.
- No es un contrato ni un acuerdo de confidencialidad.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-21:** `P-PSEA-21` es el procedimiento; `F-PSEA-17` es el registro.
- **Extenderse a compras generales:** Debe mantenerse acotado a proveedores que afectan la validez del EA.
- **Omitir limites de tercerizacion:** Debe respetar los limites de ISO/IEC 17043.
- **Cerrar estructura prematuramente:** Es preliminar; requiere confirmacion de estructura.

---

## Criterio minimo de elaboracion

El registro de evaluacion de proveedores documenta criterios, resultados y decisiones para proveedores criticos del PEA, vinculado con `P-PSEA-21` y `P-PSEA-20`, con estructura preliminar por confirmar, sin extenderse a compras generales.
