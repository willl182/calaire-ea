# Ficha Resumen: F-PSEA-08

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-08` |
| **Nombre decidido** | Datos reportados por participante |
| **Tipo documental** | Registro |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Registro donde cada participante reporta sus datos de medicion para una ronda de ensayo de aptitud. Es el registro primario de datos crudos de participantes y se captura en `calaire-app`. Alimenta la exportacion oficial (`F-PSEA-09`) y eventualmente el dataset consolidado (`F-PSEA-12`).

### Rol en el flujo

- [x] Registro oficial
- [x] Entrada
- [x] Evidencia
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

Se captura en `calaire-app` por cada participante.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| Participantes | Datos de medicion reportados por laboratorios | Origen |
| `calaire-app` | Interfaz de captura | Origen |
| `F-PSEA-03` | Registro de participacion | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-09` | Datos exportados para analisis PT | Referencia |
| `F-PSEA-12` | Dataset consolidado (usa estos datos) | Referencia |
| `P-PSEA-07` | Analisis estadistico | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-03` | Registro de participacion | Obligatorio |
| `F-PSEA-09` | Datos exportados derivados | Obligatorio |
| `F-PSEA-12` | Dataset consolidado | Obligatorio |
| `I-PSEA-02` | Instructivo para participante | Obligatorio |
| `DG-PSEA-02` | Aplicativo de captura | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el registro de participacion (eso es `F-PSEA-03`); es el registro de datos.
- No es la exportacion oficial (eso es `F-PSEA-09`); es la captura individual.
- No es el dataset consolidado (eso es `F-PSEA-12`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-09:** `F-PSEA-08` es la captura individual; `F-PSEA-09` es la exportacion oficial consolidada.
- **Confundir con F-PSEA-12:** `F-PSEA-12` es el dataset consolidado en `pt_app`; `F-PSEA-08` es la captura en `calaire-app`.
- **Omitir trazabilidad:** Cada dato debe vincularse con el participante y la ronda correspondiente.
- **Incluir analisis estadistico:** Este registro contiene datos crudos, no resultados.

---

## Criterio minimo de elaboracion

El registro de datos reportados contiene las mediciones individuales por participante, capturadas en `calaire-app`, vinculadas con `F-PSEA-03`, y constituyen la fuente primaria para `F-PSEA-09` y `F-PSEA-12`.
