# Ficha Resumen: P-PSEA-28

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-28` |
| **Nombre decidido** | Proveedores criticos del PEA |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna la evaluacion, seleccion, seguimiento y control de proveedores y servicios criticos para el PEA. Se acota a proveedores cuyo desempeno afecta directamente la validez de los ensayos de aptitud (cilindros de gas, calibradores, servicios de software, etc.) y respeta los limites de tercerizacion permitidos por ISO/IEC 17043.

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

Es un procedimiento de gestion de proveedores; no depende de aplicativo.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-23` | Evaluacion de proveedores criticos | Referencia |
| `P-PSEA-27` | Competencia y autorizacion de terceros | Referencia |
| `P-PSEA-10` | Preparacion del item (usa proveedores) | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-23` | Evaluacion documentada | Referencia |
| `P-PSEA-10` | Preparacion del item (usa proveedores aprobados) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-23` | Evaluacion de proveedores criticos | Obligatorio |
| `P-PSEA-27` | Competencia de terceros | Obligatorio |
| `P-PSEA-10` | Preparacion del item que usa proveedores | Obligatorio |
| `P-PSEA-06` | Criterio estadistico (afectado por proveedores) | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No cubre compras generales ni servicios administrativos; solo proveedores criticos del PEA.
- No es un procedimiento de competencia (eso es `P-PSEA-27`); conecta con el.
- No es un procedimiento de preparacion del item (eso es `P-PSEA-10`); conecta con el.
- Debe respetar limites de tercerizacion de ISO/IEC 17043.

#### Riesgos de interpretacion

- **Extenderse a compras generales:** Debe mantenerse acotado a proveedores que afectan la validez del EA.
- **Omitir F-PSEA-23:** Debe vincularse con la evaluacion documentada de proveedores.
- **Omitir limites de tercerizacion:** ISO/IEC 17043 permite tercerizacion limitada; este procedimiento debe respetar esos limites.
- **Confundir con P-PSEA-27:** `P-PSEA-27` es competencia interna; `P-PSEA-28` es gestion de proveedores externos.

---

## Criterio minimo de elaboracion

El procedimiento define evaluacion, seleccion y seguimiento de proveedores criticos del PEA, vinculado con `F-PSEA-23`, `P-PSEA-27` y `P-PSEA-10`, respetando limites de tercerizacion de ISO/IEC 17043 y sin extenderse a compras generales.
