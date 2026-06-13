# Ficha Resumen: P-PSEA-26

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-26` |
| **Nombre decidido** | Confidencialidad operativa interna del PEA |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna la confidencialidad de datos, participantes y resultados del PEA a nivel operativo. Se diferencia de la politica institucional general; esta acotada especificamente a la informacion generada y manejada durante las rondas de ensayo de aptitud. Conecta con control de valores sensibles y colusion.

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
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Ambos aplicativos contienen informacion confidencial; este procedimiento gobierna su proteccion.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-21` | Divulgacion y control de valores sensibles | Referencia |
| `P-PSEA-08` | Colusion y falsificacion | Referencia |
| `P-PSEA-27` | Competencia y autorizacion | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-20` | Comunicaciones (control de divulgacion) | Referencia |
| `F-PSEA-04` | Informe (emision controlada) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-21` | Control de valores sensibles | Obligatorio |
| `P-PSEA-08` | Colusion que rompe confidencialidad | Obligatorio |
| `P-PSEA-27` | Competencia y autorizacion (quien accede) | Obligatorio |
| `P-PSEA-20` | Comunicaciones que deben respetar confidencialidad | Obligatorio |
| `F-PSEA-04` | Informe que debe respetar confidencialidad | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es la politica institucional de confidencialidad general; es la confidencialidad operativa del PEA.
- No es un procedimiento de control de valores sensibles (eso es `P-PSEA-21`); conecta con el.
- No es un procedimiento de colusion (eso es `P-PSEA-08`); conecta con el.
- No es un procedimiento de competencia (eso es `P-PSEA-27`); conecta con el.

#### Riesgos de interpretacion

- **Confundir con politica institucional:** Este procedimiento es especifico del PEA; no reemplaza la politica institucional.
- **Omitir conexion con P-PSEA-21:** La confidencialidad operativa debe conectar con el control de valores sensibles.
- **Omitir roles y autorizaciones:** Debe indicar quienes tienen acceso a que informacion (conecta con `P-PSEA-27`).
- **Extenderse a talento humano general:** No cubre talento humano general; solo roles tecnicos y operativos del PEA.

---

## Criterio minimo de elaboracion

El procedimiento define confidencialidad operativa especifica del PEA (datos, participantes, resultados), conectando con `P-PSEA-21`, `P-PSEA-08` y `P-PSEA-27`, sin reemplazar politica institucional ni duplicar control de valores sensibles.
