# Ficha Resumen: P-PSEA-20

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-20` |
| **Nombre decidido** | Competencia y autorizacion operativa del PEA |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna los requisitos de competencia, autorizacion, formacion y experiencia de los roles tecnicos y operativos del PEA. Se acota a las funciones especificas del ensayo de aptitud (planificacion, operacion de aplicativos, analisis estadistico, emision de informes) y no cubre talento humano general de la institucion.

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

Es un procedimiento de gestion de recursos humanos tecnicos; no depende de aplicativo.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-16` | Matriz de competencia/autorizacion | Referencia |
| `P-PSEA-19` | Confidencialidad operativa | Referencia |
| `P-PSEA-21` | Proveedores criticos (competencia de terceros) | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-16` | Matriz de competencia/autorizacion | Referencia |
| `P-PSEA-07` | Analisis estadistico (requiere competencia) | Referencia |
| `P-PSEA-09` | Emision de informe (requiere autorizacion) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-16` | Matriz de competencia/autorizacion | Obligatorio |
| `P-PSEA-19` | Confidencialidad operativa (quien accede) | Obligatorio |
| `P-PSEA-21` | Proveedores criticos (competencia de terceros) | Obligatorio |
| `P-PSEA-07` | Analisis que requiere competencia estadistica | Referencia |
| `P-PSEA-09` | Informe que requiere autorizacion | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No cubre talento humano general de la institucion; solo roles tecnicos y operativos del PEA.
- No es un procedimiento de confidencialidad (eso es `P-PSEA-19`); conecta con el.
- No es un procedimiento de proveedores (eso es `P-PSEA-21`); conecta con el.
- No es un instructivo de formacion.

#### Riesgos de interpretacion

- **Extenderse a talento humano general:** Debe mantenerse acotado a roles del PEA.
- **Omitir matriz F-PSEA-16:** Debe vincularse con la matriz de competencia/autorizacion.
- **Confundir con P-PSEA-19:** `P-PSEA-19` es confidencialidad; `P-PSEA-20` es competencia.
- **Omitir autorizacion para emision:** Debe indicar quien autoriza la emision del informe (`P-PSEA-09`).

---

## Criterio minimo de elaboracion

El procedimiento define requisitos de competencia y autorizacion para roles tecnicos/operativos del PEA, vinculado con `F-PSEA-16`, `P-PSEA-19` y `P-PSEA-21`, sin extenderse a talento humano general ni duplicar confidencialidad.
